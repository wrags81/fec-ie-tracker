"""Clean cached FEC data, assign races, build weekly tables, find shifts, and reconcile
against FEC aggregates. Reads only from cache/raw (run pull.py first).

Spenders are the committees named in committees.json, plus two catch-all groups for every
other committee making general-election independent expenditures ("Other R", "Other D"),
plus party coordinated expenditures (Schedule F) for committees flagged "coordinated".

Outputs (in output/):
  ie_transactions.csv           cleaned transaction-level data
  ie_weekly_committee_race.csv  weekly spender-by-race table (plus party-side roll-up)
  cleaning_log.md               rows dropped at each step, reconciliation, currency
  data.json                     everything report.py needs
"""
import glob, json, os, re, warnings
warnings.filterwarnings("ignore")
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "cache", "raw")
ALL = os.path.join(RAW, "_all")
OUT = os.path.join(HERE, "output")
os.makedirs(OUT, exist_ok=True)
COMMITTEES = json.load(open(os.path.join(HERE, "committees.json")))
LABEL = {c["id"]: c["label"] for c in COMMITTEES}
SIDE = {c["id"]: c["side"] for c in COMMITTEES}
COLUMN = {c["label"]: c.get("chart_column", c["label"]) for c in COMMITTEES}
OTHER = {"R": "Other R", "D": "Other D"}
ORDER = [c["label"] for c in COMMITTEES if c["side"] == "R"] + ["Other R"] + \
        [c["label"] for c in COMMITTEES if c["side"] == "D"] + ["Other D"]
SPENDER_SIDE = {**{c["label"]: c["side"] for c in COMMITTEES}, "Other R": "R", "Other D": "D"}

# Senate specials decided on the Nov. 3, 2026 general ballot. Filers code these S2026
# or G2026 inconsistently; S2026 rows dated after the state's primary are treated as general.
SPECIAL_GENERAL = {("S", "OH"): "2026-05-05", ("S", "FL"): "2026-08-18"}
# E-file rows carry no election code. A row seen only in the e-file feed is treated as
# general if dated after the last 2026 state primaries.
EFILE_GENERAL_FROM = "2026-09-16"
CHART_START = "2026-08-31"   # charts begin with the week containing September 1
AT_LARGE = {"AK", "DE", "ND", "SD", "VT", "WY"}

log = []
def say(s=""):
    print(s); log.append(s)

def load(d, tag):
    rows = []
    for f in sorted(glob.glob(os.path.join(d, f"{tag}_[0-9]*.json"))):
        rows += json.load(open(f))["results"]
    return rows

def money(x):
    return f"${x:,.0f}"

def isnull(x):
    return x is None or (isinstance(x, float) and pd.isna(x))

# ---------------------------------------------------------------- load
proc = load(ALL, "proc_H") + load(ALL, "proc_S")
efile = load(ALL, "efile_H") + load(ALL, "efile_S")
filings, fec_bycand, fec_totals = [], [], {}
for c in COMMITTEES:
    d = os.path.join(RAW, c["id"])
    filings += load(d, "filings")
    for f in glob.glob(os.path.join(d, "bycand_*_[0-9]*.json")):
        fec_bycand += json.load(open(f))["results"]
    t = load(d, "totals")
    fec_totals[c["id"]] = t[0] if t else None
m = os.path.join(ALL, "proc_S.DONE")
pulled_at = json.load(open(m))["pulled_at"] if os.path.exists(m) else None

