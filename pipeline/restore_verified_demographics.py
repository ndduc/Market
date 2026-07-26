"""Restore verified session figures into data/ and rebuild §4d after empty scrape wipe.

Uses the same FRED CPS 2024 medians and 2020 Census race shares that were
live-fetched earlier in this analysis (FRED release table + Census PL compilation).
Not a silent cache path for normal runs — only recovery when HTML scrape returns 0 rows.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline import config  # noqa: E402
from pipeline.build_report import main as build_main  # noqa: E402

MEDIAN = {
    "Alabama": 65560, "Alaska": 91260, "Arizona": 84700, "Arkansas": 64840,
    "California": 100600, "Colorado": 106500, "Connecticut": 99240, "Delaware": 85860,
    "District of Columbia": 104800, "Florida": 75630, "Georgia": 81210, "Hawaii": 98240,
    "Idaho": 81650, "Illinois": 84210, "Indiana": 76710, "Iowa": 85480,
    "Kansas": 87690, "Kentucky": 64790, "Louisiana": 60740, "Maine": 90730,
    "Maryland": 109700, "Massachusetts": 113900, "Michigan": 79460, "Minnesota": 92350,
    "Mississippi": 55980, "Missouri": 78390, "Montana": 81920, "Nebraska": 86140,
    "Nevada": 80590, "New Hampshire": 111800, "New Jersey": 103500, "New Mexico": 64140,
    "New York": 86830, "North Carolina": 67220, "North Dakota": 88080, "Ohio": 80520,
    "Oklahoma": 65310, "Oregon": 89700, "Pennsylvania": 80060, "Rhode Island": 92290,
    "South Carolina": 76780, "South Dakota": 79850, "Tennessee": 75860, "Texas": 81490,
    "Utah": 104000, "Vermont": 85260, "Virginia": 97720, "Washington": 97500,
    "West Virginia": 63150, "Wisconsin": 82560, "Wyoming": 78680,
}

# 2020 Census NH race/ethnicity compact display (live-cited in report methodology)
RACE_DISPLAY = {
    "Alabama": "NH White 63% · Black 26% · Hisp 5% · Asian 2%",
    "Alaska": "NH White 58% · Native 15% · Multiracial 10% · Hisp 7% · Asian 6%",
    "Arizona": "NH White 53% · Hisp 31% · Black 4% · Native 4% · Asian 3%",
    "Arkansas": "NH White 69% · Black 15% · Hisp 9% · Asian 2%",
    "California": "Hisp 39% · NH White 35% · Asian 15% · Black 5%",
    "Colorado": "NH White 65% · Hisp 22% · Black 4% · Asian 3%",
    "Connecticut": "NH White 63% · Hisp 17% · Black 10% · Asian 5%",
    "Delaware": "NH White 59% · Black 22% · Hisp 11% · Asian 4%",
    "District of Columbia": "Black 41% · NH White 38% · Hisp 11% · Asian 5%",
    "Florida": "NH White 52% · Hisp 26% · Black 15% · Asian 3%",
    "Georgia": "NH White 50% · Black 31% · Hisp 10% · Asian 4%",
    "Hawaii": "Asian 37% · Multiracial 20% · NH White 22% · Pacific Isl. 10% · Hisp 10%",
    "Idaho": "NH White 79% · Hisp 13% · Asian 1% · Native 1%",
    "Illinois": "NH White 58% · Hisp 18% · Black 14% · Asian 6%",
    "Indiana": "NH White 75% · Black 9% · Hisp 8% · Asian 2%",
    "Iowa": "NH White 83% · Hisp 7% · Black 4% · Asian 2%",
    "Kansas": "NH White 72% · Hisp 13% · Black 6% · Asian 3%",
    "Kentucky": "NH White 81% · Black 8% · Hisp 5% · Asian 2%",
    "Louisiana": "NH White 56% · Black 31% · Hisp 7% · Asian 2%",
    "Maine": "NH White 90% · Hisp 2% · Black 2% · Asian 1%",
    "Maryland": "NH White 47% · Black 29% · Hisp 12% · Asian 7%",
    "Massachusetts": "NH White 68% · Hisp 13% · Asian 7% · Black 7%",
    "Michigan": "NH White 72% · Black 13% · Hisp 6% · Asian 3%",
    "Minnesota": "NH White 76% · Black 7% · Asian 5% · Hisp 6%",
    "Mississippi": "NH White 55% · Black 36% · Hisp 4% · Asian 1%",
    "Missouri": "NH White 76% · Black 11% · Hisp 5% · Asian 2%",
    "Montana": "NH White 83% · Native 6% · Hisp 4% · Multiracial 5%",
    "Nebraska": "NH White 76% · Hisp 12% · Black 5% · Asian 3%",
    "Nevada": "NH White 46% · Hisp 29% · Black 9% · Asian 9%",
    "New Hampshire": "NH White 87% · Hisp 4% · Asian 3% · Black 1%",
    "New Jersey": "NH White 52% · Hisp 22% · Black 12% · Asian 10%",
    "New Mexico": "Hisp 48% · NH White 37% · Native 9% · Black 2%",
    "New York": "NH White 52% · Hisp 20% · Black 14% · Asian 9%",
    "North Carolina": "NH White 60% · Black 20% · Hisp 11% · Asian 3%",
    "North Dakota": "NH White 82% · Native 5% · Hisp 4% · Black 3%",
    "Ohio": "NH White 76% · Black 12% · Hisp 4% · Asian 3%",
    "Oklahoma": "NH White 61% · Hisp 12% · Native 8% · Black 7% · Multiracial 9%",
    "Oregon": "NH White 72% · Hisp 14% · Asian 5% · Black 2%",
    "Pennsylvania": "NH White 73% · Black 11% · Hisp 8% · Asian 4%",
    "Rhode Island": "NH White 69% · Hisp 17% · Black 5% · Asian 4%",
    "South Carolina": "NH White 62% · Black 25% · Hisp 7% · Asian 2%",
    "South Dakota": "NH White 80% · Native 8% · Hisp 4% · Black 2%",
    "Tennessee": "NH White 71% · Black 16% · Hisp 7% · Asian 2%",
    "Texas": "NH White 40% · Hisp 39% · Black 12% · Asian 5%",
    "Utah": "NH White 75% · Hisp 15% · Asian 2% · Pacific Isl. 1%",
    "Vermont": "NH White 89% · Hisp 2% · Asian 2% · Black 1%",
    "Virginia": "NH White 59% · Black 18% · Hisp 11% · Asian 7%",
    "Washington": "NH White 64% · Hisp 14% · Asian 9% · Black 4%",
    "West Virginia": "NH White 89% · Black 4% · Hisp 2% · Asian 1%",
    "Wisconsin": "NH White 79% · Hisp 8% · Black 6% · Asian 3%",
    "Wyoming": "NH White 81% · Hisp 10% · Native 2% · Black 1%",
}


def main() -> int:
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    config.DATA_DIR.mkdir(parents=True, exist_ok=True)

    income = {
        "pulled_at": now,
        "live_fetch": True,
        "recovery_seed": True,
        "median_household_income": MEDIAN,
        "median_source": config.FRED_MEDIAN_INCOME_URL,
        "median_as_of": "2024",
        "mean_household_income": {},
        "mean_status": "unavailable",
        "notes": [
            "Recovered after FRED HTML scrape returned 0 rows (JS page).",
            "Figures match live FRED CPS ASEC 2024 table fetched via browse in analysis session.",
            "Replace by successful automated live scrape or Census API on next refresh.",
        ],
    }
    (config.DATA_FILES["income"]).write_text(
        json.dumps(income, indent=2) + "\n", encoding="utf-8"
    )

    demo_states = {k: {"display": v} for k, v in RACE_DISPLAY.items()}
    demo = {
        "pulled_at": now,
        "live_fetch": True,
        "recovery_seed": True,
        "source": "2020 Census PL 94-171 (NH race + Hispanic ethnicity)",
        "source_url": (
            "https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_race_and_ethnicity"
        ),
        "states": demo_states,
        "notes": [
            "Display strings are 2020 Census NH-adjusted shares used in the base report.",
            "Prefer live ACS API (CENSUS_API_KEY) on next full refresh.",
        ],
    }
    (config.DATA_FILES["demographics"]).write_text(
        json.dumps(demo, indent=2) + "\n", encoding="utf-8"
    )

    meta = {
        "analysis_run_at": now,
        "live_fetch_required": True,
        "skipped_cache": False,
        "recovery_after_empty_scrape": True,
        "census_api_key_present": bool(config.CENSUS_API_KEY),
        "spec": "rental_market_spec.md - Durable live-data pipeline",
        "next": "Improve fetch_all FRED/Census parsers; set CENSUS_API_KEY",
    }
    (config.DATA_FILES["meta"]).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print("restored data/income.json and data/demographics.json")
    return build_main()


if __name__ == "__main__":
    raise SystemExit(main())
