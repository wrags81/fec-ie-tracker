"""Clean cached Schedule E data, assign races, build weekly tables, find shifts,
and reconcile against FEC aggregates. Reads only from cache/raw (run pull.py first).

Outputs (in output/):
  ie_transactions.csv           cleaned transaction-level data
  ie_weekly_committee_race.csv  weekly committee-by-race table (plus party-side roll-up)
  cleaning_log.md               rows dropped at each step, reconciliation, currency
  data.json                     everything report.py needs
"""
import glob, json, os, re, warnings
warnings.filterwarnings("ignore")
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "cache", "raw")
OUT = os.path.join(HERE, "output")
os.makedirs(OUT, exist_ok=True)
COMMITTEES = json.load(open(os.path.join(HERE, "committees.json")))
LABEL = {c["id"]: c["label"] for c in COMMITTEES}
SIDE = {c["id"]: c["side"] for c in COMMITTEES}
ORDER = [c["label"] for c in COMMITTEES]

# Senate specials decided on the Nov. 3, 2026 general ballot. Filers code these S2026
# or G2026 inconsistently; S2026 rows dated after the state's primary are treated as general.
SPECIAL_GENERAL = {("S", "OH"): "2026-05-05", ("S", "FL"): "2026-08-18"}
# E-file rows carry no election code. A row seen only in the e-file feed is treated as
# general if dated after the last 2026 state primaries.
EFILE_GENERAL_FROM = "2026-09-16"

log = []
def say(s=""):
    print(s); log.append(s)

def load(cid, tag):
    rows = []
    for f in sorted(glob.glob(os.path.join(RAW, cid, f"{tag}_[0-9]*.json"))):
        rows += json.load(open(f))["results"]
    return rows

def money(x):
    return f"${x:,.0f}"

# ---------------------------------------------------------------- load
proc, efile, filings, fec_bycand, fec_totals, pulled = [], [], [], [], {}, {}
for c in COMMITTEES:
    cid = c["id"]
    proc += load(cid, "proc"); efile += load(cid, "efile"); filings += load(cid, "filings")
    for f in glob.glob(os.path.join(RAW, cid, "bycand_*_[0-9]*.json")):
        fec_bycand += json.load(open(f))["results"]
    t = load(cid, "totals")
    fec_totals[cid] = t[0] if t else None
    m = os.path.join(RAW, cid, "efile.DONE")
    pulled[cid] = json.load(open(m))["pulled_at"] if os.path.exists(m) else None

