"""
One-shot monthly refresh: live fetch → rebuild all sibling reports.

Usage (from repo root):
  python -m pipeline.refresh_all
  python -m pipeline.refresh_all --skip-fetch   # rebuild from existing data/ only
  python -m pipeline.refresh_all --fetch-only

Requires env (or .env): CENSUS_API_KEY, FRED_API_KEY, BLS_API_KEY, BEA_API_KEY.
FHFA + Redfin need no keys.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from pipeline import config


REQUIRED_SOURCES = (
    "fred_median_income",
    "census_acs1",
    "bea_sainc1",
    "bls_laus",
    "bls_ces_industries",
    "fhfa_hpi",
    "redfin_state_prices",
)


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m")


def _check_meta(*, strict: bool) -> int:
    path = config.DATA_FILES["meta"]
    if not path.exists():
        print(f"ERROR: missing {path}", file=sys.stderr)
        return 1
    meta = json.loads(path.read_text(encoding="utf-8"))
    sources = meta.get("sources") or {}
    failed = [name for name in REQUIRED_SOURCES if not (sources.get(name) or {}).get("ok")]
    missing_keys = [
        k
        for k, present in (
            ("CENSUS_API_KEY", meta.get("census_api_key_present")),
            ("FRED_API_KEY", meta.get("fred_api_key_present")),
            ("BLS_API_KEY", meta.get("bls_api_key_present")),
            ("BEA_API_KEY", meta.get("bea_api_key_present")),
        )
        if not present
    ]
    if missing_keys:
        print(f"WARN: keys not present in env: {', '.join(missing_keys)}")
    if failed:
        msg = f"source fetch failures: {', '.join(failed)}"
        if strict:
            print(f"ERROR: {msg}", file=sys.stderr)
            return 1
        print(f"WARN: {msg} (continuing; builders mark unavailable)")
    print(f"meta ok - analysis_run_at={meta.get('analysis_run_at')}")
    return 0


def _build_apartment() -> None:
    from pipeline import build_apartment_report as apt

    text = apt.build()
    apt.OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {apt.OUT.name} ({len(text):,} chars)")


def _build_sfh() -> None:
    from pipeline import build_sfh_appreciation_report as sfh

    sfh.main()


def _archive_reports(month: str) -> None:
    arch = config.ROOT / "archives" / month
    arch.mkdir(parents=True, exist_ok=True)
    for name in (
        "rental_market_report.md",
        "apartment_market_report.md",
        "sfh_appreciation_report.md",
        "data/meta.json",
    ):
        src = config.ROOT / name
        if not src.exists():
            continue
        dest = arch / Path(name).name
        dest.write_bytes(src.read_bytes())
        print(f"archived {dest.relative_to(config.ROOT)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fetch live data and rebuild all Market reports.")
    parser.add_argument("--skip-fetch", action="store_true", help="Skip pipeline.fetch_all")
    parser.add_argument("--fetch-only", action="store_true", help="Only fetch; do not build reports")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if any required source in meta.json is not ok",
    )
    parser.add_argument(
        "--archive",
        action="store_true",
        help="Copy reports + meta into archives/YYYY-MM/",
    )
    args = parser.parse_args(argv)

    if not args.skip_fetch:
        from pipeline.fetch_all import main as fetch_main

        code = fetch_main()
        if code:
            return code
    else:
        print("skip-fetch: using existing data/")

    if _check_meta(strict=args.strict):
        return 1

    if args.fetch_only:
        print("fetch-only: done")
        return 0

    from pipeline.build_report import main as build_base

    if build_base():
        return 1
    _build_apartment()
    _build_sfh()

    if args.archive:
        _archive_reports(_stamp())

    print("refresh_all complete")
    print("Judgment pass still recommended for Top 10 / Legal / apartment narrative overlays.")
    return 0


if __name__ == "__main__":
    if str(config.ROOT) not in sys.path:
        sys.path.insert(0, str(config.ROOT))
    raise SystemExit(main())
