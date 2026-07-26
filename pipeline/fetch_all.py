"""
Live-fetch orchestrator.

HARD RULE (spec): pull fresh data on EVERY full run and OVERWRITE data/*.json.
Never skip because prior files exist. Never treat cache as current without re-fetch.

Usage:
  python -m pipeline.fetch_all
  set CENSUS_API_KEY=... && python -m pipeline.fetch_all

Partial coverage is OK: mark failed series in meta.json and write unavailable fields.
Expand fetchers over time; do not invent numbers.
"""
from __future__ import annotations

import csv
import gzip
import io
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline import config


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(config.ROOT)}")


def _http_get(url: str, timeout: int = 45) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return False, str(exc)


def _http_post_json(url: str, payload: dict[str, Any], timeout: int = 90) -> tuple[bool, Any]:
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "User-Agent": config.USER_AGENT,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, json.loads(resp.read().decode("utf-8", errors="replace"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        return False, str(exc)


_STATE_ABBREV = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
    "District of Columbia": "DC", "Florida": "FL", "Georgia": "GA", "Hawaii": "HI",
    "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
    "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
    "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
    "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
    "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY",
}

_STATE_NAMES = set(_STATE_ABBREV)


def fetch_fred_median_income_api() -> dict[str, Any]:
    """CPS ASEC median HH income via FRED series API (MEHOINUS{ST}A646N)."""
    result: dict[str, Any] = {
        "metric": "median_household_income",
        "source": "CPS ASEC via FRED API",
        "source_url": config.FRED_MEDIAN_INCOME_URL,
        "as_of": None,
        "pulled_at": _now_iso(),
        "fetch_ok": False,
        "states": {},
        "notes": [],
    }
    if not config.FRED_API_KEY:
        result["notes"].append("FRED_API_KEY not set — skipped FRED API.")
        return result

    years: list[str] = []
    for name, abbr in _STATE_ABBREV.items():
        series_id = f"MEHOINUS{abbr}{config.FRED_MEDIAN_SERIES_SUFFIX}"
        url = (
            f"{config.FRED_API_BASE}/series/observations"
            f"?series_id={series_id}"
            f"&api_key={config.FRED_API_KEY}"
            f"&file_type=json&sort_order=desc&limit=1"
        )
        ok, body = _http_get(url, timeout=30)
        if not ok:
            result["notes"].append(f"{series_id}: {body}")
            continue
        try:
            payload = json.loads(body)
            obs = (payload.get("observations") or [None])[0]
            if not obs or obs.get("value") in (None, "."):
                continue
            result["states"][name] = int(float(obs["value"]))
            if obs.get("date"):
                years.append(obs["date"][:4])
        except (json.JSONDecodeError, TypeError, ValueError, KeyError) as exc:
            result["notes"].append(f"{series_id}: parse error {exc}")

    if years:
        # Use most common observation year
        result["as_of"] = max(set(years), key=years.count)
    result["fetch_ok"] = len(result["states"]) >= 40
    result["notes"].append(
        f"FRED API pulled {len(result['states'])} state/DC medians "
        f"(series *{config.FRED_MEDIAN_SERIES_SUFFIX})."
    )
    return result


def fetch_fred_median_income_html() -> dict[str, Any]:
    """Parse FRED CPS ASEC median HH income release table HTML when available."""
    ok, body = _http_get(config.FRED_MEDIAN_INCOME_URL)
    result: dict[str, Any] = {
        "metric": "median_household_income",
        "source": "CPS ASEC via FRED HTML",
        "source_url": config.FRED_MEDIAN_INCOME_URL,
        "as_of": "2024",
        "pulled_at": _now_iso(),
        "fetch_ok": ok,
        "states": {},
        "notes": [],
    }
    if not ok:
        result["notes"].append(f"FRED HTML fetch failed: {body}")
        return result

    matches = re.findall(
        r"\|\s*([A-Za-z .]+?)\s*\|\s*([\d,]+)\s*\|",
        body,
    )
    skip = {"name", "the united states", "current dollars"}
    for name, num in matches:
        name = name.strip()
        if name.lower() in skip or not name:
            continue
        if name in _STATE_NAMES:
            try:
                result["states"][name] = int(num.replace(",", ""))
            except ValueError:
                continue

    if not result["states"]:
        result["fetch_ok"] = False
        result["notes"].append(
            "FRED HTML parsed but no state rows found — site layout may have changed "
            "or content was blocked."
        )
    else:
        result["fetch_ok"] = True
        result["notes"].append(f"Parsed {len(result['states'])} state/DC medians from FRED HTML.")
    return result


def fetch_fred_median_income() -> dict[str, Any]:
    """Prefer FRED API; fall back to release-table HTML scrape."""
    api = fetch_fred_median_income_api()
    if api.get("fetch_ok") and len(api.get("states") or {}) >= 40:
        return api
    html = fetch_fred_median_income_html()
    if html.get("fetch_ok") and len(html.get("states") or {}) >= 40:
        html["notes"] = (api.get("notes") or []) + (html.get("notes") or [])
        return html
    # Prefer whichever returned more states
    if len(api.get("states") or {}) >= len(html.get("states") or {}):
        api["notes"] = (api.get("notes") or []) + (html.get("notes") or [])
        return api
    html["notes"] = (api.get("notes") or []) + (html.get("notes") or [])
    return html


def fetch_census_acs_income_and_race(year: int = 2023) -> dict[str, Any]:
    """
    Live Census API pull for median HH income + race counts when CENSUS_API_KEY is set.
    Mean HH income requires subject tables; mark unavailable if not fetched.
    """
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "year": year,
        "fetch_ok": False,
        "median": {},
        "mean": {},
        "race": {},
        "notes": [],
    }
    if not config.CENSUS_API_KEY:
        out["notes"].append(
            "CENSUS_API_KEY not set — skipped Census API. "
            "Set env var or .env for live ACS median/mean/race pulls."
        )
        return out

    # B19013 median HH income; B02001 race alone; B03003 Hispanic
    vars_ = (
        "NAME,B19013_001E,B02001_001E,B02001_002E,B02001_003E,B02001_005E,B03003_003E"
    )
    url = (
        f"{config.CENSUS_API_ACS1.format(year=year)}"
        f"?get={vars_}&for=state:*&key={config.CENSUS_API_KEY}"
    )
    ok, body = _http_get(url)
    if not ok:
        out["notes"].append(f"Census API failed: {body}")
        return out
    try:
        rows = json.loads(body)
    except json.JSONDecodeError:
        out["notes"].append("Census API returned non-JSON (often missing/invalid key).")
        return out

    header, *data = rows
    idx = {h: i for i, h in enumerate(header)}
    for row in data:
        name = row[idx["NAME"]]
        try:
            total = float(row[idx["B02001_001E"]])
            white = float(row[idx["B02001_002E"]])
            black = float(row[idx["B02001_003E"]])
            asian = float(row[idx["B02001_005E"]])
            hisp = float(row[idx["B03003_003E"]])
            med = int(float(row[idx["B19013_001E"]]))
        except (KeyError, TypeError, ValueError):
            continue
        out["median"][name] = med
        out["race"][name] = {
            "white_alone_pct": round(100 * white / total, 1) if total else None,
            "black_alone_pct": round(100 * black / total, 1) if total else None,
            "asian_alone_pct": round(100 * asian / total, 1) if total else None,
            "hispanic_any_race_pct": round(100 * hisp / total, 1) if total else None,
            "note": "Race alone categories; Hispanic is ethnicity (any race). Not NH-adjusted.",
        }
    out["fetch_ok"] = bool(out["median"])

    # Mean HH income from ACS subject table S1901
    mean_url = (
        f"{config.CENSUS_API_ACS1_SUBJECT.format(year=year)}"
        f"?get=NAME,S1901_C01_013E&for=state:*&key={config.CENSUS_API_KEY}"
    )
    mok, mbody = _http_get(mean_url)
    if mok:
        try:
            mrows = json.loads(mbody)
            mheader, *mdata = mrows
            mi = {h: i for i, h in enumerate(mheader)}
            for row in mdata:
                name = row[mi["NAME"]]
                try:
                    out["mean"][name] = int(float(row[mi["S1901_C01_013E"]]))
                except (KeyError, TypeError, ValueError):
                    continue
            out["notes"].append(
                f"ACS subject S1901 mean HH income for {len(out['mean'])} areas (year {year})."
            )
        except (json.JSONDecodeError, ValueError, KeyError) as exc:
            out["notes"].append(f"Census mean (S1901) parse failed: {exc}")
    else:
        out["notes"].append(f"Census mean (S1901) fetch failed: {mbody}")
    return out


