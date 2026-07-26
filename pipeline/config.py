"""Shared paths and source config for the rental-market pipeline."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REPORT_PATH = ROOT / "rental_market_report.md"
SPEC_PATH = ROOT / "rental_market_spec.md"


def _load_dotenv(path: Path) -> None:
    """Load KEY=VALUE from .env into os.environ (does not overwrite existing env vars)."""
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


_load_dotenv(ROOT / ".env")

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
    "bea": DATA_DIR / "bea.json",
    "fhfa": DATA_DIR / "fhfa.json",
}

# Optional secrets / keys — never commit real keys
CENSUS_API_KEY = os.environ.get("CENSUS_API_KEY", "").strip()
FRED_API_KEY = os.environ.get("FRED_API_KEY", "").strip()
BLS_API_KEY = os.environ.get("BLS_API_KEY", "").strip()
BEA_API_KEY = os.environ.get("BEA_API_KEY", "").strip()

FRED_API_BASE = "https://api.stlouisfed.org/fred"
FRED_MEDIAN_INCOME_URL = (
    "https://fred.stlouisfed.org/release/tables?eid=259462&rid=249"
)
# CPS ASEC median HH income (current $): MEHOINUS{ST}A646N
FRED_MEDIAN_SERIES_SUFFIX = "A646N"
CENSUS_ACS_INCOME_BRIEF = (
    "https://www2.census.gov/library/publications/2025/demo/acsbr-025.pdf"
)
CENSUS_API_ACS1 = "https://api.census.gov/data/{year}/acs/acs1"
CENSUS_API_ACS1_SUBJECT = "https://api.census.gov/data/{year}/acs/acs1/subject"
BLS_API_TIMESERIES = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
BLS_INDUSTRY_CHART = (
    "https://www.bls.gov/charts/state-employment-and-unemployment/"
    "industry-employment-by-state.htm"
)
BLS_LAUS = "https://www.bls.gov/news.release/laus.htm"
BEA_API = "https://apps.bea.gov/api/data/"
FHFA_HPI_PO_STATE = (
    "https://www.fhfa.gov/hpi/download/quarterly_datasets/hpi_po_state.txt"
)
REDFIN_STATE_TRACKER = (
    "https://redfin-public-data.s3.us-west-2.amazonaws.com/"
    "redfin_market_tracker/state_market_tracker.tsv000.gz"
)

# State FIPS for LAUS (LASST) / CES SAE (SMU) series
STATE_FIPS = {
    "Alabama": "01", "Alaska": "02", "Arizona": "04", "Arkansas": "05",
    "California": "06", "Colorado": "08", "Connecticut": "09", "Delaware": "10",
    "District of Columbia": "11", "Florida": "12", "Georgia": "13", "Hawaii": "15",
    "Idaho": "16", "Illinois": "17", "Indiana": "18", "Iowa": "19", "Kansas": "20",
    "Kentucky": "21", "Louisiana": "22", "Maine": "23", "Maryland": "24",
    "Massachusetts": "25", "Michigan": "26", "Minnesota": "27", "Mississippi": "28",
    "Missouri": "29", "Montana": "30", "Nebraska": "31", "Nevada": "32",
    "New Hampshire": "33", "New Jersey": "34", "New Mexico": "35", "New York": "36",
    "North Carolina": "37", "North Dakota": "38", "Ohio": "39", "Oklahoma": "40",
    "Oregon": "41", "Pennsylvania": "42", "Rhode Island": "44", "South Carolina": "45",
    "South Dakota": "46", "Tennessee": "47", "Texas": "48", "Utah": "49",
    "Vermont": "50", "Virginia": "51", "Washington": "53", "West Virginia": "54",
    "Wisconsin": "55", "Wyoming": "56",
}

# CES SAE supersectors (thousands of employees, data type 01)
BLS_CES_INDUSTRIES = [
    ("00000000", "Total nonfarm"),
    ("10000000", "Mining / energy-adjacent"),
    ("20000000", "Construction"),
    ("30000000", "Manufacturing"),
    ("40000000", "Trade / logistics"),
    ("50000000", "Information"),
    ("55000000", "Financial activities"),
    ("60000000", "Professional services"),
    ("65000000", "Education & health"),
    ("70000000", "Leisure / hospitality"),
    ("80000000", "Other services"),
    ("90000000", "Government"),
]

USER_AGENT = (
    "Mozilla/5.0 (compatible; MarketPipeline/1.0; +local research; not for abuse)"
)
