# Market

US rental-market screening report for all 50 states + D.C. (single-family and 2–4 unit multifamily). Informational only — not financial or legal advice.

## Read the report (web view)

Open the full rendered Markdown on GitHub:

**https://github.com/ndduc/Market/blob/master/rental_market_report.md**

Alternate clean Markdown preview (raw file → HTML):

**https://markdown.github.com/?url=https://raw.githubusercontent.com/ndduc/Market/master/rental_market_report.md**

## Files

| File | Role |
|------|------|
| [`rental_market_report.md`](rental_market_report.md) | Canonical report (index, matrices, all-state deep dives) |
| [`rental_market_spec.md`](rental_market_spec.md) | Spec + rebuild contract |
| `pipeline/` | Live fetch → `data/` → report build |
| `data/` | Fetched JSON used by the builder |

## Refresh

Copy `.env.example` → `.env` and set `CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, and `BEA_API_KEY` (gitignored; never commit).

No-key sources also pulled each run: **FHFA** HPI (appreciation) and **Redfin** public state market tracker (sale prices).

```bash
python -m pipeline.fetch_all
python -m pipeline.build_report
```
