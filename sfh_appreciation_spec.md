# US Single-Family Home Appreciation Investment Spec

## Goal
[↑ Back to Spec index](#spec-index)

Produce a comparable, evidence-based **single-family home appreciation / equity-path** analysis for **all 50 US states + DC**, and for each state’s **major cities / metros**, so an investor can:

1. Identify the best markets for **appreciation-first** single-family investing (5–10+ year hold)
2. Rank markets by **price growth, jobs/migration demand, supply constraints, entry vs income, liquidity/exit, and owner-law / remote ops**
3. Accept that **day-one cash flow is secondary** (thin or break-even carry can be OK if reserves and exit liquidity hold)
4. Understand **why** each market ranks where it does under this lens
5. Stay clearly separate from the base **cash-flow–balanced rental** analysis

This document is both the analysis specification and the reusable AI prompt.

**Canonical sibling report:** `sfh_appreciation_report.md`  
**Format parent (section skeleton):** `rental_market_report.md` — same section order, Index / Back to Index, companion tables, city boards, all-state deep dives, A–Z. Retitle and re-score for appreciation-first single-family; do **not** invent a different outline.  
**Do not break:** `rental_market_spec.md`, `rental_market_report.md`, or the existing `pipeline/` + `data/` contract for the base rental report.  
**Apartment sibling:** `apartment_market_spec.md` / `apartment_market_report.md` — 5+ unit multifamily; do not merge rankings.

**Canonical data philosophy:** reuse the durable live-fetch → `data/` → build approach:

```text
python -m pipeline.fetch_all
# then rebuild this sibling report (see Durable live-data pipeline)
```

Keys live in `.env` (`CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY`). Data must be **pulled live on every full refresh** — never treat prior `data/` files as current without re-fetching.

---

## Spec index

Every section below includes **[↑ Back to Spec index](#spec-index)** under its heading.

| Section | What it’s for |
|---------|----------------|
| [Goal](#goal) | Purpose of this sibling analysis |
| [Scope](#scope) | SFH-only, appreciation objective, geography |
| [How this differs from the base rental spec](#how-this-differs-from-the-base-rental-spec) | Explicit contrast |
| [Ranking dimensions](#ranking-dimensions) | Pillars, weights, overlays |
| [Required outputs](#required-outputs) | Report format must match base skeleton |
| [Durable live-data pipeline](#durable-live-data-pipeline-mandatory) | fetch_all + sibling build; `data/` map |
| [Live data & web search](#live-data--web-search-requirements-mandatory) | What is automated vs still searched |
| [Analysis rules](#analysis-rules-for-the-ai) | Scoring and honesty rules |
| [Scoring rubric](#suggested-scoring-rubric-directional) | 1–10 directional guide |
| [Deliverable format](#deliverable-format) | Exact report shape to emit |
| [AI prompt](#ai-prompt-copy-paste) | Copy-paste operator prompt |
| [Optional follow-ups](#optional-follow-up-prompts) | Screens and refresh prompts |
| [Out of scope](#out-of-scope-unless-asked-later) | What this analysis does not do |

---

## Scope
[↑ Back to Spec index](#spec-index)

### Geography

[↑ Back to Spec index](#spec-index)

- **States:** all 50 states + District of Columbia
- **Cities / metros:** major metro / city markets that matter for **single-family** equity (default top 2–5 by population / SFH inventory)
- Prefer **MSA / metro framing**; keep parent metro names visible; research **1–3 top suburbs** with an **appreciation / tenant-quality** tilt (cash-flow suburbs optional for contrast only)
- Do **not** create a separate national rank row for every suburb

### Property type scope (in scope)

[↑ Back to Spec index](#spec-index)

| Type | In this sibling? |
|------|------------------|
| **Single-family house (SFR)** — detached 1-unit | **Yes — primary and only ranking universe** |
| **2–4 unit multifamily** | **Out of primary scope** (may note as alternate product; do not dual-rank) |
| **Large apartments (5+)** | Out of scope |
| **Condos / HOA-heavy** | Risk overlay only unless user asks |

### Investor objective

[↑ Back to Spec index](#spec-index)

| Input | Default for this sibling |
|-------|--------------------------|
| Strategy preference | **Appreciation / equity path** (not cash-flow-first) |
| Property types | **Single-family only** |
| Hold period | **5–10+ years** |
| Cash flow | **Secondary** — thin / break-even acceptable with adequate reserves |
| Capital / buy box | Mid-to-upper entry OK if liquidity and demand support; disclose capital burden |
| Local vs remote | Remote-capable preferred |
| Risk tolerance | Moderate (equity path ≠ ignore insurance / regulation / exit risk) |

### Investor lenses (two parallel leaderboards)

[↑ Back to Spec index](#spec-index)

Keep the base report’s dual legal lenses, applied to equity-path markets:

| Lens | Focus |
|------|--------|
| **Landlord-protection set** | Owner-friendly law + workable remote ops **and** a coherent appreciation thesis |
| **Tenant-protection set** | Stronger renter protections that still have an **equity / long-hold** case (e.g., Chicago, upstate NY, North Jersey) |

---

## How this differs from the base rental spec
[↑ Back to Spec index](#spec-index)

| Topic | Base (`rental_market_spec.md`) | This sibling |
|-------|--------------------------------|--------------|
| Primary goal | Balanced rental investing (cash flow + appreciation) | **Appreciation / equity path** |
| Property types | SFR **and** 2–4 unit MF | **SFR only** |
| Econ weights | Equal Job / Price / Cash / Appr (25% each) | **Appr 40% / Jobs 30% / Price 20% / Cash 10%** |
| Price pillar | Affordability (higher = cheaper entry) | **Entry vs income + exit liquidity** for equity buys |
| Cash pillar | Primary income realism | **Carry tolerance** (thin OK) |
| Typical top markets | Midwest CF leaders (OH, IN, AR, …) | **FHFA + liquidity / structural demand** leaders (often IL, WI, CT, NJ, PA, upstate NY, KY, … plus selected supply-constrained coasts/Sun Belt) |
| Report file | `rental_market_report.md` | `sfh_appreciation_report.md` |
| Format | Canonical | **Must mirror** base section skeleton |

---

## Ranking dimensions
[↑ Back to Spec index](#spec-index)

Score every state and major city on these pillars (1–10) plus composite.

| Pillar | Weight in Econ | What to measure | Example signals |
|--------|---------------:|-----------------|-----------------|
| **1. Appreciation** | **40%** | Equity path | FHFA HPI YoY (required), 5–10y context, supply constraints, oversupply risk |
| **2. Jobs / demand** | **30%** | Employment + migration | Unemployment, payroll growth, **top industries**, migration / population, concentration risk |
| **3. Price (entry vs income + liquidity)** | **20%** | Capital feasibility for equity | Median/typical price, **price-to-income**, buyer-pool / exit depth — **not** “cheapest wins” |
| **4. Cash (carry)** | **10%** | Ability to hold | Thin yield OK; haircut for tax/insurance/vacancy; flag forced-sale risk |

**Also score (shown, not necessarily in Econ):** Owner law, Tenant law, Confidence.

### Required metrics (do not skip)

[↑ Back to Spec index](#spec-index)

Reuse the base spec’s required metric definitions for:

- **Top job industries** (state + featured metros)
- **Demographics & income** (race/ethnicity context; median + mean HH income; price-to-income)
- **Median + typical prices** (label measure; no invented averages)
- **Entry capital & shock reserves** (25% down default, cash to close ≈ 28%, 6–9 mo PITI)
- **Suburb research** with **App** tilt labeled

Cash-flow / gross-yield screens are **optional secondary** notes — not the ranking objective.

### Standard financing / entry capital (appreciation-adapted)

[↑ Back to Spec index](#spec-index)

| Assumption | Default (disclose in Methodology) |
|------------|-----------------------------------|
| Down payment | **25%** investor default for **comparability**. Note that some appreciation buyers use other leverage or cash — **any override must be labeled**; do not hide capital needs. |
| Closing | about **3%** of purchase (cash to close ≈ **28%** of median) |
| Rate band | Live investor band (cite); July 2026 midpoint screen **7.5%** if using about 7.0%–8.5% |
| Shock liquid | **6 months** PITI default; **9–12 months** if thin carry + high insurance/tax/regulation |
| Hold | **5–10+ years** |
| Stress | Rate +1%, rent −5%, insurance +50%, **price flat 24 months**, 6 months vacancy |

### Tie-breakers (when Econ is equal)

[↑ Back to Spec index](#spec-index)

1. Exit liquidity / metro depth  
2. Data confidence (High > Medium > Low)  
3. Lower catastrophe / insurance risk  
4. Stronger remote-operability  
5. Diversified job base over single-employer dependence  

### Mandatory overlays

[↑ Back to Spec index](#spec-index)

Insurance/catastrophe, property-tax drag, new supply / concessions, **liquidity/exit**, remote PM availability, ops intensity, industry concentration. For App buys: **under-reserved thin carry** is a first-class risk.

---

## Required outputs
[↑ Back to Spec index](#spec-index)

### Canonical report format (mandatory)

[↑ Back to Spec index](#spec-index)

**Format file:** match `rental_market_report.md` section order and navigation.  
**Output file:** `sfh_appreciation_report.md`.

#### Required section order

1. Header — title, date, coverage, **SFH-only**, appreciation objective, live-research note, disclaimer  
2. **Index** + **[↑ Back to Index](#index)** under every indexed heading  
3. What changed vs prior run (or vs base rental report on first publish)  
4. National market snapshot — **equity-path definition** + core conclusion (no SFR vs 2–4 dual takeaway as primary)  
5. Top 10 actionable → landlord-protection → tenant-protection (equity case) → avoid/watch  
6. All-state matrix companions **4a–4e** (same columns as base; redefine Price/Cash/Appr framing in prose)  
7. City leaderboards — appreciation-path metros; SFH equity list; jobs/migration; supply-constrained screens; App-tilt suburbs; light carry notes (not CF-primary boards)  
8. All-state deep dives (**every** state + D.C.) with Scores / Prices / Entry capital / Industries / Demographics / Top suburbs / Best fit / Risks / Confidence  
9. Legal highlights  
10. Insurance & property tax  
11. Property management & remote ops (**lighter** than base, still present)  
12. Acquisition workflow (appreciation-adapted)  
13. Methodology + **A–Z rank index**

**Markdown rule:** never use `~` for “approximately” (strikethrough). Use `about` or `≈`.

**Disclaimer:** informational only — not financial, legal, tax, insurance, or investment advice.

---

## Durable live-data pipeline (mandatory)
[↑ Back to Spec index](#spec-index)

### Exact refresh commands

[↑ Back to Spec index](#spec-index)

From repo root (`Market/`):

```powershell
# 1) Secrets — copy once, never commit
copy .env.example .env
# Set CENSUS_API_KEY, FRED_API_KEY, BLS_API_KEY, BEA_API_KEY

# 2) Live fetch (ALWAYS re-pull; overwrites data/*.json)
python -m pipeline.fetch_all

# 3) Confirm data/meta.json timestamps and per-source "ok": true

# 4) Build this sibling report from data/
python pipeline/build_sfh_appreciation_report.py

# 5) Narrative / web-search pass for legal, insurance, metro YoY leaders, suburb notes
#    Revise Top 10 / avoid / §7–§8 only if evidence moved
```

Do **not** wipe or rebuild `rental_market_report.md` when refreshing this sibling unless the user explicitly asks for a base rental refresh (`python -m pipeline.build_report`).

### Which base `data/` files apply

[↑ Back to Spec index](#spec-index)

| File | Use in this sibling |
|------|---------------------|
| `data/fhfa.json` | **Primary** appreciation signal (state YoY) |
| `data/state_prices.json` | Median / typical prices, entry capital |
| `data/jobs.json` | Unemployment / jobs pillar |
| `data/industries.json` | §4c + deep-dive industries |
| `data/income.json` | Median / mean HH income, price-to-income |
| `data/demographics.json` | Race/ethnicity context (§4d) |
| `data/bea.json` | Per-capita personal income context |
| `data/meta.json` / `sources.json` | Live-fetch stamp in Methodology |
| `data/metro_prices.json` | Placeholder until wired — mark metro averages `unavailable` if empty |
| `data/suburbs.json` | Placeholder — suburb notes still need web search |

### What still needs web search each refresh

[↑ Back to Spec index](#spec-index)

- Metro-level FHFA / price YoY leaderboards beyond state file  
- Suburb qualitative App notes and local comps  
- Landlord–tenant law updates  
- Insurance / tax overlay changes  
- Migration / permits / concessions narratives  
- §4a judgment tweaks when live data contradicts prior ranks  

---

## Live data & web search requirements (mandatory)
[↑ Back to Spec index](#spec-index)

Same hard rules as the base rental spec:

1. Re-fetch on every full run; overwrite `data/`.  
2. Do not invent prices, incomes, FHFA, or statutes.  
3. Mark missing fields `unavailable`.  
4. Cite sources with links / as-of dates.  
5. Prefer last 12–24 months for jobs/prices; longer windows OK for structural appreciation.  
6. If fetch/search unavailable, stop — do not fabricate a national ranking from memory.

---

## Analysis rules for the AI
[↑ Back to Spec index](#spec-index)

1. **Live data first** — FHFA, prices, jobs, income from `data/` after `fetch_all`.  
2. **Do not damage** base rental report/spec/pipeline outputs unless asked.  
3. **Appreciation-first honesty** — do not rank a market highly only because it is cheap or high-yield.  
4. **Carry honesty** — thin cash flow is allowed; **zero reserves** is not.  
5. **Liquidity honesty** — high FHFA in a tiny market is not automatically Top 10 actionable.  
6. **One-year ≠ destiny** — label structural App overlays as judgment; soft FHFA coasts need explicit caution.  
7. **SFH only** — no primary 2–4 unit shortlists.  
8. **Format match** — section skeleton of `rental_market_report.md`.  
9. **Plain English**; no `~` approx tildes.  
10. **Coverage completeness** — all 51 deep dives with the same field labels (narratives may be shorter).

---

## Suggested scoring rubric (directional)
[↑ Back to Spec index](#spec-index)

| Score | Appreciation | Jobs / demand | Price (entry+liquidity) | Cash (carry) |
|------:|--------------|---------------|-------------------------|--------------|
| 9–10 | Clear multi-year upside + strong recent HPI or structural constraint | Strong growth, diverse employers | Supported PTI + deep buyer pool | Comfortable carry |
| 7–8 | Solid upside / strong YoY | Solid / stable | Moderate capital, workable liquidity | Thin but manageable |
| 5–6 | Uncertain / flat | Mixed | Stretch or thinner exits | Break-even / soft |
| 3–4 | Soft / volatile | Weak or concentrated | Expensive vs income or illiquid | Likely negative without care |
| 1–2 | Declining thesis | Declining | Extreme capital + poor exit | Structurally poor / insurance-broken |

---

## Deliverable format
[↑ Back to Spec index](#spec-index)

Respond in Markdown **and**:

1. Live-fetch (overwrite `data/`) via `python -m pipeline.fetch_all`  
2. Build / refresh `sfh_appreciation_report.md` via `python pipeline/build_sfh_appreciation_report.py`  
3. Optionally archive `sfh_appreciation_report_YYYY-MM-DD.md`  
4. Leave `rental_market_report.md` unchanged unless a base refresh was requested  

If output length is limited: compress deep-dive narratives before dropping states or sections. **Never** drop all-state matrix prices or replace deep dives with remaining-state bullet cards.

---

## AI prompt (copy-paste)
[↑ Back to Spec index](#spec-index)

```text
You are a US single-family home APPRECIATION / equity-path investment analyst.

SIBLING SCOPE (MANDATORY):
- Strategy: appreciation / equity path, 5–10+ year hold. Cash flow is SECONDARY (thin OK with reserves).
- Property type: SINGLE-FAMILY HOUSES ONLY. Not apartments. Not 2–4 unit MF as primary lens.
- Output file: sfh_appreciation_report.md
- Spec: sfh_appreciation_spec.md
- Do NOT overwrite or break rental_market_report.md / rental_market_spec.md unless the user asks for a base rental refresh.

FORMAT (MANDATORY):
- Mirror rental_market_report.md section order, Index, [↑ Back to Index], companion tables 4a–4e, city boards, all-state deep dives, legal, insurance/tax, lighter PM, acquisition workflow, methodology, A–Z.
- Retitle and re-score for appreciation-first SFH. Do NOT invent a different outline.
- Column meanings: Price = entry-vs-income + liquidity (not pure cheapness); Cash = carry tolerance; Appr dominates.
- Econ weights: Appreciation 40% / Jobs 30% / Price 20% / Cash 10%.
- Plain English. No Markdown ~ for approximately (use about or ≈).
- Disclaimer: informational only — not financial advice.

LIVE DATA EVERY RUN:
1) Confirm .env keys: CENSUS_API_KEY, FRED_API_KEY, BLS_API_KEY, BEA_API_KEY
2) python -m pipeline.fetch_all  (overwrite data/)
3) Confirm data/meta.json timestamps and source ok flags
4) python pipeline/build_sfh_appreciation_report.py
5) Web-search pass: metro Appr leaders, App-tilt suburbs, legal/insurance updates
6) Only revise Top 10 / avoid / legal if evidence warrants
7) Cite FHFA YoY, Redfin prices, BLS jobs, income for rankings — do not invent numbers
8) Mark unavailable honestly

FINANCING DEFAULTS (disclose; label overrides):
- 25% down + about 3% closing (cash to close ≈ 28% of median)
- Shock liquid 6–9 months PITI
- Investor rate band about 7.0%–8.5% (7.5% screen midpoint) unless live quote
- Some App buyers use different leverage — still show transparent defaults

RANKING PRIORITIES:
- Overweight: FHFA/local price growth, jobs/migration, supply constraints, entry vs income, liquidity/exit, owner-law/remote ops
- De-emphasize: day-one cash-flow vs base rental report
- Favor appreciation leaders (often higher-price / supply-constrained / rebound metros) over Midwest CF leaders when evidence supports — justify with FHFA YoY / jobs / prices
- Tie-break: liquidity, confidence, lower catastrophe risk, remote ops, job diversity

Produce the full report with all 51 deep dives (shorter OK) matching base navigability.
```

---

## Optional follow-up prompts
[↑ Back to Spec index](#spec-index)

1. **Capital constraint:** “Re-rank for max purchase price of $[X] per SFH.”  
2. **Remote-only App screen:** “Prefer owner-friendly states with PM depth; keep App weights.”  
3. **Structural vs cyclical:** “Split Top 20 into (A) strong 1y FHFA and (B) soft FHFA but high structural constraint.”  
4. **Update pass:** “Re-run fetch_all, rebuild sfh_appreciation_report.md, show what changed.”  
5. **Contrast memo:** “Diff Top 10 vs rental_market_report.md Top 10 and explain each flip.”  
6. **Single-state deep dive:** “Expand [State] with ZIP-level App suburbs, DOM/exit notes, and 10-year hold stress.”  

---

## Out of scope (unless asked later)
[↑ Back to Spec index](#spec-index)

- Address-level underwriting  
- Primary rankings for 2–4 unit or large apartments  
- Short-term rental / Airbnb strategies  
- International markets  
- Personalized portfolio, tax filing, or insurance brokerage advice  
- Replacing the base cash-flow rental report  

---

*End of SFH appreciation sibling spec.*
