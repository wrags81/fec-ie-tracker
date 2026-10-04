"""Pull 2026-cycle spending data from OpenFEC and cache every response as JSON.

What is pulled:
  cache/raw/_all/        every House and Senate Schedule E row in the cycle (processed data),
                         plus the raw e-file feed for filings received in the last few days
  cache/raw/<committee>/ filings, committee totals and FEC by-candidate aggregates for the
                         committees named in committees.json
  cache/raw/<party>/     Schedule F (coordinated party expenditures) for party committees

A finished pull writes a DONE marker, so reruns never re-hit the API.
Use `python3 pull.py --refresh` to discard the cache and pull fresh data."""
import glob, json, os, shutil, sys, datetime
import requests
from fecapi import get, HERE

RAW = os.path.join(HERE, "cache", "raw")
ALL = os.path.join(RAW, "_all")
CYCLE = 2026
EFILE_DAYS = 7   # e-file feed window: filings older than this are in the processed data
COMMITTEES = json.load(open(os.path.join(HERE, "committees.json")))

def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(obj, open(path, "w"))

def done(d, tag):
    return os.path.exists(os.path.join(d, f"{tag}.DONE"))

def mark(d, tag, info):
    save(os.path.join(d, f"{tag}.DONE"), dict(info, pulled_at=datetime.datetime.now().isoformat(timespec="seconds")))

def clear(d, tag):
    for f in glob.glob(os.path.join(d, f"{tag}_[0-9]*.json")):
        os.remove(f)

def pull_keyset(d, tag, path, params, quiet=False):
    """Keyset pagination: feed pagination.last_indexes back in until results run out."""
    if done(d, tag):
        return
    clear(d, tag)
    params = dict(params, per_page=100)
    n, rows, count = 0, 0, None
    while True:
        page = get(path, params)
        if count is None:
            count = page["pagination"].get("count")
        if not page["results"]:
            break
        n += 1; rows += len(page["results"])
        save(os.path.join(d, f"{tag}_{n:04d}.json"), page)
        li = page["pagination"].get("last_indexes")
        if not li:
            break
        params.update(li)
        if n % 50 == 0:
            print(f"    {tag}: {rows} of {count} rows")
    mark(d, tag, {"pages": n, "rows": rows, "api_count": count})
    if not quiet:
        print(f"  {tag}: {rows} rows in {n} pages (API count {count})")

def pull_paged(d, tag, path, params, quiet=False):
    """Page-numbered pagination."""
    if done(d, tag):
        return
    clear(d, tag)
    n, rows = 0, 0
    while True:
        page = get(path, dict(params, per_page=100, page=n + 1))
        n += 1; rows += len(page["results"])
        save(os.path.join(d, f"{tag}_{n:04d}.json"), page)
        if n >= (page["pagination"].get("pages") or 1):
            break
    mark(d, tag, {"pages": n, "rows": rows})
    if not quiet:
        print(f"  {tag}: {rows} rows")

def load(d, tag):
    rows = []
    for f in sorted(glob.glob(os.path.join(d, f"{tag}_[0-9]*.json"))):
        rows += json.load(open(f))["results"]
    return rows

# .fec field positions for Schedule F lines (FEC electronic filing format v8.x)
SF = dict(transaction_id=2, payee_org=16, payee_last=17, expenditure_date=27, expenditure_amount=28,
          purpose=30, candidate_id=33, cand_last=34, cand_first=35, office=39, state=40, district=41, memo_code=42)

def parse_fec_schedule_f(cid, file_number, url):
    """Fallback for a filing whose Schedule F rows are not yet in the API: read them from the
    raw .fec filing on the FEC's server."""
    out = os.path.join(RAW, cid, f"sffec_{file_number}.json")
    if os.path.exists(out):
        return
    rows = []
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        for raw in r.iter_lines():
            if not raw.startswith(b"SF"):
                continue
            f = raw.decode("latin-1").split("\x1c")
            g = lambda k: (f[SF[k]].strip() if len(f) > SF[k] else "")
            dt = g("expenditure_date")
            rows.append(dict(
                committee_id=cid, file_number=file_number, transaction_id=g("transaction_id"),
                payee_name=g("payee_org") or g("payee_last"),
                expenditure_date=f"{dt[:4]}-{dt[4:6]}-{dt[6:8]}" if len(dt) == 8 else None,
                expenditure_amount=float(g("expenditure_amount") or 0), expenditure_purpose_full=g("purpose"),
                candidate_id=g("candidate_id") or None,
                candidate_name=", ".join(x for x in (g("cand_last"), g("cand_first")) if x).upper(),
                candidate_office=g("office"), candidate_office_state=g("state"),
                candidate_office_district=g("district"), memo_code=g("memo_code") or None,
                pdf_url=f"https://docquery.fec.gov/cgi-bin/forms/{cid}/{file_number}/", from_fec_file=True))
    save(out, {"results": rows})
    print(f"  Schedule F read from the raw filing {file_number}: {len(rows)} rows, ${sum(x['expenditure_amount'] for x in rows):,.0f}")