def norm_proc(r):
    return dict(
        source="processed", committee_id=r["committee_id"], file_number=r["file_number"],
        transaction_id=r.get("transaction_id"), sub_id=r.get("sub_id"),
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
        source="efile", committee_id=r["committee_id"], file_number=r["file_number"],
        transaction_id=r.get("transaction_id"), sub_id=None,
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

say("# Cleaning log\n")
say("## Rows pulled\n")
say("| Committee | Processed rows (cycle 2026) | E-file feed rows | Pulled at |")
say("|---|---|---|---|")
for c in COMMITTEES:
    say(f"| {c['label']} | {(P.committee_id == c['id']).sum() if len(P) else 0} | {(E.committee_id == c['id']).sum() if len(E) else 0} | {pulled[c['id']]} |")

steps = []  # (step, committee, rows, dollars)
def record(step, df):
    for cid, g in df.groupby("committee_id"):
        steps.append(dict(step=step, committee=LABEL[cid], rows=len(g), amount=g.amount.sum()))

# ---------------------------------------------------------------- step 1: add e-file-only filings
new = E[~E.file_number.isin(proc_files)]
add = new[new.most_recent == True]
record("1a. E-file rows added (filings not yet in processed data)", add)
superseded_efile = new[new.most_recent != True]
record("1b. E-file-only rows ignored (filing already superseded by an amendment)", superseded_efile)
chain = set()
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

# ---------------------------------------------------------------- step 4: notices vs regular reports
F = pd.DataFrame(filings)
reg = F[(F.form_type == "F3X") & (F.most_recent == True)]
cov_end = reg.groupby("committee_id").coverage_end_date.max().str[:10].to_dict()
D["coverage_end"] = D.committee_id.map(cov_end)
drop = D.is_notice & D.coverage_end.notna() & (D.date <= D.coverage_end)
record("4a. Dropped: 24/48-hour notice dated within a period covered by a regular report", D[drop])
D = D[~drop]
key = ["committee_id", "office", "state", "district", "support_oppose", "amount", "expenditure_date", "dissemination_date"]
regkeys = set(map(tuple, D[~D.is_notice][key].astype(str).values))
drop = D.is_notice & D[key].astype(str).apply(tuple, axis=1).isin(regkeys)
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
    if et is None or (isinstance(et, float) and pd.isna(et)):
        return r.source == "efile" and (r.date or "") >= EFILE_GENERAL_FROM
    return False
gen = D.apply(is_general, axis=1)
D["election_basis"] = D.apply(lambda r: "G2026" if r.election_type == "G2026" else
                              ("S2026 special on general ballot" if r.election_type == "S2026" else
                               "inferred general (e-file feed, no election code)"), axis=1)
nong = D[~gen].copy()
nong["step"] = "5. Dropped: not 2026 general (" + nong.election_type.fillna("no code").astype(str) + ")"
for s, g in nong.groupby("step"):
    record(s, g)
D = D[gen].copy()

# ---------------------------------------------------------------- race assignment
def cand_key(r):
    last = re.sub(r"[^A-Z ]", "", (r.candidate_name or "").upper().split(",")[0]).strip()
    first = re.sub(r"[^A-Z]", "", (r.candidate_name or "").upper().split(",")[-1])[:3] if "," in (r.candidate_name or "") else ""
    return f"{r.office}|{r.state}|{last}|{first}"
D["cand_key"] = D.apply(cand_key, axis=1)
def race_of(office, state, district):
    if not state or not isinstance(state, str) or office not in ("H", "S"):
        return None
    if office == "S":
        return f"{state}-SEN"
    if district is None or (isinstance(district, float) and pd.isna(district)) or str(district).strip() == "":
        return None
    d = str(district).zfill(2)
    return f"{state}-AL" if d == "00" else f"{state}-{d}"
# District comes from the filing. At-large states are normalised to 00; any candidate a
# filer reported under two districts is listed in the log rather than silently moved.
AT_LARGE = {"AK", "DE", "ND", "SD", "VT", "WY"}
D["district"] = D.apply(lambda r: "00" if (r.office == "H" and r.state in AT_LARGE) else r.district, axis=1)
conflicts = []
for k, g in D[D.office == "H"].groupby("cand_key"):
    by = g.groupby(g.district.fillna("").astype(str)).amount.sum()
    if len(by) > 1:
        conflicts.append((k, {d: round(float(v)) for d, v in by.items()}))
D["race"] = D.apply(lambda r: race_of(r.office, r.state, r.district), axis=1)
unmapped = D[D.race.isna()]
D = D[D.race.notna()].copy()
D["committee"] = D.committee_id.map(LABEL)
D["side"] = D.committee_id.map(SIDE)
D["week_start"] = (pd.to_datetime(D.date) - pd.to_timedelta(pd.to_datetime(D.date).dt.weekday, unit="D")).dt.strftime("%Y-%m-%d")
D["filing_url"] = D.apply(lambda r: f"https://docquery.fec.gov/cgi-bin/forms/{r.committee_id}/{int(r.file_number)}/", axis=1)
# display name: most common spelling per candidate
names = D.groupby("cand_key").candidate_name.agg(lambda s: s.value_counts().index[0]).to_dict()
D["candidate_name"] = D.cand_key.map(names)

say("\n## Rows added and dropped at each step\n")
say("| Step | Committee | Rows | Amount |")
say("|---|---|---|---|")
S = pd.DataFrame(steps)
for s, g in S.groupby("step", sort=True):
    for r in g.itertuples():
        say(f"| {s} | {r.committee} | {r.rows} | {money(r.amount)} |")
    say(f"| {s} | **All** | **{g.rows.sum()}** | **{money(g.amount.sum())}** |")
say(f"\nFinal cleaned general-election rows: **{len(D)}**, {money(D.amount.sum())}.")
say("\nLatest regular-report coverage end date used for the notice cut-off: " +
    "; ".join(f"{LABEL[c]} {cov_end.get(c, 'none filed')}" for c in LABEL) + ".")
if conflicts:
    say("\nCandidates reported under more than one district (left as filed): " +
        "; ".join(f"{k} {v}" for k, v in conflicts) + ".")

cols = ["committee", "committee_id", "side", "race", "candidate_name", "candidate_id", "candidate_party", "office", "state",
        "district", "support_oppose", "amount", "expenditure_date", "dissemination_date", "date", "date_source",
        "week_start", "payee", "purpose", "file_number", "filing_form", "report_type", "is_notice", "source",
        "election_type", "election_basis", "transaction_id", "filing_date", "filing_url", "pdf_url"]
T = D[cols].rename(columns={"date": "date_used", "file_number": "filing_id"}).sort_values(["date_used", "committee", "race"])
T.to_csv(os.path.join(OUT, "ie_transactions.csv"), index=False)

# ---------------------------------------------------------------- weekly tables
D["wk"] = pd.to_datetime(D.week_start)
last_wk = D.wk.max()
weeks = pd.date_range(D.wk.min(), last_wk, freq="7D")
def weekly(df, group_label, level):
    """df: transactions for one spender group. Returns tidy weekly rows for every race x week."""
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
        w, PIV[lab] = weekly(g, lab, "committee"); w["side"] = g.side.iloc[0]; W.append(w)
for side, lab in (("R", "All R committees"), ("D", "All D committees")):
    g = D[D.side == side]
    if len(g):
        w, PIV[lab] = weekly(g, lab, "side"); w["side"] = side; W.append(w)
W = pd.concat(W, ignore_index=True)
W["office"] = W.race.map(lambda r: "S" if r.endswith("-SEN") else "H")
W["week_start"] = W.wk.dt.strftime("%Y-%m-%d")
first_active = W[W.weekly_spend != 0].groupby(["spender", "race"]).wk.min().rename("first_wk")
W = W.merge(first_active, on=["spender", "race"])
W = W[W.wk >= W.first_wk]  # no rows before a spender entered a race
W[["level", "side", "spender", "race", "office", "week_start", "weekly_spend", "cumulative_spend",
   "spender_week_total", "share_of_spender_week"]].to_csv(os.path.join(OUT, "ie_weekly_committee_race.csv"), index=False)

# ---------------------------------------------------------------- shifts
movers, entries, stopped = [], [], []
for lab, piv in PIV.items():
    nw = len(weeks)
    for n in (2, 4, 8):
        rec = piv.iloc[:, max(0, nw - n):]
        pri = piv.iloc[:, max(0, nw - 2 * n):max(0, nw - n)]
        rt, pt = rec.values.sum(), pri.values.sum()
        for race in piv.index:
            r, p = rec.loc[race].sum(), (pri.loc[race].sum() if pri.shape[1] else 0.0)
            if r == 0 and p == 0:
                continue
            movers.append(dict(spender=lab, race=race, window=n, recent=r, prior=p,
                               recent_share=(r / rt if rt > 0 else None), prior_share=(p / pt if pt > 0 else None),
                               change_pp=((r / rt - p / pt) * 100 if rt > 0 and pt > 0 else None),
                               spender_recent_total=float(rt), spender_prior_total=float(pt),
                               thin_base=bool(pt < 0.10 * rt)))
    for race in piv.index:
        act = [w for w in weeks if piv.loc[race, w] != 0]
        entries.append(dict(spender=lab, race=race, first_week=act[0].strftime("%Y-%m-%d"),
                            first_week_spend=float(piv.loc[race, act[0]]), total=float(piv.loc[race].sum())))
        gap = int((last_wk - act[-1]).days // 7)  # 3 = the two full weeks before the current partial week are empty
        if gap >= 3:
            stopped.append(dict(spender=lab, race=race, last_week=act[-1].strftime("%Y-%m-%d"),
                                weeks_silent=gap - 1, total=float(piv.loc[race].sum()), active_weeks=len(act)))
M = pd.DataFrame(movers)

# ---------------------------------------------------------------- validation
say("\n## Reconciliation against FEC aggregates\n")
say("The FEC's `/schedules/schedule_e/by_candidate/` aggregates and committee totals are built from regular "
    "reports only, so they stop at each committee's latest regular-report coverage end date and exclude 24/48-hour "
    "notices. The comparison below therefore uses the regular-report rows in this dataset, across all election "
    "types. Spending after the coverage end date has no FEC aggregate to check against.\n")
A = ALLTYPES[~ALLTYPES.is_notice]
B = pd.DataFrame(fec_bycand)
say("| Committee | Regular-report rows here | FEC by_candidate total | Gap | FEC committee-total IEs (through) | Gap |")
say("|---|---|---|---|---|---|")
recon = []
for c in COMMITTEES:
    cid = c["id"]
    mine = A[A.committee_id == cid].amount.sum()
    bc = B[B.committee_id == cid].total.sum() if len(B) else 0.0
    t = fec_totals.get(cid) or {}
    ct = t.get("independent_expenditures") or 0.0
    def gap(a, b):
        return None if max(a, b) == 0 else (a - b) / max(a, b) * 100
    g1, g2 = gap(mine, bc), gap(mine, ct)
    recon.append(dict(committee=c["label"], mine=mine, by_candidate=bc, gap_by_candidate_pct=g1, committee_total=ct,
                      committee_total_through=(t.get("coverage_end_date") or "")[:10], gap_committee_total_pct=g2))
    f = lambda g: "n/a" if g is None else f"{g:+.1f}%" + (" **(over 2%)**" if abs(g) > 2 else "")
    say(f"| {c['label']} | {money(mine)} | {money(bc)} | {f(g1)} | {money(ct)} ({(t.get('coverage_end_date') or 'n/a')[:10]}) | {f(g2)} |")

say("\n### Per-race gaps over 2% (regular-report rows vs FEC by_candidate)\n")
A2 = A.copy()
A2["race"] = A2.apply(lambda r: race_of(r.office, r.state, r.district), axis=1)
mine_r = A2.groupby(["committee_id", "race"]).amount.sum()
race_gaps = []
if len(B):
    cand_race = A2[A2.candidate_id.notna()].drop_duplicates(["committee_id", "candidate_id"]).set_index(["committee_id", "candidate_id"]).race
    B["race"] = [cand_race.get((a, b)) for a, b in zip(B.committee_id, B.candidate_id)]
    fec_r = B.groupby(["committee_id", "race"], dropna=False).total.sum()
    keys = set(mine_r.index) | set(fec_r.index)
    for k in sorted(keys, key=str):
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
noid = A[A.candidate_id.isna()].groupby("committee_id").amount.agg(["size", "sum"])
for cid, r in noid.iterrows():
    say(f"\n{LABEL[cid]}: {int(r['size'])} regular-report rows ({money(r['sum'])}) carry no candidate ID in the FEC data, "
        "so the by_candidate aggregate cannot include them.")

say("\n## Expenditures not mapped to a race\n")
if len(unmapped):
    say("| Committee | Candidate | Office | State | District | Amount | Date | Filing |")
    say("|---|---|---|---|---|---|---|---|")
    for r in unmapped.itertuples():
        say(f"| {LABEL[r.committee_id]} | {r.candidate_name} | {r.office} | {r.state} | {r.district} | {money(r.amount)} | {r.date} | {r.file_number} |")
else:
    say("None. Every general-election row carried an office, state and (for House) district.")

say("\n## Most recent transaction per committee\n")
say("| Committee | Latest date in cleaned general-election data | Latest filing received | Rows | Total |")
say("|---|---|---|---|---|")
currency = []
for c in COMMITTEES:
    g = D[D.committee == c["label"]]
    row = dict(committee=c["label"], side=c["side"], latest=g.date.max() if len(g) else None,
               latest_filing=g.filing_date.max() if len(g) else None, rows=len(g), total=float(g.amount.sum()),
               coverage_end=cov_end.get(c["id"]))
    currency.append(row)
    say(f"| {c['label']} | {row['latest'] or 'no general-election IEs'} | {row['latest_filing'] or 'n/a'} | {len(g)} | {money(row['total'])} |")

open(os.path.join(OUT, "cleaning_log.md"), "w").write("\n".join(log) + "\n")

# ---------------------------------------------------------------- data for the report
race_tot = D.groupby("race").amount.sum().sort_values(ascending=False)
ck = D.groupby(["race", "cand_key"]).agg(amount=("amount", "sum"), name=("candidate_name", "first"),
                                         party=("candidate_party", lambda x: next((p for p in x if isinstance(p, str)), None))).reset_index()
ck["last"] = ck.cand_key.str.split("|").str[2]
ck = ck.sort_values("amount", ascending=False).drop_duplicates(["race", "last"])
race_cands = {r: [f"{n.title()} ({p})" if p else n.title() for n, p in zip(g.name, g.party)] for r, g in ck.groupby("race")}
so = D.groupby(["committee", "race", "support_oppose", "candidate_name"]).amount.sum().reset_index()
json.dump(dict(
    weeks=[w.strftime("%Y-%m-%d") for w in weeks],
    last_date=D.date.max(), generated=pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
    committees=[dict(label=c["label"], name=c["name"], side=c["side"], id=c["id"]) for c in COMMITTEES],
    heat={lab: dict(races=list(p.sum(axis=1).sort_values(ascending=False).index),
                    values={r: [round(float(v), 2) for v in p.loc[r]] for r in p.index}) for lab, p in PIV.items()},
    race_totals={r: float(v) for r, v in race_tot.items()}, race_cands=race_cands,
    movers=json.loads(M.to_json(orient="records")), entries=entries, stopped=stopped,
    currency=currency, recon=recon, steps=json.loads(S.to_json(orient="records")),
    targets=json.loads(so.to_json(orient="records")),
), open(os.path.join(OUT, "data.json"), "w"))
print(f"\nwrote {OUT}")