def norm_proc(r):
    return dict(
        source="processed", committee_id=r["committee_id"], committee_name=(r.get("committee") or {}).get("name"),
        file_number=r["file_number"], transaction_id=r.get("transaction_id"),
        is_notice=bool(r.get("is_notice")), filing_form=r.get("filing_form"), report_type=r.get("report_type"),
        most_recent=r.get("most_recent"), memo=(r.get("memo_code") == "X") or bool(r.get("memoed_subtotal")),
        election_type=r.get("election_type"), candidate_id=r.get("candidate_id"),
        candidate_name=r.get("candidate_name"), candidate_party=r.get("candidate_party"),
        office=r.get("candidate_office"), state=r.get("candidate_office_state"),
        district=r.get("candidate_office_district"), support_oppose=r.get("support_oppose_indicator"),
        amount=r.get("expenditure_amount") or 0.0, expenditure_date=(r.get("expenditure_date") or "")[:10] or None,
        dissemination_date=(r.get("dissemination_date") or "")[:10] or None,
        payee=r.get("payee_name"), purpose=r.get("expenditure_description"),
        filing_date=(r.get("filing_date") or "")[:10] or None, pdf_url=r.get("pdf_url"), chain=None)

def norm_efile(r):
    fl = r.get("filing") or {}
    last, first = (r.get("candidate_name") or "").strip(), (r.get("candidate_first_name") or "").strip()
    return dict(
        source="efile", committee_id=r["committee_id"], committee_name=(r.get("committee") or {}).get("name"),
        file_number=r["file_number"], transaction_id=r.get("transaction_id"),
        is_notice=bool(r.get("is_notice")), filing_form=r.get("filing_form"), report_type=r.get("report_type"),
        most_recent=fl.get("most_recent", r.get("most_recent")), memo=(r.get("memo_code") == "X"),
        election_type=None, candidate_id=r.get("candidate_id"),
        candidate_name=(f"{last}, {first}" if first else last).upper() or None, candidate_party=r.get("candidate_party"),
        office=r.get("candidate_office"), state=r.get("candidate_office_state"),
        district=r.get("candidate_office_district"), support_oppose=r.get("support_oppose_indicator"),
        amount=float(r.get("expenditure_amount") or 0), expenditure_date=(r.get("expenditure_date") or "")[:10] or None,
        dissemination_date=(r.get("dissemination_date") or "")[:10] or None,
        payee=(r.get("payee_name") or "").strip().rstrip(",").strip() or None, purpose=r.get("expenditure_description"),
        filing_date=(fl.get("receipt_date") or "")[:10] or None, pdf_url=r.get("pdf_url"),
        chain=fl.get("amendment_chain"))

P = pd.DataFrame([norm_proc(r) for r in proc])
E = pd.DataFrame([norm_efile(r) for r in efile])
proc_files = set(P.file_number)
grp = lambda cid: LABEL.get(cid, "All other committees")

say("# Cleaning log\n")
say(f"Data pulled {pulled_at}.\n")
say("## Rows pulled\n")
say(f"- Processed Schedule E rows, House and Senate candidates, 2026 cycle: {len(P):,} from {P.committee_id.nunique():,} committees")
say(f"- Raw e-file feed rows from filings received in the last 7 days: {len(E):,}")

steps = []
def record(step, df):
    if not len(df):
        return
    for g, x in df.groupby(df.committee_id.map(grp)):
        steps.append(dict(step=step, committee=g, rows=len(x), amount=x.amount.sum()))

# ---------------------------------------------------------------- step 1: add e-file-only filings
new = E[~E.file_number.isin(proc_files)] if len(E) else E
add = new[new.most_recent == True] if len(new) else new
record("1a. E-file rows added (filings not yet in processed data)", add)
record("1b. E-file-only rows ignored (filing already superseded by an amendment)", new[new.most_recent != True] if len(new) else new)
chain = set()
if len(add):
    for fn, ch in add.drop_duplicates("file_number")[["file_number", "chain"]].itertuples(index=False):
        chain |= {x for x in (ch or []) if x != fn}
D = pd.concat([P, add], ignore_index=True)
drop = D.file_number.isin(chain)
record("1c. Processed rows dropped (filing amended by a newer e-file-only filing)", D[drop])
D = D[~drop]

# ---------------------------------------------------------------- step 2: latest amendment only
drop = D.most_recent != True
record("2. Dropped: superseded amendment (not the most recent version of the filing)", D[drop])
D = D[~drop]