def fetch_bea_personal_income(year: str = "2024") -> dict[str, Any]:
    """BEA Regional SAINC1: personal income + per capita personal income by state."""
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "BEA Regional SAINC1 API",
        "source_url": config.BEA_API,
        "year": year,
        "fetch_ok": False,
        "per_capita_personal_income": {},
        "personal_income_thousands": {},
        "notes": [],
    }
    if not config.BEA_API_KEY:
        out["notes"].append("BEA_API_KEY not set - skipped BEA.")
        return out

    fips_to_state = {v: k for k, v in config.STATE_FIPS.items()}

    def _pull(line_code: str) -> dict[str, float]:
        q = urllib.parse.urlencode(
            {
                "UserID": config.BEA_API_KEY,
                "method": "GetData",
                "datasetname": "Regional",
                "TableName": "SAINC1",
                "GeoFIPS": "STATE",
                "LineCode": line_code,
                "Year": year,
                "ResultFormat": "JSON",
            }
        )
        ok, body = _http_get(f"{config.BEA_API}?{q}", timeout=60)
        if not ok:
            out["notes"].append(f"BEA line {line_code} failed: {body}")
            return {}
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            out["notes"].append(f"BEA line {line_code} non-JSON")
            return {}
        data = ((payload.get("BEAAPI") or {}).get("Results") or {}).get("Data") or []
        got: dict[str, float] = {}
        for row in data:
            geo = str(row.get("GeoFips") or "")
            if len(geo) < 2 or geo == "00000":
                continue
            # GeoFips like 01000 for Alabama
            fips = geo[:2]
            name = fips_to_state.get(fips)
            if not name:
                # try GeoName
                gname = (row.get("GeoName") or "").split(",")[0].strip()
                if gname in _STATE_NAMES:
                    name = gname
                else:
                    continue
            try:
                raw = str(row.get("DataValue") or "").replace(",", "")
                got[name] = float(raw)
            except (TypeError, ValueError):
                continue
        return got

    pc = _pull("3")  # per capita personal income (dollars)
    tot = _pull("1")  # personal income (thousands of dollars)
    out["per_capita_personal_income"] = {k: int(v) for k, v in pc.items()}
    out["personal_income_thousands"] = {k: int(v) for k, v in tot.items()}
    out["fetch_ok"] = len(pc) >= 40
    out["notes"].append(
        f"BEA SAINC1 {year}: per-capita for {len(pc)} states; total PI for {len(tot)} states."
    )
    return out