if __name__ == "__main__":
    if "--refresh" in sys.argv and os.path.isdir(RAW):
        shutil.rmtree(RAW)

    print("All House and Senate independent expenditures")
    since = (datetime.date.today() - datetime.timedelta(days=EFILE_DAYS)).isoformat()
    for off in ("H", "S"):
        pull_keyset(ALL, f"proc_{off}", "/schedules/schedule_e/",
                    {"candidate_office": off, "cycle": CYCLE, "sort": "-expenditure_date"})
        # The e-file feed is page-numbered and its sort keys have many ties, so pages overlap
        # and skip rows. Pull it under several sort orders until every row has been seen once.
        seen, want = set(), None
        for i, sort in enumerate(("-expenditure_amount", "expenditure_amount", "-dissemination_date", "-expenditure_date")):
            tag = f"efile{i}_{off}"
            pull_paged(ALL, tag, "/schedules/schedule_e/efile/",
                       {"candidate_office": off, "min_filed_date": since, "sort": sort}, quiet=True)
            pages = sorted(glob.glob(os.path.join(ALL, f"{tag}_[0-9]*.json")))
            want = json.load(open(pages[0]))["pagination"]["count"] if pages else 0
            seen |= {(r["file_number"], r["transaction_id"]) for r in load(ALL, tag)}
            if len(seen) >= want:
                break
        print(f"  efile_{off}: {len(seen)} distinct rows of {want} reported by the API")

    by_committee = {}
    for off in ("H", "S"):
        for r in load(ALL, f"proc_{off}") + [x for i in range(4) for x in load(ALL, f"efile{i}_{off}")]:
            if r.get("candidate_office_state"):
                by_committee.setdefault(r["committee_id"], set()).add(
                    (off, r["candidate_office_state"], (r.get("candidate_office_district") or "00") if off == "H" else "00"))

    for c in COMMITTEES:
        cid = c["id"]; d = os.path.join(RAW, cid)
        print(f"{c['label']} ({cid})")
        pull_paged(d, "filings", f"/committee/{cid}/filings/", {"cycle": CYCLE, "form_type": ["F3X", "F24", "F5"]})
        pull_paged(d, "totals", f"/committee/{cid}/totals/", {"cycle": CYCLE})
        # FEC's own per-candidate aggregates, for reconciliation (endpoint needs office + state [+ district])
        for off, st, dist in sorted(by_committee.get(cid, ())):
            pull_paged(d, f"bycand_{off}_{st}_{dist}", "/schedules/schedule_e/by_candidate/",
                       {"committee_id": cid, "cycle": CYCLE, "election_full": "false",
                        "office": "house" if off == "H" else "senate", "state": st,
                        **({"district": dist} if off == "H" else {})}, quiet=True)
        if c.get("coordinated"):
            pull_keyset(d, "sf", "/schedules/schedule_f/", {"committee_id": cid, "cycle": CYCLE})
            pull_paged(d, "reports", f"/committee/{cid}/reports/", {"cycle": CYCLE, "is_amended": "false"})
            api = {}
            for r in load(d, "sf"):
                api[r["file_number"]] = api.get(r["file_number"], 0) + (r["expenditure_amount"] or 0)
            for rep in load(d, "reports"):
                want = rep.get("coordinated_expenditures_by_party_committee_period") or 0
                have = api.get(rep["file_number"], 0)
                if want > 0 and abs(want - have) > 0.01 * want and rep.get("fec_url"):
                    parse_fec_schedule_f(cid, rep["file_number"], rep["fec_url"])
    print("pull complete")