# ---------------------------------------------------------------- step 3: memo rows
drop = D.memo
record("3. Dropped: memo / memoed-subtotal rows", D[drop])
D = D[~drop]

D["date"] = D.dissemination_date.fillna(D.expenditure_date)
D["date_source"] = D.dissemination_date.notna().map({True: "dissemination", False: "expenditure"})
nodate = D.date.isna()
record("3b. Dropped: no dissemination or expenditure date", D[nodate])
D = D[~nodate]

# ---------------------------------------------------------------- step 4: notices vs regular reports
# Named committees: coverage end date of the latest regular report, from the filings endpoint.
# All other committees: the latest date among their regular-report rows (no filings lookup).
F = pd.DataFrame(filings)
reg = F[(F.form_type == "F3X") & (F.most_recent == True)]
cov_end = reg.groupby("committee_id").coverage_end_date.max().str[:10].to_dict()
derived = D[~D.is_notice].groupby("committee_id").date.max().to_dict()
D["coverage_end"] = D.committee_id.map(lambda c: cov_end.get(c) if c in LABEL else derived.get(c))
drop = D.is_notice & D.coverage_end.notna() & (D.date <= D.coverage_end)
record("4a. Dropped: 24/48-hour notice dated within a period covered by a regular report", D[drop])
D = D[~drop]
key = ["committee_id", "office", "state", "district", "support_oppose", "amount", "expenditure_date", "dissemination_date"]
regkeys = set(map(tuple, D[~D.is_notice][key].astype(str).values))
drop = D.is_notice & pd.Series(list(map(tuple, D[key].astype(str).values)), index=D.index).isin(regkeys)
record("4b. Dropped: notice duplicating a kept regular-report row (same race, amount and dates)", D[drop])
D = D[~drop]
ALLTYPES = D.copy()  # de-duplicated, every election type: basis for FEC reconciliation

# ---------------------------------------------------------------- step 5: general election only
def is_general(r):
    if r.office not in ("H", "S"):
        return False
    et = r.election_type
    if et == "G2026":
        return True
    if et == "S2026" and (r.office, r.state) in SPECIAL_GENERAL:
        return r.date > SPECIAL_GENERAL[(r.office, r.state)]
    if isnull(et):
        return r.source == "efile" and r.date >= EFILE_GENERAL_FROM
    return False
gen = D.apply(is_general, axis=1)
D["election_basis"] = D.election_type.map(lambda et: "G2026" if et == "G2026" else
                                          ("S2026 special on general ballot" if et == "S2026" else
                                           "inferred general (e-file feed, no election code)"))
nong = D[~gen].copy()
nong["k"] = nong.election_type.fillna("no code").astype(str).str[:1].map(
    {"P": "primary", "R": "runoff", "S": "special", "C": "convention", "G": "general in another year", "O": "other"}).fillna("no or other code")
for s, g in nong.groupby("k"):
    record(f"5. Dropped: not 2026 general ({s})", g)
D = D[gen].copy()
D["spending_type"] = "independent expenditure"