def fetch_fhfa_hpi_yoy() -> dict[str, Any]:
    """FHFA purchase-only state HPI (no key) -> latest index + YoY % change."""
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "FHFA HPI purchase-only state (quarterly TXT)",
        "source_url": config.FHFA_HPI_PO_STATE,
        "fetch_ok": False,
        "states": {},
        "notes": [],
    }
    ok, body = _http_get(config.FHFA_HPI_PO_STATE, timeout=60)
    if not ok:
        out["notes"].append(f"FHFA download failed: {body}")
        return out

    abbr_to_name = {v: k for k, v in _STATE_ABBREV.items()}
    # state yr qtr index_nsa index_sa ...
    by_state: dict[str, list[tuple[int, int, float]]] = {}
    for line in body.splitlines()[1:]:
        parts = line.strip().split("\t")
        if len(parts) < 5:
            parts = line.split()
        if len(parts) < 5:
            continue
        abbr, yr_s, q_s, _nsa, sa = parts[0], parts[1], parts[2], parts[3], parts[4]
        name = abbr_to_name.get(abbr)
        if not name:
            continue
        try:
            by_state.setdefault(name, []).append((int(yr_s), int(q_s), float(sa)))
        except ValueError:
            continue

    for name, series in by_state.items():
        series.sort()
        yr, qtr, idx = series[-1]
        # same quarter prior year
        prior = next((v for y, q, v in reversed(series) if y == yr - 1 and q == qtr), None)
        yoy = round(100.0 * (idx / prior - 1.0), 1) if prior else None
        out["states"][name] = {
            "index_sa": idx,
            "year": yr,
            "quarter": qtr,
            "as_of": f"{yr}Q{qtr}",
            "yoy_pct": yoy,
        }
    out["fetch_ok"] = len(out["states"]) >= 40
    out["notes"].append(f"FHFA PO HPI YoY for {len(out['states'])} states/DC.")
    return out


