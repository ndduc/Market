"""Shared paths and source config for the rental-market pipeline."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REPORT_PATH = ROOT / "rental_market_report.md"
SPEC_PATH = ROOT / "rental_market_spec.md"

# Live fetch always overwrites these (see rental_market_spec.md — Durable live-data pipeline)
DATA_FILES = {
    "meta": DATA_DIR / "meta.json",
    "income": DATA_DIR / "income.json",
    "demographics": DATA_DIR / "demographics.json",
    "industries": DATA_DIR / "industries.json",
    "state_prices": DATA_DIR / "state_prices.json",
    "metro_prices": DATA_DIR / "metro_prices.json",
    "jobs": DATA_DIR / "jobs.json",
    "suburbs": DATA_DIR / "suburbs.json",
    "sources": DATA_DIR / "sources.json",
}

# Optional secrets / keys — never commit real keys
CENSUS_API_KEY = os.environ.get("CENSUS_API_KEY", "").strip()

FRED_MEDIAN_INCOME_URL = (
    "https://fred.stlouisfed.org/release/tables?eid=259462&rid=249"
)
CENSUS_ACS_INCOME_BRIEF = (
    "https://www2.census.gov/library/publications/2025/demo/acsbr-025.pdf"
)
CENSUS_API_ACS1 = "https://api.census.gov/data/{year}/acs/acs1"
BLS_INDUSTRY_CHART = (
    "https://www.bls.gov/charts/state-employment-and-unemployment/"
    "industry-employment-by-state.htm"
)
BLS_LAUS = "https://www.bls.gov/news.release/laus.htm"

USER_AGENT = (
    "Mozilla/5.0 (compatible; MarketPipeline/1.0; +local research; not for abuse)"
)