# ---------------------------------------------------------------- coordinated party expenditures
coord_rows, coord_note = [], []
for c in COMMITTEES:
    if not c.get("coordinated"):
        continue
    d = os.path.join(RAW, c["id"])
    current = {r["file_number"] for r in load(d, "reports")}
    fromfile = {}
    for f in glob.glob(os.path.join(d, "sffec_*.json")):
        rows = json.load(open(f))["results"]
        if rows:
            fromfile[rows[0]["file_number"]] = rows
    rows = [r for r in load(d, "sf") if r["file_number"] in current and r["file_number"] not in fromfile]
    for fn, rr in fromfile.items():
        rows += rr
        coord_note.append(f"{c['label']} filing {fn}: {len(rr)} Schedule F rows read from the raw filing because the API had not loaded them")
    for r in rows:
        if r.get("memo_code") == "X" or r.get("candidate_office") not in ("H", "S"):
            continue
        coord_rows.append(dict(
            source="fec file" if r.get("from_fec_file") else "processed", committee_id=c["id"], committee_name=c["name"],
            file_number=r["file_number"], transaction_id=r.get("transaction_id"), is_notice=False,
            filing_form="F3X", report_type=r.get("report_type"), most_recent=True, memo=False, election_type="G2026",
            candidate_id=r.get("candidate_id"), candidate_name=(r.get("candidate_name") or "").upper() or None,
            candidate_party={"R": "REP", "D": "DEM"}[c["side"]], office=r["candidate_office"],
            state=r.get("candidate_office_state"), district=r.get("candidate_office_district"), support_oppose="S",
            amount=float(r.get("expenditure_amount") or 0), expenditure_date=(r.get("expenditure_date") or "")[:10] or None,
            dissemination_date=None, payee=r.get("payee_name"), purpose=r.get("expenditure_purpose_full"),
            filing_date=None, pdf_url=r.get("pdf_url"), chain=None, date=(r.get("expenditure_date") or "")[:10] or None,
            date_source="expenditure", coverage_end=None, election_basis="coordinated party expenditure (general election by law)",
            spending_type="coordinated party expenditure"))
C = pd.DataFrame(coord_rows)
if len(C):
    C = C[C.date.notna()]
    D = pd.concat([D, C], ignore_index=True)

# ---------------------------------------------------------------- race assignment
def cand_key(r):
    nm = r.candidate_name if isinstance(r.candidate_name, str) else ""
    last = re.sub(r"[^A-Z ]", "", nm.upper().split(",")[0]).strip()
    first = re.sub(r"[^A-Z]", "", nm.upper().split(",")[-1])[:3] if "," in nm else ""
    return f"{r.office}|{r.state}|{last}|{first}"
D["cand_key"] = D.apply(cand_key, axis=1)
def race_of(office, state, district):
    if not isinstance(state, str) or not state or office not in ("H", "S"):
        return None
    if office == "S":
        return f"{state}-SEN"
    if isnull(district) or str(district).strip() == "":
        return None
    d = str(district).zfill(2)
    return f"{state}-AL" if d == "00" else f"{state}-{d}"
D["district"] = D.apply(lambda r: "00" if (r.office == "H" and r.state in AT_LARGE) else (None if r.office == "S" else r.district), axis=1)
D["race"] = D.apply(lambda r: race_of(r.office, r.state, r.district), axis=1)
unmapped = D[D.race.isna()]
D = D[D.race.notna()].copy()

# candidate party: fill blanks from other rows naming the same candidate
D["last"] = D.cand_key.str.split("|").str[2]
known = D[D.candidate_party.notna()]
by_id = known[known.candidate_id.notna()].groupby("candidate_id").candidate_party.agg(lambda s: s.value_counts().index[0]).to_dict()
by_name = known.groupby(["race", "last"]).candidate_party.agg(lambda s: s.value_counts().index[0]).to_dict()
D["candidate_party"] = [p if not isnull(p) else by_id.get(i, by_name.get((r, l)))
                        for p, i, r, l in zip(D.candidate_party, D.candidate_id, D.race, D["last"])]

# ---------------------------------------------------------------- which side each expenditure helps
# Named committees keep the side set in committees.json. Every other committee is classed by
# the expenditure itself: supporting a Republican or opposing a Democrat is Republican-side,
# and the reverse. An independent or third-party candidate who draws more money than any
# Democrat in the race is treated as the Democratic-side candidate.
dem = D[D.candidate_party == "DEM"].groupby("race").amount.sum()
minor = D[~D.candidate_party.isin(["DEM", "REP"]) & D.candidate_party.notna()].groupby(["race", "last"]).amount.sum()
as_dem = {k for k, v in minor.items() if v > dem.get(k[0], 0)}
def lean(r):
    if r.committee_id in SIDE:
        return SIDE[r.committee_id]
    p = r.candidate_party
    if p == "REP":
        return "R" if r.support_oppose == "S" else ("D" if r.support_oppose == "O" else None)
    if p == "DEM" or (r.race, r["last"]) in as_dem:
        return "D" if r.support_oppose == "S" else ("R" if r.support_oppose == "O" else None)
    return None
