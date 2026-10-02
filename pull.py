"""Pull 2026-cycle Schedule E (processed + raw e-file feed), filings and FEC totals
for each committee. Every API response is cached as JSON under cache/raw/<committee>/;
a completed pull writes a DONE marker so reruns never re-hit the API.
Use `python3 pull.py --refresh` to discard the cache and pull fresh data."""
import glob, json, os, shutil, sys, datetime
from fecapi import get, HERE

RAW = os.path.join(HERE, "cache", "raw")
CYCLE = 2026
CYCLE_START = "2025-01-01"
COMMITTEES = json.load(open(os.path.join(HERE, "committees.json")))

def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(obj, open(path, "w"))

def done(d, tag):
    return os.path.exists(os.path.join(d, f"{tag}.DONE"))

def mark(d, tag, info):
    save(os.path.join(d, f"{tag}.DONE"), dict(info, pulled_at=datetime.datetime.now().isoformat(timespec="seconds")))

def pull_processed(cid, d):
    """Keyset pagination on /schedules/schedule_e/ (last_index + last_expenditure_date)."""
    for tag, extra in [("proc", {})]:
        if done(d, tag):
            continue
        for f in glob.glob(os.path.join(d, f"{tag}_*.json")):
            os.remove(f)
        params = {"committee_id": cid, "cycle": CYCLE, "per_page": 100, "sort": "-expenditure_date", **extra}
        n, rows, count = 0, 0, None
        while True:
            page = get("/schedules/schedule_e/", params)
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
        mark(d, tag, {"pages": n, "rows": rows, "api_count": count})
        print(f"  {tag}: {rows} rows in {n} pages (API count {count})")

def pull_efile(cid, d):
    """Raw e-file feed is page-numbered; newest first, stop once past the cycle start."""
    if done(d, "efile"):
        return
    for f in glob.glob(os.path.join(d, "efile_*.json")):
        os.remove(f)
    n, rows = 0, 0
    while True:
        page = get("/schedules/schedule_e/efile/", {"committee_id": cid, "per_page": 100,
                   "sort": "-expenditure_date", "page": n + 1})
        res = page["results"]
        if not res:
            break
        n += 1; rows += len(res)
        save(os.path.join(d, f"efile_{n:04d}.json"), page)
        dates = [r["expenditure_date"] for r in res if r.get("expenditure_date")]
        if n >= page["pagination"]["pages"] or (dates and max(dates) < CYCLE_START):
            break
    mark(d, "efile", {"pages": n, "rows": rows})
    print(f"  efile: {rows} rows in {n} pages")

def pull_simple(cid, d, tag, path, params):
    if done(d, tag):
        return
    n, rows = 0, 0
    while True:
        page = get(path, dict(params, per_page=100, page=n + 1))
        n += 1; rows += len(page["results"])
        save(os.path.join(d, f"{tag}_{n:04d}.json"), page)
        if n >= (page["pagination"].get("pages") or 1):
            break
    mark(d, tag, {"pages": n, "rows": rows})
    if not tag.startswith("bycand"):
        print(f"  {tag}: {rows} rows")

if __name__ == "__main__":
    if "--refresh" in sys.argv and os.path.isdir(RAW):
        shutil.rmtree(RAW)
    for c in COMMITTEES:
        cid = c["id"]; d = os.path.join(RAW, cid)
        print(f"{c['label']} ({cid})")
        pull_simple(cid, d, "filings", f"/committee/{cid}/filings/", {"cycle": CYCLE, "form_type": ["F3X", "F24", "F5"]})
        pull_simple(cid, d, "totals", f"/committee/{cid}/totals/", {"cycle": CYCLE})
        pull_processed(cid, d)
        pull_efile(cid, d)
    # FEC's own per-candidate aggregates, for reconciliation. The endpoint requires
    # office + state, so query each office/state the committee's rows touch.
    for c in COMMITTEES:
        cid = c["id"]; d = os.path.join(RAW, cid)
        seen = set()
        for f in glob.glob(os.path.join(d, "proc_*.json")) + glob.glob(os.path.join(d, "efile_*.json")):
            for r in json.load(open(f))["results"]:
                if r.get("candidate_office") in ("H", "S") and r.get("candidate_office_state"):
                    seen.add((r["candidate_office"], r["candidate_office_state"],
                              (r.get("candidate_office_district") or "00") if r["candidate_office"] == "H" else "00"))
        for off, st, dist in sorted(seen):
            pull_simple(cid, d, f"bycand_{off}_{st}_{dist}", "/schedules/schedule_e/by_candidate/",
                        {"committee_id": cid, "cycle": CYCLE, "election_full": "false",
                         "office": "house" if off == "H" else "senate", "state": st,
                         **({"district": dist} if off == "H" else {})})
    print("pull complete")
