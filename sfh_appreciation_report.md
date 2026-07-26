# US Single-Family Home Appreciation Investment Analysis

**Sibling report (appreciation-first):** `sfh_appreciation_report.md`  
**Spec:** `sfh_appreciation_spec.md`  
**Base rental format template:** `rental_market_report.md` (section skeleton mirrored; scores and rankings retitled for equity-path single-family)  
**Analysis date:** July 26, 2026  
**Coverage:** All 50 states + Washington, D.C.; major metro screening; appreciation-focused deep dives  
**Property types:** **Single-family houses only** (detached 1-unit). Not apartments; not 2–4 unit multifamily as the primary lens.  
**Investor objective:** **Appreciation / equity path** on a **5–10+ year** hold. Day-one cash flow is secondary — thin or break-even carry can be acceptable if demand, supply constraints, and exit liquidity support the thesis.  
**Live research:** Yes. Tabular fields from live `data/` (FHFA YoY, Redfin state prices, BLS jobs/industries, Census/FRED demographics & income, BEA). Legal / insurance / suburb qualitative notes adapted from the base report research layer.

> Informational screening only — not financial, legal, tax, insurance, or investment advice. Confirm laws with local counsel and underwrite an actual address before buying.

---

## Index

Jump to a section (companion tables in §4 share the same state order):