D["side"] = D.apply(lean, axis=1)
unclassified = D[D.side.isna()]
D = D[D.side.notna()].copy()
D["committee"] = [LABEL.get(c, OTHER[s]) for c, s in zip(D.committee_id, D.side)]
D["chart_column"] = D.committee.map(lambda x: COLUMN.get(x, x))
dts = pd.to_datetime(D.date)
D["week_start"] = (dts - pd.to_timedelta(dts.dt.weekday, unit="D")).dt.strftime("%Y-%m-%d")
D["filing_url"] = [f"https://docquery.fec.gov/cgi-bin/forms/{c}/{int(f)}/" for c, f in zip(D.committee_id, D.file_number)]
names = D[D.candidate_name.notna()].groupby("cand_key").candidate_name.agg(lambda s: s.value_counts().index[0]).to_dict()
D["candidate_name"] = D.cand_key.map(names)

say("\n## Rows added and dropped at each step\n")
say("Independent expenditures only. \"All other committees\" is every committee not named in committees.json.\n")
say("| Step | Committee | Rows | Amount |")
say("|---|---|---|---|")
S = pd.DataFrame(steps)
for s, g in S.groupby("step", sort=True):
    for r in g.sort_values("amount", ascending=False).itertuples():
        say(f"| {s} | {r.committee} | {r.rows:,} | {money(r.amount)} |")
    say(f"| {s} | **All** | **{g.rows.sum():,}** | **{money(g.amount.sum())}** |")
ie, co = D[D.spending_type == "independent expenditure"], D[D.spending_type != "independent expenditure"]
say(f"\nFinal cleaned general-election independent expenditure rows: **{len(ie):,}**, {money(ie.amount.sum())}.")
say(f"\nCoordinated party expenditure rows added (Schedule F): **{len(co):,}**, {money(co.amount.sum())}.")
for n in coord_note:
    say(f"- {n}")
say("\nNotice cut-off for the named committees (latest regular-report coverage end date): " +
    "; ".join(f"{c['label']} {cov_end.get(c['id'], 'none filed')}" for c in COMMITTEES if not c.get("coordinated")) +
    ". For all other committees the cut-off is the latest date among that committee's regular-report rows.")
