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

import json
import re
import sys
import urllib.error
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


def fetch_fred_median_income() -> dict[str, Any]:
    """Parse FRED CPS ASEC median HH income release table HTML when available."""
    ok, body = _http_get(config.FRED_MEDIAN_INCOME_URL)
    result: dict[str, Any] = {
        "metric": "median_household_income",
        "source": "CPS ASEC via FRED",
        "source_url": config.FRED_MEDIAN_INCOME_URL,
        "as_of": "2024",
        "pulled_at": _now_iso(),
        "fetch_ok": ok,
        "states": {},
        "mean_household_income": {},  # filled by Census ACS when key available
        "notes": [],
    }
    if not ok:
        result["notes"].append(f"FRED fetch failed: {body}")
        return result

    # Rows look like: | Alabama | 65,560 | ...
    matches = re.findall(
        r"\|\s*([A-Za-z .]+?)\s*\|\s*([\d,]+)\s*\|",
        body,
    )
    skip = {"name", "the united states", "current dollars"}
    for name, num in matches:
        name = name.strip()
        if name.lower() in skip or not name:
            continue
        if name == "District of Columbia" or name in _STATE_NAMES:
            try:
                result["states"][name] = int(num.replace(",", ""))
            except ValueError:
                continue

    if not result["states"]:
        result["fetch_ok"] = False
        result["notes"].append(
            "FRED HTML parsed but no state rows found 窶・site layout may have changed "
            "or content was blocked; mark median income unavailable or re-fetch via browse."
        )
    else:
        result["notes"].append(f"Parsed {len(result['states'])} state/DC medians from FRED HTML.")
    return result


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
            "CENSUS_API_KEY not set 窶・skipped Census API. "
            "Set env var for live ACS median/mean/race pulls."
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
        out["mean"][name] = None  # subject table S1901 mean not in this call
        out["race"][name] = {
            "white_alone_pct": round(100 * white / total, 1) if total else None,
            "black_alone_pct": round(100 * black / total, 1) if total else None,
            "asian_alone_pct": round(100 * asian / total, 1) if total else None,
            "hispanic_any_race_pct": round(100 * hisp / total, 1) if total else None,
            "note": "Race alone categories; Hispanic is ethnicity (any race). Not NH-adjusted.",
        }
    out["fetch_ok"] = bool(out["median"])
    out["notes"].append(
        "Mean household income not included in this endpoint 窶・extend fetch with S1901/S1902."
    )
    return out


_STATE_NAMES = {
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
    "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho",
    "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
    "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
    "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
    "Washington", "West Virginia", "Wisconsin", "Wyoming",
}


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

    # Merge income file: prefer live FRED medians; attach Census medians as alternate if present
    income_payload = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "median_household_income": income_fred.get("states") or {},
        "median_source": income_fred.get("source_url"),
        "median_as_of": income_fred.get("as_of"),
        "mean_household_income": {},
        "mean_status": "unavailable",
        "census_acs_median_alt": census.get("median") or {},
        "notes": (income_fred.get("notes") or []) + (census.get("notes") or []),
    }
    if census.get("mean"):
        # reserved for future S1901 pull
        filled = {k: v for k, v in census["mean"].items() if v is not None}
        if filled:
            income_payload["mean_household_income"] = filled
            income_payload["mean_status"] = "partial"
    _write_json(config.DATA_FILES["income"], income_payload)

    demo_payload = {
        "pulled_at": _now_iso(),
        "live_fetch": True,
        "source": "Census ACS 1-year API" if census.get("fetch_ok") else "unavailable_this_run",
        "states": census.get("race") or {},
        "notes": census.get("notes")
        or [
            "Race shares not live-fetched this run (set CENSUS_API_KEY). "
            "Builder/report may keep prior Decennial figures only if explicitly labeled STALE 窶・"
            "default spec forbids silent stale reuse."
        ],
    }
    _write_json(config.DATA_FILES["demographics"], demo_payload)

    # Placeholders overwritten each run so meta proves attempt; expand with real live pulls next
    for key, note in [
        ("industries", "Extend with BLS CES / industry chart live parse or download."),
        ("state_prices", "Extend with Redfin/Zillow/Forbes live scrape or published tables."),
        ("metro_prices", "Extend with Redfin metro medians live pull."),
        ("jobs", "Extend with BLS LAUS / metro employment live pull."),
        ("suburbs", "Usually web-researched; write structured results after live suburb search."),
    ]:
        _write_json(
            config.DATA_FILES[key],
            {
                "pulled_at": _now_iso(),
                "live_fetch_attempted": True,
                "fetch_ok": False,
                "states": {},
                "notes": [note, "Marked incomplete 窶・do not invent values in build_report."],
            },
        )

    sources_payload = {
        "pulled_at": _now_iso(),
        "urls": {
            "fred_median_income": config.FRED_MEDIAN_INCOME_URL,
            "census_acs_income_brief": config.CENSUS_ACS_INCOME_BRIEF,
            "bls_industry_chart": config.BLS_INDUSTRY_CHART,
            "bls_laus": config.BLS_LAUS,
        },
        "status": sources_status,
    }
    _write_json(config.DATA_FILES["sources"], sources_payload)

    meta = {
        "analysis_run_at": _now_iso(),
        "live_fetch_required": True,
        "skipped_cache": True,
        "census_api_key_present": bool(config.CENSUS_API_KEY),
        "sources": sources_status,
        "spec": "rental_market_spec.md 窶・Durable live-data pipeline",
        "next": "Run: python -m pipeline.build_report",
    }
    _write_json(config.DATA_FILES["meta"], meta)

    print("fetch complete 窶・review data/meta.json for failures before building scores")
    return 0


if __name__ == "__main__":
    # Allow `python pipeline/fetch_all.py` from repo root
    if str(config.ROOT) not in sys.path:
        sys.path.insert(0, str(config.ROOT))
    raise SystemExit(main())

