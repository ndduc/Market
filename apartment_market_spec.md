# US Apartment (Multifamily) Market Analysis Spec

## Goal
[↑ Back to Spec index](#spec-index)


Produce a comparable, evidence-based **apartment / conventional multifamily** investment analysis for **all 50 US states + D.C.**, and for each state's **major apartment metros / submarkets**, so an investor can:

1. Identify the best markets for **landlord-friendly** apartment investing (5+ unit communities)
2. Identify the best markets for **tenant-friendly / rent-regulated** environments that still have an apartment case
3. Rank markets by apartment economics: **jobs, entry / door pricing context, NOI / cash flow screens, value change / cap-rate context**
4. Understand **why** each market ranks where it does for apartments (not SFR / 2–4)
5. Distinguish **Class A vs B/C**, **garden vs mid/high-rise**, and **stabilized vs value-add** fit

This document is both the apartment analysis specification and the reusable AI prompt.

**Sibling (SFR / 2–4) report:** `rental_market_report.md` + `rental_market_spec.md` — residential small-property screens. Do **not** mix those rankings into apartment scores without re-underwriting.

**Sibling (SFH appreciation):** `sfh_appreciation_spec.md` / `sfh_appreciation_report.md` — equity-path single-family lens; separate rankings.

**Format contract (mandatory):** Every apartment report must reuse the **same section order, Index / Back-to-Index navigation, companion-table style, deep-dive field labels, tone, and plain-English rules** as the base file `rental_market_report.md`. Only the **property-type lens, metrics, and rankings** change.

**Canonical apartment report:** `apartment_market_report.md`

**Web presentation (GitHub Pages):** Served on **https://ndduc.github.io/Market/** — Top 10 overview + full detailed report for this sibling. Full contract: parent [`rental_market_spec.md` → Web presentation / GitHub Pages](rental_market_spec.md#web-presentation--github-pages). Do not rename §3 / §4 headings (overview extractor).

**Shared data:** Reuse live `data/` pulls from the parent pipeline (BLS jobs, Census demographics, FRED income, BEA, FHFA, Redfin) as **demand / context** inputs. Apartment-specific rents, occupancy, concessions, deliveries, cap rates, and per-door pricing require **live apartment search** each refresh — mark `unavailable` when missing. Do not invent numbers.

---

## Spec index

Every section below includes **[↑ Back to Spec index](#spec-index)** under its heading.

| Section | What it’s for |
|---------|----------------|
| [Goal](#goal) | Purpose of the apartment analysis |
| [Scope](#scope) | Geography, property types, investor lenses |
| [Ranking dimensions](#ranking-dimensions) | Apartment pillars, supply, cap rates, financing, PM |
| [Required outputs](#required-outputs) | Same format as base report; apartment column meanings |
| [Web presentation / GitHub Pages](#web-presentation--github-pages) | Overview + full URLs; §3/§4 lock (parent contract) |
| [Data & live search](#data--live-search-requirements-mandatory) | Shared `data/` + apartment-specific sources |
| [Analysis rules](#analysis-rules-for-the-ai) | Honesty and scoring rules |
| [Scoring rubric](#suggested-scoring-rubric-directional) | 1–10 directional guide for apartments |
| [Deliverable format](#deliverable-format) | Exact report shape |
| [AI prompt](#ai-prompt-copy-paste) | Copy-paste operator prompt |
| [Out of scope](#out-of-scope-unless-asked-later) | What this analysis does not do |

**Related files:** [Parent SFR/2–4 spec](rental_market_spec.md) · [Base format report](rental_market_report.md) · [Apartment report](apartment_market_report.md) · [SFH appreciation](sfh_appreciation_spec.md)

---

## Scope
[↑ Back to Spec index](#spec-index)


### Geography

[↑ Back to Spec index](#spec-index)

- **States:** all 50 states + District of Columbia
- **Cities / metros:** major **apartment** metros (MSA framing). Prefer metros with meaningful 5+ unit inventory.
- **Submarkets (not SFR suburbs):** Inside each major metro in Top 10, city boards, and deep dives, name **1–3 apartment submarkets** (e.g., Class B inner-ring, suburban garden corridor, CBD high-rise). Label **cash-flow / value-add**, **balanced**, or **growth / Class A** when they diverge.
- In the all-state matrix, keep primary apartment metros visible next to each state.

### Property types (this report only)

[↑ Back to Spec index](#spec-index)

| Type | In scope? | Notes |
|------|-----------|-------|
| **Conventional apartments (5+ units)** | **Yes — primary** | Garden, mid-rise, high-rise; Class A / B / C |
| **Small residential multifamily (2–4)** | No (cross-link only) | Covered by `rental_market_report.md` |
| **Single-family / build-to-rent SFR** | No (cross-link only) | Covered by base report |
| **Student / senior / affordable (LIHTC) / short-term** | Only if labeled | Do not fold into conventional screens without a label |
| **Condo / co-op as apartment substitute** | Out unless labeled | Different ownership / insurance stack |

### Investor lenses

[↑ Back to Spec index](#spec-index)

Default assumptions unless the user overrides:

- Balanced strategy (cash flow + modest value change), not pure trophy Class A coastal
- Willing to use **agency / commercial / DSCR-style** multifamily financing when available
- Prefer markets with **third-party multifamily operators** or on-site staffing norms
- 5–10+ year hold; moderate risk; remote ownership OK if professional management is available
- Underwrite **economic occupancy** (physical occupancy after concessions / bad debt), not asking rent alone

---

## Ranking dimensions
[↑ Back to Spec index](#spec-index)


Use the same **1–10 pillars** and companion tables as the base format (**4a–4e**), with apartment meanings:

| Pillar / table | Apartment meaning |
|----------------|-------------------|
| **Jobs** | Metro / state employment strength supporting renter demand (BLS) |
| **Price** | Affordability of **entry** for apartment deals — prefer **$/door**, **$/unit**, or **price per SF** when live; else directional affordability vs coastal trophy. Higher = easier entry. Redfin All-Residential medians are **context only**, not apartment comps. |
| **Cash** | Realistic NOI / cash-flow screen after vacancy, concessions, taxes, insurance, and **multifamily PM** (often about **4–8%** of EGI or flat per door — not the SFR 8–12% default) |
| **Appr.** | Value-change / cap-rate context (transaction cap rates, NOI growth, not only FHFA house HPI) |
| **Econ** | Simple average of Jobs / Price / Cash / Appr. (same formula as base) |
| **Owner / Tenant** | Same legal scoring idea as base, but **weight rent control, just-cause, and TOPA-like transfer rules more heavily** — they bind apartment portfolios harder than scattered SFR |
| **Conf.** | Data confidence (High / Medium / Low) |
| **4b** | Apartment price / rent / occupancy / concessions / cap-rate screens + major metros (not SFR sale medians as the primary buy-box) |
| **4c** | Top job industries (reuse BLS; same demand context as base) |
| **4d** | Demographics & income (reuse ACS / CPS; demand context only — never an exclusion criterion) |
| **4e** | **Apartment entry capital:** typical down **25–35%**, cash to close, reserves (often **6–12 months** debt service / operating), on a **stated deal-size screen** (e.g. illustrative 50–150 unit community) — label assumptions; mark `unavailable` if no live $/door |

### Apartment-specific overlays (required in narrative)

[↑ Back to Spec index](#spec-index)

Every full refresh must discuss:

1. **Supply / deliveries** — units under construction, deliveries, lease-up competition
2. **Occupancy & concessions** — physical vs economic occupancy; months free / fee waivers
3. **Cap rates** — transactional / survey ranges by class when available (national + regional direction)
4. **Financing** — agency (Fannie / Freddie), banks, life companies, bridge; DSCR / LTV norms; rate screens
5. **Operations** — on-site staff, turnover, amenity competition, Class A vs B/C expense ratios
6. **Regulation** — rent caps, just cause, local registration, TOPA / right of first refusal where material
7. **Insurance / tax** — same catastrophe and effective-rate overlays as base, applied to multifamily

### Yield / return definitions (do not improvise)

[↑ Back to Spec index](#spec-index)

- Prefer **cap rate** = NOI ÷ purchase price (trailing or forward — label which).
- **Gross rent multiplier / gross yield** only as a crude screen; never treat as cash-on-cash.
- Prefer **in-place / economic rent** after concessions; label **asking** when that is all that is available.
- Cash-flow score must haircut for vacancy, concessions, taxes, insurance, management, and turnover.

### Property management (apartment)

[↑ Back to Spec index](#spec-index)

| Field | Requirement |
|-------|-------------|
| **Monthly management** | Third-party multifamily often about **3–8%** of effective gross income (or flat **$/door/mo**); institutional self-managed portfolios differ |
| **Leasing** | Often in-house or lower % than SFR placement; still model turnover cost |
| **Notable operators** | Greystar, Avenue5, Asset Living, RPM Living, FPI, BH Management, and similar — landscape, not endorsement |
| **Underwriting default** | Unless quoted, assume about **5–6% of EGI** ongoing management for third-party screens (state in Methodology) |

### Entry capital & shock reserves (apartment)

[↑ Back to Spec index](#spec-index)

- Default screen: **30% down** (midpoint of 25–35%) + closing / acquisition costs (state assumption, often about **2–4%** of price).
- Shock / reserve: **6–12 months** of debt service + operating expense screen (use **9–12** in high-insurance, heavy-concession, or heavy-regulation markets).
- State a **illustrative deal size** in 4e / deep dives (e.g. “screen assumes a mid-size garden community”; `$/door unavailable` when no live print).
- Do **not** copy SFR “cash to close on Redfin median home” as the apartment buy-box without labeling it as residential context only.

---

## Required outputs
[↑ Back to Spec index](#spec-index)


### Canonical report format (mandatory)

[↑ Back to Spec index](#spec-index)

**Base format file:** `rental_market_report.md`

The apartment report **must match that report’s structure, tone, and section order**. Do not invent a different outline.

#### Required section order

1. **Header** — title (Apartment / Multifamily), analysis date, coverage, property types (**5+ unit apartments**), live-research confirmation, disclaimer; link to sibling SFR/2–4 report
2. **Index** — same jump-link pattern; every indexed heading gets **[↑ Back to Index](#index)** underneath; link What changed last as appendix
3. **National market snapshot** — apartment national bullets + yield/cap-rate definition + core conclusion + **Class A vs B/C** takeaway (replaces SFR vs 2–4 takeaway)
4. **Top 10 actionable markets** — apartment fit / caution  
   then **Best landlord-protection markets**  
   then **Best tenant-protection markets that still have an investment case**  
   then **Markets to avoid / watch**  
   (**Heading must remain exactly** `## 3. Top 10 actionable markets` — Pages overview extractor.)
5. **All-state ranking matrix** — companion **4a–4e** (apartment column meanings above)  
   (**Heading must remain exactly** `## 4. All-state ranking matrix` — overview stops before this.)
6. **City leaderboards** — cash flow / Class B-C value-add / Class A growth / submarkets / jobs (adapt board titles to apartments; no “best single-family” board)
7. **All-state deep dives** — **every state + D.C.** with fields: Scores, Prices (apartment screens), Entry capital, Top industries, Demographics / income, Top submarkets, Best fit, Risks, Confidence
8. **Legal** — verified highlights; emphasize rent regulation impact on apartments
9. **Insurance and property tax overlays**
10. **Property management rates & remote ops** — multifamily fee stack + operators
11. **Practical acquisition workflow** — multifamily LOI / PSA / due diligence / agency debt path
12. **Methodology and sources**
13. **A–Z actionable rank index**
14. **Appendix: What changed vs the prior run** (bottom; keep `#1-what-changed-vs-the-prior-run` anchor)

**Language:** Plain English. Do not use `~` or `~~` for “approximately” (Markdown strikethrough). Use **about** or **≈**.

**Honesty:** Cite sources or mark `unavailable`. Never invent apartment rents, cap rates, occupancy, or $/door.

---

## Web presentation / GitHub Pages
[↑ Back to Spec index](#spec-index)

Full contract (files, extractor, link/UX rules, appendix placement): parent **[Web presentation / GitHub Pages](rental_market_spec.md#web-presentation--github-pages)**.

This sibling’s live URLs:

| View | URL |
|------|-----|
| Hub | https://ndduc.github.io/Market/ |
| Overview | `overview.html?src=apartment_market_report.md` |
| Full | `view.html?src=apartment_market_report.md` |

**Locked headings (do not change):** `## 3. Top 10 actionable markets` and `## 4. All-state ranking matrix` — overview Pages slice between them.

---

## Data & live search requirements (mandatory)
[↑ Back to Spec index](#spec-index)


### Shared pipeline (parent repo)

[↑ Back to Spec index](#spec-index)

Reuse when present:

```text
python -m pipeline.fetch_all
```

Useful shared files: BLS unemployment / industries, Census ACS demographics, FRED income, BEA personal income, FHFA HPI (house — **context only**), Redfin residential medians (**context only**).

Apartment report builder may be added later; until then, refreshes may update `apartment_market_report.md` directly from live search + shared `data/`, still following this spec and the base format.

### Apartment-specific live search (every full refresh)

[↑ Back to Spec index](#spec-index)

Search and cite (as available): NMHC, Freddie Mac multifamily outlook, Fannie Mae, CoStar / CBRE / Cushman / Colliers / RealPage / Yardi Matrix summaries, local brokerage multifamily reports, HUD / Census housing vacancy where useful. Prefer primary or named research URLs and as-of dates.

Minimum national snapshot inputs each refresh:

- National / major-metro **occupancy or vacancy** direction
- **Concession** prevalence direction
- **Delivery / under-construction** direction
- **Cap rate** band by class or national average
- **Multifamily financing** rate / LTV / DSCR screen

---

## Analysis rules for the AI
[↑ Back to Spec index](#spec-index)


1. Rank for **apartments**, not SFR. Thin apartment inventory (many small Plains / Mountain states) lowers **Price** liquidity and **Conf.** even if SFR yields look strong in the sibling report.
2. **Supply and concessions** can dominate near-term Cash scores in Sun Belt lease-up markets.
3. **Rent control / just cause / TOPA** reduce Owner scores and Cash realism for apartments more than for scattered SFR.
4. Jobs + income support demand; demographics are context only — never rank states by race.
5. Extreme printed yields on Class C product often price in ops intensity, crime variance, deferred maintenance, and exit illiquidity — haircut Cash and Conf.
6. Keep sibling SFR rankings out of the apartment Top 10 unless re-scored under this spec.
7. When apartment metrics are missing, write `unavailable` and lower Confidence — do not backfill from Zillow SFR rents as if they were apartment comps without a label.

---

## Suggested scoring rubric (directional)
[↑ Back to Spec index](#spec-index)


| Score | Jobs | Price (entry) | Cash (NOI realism) | Appr. / cap context |
|------:|------|---------------|--------------------|---------------------|
| 9–10 | Very strong payroll / low UE | Cheap doors / high going-in yields available | Strong economic occupancy, light concessions | Clear value tailwind or wide cap vs peers |
| 7–8 | Solid | Affordable vs U.S. apartment peers | Workable after haircuts | Stable / modest positive |
| 5–6 | Mixed | Average | Thin after tax/ins/PM/concessions | Flat / uncertain |
| 3–4 | Soft | Expensive | Weak or concession-heavy | Soft values / expanding caps |
| 1–2 | Severe job loss | Trophy / infeasible for screen | Structurally poor | Distress or hostile regulation + price |

Owner law 9–10 = strong landlord baseline + rent-control preemption where relevant. Tenant law 9–10 = strong renter protections (still may have an investment case via appreciation or specialist operators).

---

## Deliverable format
[↑ Back to Spec index](#spec-index)


Emit **`apartment_market_report.md`** matching `rental_market_report.md` section order with apartment content. Update README links when the file is created or refreshed.

**Section order (aligned with Pages):** Index → National snapshot → Top 10 (`## 3. Top 10 actionable markets`) → matrix (`## 4. All-state ranking matrix`) → … → What changed appendix last (keep `#1-what-changed-vs-the-prior-run`). Do not put What changed early in the body.

---

## AI prompt (copy-paste)
[↑ Back to Spec index](#spec-index)


```text
Follow apartment_market_spec.md. Produce / refresh apartment_market_report.md using rental_market_report.md as the mandatory format template (same sections, Index, Back to Index, 4a–4e, all-state deep dives, A–Z).

Property types: conventional apartments 5+ units only. Cross-link the SFR/2–4 sibling report; do not copy its rankings blindly.

Section order: Index → National snapshot (first body) → Top 10 → matrix → city boards → deep dives → legal → insurance/tax → PM → workflow → methodology/A–Z → What changed appendix LAST. Keep headings EXACTLY `## 3. Top 10 actionable markets` and `## 4. All-state ranking matrix` (GitHub Pages overview). Keep `## 1. What changed vs the prior run` for the appendix anchor.

Live-search apartment occupancy, concessions, deliveries, cap rates, and multifamily financing. Reuse shared data/ for jobs, demographics, and income. Mark unavailable when apartment pricing is missing. No invented numbers. No tilde-as-approximately (use about / ≈).

Defaults: balanced strategy; professional multifamily management; 25–35% down screen (state 30% midpoint); haircut Cash for concessions, tax, insurance, and PM ≈5–6% of EGI unless quoted.
```

---

## Out of scope (unless asked later)
[↑ Back to Spec index](#spec-index)


- Single-family and 2–4 unit primary rankings (see sibling report)
- Short-term rental / Airbnb hotelization strategies
- Mobile-home parks, self-storage, retail, office
- Broker opinions of value for a specific address
- Legal opinions — screening notes only; confirm with counsel
- Automated apartment pipeline parity with `pipeline/build_report.py` (optional future work)