if len(unclassified):
    u = unclassified.groupby(["race", "candidate_name", "candidate_party", "support_oppose"], dropna=False).amount.agg(["size", "sum"]).reset_index().sort_values("sum", ascending=False)
    say("\n## Expenditures by other committees that could not be assigned to a party side\n")
    say(f"{len(unclassified):,} rows, {money(unclassified.amount.sum())}. These are left out of the tables and charts.\n")
    say("| Race | Candidate | Party | Support/oppose | Rows | Amount |")
    say("|---|---|---|---|---|---|")
    for r in u.head(25).itertuples(index=False):
        say(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {money(r[5])} |")
    if len(u) > 25:
        say(f"\nPlus {len(u) - 25} smaller groups totalling {money(u.iloc[25:]['sum'].sum())}.")

cols = ["committee", "committee_name", "committee_id", "side", "chart_column", "spending_type", "race", "candidate_name",
        "candidate_id", "candidate_party", "office", "state", "district", "support_oppose", "amount", "expenditure_date",
        "dissemination_date", "date", "date_source", "week_start", "payee", "purpose", "file_number", "filing_form",
        "report_type", "is_notice", "source", "election_type", "election_basis", "transaction_id", "filing_date",
        "filing_url", "pdf_url"]
T = D[cols].rename(columns={"date": "date_used", "file_number": "filing_id", "committee": "spender"}).sort_values(["date_used", "spender", "race"])
T.to_csv(os.path.join(OUT, "ie_transactions.csv"), index=False)

# ---------------------------------------------------------------- weekly tables
D["wk"] = pd.to_datetime(D.week_start)
last_wk = pd.Timestamp.now().normalize() - pd.Timedelta(days=pd.Timestamp.now().weekday())
future = D[D.wk > last_wk]
if len(future):
    say(f"\n{len(future):,} rows ({money(future.amount.sum())}) are dated after the current week; they are in the transaction file but not the weekly tables or charts.")
D = D[D.wk <= last_wk]
last_wk = D.wk.max()
weeks = pd.date_range(D.wk.min(), last_wk, freq="7D")
def weekly(df, group_label, level):
    piv = df.pivot_table(index="race", columns="wk", values="amount", aggfunc="sum", fill_value=0.0)
    piv = piv.reindex(columns=weeks, fill_value=0.0)
    tot = piv.sum(axis=0)
    out = piv.stack().rename("weekly_spend").reset_index().rename(columns={"level_1": "wk"})
    out["cumulative_spend"] = piv.cumsum(axis=1).stack().values
    out["spender_week_total"] = out.wk.map(tot)
    out["share_of_spender_week"] = (out.weekly_spend / out.spender_week_total).where(out.spender_week_total > 0)
    out["level"] = level; out["spender"] = group_label
    return out, piv
W, PIV = [], {}
for lab in ORDER:
    g = D[D.committee == lab]
    if len(g):
        w, PIV[lab] = weekly(g, lab, "committee"); w["side"] = SPENDER_SIDE[lab]; W.append(w)
for side, lab in (("R", "All R committees"), ("D", "All D committees")):
    g = D[D.side == side]
    if len(g):
        w, PIV[lab] = weekly(g, lab, "side"); w["side"] = side; W.append(w)
W = pd.concat(W, ignore_index=True)
W["office"] = W.race.map(lambda r: "S" if r.endswith("-SEN") else "H")
W["week_start"] = W.wk.dt.strftime("%Y-%m-%d")
first_active = W[W.weekly_spend != 0].groupby(["spender", "race"]).wk.min().rename("first_wk")
W = W.merge(first_active, on=["spender", "race"])
W = W[W.wk >= W.first_wk]
W[["level", "side", "spender", "race", "office", "week_start", "weekly_spend", "cumulative_spend",
   "spender_week_total", "share_of_spender_week"]].to_csv(os.path.join(OUT, "ie_weekly_committee_race.csv"), index=False)

# ---------------------------------------------------------------- shifts
movers, entries, stopped = [], [], []
nw = len(weeks)
for lab, piv in PIV.items():
    for n in (2, 4, 8):
        rec = piv.iloc[:, max(0, nw - n):]
        pri = piv.iloc[:, max(0, nw - 2 * n):max(0, nw - n)]
        rt, pt = rec.values.sum(), pri.values.sum()
        rs, ps = rec.sum(axis=1), pri.sum(axis=1)
        for race in piv.index:
            r, p = float(rs[race]), float(ps[race])
            if r == 0 and p == 0:
                continue
            movers.append(dict(spender=lab, race=race, window=n, recent=r, prior=p,
                               recent_share=(r / rt if rt > 0 else None), prior_share=(p / pt if pt > 0 else None),
                               change_pp=((r / rt - p / pt) * 100 if rt > 0 and pt > 0 else None),
                               spender_recent_total=float(rt), spender_prior_total=float(pt),
                               thin_base=bool(pt < 0.10 * rt)))
    for race in piv.index:
        row = piv.loc[race]
        act = [w for w in weeks if row[w] != 0]
        if not act:
            continue
        entries.append(dict(spender=lab, race=race, first_week=act[0].strftime("%Y-%m-%d"),
                            first_week_spend=float(row[act[0]]), total=float(row.sum())))
        gap = int((last_wk - act[-1]).days // 7)  # 3 = the two full weeks before the current partial week are empty
        if gap >= 3:
            stopped.append(dict(spender=lab, race=race, last_week=act[-1].strftime("%Y-%m-%d"),
                                weeks_silent=gap - 1, total=float(row.sum()), active_weeks=len(act)))
M = pd.DataFrame(movers)

# ---------------------------------------------------------------- validation
say("\n## Reconciliation against FEC aggregates\n")
say("The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular "
    "reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour "
    "notices. The comparison below therefore uses the regular-report rows in this dataset, across all election "
    "types, for the named committees. Spending after the coverage end date, and spending by the other committees, "
    "has no FEC aggregate checked here.\n")
A = ALLTYPES[~ALLTYPES.is_notice & ALLTYPES.committee_id.isin(LABEL)]
B = pd.DataFrame(fec_bycand)
say("| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |")
say("|---|---|---|---|---|---|")
recon = []
def gap(a, b):
    return None if max(a, b) == 0 else (a - b) / max(a, b) * 100
fg = lambda g: "n/a" if g is None else f"{g:+.1f}%" + (" **(over 2%)**" if abs(g) > 2 else "")
for c in COMMITTEES:
    cid = c["id"]
    mine = A[A.committee_id == cid].amount.sum()
    bc = B[B.committee_id == cid].total.sum() if len(B) else 0.0
    t = fec_totals.get(cid) or {}
    ct = t.get("independent_expenditures") or 0.0
    g1, g2 = gap(mine, bc), gap(mine, ct)
    recon.append(dict(committee=c["label"], mine=mine, by_candidate=bc, gap_by_candidate_pct=g1, committee_total=ct,
                      committee_total_through=(t.get("coverage_end_date") or "")[:10], gap_committee_total_pct=g2))
    say(f"| {c['label']} | {money(mine)} | {money(bc)} | {fg(g1)} | {money(ct)} ({(t.get('coverage_end_date') or 'n/a')[:10]}) | {fg(g2)} |")

say("\n### Coordinated party expenditures\n")
say("| Committee | Schedule F rows here (House and Senate) | FEC committee-total coordinated expenditures (through) | Gap |")
say("|---|---|---|---|")
for c in COMMITTEES:
    if c.get("coordinated"):
        t = fec_totals.get(c["id"]) or {}
        ct = t.get("coordinated_expenditures_by_party_committee") or 0.0
        mine = C[C.committee_id == c["id"]].amount.sum() if len(C) else 0.0
        say(f"| {c['label']} | {money(mine)} | {money(ct)} ({(t.get('coverage_end_date') or 'n/a')[:10]}) | {fg(gap(mine, ct))} |")

say("\n### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)\n")
A2 = A.copy()
A2["race"] = [race_of(o, s, "00" if (o == "H" and s in AT_LARGE) else d) for o, s, d in zip(A2.office, A2.state, A2.district)]
mine_r = A2.groupby(["committee_id", "race"]).amount.sum()
race_gaps = []
if len(B):
    cand_race = A2[A2.candidate_id.notna()].drop_duplicates(["committee_id", "candidate_id"]).set_index(["committee_id", "candidate_id"]).race
    B["race"] = [cand_race.get((a, b)) for a, b in zip(B.committee_id, B.candidate_id)]
    fec_r = B.groupby(["committee_id", "race"], dropna=False).total.sum()
    for k in sorted(set(mine_r.index) | set(fec_r.index), key=str):
        a, b = float(mine_r.get(k, 0.0)), float(fec_r.get(k, 0.0))
        if max(a, b) > 0 and abs(a - b) / max(a, b) > 0.02:
            race_gaps.append(dict(committee=LABEL[k[0]], race=k[1], mine=a, fec=b))
if race_gaps:
    say("| Committee | Race | Regular-report rows here | FEC by_candidate |")
    say("|---|---|---|---|")
    for g in race_gaps:
        say(f"| {g['committee']} | {g['race']} | {money(g['mine'])} | {money(g['fec'])} |")
else:
    say("None.")

say("\n## Expenditures not mapped to a race\n")
if len(unmapped):
    say(f"{len(unmapped):,} general-election rows, {money(unmapped.amount.sum())}, had no usable state or House district. Largest:\n")
    say("| Committee | Candidate | Office | State | District | Amount | Date | Filing |")
    say("|---|---|---|---|---|---|---|---|")
    for r in unmapped.sort_values("amount", ascending=False).head(40).itertuples():
        say(f"| {r.committee_name} | {r.candidate_name} | {r.office} | {r.state} | {r.district} | {money(r.amount)} | {r.date} | {r.file_number} |")
else:
    say("None. Every general-election row carried an office, state and (for House) district.")

say("\n## Most recent transaction per spender\n")
say("| Spender | Latest date in cleaned data | Latest filing received | Rows | Total |")
say("|---|---|---|---|---|")
currency = []
for lab in ORDER:
    g = D[D.committee == lab]
    cm = next((c for c in COMMITTEES if c["label"] == lab), None)
    row = dict(committee=lab, side=SPENDER_SIDE[lab], latest=g.date.max() if len(g) else None,
               latest_filing=(g.filing_date.dropna().max() if len(g) and g.filing_date.notna().any() else None),
               rows=len(g), total=float(g.amount.sum()), coverage_end=cov_end.get(cm["id"]) if cm else None,
               kind=("coordinated party expenditures" if cm and cm.get("coordinated") else "independent expenditures"),
               ncommittees=int(g.committee_id.nunique()))
    currency.append(row)
    say(f"| {lab} | {row['latest'] or 'no general-election spending'} | {row['latest_filing'] or 'n/a'} | {len(g):,} | {money(row['total'])} |")

open(os.path.join(OUT, "cleaning_log.md"), "w").write("\n".join(log) + "\n")

# ---------------------------------------------------------------- data for the report
race_tot = D.groupby("race").amount.sum().sort_values(ascending=False)
ck = D.groupby(["race", "cand_key"]).agg(amount=("amount", "sum"), name=("candidate_name", "first"),
                                         party=("candidate_party", lambda x: next((p for p in x if isinstance(p, str)), None))).reset_index()
ck = ck[ck.name.notna()]
ck["last"] = ck.cand_key.str.split("|").str[2]
ck = ck.sort_values("amount", ascending=False).drop_duplicates(["race", "last"])
race_cands = {r: [f"{n.title()} ({p})" if p else n.title() for n, p in zip(g.name, g.party)][:4] for r, g in ck.groupby("race")}
oth = D[D.committee.isin(["Other R", "Other D"])].groupby(["committee", "race", "committee_name"]).amount.sum().reset_index()
other_top = {}
for (sp, race), g in oth.groupby(["committee", "race"]):
    other_top.setdefault(sp, {})[race] = [[n, round(float(a))] for n, a in g.sort_values("amount", ascending=False).head(5)[["committee_name", "amount"]].values]
json.dump(dict(
    weeks=[w.strftime("%Y-%m-%d") for w in weeks], chart_start=CHART_START,
    last_date=D[D.spending_type == "independent expenditure"].date.max(), generated=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
    committees=[dict(label=c["label"], name=c["name"], side=c["side"], id=c["id"], coordinated=bool(c.get("coordinated"))) for c in COMMITTEES],
    spender_side=SPENDER_SIDE,
    heat={lab: dict(races=list(p.sum(axis=1).sort_values(ascending=False).index),
                    values={r: [round(float(v), 2) for v in p.loc[r]] for r in p.index}) for lab, p in PIV.items()},
    race_totals={r: float(v) for r, v in race_tot.items()}, race_cands=race_cands, other_top=other_top,
    movers=json.loads(M.to_json(orient="records")), entries=entries, stopped=stopped,
    currency=currency, recon=recon,
), open(os.path.join(OUT, "data.json"), "w"))
print(f"\nwrote {OUT}")
