"""Shared OpenFEC helpers: key loading (env or .env), throttled GET with retry."""
import os, time, warnings
warnings.filterwarnings("ignore")
import requests

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://api.open.fec.gov/v1"

def _key():
    k = os.environ.get("FEC_API_KEY")
    p = os.path.join(HERE, ".env")
    if not k and os.path.exists(p):
        for line in open(p):
            if line.strip().startswith("FEC_API_KEY="):
                k = line.strip().split("=", 1)[1].strip().strip("'\"")
    if not k:
        raise SystemExit("FEC_API_KEY not found in environment or .env")
    return k

_last = [0.0]
def get(path, params, min_interval=0.6):
    """GET with throttle (~100/min max) and backoff. Never logs the URL or key."""
    p = dict(params, api_key=_key())
    for attempt in range(8):
        wait = min_interval - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        try:
            r = requests.get(BASE + path, params=p, timeout=90)
        except requests.RequestException as e:
            print(f"  network error ({type(e).__name__}), retrying")
            time.sleep(5 * (attempt + 1)); continue
        if r.status_code == 200:
            return r.json()
        if r.status_code == 429:
            print("  rate limited, sleeping 60s"); time.sleep(60); continue
        if r.status_code >= 500:
            time.sleep(5 * (attempt + 1)); continue
        raise SystemExit(f"HTTP {r.status_code} on {path}: {r.text[:300]}")
    raise SystemExit(f"gave up on {path}")