def fetch_redfin_state_prices() -> dict[str, Any]:
    """Redfin public state market tracker (no key) - latest All Residential median sale price."""
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "Redfin public state_market_tracker (All Residential)",
        "source_url": config.REDFIN_STATE_TRACKER,
        "fetch_ok": False,
        "as_of": None,
        "states": {},
        "notes": [],
    }
    ok, body = _http_get(config.REDFIN_STATE_TRACKER, timeout=120)
    if not ok:
        # _http_get expects text; for binary gz we need raw bytes
        out["notes"].append(f"Redfin fetch via text helper failed: {body}")
    # Always fetch as bytes for gzip
    req = urllib.request.Request(
        config.REDFIN_STATE_TRACKER, headers={"User-Agent": config.USER_AGENT}
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
        text = gzip.GzipFile(fileobj=io.BytesIO(raw)).read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        out["notes"].append(f"Redfin gzip download failed: {exc}")
        return out

    rdr = csv.DictReader(io.StringIO(text), delimiter="\t")
    by_end: dict[str, dict[str, dict[str, Any]]] = {}
    for row in rdr:
        pt = (row.get("PROPERTY_TYPE") or "").strip('"')
        if pt != "All Residential":
            continue
        pe = (row.get("PERIOD_END") or "").strip('"')
        st = (row.get("STATE") or row.get("REGION") or "").strip('"')
        if not pe or st not in _STATE_NAMES:
            continue
        try:
            med = int(float(row.get("MEDIAN_SALE_PRICE") or ""))
        except (TypeError, ValueError):
            continue
        typ = None
        try:
            # AVG_SALE_TO_LIST or inventory proxies; use MEDIAN_PPSF * typical only if needed
            typ_raw = row.get("AVG_SALE_TO_LIST")  # not typical price
            _ = typ_raw
        except Exception:
            pass
        # Redfin tracker has no average sale price column consistently; mark typical as median
        # when average unavailable
        entry: dict[str, Any] = {"median_sale_price": med, "typical_home_value": None}
        # Some exports include AVERAGE_SALE_PRICE
        for key in ("AVERAGE_SALE_PRICE", "AVG_SALE_PRICE", "MEDIAN_LIST_PRICE"):
            if row.get(key):
                try:
                    entry["typical_home_value"] = int(float(row[key]))
                    entry["typical_field"] = key
                    break
                except (TypeError, ValueError):
                    continue
        by_end.setdefault(pe, {})[st] = entry

    if not by_end:
        out["notes"].append("Redfin parsed but no All Residential state rows.")
        return out
    latest = max(by_end)
    out["as_of"] = latest
    out["states"] = by_end[latest]
    out["fetch_ok"] = len(out["states"]) >= 40
    out["notes"].append(
        f"Redfin All Residential medians for {len(out['states'])} states as of {latest}."
    )
    return out


def _bls_latest_obs(series_list: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Map seriesID -> latest observation dict with value/year/period."""
    out: dict[str, dict[str, Any]] = {}
    for s in series_list:
        sid = s.get("seriesID")
        data = s.get("data") or []
        if not sid or not data:
            continue
        # BLS returns newest-first typically; take first numeric value
        for row in data:
            try:
                val = float(row["value"])
            except (KeyError, TypeError, ValueError):
                continue
            out[sid] = {
                "value": val,
                "year": row.get("year"),
                "period": row.get("period"),
                "periodName": row.get("periodName"),
            }
            break
    return out


def _bls_post_series(series_ids: list[str], startyear: str, endyear: str) -> tuple[bool, Any]:
    if not config.BLS_API_KEY:
        return False, "BLS_API_KEY not set"
    # API max 50 series per request
    merged: list[dict[str, Any]] = []
    messages: list[str] = []
    for i in range(0, len(series_ids), 50):
        chunk = series_ids[i : i + 50]
        ok, resp = _http_post_json(
            config.BLS_API_TIMESERIES,
            {
                "seriesid": chunk,
                "startyear": startyear,
                "endyear": endyear,
                "registrationkey": config.BLS_API_KEY,
            },
        )
        if not ok:
            return False, resp
        if not isinstance(resp, dict):
            return False, "unexpected BLS response"
        messages.extend(resp.get("message") or [])
        if resp.get("status") != "REQUEST_SUCCEEDED":
            return False, resp.get("status") or messages
        merged.extend((resp.get("Results") or {}).get("series") or [])
    return True, {"series": merged, "messages": messages}


def fetch_bls_laus_jobs(startyear: str = "2025", endyear: str = "2026") -> dict[str, Any]:
    """Statewide seasonally adjusted unemployment rate (LASST…003)."""
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "BLS LAUS API (LASST unemployment rate)",
        "source_url": config.BLS_LAUS,
        "fetch_ok": False,
        "states": {},
        "notes": [],
    }
    if not config.BLS_API_KEY:
        out["notes"].append("BLS_API_KEY not set - skipped LAUS.")
        return out

    sid_to_state = {
        f"LASST{fips}0000000000003": name for name, fips in config.STATE_FIPS.items()
    }
    ok, payload = _bls_post_series(list(sid_to_state), startyear, endyear)
    if not ok:
        out["notes"].append(f"BLS LAUS failed: {payload}")
        return out

    latest = _bls_latest_obs(payload.get("series") or [])
    for sid, state in sid_to_state.items():
        obs = latest.get(sid)
        if not obs:
            continue
        out["states"][state] = {
            "unemployment_rate": obs["value"],
            "as_of": f"{obs.get('periodName', obs.get('period'))} {obs.get('year')}",
            "series_id": sid,
        }
    out["fetch_ok"] = len(out["states"]) >= 40
    out["notes"].append(f"LAUS unemployment rates for {len(out['states'])} states/DC.")
    if payload.get("messages"):
        out["notes"].extend([str(m) for m in payload["messages"][:5]])
    return out


def fetch_bls_ces_industries(startyear: str = "2025", endyear: str = "2026") -> dict[str, Any]:
    """CES SAE statewide employment by supersector; top sectors by share of total nonfarm."""
    out: dict[str, Any] = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "BLS CES SAE API (SMU statewide supersectors)",
        "source_url": config.BLS_INDUSTRY_CHART,
        "fetch_ok": False,
        "states": {},
        "notes": [],
    }
    if not config.BLS_API_KEY:
        out["notes"].append("BLS_API_KEY not set - skipped CES industries.")
        return out

    # Build all series IDs: SMU{ss}00000{industry}01
    series_meta: dict[str, tuple[str, str, str]] = {}  # sid -> (state, code, label)
    for state, fips in config.STATE_FIPS.items():
        for code, label in config.BLS_CES_INDUSTRIES:
            sid = f"SMU{fips}00000{code}01"
            series_meta[sid] = (state, code, label)

    ok, payload = _bls_post_series(list(series_meta), startyear, endyear)
    if not ok:
        out["notes"].append(f"BLS CES failed: {payload}")
        return out

    latest = _bls_latest_obs(payload.get("series") or [])
    by_state: dict[str, dict[str, float]] = {}
    as_of_by_state: dict[str, str] = {}
    for sid, (state, code, label) in series_meta.items():
        obs = latest.get(sid)
        if not obs:
            continue
        by_state.setdefault(state, {})[label] = obs["value"]
        as_of_by_state[state] = f"{obs.get('periodName', obs.get('period'))} {obs.get('year')}"

    for state, sectors in by_state.items():
        total = sectors.get("Total nonfarm")
        if not total or total <= 0:
            continue
        ranked = []
        for label, val in sectors.items():
            if label == "Total nonfarm":
                continue
            share = round(100.0 * val / total, 1)
            ranked.append({"label": label, "employees_thousands": val, "share_pct": share})
        ranked.sort(key=lambda x: -x["share_pct"])
        top = ranked[:4]
        out["states"][state] = {
            "as_of": as_of_by_state.get(state),
            "total_nonfarm_thousands": total,
            "top": top,
            "top_labels": [t["label"] for t in top],
            "display": "; ".join(t["label"].lower() for t in top),
        }

    out["fetch_ok"] = len(out["states"]) >= 40
    out["notes"].append(
        f"CES supersector shares for {len(out['states'])} states/DC "
        f"({len(latest)} series observations)."
    )
    if payload.get("messages"):
        # Filter noise; keep a few existence warnings if any
        out["notes"].extend([str(m) for m in payload["messages"] if "does not exist" in str(m)][:3])
    return out


def main() -> int:
    print("LIVE FETCH - overwriting data/ (spec: every full run must re-pull)")
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)

    sources_status: dict[str, Any] = {}

    income_fred = fetch_fred_median_income()
    sources_status["fred_median_income"] = {
        "ok": income_fred.get("fetch_ok"),
        "pulled_at": income_fred.get("pulled_at"),
        "n_states": len(income_fred.get("states") or {}),
    }

    census = fetch_census_acs_income_and_race()
    sources_status["census_acs1"] = {
        "ok": census.get("fetch_ok"),
        "pulled_at": census.get("pulled_at"),
        "n_states": len(census.get("median") or {}),
        "notes": census.get("notes"),
    }

    # Prefer FRED CPS medians; fall back to Census ACS 1-year when FRED scrape fails
    fred_medians = {
        k: v
        for k, v in (income_fred.get("states") or {}).items()
        if k in _STATE_NAMES or k == "District of Columbia"
    }
    census_medians = {
        k: v for k, v in (census.get("median") or {}).items() if k in _STATE_NAMES
    }
    used_census_fallback = False
    if len(fred_medians) >= 40:
        medians = fred_medians
        as_of = income_fred.get("as_of") or "latest"
        median_source = (
            f"CPS ASEC via FRED API (MEHOINUS*A646N), as_of {as_of}; "
            f"{config.FRED_MEDIAN_INCOME_URL}"
        )
        median_as_of = f"CPS {as_of}" if as_of and as_of.isdigit() else str(as_of)
    elif len(census_medians) >= 40:
        medians = census_medians
        median_source = (
            f"Census ACS {census.get('year', 2023)} 1-year API (B19013); "
            "FRED CPS scrape unavailable this run"
        )
        median_as_of = f"ACS {census.get('year', 2023)}"
        used_census_fallback = True
    else:
        medians = fred_medians or census_medians
        median_source = income_fred.get("source_url")
        median_as_of = income_fred.get("as_of")

    income_payload = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "median_household_income": medians,
        "median_source": median_source,
        "median_as_of": median_as_of,
        "mean_household_income": {},
        "mean_status": "unavailable",
        "census_acs_median_alt": census.get("median") or {},
        "notes": (income_fred.get("notes") or []) + (census.get("notes") or []),
    }
    if used_census_fallback:
        income_payload["notes"].append(
            "Primary medians filled from Census ACS because FRED returned <40 states."
        )
    if census.get("mean"):
        filled = {k: v for k, v in census["mean"].items() if v is not None}
        if filled:
            income_payload["mean_household_income"] = filled
            income_payload["mean_status"] = "acs_s1901"
            income_payload["mean_as_of"] = f"ACS {census.get('year', 2023)}"
            income_payload["mean_source"] = "Census ACS 1-year subject S1901_C01_013E"
    _write_json(config.DATA_FILES["income"], income_payload)

    demo_payload = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "Census ACS 1-year API" if census.get("fetch_ok") else "unavailable_this_run",
        "states": census.get("race") or {},
        "notes": census.get("notes")
        or [
            "Race shares not live-fetched this run (set CENSUS_API_KEY)."
        ],
    }
    _write_json(config.DATA_FILES["demographics"], demo_payload)

    bea = fetch_bea_personal_income()
    sources_status["bea_sainc1"] = {
        "ok": bea.get("fetch_ok"),
        "pulled_at": bea.get("pulled_at"),
        "n_states": len(bea.get("per_capita_personal_income") or {}),
        "notes": bea.get("notes"),
    }
    _write_json(config.DATA_FILES["bea"], bea)

    jobs = fetch_bls_laus_jobs()
    sources_status["bls_laus"] = {
        "ok": jobs.get("fetch_ok"),
        "pulled_at": jobs.get("pulled_at"),
        "n_states": len(jobs.get("states") or {}),
        "notes": jobs.get("notes"),
    }
    _write_json(config.DATA_FILES["jobs"], jobs)

    industries = fetch_bls_ces_industries()
    sources_status["bls_ces_industries"] = {
        "ok": industries.get("fetch_ok"),
        "pulled_at": industries.get("pulled_at"),
        "n_states": len(industries.get("states") or {}),
        "notes": industries.get("notes"),
    }
    _write_json(config.DATA_FILES["industries"], industries)

    fhfa = fetch_fhfa_hpi_yoy()
    sources_status["fhfa_hpi"] = {
        "ok": fhfa.get("fetch_ok"),
        "pulled_at": fhfa.get("pulled_at"),
        "n_states": len(fhfa.get("states") or {}),
        "notes": fhfa.get("notes"),
    }
    _write_json(config.DATA_FILES["fhfa"], fhfa)

    redfin = fetch_redfin_state_prices()
    sources_status["redfin_state_prices"] = {
        "ok": redfin.get("fetch_ok"),
        "pulled_at": redfin.get("pulled_at"),
        "n_states": len(redfin.get("states") or {}),
        "notes": redfin.get("notes"),
    }
    _write_json(config.DATA_FILES["state_prices"], redfin)

    # Still manual / web-researched
    for key, note in [
        ("metro_prices", "Extend with Redfin metro medians live pull."),
        ("suburbs", "Usually web-researched; write structured results after live suburb search."),
    ]:
        _write_json(
            config.DATA_FILES[key],
            {
                "pulled_at": _now_iso(),
                "live_fetch_attempted": True,
                "fetch_ok": False,
                "states": {},
                "notes": [note, "Marked incomplete - do not invent values in build_report."],
            },
        )

    sources_payload = {
        "pulled_at": _now_iso(),
        "urls": {
            "fred_median_income": config.FRED_MEDIAN_INCOME_URL,
            "census_acs_income_brief": config.CENSUS_ACS_INCOME_BRIEF,
            "bls_api": config.BLS_API_TIMESERIES,
            "bls_industry_chart": config.BLS_INDUSTRY_CHART,
            "bls_laus": config.BLS_LAUS,
            "bea_api": config.BEA_API,
            "fhfa_hpi_po_state": config.FHFA_HPI_PO_STATE,
            "redfin_state_tracker": config.REDFIN_STATE_TRACKER,
        },
        "status": sources_status,
    }
    _write_json(config.DATA_FILES["sources"], sources_payload)

    meta = {
        "analysis_run_at": _now_iso(),
        "live_fetch_required": True,
        "skipped_cache": True,
        "census_api_key_present": bool(config.CENSUS_API_KEY),
        "fred_api_key_present": bool(config.FRED_API_KEY),
        "bls_api_key_present": bool(config.BLS_API_KEY),
        "bea_api_key_present": bool(config.BEA_API_KEY),
        "sources": sources_status,
        "spec": "rental_market_spec.md - Durable live-data pipeline",
        "next": "Run: python -m pipeline.build_report",
    }
    _write_json(config.DATA_FILES["meta"], meta)

    print("fetch complete - review data/meta.json for failures before building scores")
    return 0


if __name__ == "__main__":
    # Allow `python pipeline/fetch_all.py` from repo root
    if str(config.ROOT) not in sys.path:
        sys.path.insert(0, str(config.ROOT))
    raise SystemExit(main())

