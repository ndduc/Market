# US Rental Market Analysis Spec

## Goal
[↑ Back to Spec index](#spec-index)


Produce a comparable, evidence-based rental-investment analysis for **all 50 US states + DC**, and for each state's **major cities**, so an investor can:

1. Identify the best markets for **landlord-friendly** investing
2. Identify the best markets for **tenant-friendly** environments (still investable, but with stronger renter protections)
3. Rank markets by economics: **job market, home prices, rental cash flow, and property appreciation**
4. Understand **why** each market ranks where it does
5. Distinguish where **single-family houses** vs **multifamily homes** are the better fit

This document is both the analysis specification and the reusable AI prompt.

**Canonical report:** `rental_market_report.md` is the base format and latest full analysis. Future runs must match that report’s section order, tables, and plain-English tone. **Median and average/typical prices**, **top job industries**, and **demographics / income** (race/ethnicity mix plus **median and average** household income) must appear **in context** (companion tables in the all-state matrix, city/metro notes, deep dives, cards) — not as standalone dumps that break top-to-bottom reading.

**Apartment sibling:** Conventional **5+ unit** apartments are specified in `apartment_market_spec.md` and reported in `apartment_market_report.md`. That sibling **must reuse this report’s format** but ranks apartments only — do not merge the two Top 10 lists without re-underwriting.

**SFH appreciation sibling:** Appreciation-first **single-family** is specified in `sfh_appreciation_spec.md` and reported in `sfh_appreciation_report.md`. That sibling **must reuse this report’s format** but ranks for equity-path / price growth — do not merge the two Top 10 lists without re-underwriting.

**Canonical build method:** Do **not** maintain one-off “patch the Markdown” scripts (`_add_*.py` that string-replace sections). Every full refresh must use the **durable pipeline**:

```text
python -m pipeline.fetch_all
python -m pipeline.build_report
```

Keys live in `.env` (`CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY`). Data must be **pulled live on every run** — never treat prior `data/` files as current without re-fetching. See **Durable live-data pipeline** for the full contract.

---

## Spec index

Every section below includes **[↑ Back to Spec index](#spec-index)** under its heading.

| Section | What it’s for |
|---------|----------------|
| [Goal](#goal) | Purpose of the analysis |
| [Scope](#scope) | Geography, suburbs, property types, investor lenses |
| [Ranking dimensions](#ranking-dimensions) | Pillars, industries, demographics/income, prices, cash flow, financing, overlays |
| [Required outputs](#required-outputs) | Report format, section order, **Index requirement**, presentation rules |
| [Durable live-data pipeline](#durable-live-data-pipeline-mandatory) | Exact commands: `fetch_all` → `build_report`; keys + `data/` map |
| [Live data & web search](#live-data--web-search-requirements-mandatory) | Hard fetch/search rules and sources |
| [Analysis rules](#analysis-rules-for-the-ai) | Scoring and honesty rules |
| [Scoring rubric](#suggested-scoring-rubric-directional) | 1–10 directional guide |
| [Deliverable format](#deliverable-format) | Exact report shape to emit |
| [AI prompt](#ai-prompt-copy-paste) | Copy-paste operator prompt |
| [Optional follow-ups](#optional-follow-up-prompts) | Screens and refresh prompts |
| [Out of scope](#out-of-scope-unless-asked-later) | What this analysis does not do |

**Ranking metrics (quick):** [Industries](#required-job-industry-metrics-do-not-skip) · [Demographics & income](#required-demographics--income-metrics-do-not-skip) · [Prices](#required-price-metrics-do-not-skip) · [Entry capital & shock reserves](#required-entry-capital--shock-reserves-do-not-skip) · [Cash flow](#required-cash-flow-definition-do-not-improvise) · [Property management](#required-property-management-metrics-do-not-skip) · [Suburbs](#required-suburb-research-mandatory)

---

## Scope
[↑ Back to Spec index](#spec-index)


### Geography

[↑ Back to Spec index](#spec-index)

- **States:** all 50 states + District of Columbia
- **Cities / metros:** for each state, analyze the major **metro / city markets** that matter for rentals
  - Default: top 2–5 markets by population / metro rental inventory
  - Prefer **MSA / metro framing** when data is metro-based (e.g., Dallas–Fort Worth, not only Dallas city limits; **Phoenix metro**, not a separate national row for every East Valley city)
  - **Suburbs are usually inside the metro:** Tempe, Gilbert, Chandler, Mesa, Scottsdale → Phoenix metro; Irving / Plano → Dallas–Fort Worth; etc. Do **not** omit the primary metro name (always list Phoenix for Arizona).
  - Call out when city vs metro data diverge meaningfully
  - In the all-state matrix, keep primary metro names visible on the scores table (or an adjacent companion prices/metros table), so readers never see a state with no city context

### Required suburb research (mandatory)

[↑ Back to Spec index](#spec-index)

National rankings stay at **state / metro** level. Inside each major metro that appears in top lists or deep dives, also research **top suburbs / submarkets** with live search:

| Requirement | Detail |
|-------------|--------|
| Coverage | For every metro in the **Top 10 actionable**, **city leaderboards**, and **all-state deep dives**, name **1–3 top suburbs** (or named submarkets) worth underwriting when the metro is material |
| Split angles | Label each suburb as mainly **cash-flow**, **balanced**, or **appreciation / tenant-quality** when they diverge (e.g., Phoenix West Valley yield vs East Valley schools/prestige) |
| Prices | Prefer suburb-level median / typical price and rent or gross-yield proxy when published; otherwise mark `unavailable` and use metro proxy with a label |
| Depth | Every state’s deep dive should name **1–3 top suburbs** when major metros exist; small-scale states may note limited suburb inventory |
| Do not | Create a separate national ranking row for every suburb unless the user asks or the suburb trades as its own MSA |
| Do | Always keep the parent metro name visible (e.g., “Phoenix — Tempe / Gilbert / Chandler”) |

**Examples of correct suburb framing:**
- Arizona → Phoenix metro → East Valley: Tempe, Gilbert, Chandler, Mesa; West Valley: Buckeye, Surprise, Avondale, Glendale
- Indianapolis → Fishers, Carmel, Noblesville, Greenwood
- Kansas City → Independence (cash flow) vs Overland Park / Lee’s Summit (higher entry)
- Cleveland → Lakewood, Parma, Cleveland Heights, Maple Heights (plus city neighborhoods when relevant)
- Dallas–Fort Worth → Frisco, McKinney, Plano, Forney, Mansfield
- Houston → Katy, Cypress, Spring / Klein, Pearland

### Property type scope (in scope)

[↑ Back to Spec index](#spec-index)

Analyze **both** of these long-term residential rental asset types:

| Type | Definition for this spec |
|------|--------------------------|
| **Single-family house (SFR)** | Detached 1-unit home used as a long-term rental (prefer 3BR comps when available) |
| **Multifamily home (small MF)** | 2–4 unit residential buildings (duplex / triplex / fourplex). If data is only available for larger apartments, label it clearly and do not treat it as identical to 2–4 unit homes |

**Rules:**
- Produce rankings that work for **both** SFR and small multifamily unless a market clearly favors one.
- When SFR and MF diverge (price, yield, vacancy, regulation, insurance), say so and optionally show a split shortlist: “best for SFR” vs “best for 2–4 unit MF.”
- Prefer **like-for-like comps** (SFR price vs SFR rent; 2–4 unit price vs unit rents).
- Condos / HOA-heavy product may be noted as a risk overlay, but are **not** the primary ranking universe unless the user asks.

### Investor lenses (two parallel leaderboards)

[↑ Back to Spec index](#spec-index)

| Lens | Focus |
|------|--------|
| **Landlord-protection set** | Strong eviction process predictability, reasonable rent-control risk, favorable landlord-tenant statute balance, lower legal friction |
| **Tenant-protection set** | Stronger habitability / rent-stabilization / notice / anti-discrimination / just-cause frameworks — still evaluate investability honestly |

Markets can appear on both lists for different reasons; do not force mutual exclusivity.

### Investor profile inputs (ask or state defaults)

[↑ Back to Spec index](#spec-index)

Before final ranking, record assumptions. If the user does not specify, use these defaults and label them:

| Input | Default |
|-------|---------|
| Strategy preference | Balanced (cash flow + appreciation) |
| Property types | SFR **and** 2–4 unit multifamily |
| Capital / buy box | Mid-market investor; note if a market requires unusually high capital |
| Local vs remote | Remote-capable preferred unless stated otherwise |
| Hold period | 5–10 years |
| Risk tolerance | Moderate |

---

## Ranking dimensions
[↑ Back to Spec index](#spec-index)


Score and rank every state and major city on these four pillars (plus a composite). Use a consistent 1–10 scale per pillar unless data forces a relative rank-only approach — if so, say so explicitly.

| Pillar | What to measure | Example signals |
|--------|-----------------|-----------------|
| **1. Job market** | Employment strength and demand for housing | Unemployment, job growth, **top industries / major employers**, wage growth, population / migration inflows, industry concentration risk, **demographic / income context** (renter pool shape) |
| **2. House price** | Acquisition affordability and entry barrier | **Median and average** sale / home-value prices for the state and each major city (SFR and 2–4 unit where available), **price-to-income** (vs median / average household income), inventory, typical down-payment burden |
| **3. Rental cash flow** | Income vs carrying cost after realistic expenses | Rent-to-price, gross yield, **effective rent after concessions**, vacancy, **property tax**, **insurance**, HOA, management, repairs → rough net yield / cash-on-cash under the standard financing case |
| **4. Property appreciation** | Long-term equity path | 1y and 5–10y price appreciation, supply constraints, income/job support, oversupply risk (permits / deliveries) |

### Required job-industry metrics (do not skip)

[↑ Back to Spec index](#spec-index)

For **every state + D.C.**, and for **each major metro** in top lists / deep dives / city leaderboards, report the **top job industries** that drive local employment and renter demand.

| Metric | Definition / preference |
|--------|-------------------------|
| **Top industries (state)** | Name the **top 2–4 industries** by employment share or recent job growth (e.g., healthcare, government, manufacturing, tech, tourism, energy, logistics). Prefer Bureau of Labor Statistics / state labor department / BEA industry data. |
| **Top industries (metro)** | Name the **top 2–4 industries or employer clusters** for that metro when they differ from the state (e.g., Columbus = government + Ohio State + Intel/tech; Houston = energy + healthcare + logistics). |
| **Concentration risk** | Flag if one industry or employer dominates (single-employer / boom-bust risk). |
| **Renter demand link** | Briefly note which renter profiles those industries support (e.g., hospital workers, logistics shift workers, tech professionals, tourism seasonality). |

**Rules:**
- Use live-searched industry data when available; if only qualitative employer lists are found, label as judgment and lower confidence.
- Do not invent precise employment shares — mark `unavailable` or use directional language (“largest sectors include…”).
- Industry mix should inform Jobs scores and appreciation / vacancy narratives (e.g., tourism-heavy → seasonal vacancy risk; diversified healthcare/government → more stable demand).
- Present industries **in context**: companion column or note in the all-state matrix, metro/suburb screens, and **all-state deep dives** — not a disconnected dump section.

### Required demographics & income metrics (do not skip)

[↑ Back to Spec index](#spec-index)

For **every state + D.C.**, and for **major cities / metros** (and researched top suburbs when published), report **population composition** and **household income**.

| Metric | Definition / preference |
|--------|-------------------------|
| **Race / ethnicity mix** | Top groups by share (plain English): e.g. non-Hispanic White, Black, Hispanic/Latino (any race), Asian, and other material groups (Native American, Pacific Islander, multiracial) when ≥ ~5% or when they define the market. Prefer U.S. Census / ACS (Decennial or ACS 1-year / 5-year). State that **Hispanic/Latino is an ethnicity** (any race). |
| **Median household income** | Prefer ACS median household income; CPS ASEC / FRED state medians OK if labeled. Report for every state + D.C.; report metro medians for featured cities when available. |
| **Average (mean) household income** | Prefer ACS mean household income (e.g. S1901 / S1902 / DP03). If mean is missing after search, mark `unavailable` — do not invent. Per-capita personal income may be noted only as a **labeled proxy**, never as a substitute for household mean without saying so. |
| **Metro / suburb drill** | For deep-dive metros and top suburbs, note when race mix or income diverges from the state (e.g. city vs suburb, East Valley vs West Valley). Mark `unavailable` when suburb-level ACS is not found. |
| **Investor use** | Use income for **price-to-income** and rent-support context; use demographics as **demand / tenant-pool context** only — never as a scoring proxy for “desirability,” credit, or discrimination. |

**Rules:**
- Live-search Census / ACS (or clearly labeled CPS / state demographic reports). Do not invent percentages or dollar incomes.
- Keep race/ethnicity and income **in context** (companion **4d** table and/or deep-dive / card lines) — not a disconnected dump section.
- Prefer compact display (`$84k` medians; `NH White 54% · Hisp 31% · Black 4% · Asian 3%`).
- When Decennial (e.g. 2020) race shares and ACS income years differ, label both as-of dates.

### Required price metrics (do not skip)

[↑ Back to Spec index](#spec-index)

For **every state + D.C.** and for **each major city / metro** listed for that state, report both:

| Metric | Definition / preference |
|--------|-------------------------|
| **Median price** | Prefer median sale price when available; otherwise typical home value (e.g. Zillow typical value). Label which measure was used. |
| **Average price** | Prefer average / mean sale price when available; otherwise a clearly labeled average home-value proxy. If only median exists after searching, mark average as `unavailable` — do not invent it. |

**Rules:**
- Cover **all 50 states + D.C.** and each state’s major cities/metros named in the report.
- Prefer **single-family** prices as the primary comparable; add **2–4 unit** median/average when available (building price).
- Always state **source + as-of date** for price figures.
- Do not treat “typical value,” median sale, and average sale as interchangeable — label each measure.
- When median and average diverge a lot, note that skew (luxury / distressed tails) in deep dives or footnotes.
- Use median as the default input for yield screens unless the user asks otherwise; still **display both** median and average in the price tables.

### Required cash-flow definition (do not improvise)

[↑ Back to Spec index](#spec-index)

- **Gross yield** = (annual rent) / (purchase price). Screening metric only.
- Prefer **achieved / signed lease rent** over asking rent when available. If only asking rent indexes are available, say so.
- For single-family, prefer **3-bedroom** rent comps when available.
- For multifamily homes, use **total unit rent** vs **building price** when available; otherwise label the proxy.
- Prefer **median price** (labeled) as the purchase-price input for yield screens; note if average is used instead.
- **Net / realistic cash-flow score** must haircut for: vacancy, management, maintenance, property tax, insurance, and concessions.
- Never present gross yield as if it were cash-on-cash.

### Standard financing scenario (default, for comparability)

[↑ Back to Spec index](#spec-index)

Use unless the user overrides. State all assumptions in Methodology:

| Assumption | Default |
|------------|---------|
| Down payment | **25%** (investor / non-owner-occupied default). Note if a market commonly requires **20%**, **25%**, or **30%+**. |
| Loan type | Investor / DSCR-style financing |
| Interest rate | Current prevailing investor rate band from live search (cite source); if unavailable, state `unavailable` and avoid fake precision |
| Closing / acquisition costs | Screen **~2–4%** of purchase (title, lender fees, inspections, initial reserves at closing). Use **3%** midpoint unless local data says otherwise. |
| Vacancy | 5–8% (higher if concessions / soft rent market) |
| Operating expense ratio (ex-debt) | ~35–50% of gross rent depending on market; raise for high-tax / high-insurance / older-stock markets |
| Stress tests (required for top markets) | Rate +1%, rent −5%, insurance +50%, and **6 months** of nonpayment / vacancy |

### Required entry capital & shock reserves (do not skip)

[↑ Back to Spec index](#spec-index)

For **every state + D.C.**, and for **major cities / metros** (and researched top suburbs when a price is available), report how much **liquid cash** an investor should plan for.

| Metric | Definition / preference |
|--------|-------------------------|
| **Down payment %** | Default **25%** of buy-box price (median preferred). Call out if local lending practice differs. |
| **Cash to close (entry liquid)** | Down payment + closing/acquisition costs screen (**~3%** of price unless better local figure). Compact: `≈28% × median`. |
| **Recommended shock liquid** | Cash **after closing** to absorb vacancy, repairs, insurance spikes, and rate stress — default **6 months** of estimated PITI (principal & interest + property tax + insurance) under the standard financing case. Raise toward **9–12 months** in high-insurance, high-tax, soft-rent, or thin-liquidity markets. |
| **Total recommended liquid** | **Cash to close + shock liquid** (what a prudent investor should have available before bidding). |
| **Metro / suburb** | Recompute on that geography’s median / typical / screen price when it differs materially from the state (e.g., Phoenix West Valley vs Gilbert). |

**Screening formulas (state in Methodology; label as screens, not quotes):**
1. `Cash_to_close ≈ Price × (Down% + Closing%)` with defaults `0.25 + 0.03 = 0.28`
2. `Loan = Price × (1 − Down%)`
3. `Monthly_PI ≈` amortizing payment on Loan at the live investor rate midpoint (or **7.5%** if using the July 2026 ~7.0%–8.5% band)
4. `Monthly_PITI ≈ Monthly_PI + (effective_tax_rate × Price)/12 + (annual_insurance)/12`
5. `Shock_liquid ≈ Months × Monthly_PITI` (default Months = **6**; **9** if catastrophe/tax/soft-rent overlay is severe)
6. `Total_recommended_liquid ≈ Cash_to_close + Shock_liquid`

**Rules:**
- Prefer **median** purchase price for the screen; show metro/suburb variants when prices diverge.
- Round to nearest **$1k** for readability (`~$74k` cash to close).
- Do not invent lender quotes — these are **capital screens**, not loan commitments.
- Present **in context**: companion **4e** table and/or **Entry capital:** lines in every deep dive (and metro/suburb notes when useful).
- Insurance and tax overlays must feed the shock months / monthly PITI haircut (Florida insurance ≠ Ohio insurance).

### Composite ranking

[↑ Back to Spec index](#spec-index)

- Default equal weights: Job 25% / Price 25% / Cash flow 25% / Appreciation 25%
- Also report a **landlord-protection-adjusted** and **tenant-protection-adjusted** score by blending legal environment as a fifth factor (20% legal / 20% each economic pillar, or show both raw and adjusted)
- State clearly if weights are changed

### Tie-breakers (when composites are equal)

[↑ Back to Spec index](#spec-index)

Apply in order:
1. Metro depth / liquidity (management availability, resale buyer pool, inventory depth)
2. Data confidence (High > Medium > Low)
3. Lower catastrophe / insurance risk
4. Stronger remote-operability
5. Diversified job base over single-employer dependence

### City vs state scoring rule

[↑ Back to Spec index](#spec-index)

- Score the **state** on statewide economics + statewide baseline law.
- Score **cities/metros** separately when local ordinances, rents, prices, or insurance differ materially.
- If a city is much more tenant-protective than its state (e.g., Chicago vs Illinois; NYC vs upstate NY), the city legal score overrides the state score for that city’s ranking.
- Do not let one outlier city alone define the whole state score without calling out the split.

### Legal / protection layer (separate score, 1–10)

[↑ Back to Spec index](#spec-index)

For each state (and city where local rules differ, e.g., NYC, SF, LA, Seattle, Chicago):
- Landlord favorability (eviction timeline, rent control risk, security deposit rules, repair liability tilt)
- Tenant favorability (just-cause, rent caps, longer notice, stronger remedies)
- Landlord licensing / registration / inspection / rental certificate regimes
- Cite statute themes and notable local ordinances; flag uncertainty

### Additional required risk overlays (score haircuts or explicit risk bullets)

[↑ Back to Spec index](#spec-index)

These are mandatory in analysis even if not separate 1–10 pillars:

| Overlay | Why it matters |
|---------|----------------|
| **Insurance / catastrophe risk** | Hurricane, flood, wind, hail, wildfire can erase headline yield |
| **Property tax drag** | High effective tax rates reduce NOI and cash-on-cash |
| **New supply / vacancy / concessions** | Oversupply markets can look “cheap” while rents stagnate |
| **Liquidity / exit risk** | Days on market, sale-to-list, thin buyer pools |
| **Remote-operability / PM availability** | Critical for out-of-state investors |
| **Ops intensity** | Ultra-high-yield cities may imply crime, condition, turnover, or collection risk — say so |

### Required property-management metrics (do not skip)

[↑ Back to Spec index](#spec-index)

Every full refresh must include a **Property management rates & remote ops** section in the report (after insurance/tax overlays; before acquisition workflow). Live-search current fee benchmarks and notable operators; cite URLs and as-of dates. Do not invent company fee schedules.

| Field | Requirement |
|-------|-------------|
| **Monthly management fee** | National typical range for **long-term residential** (single-family and 2–4 unit): usually **8–12% of collected rent**; note published national averages when available (e.g. about **8.5%** survey averages). Flat-fee alternatives (often about **$80–$150+/unit/mo**) when common. |
| **Leasing / tenant placement** | Typical **50–100% of one month’s rent** (or flat $500–$1,500); note average about **70%** of one month’s rent when sourced. |
| **Other common fees** | Setup / onboarding, lease renewal, inspections, eviction coordination, and **maintenance markups** (often about **5–15%** of vendor invoices) — list as a fee stack, not only the headline %. |
| **All-in cost screen** | State that first-year / fully loaded PM cost often lands about **15–20%+ of gross rent** once placement + add-ons are included — use this haircut in cash-flow scoring. |
| **Property-type note** | Single-family often prices at the **higher** end of the % range; small multifamily (2–4) similar or slightly lower; large multifamily / institutional often **lower %** or flat per door. Short-term / vacation management is a **different** business (often **20–35%+**) — keep out of LTR screens unless labeled. |
| **Regional direction** | Note when high-rent coasts quote **lower %** and lower-rent Midwest/Southeast quote **higher %** to cover fixed labor. Flag thin-PM metros as remote-ops risk. |
| **Notable operators (landscape, not endorsement)** | List **third-party** residential managers / marketplaces useful to remote investors (e.g. large multifamily managers like Greystar / Avenue5 for scale context; SFR third-party specialists / marketplaces such as Evernest, All Property Management directories) **and** separate **institutional SFR landlords** (Invitation Homes, Progress Residential, American Homes 4 Rent, etc.) that are **not** typically available as mom-and-pop third-party PMs. Always label: scale ≠ quote for a one-off duplex. |
| **Underwriting default** | Unless the user supplies a live PM quote, cash-flow screens should assume **about 10% of gross rent** for ongoing management **plus** a leasing-fee allowance on turnover (or fold leasing into higher effective expense). State the assumption in Methodology. |

---

## Required outputs
[↑ Back to Spec index](#spec-index)


### Canonical report format (mandatory)
[↑ Back to Spec index](#spec-index)


**Base format file:** `rental_market_report.md` in this workspace.

Every full analysis **must match that report’s structure, tone, and section order**. Do not invent a different outline. Treat `rental_market_report.md` as the template; update scores and evidence with live data, but keep the same numbered sections and table styles.

#### Required section order
1. **Header** — title, analysis date, coverage, property types, live-research confirmation, disclaimer
2. **Index (table of contents)** — clickable jump links to every major section, plus shortcuts to **4a–4e**, deep dives, city boards, and the **A–Z state rank index**. **Every indexed heading** must include **[↑ Back to Index](#index)** directly underneath. Required because the report is long and multi-table.
3. **What changed vs the prior run** — short table of score / ranking / data updates (required whenever a prior report exists)
4. **National market snapshot** — live national bullets + yield definition + core conclusion + single-family vs 2–4 unit takeaway
5. **Top 10 actionable markets** — ranked table with why / property-type fit / main caution  
   then **Best landlord-protection markets**  
   then **Best tenant-protection markets that still have an investment case**  
   then **Markets to avoid / watch**
6. **All-state ranking matrix** — use **companion tables in the same section** (not one mega-table):  
   - **4a Scores:** # / State (primary metros) / Jobs / Price / Cash / Appr. / Econ / Owner / Tenant / Conf.  
   - **4b Prices & metros:** # / State / Median / Typical / Major metros (same `#` order; compact $263k-style display is OK)  
   - **4c Top industries (optional companion, or fold into deep dives + cards if space-constrained):** # / State / Top industries (2–4) / Concentration note  
   - **4d Demographics & income:** # / State / Race–ethnicity mix / Median HH income / Mean HH income  
   - **4e Entry capital (optional companion):** # / State / Down % / Cash to close / Shock liquid (6–9 mo) / Total recommended liquid — same `#` order; based on median price × financing defaults  
   plus composite buckets and score-change notes. Do not merge scores + dollars + long metro lists + long industry + demographic + capital strings into a single wide table.
7. **City leaderboards** — cash-flow screen (include metro median / screen price column); best for single-family; best for 2–4 unit; appreciation leaders; job-market leaders; best balanced city shortlist; **top suburbs screen**; and for featured metros, **top job industries / employer clusters**, **race–ethnicity notes**, and **median / mean income** when available
8. **All-state deep dives** — fuller writeups for **every state + D.C.** in actionable-rank order (scores, **Prices:**, **Entry capital:**, **Top industries:**, **Demographics / income:**, **Top suburbs:** when researched, narrative, best fit, risks, confidence). Do **not** use remaining-state bullet cards as a substitute.
9. **Legal environment — verified highlights** — dated rent-cap / just-cause / city-override notes with links
10. **Insurance and property-tax overlays** — directional high/low drag and catastrophe haircuts
11. **Property management rates & remote ops** — fee stack (management %, leasing, add-ons), all-in cost screen, notable third-party vs institutional operators (live-searched; not an endorsement)
12. **Practical acquisition workflow** — numbered steps from strategy → address underwriting (include get PM fee schedule in writing)
13. **Methodology and sources** — live-research confirmation, financing assumptions, **PM fee defaults**, price-measure definitions, demographics/income definitions, primary links, caveats, **navigable A–Z actionable-rank index** (link every state to its §6 deep dive)

**Navigation rules:**
- Keep a top **Index** with Markdown anchor links (works in GitHub / most Markdown previews), including shortcuts to **all** deep-dive state headings (or A–Z → deep dive).
- Keep an end **A–Z rank index** that links **every** state abbreviation to its deep-dive heading.
- **Every indexed section / subsection** (including each deep-dive state and 4a–4e) must show **[↑ Back to Index](#index)** directly under its heading.
- Within dense sections (§4, §5, §6), prefer short “jump” lines or Index shortcuts rather than duplicating full tables.

**Flow rule:** Do **not** create separate standalone “Price levels”, “Demographics dump”, or “Income dump” sections that isolate every geography. Keep prices, industries, and demographics/income as **companion tables** (same rank order) plus city/deep-dive inline notes, so the report still reads top-to-bottom.

#### Writing / language rules for the report
- Prefer **plain English**; spell out agency and index names on first use.
- Avoid stacking abbreviations (do not fill the report with BLS / FHFA / ZORI / DSCR / NOI / etc.). Use everyday labels in tables: Jobs, Price score, Cash flow, Appreciation, Owner law, Tenant law, Median $, Typical $.
- Say **single-family** and **2–4 unit** / duplex–fourplex in reader-facing text; reserve short forms for methodology notes if needed.
- Keep the same concise, comparative tone as `rental_market_report.md`.

### Content that must appear (mapped to the format above)

[↑ Back to Spec index](#spec-index)

- Top 10 **actionable** markets (state + preferred metros), noting single-family vs 2–4 unit fit
- Top 10 **landlord-protection** markets (law + economics)
- Top 10 **tenant-protection** markets that still have a coherent investment thesis
- Markets to avoid / watch (jobs, price, cash flow, legal friction, or insurance-broken economics)
- Full all-state matrix **including median and typical prices** + **top industries** + **demographics / median & mean income** + city leaderboards (with metro median / screen price, suburbs, industry, and demographic/income notes where available)
- **Index / TOC** at the top and a **navigable A–Z rank index** at the end (**every** state links to its §6 deep dive)
- **Deep dives for every state + D.C.** (with Prices, **Entry capital**, Top industries, Demographics / income, Top suburbs when researched) — no remaining-state bullet cards
- **Entry capital screens** for every state (down %, cash to close, shock liquid, total recommended liquid) + metro/suburb variants when prices diverge
- **Property management rates & remote ops** — fee stack + notable third-party vs institutional operators (live-searched)
- Insurance / property-tax overlays and legal highlights with citations
- Methodology: live search confirmation, financing defaults, yield definition, price-measure definitions, industry sources, demographics/income sources, **PM fee sources**, sources, data gaps, disclaimer

### How to present median and average prices (integrated, not isolated)

[↑ Back to Spec index](#spec-index)

| Where | What to show |
|-------|----------------|
| **All-state matrix** | Companion tables: **4a–4e** (scores, prices, industries, demographics/income, **entry capital**) — fold companions into deep dives only if space-constrained. Avoid one ultra-wide table. |
| **City leaderboards** | Metro median / screen price column on cash-flow; **Top suburbs** table/bullets; **top industries**; **income / race** notes for featured metros |
| **Deep dives** | **Every state + D.C.**: **Prices:**; **Entry capital:**; **Top industries:**; **Demographics / income:**; **Top suburbs:** when researched |
| **Methodology** | Define measures, sources, as-of dates, **financing + entry-capital formulas**; mark `unavailable` rather than inventing |

### How to present demographics and income (integrated, not isolated)

[↑ Back to Spec index](#spec-index)

| Where | What to show |
|-------|----------------|
| **4d companion table** | Same `#` order as 4a: top race–ethnicity groups + **median** HH income + **mean** HH income (or `unavailable`) |
| **Metros / suburbs** | Note divergences (city vs suburb; Hispanic-heavy vs majority-White suburbs, etc.) when live data exists |
| **Price-to-income** | Prefer median home price ÷ median HH income in narrative; do not invent mean income to force a ratio |
| **Deep dives (all states)** | Repeat **Demographics / income:** on every state writeup; note metro divergences |
| **Ethics** | Demographics inform tenant-pool / demand context only — never a ranking criterion for exclusion or “target race” investing |

- Prefer **single-family** as the primary comparable; add 2–4 unit when available.
- Prefer **median** for yield screens; still display typical/average alongside.
- Never invent missing metro averages — label `unavailable`.

### Per-state content depth

[↑ Back to Spec index](#spec-index)

**Every state + D.C. (deep dive — mandatory):**
1. Snapshot scores: Jobs / Price / Cash flow / Appreciation / Owner law / Tenant law
2. **Prices:** median and typical for the state + major-city medians covered (cite source/as-of; note single-family vs 2–4 unit)
3. **Entry capital:** down %; cash to close on median (and key metros/suburbs when prices differ); recommended shock liquid (6–9 months PITI); total recommended liquid
4. **Top industries:** 2–4 leading sectors / employer clusters for the state and key metros; flag concentration risk
5. **Demographics / income:** top race–ethnicity shares + **median and mean** household income (state; metro when available); note city/suburb divergences
6. **Top suburbs:** 1–3 named suburbs / submarkets when the state has major metros in top lists or meaningful rental screens; otherwise note `unavailable` / limited scale — include suburb entry-capital note when suburb prices differ a lot
7. Why it ranks (jobs, industries, prices, rents, income support, appreciation, law, insurance/tax, supply, capital burden)
8. Best fit (single-family vs 2–4 unit; investor style; which suburb angle; capital tier)
9. Key risks (include industry concentration / boom-bust and under-reserved shock risk when relevant)
10. Data confidence: High / Medium / Low  
   High only if live-cited figures exist for price (at least median), rent/yield proxy, jobs, and legal direction

**Length guidance:** Top actionable states may run longer; lower-ranked states stay shorter but **must** keep the same field labels (Scores / Prices / Entry capital / Top industries / Demographics / income / Best fit / Risks / Confidence). Do **not** collapse any state into a one-line “remaining card.”

### Deliverable file requirements

[↑ Back to Spec index](#spec-index)

- **Canonical / latest base report:** keep or refresh `rental_market_report.md` so it always reflects the current preferred format and latest full analysis
- **Dated archive (optional on each re-run):** also save `rental_market_report_YYYY-MM-DD.md` when useful for history
- **Pipeline artifacts (mandatory on each full refresh):** overwrite live-fetched files under `data/` and regenerate report tables via `pipeline/` (see **Durable live-data pipeline** below)
- Include analysis date in the header
- Always include **What changed vs the prior run** when a prior report exists
- Suggested refresh cadence: after major jobs / house-price / rent / legal releases, or at least quarterly — **each refresh still re-fetches live data**

---

## Durable live-data pipeline (mandatory)
[↑ Back to Spec index](#spec-index)


Hand-editing giant Markdown tables and disposable `_add_industries.py` / `_add_demographics.py` patch scripts are **out of process**. They are slow, error-prone (section-boundary bugs), and encourage stale numbers.

### Exact refresh commands (run these)

[↑ Back to Spec index](#spec-index)

From the repo root (`Market/`):

```powershell
# 1) Secrets — copy once, never commit
copy .env.example .env
# Edit .env and set:
#   CENSUS_API_KEY=...
#   FRED_API_KEY=...
#   BLS_API_KEY=...
#   BEA_API_KEY=...

# 2) Live fetch (ALWAYS re-pull; overwrites data/*.json)
python -m pipeline.fetch_all

# 3) Build report from data/ (companion tables + deep-dive fields + capital/narratives)
python -m pipeline.build_report
```

That is the **minimum full tabular refresh**. `build_report` already calls `pipeline.update_from_data` at the end.

Optional explicit re-propagation without re-fetching (only if `data/` is already fresh from this session):

```powershell
python -m pipeline.update_from_data
```

Do **not** invent new disposable `_add_*.py` / `_fix_*.py` patchers for routine refreshes. Extend `pipeline/fetch_all.py`, `pipeline/build_report.py`, or `pipeline/update_from_data.py` instead.

### Required architecture

[↑ Back to Spec index](#spec-index)

Every full analysis / refresh **must** follow this order:

```text
1) LIVE FETCH   → python -m pipeline.fetch_all  (APIs + no-key downloads)
2) WRITE data/  → overwrite JSON snapshots (as-of + source URLs in meta/sources)
3) BUILD        → python -m pipeline.build_report
                  (4b–4e, deep-dive Prices/Entry capital/Industries/Demographics,
                   unemployment/appreciation leads, §1/§2 live bullets)
4) NARRATIVE    → judgment-only sections if evidence moved enough to change ranks
                  (4a score numbers, top 10, legal, avoid list, city boards)
5) REPORT       → rental_market_report.md is the canonical output
```

### Pipeline modules (current contract)

[↑ Back to Spec index](#spec-index)

| Path | Role | Operator action |
|------|------|-----------------|
| `.env` (gitignored) | API keys; load via `pipeline/config.py` | Maintain locally; never commit |
| `.env.example` | Key names only | Safe to commit |
| `pipeline/config.py` | Paths, URLs, series IDs, FIPS, env var names | Edit when adding sources |
| `pipeline/fetch_all.py` | Live pullers → overwrite `data/` | `python -m pipeline.fetch_all` |
| `pipeline/build_report.py` | Rebuild §4b–4d (+ industries/demos) then call update_from_data | `python -m pipeline.build_report` |
| `pipeline/update_from_data.py` | Deep-dive Prices / Entry capital / §4e; LAUS+FHFA narrative leads; §1/§2 bullets | Invoked by build_report; or run alone |
| `pipeline/add_entry_capital.py` | **Legacy** capital injector — superseded by `update_from_data` | Do not use for routine refresh |
| `rental_market_report.md` | Canonical human report | Output of build |
| `rental_market_spec.md` | This process contract | Follow on every refresh |

### API keys vs no-key sources

[↑ Back to Spec index](#spec-index)

| Env var | Source | What it feeds |
|---------|--------|----------------|
| `CENSUS_API_KEY` | Census ACS 1-year + subject S1901 | Race shares, ACS median alt, **mean HH income** → `demographics.json`, `income.json` |
| `FRED_API_KEY` | FRED series `MEHOINUS*A646N` | CPS median HH income (preferred) → `income.json` |
| `BLS_API_KEY` | BLS API v2 | LAUS unemployment → `jobs.json`; CES SAE industries → `industries.json` |
| `BEA_API_KEY` | BEA Regional SAINC1 | Per-capita + total personal income → `bea.json` |
| *(none)* | FHFA HPI purchase-only TXT | State YoY appreciation → `fhfa.json` → §4b FHFA YoY |
| *(none)* | Redfin public state market tracker (gzip TSV) | State median / list prices → `state_prices.json` → §4b + deep-dive Prices/Entry capital |

Still **manual / web search** each refresh until automated: metro price drill-downs beyond preserved screens, suburb qualitative notes, landlord–tenant law, tax/insurance overlays, rents/concessions, and **4a score number changes**.

### `data/` files written every fetch

[↑ Back to Spec index](#spec-index)

| File | Contents |
|------|----------|
| `data/meta.json` | Run timestamp; `*_api_key_present`; per-source ok / n_states / notes |
| `data/sources.json` | Canonical URLs + status mirror |
| `data/income.json` | Median HH income (FRED CPS preferred; ACS fallback) + mean (ACS S1901) |
| `data/demographics.json` | Race/ethnicity shares (ACS) |
| `data/bea.json` | BEA per-capita / total personal income |
| `data/jobs.json` | BLS LAUS unemployment rates |
| `data/industries.json` | BLS CES top supersectors by share |
| `data/fhfa.json` | FHFA PO HPI index + YoY % |
| `data/state_prices.json` | Redfin All Residential median (+ list as typical when present) |
| `data/metro_prices.json` | Placeholder until metro tracker wired (`fetch_ok: false`) |
| `data/suburbs.json` | Placeholder until structured suburb research wired |

### What `build_report` / `update_from_data` auto-refresh

[↑ Back to Spec index](#spec-index)

| Report section | Auto-updated from `data/`? |
|----------------|----------------------------|
| §4b Prices (+ FHFA YoY) | Yes — Redfin + FHFA |
| §4c Industries | Yes — BLS CES |
| §4d Demographics & income | Yes — Census + FRED |
| §4e Entry capital | Yes — Redfin medians + financing screen (25% / ~3% / 7.5% / 6–9 mo PITI) |
| §6 deep-dive **Prices:** / **Entry capital:** / **Top industries:** / **Demographics / income:** | Yes |
| §6 narrative unemployment / FHFA appreciation leads (patterned sentences) | Yes when patterns match |
| §1 What changed + §2 national snapshot live bullets | Partially yes |
| §4a **score numbers** (Jobs / Price / Cash / Appr / …) | **No** — analyst/AI judgment after reviewing new data |
| Top 10 / avoid / city boards / legal / insurance narrative | **No** — judgment + web search |

**Builder safety:** refuse to wipe §4d if fewer than ~40 medians; skip §4b/§4c rebuilds if those `data/` files are empty/failed. Prefer aborting a section over all-`unavailable` overwrite.

**Markdown rule:** never use `~` for “approximately” in the report (single/double tildes render as strikethrough). Use `about` or `≈`.

### Live pull every time (hard rule)

[↑ Back to Spec index](#spec-index)

1. **Re-fetch on every full run.** Do not skip network pulls because `data/*.json` already exists.
2. **Overwrite `data/`** with this run’s results. Prior files are previous-run artifacts only.
3. **Do not use cached `data/` as “current”** without a successful re-fetch for that dataset.
4. If a source **fails** mid-run: mark fields `unavailable` (or label a prior snapshot **STALE** with its old as-of date **only** if the user explicitly allows stale fallback). Default = **no silent stale reuse**.
5. **Builder safety:** do **not** overwrite companion tables when `data/` for that table is empty or clearly failed (e.g. fewer than ~40 state medians) — abort the build for that section so a bad scrape cannot wipe the report to all-`unavailable`.
6. Training memory and yesterday’s report numbers are **not** acceptable substitutes for a live pull.
7. Web search / browse remains required for legal, insurance, suburb qualitative notes, and any series the scripts cannot automate — but **tabular national fields** should prefer scripted live fetch into `data/` when possible.

### What the builder may and may not do

[↑ Back to Spec index](#spec-index)

| Allowed | Forbidden |
|---------|-----------|
| Render 4b–4e + structured deep-dive fields from `data/` | String-replace random sections with one-off `_add_*.py` / `_fix_*.py` scripts |
| Leave 4a score numbers / top-10 / legal to analyst/AI after data lands | Invent income, race %, prices, or industry ranks in the builder |
| Mark `unavailable` when fetch fails | Pretend a cached file is a fresh live pull |
| Abort build for a table when fetch clearly failed / empty | Overwrite a good table with all-`unavailable` rows |
| Keep durable, versioned `pipeline/*.py` and improve them over time | Delete fetch/build scripts after each chat turn |

### AI / operator checklist on each refresh

[↑ Back to Spec index](#spec-index)

1. Confirm `.env` has `CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY` (and network).
2. Run `python -m pipeline.fetch_all`.
3. Open `data/meta.json` — confirm fresh `analysis_run_at` and which sources have `"ok": true`.
4. Run `python -m pipeline.build_report` (includes `update_from_data`).
5. Spot-check: §4b Ohio median matches `data/state_prices.json`; §4d means present; one deep dive Prices/Entry capital; no `~~` / stray `~` strikethroughs.
6. **Only if** rankings should move: revise §4a scores, top 10, avoid list, legal — with cites. Otherwise leave judgment sections and note “tabular refresh only.”
7. In Methodology: pipeline live-fetch stamp must show all four `*_api_key_present` flags from this run.

### Efficiency intent

[↑ Back to Spec index](#spec-index)

Keeping and improving the **same** `pipeline/` scripts is the speed win. Do **not** accumulate disposable patch scripts. Expand fetch coverage over time (metro Redfin tracker, HUD FMR, tax/insurance tables) without changing the report outline.

---

## Live data & web search requirements (mandatory)
[↑ Back to Spec index](#spec-index)


Any AI running this analysis **must actively pull current public data via web search / browsing and/or the durable pipeline fetchers**. Training memory alone is not acceptable as the primary source. **Every full refresh re-fetches** — see **Live pull every time** above.

### Hard requirements

[↑ Back to Spec index](#spec-index)

1. **Turn on and use web search / browse tools and/or `pipeline/fetch_*.py` before scoring.** Do not produce national rankings from remembered knowledge only.
2. **Pull fresh figures on this run** for jobs, home prices (**median and average** where available), **demographics (race/ethnicity)**, **median and average household income**, rents, appreciation, insurance/tax context, supply/vacancy, and legal notes. Prefer data from the last **12–24 months** (longer windows OK for appreciation trends and Decennial race baselines).
3. **Write fetch results into `data/`** (overwrite) before treating tabular fields as final in the report.
4. **Cite sources with links** (or exact publication names + dates) for key numbers used in rankings and city tables.
5. **Record the analysis date** and the approximate “as of” date of each major dataset in the report **and** in `data/meta.json`.
6. **If web search / browsing / fetch is unavailable**, stop and say so — do not silently fall back to outdated memory or unlabeled cache for a full national ranking.
7. **If a search/fetch fails or data is missing** for a market, mark that field as `unavailable`, lower data confidence, and continue — do not invent precise numbers.
8. **Cross-check** important claims across at least two independent source types when possible (e.g., BLS + local workforce report; Zillow/Redfin + Census ACS).

### Minimum source types to query

[↑ Back to Spec index](#spec-index)

Search and pull from as many of these as available (use current equivalents if product names change):

| Topic | Example sources to search |
|-------|---------------------------|
| Jobs / unemployment / wages / **industries** | BLS (including industry employment / QCEW or CES industry tables), BEA, Census, state labor departments, major metro economic / chamber reports, largest-employer lists |
| Home prices / inventory / liquidity | Zillow, Redfin, NAR, FHFA, local MLS summaries — pull **median and average** sale / home-value prices by state and metro when published; days on market, sale-to-list |
| **Demographics (race / ethnicity) & household income** | U.S. Census Decennial / ACS (DP05, B02001, B03003, B19013, S1901/S1902), Census ACS income briefs, CPS ASEC / FRED state median income tables, state demographic reports; metro ACS for featured cities; suburb ACS / QuickFacts when available |
| Rents / vacancy / concessions | Zillow Observed Rent Index, Apartment List, HUD, Census ACS, concession-rate reports |
| Appreciation | FHFA HPI, Case-Shiller (where available), Zillow/Redfin YoY and multi-year |
| Migration / population | Census, IRS migration, state demographic reports |
| New supply | Building permits, multifamily completions / deliveries, local pipeline reports |
| Property tax | Effective property tax rate by state/county; assessor or tax-burden summaries |
| Insurance / catastrophe | Landlord insurance cost reports, carrier exits, hurricane/flood/hail/wildfire risk summaries |
| Landlord / tenant law | State statutes, AG/housing agency pages, city ordinance pages, rent-control / just-cause / licensing news |
| Property management / remote ops | PM availability, **management % + leasing fees + add-on stack**, third-party vs institutional SFR operators, licensing friction for out-of-state owners |

### Metrics required before High confidence

[↑ Back to Spec index](#spec-index)

A market should not be labeled **High** confidence unless live-cited values (or clearly labeled proxies) exist for most of:
- Price level (**median required**; average preferred — mark `unavailable` if missing after search)
- Rent or yield proxy
- Job / unemployment signal
- **Top industries** (at least directional, with source or labeled judgment)
- **Median household income** (mean preferred; mark `unavailable` if missing)
- Legal direction (landlord vs tenant)
- At least a qualitative read on insurance/tax or an explicit `unavailable`

### Search / fetch workflow (required)

[↑ Back to Spec index](#spec-index)

1. **Run live fetchers first** (overwrite `data/`), then broad national web queries for anything not yet automated (state unemployment, **top industries by state**, **median and average** home values / sale prices, **race/ethnicity by state**, **median and mean household income by state**, rent indexes, landlord-tenant law, insurance/tax burden overviews).
2. Then run targeted queries for each state’s major metros (**median and average** single-family and 2–4 unit prices where available, rents, job growth, **metro industry / employer mix**, **metro demographics / income**, vacancy/concessions) **and top suburbs / submarkets** (cash-flow vs appreciation angles; suburb income/race when published). Write results into `data/` where structured.
3. For legal outliers (New York City, San Francisco, Los Angeles, Seattle, Chicago, etc.), run city-specific ordinance / rent-control / licensing searches.
4. For catastrophe-exposed regions (Florida, Louisiana, Texas Gulf, Oklahoma/Kansas hail belt, California wildfire zones), run insurance-cost / insurability searches and apply cash-flow haircuts.
5. **Build companion tables from `data/`**, then set scores **only after** collecting data; revise scores if later searches contradict earlier assumptions.
6. In the methodology appendix, list: tools used (pipeline fetch + web search/browse), confirmation that data was **re-fetched this run**, query themes, primary URLs, property-type scope, financing assumptions, **price-measure definitions (median vs average)**, industry sources, **demographics/income sources**, suburb sources, and data gaps.

---

## Analysis rules for the AI
[↑ Back to Spec index](#spec-index)


1. **Live data first — every run.** Re-fetch via pipeline and/or web search before ranking; never fabricate statistics or statute details; never treat prior `data/` as current without re-fetch.
2. **Pipeline over patch scripts.** Use durable `pipeline/fetch_*.py` + `pipeline/build_report.py`; do not create disposable `_add_*.py` Markdown patchers.
3. **Be comparative.** Absolute numbers matter less than relative ranking across states/cities.
4. **Separate facts from judgment.** Label opinions as judgment; every scored pillar should rest on searched/fetched data or an explicit estimate labeled as such.
5. **Do not invent precise statutes or numbers.** If unsure after searching, say “verify locally” and give the directional read.
6. **City overrides state.** Note when a city is much more tenant-protective than its state (e.g., California cities, NYC, Chicago).
7. **Cash flow honesty.** High prices + moderate rents = weak cash flow — say so even for “hot” markets. Gross yield ≠ net yield.
8. **Insurance honesty.** Do not rank Florida / Gulf / high-catastrophe markets as strong cash-flow markets without an insurance haircut or explicit warning.
9. **Jobs drive demand.** Weak job/migration story should cap appreciation and occupancy optimism. **Industry mix matters** — flag tourism seasonality, energy boom-bust, single-employer dependence, or diversified healthcare/government anchors.
10. **Supply can break rents.** High deliveries + high concessions should lower cash-flow and near-term appreciation scores.
11. **Two leaderboards, one dataset.** Reuse the same economic scores; only the legal lens and narrative change.
12. **Property-type clarity.** Always state whether a recommendation is for SFR, 2–4 unit multifamily, or both.
13. **Prefer recent data** (last 12–24 months for rents/prices/jobs; longer window for appreciation trends).
14. **Coverage completeness.** Do not skip small states; they can still rank well on cash flow or landlord law.
15. **Ultra-high yield skepticism.** Markets with extreme printed yields need ops/condition/crime/liquidity caveats.
16. **Actionable close.** End with how to use the rankings (screen → shortlist → local due diligence → address-level underwriting).
17. **Price completeness in context.** Every state + D.C. needs **median and typical/average** in the ranking matrix; major cities need median/screen prices in city tables or deep dives (or `unavailable` after search). Do not isolate prices in a separate dump section.
18. **Suburb completeness.** Top metros need **1–3 researched top suburbs** with live-cited notes; label cash-flow vs appreciation angles; keep the parent metro name.
19. **Industry completeness.** Every state + D.C. needs **top 2–4 job industries**; major metros in deep dives / city boards need metro industry notes when they differ from the state.
20. **Demographics & income completeness.** Every state + D.C. needs **top race/ethnicity shares** plus **median and mean household income** (mean may be `unavailable` after search). Featured metros/suburbs need notes when they diverge from the state. Use demographics for demand context only — never as an exclusion ranking criterion.
22. **Entry-capital completeness.** Every state + D.C. needs **down %**, **cash to close**, **shock liquid**, and **total recommended liquid** screens (metro/suburb when prices diverge). Label as screens under the standard financing case.

---

## Suggested scoring rubric (directional)
[↑ Back to Spec index](#spec-index)


Use as a starting framework; adjust with real data and document changes.

| Score | Job market | House price (investor entry) | Cash flow (after tax/insurance realism) | Appreciation | Landlord legal |
|------:|------------|------------------------------|------------------------------------------|---------------|----------------|
| 9–10 | Strong growth, **diverse** employers / industries | Relatively affordable vs income/rents | Attractive net yields after expenses | Clear multi-year upside + demand | Predictable, landlord-leaning |
| 7–8 | Solid / stable growth; clear industry anchors | Moderate entry cost | Acceptable net yields | Moderate upside | Balanced, manageable |
| 5–6 | Mixed / slow; some concentration risk | Stretch affordability | Thin / break-even after expenses | Uncertain / flat | Mixed; local traps |
| 3–4 | Weak / **highly concentrated** industry risk | Expensive | Likely negative without aggressive leverage | Soft or volatile | Tenant-leaning friction |
| 1–2 | Declining | Very expensive / poor rent support | Structurally poor or insurance-broken | Declining thesis | High rent-control / eviction risk |

---

## Deliverable format
[↑ Back to Spec index](#spec-index)


**Match `rental_market_report.md` exactly** for structure, section numbering, table style, and plain-English tone.

Respond in Markdown **and**:
1. **Live-fetch** all tabular datasets (overwrite `data/`) — do not skip because files already exist
2. **Build** companion tables / structured fields via `pipeline/build_report.py` (or equivalent durable builder)
3. Refresh / overwrite `rental_market_report.md` as the latest base report (same format)
4. Optionally also save a dated archive: `rental_market_report_YYYY-MM-DD.md`

Required shape (do not reorder):
1. Header + disclaimer
2. **Index** (clickable TOC + shortcuts to 4a–4d, deep dives, city boards, A–Z)
3. What changed vs prior run
4. National market snapshot (yield definition + core conclusion + single-family vs 2–4 unit)
5. Top 10 actionable → landlord-protection → tenant-protection → avoid/watch
6. All-state ranking matrix as companion tables (**4a–4e** including **entry capital**) + composite buckets
7. City leaderboards (cash flow with metro median column; single-family; 2–4 unit; appreciation; jobs; balanced; **top suburbs**; **top industries**; **income / race notes**; **entry-capital notes for featured metros**)
8. All-state deep dives (**every state + D.C.**) with inline **Prices:**, **Entry capital:**, **Top industries:**, **Demographics / income:**, and **Top suburbs:** when researched
9. Legal environment highlights
10. Insurance and property-tax overlays
11. Practical acquisition workflow
12. Methodology and sources + **navigable A–Z actionable-rank index** (every state links to its deep dive)

If output length is limited, still keep this outline: compress deep-dive narratives before dropping whole sections or whole states. **Never drop median/typical prices from the all-state matrix.** Prefer keeping **top industries**, **demographics / income**, and **entry capital** for all states. **Never replace deep dives with remaining-state bullet cards.** Do **not** add a separate standalone price-, demographics-, or income-dump section. Never replace this format with a different report layout.

---

## AI prompt (copy-paste)
[↑ Back to Spec index](#spec-index)


```text
You are a US residential rental-market analyst.

FORMAT (MANDATORY):
- Open and follow the workspace base report `rental_market_report.md` as the template.
- Keep the SAME numbered section order, table styles, and concise comparative tone.
- Do NOT invent a different outline or dashboard-style report.
- Prefer plain English. Spell out agency/index names. Avoid stacking abbreviations in reader-facing text.
- Use everyday table labels: Jobs, Price, Cash flow, Appreciation, Owner law, Tenant law.
- Say “single-family” and “2–4 unit” (duplex/triplex/fourplex) in reader-facing text.
- Refresh `rental_market_report.md` as the latest base report. Optionally also save `rental_market_report_YYYY-MM-DD.md`.
- Always include “What changed vs the prior run” when a prior report exists.
- Always include a top **Index** (TOC with anchors) and a navigable end **A–Z rank index**.
- Put **[↑ Back to Index](#index)** under every indexed section / subsection heading (including each deep dive and 4a–4e).
- Use the durable pipeline: LIVE FETCH → overwrite `data/` → BUILD report tables → narrative update. Do NOT create disposable `_add_*.py` Markdown patch scripts.

PROPERTY TYPE SCOPE:
- Analyze long-term rentals for BOTH:
  1) Single-family houses, preferably 3-bedroom comps when available
  2) Small multifamily homes (2–4 units: duplex/triplex/fourplex)
- If single-family and 2–4 unit rankings diverge, say so and provide split shortlists.
- Condos/HOA product are not the primary universe unless noted as a risk overlay.
- Prefer like-for-like price/rent comps. Do not mix large apartment-tower data with 2–4 unit homes without labeling.

CRITICAL — LIVE DATA REQUIRED EVERY RUN:
- You MUST actively live-fetch current public data on EVERY full refresh (pipeline fetchers and/or web search/browse) BEFORE scoring or ranking.
- OVERWRITE `data/*.json` (or CSV) with this run’s pulls. Do NOT skip fetch because prior data files exist. Do NOT silently reuse unlabeled cache.
- Do NOT rely on training memory or the previous report’s numbers as the primary source for prices, rents, jobs, demographics, household income, appreciation, insurance, taxes, supply, or landlord/tenant law.
- If web search / browsing / fetch is unavailable, STOP and say you cannot complete this analysis properly. Do not invent a full national ranking from memory.
- Cite sources with URLs (or exact publication name + date) for key figures.
- State the analysis date and the “as of” date for major datasets in the report and in `data/meta.json`.
- If a datapoint cannot be found after searching/fetching, mark it `unavailable`, lower confidence, and do not fabricate numbers. Default: no silent STALE fallback unless the user explicitly allows it.
- Prefer data from the last 12–24 months; use longer windows for appreciation trends and Decennial race baselines.
- Cross-check important claims with at least two independent source types when possible.
- Suggested sources to search/fetch: Bureau of Labor Statistics / Bureau of Economic Analysis / Census (jobs), Census Decennial / ACS / CPS ASEC / FRED (demographics and household income), Zillow / Redfin / National Association of Realtors / Federal Housing Finance Agency (prices/liquidity), Zillow / Apartment List / HUD / American Community Survey (rents/vacancy/concessions), Federal Housing Finance Agency / Case-Shiller (appreciation), Census / IRS migration, permits/delivery reports (supply), effective property-tax summaries, landlord-insurance/catastrophe reports, and state/city statute or ordinance pages (including licensing/registration).

Required search / fetch workflow:
1) Confirm `.env` keys: `CENSUS_API_KEY`, `FRED_API_KEY`, `BLS_API_KEY`, `BEA_API_KEY`.
2) Run `python -m pipeline.fetch_all` — overwrites `data/`; confirm `data/meta.json` timestamps and per-source `"ok"`.
3) Run `python -m pipeline.build_report` — rebuilds §4b–4e, deep-dive Prices/Entry capital/Industries/Demographics, patterned unemployment/FHFA leads, and live §1/§2 bullets (via `update_from_data`).
4) Metro/city / suburb / legal / insurance web queries for anything not yet in `data/` (especially metro prices beyond preserved screens, rents/concessions, statutes).
5) Extra legal searches for known local-rule cities (e.g., New York City, San Francisco, Los Angeles, Seattle, Chicago), including rent caps, just-cause, and rental licensing.
6) Extra insurance searches for catastrophe-exposed markets (Florida, Louisiana, Texas Gulf, hail belt, California wildfire zones) and apply cash-flow haircuts.
7) Only if evidence warrants: revise §4a **score numbers**, top 10, avoid list, and city boards — do not invent score changes without citing the new `data/` or web sources.
8) Write/keep the report in the `rental_market_report.md` format; optionally save a dated archive.
9) In Methodology, list live-fetch confirmation (this run), all `*_api_key_present` flags, property-type scope, financing assumptions, yield definition, **price-measure definitions (median vs typical/list)**, **industry sources**, **demographics/income sources**, suburb sources, source links, and data gaps.
10) Never use Markdown `~` / `~~` for “approximately” (causes strikethrough); use `about` or `≈`.

DEFAULT UNDERWRITING ASSUMPTIONS (state them; override only if user specifies):
- 25% down, investor / cash-flow–qualified rental financing at current live-searched rate band
- Closing/acquisition costs screen ~3% of purchase (cash to close ≈ 28% of price at defaults)
- Recommended shock liquid: **6 months** PITI (raise to **9–12 months** in high-insurance / high-tax / soft-rent markets)
- Vacancy 5–8% (higher if concessions are elevated)
- **Property management:** about **10% of collected rent** ongoing (within the common 8–12% band; national survey averages near ~8.5%) unless a live PM quote is used; plus leasing/placement allowance of about **50–100% of one month’s rent** on turnover
- Operating expenses ~35–50% of gross rent before debt (includes management), higher in high-tax/high-insurance/older-stock markets
- Gross yield = annual rent / price (screen only)
- Prefer achieved rent over asking rent; if using asking rent indexes, label it
- Stress top markets for rate +1%, rent −5%, insurance +50%, and 6 months vacancy/nonpayment

Using that live-researched data and clear assumptions, analyze the rental investment landscape for all 50 US states + DC and each state’s major cities/metros.

Produce two parallel views:
1) Best markets with relatively strong LANDLORD protections (and why).
2) Best markets with relatively strong TENANT protections that still have an investment case (and why).

For every state and its major cities, evaluate and score (1–10) and rank on:
- Job market (employment strength, growth, wages, migration/demand, **top 2–4 industries / employer clusters**, concentration risk)
- House price (affordability / investor entry cost for single-family and small multifamily — report **both median and average** prices for the state and each major city; use **price-to-income** vs median/mean household income)
- Rental cash flow (rent vs price, gross yield, then realistic net after tax/insurance/vacancy/concessions)
- Property appreciation (recent trend + forward demand/supply thesis)
- Legal environment: owner favorability and tenant favorability (note city-level overrides and licensing regimes)

Also report for every state + D.C. (and featured metros/suburbs when available):
- **Race/ethnicity mix** (top groups; Hispanic/Latino as ethnicity any race)
- **Median and mean household income** (mark mean `unavailable` if not found after search)

Also apply mandatory overlays:
- Insurance/catastrophe risk
- Property-tax drag
- New supply / vacancy / concessions
- Liquidity/exit risk
- Remote-operability / property-management availability
- Ops-intensity caveats for ultra-high-yield markets
- **Industry concentration / boom-bust risk** when one sector dominates

Then provide the report in this exact section order:
1) Header + disclaimer
2) **Index** (TOC + shortcuts to 4a–4d, deep dives, city boards, A–Z)
3) What changed vs prior run
4) National market snapshot + yield definition + core conclusion + single-family vs 2–4 unit takeaway
5) Top 10 actionable markets; landlord-protection list; tenant-protection list; avoid/watch
6) All-state ranking matrix as companion tables (**4a–4e** including **entry capital**) + composite buckets
7) City leaderboards (cash flow with metro median/screen price; best single-family; best 2–4 unit; appreciation; jobs; balanced shortlist; **top suburbs**; **top industries**; **income / race notes**; **entry-capital notes for featured metros**)
8) All-state deep dives (**every state + D.C.**) with inline **Prices:**, **Entry capital:**, **Top industries:**, **Demographics / income:**, and **Top suburbs:** when researched
9) Legal environment highlights with links
10) Insurance and property-tax overlays
11) Practical acquisition workflow
12) Methodology and sources + **navigable A–Z actionable-rank index** (every state → deep dive)

Rules:
- Match `rental_market_report.md` format first; **live-fetch every run** before you rank; overwrite `data/`; build tables from `data/`.
- Do **not** use disposable `_add_*.py` string-replace patch scripts.
- Put median **and** typical/average prices **in context** (matrix columns, city tables, deep dives). Do **not** create a separate standalone price-dump section.
- Write a **deep dive for every state + D.C.** (same field labels including **Entry capital:**); do not use remaining-state bullet cards.
- Report **entry capital screens** (down %, cash to close, shock liquid, total recommended liquid) for every state + D.C., and metro/suburb variants when prices diverge.
- Report **top 2–4 job industries** for every state + D.C., and metro industries when they differ; flag concentration risk.
- Report **race/ethnicity mix** and **median + mean household income** for every state + D.C. (4d companion or cards); metro/suburb notes when they diverge. Demographics are demand-context only — never an exclusion ranking criterion.
- Research **top suburbs** inside major metros (1–3 each); label cash-flow vs appreciation; keep the parent metro name; do not invent a national rank row per suburb unless asked.
- Be comparative across the whole country; do not skip small states.
- Separate cited/estimated figures from judgment.
- Do not invent precise legal citations or fake statistics; mark uncertainty after searching.
- Prefer metro-level data when that is how housing markets trade; drill to suburbs for underwriting screens.
- Default equal weights for Job/Price/Cash flow/Appreciation; also show legal-adjusted views where useful.
- City legal rules override state baseline for that city’s ranking.
- Do not treat gross yield as cash-on-cash.
- Do not give High confidence without live-cited median price, rent/yield proxy, jobs, and legal direction.
- If response length is limited: keep the section outline; compress deep-dive narratives before dropping sections or states; never drop Median $/Typical $ from the all-state matrix; keep state top industries and demographics/income; never replace deep dives with bullet cards.
```

---

## Optional follow-up prompts
[↑ Back to Spec index](#spec-index)


Use after the base analysis:

1. **Cash-flow screen:** “From the full list, keep only markets with estimated gross yield ≥ X% and landlord legal ≥ 7 after insurance/tax haircuts. Re-rank. Split SFR vs 2–4 unit.”
2. **Remote-investor screen:** “Prefer landlord-friendly states with professional property-management availability and strong job diversity; exclude heavy rent-control cities and insurance-broken coastal markets.”
3. **Appreciation screen:** “Re-rank top 20 by appreciation + job growth; accept thinner near-term cash flow. Note SFR vs MF.”
4. **Single-state deep dive:** “Expand [State] with top metros, SFR vs 2–4 unit comps, neighborhood-level caveats, tax/insurance notes, licensing/eviction timeline summary, and stress tests.”
5. **Update pass:** “Re-run **live fetch** (overwrite `data/`), rebuild via pipeline, and refresh `rental_market_report.md` with data as of [date]; keep the same format; show what changed, old vs new figures, and source links. Optionally also save a dated archive.”
6. **Source audit:** “For the top 20 markets, list every key figure with URL, publisher, and as-of date. Flag anything that came from estimate rather than a cited source. Confirm each tabular field was live-fetched this run.”
7. **Property-type only:** “Re-rank using SFR-only comps” or “Re-rank using 2–4 unit multifamily-only comps.”
8. **Capital constraint:** “Re-rank for a max purchase price of $[X] per door / per property.”
9. **Pipeline expand:** “Extend `pipeline/fetch_*.py` to cover [mean income / BLS industry shares / metro ACS / …]; keep live-every-run behavior; rebuild 4c/4d.”

---

## Out of scope (unless asked later)
[↑ Back to Spec index](#spec-index)


- Specific property / address-level underwriting or deal analysis
- Large commercial apartments (5+ units) — see sibling `apartment_market_spec.md` / `apartment_market_report.md`
- SFH appreciation / equity-path rankings — see sibling `sfh_appreciation_spec.md` / `sfh_appreciation_report.md`
- Short-term rental (Airbnb), or mobile-home park strategies
- International markets
- Personalized portfolio allocation, tax filing, or insurance brokerage advice
