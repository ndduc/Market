# Market

US residential investment screening for all 50 states + D.C. Informational only — not financial or legal advice.

**Sibling lenses (same report format skeleton):**

| Lens | Report | Spec |
|------|--------|------|
| **Cash-flow–balanced rental** (SFR + 2–4 unit) | [`rental_market_report.md`](rental_market_report.md) | [`rental_market_spec.md`](rental_market_spec.md) |
| **Apartments** (5+ unit conventional multifamily) | [`apartment_market_report.md`](apartment_market_report.md) | [`apartment_market_spec.md`](apartment_market_spec.md) |
| **Single-family appreciation / equity path** | [`sfh_appreciation_report.md`](sfh_appreciation_report.md) | [`sfh_appreciation_spec.md`](sfh_appreciation_spec.md) |

## Read the reports (web view)

**GitHub Pages:**

**https://ndduc.github.io/Market/**

| Report | GitHub Pages | GitHub blob | Markdown preview |
|--------|--------------|-------------|------------------|
| SFR / 2–4 | [rental_market_report](https://ndduc.github.io/Market/rental_market_report) | [blob](https://github.com/ndduc/Market/blob/master/rental_market_report.md) | [preview](https://markdown.github.com/?url=https://raw.githubusercontent.com/ndduc/Market/master/rental_market_report.md) |
| Apartments | [apartment_market_report](https://ndduc.github.io/Market/apartment_market_report) | [blob](https://github.com/ndduc/Market/blob/master/apartment_market_report.md) | [preview](https://markdown.github.com/?url=https://raw.githubusercontent.com/ndduc/Market/master/apartment_market_report.md) |
| SFH appreciation | [sfh_appreciation_report](https://ndduc.github.io/Market/sfh_appreciation_report) | [blob](https://github.com/ndduc/Market/blob/master/sfh_appreciation_report.md) | [preview](https://markdown.github.com/?url=https://raw.githubusercontent.com/ndduc/Market/master/sfh_appreciation_report.md) |

## Files

| File | Role |
|------|------|
| [`rental_market_report.md`](rental_market_report.md) | Canonical base rental report (format template) |
| [`rental_market_spec.md`](rental_market_spec.md) | Base rental spec + rebuild contract |
| [`apartment_market_report.md`](apartment_market_report.md) | Apartment (5+) report — same section format |
| [`apartment_market_spec.md`](apartment_market_spec.md) | Apartment sub-spec |
| [`sfh_appreciation_report.md`](sfh_appreciation_report.md) | Sibling SFH appreciation / equity-path report |
| [`sfh_appreciation_spec.md`](sfh_appreciation_spec.md) | Appreciation sibling spec + refresh contract |
| `pipeline/` | Live fetch → `data/` → report build |
| `data/` | Fetched JSON used by the builders |

## Refresh

Copy `.env.example` → `.env` and set `CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, and `BEA_API_KEY` (gitignored; **do not commit `.env`**).

No-key sources also pulled each run: **FHFA** HPI (appreciation) and **Redfin** public state market tracker (sale prices).

### One-shot (local)

```bash
python -m pipeline.refresh_all              # fetch + rebuild all three reports
python -m pipeline.refresh_all --archive    # also copy into archives/YYYY-MM/
python -m pipeline.refresh_all --skip-fetch # rebuild from existing data/ only
```

Or step-by-step:

```bash
python -m pipeline.fetch_all
python -m pipeline.build_report                          # base rental report
python -m pipeline.build_apartment_report                # apartment (5+) sibling
python -m pipeline.build_sfh_appreciation_report         # SFH appreciation sibling
```

### Daily automation (GitHub Actions)

Workflow: [`.github/workflows/monthly-refresh.yml`](.github/workflows/monthly-refresh.yml)

- Runs **every day** (14:00 UTC) and on manual **Run workflow**
- Uses repo **Actions secrets** (not files in git): `CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY`
- Opens a PR on branch `chore/daily-data-refresh` with rebuilt `data/` + reports (+ `archives/YYYY-MM/`)

**One-time setup** (GitHub → this repo → **Settings → Secrets and variables → Actions → New repository secret**), add each key from your local `.env`.

Or with [GitHub CLI](https://cli.github.com/) from the repo root:

```bash
gh secret set CENSUS_API_KEY < .env   # or: gh secret set CENSUS_API_KEY
gh secret set FRED_API_KEY
gh secret set BLS_API_KEY
gh secret set BEA_API_KEY
```

Then **Actions → Daily data refresh → Run workflow** to test.

Even for free/public API keys, prefer Actions secrets over committing `.env` so keys are not permanently stored in git history.