Every section below includes **[↑ Back to Index](#index)** under its heading so you can return here after jumping.

| | |
|---|---|
| [1. What changed](#1-what-changed-vs-the-prior-run) | [2. National snapshot](#2-national-market-snapshot) |
| [3. Top 10 / lists](#3-top-10-actionable-markets) | [4. All-state matrix](#4-all-state-ranking-matrix) |
| [4a Scores](#4a-scores-actionable-order) · [4b Prices](#4b-prices--major-metros-same-order) | [4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) · [4e Entry capital](#4e-entry-capital--shock-reserves-same-order) |
| [5. City leaderboards](#5-city-leaderboards) | [6. All-state deep dives](#6-all-state-deep-dives) |
| [7. Legal](#7-legal-environment--verified-2026-highlights) | [8. Insurance & tax](#8-insurance-and-property-tax-overlays) |
| [9. Property management](#9-property-management-rates--remote-ops) | [10. Acquisition workflow](#10-practical-acquisition-workflow) |
| [11. Methodology & sources](#11-methodology-and-sources) | [A–Z state rank index](#az-actionable-rank-index) |

**Deep dives (all states + D.C., appreciation actionable order):** [IL](#illinois) · [WI](#wisconsin) · [CT](#connecticut) · [NJ](#new-jersey) · [PA](#pennsylvania) · [NY](#new-york) · [KY](#kentucky) · [IN](#indiana) · [MO](#missouri) · [MA](#massachusetts) · [ND](#north-dakota) · [TN](#tennessee) · [NH](#new-hampshire) · [NE](#nebraska) · [VT](#vermont) · [OH](#ohio) · [ID](#idaho) · [IA](#iowa) · [SD](#south-dakota) · [AR](#arkansas) · [HI](#hawaii) · [WV](#west-virginia) · [VA](#virginia) · [AL](#alabama) · [GA](#georgia) · [AK](#alaska) · [MN](#minnesota) · [MI](#michigan) · [KS](#kansas) · [ME](#maine) · [MS](#mississippi) · [SC](#south-carolina) · [NC](#north-carolina) · [MD](#maryland) · [MT](#montana) · [NM](#new-mexico) · [AZ](#arizona) · [LA](#louisiana) · [WY](#wyoming) · [NV](#nevada) · [DE](#delaware) · [OK](#oklahoma) · [UT](#utah) · [TX](#texas) · [OR](#oregon) · [FL](#florida) · [RI](#rhode-island) · [WA](#washington) · [CO](#colorado) · [CA](#california) · [DC](#district-of-columbia)

**City boards:** [Appreciation path](#appreciation-path-metros-fhfa--demand) · [Single-family equity](#best-single-family-equity-path-metros) · [Jobs / migration](#job--migration-leaders) · [Supply-constrained / high-income](#supply-constrained--high-income-screens) · [Top suburbs (App tilt)](#top-suburbs-worth-researching-appreciation-tilt) · [Carry / thin-cash notes](#carry--thin-cash-notes-secondary)

---

## 1. What changed vs the prior run
[↑ Back to Index](#index)

This is the **first sibling deliverable** focused solely on **single-family appreciation investing**. It does **not** replace `rental_market_report.md` (cash-flow–balanced SFR + 2–4 unit).

| Change | What it means |
| ------ | ------------- |
| **New strategy lens** | Rankings overweight **appreciation**, **jobs/migration**, **entry vs income**, **liquidity/exit**, and **owner-law / remote ops**; day-one cash flow is secondary |
| **Property scope** | **Single-family houses only** — apartments and 2–4 unit MF are out of primary scope |
| **Squatting overlay** | Vacant App SFH treated as first-class risk — reform vs friction jurisdictions, adverse-possession neglect, vacant monitoring |
| **Score column meanings** | Same 4a columns as the base report, but **Price** = entry-vs-income + liquidity for equity path (not pure “cheap = good”); **Cash** = carry tolerance (thin OK); **Appr.** dominates the Econ blend |
| **Econ weights** | Appreciation **40%** / Jobs **30%** / Price **20%** / Cash **10%** (vs equal 25% pillars in the base rental report) |
| **Live data reused** | Same `data/` snapshots: FHFA, Redfin state prices, BLS jobs/industries, ACS/FRED income & demographics, BEA |
| **Rank flip vs base** | Midwest cash-flow leaders (Ohio, Indiana, Arkansas) fall behind **FHFA + liquidity appreciation leaders** (Illinois, Wisconsin, Connecticut, New Jersey, Pennsylvania, upstate New York, etc.) |
| **Format** | Mirrors `rental_market_report.md` section order, Index / Back to Index, companion tables, all-state deep dives |

**Defaults used (user did not override):** appreciation-first; single-family only; remote-capable preferred; **5–10+ year** hold; moderate risk; thin day-one cash flow acceptable; **vacant SFH monitored against squatting**.

---

## 2. National market snapshot
[↑ Back to Index](#index)

- State unemployment (BLS LAUS, June 2026): lowest **South Dakota 2.0%**, highest **District of Columbia 6.0%**; unweighted state mean about **4.0%** ([Bureau of Labor Statistics](https://www.bls.gov/news.release/laus.htm)).
- **FHFA purchase-only HPI YoY (2026Q1):** state range **-2.4%** to **+7.3%**; median state about **+2.4%** (live `data/fhfa.json`).
- **State prices (live):** Redfin All Residential medians as of **2026-05-31** in §4b (state median range about **$259k–$887k**).
- Typical U.S. home value was **$370,320 in May 2026** ([Zillow via Federal Reserve Economic Data](https://fred.stlouisfed.org/series/USAUCSFRCONDOSMSAMID)).
- National median sale price was **$408,776 in June 2026**, up 2.2% year over year; average 30-year mortgage rate about **6.49%** ([Redfin](https://www.redfin.com/news/home-prices-record-high-june-2026/)).
- National house prices rose **1.7% year over year in first-quarter 2026** — recent strength tilted Midwest / Northeast ([Federal Housing Finance Agency](https://www.fhfa.gov/reports/house-price-index/2026/Q1)).
- **BEA per-capita personal income (2024):** state range about **$52k–$113k** (`data/bea.json`; demand-capacity context).
- **Entry capital tabulated:** §4e screens **25% down**, cash to close (about 28% of median), and **6–9 months** PITI shock reserves — still required even when cash flow is secondary.
- **Demographics & income tabulated:** §4d (ACS race; CPS/FRED median HH income; ACS mean HH income).
- **Job industries tabulated:** §4c from live BLS CES SAE (`data/industries.json`).
- Population growth slowed nationally; South Carolina, Idaho, and North Carolina led state percentage growth; Houston and Dallas led numeric metro gains ([U.S. Census Bureau](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html)).
- Typical investor loan rates for rental purchases in July 2026 cluster near **7.0%–8.5%** for standard files ([July 2026 investor/DSCR lender sheets](https://dscrfinder.com/blog/current-dscr-loan-rates)). Some appreciation buyers use higher leverage or cash — **this report still discloses the 25% default** for comparability.

### Equity-path definition used here
[↑ Back to Index](#index)

- **Primary success metric:** multi-year **price appreciation + equity build** (FHFA / local price path + demand/supply thesis), not year-one cash-on-cash.
- **Carry** still matters: model PITI + tax + insurance + vacancy + management so thin cash flow does not force a distressed sale.
- **Gross yield** (if shown) is a **carry screen only** — never treat it as the ranking objective.
- Prefer **owner-occupant exit liquidity** (broad single-family buyer pool) over specialty product.
- **Vacant SFH squatting risk** is first-class on App holds: longer vacancy / rehab windows attract unauthorized occupants — budget monitoring and know trespass vs eviction paths.

### Core conclusion
[↑ Back to Index](#index)

For **single-family appreciation** in mid-2026, the actionable screen shifts away from Midwest **cash-flow** leaders in the base rental report toward markets with **strong recent FHFA price growth**, **deeper exit liquidity**, and/or **structural demand** (job magnets, migration corridors, supply-constrained metros).

**Near-term price leaders** cluster in parts of the **Midwest and Northeast** (Illinois, Wisconsin, Connecticut, New Jersey, New York, Pennsylvania, Kentucky) on FHFA 2026Q1 YoY — often with thinner day-one yields than Detroit/Cleveland cash-flow screens.

**Structural / long-hold equity** still points many investors toward **supply-constrained or high-income job metros** (Boston, North Jersey, Northern Virginia, selected Sun Belt growth metros, Utah/Idaho) even when one-year FHFA is soft — underwrite the carry and do not buy a narrative without reserves.

**Squatting / vacant holds:** 2024–2026 anti-squatter reforms improved owner tools in many states, but **practice varies by county**. Unmonitored vacant App houses remain a capital-and-title risk — especially where LE still defaults to civil process. Prefer leased or actively inspected vacant inventory over “set and forget” equity holds.

**Single-family only:** this report does not split duplex/fourplex shortlists. Use `rental_market_report.md` for cash-flow–first or 2–4 unit screens.

---

## 3. Top 10 actionable markets
[↑ Back to Index](#index)

Tie-breakers after equal economic scores: **exit liquidity**, data confidence, lower insurance catastrophe risk, remote management availability, **clearer vacant-SFH / squatter removal path**, diversified jobs.

| Rank | State / preferred metros | Why it ranks | Single-family equity note | Main caution |
| ---- | ------------------------ | ------------ | ------------------------- | ------------ |
| 1 | **Illinois — Chicago, Peoria** | Top FHFA YoY nationally (+7.3%) plus Chicago metro depth | Buy Chicago / Peoria SFH for equity; accept thinner carry | City ordinance friction; Cook County ops; soft jobs pocket |
| 2 | **Wisconsin — Milwaukee, Madison** | Strong FHFA (+4.5%) with owner-friendly law and Madison/Milwaukee depth | Milwaukee suburbs + Madison for tenure / schools | Property taxes; winter maintenance |
| 3 | **Connecticut — Hartford, Bridgeport** | FHFA +4.7%; Bridgeport–Stamford among metro Appr leaders | Hartford for lower entry; Stamford corridor for spillover | Tenant-leaning climate; higher Northeast taxes |
| 4 | **New Jersey — Newark / North Jersey** | FHFA +4.5% with NYC-spillover demand and deep buyer pool | North Jersey SFH equity path; South Jersey lower entry | Nation-high property taxes; Anti-Eviction / local rent overlays |
| 5 | **Pennsylvania — Philadelphia, Pittsburgh, Lancaster** | FHFA +3.8%; Lancaster/Reading metro YoY leaders; Philly liquidity | Philadelphia suburbs + Lancaster for App; Pittsburgh more balanced | Older housing; Philly local rules / taxes |
| 6 | **New York — Buffalo, Rochester, Syracuse (upstate focus)** | FHFA +4.4%; Syracuse among metro Appr leaders | Focus **upstate** Buffalo / Rochester / Syracuse SFH — not NYC boroughs | Statewide tenant tilt; Good Cause in opt-in cities; NYC specialist-only |
| 7 | **Kentucky — Louisville, Lexington** | FHFA +4.7% with still-affordable entry vs coasts | Louisville / Lexington SFH for App + accessible capital | State unemployment 4.7%; smaller coastal-style buyer pool |
| 8 | **Indiana — Indianapolis, Fort Wayne** | FHFA +3.6%, low unemployment, scalable Indy SFH liquidity | Fishers / Carmel App suburbs; Indy turnkey SFH | Not the highest YoY; rising concessions metro-wide |
| 9 | **Missouri — Kansas City, St. Louis** | FHFA +3.9% with two scalable metros | Overland Park / Lee’s Summit App; KC/STL depth | Neighborhood selection in St. Louis |
| 10 | **Massachusetts — Boston, Worcester** | Structural supply constraint + high-income jobs; FHFA +2.2%; Boston liquidity | Boston / Worcester SFH for long equity path; expect thin/negative carry | Very high entry capital; regulation and insurance overlays |

### Best landlord-protection markets (law + equity path)
[↑ Back to Index](#index)

| Rank | Market | Why |
| ---- | ------ | --- |
| 1 | Wisconsin — Milwaukee / Madison | Owner-friendly baseline + strong FHFA |
| 2 | Indiana — Indianapolis | Rent-control preemption; App suburbs + scale |
| 3 | Kentucky — Louisville / Lexington | Favorable law + top-tier statewide appreciation |
| 4 | Missouri — Kansas City | Workable law + App suburbs |
| 5 | Pennsylvania — Pittsburgh / Lancaster | Improving prices; manageable statewide baseline |
| 6 | Utah — Salt Lake / Provo | Strong owner law + migration / jobs (softer near-term FHFA) |
| 7 | Idaho — Boise | Owner-friendly + migration; higher entry |
| 8 | Georgia — Atlanta job pockets | Strong owner law + migration; Georgia Squatter Reform Act improves vacant-SFH tools |
| 9 | North Carolina — Raleigh / Charlotte | Jobs / migration equity thesis; expanding anti-squatter toolkit — verify county practice |
| 10 | Tennessee — Nashville suburbs | Favorable law; App tilt outside Memphis CF |

### Best tenant-protection markets that still have an equity case
[↑ Back to Index](#index)

These are **not** easiest for landlords. They can still work for **appreciation / long holds** if you accept slower ops.

| Rank | Market | Protection reality | Equity case |
| ---- | ------ | ------------------ | ----------- |
| 1 | **Upstate New York — Syracuse / Rochester / Buffalo** | Good Cause in opt-in cities; statewide tenant tilt | Among strongest FHFA / metro Appr prints |
| 2 | **Chicago, Illinois** | City ordinance / Fair Notice; IL preempts rent control | Nation-leading state FHFA YoY + deep liquidity |
| 3 | **Connecticut — Hartford / Bridgeport** | Tenant-leaning statewide climate | FHFA +4.7%; coastal spillover |
| 4 | **North Jersey** | Anti-Eviction Act; local rent ordinances | FHFA +4.5%; NYC spillover buyer pool |
| 5 | **Massachusetts — Boston metro** | Tenant-leaning pockets | Structural supply + high incomes |
| 6 | **Maryland — selected suburbs** | State / county protections | D.C. spillover demand; thinner than North Jersey |
| 7 | **Minnesota — Twin Cities** | More balanced / tenant-leaning than Midwest peers | Stable demand; moderate FHFA |
| 8 | **Oregon — selected inland** | Statewide rent cap | Long-term supply constraints; weak near-term jobs/prices |
| 9 | **Washington — Spokane over Eastside** | Statewide rent cap | Prefer Spokane value vs Seattle Eastside for entry |
| 10 | **Selected inland California** | Statewide rent cap + local overlays | Supply constraint; very thin carry |

### Markets to avoid / watch (appreciation lens)
[↑ Back to Index](#index)

| Market | Issue |
| ------ | ----- |
| **District of Columbia** | Soft FHFA; weak jobs; TOPA / rent stabilization; expensive entry |
| **Colorado Front Range (near-term)** | FHFA about −2.4% — digesting pandemic prices; long thesis ≠ buy-blind |
| **Austin / selected Texas boom metros** | Population still grows, but price correction + concessions show oversupply risk |
| **Coastal California trophy SFH** | Extreme entry; thin/negative carry; regulation-heavy — specialist equity only |
| **Seattle Eastside** | Soft prices + statewide rent cap + high concessions |
| **Portland, Oregon** | Job losses + rent cap + soft near-term path |
| **Florida coastal / condo-adjacent** | Insurance can erase equity math even if rents look fine |
| **Ultra-cheap CF cities as “App” buys** | Detroit / Jackson headline yields ≠ appreciation thesis — condition and exit risk |
| **Unmonitored vacant App SFH (any market)** | Squatting / unauthorized occupancy + damage + adverse-possession neglect risk — especially where LE treats occupation as civil |
| **NYC borough vacant / specialist equity** | High friction for unauthorized-occupant removal vs upstate SFH App path |
| **Coastal CA vacant trophy holds** | Extreme entry + regulation; confirm current trespass-removal bills/status before vacant buy-and-hold |

---

## 4. All-state ranking matrix
[↑ Back to Index](#index)

Companion tables share the same `#` order. **Econ** uses appreciation-first weights (Appr 40% / Jobs 30% / Price 20% / Cash 10%).

### 4a. Scores (actionable order)
[↑ Back to Index](#index)

`#` = appreciation actionable rank after tie-breakers. **Price** = entry-vs-income **plus liquidity** for an equity-path buy (higher ≠ always cheapest). **Cash** = carry tolerance (thin OK). **Appr.** = FHFA YoY + structural demand overlay.

| # | State (primary metros) | Jobs | Price | Cash | Appr. | Econ | Owner | Tenant | Conf. |
| --- | ---------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ------ | ------ |
| 1 | Illinois — Chicago, Peoria | 4 | 8 | 4 | 10 | 7.20 | 6 | 6 | High |
| 2 | Wisconsin — Milwaukee, Madison | 8 | 8 | 5 | 10 | 8.50 | 9 | 2 | High |
| 3 | Connecticut — Hartford, Bridgeport | 4 | 7 | 4 | 10 | 7.00 | 5 | 7 | High |
| 4 | New Jersey — Newark / North Jersey | 6 | 7 | 1 | 10 | 7.30 | 3 | 9 | High |
| 5 | Pennsylvania — Philadelphia, Pittsburgh, Lancaster | 6 | 8 | 6 | 9 | 7.60 | 7 | 4 | High |
| 6 | New York — Buffalo, Rochester, Syracuse (upstate focus) | 5 | 7 | 2 | 10 | 7.10 | 1 | 10 | High |
| 7 | Kentucky — Louisville, Lexington | 5 | 7 | 6 | 9 | 7.10 | 8 | 3 | High |
| 8 | Indiana — Indianapolis, Fort Wayne | 8 | 8 | 7 | 8 | 7.90 | 9 | 2 | High |
| 9 | Missouri — Kansas City, St. Louis | 7 | 8 | 6 | 8 | 7.50 | 8 | 3 | High |
| 10 | Massachusetts — Boston, Worcester | 6 | 7 | 1 | 9 | 6.90 | 6 | 6 | High |
| 11 | North Dakota — Fargo, Bismarck | 10 | 6 | 4 | 9 | 8.20 | 8 | 3 | Medium |
| 12 | Tennessee — Nashville, Knoxville, Memphis | 9 | 8 | 5 | 8 | 8.00 | 9 | 2 | High |
| 13 | New Hampshire — Manchester–Nashua | 9 | 7 | 2 | 9 | 7.90 | 5 | 7 | High |
| 14 | Nebraska — Omaha, Lincoln | 9 | 7 | 5 | 8 | 7.80 | 7 | 3 | High |
| 15 | Vermont — Burlington | 9 | 6 | 2 | 9 | 7.70 | 4 | 8 | Medium |
| 16 | Ohio — Columbus, Cincinnati, Cleveland | 7 | 8 | 7 | 8 | 7.60 | 9 | 2 | High |
| 17 | Idaho — Boise | 8 | 6 | 2 | 9 | 7.40 | 10 | 1 | High |
| 18 | Iowa — Des Moines, Cedar Rapids | 8 | 6 | 6 | 8 | 7.40 | 9 | 2 | High |
| 19 | South Dakota — Sioux Falls | 10 | 6 | 4 | 7 | 7.40 | 8 | 3 | Medium |
| 20 | Arkansas — Northwest Arkansas, Little Rock | 7 | 7 | 6 | 8 | 7.30 | 9 | 2 | High |
| 21 | Hawaii — Honolulu | 9 | 4 | 1 | 9 | 7.20 | 7 | 4 | High |
| 22 | West Virginia — Charleston, Morgantown | 6 | 6 | 6 | 9 | 7.20 | 9 | 2 | Medium |
| 23 | Virginia — Northern Virginia, Richmond | 7 | 8 | 3 | 8 | 7.20 | 8 | 3 | High |
| 24 | Alabama — Birmingham, Huntsville | 8 | 7 | 6 | 7 | 7.20 | 9 | 2 | High |
| 25 | Georgia — Atlanta, Athens | 9 | 8 | 4 | 6 | 7.10 | 9 | 2 | High |
| 26 | Alaska — Anchorage | 6 | 6 | 3 | 9 | 6.90 | 8 | 3 | Medium |
| 27 | Minnesota — Minneapolis–St. Paul | 6 | 8 | 3 | 8 | 6.90 | 6 | 6 | High |
| 28 | Michigan — Detroit, Grand Rapids | 5 | 8 | 6 | 8 | 6.90 | 8 | 3 | High |
| 29 | Kansas — Wichita, Kansas City–KS | 7 | 7 | 5 | 7 | 6.80 | 8 | 3 | High |
| 30 | Maine — Portland | 8 | 7 | 2 | 7 | 6.80 | 5 | 7 | High |
| 31 | Mississippi — Jackson, Gulfport | 7 | 7 | 5 | 7 | 6.80 | 9 | 2 | High |
| 32 | South Carolina — Greenville, Charleston | 7 | 7 | 4 | 7 | 6.70 | 9 | 2 | High |
| 33 | North Carolina — Raleigh, Charlotte | 8 | 7 | 3 | 6 | 6.50 | 8 | 3 | High |
| 34 | Maryland — Baltimore | 6 | 8 | 4 | 6 | 6.20 | 5 | 7 | High |
| 35 | Montana — Billings, Bozeman | 8 | 6 | 2 | 6 | 6.20 | 9 | 2 | Medium |
| 36 | New Mexico — Albuquerque, Santa Fe | 5 | 6 | 4 | 7 | 5.90 | 8 | 3 | High |
| 37 | Arizona — Phoenix, Tucson | 5 | 8 | 3 | 6 | 5.80 | 9 | 2 | High |
| 38 | Louisiana — New Orleans, Baton Rouge | 6 | 7 | 2 | 6 | 5.80 | 9 | 2 | High |
| 39 | Wyoming — Cheyenne | 8 | 5 | 4 | 5 | 5.80 | 9 | 2 | Medium |
| 40 | Nevada — Las Vegas, Reno | 5 | 7 | 3 | 6 | 5.60 | 8 | 3 | High |
| 41 | Delaware — Wilmington | 5 | 7 | 3 | 6 | 5.60 | 8 | 3 | High |
| 42 | Oklahoma — Oklahoma City, Tulsa | 6 | 7 | 4 | 5 | 5.60 | 9 | 2 | High |
| 43 | Utah — Salt Lake City, Provo | 8 | 7 | 2 | 4 | 5.60 | 10 | 1 | High |
| 44 | Texas — Dallas–Fort Worth, Houston, Austin | 7 | 9 | 3 | 2 | 5.00 | 9 | 2 | High |
| 45 | Oregon — Portland, Salem | 3 | 7 | 2 | 6 | 4.90 | 3 | 9 | High |
| 46 | Florida — Tampa, Orlando, Jacksonville | 5 | 8 | 2 | 4 | 4.90 | 9 | 2 | High |
| 47 | Rhode Island — Providence | 6 | 6 | 2 | 3 | 4.40 | 7 | 4 | High |
| 48 | Washington — Seattle, Spokane | 3 | 7 | 2 | 4 | 4.10 | 3 | 9 | High |
| 49 | Colorado — Denver, Colorado Springs | 7 | 7 | 2 | 1 | 4.10 | 7 | 5 | High |
| 50 | California — Los Angeles, Bay Area, San Diego | 3 | 6 | 1 | 4 | 3.80 | 3 | 9 | High |
| 51 | District of Columbia — Washington, D.C. | 1 | 5 | 1 | 2 | 2.20 | 1 | 10 | Medium |

### 4b. Prices & major metros (same order)
[↑ Back to Index](#index)

**Median** = Redfin All Residential median sale price (live `2026-05-31`). **Typical** = Redfin median list when present. **FHFA YoY** = purchase-only HPI seasonally adjusted same-quarter year-ago % (`data/fhfa.json`).

| # | State | Median | Typical | FHFA YoY | Major metros / cities |
|---:|---|---:|---:|---:|---|
| 1 | Illinois | $338k | $350k | +7.3% | Chicago, Peoria, Rockford, Springfield |
| 2 | Wisconsin | $362k | $374k | +4.5% | Milwaukee, Madison, Green Bay |
| 3 | Connecticut | $498k | $522k | +4.7% | Hartford, Bridgeport, New Haven |
| 4 | New Jersey | $580k | $597k | +4.5% | Newark, Camden, New Brunswick |
| 5 | Pennsylvania | $330k | $345k | +3.8% | Pittsburgh, Philadelphia, Lancaster |
| 6 | New York | $620k | $639k | +4.4% | New York City, Buffalo, Rochester, Syracuse |
| 7 | Kentucky | $284k | $312k | +4.7% | Louisville, Lexington |
| 8 | Indiana | $287k | $297k | +3.6% | Indianapolis, Fort Wayne, South Bend |
| 9 | Missouri | $298k | $300k | +3.9% | Kansas City, St. Louis, Springfield |
| 10 | Massachusetts | $688k | $719k | +2.2% | Boston, Worcester, Springfield |
| 11 | North Dakota | $311k | $331k | +4.0% | Fargo, Bismarck |
| 12 | Tennessee | $413k | $440k | +2.2% | Memphis, Nashville, Knoxville, Chattanooga |
| 13 | New Hampshire | $538k | $564k | +3.3% | Manchester–Nashua |
| 14 | Nebraska | $319k | $328k | +3.9% | Omaha, Lincoln |
| 15 | Vermont | $448k | $486k | +4.9% | Burlington |
| 16 | Ohio | $283k | $293k | +3.2% | Cleveland, Columbus, Cincinnati, Dayton |
| 17 | Idaho | $503k | $577k | +2.8% | Boise, Idaho Falls, Coeur d’Alene |
| 18 | Iowa | $259k | $274k | +3.5% | Des Moines, Cedar Rapids, Iowa City |
| 19 | South Dakota | $347k | $368k | +2.8% | Sioux Falls, Rapid City |
| 20 | Arkansas | $276k | $306k | +3.4% | Fayetteville–Springdale, Little Rock |
| 21 | Hawaii | $741k | $780k | +2.2% | Honolulu |
| 22 | West Virginia | $265k | $273k | +4.0% | Charleston, Huntington, Morgantown |
| 23 | Virginia | $499k | $502k | +2.4% | Richmond, Virginia Beach, Northern Virginia |
| 24 | Alabama | $313k | $326k | +2.4% | Birmingham, Huntsville, Mobile |
| 25 | Georgia | $389k | $414k | +0.1% | Atlanta, Athens, Augusta, Savannah |
| 26 | Alaska | $427k | $448k | +5.5% | Anchorage, Fairbanks |
| 27 | Minnesota | $372k | $396k | +2.8% | Minneapolis–St. Paul, Duluth, Rochester |
| 28 | Michigan | $298k | $314k | +3.2% | Detroit, Grand Rapids, Lansing, Flint |
| 29 | Kansas | $316k | $319k | +2.5% | Wichita, Kansas City–KS, Topeka |
| 30 | Maine | $439k | $464k | +2.4% | Portland, Bangor |
| 31 | Mississippi | $284k | $287k | +2.1% | Jackson, Gulfport, Hattiesburg |
| 32 | South Carolina | $394k | $410k | +1.5% | Greenville, Columbia, Charleston |
| 33 | North Carolina | $398k | $427k | +0.1% | Raleigh, Charlotte, Greensboro |
| 34 | Maryland | $477k | $477k | +0.6% | Baltimore, Montgomery / Prince George’s |
| 35 | Montana | $529k | $620k | +0.2% | Billings, Missoula, Bozeman |
| 36 | New Mexico | $396k | $446k | +2.2% | Albuquerque, Santa Fe, Las Cruces |
| 37 | Arizona | $454k | $473k | +0.2% | Phoenix metro (Tempe, Gilbert, Chandler), Tucson |
| 38 | Louisiana | $269k | $276k | +1.3% | New Orleans, Baton Rouge, Lafayette |
| 39 | Wyoming | $464k | $647k | -0.0% | Cheyenne, Casper |
| 40 | Nevada | $481k | $506k | +0.7% | Las Vegas, Reno |
| 41 | Delaware | $384k | $408k | +1.0% | Wilmington, Dover |
| 42 | Oklahoma | $265k | $285k | +0.2% | Oklahoma City, Tulsa |
| 43 | Utah | $560k | $619k | -0.1% | Salt Lake City, Provo, Ogden |
| 44 | Texas | $356k | $378k | -1.6% | Houston, Dallas–Fort Worth, San Antonio, Austin |
| 45 | Oregon | $526k | $569k | +0.6% | Portland, Salem, Eugene |
| 46 | Florida | $422k | $439k | -0.5% | Tampa, Orlando, Jacksonville, Miami |
| 47 | Rhode Island | $537k | $583k | -0.7% | Providence |
| 48 | Washington | $652k | $686k | -0.4% | Seattle, Tacoma, Spokane |
| 49 | Colorado | $617k | $620k | -2.4% | Denver, Colorado Springs, Fort Collins |
| 50 | California | $887k | $865k | -0.5% | Los Angeles, Bay Area, San Diego, Sacramento |
| 51 | District of Columbia | unavailable | unavailable | -1.4% | Washington, D.C. |

### 4c. Top job industries (same order)
[↑ Back to Index](#index)

**Source framing:** Live `data/industries.json` (pulled_at=2026-07-26T08:29:05+00:00; BLS CES SAE). Sectors ranked by share of statewide total nonfarm employment.

| # | State | Top industries (largest →) | Concentration / demand note |
|---:|---|---|---|
| 1 | Illinois | trade / logistics; education & health; professional services; government | Diversified |
| 2 | Wisconsin | trade / logistics; education & health; manufacturing; government | Diversified |
| 3 | Connecticut | education & health; trade / logistics; government; professional services | Diversified |
| 4 | New Jersey | trade / logistics; education & health; professional services; government | Diversified |
| 5 | Pennsylvania | education & health; trade / logistics; professional services; government | Diversified |
| 6 | New York | education & health; government; trade / logistics; professional services | Diversified |
| 7 | Kentucky | trade / logistics; education & health; government; manufacturing | Diversified |
| 8 | Indiana | trade / logistics; education & health; manufacturing; government | Diversified |
| 9 | Missouri | trade / logistics; education & health; government; professional services | Diversified |
| 10 | Massachusetts | education & health; professional services; trade / logistics; government | Diversified |
| 11 | North Dakota | trade / logistics; government; education & health; leisure / hospitality | Energy boom-bust risk outside Fargo |
| 12 | Tennessee | trade / logistics; education & health; professional services; government | Diversified |
| 13 | New Hampshire | trade / logistics; education & health; professional services; leisure / hospitality | Diversified |
| 14 | Nebraska | trade / logistics; government; education & health; professional services | Diversified |
| 15 | Vermont | education & health; government; trade / logistics; leisure / hospitality | Diversified |
| 16 | Ohio | trade / logistics; education & health; government; professional services | Diversified |
| 17 | Idaho | trade / logistics; education & health; government; professional services | Diversified |
| 18 | Iowa | trade / logistics; government; education & health; manufacturing | Diversified |
| 19 | South Dakota | trade / logistics; government; education & health; leisure / hospitality | Diversified |
| 20 | Arkansas | trade / logistics; education & health; government; professional services | Diversified |
| 21 | Hawaii | government; leisure / hospitality; trade / logistics; education & health | Concentration / cyclical risk — see deep dive |
| 22 | West Virginia | education & health; government; trade / logistics; leisure / hospitality | Diversified |
| 23 | Virginia | professional services; government; trade / logistics; education & health | Diversified |
| 24 | Alabama | government; trade / logistics; manufacturing; professional services | Diversified |
| 25 | Georgia | trade / logistics; education & health; professional services; government | Diversified |
| 26 | Alaska | government; trade / logistics; education & health; leisure / hospitality | Concentration / cyclical risk — see deep dive |
| 27 | Minnesota | education & health; trade / logistics; government; professional services | Diversified |
| 28 | Michigan | trade / logistics; education & health; professional services; government | Diversified |
| 29 | Kansas | trade / logistics; government; education & health; manufacturing | Diversified |
| 30 | Maine | education & health; trade / logistics; government; leisure / hospitality | Diversified |
| 31 | Mississippi | trade / logistics; government; education & health; leisure / hospitality | Diversified |
| 32 | South Carolina | trade / logistics; government; education & health; professional services | Diversified |
| 33 | North Carolina | trade / logistics; government; professional services; education & health | Diversified |
| 34 | Maryland | government; education & health; professional services; trade / logistics | Diversified |
| 35 | Montana | trade / logistics; government; education & health; leisure / hospitality | Diversified |
| 36 | New Mexico | government; education & health; trade / logistics; professional services | Diversified |
| 37 | Arizona | trade / logistics; education & health; professional services; government | Diversified |
| 38 | Louisiana | trade / logistics; education & health; government; professional services | Concentration / cyclical risk — see deep dive |
| 39 | Wyoming | government; trade / logistics; leisure / hospitality; education & health | Concentration / cyclical risk — see deep dive |
| 40 | Nevada | leisure / hospitality; trade / logistics; professional services; education & health | Tourism / gaming concentration (Las Vegas) |
| 41 | Delaware | education & health; trade / logistics; government; professional services | Diversified |
| 42 | Oklahoma | government; trade / logistics; education & health; professional services | Concentration / cyclical risk — see deep dive |
| 43 | Utah | trade / logistics; government; professional services; education & health | Diversified |
| 44 | Texas | trade / logistics; professional services; government; education & health | Diversified |
| 45 | Oregon | education & health; trade / logistics; government; professional services | Diversified |
| 46 | Florida | trade / logistics; professional services; education & health; leisure / hospitality | Diversified |
| 47 | Rhode Island | education & health; trade / logistics; professional services; leisure / hospitality | Diversified |
| 48 | Washington | trade / logistics; government; education & health; professional services | Diversified |
| 49 | Colorado | trade / logistics; professional services; government; education & health | Diversified |
| 50 | California | education & health; trade / logistics; professional services; government | Diversified |
| 51 | District of Columbia | government; professional services; education & health; leisure / hospitality | Federal / professional concentration — cyclical with federal payrolls |

### 4d. Demographics & income (same order)
[↑ Back to Index](#index)

**Source framing:** Live `data/income.json` + `data/demographics.json`. Median: CPS ASEC via FRED (as_of CPS 2024). Mean: ACS S1901. Demographics are demand-context only — not a ranking filter.

| # | State | Race / ethnicity (top groups) | Median HH income | Mean HH income |
|---:|---|---|---:|---:|
| 1 | Illinois | White 60.7% · Black 13.3% · Hisp 19.0% · Asian 6.0% | $84k | $111k |
| 2 | Wisconsin | White 79.9% · Black 5.9% · Hisp 8.1% · Asian 3.0% | $83k | $98k |
| 3 | Connecticut | White 64.5% · Black 10.9% · Hisp 18.6% · Asian 4.9% | $99k | $131k |
| 4 | New Jersey | White 53.5% · Black 12.7% · Hisp 22.7% · Asian 10.2% | $104k | $138k |
| 5 | Pennsylvania | White 74.0% · Black 10.6% · Hisp 8.9% · Asian 3.9% | $80k | $103k |
| 6 | New York | White 55.1% · Black 14.3% · Hisp 19.8% · Asian 9.1% | $87k | $122k |
| 7 | Kentucky | White 82.5% · Black 7.5% · Hisp 4.9% · Asian 1.4% | $65k | $83k |
| 8 | Indiana | White 76.7% · Black 9.0% · Hisp 8.7% · Asian 2.7% | $77k | $92k |
| 9 | Missouri | White 77.8% · Black 10.8% · Hisp 5.2% · Asian 2.1% | $78k | $93k |
| 10 | Massachusetts | White 67.9% · Black 7.0% · Hisp 13.5% · Asian 7.4% | $114k | $139k |
| 11 | North Dakota | White 82.5% · Black 3.1% · Hisp 4.9% · Asian 1.5% | $88k | $98k |
| 12 | Tennessee | White 72.3% · Black 15.3% · Hisp 7.5% · Asian 1.8% | $76k | $94k |
| 13 | New Hampshire | White 87.5% · Black 1.5% · Hisp 4.7% · Asian 2.6% | $112k | $124k |
| 14 | Nebraska | White 77.7% · Black 4.6% · Hisp 12.9% · Asian 2.5% | $86k | $101k |
| 15 | Vermont | White 89.9% · Black 1.2% · Hisp 2.5% · Asian 1.7% | $85k | $106k |
| 16 | Ohio | White 76.6% · Black 11.9% · Hisp 4.8% · Asian 2.6% | $81k | $94k |
| 17 | Idaho | White 81.7% · Black 0.8% · Hisp 13.8% · Asian 1.4% | $82k | $99k |
| 18 | Iowa | White 84.2% · Black 4.0% · Hisp 7.3% · Asian 2.4% | $85k | $94k |
| 19 | South Dakota | White 80.5% · Black 2.5% · Hisp 5.1% · Asian 1.5% | $80k | $97k |
| 20 | Arkansas | White 68.9% · Black 14.4% · Hisp 9.1% · Asian 1.7% | $65k | $81k |
| 21 | Hawaii | White 21.9% · Black 1.7% · Hisp 10.1% · Asian 36.7% | $98k | $125k |
| 22 | West Virginia | White 90.1% · Black 3.2% · Hisp 2.1% · Asian 0.7% | $63k | $77k |
| 23 | Virginia | White 59.8% · Black 18.4% · Hisp 11.1% · Asian 6.9% | $98k | $123k |
| 24 | Alabama | White 64.7% · Black 25.4% · Hisp 5.7% · Asian 1.5% | $66k | $86k |
| 25 | Georgia | White 50.3% · Black 30.8% · Hisp 11.1% · Asian 4.5% | $81k | $103k |
| 26 | Alaska | White 59.6% · Black 2.9% · Hisp 7.5% · Asian 5.9% | $91k | $114k |
| 27 | Minnesota | White 76.7% · Black 7.2% · Hisp 6.4% · Asian 5.2% | $92k | $113k |
| 28 | Michigan | White 73.8% · Black 13.2% · Hisp 6.0% · Asian 3.4% | $79k | $94k |
| 29 | Kansas | White 75.9% · Black 5.3% · Hisp 13.7% · Asian 2.6% | $88k | $94k |
| 30 | Maine | White 90.1% · Black 1.8% · Hisp 2.2% · Asian 1.1% | $91k | $97k |
| 31 | Mississippi | White 55.6% · Black 35.6% · Hisp 3.7% · Asian 0.9% | $56k | $76k |
| 32 | South Carolina | White 63.6% · Black 24.4% · Hisp 7.4% · Asian 1.8% | $77k | $93k |
| 33 | North Carolina | White 61.4% · Black 20.1% · Hisp 11.4% · Asian 3.3% | $67k | $98k |
| 34 | Maryland | White 47.9% · Black 29.2% · Hisp 12.6% · Asian 6.6% | $110k | $129k |
| 35 | Montana | White 84.6% · Black 0.4% · Hisp 4.6% · Asian 0.8% | $82k | $94k |
| 36 | New Mexico | White 47.5% · Black 2.0% · Hisp 48.6% · Asian 1.8% | $64k | $86k |
| 37 | Arizona | White 58.3% · Black 4.8% · Hisp 31.6% · Asian 3.6% | $85k | $105k |
| 38 | Louisiana | White 56.7% · Black 30.3% · Hisp 7.1% · Asian 1.8% | $61k | $83k |
| 39 | Wyoming | White 84.3% · Black 0.7% · Hisp 10.8% · Asian 0.9% | $79k | $93k |
| 40 | Nevada | White 49.8% · Black 9.4% · Hisp 29.9% · Asian 9.1% | $81k | $103k |
| 41 | Delaware | White 59.3% · Black 22.5% · Hisp 11.1% · Asian 4.3% | $86k | $109k |
| 42 | Oklahoma | White 64.6% · Black 6.8% · Hisp 12.9% · Asian 2.3% | $65k | $86k |
| 43 | Utah | White 78.6% · Black 1.1% · Hisp 16.0% · Asian 2.5% | $104k | $118k |
| 44 | Texas | White 47.7% · Black 12.3% · Hisp 39.8% · Asian 5.7% | $81k | $107k |
| 45 | Oregon | White 73.9% · Black 2.1% · Hisp 14.9% · Asian 4.6% | $90k | $107k |
| 46 | Florida | White 55.5% · Black 14.9% · Hisp 27.4% · Asian 3.0% | $76k | $104k |
| 47 | Rhode Island | White 69.7% · Black 5.4% · Hisp 18.0% · Asian 3.4% | $92k | $113k |
| 48 | Washington | White 65.2% · Black 4.0% · Hisp 14.6% · Asian 10.0% | $98k | $129k |
| 49 | Colorado | White 70.4% · Black 3.9% · Hisp 22.7% · Asian 3.3% | $106k | $125k |
| 50 | California | White 38.5% · Black 5.4% · Hisp 40.4% · Asian 15.8% | $101k | $134k |
| 51 | District of Columbia | White 38.8% · Black 40.9% · Hisp 12.0% · Asian 4.2% | $105k | $161k |

### 4e. Entry capital & shock reserves (same order)
[↑ Back to Index](#index)

**Screen framing (not a lender quote):** Investor default **25% down** + about **3% closing** ⇒ cash to close ≈ **28%** of median. Some appreciation buyers use different leverage — **defaults stay transparent here**. Loan priced at **7.5%** midpoint of the July 2026 about 7.0%–8.5% investor band. Shock = **6** or **9** months PITI. **Total recommended liquid** = cash to close + shock.

| # | State | Down | Cash to close | Shock liquid | Total liquid |
|---:|---|---:|---:|---:|---:|
| 1 | Illinois | 25% | $95k | $23k (9 mo) | $118k |
| 2 | Wisconsin | 25% | $101k | $16k (6 mo) | $117k |
| 3 | Connecticut | 25% | $139k | $33k (9 mo) | $172k |
| 4 | New Jersey | 25% | $162k | $38k (9 mo) | $200k |
| 5 | Pennsylvania | 25% | $92k | $13k (6 mo) | $106k |
| 6 | New York | 25% | $174k | $38k (9 mo) | $211k |
| 7 | Kentucky | 25% | $80k | $12k (6 mo) | $91k |
| 8 | Indiana | 25% | $80k | $12k (6 mo) | $92k |
| 9 | Missouri | 25% | $83k | $12k (6 mo) | $95k |
| 10 | Massachusetts | 25% | $193k | $27k (6 mo) | $219k |
| 11 | North Dakota | 25% | $87k | $13k (6 mo) | $100k |
| 12 | Tennessee | 25% | $116k | $16k (6 mo) | $132k |
| 13 | New Hampshire | 25% | $151k | $21k (6 mo) | $172k |
| 14 | Nebraska | 25% | $89k | $14k (6 mo) | $103k |
| 15 | Vermont | 25% | $126k | $18k (6 mo) | $143k |
| 16 | Ohio | 25% | $79k | $11k (6 mo) | $91k |
| 17 | Idaho | 25% | $141k | $20k (6 mo) | $161k |
| 18 | Iowa | 25% | $72k | $11k (6 mo) | $83k |
| 19 | South Dakota | 25% | $97k | $14k (6 mo) | $111k |
| 20 | Arkansas | 25% | $77k | $11k (6 mo) | $88k |
| 21 | Hawaii | 25% | $208k | $41k (9 mo) | $249k |
| 22 | West Virginia | 25% | $74k | $11k (6 mo) | $85k |
| 23 | Virginia | 25% | $140k | $20k (6 mo) | $159k |
| 24 | Alabama | 25% | $88k | $12k (6 mo) | $99k |
| 25 | Georgia | 25% | $109k | $15k (6 mo) | $124k |
| 26 | Alaska | 25% | $120k | $17k (6 mo) | $136k |
| 27 | Minnesota | 25% | $104k | $15k (6 mo) | $119k |
| 28 | Michigan | 25% | $83k | $12k (6 mo) | $95k |
| 29 | Kansas | 25% | $89k | $13k (6 mo) | $101k |
| 30 | Maine | 25% | $123k | $17k (6 mo) | $140k |
| 31 | Mississippi | 25% | $80k | $19k (9 mo) | $98k |
| 32 | South Carolina | 25% | $110k | $23k (9 mo) | $133k |
| 33 | North Carolina | 25% | $111k | $16k (6 mo) | $127k |
| 34 | Maryland | 25% | $134k | $19k (6 mo) | $152k |
| 35 | Montana | 25% | $148k | $21k (6 mo) | $169k |
| 36 | New Mexico | 25% | $111k | $16k (6 mo) | $126k |
| 37 | Arizona | 25% | $127k | $18k (6 mo) | $145k |
| 38 | Louisiana | 25% | $75k | $17k (9 mo) | $92k |
| 39 | Wyoming | 25% | $130k | $18k (6 mo) | $148k |
| 40 | Nevada | 25% | $135k | $19k (6 mo) | $154k |
| 41 | Delaware | 25% | $108k | $14k (6 mo) | $122k |
| 42 | Oklahoma | 25% | $74k | $18k (9 mo) | $92k |
| 43 | Utah | 25% | $157k | $22k (6 mo) | $179k |
| 44 | Texas | 25% | $100k | $24k (9 mo) | $124k |
| 45 | Oregon | 25% | $147k | $32k (9 mo) | $179k |
| 46 | Florida | 25% | $118k | $27k (9 mo) | $145k |
| 47 | Rhode Island | 25% | $150k | $21k (6 mo) | $171k |
| 48 | Washington | 25% | $183k | $39k (9 mo) | $222k |
| 49 | Colorado | 25% | $173k | $24k (6 mo) | $197k |
| 50 | California | 25% | $248k | $53k (9 mo) | $301k |
| 51 | District of Columbia | 25% | unavailable | unavailable | unavailable |

### Notes on score framing vs the base rental report
[↑ Back to Index](#index)

- **Ohio / Indiana / Arkansas** remain solid markets but **rank lower here** because this lens privileges FHFA + liquidity over day-one yield.
- **Illinois / Connecticut / New Jersey / New York** rise because **appreciation + exit depth** outweigh thin cash-flow scores.
- **Colorado / Washington / California** stay cautious on **near-term** FHFA even when long-run supply narratives remain popular.
- Small high-YoY states (**Alaska, Vermont, North Dakota**) keep strong Appr scores but lose actionable rank on **liquidity / scale**.

### Strict economic-composite buckets
[↑ Back to Index](#index)

| Composite | States |
| --------- | ------ |
| 8.50 | Wisconsin |
| 8.20 | North Dakota |
| 8.00 | Tennessee |
| 7.90 | Indiana, New Hampshire |
| 7.80 | Nebraska |
| 7.70 | Vermont |
| 7.60 | Pennsylvania, Ohio |
| 7.50 | Missouri |
| 7.40 | Idaho, Iowa, South Dakota |
| 7.30 | New Jersey, Arkansas |
| 7.20 | Illinois, Hawaii, West Virginia, Virginia, Alabama |
| 7.10 | New York, Kentucky, Georgia |
| 7.00 | Connecticut |
| 6.90 | Massachusetts, Alaska, Minnesota, Michigan |
| 6.80 | Kansas, Maine, Mississippi |
| 6.70 | South Carolina |
| 6.50 | North Carolina |
| 6.20 | Maryland, Montana |
| 5.90 | New Mexico |
| 5.80 | Arizona, Louisiana, Wyoming |
| 5.60 | Nevada, Delaware, Oklahoma, Utah |
| 5.00 | Texas |
| 4.90 | Oregon, Florida |
| 4.40 | Rhode Island |
| 4.10 | Washington, Colorado |
| 3.80 | California |
| 2.20 | District of Columbia |

---

## 5. City leaderboards
[↑ Back to Index](#index)

Metro screens emphasize **equity path** (FHFA / demand / supply / exit). Cash-flow boards from the base report are **not** copied as primary rankings.

### Appreciation-path metros (FHFA + demand)
[↑ Back to Index](#index)

| Rank | Metro | Evidence | Judgment |
| ---- | ----- | -------- | -------- |
| 1 | Chicago, Illinois | State FHFA +7.3%; deep SFH buyer pool | Top actionable App metro despite tenant-leaning city rules |
| 2 | Milwaukee / Madison, Wisconsin | State FHFA +4.5%; owner-friendly | Strong equity + operable law |
| 3 | Bridgeport–Stamford / Hartford, Connecticut | Metro YoY leaders in base FHFA table; state +4.7% | Northeast rebound; higher taxes |
| 4 | North Jersey / Newark corridor | State FHFA +4.5%; NYC spillover | Equity path; tax drag severe |
| 5 | Syracuse / Rochester / Buffalo, New York | Metro Appr leaders; state +4.4% | Upstate SFH — not NYC boroughs |
| 6 | Lancaster / Reading / Philadelphia, Pennsylvania | Metro YoY leaders; state +3.8% | Liquidity + App; Philly local rules |
| 7 | Louisville / Lexington, Kentucky | State FHFA +4.7%; affordable entry | App with accessible capital |
| 8 | Indianapolis suburbs (Fishers / Carmel) | State +3.6%; strong jobs | App suburbs over pure CF city stock |
| 9 | Boston / Worcester, Massachusetts | Structural supply + incomes; state FHFA +2.2% | Long equity; thin carry; high capital |
| 10 | Raleigh / Charlotte, North Carolina | Jobs/migration leaders; soft near-term FHFA (+0.1%) | Structural App > one-year print |

### Best single-family equity-path metros
[↑ Back to Index](#index)

1. Chicago (selected neighborhoods / inner-ring suburbs)
2. Milwaukee suburbs / Madison
3. Bridgeport–Stamford corridor
4. North Jersey
5. Philadelphia suburbs / Lancaster
6. Buffalo / Rochester / Syracuse
7. Louisville
8. Indianapolis — Fishers / Carmel
9. Boston metro (capital-heavy)
10. Salt Lake City / Provo (migration; softer FHFA)

### Job / migration leaders
[↑ Back to Index](#index)

| Rank | Metro | Evidence |
| ---- | ----- | -------- |
| 1 | Las Vegas, Nevada | +24,500 jobs; +2.1% (May 2026 payroll) |
| 2 | Salt Lake City, Utah | +17,800; +2.1% |
| 3 | San Jose, California | +17,600; +1.5% |
| 4 | Raleigh, North Carolina | +16,700; +2.2% |
| 5 | Greenville, South Carolina | +10,600; +2.2% |
| 6 | Fresno, California | +9,100; +2.0% |
| 7 | Fayetteville–Springdale–Rogers, Arkansas | +7,700; +2.5% |
| 8 | Athens, Georgia | +3,200; +3.0% |

**Weakest confirmed large metros:** Washington–Arlington–Alexandria (−100,500; −3.0%) and Portland–Vancouver–Hillsboro (−35,000; −2.8%).

### Supply-constrained / high-income screens
[↑ Back to Index](#index)

| Metro | Why it matters for equity | Caution |
| ----- | ------------------------- | ------- |
| Boston, MA | Chronic supply constraint; high incomes | Extreme entry capital; thin carry |
| North Jersey / NYC spillover | Buyer pool + land constraint | Taxes + tenant law |
| Honolulu, HI | Island supply constraint | Tourism concentration; insurance; tiny yields |
| Seattle Eastside / Bay Area | Long-run supply stories | Soft near-term FHFA; regulation; concessions |
| Northern Virginia | Federal / cyber / professional demand | Federal cycle risk; high prices |
| Salt Lake / Boise | Migration + young demographics | Near-term FHFA soft / high entry |

### Top suburbs worth researching (appreciation tilt)
[↑ Back to Index](#index)

| Parent metro | Top suburbs / submarkets | Angle | Note |
| ------------ | ------------------------ | ----- | ---- |
| **Chicago, IL** | Naperville, Evanston, Oak Park | App | Tenure / schools; pay for liquidity |
| **Milwaukee, WI** | Wauwatosa, Brookfield | App | Owner-friendly state + App suburbs |
| **Indianapolis, IN** | Fishers, Carmel | App | Higher entry; thinner day-one cash |
| **Kansas City, MO** | Overland Park, Lee’s Summit | App | Vs Independence CF |
| **Dallas–Fort Worth, TX** | Frisco, McKinney, Plano | App | Tax + insurance; supply watch |
| **Phoenix, AZ** | Gilbert, Chandler | App | Prestige premium compresses yield |
| **Raleigh, NC** | Cary, Apex | App/Jobs | Soft statewide FHFA; strong jobs |
| **Salt Lake, UT** | Utah County suburbs | App | Migration; high entry |
| **Boston, MA** | Inner-ring / Worcester corridor | App | Capital-heavy |
| **Philadelphia, PA** | Main Line selected; Lancaster metro | App/Bal | Local rules vary |

### Carry / thin-cash notes (secondary)
[↑ Back to Index](#index)

Appreciation buys often print **weaker gross yields** than Midwest CF leaders. Before bidding:

- Stress **6–9 months** PITI reserves (§4e).
- Assume management about **10%** of rent unless quoted (§9).
- Do not stretch leverage so a soft rent year forces a sale — that destroys the equity thesis.
- For comparative CF boards, see `rental_market_report.md` §5.

---

## 6. All-state deep dives
[↑ Back to Index](#index)

Deep dives for **all 50 states + D.C.** in **appreciation actionable-rank** order. Field labels match the base report, with Cash reframed as carry. [↑ Index](#index) · [A–Z](#az-actionable-rank-index)

### Illinois
[↑ Back to Index](#index)

**Scores:** Jobs 4 / Price 8 / Cash (carry) 4 / Appreciation 10 / Owner law 6 / Tenant law 6

**Prices:** State median **$338k** / typical **$350k** (Redfin All Residential, 2026-05-31). FHFA YoY **+7.3%** (2026Q1). Major metros: Chicago, Peoria, Rockford, Springfield.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$95k**; shock liquid ≈ **$23k (9 mo)**; **total recommended liquid ≈ $118k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 60.7% · Black 13.3% · Hisp 19.0% · Asian 6.0%. Median HH income **$84k** (CPS 2024); mean HH income **$111k**. Price-to-income screen about **4.0x**.
**Top suburbs:** Chicago — Naperville / Evanston / Oak Park (App); Peoria metro for high FHFA YoY screens.

**Why it ranks:** FHFA YoY +7.3%; unemployment 5.1%; median $338k; price-to-income about 4.0x. Appreciation actionable rank **#1** (Econ 7.20).
**Best fit:** **Single-family appreciation hold** in Chicago, Peoria. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; vacant App holds need active monitoring — large-metro LE may treat unauthorized occupancy as civil until paperwork clears.
**Data confidence:** High

### Wisconsin
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 8 / Cash (carry) 5 / Appreciation 10 / Owner law 9 / Tenant law 2

**Prices:** State median **$362k** / typical **$374k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.5%** (2026Q1). Major metros: Milwaukee, Madison, Green Bay.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$101k**; shock liquid ≈ **$16k (6 mo)**; **total recommended liquid ≈ $117k**.
**Top industries:** trade / logistics; education & health; manufacturing; government (BLS CES SAE).
**Demographics / income:** White 79.9% · Black 5.9% · Hisp 8.1% · Asian 3.0%. Median HH income **$83k** (CPS 2024); mean HH income **$98k**. Price-to-income screen about **4.4x**.
**Top suburbs:** Milwaukee — Wauwatosa / Brookfield (App); Madison — Middleton / Fitchburg (App).

**Why it ranks:** FHFA YoY +4.5%; unemployment 3.3%; median $362k; price-to-income about 4.4x. Appreciation actionable rank **#2** (Econ 8.50).
**Best fit:** **Single-family appreciation hold** in Milwaukee, Madison. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Connecticut
[↑ Back to Index](#index)

**Scores:** Jobs 4 / Price 7 / Cash (carry) 4 / Appreciation 10 / Owner law 5 / Tenant law 7

**Prices:** State median **$498k** / typical **$522k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.7%** (2026Q1). Major metros: Hartford, Bridgeport, New Haven.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$139k**; shock liquid ≈ **$33k (9 mo)**; **total recommended liquid ≈ $172k**.
**Top industries:** education & health; trade / logistics; government; professional services (BLS CES SAE).
**Demographics / income:** White 64.5% · Black 10.9% · Hisp 18.6% · Asian 4.9%. Median HH income **$99k** (CPS 2024); mean HH income **$131k**. Price-to-income screen about **5.0x**.
**Top suburbs:** Bridgeport–Stamford suburbs; Hartford inner-ring for lower entry with still-strong YoY.

**Why it ranks:** FHFA YoY +4.7%; unemployment 5.2%; median $498k; price-to-income about 5.0x. Appreciation actionable rank **#3** (Econ 7.00).
**Best fit:** **Single-family appreciation hold** in Hartford, Bridgeport. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated.
**Data confidence:** High

### New Jersey
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 7 / Cash (carry) 1 / Appreciation 10 / Owner law 3 / Tenant law 9

**Prices:** State median **$580k** / typical **$597k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.5%** (2026Q1). Major metros: Newark, Camden, New Brunswick.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$162k**; shock liquid ≈ **$38k (9 mo)**; **total recommended liquid ≈ $200k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 53.5% · Black 12.7% · Hisp 22.7% · Asian 10.2%. Median HH income **$104k** (CPS 2024); mean HH income **$138k**. Price-to-income screen about **5.6x**.
**Top suburbs:** North Jersey NYC-spillover towns; Camden / South Jersey lower entry, thinner App thesis.

**Why it ranks:** FHFA YoY +4.5%; unemployment 4.5%; median $580k; price-to-income about 5.6x; structural supply / demand support. Appreciation actionable rank **#4** (Econ 7.30).
**Best fit:** **Single-family appreciation hold** in Newark / North Jersey. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds.
**Data confidence:** High

### Pennsylvania
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 8 / Cash (carry) 6 / Appreciation 9 / Owner law 7 / Tenant law 4

**Prices:** State median **$330k** / typical **$345k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.8%** (2026Q1). Major metros: Pittsburgh, Philadelphia, Lancaster.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$92k**; shock liquid ≈ **$13k (6 mo)**; **total recommended liquid ≈ $106k**.
**Top industries:** education & health; trade / logistics; professional services; government (BLS CES SAE).
**Demographics / income:** White 74.0% · Black 10.6% · Hisp 8.9% · Asian 3.9%. Median HH income **$80k** (CPS 2024); mean HH income **$103k**. Price-to-income screen about **4.1x**.
**Top suburbs:** Lancaster / Reading (App YoY leaders); Philly Main Line vs Pittsburgh suburbs split.

**Why it ranks:** FHFA YoY +3.8%; unemployment 4.1%; median $330k; price-to-income about 4.1x. Appreciation actionable rank **#5** (Econ 7.60).
**Best fit:** **Single-family appreciation hold** in Philadelphia, Pittsburgh, Lancaster. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### New York
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 7 / Cash (carry) 2 / Appreciation 10 / Owner law 1 / Tenant law 10

**Prices:** State median **$620k** / typical **$639k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.4%** (2026Q1). Major metros: New York City, Buffalo, Rochester, Syracuse.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$174k**; shock liquid ≈ **$38k (9 mo)**; **total recommended liquid ≈ $211k**.
**Top industries:** education & health; government; trade / logistics; professional services (BLS CES SAE).
**Demographics / income:** White 55.1% · Black 14.3% · Hisp 19.8% · Asian 9.1%. Median HH income **$87k** (CPS 2024); mean HH income **$122k**. Price-to-income screen about **7.1x**.
**Top suburbs:** Buffalo / Rochester / Syracuse suburbs (App); avoid treating NYC boroughs as same buy box.

**Why it ranks:** FHFA YoY +4.4%; unemployment 4.6%; median $620k; price-to-income about 7.1x. Appreciation actionable rank **#6** (Econ 7.10).
**Best fit:** **Single-family appreciation hold** in Buffalo, Rochester, Syracuse (upstate focus). Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds.
**Data confidence:** High

### Kentucky
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 7 / Cash (carry) 6 / Appreciation 9 / Owner law 8 / Tenant law 3

**Prices:** State median **$284k** / typical **$312k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.7%** (2026Q1). Major metros: Louisville, Lexington.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$80k**; shock liquid ≈ **$12k (6 mo)**; **total recommended liquid ≈ $91k**.
**Top industries:** trade / logistics; education & health; government; manufacturing (BLS CES SAE).
**Demographics / income:** White 82.5% · Black 7.5% · Hisp 4.9% · Asian 1.4%. Median HH income **$65k** (CPS 2024); mean HH income **$83k**. Price-to-income screen about **4.4x**.
**Top suburbs:** Louisville East End / Lexington suburbs (App/Bal).

**Why it ranks:** FHFA YoY +4.7%; unemployment 4.7%; median $284k; price-to-income about 4.4x. Appreciation actionable rank **#7** (Econ 7.10).
**Best fit:** **Single-family appreciation hold** in Louisville, Lexington. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Indiana
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 8 / Cash (carry) 7 / Appreciation 8 / Owner law 9 / Tenant law 2

**Prices:** State median **$287k** / typical **$297k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.6%** (2026Q1). Major metros: Indianapolis, Fort Wayne, South Bend.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$80k**; shock liquid ≈ **$12k (6 mo)**; **total recommended liquid ≈ $92k**.
**Top industries:** trade / logistics; education & health; manufacturing; government (BLS CES SAE).
**Demographics / income:** White 76.7% · Black 9.0% · Hisp 8.7% · Asian 2.7%. Median HH income **$77k** (CPS 2024); mean HH income **$92k**. Price-to-income screen about **3.7x**.
**Top suburbs:** Fishers / Carmel (App); Noblesville / Greenwood (Bal).

**Why it ranks:** FHFA YoY +3.6%; unemployment 3.3%; median $287k; price-to-income about 3.7x. Appreciation actionable rank **#8** (Econ 7.90).
**Best fit:** **Single-family appreciation hold** in Indianapolis, Fort Wayne. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Missouri
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 8 / Cash (carry) 6 / Appreciation 8 / Owner law 8 / Tenant law 3

**Prices:** State median **$298k** / typical **$300k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.9%** (2026Q1). Major metros: Kansas City, St. Louis, Springfield.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$83k**; shock liquid ≈ **$12k (6 mo)**; **total recommended liquid ≈ $95k**.
**Top industries:** trade / logistics; education & health; government; professional services (BLS CES SAE).
**Demographics / income:** White 77.8% · Black 10.8% · Hisp 5.2% · Asian 2.1%. Median HH income **$78k** (CPS 2024); mean HH income **$93k**. Price-to-income screen about **3.8x**.
**Top suburbs:** Overland Park / Lee’s Summit (App); Independence more CF.

**Why it ranks:** FHFA YoY +3.9%; unemployment 3.7%; median $298k; price-to-income about 3.8x. Appreciation actionable rank **#9** (Econ 7.50).
**Best fit:** **Single-family appreciation hold** in Kansas City, St. Louis. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Massachusetts
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 7 / Cash (carry) 1 / Appreciation 9 / Owner law 6 / Tenant law 6

**Prices:** State median **$688k** / typical **$719k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.2%** (2026Q1). Major metros: Boston, Worcester, Springfield.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$193k**; shock liquid ≈ **$27k (6 mo)**; **total recommended liquid ≈ $219k**.
**Top industries:** education & health; professional services; trade / logistics; government (BLS CES SAE).
**Demographics / income:** White 67.9% · Black 7.0% · Hisp 13.5% · Asian 7.4%. Median HH income **$114k** (CPS 2024); mean HH income **$139k**. Price-to-income screen about **6.0x**.
**Top suburbs:** Boston inner-ring / Worcester corridor (App, high entry).

**Why it ranks:** FHFA YoY +2.2%; unemployment 4.4%; median $688k; price-to-income about 6.0x; structural supply / demand support. Appreciation actionable rank **#10** (Econ 6.90).
**Best fit:** **Single-family appreciation hold** in Boston, Worcester. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** vacant App holds need active monitoring — large-metro LE may treat unauthorized occupancy as civil until paperwork clears.
**Data confidence:** High

### North Dakota
[↑ Back to Index](#index)

**Scores:** Jobs 10 / Price 6 / Cash (carry) 4 / Appreciation 9 / Owner law 8 / Tenant law 3

**Prices:** State median **$311k** / typical **$331k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.0%** (2026Q1). Major metros: Fargo, Bismarck.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$87k**; shock liquid ≈ **$13k (6 mo)**; **total recommended liquid ≈ $100k**.
**Top industries:** trade / logistics; government; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 82.5% · Black 3.1% · Hisp 4.9% · Asian 1.5%. Median HH income **$88k** (CPS 2024); mean HH income **$98k**. Price-to-income screen about **3.5x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +4.0%; unemployment 2.3%; median $311k; price-to-income about 3.5x. Appreciation actionable rank **#11** (Econ 8.20).
**Best fit:** **Single-family appreciation hold** in Fargo, Bismarck. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; scale / remote-ops depth limited.
**Data confidence:** Medium

### Tennessee
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 8 / Cash (carry) 5 / Appreciation 8 / Owner law 9 / Tenant law 2

**Prices:** State median **$413k** / typical **$440k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.2%** (2026Q1). Major metros: Memphis, Nashville, Knoxville, Chattanooga.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$116k**; shock liquid ≈ **$16k (6 mo)**; **total recommended liquid ≈ $132k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 72.3% · Black 15.3% · Hisp 7.5% · Asian 1.8%. Median HH income **$76k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **5.4x**.
**Top suburbs:** Nashville suburbs (App); Memphis more CF.

**Why it ranks:** FHFA YoY +2.2%; unemployment 3.5%; median $413k; price-to-income about 5.4x. Appreciation actionable rank **#12** (Econ 8.00).
**Best fit:** **Single-family appreciation hold** in Nashville, Knoxville, Memphis. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### New Hampshire
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 7 / Cash (carry) 2 / Appreciation 9 / Owner law 5 / Tenant law 7

**Prices:** State median **$538k** / typical **$564k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.3%** (2026Q1). Major metros: Manchester–Nashua.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$151k**; shock liquid ≈ **$21k (6 mo)**; **total recommended liquid ≈ $172k**.
**Top industries:** trade / logistics; education & health; professional services; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 87.5% · Black 1.5% · Hisp 4.7% · Asian 2.6%. Median HH income **$112k** (CPS 2024); mean HH income **$124k**. Price-to-income screen about **4.8x**.
**Top suburbs:** Manchester–Nashua / Seacoast Boston spillover.

**Why it ranks:** FHFA YoY +3.3%; unemployment 2.9%; median $538k; price-to-income about 4.8x. Appreciation actionable rank **#13** (Econ 7.90).
**Best fit:** **Single-family appreciation hold** in Manchester–Nashua. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** High

### Nebraska
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 7 / Cash (carry) 5 / Appreciation 8 / Owner law 7 / Tenant law 3

**Prices:** State median **$319k** / typical **$328k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.9%** (2026Q1). Major metros: Omaha, Lincoln.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$89k**; shock liquid ≈ **$14k (6 mo)**; **total recommended liquid ≈ $103k**.
**Top industries:** trade / logistics; government; education & health; professional services (BLS CES SAE).
**Demographics / income:** White 77.7% · Black 4.6% · Hisp 12.9% · Asian 2.5%. Median HH income **$86k** (CPS 2024); mean HH income **$101k**. Price-to-income screen about **3.7x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +3.9%; unemployment 2.9%; median $319k; price-to-income about 3.7x. Appreciation actionable rank **#14** (Econ 7.80).
**Best fit:** **Single-family appreciation hold** in Omaha, Lincoln. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Vermont
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 6 / Cash (carry) 2 / Appreciation 9 / Owner law 4 / Tenant law 8

**Prices:** State median **$448k** / typical **$486k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.9%** (2026Q1). Major metros: Burlington.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$126k**; shock liquid ≈ **$18k (6 mo)**; **total recommended liquid ≈ $143k**.
**Top industries:** education & health; government; trade / logistics; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 89.9% · Black 1.2% · Hisp 2.5% · Asian 1.7%. Median HH income **$85k** (CPS 2024); mean HH income **$106k**. Price-to-income screen about **5.3x**.
**Top suburbs:** Burlington / Chittenden County — thin inventory.

**Why it ranks:** FHFA YoY +4.9%; unemployment 2.6%; median $448k; price-to-income about 5.3x. Appreciation actionable rank **#15** (Econ 7.70).
**Best fit:** **Single-family appreciation hold** in Burlington. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; scale / remote-ops depth limited.
**Data confidence:** Medium

### Ohio
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 8 / Cash (carry) 7 / Appreciation 8 / Owner law 9 / Tenant law 2

**Prices:** State median **$283k** / typical **$293k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.2%** (2026Q1). Major metros: Cleveland, Columbus, Cincinnati, Dayton.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$79k**; shock liquid ≈ **$11k (6 mo)**; **total recommended liquid ≈ $91k**.
**Top industries:** trade / logistics; education & health; government; professional services (BLS CES SAE).
**Demographics / income:** White 76.6% · Black 11.9% · Hisp 4.8% · Asian 2.6%. Median HH income **$81k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **3.5x**.
**Top suburbs:** Columbus New Albany / Hilliard (App); Cleveland still more CF.

**Why it ranks:** FHFA YoY +3.2%; unemployment 3.6%; median $283k; price-to-income about 3.5x. Appreciation actionable rank **#16** (Econ 7.60).
**Best fit:** **Single-family appreciation hold** in Columbus, Cincinnati, Cleveland. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Idaho
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 6 / Cash (carry) 2 / Appreciation 9 / Owner law 10 / Tenant law 1

**Prices:** State median **$503k** / typical **$577k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.8%** (2026Q1). Major metros: Boise, Idaho Falls, Coeur d’Alene.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$141k**; shock liquid ≈ **$20k (6 mo)**; **total recommended liquid ≈ $161k**.
**Top industries:** trade / logistics; education & health; government; professional services (BLS CES SAE).
**Demographics / income:** White 81.7% · Black 0.8% · Hisp 13.8% · Asian 1.4%. Median HH income **$82k** (CPS 2024); mean HH income **$99k**. Price-to-income screen about **6.2x**.
**Top suburbs:** Boise Treasure Valley suburbs (App/migration).

**Why it ranks:** FHFA YoY +2.8%; unemployment 3.7%; median $503k; price-to-income about 6.2x; structural supply / demand support. Appreciation actionable rank **#17** (Econ 7.40).
**Best fit:** **Single-family appreciation hold** in Boise. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Iowa
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 6 / Cash (carry) 6 / Appreciation 8 / Owner law 9 / Tenant law 2

**Prices:** State median **$259k** / typical **$274k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.5%** (2026Q1). Major metros: Des Moines, Cedar Rapids, Iowa City.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$72k**; shock liquid ≈ **$11k (6 mo)**; **total recommended liquid ≈ $83k**.
**Top industries:** trade / logistics; government; education & health; manufacturing (BLS CES SAE).
**Demographics / income:** White 84.2% · Black 4.0% · Hisp 7.3% · Asian 2.4%. Median HH income **$85k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **3.0x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +3.5%; unemployment 3.2%; median $259k; price-to-income about 3.0x. Appreciation actionable rank **#18** (Econ 7.40).
**Best fit:** **Single-family appreciation hold** in Des Moines, Cedar Rapids. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### South Dakota
[↑ Back to Index](#index)

**Scores:** Jobs 10 / Price 6 / Cash (carry) 4 / Appreciation 7 / Owner law 8 / Tenant law 3

**Prices:** State median **$347k** / typical **$368k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.8%** (2026Q1). Major metros: Sioux Falls, Rapid City.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$97k**; shock liquid ≈ **$14k (6 mo)**; **total recommended liquid ≈ $111k**.
**Top industries:** trade / logistics; government; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 80.5% · Black 2.5% · Hisp 5.1% · Asian 1.5%. Median HH income **$80k** (CPS 2024); mean HH income **$97k**. Price-to-income screen about **4.3x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.8%; unemployment 2.0%; median $347k; price-to-income about 4.3x. Appreciation actionable rank **#19** (Econ 7.40).
**Best fit:** **Single-family appreciation hold** in Sioux Falls. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** Medium

### Arkansas
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 7 / Cash (carry) 6 / Appreciation 8 / Owner law 9 / Tenant law 2

**Prices:** State median **$276k** / typical **$306k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.4%** (2026Q1). Major metros: Fayetteville–Springdale, Little Rock.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$77k**; shock liquid ≈ **$11k (6 mo)**; **total recommended liquid ≈ $88k**.
**Top industries:** trade / logistics; education & health; government; professional services (BLS CES SAE).
**Demographics / income:** White 68.9% · Black 14.4% · Hisp 9.1% · Asian 1.7%. Median HH income **$65k** (CPS 2024); mean HH income **$81k**. Price-to-income screen about **4.2x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +3.4%; unemployment 4.1%; median $276k; price-to-income about 4.2x. Appreciation actionable rank **#20** (Econ 7.30).
**Best fit:** **Single-family appreciation hold** in Northwest Arkansas, Little Rock. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Hawaii
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 4 / Cash (carry) 1 / Appreciation 9 / Owner law 7 / Tenant law 4

**Prices:** State median **$741k** / typical **$780k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.2%** (2026Q1). Major metros: Honolulu.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$208k**; shock liquid ≈ **$41k (9 mo)**; **total recommended liquid ≈ $249k**.
**Top industries:** government; leisure / hospitality; trade / logistics; education & health (BLS CES SAE).
**Demographics / income:** White 21.9% · Black 1.7% · Hisp 10.1% · Asian 36.7%. Median HH income **$98k** (CPS 2024); mean HH income **$125k**. Price-to-income screen about **7.5x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.2%; unemployment 2.6%; median $741k; price-to-income about 7.5x; structural supply / demand support. Appreciation actionable rank **#21** (Econ 7.20).
**Best fit:** **Single-family appreciation hold** in Honolulu. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; insurance / tax / regulation shock reserves elevated.
**Data confidence:** High

### West Virginia
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 6 / Cash (carry) 6 / Appreciation 9 / Owner law 9 / Tenant law 2

**Prices:** State median **$265k** / typical **$273k** (Redfin All Residential, 2026-05-31). FHFA YoY **+4.0%** (2026Q1). Major metros: Charleston, Huntington, Morgantown.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$74k**; shock liquid ≈ **$11k (6 mo)**; **total recommended liquid ≈ $85k**.
**Top industries:** education & health; government; trade / logistics; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 90.1% · Black 3.2% · Hisp 2.1% · Asian 0.7%. Median HH income **$63k** (CPS 2024); mean HH income **$77k**. Price-to-income screen about **4.2x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +4.0%; unemployment 4.2%; median $265k; price-to-income about 4.2x. Appreciation actionable rank **#22** (Econ 7.20).
**Best fit:** **Single-family appreciation hold** in Charleston, Morgantown. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; scale / remote-ops depth limited.
**Data confidence:** Medium

### Virginia
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 8 / Cash (carry) 3 / Appreciation 8 / Owner law 8 / Tenant law 3

**Prices:** State median **$499k** / typical **$502k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.4%** (2026Q1). Major metros: Richmond, Virginia Beach, Northern Virginia.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$140k**; shock liquid ≈ **$20k (6 mo)**; **total recommended liquid ≈ $159k**.
**Top industries:** professional services; government; trade / logistics; education & health (BLS CES SAE).
**Demographics / income:** White 59.8% · Black 18.4% · Hisp 11.1% · Asian 6.9%. Median HH income **$98k** (CPS 2024); mean HH income **$123k**. Price-to-income screen about **5.1x**.
**Top suburbs:** Northern Virginia (App/jobs); Richmond more balanced.

**Why it ranks:** FHFA YoY +2.4%; unemployment 3.7%; median $499k; price-to-income about 5.1x. Appreciation actionable rank **#23** (Econ 7.20).
**Best fit:** **Single-family appreciation hold** in Northern Virginia, Richmond. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Alabama
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 7 / Cash (carry) 6 / Appreciation 7 / Owner law 9 / Tenant law 2

**Prices:** State median **$313k** / typical **$326k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.4%** (2026Q1). Major metros: Birmingham, Huntsville, Mobile.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$88k**; shock liquid ≈ **$12k (6 mo)**; **total recommended liquid ≈ $99k**.
**Top industries:** government; trade / logistics; manufacturing; professional services (BLS CES SAE).
**Demographics / income:** White 64.7% · Black 25.4% · Hisp 5.7% · Asian 1.5%. Median HH income **$66k** (CPS 2024); mean HH income **$86k**. Price-to-income screen about **4.8x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.4%; unemployment 3.2%; median $313k; price-to-income about 4.8x. Appreciation actionable rank **#24** (Econ 7.20).
**Best fit:** **Single-family appreciation hold** in Birmingham, Huntsville. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Georgia
[↑ Back to Index](#index)

**Scores:** Jobs 9 / Price 8 / Cash (carry) 4 / Appreciation 6 / Owner law 9 / Tenant law 2

**Prices:** State median **$389k** / typical **$414k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.1%** (2026Q1). Major metros: Atlanta, Athens, Augusta, Savannah.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$109k**; shock liquid ≈ **$15k (6 mo)**; **total recommended liquid ≈ $124k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 50.3% · Black 30.8% · Hisp 11.1% · Asian 4.5%. Median HH income **$81k** (CPS 2024); mean HH income **$103k**. Price-to-income screen about **4.8x**.
**Top suburbs:** North Atlanta job-pocket suburbs; Athens growth sibling.

**Why it ranks:** FHFA YoY +0.1%; unemployment 3.4%; median $389k; price-to-income about 4.8x. Appreciation actionable rank **#25** (Econ 7.10).
**Best fit:** **Single-family appreciation hold** in Atlanta, Athens. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Alaska
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 6 / Cash (carry) 3 / Appreciation 9 / Owner law 8 / Tenant law 3

**Prices:** State median **$427k** / typical **$448k** (Redfin All Residential, 2026-05-31). FHFA YoY **+5.5%** (2026Q1). Major metros: Anchorage, Fairbanks.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$120k**; shock liquid ≈ **$17k (6 mo)**; **total recommended liquid ≈ $136k**.
**Top industries:** government; trade / logistics; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 59.6% · Black 2.9% · Hisp 7.5% · Asian 5.9%. Median HH income **$91k** (CPS 2024); mean HH income **$114k**. Price-to-income screen about **4.7x**.
**Top suburbs:** Anchorage neighborhoods — thin suburb inventory.

**Why it ranks:** FHFA YoY +5.5%; unemployment 4.4%; median $427k; price-to-income about 4.7x. Appreciation actionable rank **#26** (Econ 6.90).
**Best fit:** **Single-family appreciation hold** in Anchorage. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; scale / remote-ops depth limited.
**Data confidence:** Medium

### Minnesota
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 8 / Cash (carry) 3 / Appreciation 8 / Owner law 6 / Tenant law 6

**Prices:** State median **$372k** / typical **$396k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.8%** (2026Q1). Major metros: Minneapolis–St. Paul, Duluth, Rochester.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$104k**; shock liquid ≈ **$15k (6 mo)**; **total recommended liquid ≈ $119k**.
**Top industries:** education & health; trade / logistics; government; professional services (BLS CES SAE).
**Demographics / income:** White 76.7% · Black 7.2% · Hisp 6.4% · Asian 5.2%. Median HH income **$92k** (CPS 2024); mean HH income **$113k**. Price-to-income screen about **4.0x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.8%; unemployment 4.4%; median $372k; price-to-income about 4.0x. Appreciation actionable rank **#27** (Econ 6.90).
**Best fit:** **Single-family appreciation hold** in Minneapolis–St. Paul. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Michigan
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 8 / Cash (carry) 6 / Appreciation 8 / Owner law 8 / Tenant law 3

**Prices:** State median **$298k** / typical **$314k** (Redfin All Residential, 2026-05-31). FHFA YoY **+3.2%** (2026Q1). Major metros: Detroit, Grand Rapids, Lansing, Flint.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$83k**; shock liquid ≈ **$12k (6 mo)**; **total recommended liquid ≈ $95k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 73.8% · Black 13.2% · Hisp 6.0% · Asian 3.4%. Median HH income **$79k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **3.7x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +3.2%; unemployment 5.0%; median $298k; price-to-income about 3.7x. Appreciation actionable rank **#28** (Econ 6.90).
**Best fit:** **Single-family appreciation hold** in Detroit, Grand Rapids. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Kansas
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 7 / Cash (carry) 5 / Appreciation 7 / Owner law 8 / Tenant law 3

**Prices:** State median **$316k** / typical **$319k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.5%** (2026Q1). Major metros: Wichita, Kansas City–KS, Topeka.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$89k**; shock liquid ≈ **$13k (6 mo)**; **total recommended liquid ≈ $101k**.
**Top industries:** trade / logistics; government; education & health; manufacturing (BLS CES SAE).
**Demographics / income:** White 75.9% · Black 5.3% · Hisp 13.7% · Asian 2.6%. Median HH income **$88k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **3.6x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.5%; unemployment 3.8%; median $316k; price-to-income about 3.6x. Appreciation actionable rank **#29** (Econ 6.80).
**Best fit:** **Single-family appreciation hold** in Wichita, Kansas City–KS. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Maine
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 7 / Cash (carry) 2 / Appreciation 7 / Owner law 5 / Tenant law 7

**Prices:** State median **$439k** / typical **$464k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.4%** (2026Q1). Major metros: Portland, Bangor.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$123k**; shock liquid ≈ **$17k (6 mo)**; **total recommended liquid ≈ $140k**.
**Top industries:** education & health; trade / logistics; government; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 90.1% · Black 1.8% · Hisp 2.2% · Asian 1.1%. Median HH income **$91k** (CPS 2024); mean HH income **$97k**. Price-to-income screen about **4.8x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.4%; unemployment 3.1%; median $439k; price-to-income about 4.8x. Appreciation actionable rank **#30** (Econ 6.80).
**Best fit:** **Single-family appreciation hold** in Portland. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** High

### Mississippi
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 7 / Cash (carry) 5 / Appreciation 7 / Owner law 9 / Tenant law 2

**Prices:** State median **$284k** / typical **$287k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.1%** (2026Q1). Major metros: Jackson, Gulfport, Hattiesburg.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$80k**; shock liquid ≈ **$19k (9 mo)**; **total recommended liquid ≈ $98k**.
**Top industries:** trade / logistics; government; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 55.6% · Black 35.6% · Hisp 3.7% · Asian 0.9%. Median HH income **$56k** (CPS 2024); mean HH income **$76k**. Price-to-income screen about **5.1x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.1%; unemployment 3.8%; median $284k; price-to-income about 5.1x. Appreciation actionable rank **#31** (Econ 6.80).
**Best fit:** **Single-family appreciation hold** in Jackson, Gulfport. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; insurance / tax / regulation shock reserves elevated; anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### South Carolina
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 7 / Cash (carry) 4 / Appreciation 7 / Owner law 9 / Tenant law 2

**Prices:** State median **$394k** / typical **$410k** (Redfin All Residential, 2026-05-31). FHFA YoY **+1.5%** (2026Q1). Major metros: Greenville, Columbia, Charleston.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$110k**; shock liquid ≈ **$23k (9 mo)**; **total recommended liquid ≈ $133k**.
**Top industries:** trade / logistics; government; education & health; professional services (BLS CES SAE).
**Demographics / income:** White 63.6% · Black 24.4% · Hisp 7.4% · Asian 1.8%. Median HH income **$77k** (CPS 2024); mean HH income **$93k**. Price-to-income screen about **5.1x**.
**Top suburbs:** Greenville / Charleston suburbs (migration).

**Why it ranks:** FHFA YoY +1.5%; unemployment 4.4%; median $394k; price-to-income about 5.1x. Appreciation actionable rank **#32** (Econ 6.70).
**Best fit:** **Single-family appreciation hold** in Greenville, Charleston. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### North Carolina
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 7 / Cash (carry) 3 / Appreciation 6 / Owner law 8 / Tenant law 3

**Prices:** State median **$398k** / typical **$427k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.1%** (2026Q1). Major metros: Raleigh, Charlotte, Greensboro.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$111k**; shock liquid ≈ **$16k (6 mo)**; **total recommended liquid ≈ $127k**.
**Top industries:** trade / logistics; government; professional services; education & health (BLS CES SAE).
**Demographics / income:** White 61.4% · Black 20.1% · Hisp 11.4% · Asian 3.3%. Median HH income **$67k** (CPS 2024); mean HH income **$98k**. Price-to-income screen about **5.9x**.
**Top suburbs:** Raleigh / Cary / Apex (App/jobs); Charlotte south suburbs.

**Why it ranks:** FHFA YoY +0.1%; unemployment 3.6%; median $398k; price-to-income about 5.9x; structural supply / demand support. Appreciation actionable rank **#33** (Econ 6.50).
**Best fit:** **Single-family appreciation hold** in Raleigh, Charlotte. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Maryland
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 8 / Cash (carry) 4 / Appreciation 6 / Owner law 5 / Tenant law 7

**Prices:** State median **$477k** / typical **$477k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.6%** (2026Q1). Major metros: Baltimore, Montgomery / Prince George’s.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$134k**; shock liquid ≈ **$19k (6 mo)**; **total recommended liquid ≈ $152k**.
**Top industries:** government; education & health; professional services; trade / logistics (BLS CES SAE).
**Demographics / income:** White 47.9% · Black 29.2% · Hisp 12.6% · Asian 6.6%. Median HH income **$110k** (CPS 2024); mean HH income **$129k**. Price-to-income screen about **4.4x**.
**Top suburbs:** Montgomery / Howard County (App); Baltimore city more CF/ops.

**Why it ranks:** FHFA YoY +0.6%; unemployment 4.3%; median $477k; price-to-income about 4.4x. Appreciation actionable rank **#34** (Econ 6.20).
**Best fit:** **Single-family appreciation hold** in Baltimore. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Montana
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 6 / Cash (carry) 2 / Appreciation 6 / Owner law 9 / Tenant law 2

**Prices:** State median **$529k** / typical **$620k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.2%** (2026Q1). Major metros: Billings, Missoula, Bozeman.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$148k**; shock liquid ≈ **$21k (6 mo)**; **total recommended liquid ≈ $169k**.
**Top industries:** trade / logistics; government; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 84.6% · Black 0.4% · Hisp 4.6% · Asian 0.8%. Median HH income **$82k** (CPS 2024); mean HH income **$94k**. Price-to-income screen about **6.5x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +0.2%; unemployment 3.3%; median $529k; price-to-income about 6.5x. Appreciation actionable rank **#35** (Econ 6.20).
**Best fit:** **Single-family appreciation hold** in Billings, Bozeman. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** Medium

### New Mexico
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 6 / Cash (carry) 4 / Appreciation 7 / Owner law 8 / Tenant law 3

**Prices:** State median **$396k** / typical **$446k** (Redfin All Residential, 2026-05-31). FHFA YoY **+2.2%** (2026Q1). Major metros: Albuquerque, Santa Fe, Las Cruces.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$111k**; shock liquid ≈ **$16k (6 mo)**; **total recommended liquid ≈ $126k**.
**Top industries:** government; education & health; trade / logistics; professional services (BLS CES SAE).
**Demographics / income:** White 47.5% · Black 2.0% · Hisp 48.6% · Asian 1.8%. Median HH income **$64k** (CPS 2024); mean HH income **$86k**. Price-to-income screen about **6.2x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +2.2%; unemployment 4.8%; median $396k; price-to-income about 6.2x. Appreciation actionable rank **#36** (Econ 5.90).
**Best fit:** **Single-family appreciation hold** in Albuquerque, Santa Fe. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** High

### Arizona
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 8 / Cash (carry) 3 / Appreciation 6 / Owner law 9 / Tenant law 2

**Prices:** State median **$454k** / typical **$473k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.2%** (2026Q1). Major metros: Phoenix metro (Tempe, Gilbert, Chandler), Tucson.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$127k**; shock liquid ≈ **$18k (6 mo)**; **total recommended liquid ≈ $145k**.
**Top industries:** trade / logistics; education & health; professional services; government (BLS CES SAE).
**Demographics / income:** White 58.3% · Black 4.8% · Hisp 31.6% · Asian 3.6%. Median HH income **$85k** (CPS 2024); mean HH income **$105k**. Price-to-income screen about **5.4x**.
**Top suburbs:** Gilbert / Chandler (App); West Valley more CF.

**Why it ranks:** FHFA YoY +0.2%; unemployment 4.9%; median $454k; price-to-income about 5.4x. Appreciation actionable rank **#37** (Econ 5.80).
**Best fit:** **Single-family appreciation hold** in Phoenix, Tucson. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Louisiana
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 7 / Cash (carry) 2 / Appreciation 6 / Owner law 9 / Tenant law 2

**Prices:** State median **$269k** / typical **$276k** (Redfin All Residential, 2026-05-31). FHFA YoY **+1.3%** (2026Q1). Major metros: New Orleans, Baton Rouge, Lafayette.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$75k**; shock liquid ≈ **$17k (9 mo)**; **total recommended liquid ≈ $92k**.
**Top industries:** trade / logistics; education & health; government; professional services (BLS CES SAE).
**Demographics / income:** White 56.7% · Black 30.3% · Hisp 7.1% · Asian 1.8%. Median HH income **$61k** (CPS 2024); mean HH income **$83k**. Price-to-income screen about **4.4x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +1.3%; unemployment 4.4%; median $269k; price-to-income about 4.4x. Appreciation actionable rank **#38** (Econ 5.80).
**Best fit:** **Single-family appreciation hold** in New Orleans, Baton Rouge. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated.
**Data confidence:** High

### Wyoming
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 5 / Cash (carry) 4 / Appreciation 5 / Owner law 9 / Tenant law 2

**Prices:** State median **$464k** / typical **$647k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.0%** (2026Q1). Major metros: Cheyenne, Casper.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$130k**; shock liquid ≈ **$18k (6 mo)**; **total recommended liquid ≈ $148k**.
**Top industries:** government; trade / logistics; leisure / hospitality; education & health (BLS CES SAE).
**Demographics / income:** White 84.3% · Black 0.7% · Hisp 10.8% · Asian 0.9%. Median HH income **$79k** (CPS 2024); mean HH income **$93k**. Price-to-income screen about **5.9x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY -0.0%; unemployment 3.2%; median $464k; price-to-income about 5.9x. Appreciation actionable rank **#39** (Econ 5.80).
**Best fit:** **Single-family appreciation hold** in Cheyenne. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; scale / remote-ops depth limited.
**Data confidence:** Medium

### Nevada
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 7 / Cash (carry) 3 / Appreciation 6 / Owner law 8 / Tenant law 3

**Prices:** State median **$481k** / typical **$506k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.7%** (2026Q1). Major metros: Las Vegas, Reno.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$135k**; shock liquid ≈ **$19k (6 mo)**; **total recommended liquid ≈ $154k**.
**Top industries:** leisure / hospitality; trade / logistics; professional services; education & health (BLS CES SAE).
**Demographics / income:** White 49.8% · Black 9.4% · Hisp 29.9% · Asian 9.1%. Median HH income **$81k** (CPS 2024); mean HH income **$103k**. Price-to-income screen about **6.0x**.
**Top suburbs:** Las Vegas suburbs (jobs + tourism concentration).

**Why it ranks:** FHFA YoY +0.7%; unemployment 5.1%; median $481k; price-to-income about 6.0x. Appreciation actionable rank **#40** (Econ 5.60).
**Best fit:** **Single-family appreciation hold** in Las Vegas, Reno. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy.
**Data confidence:** High

### Delaware
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 7 / Cash (carry) 3 / Appreciation 6 / Owner law 8 / Tenant law 3

**Prices:** State median **$384k** / typical **$408k** (Redfin All Residential, 2026-05-31). FHFA YoY **+1.0%** (2026Q1). Major metros: Wilmington, Dover.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$108k**; shock liquid ≈ **$14k (6 mo)**; **total recommended liquid ≈ $122k**.
**Top industries:** education & health; trade / logistics; government; professional services (BLS CES SAE).
**Demographics / income:** White 59.3% · Black 22.5% · Hisp 11.1% · Asian 4.3%. Median HH income **$86k** (CPS 2024); mean HH income **$109k**. Price-to-income screen about **4.5x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +1.0%; unemployment 4.9%; median $384k; price-to-income about 4.5x. Appreciation actionable rank **#41** (Econ 5.60).
**Best fit:** **Single-family appreciation hold** in Wilmington. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool.
**Data confidence:** High

### Oklahoma
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 7 / Cash (carry) 4 / Appreciation 5 / Owner law 9 / Tenant law 2

**Prices:** State median **$265k** / typical **$285k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.2%** (2026Q1). Major metros: Oklahoma City, Tulsa.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$74k**; shock liquid ≈ **$18k (9 mo)**; **total recommended liquid ≈ $92k**.
**Top industries:** government; trade / logistics; education & health; professional services (BLS CES SAE).
**Demographics / income:** White 64.6% · Black 6.8% · Hisp 12.9% · Asian 2.3%. Median HH income **$65k** (CPS 2024); mean HH income **$86k**. Price-to-income screen about **4.1x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +0.2%; unemployment 4.2%; median $265k; price-to-income about 4.1x. Appreciation actionable rank **#42** (Econ 5.60).
**Best fit:** **Single-family appreciation hold** in Oklahoma City, Tulsa. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated.
**Data confidence:** High

### Utah
[↑ Back to Index](#index)

**Scores:** Jobs 8 / Price 7 / Cash (carry) 2 / Appreciation 4 / Owner law 10 / Tenant law 1

**Prices:** State median **$560k** / typical **$619k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.1%** (2026Q1). Major metros: Salt Lake City, Provo, Ogden.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$157k**; shock liquid ≈ **$22k (6 mo)**; **total recommended liquid ≈ $179k**.
**Top industries:** trade / logistics; government; professional services; education & health (BLS CES SAE).
**Demographics / income:** White 78.6% · Black 1.1% · Hisp 16.0% · Asian 2.5%. Median HH income **$104k** (CPS 2024); mean HH income **$118k**. Price-to-income screen about **5.4x**.
**Top suburbs:** Salt Lake / Utah County suburbs (App, high entry).

**Why it ranks:** FHFA YoY -0.1%; unemployment 3.6%; median $560k; price-to-income about 5.4x; structural supply / demand support. Appreciation actionable rank **#43** (Econ 5.60).
**Best fit:** **Single-family appreciation hold** in Salt Lake City, Provo. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** High

### Texas
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 9 / Cash (carry) 3 / Appreciation 2 / Owner law 9 / Tenant law 2

**Prices:** State median **$356k** / typical **$378k** (Redfin All Residential, 2026-05-31). FHFA YoY **-1.6%** (2026Q1). Major metros: Houston, Dallas–Fort Worth, San Antonio, Austin.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$100k**; shock liquid ≈ **$24k (9 mo)**; **total recommended liquid ≈ $124k**.
**Top industries:** trade / logistics; professional services; government; education & health (BLS CES SAE).
**Demographics / income:** White 47.7% · Black 12.3% · Hisp 39.8% · Asian 5.7%. Median HH income **$81k** (CPS 2024); mean HH income **$107k**. Price-to-income screen about **4.4x**.
**Top suburbs:** Frisco / McKinney / Plano (App); watch Austin supply digestion.

**Why it ranks:** FHFA YoY -1.6%; unemployment 4.4%; median $356k; price-to-income about 4.4x. Appreciation actionable rank **#44** (Econ 5.00).
**Best fit:** **Single-family appreciation hold** in Dallas–Fort Worth, Houston, Austin. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; near-term FHFA softness — do not extrapolate past boom blindly; anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Oregon
[↑ Back to Index](#index)

**Scores:** Jobs 3 / Price 7 / Cash (carry) 2 / Appreciation 6 / Owner law 3 / Tenant law 9

**Prices:** State median **$526k** / typical **$569k** (Redfin All Residential, 2026-05-31). FHFA YoY **+0.6%** (2026Q1). Major metros: Portland, Salem, Eugene.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$147k**; shock liquid ≈ **$32k (9 mo)**; **total recommended liquid ≈ $179k**.
**Top industries:** education & health; trade / logistics; government; professional services (BLS CES SAE).
**Demographics / income:** White 73.9% · Black 2.1% · Hisp 14.9% · Asian 4.6%. Median HH income **$90k** (CPS 2024); mean HH income **$107k**. Price-to-income screen about **5.9x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY +0.6%; unemployment 5.2%; median $526k; price-to-income about 5.9x. Appreciation actionable rank **#45** (Econ 4.90).
**Best fit:** **Single-family appreciation hold** in Portland, Salem. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds.
**Data confidence:** High

### Florida
[↑ Back to Index](#index)

**Scores:** Jobs 5 / Price 8 / Cash (carry) 2 / Appreciation 4 / Owner law 9 / Tenant law 2

**Prices:** State median **$422k** / typical **$439k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.5%** (2026Q1). Major metros: Tampa, Orlando, Jacksonville, Miami.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$118k**; shock liquid ≈ **$27k (9 mo)**; **total recommended liquid ≈ $145k**.
**Top industries:** trade / logistics; professional services; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 55.5% · Black 14.9% · Hisp 27.4% · Asian 3.0%. Median HH income **$76k** (CPS 2024); mean HH income **$104k**. Price-to-income screen about **5.6x**.
**Top suburbs:** Tampa / Jacksonville selected (Bal); coastal insurance-first.

**Why it ranks:** FHFA YoY -0.5%; unemployment 4.7%; median $422k; price-to-income about 5.6x. Appreciation actionable rank **#46** (Econ 4.90).
**Best fit:** **Single-family appreciation hold** in Tampa, Orlando, Jacksonville. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; near-term FHFA softness — do not extrapolate past boom blindly; anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants.
**Data confidence:** High

### Rhode Island
[↑ Back to Index](#index)

**Scores:** Jobs 6 / Price 6 / Cash (carry) 2 / Appreciation 3 / Owner law 7 / Tenant law 4

**Prices:** State median **$537k** / typical **$583k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.7%** (2026Q1). Major metros: Providence.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$150k**; shock liquid ≈ **$21k (6 mo)**; **total recommended liquid ≈ $171k**.
**Top industries:** education & health; trade / logistics; professional services; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 69.7% · Black 5.4% · Hisp 18.0% · Asian 3.4%. Median HH income **$92k** (CPS 2024); mean HH income **$113k**. Price-to-income screen about **5.8x**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY -0.7%; unemployment 4.1%; median $537k; price-to-income about 5.8x. Appreciation actionable rank **#47** (Econ 4.40).
**Best fit:** **Single-family appreciation hold** in Providence. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** thin exit / smaller buyer pool; near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** High

### Washington
[↑ Back to Index](#index)

**Scores:** Jobs 3 / Price 7 / Cash (carry) 2 / Appreciation 4 / Owner law 3 / Tenant law 9

**Prices:** State median **$652k** / typical **$686k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.4%** (2026Q1). Major metros: Seattle, Tacoma, Spokane.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$183k**; shock liquid ≈ **$39k (9 mo)**; **total recommended liquid ≈ $222k**.
**Top industries:** trade / logistics; government; education & health; professional services (BLS CES SAE).
**Demographics / income:** White 65.2% · Black 4.0% · Hisp 14.6% · Asian 10.0%. Median HH income **$98k** (CPS 2024); mean HH income **$129k**. Price-to-income screen about **6.7x**.
**Top suburbs:** Spokane value vs Eastside premium; statewide rent-cap overlay.

**Why it ranks:** FHFA YoY -0.4%; unemployment 5.2%; median $652k; price-to-income about 6.7x. Appreciation actionable rank **#48** (Econ 4.10).
**Best fit:** **Single-family appreciation hold** in Seattle, Spokane. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds; near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** High

### Colorado
[↑ Back to Index](#index)

**Scores:** Jobs 7 / Price 7 / Cash (carry) 2 / Appreciation 1 / Owner law 7 / Tenant law 5

**Prices:** State median **$617k** / typical **$620k** (Redfin All Residential, 2026-05-31). FHFA YoY **-2.4%** (2026Q1). Major metros: Denver, Colorado Springs, Fort Collins.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$173k**; shock liquid ≈ **$24k (6 mo)**; **total recommended liquid ≈ $197k**.
**Top industries:** trade / logistics; professional services; government; education & health (BLS CES SAE).
**Demographics / income:** White 70.4% · Black 3.9% · Hisp 22.7% · Asian 3.3%. Median HH income **$106k** (CPS 2024); mean HH income **$125k**. Price-to-income screen about **5.8x**.
**Top suburbs:** Denver Front Range suburbs — soft near-term FHFA; long structural demand.

**Why it ranks:** FHFA YoY -2.4%; unemployment 3.9%; median $617k; price-to-income about 5.8x. Appreciation actionable rank **#49** (Econ 4.10).
**Best fit:** **Single-family appreciation hold** in Denver, Colorado Springs. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** High

### California
[↑ Back to Index](#index)

**Scores:** Jobs 3 / Price 6 / Cash (carry) 1 / Appreciation 4 / Owner law 3 / Tenant law 9

**Prices:** State median **$887k** / typical **$865k** (Redfin All Residential, 2026-05-31). FHFA YoY **-0.5%** (2026Q1). Major metros: Los Angeles, Bay Area, San Diego, Sacramento.
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **$248k**; shock liquid ≈ **$53k (9 mo)**; **total recommended liquid ≈ $301k**.
**Top industries:** education & health; trade / logistics; professional services; government (BLS CES SAE).
**Demographics / income:** White 38.5% · Black 5.4% · Hisp 40.4% · Asian 15.8%. Median HH income **$101k** (CPS 2024); mean HH income **$134k**. Price-to-income screen about **8.8x**.
**Top suburbs:** Inland / Sacramento screens vs coastal trophy (App/supply constraint, thin Cash).

**Why it ranks:** FHFA YoY -0.5%; unemployment 5.2%; median $887k; price-to-income about 8.8x; structural supply / demand support. Appreciation actionable rank **#50** (Econ 3.80).
**Best fit:** **Single-family appreciation hold** in Los Angeles, Bay Area, San Diego. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** insurance / tax / regulation shock reserves elevated; owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds; near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** High

### District of Columbia
[↑ Back to Index](#index)

**Scores:** Jobs 1 / Price 5 / Cash (carry) 1 / Appreciation 2 / Owner law 1 / Tenant law 10

**Prices:** State median unavailable / typical unavailable (Redfin All Residential, 2026-05-31). FHFA YoY **-1.4%** (2026Q1). Major metros: Washington, D.C..
**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). On state median: cash to close ≈ **unavailable**; shock liquid ≈ **unavailable**; **total recommended liquid ≈ unavailable**.
**Top industries:** government; professional services; education & health; leisure / hospitality (BLS CES SAE).
**Demographics / income:** White 38.8% · Black 40.9% · Hisp 12.0% · Asian 4.2%. Median HH income **$105k** (CPS 2024); mean HH income **$161k**. Price-to-income screen about **unavailable**.
**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.

**Why it ranks:** FHFA YoY -1.4%; unemployment 6.0%. Appreciation actionable rank **#51** (Econ 2.20).
**Best fit:** **Single-family appreciation hold** in Washington, D.C.. Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold.
**Key risks:** owner-law friction (rent caps / just-cause / eviction delay); vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds; near-term FHFA softness — do not extrapolate past boom blindly.
**Data confidence:** Medium

---

## 7. Legal environment — verified 2026 highlights
[↑ Back to Index](#index)

Legal scores are reused directionally from the base rental report research layer. For appreciation holds, **owner-law friction matters for ops and exit timing**, even when cash flow is secondary. **Vacant single-family houses** also face **squatting / unauthorized occupancy** risk — treat that separately from ordinary tenant eviction.

| Theme | 2026 highlight | Investor takeaway |
| ----- | -------------- | ----------------- |
| **Washington / Oregon rent caps** | Statewide caps about **9.683%** (WA) and **9.5%** (OR) for 2026 | Long equity possible; near-term rent growth capped — size reserves |
| **California** | Statewide rent cap (5% + inflation, max 10%) + local overlays; trespass-removal bills active in 2025–26 sessions | Supply-constrained equity ≠ easy ops; **verify current vacant-occupant removal path** before long vacant holds |
| **New York** | Good Cause in opt-in cities; strong tenant tilt | Prefer **upstate SFH** for App; NYC specialist-only; vacant borough product = high ops friction |
| **New Jersey** | Anti-Eviction Act; many local rent ordinances | Equity / spillover demand with tax + ops drag |
| **Illinois** | State preempts rent control; Chicago strong local L-T ordinance; newer anti-squatter tools expanding post-2025 | Chicago App works with city-rule underwriting; still monitor vacant SFH |
| **Midwest owner-friendly cluster** | OH / IN / WI / MO / KY baselines generally landlord-leaning | Good remote-ops backdrop for equity holds |
| **Idaho / Utah** | Strong owner law | Pair with migration thesis; watch entry prices |
| **Anti-squatter reform cluster** | GA Squatter Reform Act; FL unauthorized-occupant sheriff complaint path; 2025–26 expansions in TX, NC, OR, KS, MS, AZ, SC and others ([NAA tracker](https://naahq.org/news/anti-squatter-legislation-continues-third-year)) | Better **paper tools** for true unauthorized occupants — still confirm **local LE practice**; not a free pass to neglect vacant homes |

City rules can override state baselines (Chicago, NYC, coastal CA, Seattle). Verify locally before bidding.

### Squatting / vacant SFH (appreciation overlay)
[↑ Back to Index](#index)

Why this sibling emphasizes squatting: App investors often accept **longer vacancy, rehab, or thin leasing** — vacant detached houses are the usual target, not occupied rentals with clear leases.

| Concept | Screen rule |
| ------- | ----------- |
| **Unauthorized occupant / squatter** | Entered **without** consent; **no** bona fide lease — some states now allow expedited LE / sheriff removal after owner affidavit |
| **Holdover or claimed tenant** | Usually **eviction court**, not “trespass remove” — fake-lease fraud is common; document ownership and prior vacancy |
| **Adverse possession** | Long open/hostile statutory path to a **title** claim — rare vs headlines, real if you abandon an App hold for years |
| **Reform vs friction** | Reform statutes help **paper process**; large metros can still be slow if LE defaults to civil |

**Operating controls (minimum for vacant App SFH):** change locks at closing; keep utilities intentional (not “dark and abandoned”); weekly or biweekly exterior/interior checks (PM vacant product or trusted local); cameras / smart locks where lawful; immediate counsel if someone claims tenancy; never self-help lockouts of people who may be tenants.

**Ranking use:** clearer vacant-occupant removal + strong remote monitoring **tie-breaks upward** for remote App buyers; unmonitored vacant product in friction metros **tie-breaks downward** even when FHFA looks strong.

---

## 8. Insurance and property-tax overlays
[↑ Back to Index](#index)

Appreciation math dies if insurance or taxes force a sale. Apply the same overlays as the base report, with extra emphasis on **not under-reserving** thin-cash App buys.

### Property tax
[↑ Back to Index](#index)

- Effective rates range from about **0.27% (Hawaii)** to **2.23% (New Jersey)**.
- **New Jersey, Illinois, Connecticut, Texas, Nebraska, Wisconsin** — budget tax drag explicitly in carry models.
- Low-tax states (e.g., Alabama, Hawaii) help carry but do not automatically create appreciation.

### Insurance / catastrophe
[↑ Back to Index](#index)

- National landlord policies often **$800–$3,000/year**.
- Commonly **$2,200–$4,600+** in Florida, Louisiana, Texas, Oklahoma, Mississippi, and hail-belt pockets.
- Treat Florida coastal, Louisiana, Texas Gulf, and Oklahoma as **insurance-first** markets — equity thesis second.
- Ask carriers about **vacancy clauses** — many policies restrict or exclude coverage after 30–60 days vacant; squatting loss without coverage can erase equity.

---

## 9. Property management rates & remote ops
[↑ Back to Index](#index)

Lighter section than the base rental report: appreciation investors still need **professional ops** so thin cash flow does not become deferred maintenance — and so **vacant houses are not left unwatched**.

| Fee | Typical screen |
| --- | -------------- |
| Monthly management | **8–12%** of collected rent (default screen **10%**) |
| Leasing / placement | **50–100%** of one month’s rent on turnover |
| Vacant / caretaking | Flat monthly vacant fee or reduced % — **budget explicitly** on App holds |
| All-in first-year | Often **15–20%+** of gross once add-ons included |

Prefer metros with **multiple competing local PMs** (Chicago suburbs, Indianapolis, Milwaukee, Dallas–Fort Worth, Atlanta, Phoenix, Raleigh). Interview 2–3 managers; get fee schedules in writing; ask for **vacant inspection cadence** and unauthorized-occupant response SOP. Institutional SFR landlords (Invitation Homes, Progress Residential, etc.) are **comps / competitors**, not your third-party PM.

---

## 10. Practical acquisition workflow
[↑ Back to Index](#index)

1. Confirm strategy: **appreciation / equity path** (this report) vs cash-flow-first (base rental report).
2. Property type: **single-family only** for this screen.
3. Shortlist 3–5 metros from §3 / §5 — not a whole state.
4. Pull ZIP-level sale comps and **days-on-market / sale-to-list** (exit liquidity).
5. Get property-tax history and a **bindable insurance quote** before finalizing — confirm **vacancy endorsement** limits.
6. Model carry: vacancy, management (about 10%), leasing, repairs, tax, insurance — even if day-one cash is thin.
7. Confirm **cash to close + shock reserves** from §4e (do not skip reserves because “it’s an App deal”).
8. Use transparent financing defaults (**25% down**, investor rate band about 7.0%–8.5%) unless you have a live quote for different leverage — disclose any override.
9. Stress: rate +1%, rent −5%, insurance +50%, price flat for 24 months, and six months vacancy.
10. Verify local licensing, notice, rent-cap, just-cause rules, and **unauthorized-occupant / squatter removal path** (sheriff affidavit vs full eviction).
11. Day-of / post-close vacant controls: rekey, utilities plan, PM vacant checks, no “dark abandoned” look — document ownership if LE is called.
12. Buy only if the **address-level** equity path still works with reserves **and** a vacant-occupancy plan intact.

---

## 11. Methodology and sources
[↑ Back to Index](#index)

### Confirmation of live research
[↑ Back to Index](#index)

Tabular national fields use the Market repo’s live `data/` snapshots from this workspace run.

- **Pipeline live fetch stamp:** `data/meta.json` analysis_run_at **2026-07-26T08:29:17+00:00**; census_api_key_present=True; fred_api_key_present=True; bls_api_key_present=True; bea_api_key_present=True.
- **Format parent:** section skeleton from `rental_market_report.md`.
- **Spec:** `sfh_appreciation_spec.md` (includes mandatory squatting / vacant-SFH overlay).

### Scoring weights (appreciation-first)
[↑ Back to Index](#index)

| Pillar | Weight in Econ | Meaning in this report |
| ------ | -------------: | ---------------------- |
| Appreciation | 40% | FHFA YoY + structural demand/supply overlay |
| Jobs | 30% | Unemployment + growth-corridor nudge |
| Price | 20% | Entry vs income band + exit liquidity |
| Cash (carry) | 10% | Secondary carry tolerance — thin OK |

Owner / Tenant law scores are shown separately (not in Econ) and reused from the base legal judgment layer. **Squatting risk** is an **overlay** (Legal § + avoid/watch + deep-dive risks + acquisition controls), not a fifth Econ pillar.

### Financing and expense assumptions
[↑ Back to Index](#index)

| Item | Default used |
| ---- | ------------ |
| Down payment | **25%** (disclosed default; App buyers may use other leverage — label overrides) |
| Closing / acquisition | about 3% of purchase |
| Cash to close | ≈ **28%** of median |
| Shock liquid | **6 months** PITI default; **9 months** in high-insurance / high-tax / heavy-regulation states |
| PITI rate assumption | **7.5%** midpoint of about 7.0%–8.5% investor band; 30-year amortizing on 75% LTV |
| Property management | about **10%** of collected rent unless quoted; vacant caretaking budgeted separately when vacant |
| Hold period | **5–10+ years** |

### Primary sources
[↑ Back to Index](#index)

- [FHFA House Price Index, 2026 Q1](https://www.fhfa.gov/reports/house-price-index/2026/Q1) / live `data/fhfa.json`
- [Redfin state market tracker](https://www.redfin.com/news/) / live `data/state_prices.json`
- [BLS LAUS unemployment](https://www.bls.gov/news.release/laus.htm) / `data/jobs.json`
- [BLS CES industry employment](https://www.bls.gov/ces/) / `data/industries.json`
- [FRED / CPS median HH income](https://fred.stlouisfed.org/release/tables?eid=259462&rid=249) / `data/income.json`
- Census ACS demographics + mean income / `data/demographics.json`, `data/income.json`
- [BEA personal income](https://www.bea.gov/) / `data/bea.json`
- [BLS metro employment, May 2026](https://www.bls.gov/news.release/metro.nr0.htm)
- Base report legal / insurance / suburb research layer in `rental_market_report.md`
- Anti-squatter legislation tracker / context: [National Apartment Association](https://naahq.org/news/anti-squatter-legislation-continues-third-year); state examples include [Georgia Squatter Reform Act (HB 1017)](https://gov.georgia.gov/document/2024-signed-legislation/hb-1017/download), Florida unauthorized-occupant sheriff complaint path (Ch. 82 / related 2025 updates)
- [July 2026 investor loan rate sheets](https://dscrfinder.com/blog/current-dscr-loan-rates)

### Caveats / data gaps
[↑ Back to Index](#index)

- One-year FHFA is **backward-looking**; structural App overlays are labeled judgment.
- Metro FHFA prints in §5 cite the base report’s published metro leader table; state YoY is always from live `data/fhfa.json`.
- `data/metro_prices.json` and `data/suburbs.json` remain placeholders — suburb notes are qualitative screens.
- True mean closed-sale prices by metro are often `unavailable`.
- Squatting statutes and **county LE practice** change quickly — treat §7 as a screen, not a legal opinion; confirm with local counsel.
- Never use Markdown `~` for approximately (strikethrough risk); this report uses **about** or **≈**.
- This sibling does **not** auto-build via `pipeline/build_report.py` yet — refresh guidance is in `sfh_appreciation_spec.md`.

### A–Z actionable-rank index
[↑ Back to Index](#index)

Actionable rank by postal abbreviation (1 = highest appreciation actionable). **Every** state links to its [§6 deep dive](#6-all-state-deep-dives).

| | | | | |
|---|---|---|---|---|
| [AK](#alaska) 26 | [AL](#alabama) 24 | [AR](#arkansas) 20 | [AZ](#arizona) 37 | [CA](#california) 50 |
| [CO](#colorado) 49 | [CT](#connecticut) 3 | [DC](#district-of-columbia) 51 | [DE](#delaware) 41 | [FL](#florida) 46 |
| [GA](#georgia) 25 | [HI](#hawaii) 21 | [IA](#iowa) 18 | [ID](#idaho) 17 | [IL](#illinois) 1 |
| [IN](#indiana) 8 | [KS](#kansas) 29 | [KY](#kentucky) 7 | [LA](#louisiana) 38 | [MA](#massachusetts) 10 |
| [MD](#maryland) 34 | [ME](#maine) 30 | [MI](#michigan) 28 | [MN](#minnesota) 27 | [MO](#missouri) 9 |
| [MS](#mississippi) 31 | [MT](#montana) 35 | [NC](#north-carolina) 33 | [ND](#north-dakota) 11 | [NE](#nebraska) 14 |
| [NH](#new-hampshire) 13 | [NJ](#new-jersey) 4 | [NM](#new-mexico) 36 | [NV](#nevada) 40 | [NY](#new-york) 6 |
| [OH](#ohio) 16 | [OK](#oklahoma) 42 | [OR](#oregon) 45 | [PA](#pennsylvania) 5 | [RI](#rhode-island) 47 |
| [SC](#south-carolina) 32 | [SD](#south-dakota) 19 | [TN](#tennessee) 12 | [TX](#texas) 44 | [UT](#utah) 43 |
| [VA](#virginia) 23 | [VT](#vermont) 15 | [WA](#washington) 48 | [WI](#wisconsin) 2 | [WV](#west-virginia) 22 |
| [WY](#wyoming) 39 |  |  |  |  |

---

*End of single-family appreciation sibling report. Informational only — not financial advice. Re-pull live comps, tax bills, and bindable insurance quotes before deploying capital. For cash-flow–first SFR + 2–4 unit screens, use `rental_market_report.md`.*
