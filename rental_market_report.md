# US Rental Market Analysis

**Base report / format template:** `rental_market_report.md`  
**Analysis date:** July 25, 2026  
**Coverage:** All 50 states + Washington, D.C.; major metro screening; deeper review of leading markets  
**Property types:** Single-family houses **and** small multifamily homes (2–4 units: duplex / triplex / fourplex)  
**Live research:** Yes. Fresh web searches for jobs, **median and average/typical prices by state and major city**, **top suburbs inside major metros**, **top job industries by state/metro**, **race/ethnicity and household income**, rents, appreciation, landlord/tenant law, property taxes, insurance, investor loan rates, and single-family vs small-multifamily fit.

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
| [9. Acquisition workflow](#9-practical-acquisition-workflow) | [10. Methodology & sources](#10-methodology-and-sources) |
| [A–Z state rank index](#az-actionable-rank-index) | |

**Deep dives (all states + D.C., actionable order):** [OH](#ohio) · [IN](#indiana) · [AR](#arkansas) · [IA](#iowa) · [MO](#missouri) · [WI](#wisconsin) · [AL](#alabama) · [KY](#kentucky) · [PA](#pennsylvania) · [TN](#tennessee) · [NE](#nebraska) · [ND](#north-dakota) · [MI](#michigan) · [WV](#west-virginia) · [KS](#kansas) · [GA](#georgia) · [MS](#mississippi) · [SC](#south-carolina) · [OK](#oklahoma) · [NC](#north-carolina) · [SD](#south-dakota) · [IL](#illinois) · [TX](#texas) · [VA](#virginia) · [NM](#new-mexico) · [MN](#minnesota) · [LA](#louisiana) · [AK](#alaska) · [VT](#vermont) · [ME](#maine) · [ID](#idaho) · [FL](#florida) · [WY](#wyoming) · [UT](#utah) · [MT](#montana) · [NV](#nevada) · [CT](#connecticut) · [DE](#delaware) · [AZ](#arizona) · [MD](#maryland) · [NH](#new-hampshire) · [NY](#new-york) · [NJ](#new-jersey) · [RI](#rhode-island) · [MA](#massachusetts) · [HI](#hawaii) · [CO](#colorado) · [OR](#oregon) · [WA](#washington) · [CA](#california) · [DC](#district-of-columbia)

**City boards:** [Cash flow](#cash-flow-potential-gross-yield-is-a-screen) · [Single-family](#best-for-single-family-houses) · [2–4 unit](#best-for-24-unit-multifamily-homes) · [Top suburbs](#top-suburbs-worth-researching-live-2026-screen) · [Appreciation](#appreciation-leaders-first-quarter-2026-federal-housing-finance-agency) · [Jobs](#job-market-leaders-may-2026-payroll-changes)

---

## 1. What changed vs the prior run
[↑ Back to Index](#index)


This refresh adds the new **median + average/typical price** requirement from the updated spec while keeping the same overall report shape.


| Change                    | What it means                                                                                                                                                         |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prices in context**     | Section 4 uses **two companion tables** (scores + prices/metros) so columns stay readable; city/deep-dive prices stay inline                                          |
| **Top suburb research**   | Major metros now include **1–3 researched suburbs** (cash-flow vs appreciation), e.g. Phoenix East vs West Valley                                                     |
| **Top job industries**    | Every state lists **top industries** (BLS May 2026 CES mix); metros note industry clusters in deep dives                                                              |
| **Durable pipeline**      | Full refreshes must **live-fetch → overwrite** `data/` **→ build** (no disposable `_add_*.py` patch scripts)                                                          |
| **Entry capital / shock reserves** | Every state shows **25% down**, cash to close, **6–9 mo shock liquid**, and total recommended liquid (metro/suburb variants in deep dives) |
| **All-state deep dives** | **Every state + D.C.** has a full §6 deep dive (no remaining-state bullet cards) |
| **Index / navigation**    | Top clickable **Index** + end **A–Z rank index**; **every section** has **[↑ Back to Index](#index)** under its heading |
| **Demographics & income** | Every state lists **race/ethnicity mix** (2020 Census) + **median HH income** (CPS 2024); mean marked `unavailable` pending ACS pull; metro ACS incomes in deep dives |
| Property-type scope       | Rankings cover **single-family houses** and **2–4 unit multifamily homes**, with split shortlists                                                                     |
| Cash-flow realism         | Scores haircut for **property tax**, **insurance**, concessions, and vacancy — not just rent ÷ price                                                                  |
| Financing defaults        | Standard case: **25% down**, investor loan rates near **7.0%–8.5%** for typical files (July 2026 lender sheets)                                                       |
| Risk overlays             | Insurance catastrophe, tax drag, new supply/concessions, exit liquidity, remote management, ops intensity                                                             |
| City vs state law         | Local rules can override the state baseline (Chicago, New York City, coastal California, Seattle, etc.)                                                               |
| Language                  | Fewer abbreviations; terms spelled out in plain English                                                                                                               |


**Defaults used (user did not override):** balanced strategy; remote-capable preferred; 5–10 year hold; moderate risk.

---



## 2. National market snapshot
[↑ Back to Index](#index)


- U.S. unemployment was **4.2% in June 2026**. South Dakota lowest at 2.0%; Washington, D.C. highest at 6.0% ([Bureau of Labor Statistics](https://www.bls.gov/news.release/laus.htm)).
- **Entry capital tabulated:** Section **4e** and every deep-dive **Entry capital:** line screen **25% down**, cash to close (~28% of median), and **6–9 months** PITI shock reserves.
- **Demographics & income tabulated:** Section **4d** lists race/ethnicity mix and median household income for every state + D.C.; mean household income marked `unavailable` where ACS mean could not be pulled.
- **Job industries tabulated:** Section **4c** lists each state’s largest employment sectors (BLS May 2026 CES industry mix), with concentration notes for renter-demand risk.
- **State prices are in the ranking matrix:** May 2026 Redfin median sale and June 2026 Zillow typical value for every state + D.C. appear as columns in **Section 4** ([Forbes/Redfin](https://www.forbes.com/advisor/mortgages/real-estate/median-home-prices-by-state/); [ZHVI table](https://keepingupwithinflation.com/statistics/home-prices-by-state/)). City medians appear with city rankings and deep dives.
- Typical U.S. home value was **$370,320 in May 2026** ([Zillow via Federal Reserve Economic Data](https://fred.stlouisfed.org/series/USAUCSFRCONDOSMSAMID)).
- National median sale price was **$408,776 in June 2026**, up 2.2% year over year; average 30-year mortgage rate about **6.49%** ([Redfin](https://www.redfin.com/news/home-prices-record-high-june-2026/)).
- Typical U.S. rent was **$1,951 in May 2026**, up 2.0% year over year. About **39.6%** of rental listings offered a concession ([Zillow May Rent Report](https://www.zillow.com/research/may-2026-rent-report-36461/)).
- National house prices rose **1.7% year over year in first-quarter 2026** — recent strength tilted Midwest / Northeast ([Federal Housing Finance Agency](https://www.fhfa.gov/reports/house-price-index/2026/Q1)).
- Population growth slowed nationally; South Carolina, Idaho, and North Carolina led state percentage growth; Houston and Dallas led numeric metro gains ([U.S. Census Bureau](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html)).
- Effective property-tax rates range from about **0.27% (Hawaii)** to **2.23% (New Jersey)**; Alabama is among the lowest-cost tax states ([Tax Foundation / 2026 compilations](https://www.financewonk.com/references/property-taxes-by-state)).
- Landlord insurance often runs about **$800–$3,000/year** nationally, but **$2,200–$4,600+** is common in Florida, Louisiana, Texas, Oklahoma, Mississippi, and similar catastrophe-exposed states ([2026 landlord insurance summaries](https://richeyinsurance.com/landlord-insurance-statistics/)).
- Typical investor loan rates for rental purchases in July 2026 cluster near **7.0%–8.5%** for standard files; strongest files can print lower ([July 2026 investor/DSCR lender sheets](https://dscrfinder.com/blog/current-dscr-loan-rates)). Duplex–fourplex loans often price slightly higher than single-family.



### Yield definition used here
[↑ Back to Index](#index)


- **Gross yield** = annual rent ÷ purchase price (prefer **median** purchase price when available). Screening only — not take-home cash flow.
- Prefer **signed / achieved lease rent** when available; otherwise label **asking rent** (Zillow rent index).
- **Realistic cash-flow score** assumes vacancy, management, maintenance, property tax, insurance, and concessions.
- Never treat gross yield as cash-on-cash.



### Core conclusion
[↑ Back to Index](#index)


The best risk-adjusted 2026 screens remain **Midwest metros with affordable entry, workable landlord law, and improving prices**, plus selected Southeast growth markets. Highest printed gross yields still cluster in Detroit, Jackson, Cleveland, Birmingham, and Memphis — but insurance, taxes, concessions, property condition, and exit liquidity can erase the headline advantage.

**Single-family vs small multifamily:**  

- **Single-family** usually wins on easier management, broader buyer pool, and appreciation / exit flexibility.  
- **2–4 unit homes** usually win on cash-flow cushion and vacancy resilience (one empty unit does not zero income). Midwest cash-flow cities are where duplexes and fourplexes most often beat single-family on income math.

---



## 3. Top 10 actionable markets
[↑ Back to Index](#index)


Tie-breakers after equal economic scores: metro depth, data confidence, lower insurance catastrophe risk, remote management availability, diversified jobs.


| Rank | State / preferred metros                       | Why it ranks                                                                         | Single-family vs 2–4 unit                                                                     | Main caution                                      |
| ---- | ---------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| 1    | **Ohio — Cleveland, Cincinnati, Columbus**     | Best mix of yield, affordable entry, falling unemployment, strong recent price gains | Both work; Cleveland duplex/triplex inventory is especially income-friendly                   | Older housing; block-level variance               |
| 2    | **Indiana — Indianapolis, Fort Wayne**         | Affordable, landlord-friendly, solid yields, 3.3% unemployment                       | Strong for both; Indianapolis is the cleanest turnkey single-family market                    | Bloomington job losses; rising concessions        |
| 3    | **Arkansas — Northwest Arkansas, Little Rock** | Fayetteville metro +2.5% jobs; affordable statewide; favorable law                   | Single-family growth in Northwest Arkansas; Little Rock better for income / small multifamily | Northwest Arkansas no longer uniformly cheap      |
| 4    | **Iowa — Des Moines, Cedar Rapids**            | 3.2% unemployment, low prices, stable appreciation                                   | Mostly single-family depth; small multifamily thinner outside Des Moines                      | Ames payroll decline; smaller exit pools          |
| 5    | **Missouri — Kansas City, St. Louis**          | Balanced rent-to-price and two scalable metros                                       | Both; Kansas City more balanced, St. Louis more income-oriented                               | Neighborhood selection in St. Louis               |
| 6    | **Wisconsin — Milwaukee, Madison**             | Milwaukee yield plus strong statewide appreciation                                   | Both; Milwaukee favors income, Madison favors stability / higher entry                        | Property taxes; winter maintenance                |
| 7    | **Alabama — Birmingham, Huntsville**           | Birmingham cash flow; Huntsville jobs; very low property taxes                       | Both; Birmingham strong for duplex / fourplex income                                          | Insurance and city operating variance             |
| 8    | **Kentucky — Louisville, Lexington**           | Low entry prices and top-tier statewide appreciation                                 | Both; Louisville better scale for 2–4 units                                                   | State unemployment 4.7%                           |
| 9    | **Pennsylvania — Pittsburgh, Philadelphia**    | Strong yields and recent appreciation                                                | Both; Pittsburgh especially strong for duplex / triplex                                       | Older housing; Philadelphia local rules / taxes   |
| 10   | **Tennessee — Memphis, Nashville**             | Memphis income; Nashville growth                                                     | Memphis favors both income strategies; Nashville mostly thinner-yield single-family           | Different markets; Nashville supply / concessions |




### Best landlord-protection markets (law + economics)
[↑ Back to Index](#index)



| Rank | Market                                      | Why                                                                   |
| ---- | ------------------------------------------- | --------------------------------------------------------------------- |
| 1    | Ohio — Cleveland / Cincinnati               | Strong owner-friendly baseline; high yield; improving prices          |
| 2    | Indiana — Indianapolis                      | Rent-control preemption; scalable management; affordable inventory    |
| 3    | Alabama — Birmingham                        | Favorable statutes; low taxes; high gross-yield potential             |
| 4    | Arkansas — Little Rock / Northwest Arkansas | Favorable law plus a standout job-growth metro                        |
| 5    | Missouri — Kansas City / St. Louis          | Workable law with deeper metro options                                |
| 6    | Wisconsin — Milwaukee                       | Owner-friendly baseline and strong current appreciation               |
| 7    | Georgia — Atlanta / Athens / Augusta        | Strong owner law plus migration / job pockets                         |
| 8    | Tennessee — Memphis                         | Favorable law and strong yield if management is strong                |
| 9    | Oklahoma — Oklahoma City / Tulsa            | Very favorable law and low entry price; jobs and insurance limit rank |
| 10   | West Virginia — Charleston / Huntington     | Very low entry cost and favorable law; weak scale                     |




### Best tenant-protection markets that still have an investment case
[↑ Back to Index](#index)


These are **not** “easiest for landlords.” They can still work for appreciation, long holds, or values-aligned investors who accept slower evictions / rent caps.


| Rank | Market                                                | Protection reality                                                                                                        | Investment case                                                |
| ---- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1    | **Upstate New York — Syracuse / Rochester / Buffalo** | Good Cause applies in opt-in cities; statewide tenant tilt                                                                | Strong recent appreciation; prices far below New York City     |
| 2    | **Chicago, Illinois**                                 | City landlord-tenant ordinance and Fair Notice; Cook County rules; **no rent cap** because Illinois preempts rent control | Large economy and strong 2026 price performance                |
| 3    | **Hartford, Connecticut**                             | Tenant-leaning statewide climate                                                                                          | Better yield than coastal Northeast peers; strong appreciation |
| 4    | **Baltimore, Maryland**                               | State / county tenant protections and local stabilization in places                                                       | High reported gross yield; large employment base               |
| 5    | **Newark / secondary New Jersey metros**              | Statewide Anti-Eviction Act; many local rent ordinances                                                                   | Strong appreciation and New York spillover; taxes are severe   |
| 6    | **Portland, Maine**                                   | Local rent stabilization                                                                                                  | Tight labor market and constrained supply                      |
| 7    | **Burlington, Vermont**                               | Strong tenant-protection direction                                                                                        | Low unemployment; thin inventory                               |
| 8    | **Portland, Oregon**                                  | Statewide rent cap **9.5% for 2026**; just-cause rules                                                                    | Long-term supply constraints; current jobs are weak            |
| 9    | **Seattle, Washington**                               | Statewide rent cap **9.683% for 2026**; just cause and long notice                                                        | High-income job base; weak current price / job trend           |
| 10   | **Selected inland California metros**                 | Statewide rent cap (5% + inflation, max 10%) plus local overlays                                                          | Better entry than the coast; still regulation-heavy            |


New York City, San Francisco, Los Angeles, and Washington, D.C. remain specialist-only: strong tenant protections, but acquisition price, yield, or operating friction are severe.

### Markets to avoid / watch
[↑ Back to Index](#index)



| Market                                               | Issue                                                                                              |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Washington, D.C. metro**                           | About −100,500 jobs year over year; TOPA / rent stabilization; expensive entry                     |
| **Portland, Oregon**                                 | About −35,000 jobs; statewide rent cap; weak near-term yield                                       |
| **Coastal California trophy markets**                | High prices, low yields, statewide + local tenant rules                                            |
| **Seattle**                                          | Soft home prices, high concessions, statewide rent cap                                             |
| **Austin**                                           | Population still grows, but price correction and concessions show oversupply risk                  |
| **Florida coastal / condo**                          | Headline rents can disappear after insurance, assessments, association fees, flood / wind coverage |
| **Detroit / Jackson “too good to be true” listings** | Extreme printed yields often price in condition, taxes, vacancy, and poor exits                    |


---



## 4. All-state ranking matrix
[↑ Back to Index](#index)


Split into two companion tables so columns stay readable in Markdown preview. Both use the same `#` order — **4a** shows scores with primary metros named; **4b** adds dollars and the fuller metro list. Suburbs inside a metro (e.g., Tempe inside Phoenix) are usually not separate national rows.

### 4a. Scores (actionable order)
[↑ Back to Index](#index)


`#` = actionable rank after tie-breakers. **Price** = affordability score (higher = cheaper entry), not dollar price. Primary metros are shown next to each state (full list in 4b).


| #   | State (primary metros)                                 | Jobs | Price | Cash | Appr. | Econ | Owner | Tenant | Conf.  |
| --- | ------------------------------------------------------ | ---- | ----- | ---- | ----- | ---- | ----- | ------ | ------ |
| 1   | Ohio — Cleveland, Columbus, Cincinnati…                | 8    | 8     | 9    | 8     | 8.25 | 9     | 2      | High   |
| 2   | Indiana — Indianapolis, Fort Wayne, South Bend         | 8    | 8     | 9    | 8     | 8.25 | 9     | 2      | High   |
| 3   | Arkansas — Fayetteville–Springdale, Little Rock        | 8    | 9     | 8    | 8     | 8.25 | 9     | 2      | High   |
| 4   | Iowa — Des Moines, Cedar Rapids, Iowa City             | 8    | 9     | 8    | 8     | 8.25 | 9     | 2      | Medium |
| 5   | Missouri — Kansas City, St. Louis, Springfield         | 7    | 8     | 8    | 8     | 7.75 | 8     | 3      | High   |
| 6   | Wisconsin — Milwaukee, Madison, Green Bay              | 8    | 6     | 7    | 9     | 7.50 | 9     | 2      | High   |
| 7   | Alabama — Birmingham, Huntsville, Mobile               | 8    | 8     | 8    | 7     | 7.75 | 9     | 2      | High   |
| 8   | Kentucky — Louisville, Lexington                       | 5    | 9     | 8    | 9     | 7.75 | 8     | 3      | Medium |
| 9   | Pennsylvania — Pittsburgh, Philadelphia, Lancaster     | 6    | 7     | 8    | 8     | 7.25 | 7     | 4      | High   |
| 10  | Tennessee — Memphis, Nashville, Knoxville…             | 8    | 6     | 8    | 7     | 7.25 | 9     | 2      | High   |
| 11  | Nebraska — Omaha, Lincoln                              | 8    | 7     | 7    | 8     | 7.50 | 7     | 3      | Medium |
| 12  | North Dakota — Fargo, Bismarck                         | 10   | 7     | 6    | 9     | 8.00 | 8     | 3      | Medium |
| 13  | Michigan — Detroit, Grand Rapids, Lansing…             | 4    | 8     | 8    | 8     | 7.00 | 8     | 3      | High   |
| 14  | West Virginia — Charleston, Huntington, Morgantown     | 6    | 10    | 8    | 8     | 8.00 | 9     | 2      | Medium |
| 15  | Kansas — Wichita, Kansas City–KS, Topeka               | 7    | 8     | 7    | 7     | 7.25 | 8     | 3      | Medium |
| 16  | Georgia — Atlanta, Athens, Augusta…                    | 9    | 6     | 7    | 5     | 6.75 | 9     | 2      | High   |
| 17  | Mississippi — Jackson, Gulfport, Hattiesburg           | 7    | 10    | 6    | 7     | 7.50 | 9     | 2      | Medium |
| 18  | South Carolina — Greenville, Columbia, Charleston      | 8    | 6     | 6    | 6     | 6.50 | 9     | 2      | High   |
| 19  | Oklahoma — Oklahoma City, Tulsa                        | 5    | 9     | 6    | 5     | 6.25 | 9     | 2      | High   |
| 20  | North Carolina — Raleigh, Charlotte, Greensboro        | 9    | 6     | 6    | 5     | 6.50 | 8     | 3      | High   |
| 21  | South Dakota — Sioux Falls, Rapid City                 | 10   | 6     | 6    | 7     | 7.25 | 8     | 3      | Medium |
| 22  | Illinois — Chicago, Peoria, Rockford…                  | 4    | 7     | 6    | 10    | 6.75 | 6     | 6      | High   |
| 23  | Texas — Houston, Dallas–Fort Worth, San Antonio…       | 8    | 7     | 5    | 3     | 5.75 | 9     | 2      | High   |
| 24  | Virginia — Richmond, Virginia Beach, Northern Virginia | 7    | 4     | 5    | 7     | 5.75 | 8     | 3      | High   |
| 25  | New Mexico — Albuquerque, Santa Fe, Las Cruces         | 5    | 6     | 6    | 7     | 6.00 | 8     | 3      | Medium |
| 26  | Minnesota — Minneapolis–St. Paul, Duluth, Rochester    | 6    | 6     | 5    | 7     | 6.00 | 6     | 6      | High   |
| 27  | Louisiana — New Orleans, Baton Rouge, Lafayette        | 6    | 9     | 4    | 6     | 6.25 | 9     | 2      | Medium |
| 28  | Alaska — Anchorage, Fairbanks                          | 6    | 5     | 5    | 10    | 6.50 | 8     | 3      | Medium |
| 29  | Vermont — Burlington                                   | 8    | 5     | 4    | 9     | 6.50 | 4     | 8      | Medium |
| 30  | Maine — Portland, Bangor                               | 8    | 5     | 4    | 7     | 6.00 | 5     | 7      | Medium |
| 31  | Idaho — Boise, Idaho Falls, Coeur d’Alene              | 8    | 4     | 4    | 7     | 5.75 | 10    | 1      | High   |
| 32  | Florida — Tampa, Orlando, Jacksonville…                | 6    | 5     | 4    | 4     | 4.75 | 9     | 2      | High   |
| 33  | Wyoming — Cheyenne, Casper                             | 8    | 5     | 6    | 4     | 5.75 | 9     | 2      | Medium |
| 34  | Utah — Salt Lake City, Provo, Ogden                    | 9    | 3     | 4    | 4     | 5.00 | 10    | 1      | High   |
| 35  | Montana — Billings, Missoula, Bozeman                  | 8    | 4     | 4    | 5     | 5.25 | 9     | 2      | Medium |
| 36  | Nevada — Las Vegas, Reno                               | 7    | 4     | 5    | 5     | 5.25 | 8     | 3      | High   |
| 37  | Connecticut — Hartford, Bridgeport, New Haven          | 4    | 4     | 6    | 9     | 5.75 | 5     | 7      | High   |
| 38  | Delaware — Wilmington, Dover                           | 5    | 5     | 5    | 6     | 5.25 | 8     | 3      | Medium |
| 39  | Arizona — Phoenix, Tucson                              | 5    | 4     | 5    | 5     | 4.75 | 9     | 2      | High   |
| 40  | Maryland — Baltimore, Montgomery / Prince George’s     | 5    | 4     | 6    | 5     | 5.00 | 5     | 7      | High   |
| 41  | New Hampshire — Manchester–Nashua                      | 8    | 3     | 3    | 8     | 5.50 | 5     | 7      | Medium |
| 42  | New York — New York City, Buffalo, Rochester…          | 5    | 3     | 4    | 9     | 5.25 | 1     | 10     | High   |
| 43  | New Jersey — Newark, Camden, New Brunswick             | 6    | 3     | 2    | 9     | 5.00 | 3     | 9      | High   |
| 44  | Rhode Island — Providence                              | 6    | 3     | 4    | 4     | 4.25 | 7     | 4      | Medium |
| 45  | Massachusetts — Boston, Worcester, Springfield         | 6    | 2     | 2    | 7     | 4.25 | 6     | 6      | High   |
| 46  | Hawaii — Honolulu                                      | 8    | 1     | 2    | 7     | 4.50 | 7     | 4      | Medium |
| 47  | Colorado — Denver, Colorado Springs, Fort Collins      | 7    | 3     | 3    | 2     | 3.75 | 7     | 5      | High   |
| 48  | Oregon — Portland, Salem, Eugene                       | 3    | 3     | 3    | 5     | 3.50 | 3     | 9      | High   |
| 49  | Washington — Seattle, Tacoma, Spokane                  | 4    | 2     | 3    | 4     | 3.25 | 3     | 9      | High   |
| 50  | California — Los Angeles, Bay Area, San Diego…         | 4    | 1     | 2    | 4     | 2.75 | 3     | 9      | High   |
| 51  | District of Columbia — Washington, D.C.                | 2    | 2     | 3    | 3     | 2.50 | 1     | 10     | High   |




### 4b. Prices & major metros (same order)
[↑ Back to Index](#index)


**Median** = Redfin median single-family sale (May 2026). **Typical** = Zillow typical home value (June 2026). Rounded for display; exact figures in methodology sources.


| #   | State                | Median | Typical | Major metros / cities                                        |
| --- | -------------------- | ------ | ------- | ------------------------------------------------------------ |
| 1   | Ohio                 | $263k  | $252k   | Cleveland, Columbus, Cincinnati, Dayton, Toledo              |
| 2   | Indiana              | $273k  | $262k   | Indianapolis, Fort Wayne, South Bend                         |
| 3   | Arkansas             | $270k  | $229k   | Fayetteville–Springdale, Little Rock                         |
| 4   | Iowa                 | $251k  | $241k   | Des Moines, Cedar Rapids, Iowa City                          |
| 5   | Missouri             | $281k  | $272k   | Kansas City, St. Louis, Springfield                          |
| 6   | Wisconsin            | $338k  | $342k   | Milwaukee, Madison, Green Bay                                |
| 7   | Alabama              | $299k  | $242k   | Birmingham, Huntsville, Mobile                               |
| 8   | Kentucky             | $277k  | $235k   | Louisville, Lexington                                        |
| 9   | Pennsylvania         | $308k  | $294k   | Pittsburgh, Philadelphia, Lancaster                          |
| 10  | Tennessee            | $392k  | $339k   | Memphis, Nashville, Knoxville, Chattanooga                   |
| 11  | Nebraska             | $307k  | $284k   | Omaha, Lincoln                                               |
| 12  | North Dakota         | $310k  | $294k   | Fargo, Bismarck                                              |
| 13  | Michigan             | $270k  | $270k   | Detroit, Grand Rapids, Lansing, Flint                        |
| 14  | West Virginia        | $253k  | $183k   | Charleston, Huntington, Morgantown                           |
| 15  | Kansas               | $302k  | $253k   | Wichita, Kansas City–KS, Topeka                              |
| 16  | Georgia              | $374k  | $335k   | Atlanta, Athens, Augusta, Savannah                           |
| 17  | Mississippi          | $265k  | $198k   | Jackson, Gulfport, Hattiesburg                               |
| 18  | South Carolina       | $398k  | $309k   | Greenville, Columbia, Charleston                             |
| 19  | Oklahoma             | $257k  | $225k   | Oklahoma City, Tulsa                                         |
| 20  | North Carolina       | $382k  | $340k   | Raleigh, Charlotte, Greensboro                               |
| 21  | South Dakota         | $318k  | $326k   | Sioux Falls, Rapid City                                      |
| 22  | Illinois             | $314k  | $299k   | Chicago, Peoria, Rockford, Springfield                       |
| 23  | Texas                | $342k  | $303k   | Houston, Dallas–Fort Worth, San Antonio, Austin              |
| 24  | Virginia             | $462k  | $420k   | Richmond, Virginia Beach, Northern Virginia                  |
| 25  | New Mexico           | $378k  | $321k   | Albuquerque, Santa Fe, Las Cruces                            |
| 26  | Minnesota            | $354k  | $357k   | Minneapolis–St. Paul, Duluth, Rochester                      |
| 27  | Louisiana            | $260k  | $218k   | New Orleans, Baton Rouge, Lafayette                          |
| 28  | Alaska               | $400k  | $401k   | Anchorage, Fairbanks                                         |
| 29  | Vermont              | $438k  | $402k   | Burlington                                                   |
| 30  | Maine                | $390k  | $424k   | Portland, Bangor                                             |
| 31  | Idaho                | $476k  | $482k   | Boise, Idaho Falls, Coeur d’Alene                            |
| 32  | Florida              | $417k  | $378k   | Tampa, Orlando, Jacksonville, Miami                          |
| 33  | Wyoming              | $440k  | $373k   | Cheyenne, Casper                                             |
| 34  | Utah                 | $575k  | $542k   | Salt Lake City, Provo, Ogden                                 |
| 35  | Montana              | $506k  | $476k   | Billings, Missoula, Bozeman                                  |
| 36  | Nevada               | $469k  | $448k   | Las Vegas, Reno                                              |
| 37  | Connecticut          | $445k  | $455k   | Hartford, Bridgeport, New Haven                              |
| 38  | Delaware             | $366k  | $412k   | Wilmington, Dover                                            |
| 39  | Arizona              | $452k  | $423k   | Phoenix metro (incl. Tempe, Gilbert, Chandler, Mesa), Tucson |
| 40  | Maryland             | $447k  | $436k   | Baltimore, Montgomery / Prince George’s                      |
| 41  | New Hampshire        | $500k  | $523k   | Manchester–Nashua                                            |
| 42  | New York             | $596k  | $526k   | New York City, Buffalo, Rochester, Syracuse                  |
| 43  | New Jersey           | $545k  | $585k   | Newark, Camden, New Brunswick                                |
| 44  | Rhode Island         | $535k  | $517k   | Providence                                                   |
| 45  | Massachusetts        | $645k  | $673k   | Boston, Worcester, Springfield                               |
| 46  | Hawaii               | $773k  | $837k   | Honolulu                                                     |
| 47  | Colorado             | $605k  | $543k   | Denver, Colorado Springs, Fort Collins                       |
| 48  | Oregon               | $508k  | $504k   | Portland, Salem, Eugene                                      |
| 49  | Washington           | $644k  | $603k   | Seattle, Tacoma, Spokane                                     |
| 50  | California           | $854k  | $776k   | Los Angeles, Bay Area, San Diego, Sacramento                 |
| 51  | District of Columbia | $676k  | $579k   | Washington, D.C.                                             |


**Price-measure note:** Median sale and typical value are different measures — do not mix them in a yield formula. Prefer **median** for buy-box / gross-yield screens. Sources: [Forbes/Redfin state medians](https://www.forbes.com/advisor/mortgages/real-estate/median-home-prices-by-state/), [Zillow typical values](https://keepingupwithinflation.com/statistics/home-prices-by-state/), [Redfin June 2026 metro medians](https://www.redfin.com/news/home-prices-record-high-june-2026/) for city figures below. North Dakota / Wyoming medians from the same May 2026 Redfin-based series via [World Population Review](https://worldpopulationreview.com/state-rankings/median-home-price-by-state).

### 4c. Top job industries (same order)
[↑ Back to Index](#index)


**Source framing:** Industry mix is based on Bureau of Labor Statistics May 2026 state industry employment (CES supersectors: trade/transportation/utilities, education & health, government, professional & business services, manufacturing, leisure & hospitality, etc.) from the [BLS industry-employment-by-state chart](https://www.bls.gov/charts/state-employment-and-unemployment/industry-employment-by-state.htm) and metro economy summaries. Sectors are listed largest-first in plain English. Exact headcount shares vary by release revision.


| #   | State                | Top industries (largest →)                                                          | Concentration / renter note                                                |
| --- | -------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | Ohio                 | Trade / logistics; education & health; government; manufacturing                    | Healthcare + manufacturing; Columbus gov / education / tech                |
| 2   | Indiana              | Trade / logistics; manufacturing; education & health; government                    | Manufacturing share still above U.S. average                               |
| 3   | Arkansas             | Trade / logistics; education & health; government; professional services            | Moderate diversification                                                   |
| 4   | Iowa                 | Trade / logistics; education & health; government; manufacturing                    | Ag / manufacturing exposure outside Des Moines                             |
| 5   | Missouri             | Trade / logistics; education & health; government; professional services            | KC logistics / finance; STL health / corporate                             |
| 6   | Wisconsin            | Trade / logistics; education & health; manufacturing; government                    | Manufacturing share still meaningful                                       |
| 7   | Alabama              | Government; trade / logistics; manufacturing; education & health                    | Diversified; manufacturing still material                                  |
| 8   | Kentucky             | Trade / logistics; education & health; manufacturing; government                    | Auto / logistics corridors matter                                          |
| 9   | Pennsylvania         | Education & health; trade / logistics; government; professional services            | Healthcare heavy; Philadelphia / Pittsburgh diverge                        |
| 10  | Tennessee            | Trade / logistics; education & health; professional services; government            | Nashville health / corporate; Memphis logistics                            |
| 11  | Nebraska             | Trade / logistics; education & health; government; professional / finance           | Omaha insurance / logistics anchors                                        |
| 12  | North Dakota         | Trade / logistics; government; education & health; energy / mining-adjacent         | Energy boom-bust risk outside Fargo                                        |
| 13  | Michigan             | Trade / logistics; education & health; manufacturing; professional services         | Auto manufacturing still a metro concentration risk (Detroit)              |
| 14  | West Virginia        | Government; trade / logistics; education & health; mining-adjacent                  | Government + legacy energy / mining risk                                   |
| 15  | Kansas               | Trade / logistics; government; education & health; manufacturing                    | Aviation / manufacturing pockets (Wichita)                                 |
| 16  | Georgia              | Trade / logistics; education & health; professional services; government            | Atlanta logistics / film / corporate services                              |
| 17  | Mississippi          | Trade / logistics; government; education & health; manufacturing                    | Lower diversification; weaker wage base                                    |
| 18  | South Carolina       | Trade / logistics; education & health; manufacturing; government                    | Auto / manufacturing + ports                                               |
| 19  | Oklahoma             | Trade / logistics; government; education & health; energy-adjacent                  | Energy concentration risk                                                  |
| 20  | North Carolina       | Trade / logistics; education & health; professional services; government            | Research Triangle tech / finance; Charlotte banking                        |
| 21  | South Dakota         | Trade / logistics; education & health; government; financial / leisure              | Small scale; finance niches in Sioux Falls                                 |
| 22  | Illinois             | Trade / logistics; education & health; professional services; government            | Chicago finance / professional services dominate metro mix                 |
| 23  | Texas                | Trade / logistics; professional services; education & health; government            | Energy still signature in Houston; DFW more corporate / logistics          |
| 24  | Virginia             | Professional services; government; education & health; trade / logistics            | Federal / defense / cyber concentration (Northern Virginia)                |
| 25  | New Mexico           | Government; trade / logistics; education & health; professional / leisure           | Federal / labs / tourism mix                                               |
| 26  | Minnesota            | Education & health; trade / logistics; professional services; government            | Diversified Twin Cities corporate base                                     |
| 27  | Louisiana            | Trade / logistics; education & health; government; leisure / energy-adjacent        | Energy / petrochem concentration on Gulf                                   |
| 28  | Alaska               | Government; trade / logistics; education & health; leisure                          | Government share elevated                                                  |
| 29  | Vermont              | Education & health; trade / logistics; government; leisure                          | Small / seasonal leisure exposure                                          |
| 30  | Maine                | Education & health; trade / logistics; government; leisure                          | Health care + tourism seasonality                                          |
| 31  | Idaho                | Trade / logistics; government; education & health; professional / manufacturing     | Boise tech / services growing; still smaller base                          |
| 32  | Florida              | Trade / logistics; professional services; education & health; leisure / hospitality | Leisure / tourism seasonality is a real vacancy risk                       |
| 33  | Wyoming              | Government; trade / logistics; education & health; mining / energy                  | Energy / mining concentration; very small scale                            |
| 34  | Utah                 | Trade / logistics; professional services; education & health; government            | Salt Lake tech / professional services growth                              |
| 35  | Montana              | Trade / logistics; government; education & health; leisure                          | Thin private base outside Billings / Bozeman                               |
| 36  | Nevada               | Leisure / hospitality; trade / logistics; professional services; government         | Tourism / gaming concentration (Las Vegas)                                 |
| 37  | Connecticut          | Education & health; trade / logistics; government; professional services            | Health / insurance / finance tilt in metros                                |
| 38  | Delaware             | Trade / logistics; education & health; government; professional / finance           | Finance / corporate services overweighted vs size                          |
| 39  | Arizona              | Trade / logistics; education & health; professional services; government            | Broad Sun Belt mix; not single-employer                                    |
| 40  | Maryland             | Education & health; government; professional services; trade / logistics            | Federal / cyber / biotech spillover from D.C.                              |
| 41  | New Hampshire        | Trade / logistics; education & health; professional services; government            | Boston spillover professional / tech                                       |
| 42  | New York             | Education & health; trade / logistics; professional services; government            | NYC finance / professional services; upstate more health / gov / education |
| 43  | New Jersey           | Trade / logistics; education & health; professional services; government            | Pharma / logistics / NYC spillover                                         |
| 44  | Rhode Island         | Education & health; trade / logistics; government; professional services            | Small base; health / education anchors                                     |
| 45  | Massachusetts        | Education & health; professional services; trade / logistics; government            | Boston education / biotech / professional services                         |
| 46  | Hawaii               | Government; leisure / hospitality; trade / logistics; education & health            | Tourism + military/government concentration                                |
| 47  | Colorado             | Trade / logistics; professional services; government; education & health            | Diversified; Front Range professional services strong                      |
| 48  | Oregon               | Trade / logistics; education & health; professional services; government            | Portland tech / trade; state jobs soft recently                            |
| 49  | Washington           | Trade / logistics; education & health; professional services; government            | Seattle tech / trade concentration; aerospace legacy                       |
| 50  | California           | Education & health; trade / logistics; professional services; government            | Large & diversified; tech concentrated in metros                           |
| 51  | District of Columbia | Professional services; government; education & health                               | High federal / professional concentration — cyclical with federal payrolls |




### 4d. Demographics & income (same order)
[↑ Back to Index](#index)


**Source framing:** Built from this run’s live `data/income.json` and `data/demographics.json` (pulled_at income=2026-07-26T06:22:24+00:00, demographics=2026-07-26T06:22:24+00:00). Median source: [https://fred.stlouisfed.org/release/tables?eid=259462&rid=249](https://fred.stlouisfed.org/release/tables?eid=259462&rid=249). Mean status: **unavailable**. Race rows use live ACS/`display` fields when present; otherwise `unavailable` (spec: no silent stale reuse). Demographics are tenant-pool / demand context only - not a ranking filter.


| #   | State                | Race / ethnicity (top groups)                                            | Median HH income | Mean HH income |
| --- | -------------------- | ------------------------------------------------------------------------ | ---------------- | -------------- |
| 1   | Ohio                 | NH White 76% · Black 12% · Hisp 4% · Asian 3%                            | $81k             | `unavailable`  |
| 2   | Indiana              | NH White 75% · Black 9% · Hisp 8% · Asian 2%                             | $77k             | `unavailable`  |
| 3   | Arkansas             | NH White 69% · Black 15% · Hisp 9% · Asian 2%                            | $65k             | `unavailable`  |
| 4   | Iowa                 | NH White 83% · Hisp 7% · Black 4% · Asian 2%                             | $85k             | `unavailable`  |
| 5   | Missouri             | NH White 76% · Black 11% · Hisp 5% · Asian 2%                            | $78k             | `unavailable`  |
| 6   | Wisconsin            | NH White 79% · Hisp 8% · Black 6% · Asian 3%                             | $83k             | `unavailable`  |
| 7   | Alabama              | NH White 63% · Black 26% · Hisp 5% · Asian 2%                            | $66k             | `unavailable`  |
| 8   | Kentucky             | NH White 81% · Black 8% · Hisp 5% · Asian 2%                             | $65k             | `unavailable`  |
| 9   | Pennsylvania         | NH White 73% · Black 11% · Hisp 8% · Asian 4%                            | $80k             | `unavailable`  |
| 10  | Tennessee            | NH White 71% · Black 16% · Hisp 7% · Asian 2%                            | $76k             | `unavailable`  |
| 11  | Nebraska             | NH White 76% · Hisp 12% · Black 5% · Asian 3%                            | $86k             | `unavailable`  |
| 12  | North Dakota         | NH White 82% · Native 5% · Hisp 4% · Black 3%                            | $88k             | `unavailable`  |
| 13  | Michigan             | NH White 72% · Black 13% · Hisp 6% · Asian 3%                            | $79k             | `unavailable`  |
| 14  | West Virginia        | NH White 89% · Black 4% · Hisp 2% · Asian 1%                             | $63k             | `unavailable`  |
| 15  | Kansas               | NH White 72% · Hisp 13% · Black 6% · Asian 3%                            | $88k             | `unavailable`  |
| 16  | Georgia              | NH White 50% · Black 31% · Hisp 10% · Asian 4%                           | $81k             | `unavailable`  |
| 17  | Mississippi          | NH White 55% · Black 36% · Hisp 4% · Asian 1%                            | $56k             | `unavailable`  |
| 18  | South Carolina       | NH White 62% · Black 25% · Hisp 7% · Asian 2%                            | $77k             | `unavailable`  |
| 19  | Oklahoma             | NH White 61% · Hisp 12% · Native 8% · Black 7% · Multiracial 9%          | $65k             | `unavailable`  |
| 20  | North Carolina       | NH White 60% · Black 20% · Hisp 11% · Asian 3%                           | $67k             | `unavailable`  |
| 21  | South Dakota         | NH White 80% · Native 8% · Hisp 4% · Black 2%                            | $80k             | `unavailable`  |
| 22  | Illinois             | NH White 58% · Hisp 18% · Black 14% · Asian 6%                           | $84k             | `unavailable`  |
| 23  | Texas                | NH White 40% · Hisp 39% · Black 12% · Asian 5%                           | $81k             | `unavailable`  |
| 24  | Virginia             | NH White 59% · Black 18% · Hisp 11% · Asian 7%                           | $98k             | `unavailable`  |
| 25  | New Mexico           | Hisp 48% · NH White 37% · Native 9% · Black 2%                           | $64k             | `unavailable`  |
| 26  | Minnesota            | NH White 76% · Black 7% · Asian 5% · Hisp 6%                             | $92k             | `unavailable`  |
| 27  | Louisiana            | NH White 56% · Black 31% · Hisp 7% · Asian 2%                            | $61k             | `unavailable`  |
| 28  | Alaska               | NH White 58% · Native 15% · Multiracial 10% · Hisp 7% · Asian 6%         | $91k             | `unavailable`  |
| 29  | Vermont              | NH White 89% · Hisp 2% · Asian 2% · Black 1%                             | $85k             | `unavailable`  |
| 30  | Maine                | NH White 90% · Hisp 2% · Black 2% · Asian 1%                             | $91k             | `unavailable`  |
| 31  | Idaho                | NH White 79% · Hisp 13% · Asian 1% · Native 1%                           | $82k             | `unavailable`  |
| 32  | Florida              | NH White 52% · Hisp 26% · Black 15% · Asian 3%                           | $76k             | `unavailable`  |
| 33  | Wyoming              | NH White 81% · Hisp 10% · Native 2% · Black 1%                           | $79k             | `unavailable`  |
| 34  | Utah                 | NH White 75% · Hisp 15% · Asian 2% · Pacific Isl. 1%                     | $104k            | `unavailable`  |
| 35  | Montana              | NH White 83% · Native 6% · Hisp 4% · Multiracial 5%                      | $82k             | `unavailable`  |
| 36  | Nevada               | NH White 46% · Hisp 29% · Black 9% · Asian 9%                            | $81k             | `unavailable`  |
| 37  | Connecticut          | NH White 63% · Hisp 17% · Black 10% · Asian 5%                           | $99k             | `unavailable`  |
| 38  | Delaware             | NH White 59% · Black 22% · Hisp 11% · Asian 4%                           | $86k             | `unavailable`  |
| 39  | Arizona              | NH White 53% · Hisp 31% · Black 4% · Native 4% · Asian 3%                | $85k             | `unavailable`  |
| 40  | Maryland             | NH White 47% · Black 29% · Hisp 12% · Asian 7%                           | $110k            | `unavailable`  |
| 41  | New Hampshire        | NH White 87% · Hisp 4% · Asian 3% · Black 1%                             | $112k            | `unavailable`  |
| 42  | New York             | NH White 52% · Hisp 20% · Black 14% · Asian 9%                           | $87k             | `unavailable`  |
| 43  | New Jersey           | NH White 52% · Hisp 22% · Black 12% · Asian 10%                          | $104k            | `unavailable`  |
| 44  | Rhode Island         | NH White 69% · Hisp 17% · Black 5% · Asian 4%                            | $92k             | `unavailable`  |
| 45  | Massachusetts        | NH White 68% · Hisp 13% · Asian 7% · Black 7%                            | $114k            | `unavailable`  |
| 46  | Hawaii               | Asian 37% · Multiracial 20% · NH White 22% · Pacific Isl. 10% · Hisp 10% | $98k             | `unavailable`  |
| 47  | Colorado             | NH White 65% · Hisp 22% · Black 4% · Asian 3%                            | $106k            | `unavailable`  |
| 48  | Oregon               | NH White 72% · Hisp 14% · Asian 5% · Black 2%                            | $90k             | `unavailable`  |
| 49  | Washington           | NH White 64% · Hisp 14% · Asian 9% · Black 4%                            | $98k             | `unavailable`  |
| 50  | California           | Hisp 39% · NH White 35% · Asian 15% · Black 5%                           | $101k            | `unavailable`  |
| 51  | District of Columbia | Black 41% · NH White 38% · Hisp 11% · Asian 5%                           | $105k            | `unavailable`  |




### 4e. Entry capital & shock reserves (same order)
[↑ Back to Index](#index)


**Screen framing (not a lender quote):** Investor default **25% down** + **~3% closing** ⇒ cash to close ≈ **28%** of buy-box **median**. Loan priced at **7.5%** midpoint of the July 2026 ~7.0%–8.5% investor band, 30-year amortizing. Shock liquid = **6 months** (or **9** in high-insurance / high-tax / soft-rent / heavy-regulation states) of estimated PITI (principal & interest + property tax screen + landlord insurance screen). **Total recommended liquid** = cash to close + shock. Recompute on metro/suburb prices when they diverge — see deep dives.

| # | State | Down | Cash to close | Shock liquid | Total liquid |
|---:|---|---:|---:|---:|---:|
| 1 | Ohio | 25% | $74k | $11k (6 mo) | $84k |
| 2 | Indiana | 25% | $76k | $10k (6 mo) | $87k |
| 3 | Arkansas | 25% | $76k | $10k (6 mo) | $86k |
| 4 | Iowa | 25% | $70k | $10k (6 mo) | $81k |
| 5 | Missouri | 25% | $79k | $11k (6 mo) | $90k |
| 6 | Wisconsin | 25% | $95k | $14k (6 mo) | $109k |
| 7 | Alabama | 25% | $84k | $11k (6 mo) | $95k |
| 8 | Kentucky | 25% | $78k | $11k (6 mo) | $88k |
| 9 | Pennsylvania | 25% | $86k | $13k (6 mo) | $99k |
| 10 | Tennessee | 25% | $110k | $14k (6 mo) | $124k |
| 11 | Nebraska | 25% | $86k | $13k (6 mo) | $99k |
| 12 | North Dakota | 25% | $87k | $12k (6 mo) | $99k |
| 13 | Michigan | 25% | $76k | $11k (6 mo) | $87k |
| 14 | West Virginia | 25% | $71k | $9k (6 mo) | $80k |
| 15 | Kansas | 25% | $85k | $12k (6 mo) | $97k |
| 16 | Georgia | 25% | $105k | $14k (6 mo) | $119k |
| 17 | Mississippi | 25% | $74k | $16k (9 mo) | $90k |
| 18 | South Carolina | 25% | $111k | $22k (9 mo) | $134k |
| 19 | Oklahoma | 25% | $72k | $16k (9 mo) | $88k |
| 20 | North Carolina | 25% | $107k | $14k (6 mo) | $121k |
| 21 | South Dakota | 25% | $89k | $13k (6 mo) | $102k |
| 22 | Illinois | 25% | $88k | $21k (9 mo) | $109k |
| 23 | Texas | 25% | $96k | $23k (9 mo) | $118k |
| 24 | Virginia | 25% | $129k | $17k (6 mo) | $147k |
| 25 | New Mexico | 25% | $106k | $14k (6 mo) | $120k |
| 26 | Minnesota | 25% | $99k | $14k (6 mo) | $113k |
| 27 | Louisiana | 25% | $73k | $16k (9 mo) | $89k |
| 28 | Alaska | 25% | $112k | $15k (6 mo) | $127k |
| 29 | Vermont | 25% | $123k | $18k (6 mo) | $141k |
| 30 | Maine | 25% | $109k | $15k (6 mo) | $124k |
| 31 | Idaho | 25% | $133k | $17k (6 mo) | $151k |
| 32 | Florida | 25% | $117k | $25k (9 mo) | $142k |
| 33 | Wyoming | 25% | $123k | $16k (6 mo) | $139k |
| 34 | Utah | 25% | $161k | $20k (6 mo) | $182k |
| 35 | Montana | 25% | $142k | $19k (6 mo) | $160k |
| 36 | Nevada | 25% | $131k | $17k (6 mo) | $148k |
| 37 | Connecticut | 25% | $125k | $19k (6 mo) | $143k |
| 38 | Delaware | 25% | $103k | $13k (6 mo) | $116k |
| 39 | Arizona | 25% | $127k | $16k (6 mo) | $143k |
| 40 | Maryland | 25% | $125k | $17k (6 mo) | $142k |
| 41 | New Hampshire | 25% | $140k | $20k (6 mo) | $161k |
| 42 | New York | 25% | $167k | $35k (9 mo) | $202k |
| 43 | New Jersey | 25% | $153k | $36k (9 mo) | $189k |
| 44 | Rhode Island | 25% | $150k | $21k (6 mo) | $171k |
| 45 | Massachusetts | 25% | $181k | $24k (6 mo) | $205k |
| 46 | Hawaii | 25% | $217k | $39k (9 mo) | $256k |
| 47 | Colorado | 25% | $169k | $22k (6 mo) | $191k |
| 48 | Oregon | 25% | $142k | $28k (9 mo) | $171k |
| 49 | Washington | 25% | $180k | $36k (9 mo) | $216k |
| 50 | California | 25% | $239k | $46k (9 mo) | $286k |
| 51 | District of Columbia | 25% | $189k | $36k (9 mo) | $225k |


### Notes on score changes from the prior re-run
[↑ Back to Index](#index)


- **Wisconsin cash flow** edged down because statewide effective property taxes are elevated (~1.5% range).
- **Texas / Florida / Louisiana / Oklahoma / Mississippi cash flow** stay haircut for insurance even when owner law is excellent.
- **New Jersey cash flow** stays weak because of both regulation and the nation’s highest effective property-tax rate (~2.23%).
- Small states like **North Dakota** and **West Virginia** still post strong raw economics but rank lower on actionability due to scale and exit liquidity.



### Strict economic-composite buckets
[↑ Back to Index](#index)



| Composite | States                                          |
| --------- | ----------------------------------------------- |
| 8.25      | Ohio, Indiana, Arkansas, Iowa                   |
| 8.00      | North Dakota, West Virginia                     |
| 7.75      | Missouri, Alabama, Kentucky                     |
| 7.50      | Wisconsin*, Nebraska, Mississippi               |
| 7.25      | Pennsylvania, Tennessee, Kansas, South Dakota   |
| 7.00      | Michigan                                        |
| 6.75      | Georgia, Illinois                               |
| 6.50      | South Carolina, North Carolina, Alaska, Vermont |
| 6.25      | Oklahoma, Louisiana                             |
| 6.00      | New Mexico, Minnesota, Maine                    |
| 5.75      | Texas, Virginia, Idaho, Wyoming, Connecticut    |
| 5.50      | New Hampshire                                   |
| 5.25      | Montana, Nevada, Delaware, New York             |
| 5.00      | Utah, Maryland, New Jersey                      |
| 4.75      | Florida, Arizona                                |
| 4.50      | Hawaii                                          |
| 4.25      | Rhode Island, Massachusetts                     |
| 3.75      | Colorado                                        |
| 3.50      | Oregon                                          |
| 3.25      | Washington                                      |
| 2.75      | California                                      |
| 2.50      | District of Columbia                            |


Wisconsin’s actionable rank remains high despite a slightly lower cash-flow score after tax haircut.

---

---



## 5. City leaderboards
[↑ Back to Index](#index)


Metro **median sale prices** below are Redfin June 2026 unless labeled as an investor/study screen. True metro **average** sale prices are often unpublished — marked unavailable rather than invented. State median / typical pairs are already in Section 4. **Top suburbs** for major metros are listed later in this section (cash-flow vs appreciation angles). State **top industries** are in Section **4c**; **demographics & income** in Section **4d**; metro industry / income / race notes appear in deep dives.

### Cash-flow potential (gross yield is a screen)
[↑ Back to Index](#index)



| Rank | Metro                      | Median / screen price            | Current evidence                                 | Judgment                                               |
| ---- | -------------------------- | -------------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| 1    | Detroit, Michigan          | ~$85k (city screen)              | $1,350 achieved 3-bedroom rent / ~19% gross      | Highest headline yield; highest condition / block risk |
| 2    | Jackson, Mississippi       | ~$88k (study screen)             | ~17% gross in one mid-2026 study                 | Strong income screen; insurance and liquidity haircut  |
| 3    | Cleveland, Ohio            | $274,179 (metro)                 | ~11–12% gross; typical rent ~$1,461              | Best balance among very-high-yield metros              |
| 4    | Birmingham, Alabama        | unavailable (use AL $299k state) | Typical rent ~$1,448; studies ~11% gross         | Strong cash flow; rising concessions                   |
| 5    | Memphis, Tennessee         | ~$165k (investor screen)         | $1,350 rent / ~9.8% gross; typical rent ~$1,441  | Strong income; management-intensive                    |
| 6    | Milwaukee, Wisconsin       | $378,866 (metro)                 | ~9.4% gross on older comps; typical rent ~$1,538 | Yield plus appreciation strength; watch taxes          |
| 7    | Baltimore, Maryland        | $438,686 (metro)                 | ~10.3% gross on older comps                      | High gross income; more legal / operating friction     |
| 8    | Philadelphia, Pennsylvania | $337,988 (metro)                 | ~8.7% gross on older comps                       | Large-market scale                                     |
| 9    | Pittsburgh, Pennsylvania   | $291,527 (metro)                 | ~8.4% gross on older comps                       | Affordable and stable; older stock                     |
| 10   | Indianapolis, Indiana      | $324,030 (metro)                 | ~8.2% gross; typical rent ~$1,553                | Most repeatable turnkey single-family profile          |




### Best for single-family houses
[↑ Back to Index](#index)


1. Indianapolis
2. Columbus / Cincinnati
3. Kansas City
4. Des Moines
5. Northwest Arkansas (growth)
6. Raleigh (jobs; thinner day-one income)
7. Huntsville
8. Milwaukee suburbs
9. Houston / San Antonio (scale; tax + insurance caution)
10. St. Louis selected neighborhoods



### Best for 2–4 unit multifamily homes
[↑ Back to Index](#index)


1. Cleveland
2. Detroit suburbs (not every Detroit address)
3. Memphis
4. Birmingham
5. Indianapolis
6. Pittsburgh
7. Buffalo / Rochester
8. Milwaukee
9. Louisville
10. Philadelphia selected neighborhoods

**Why the split:** 2026 investor-loan comparisons and duplex/fourplex market guides keep pointing to Midwest cash-flow cities for small multifamily, while single-family stays preferable where management simplicity and resale to owner-occupants matter more.

### Top suburbs worth researching (live 2026 screen)
[↑ Back to Index](#index)


National ranks stay at the **metro** level. These are the **suburbs / submarkets** inside those metros that live research keeps highlighting for rental buyers. Angles: **CF** = cash-flow tilted · **Bal** = balanced · **App** = appreciation / tenant-quality tilted.


| Parent metro              | Top suburbs / submarkets                  | Angle   | 2026 evidence (rounded)                                                                                                                                                                                                             | Caution                                                      |
| ------------------------- | ----------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **Phoenix, AZ**           | Buckeye, Surprise, Avondale               | CF      | Typical values ~$395k–$422k; gross yields ~5.3%–6.0% ([Lux AZ, Mar 2026 ZHVI/ZORI](https://luxazrentals.com/phoenix-metro-cap-rates-2026/))                                                                                         | Newer fringe product; underwrite insurance and commute       |
| **Phoenix, AZ**           | Mesa, Tempe                               | Bal     | Mesa ~$435k / ~4.3% gross; Tempe ~$468k / ~4.3% gross; ASU + East Valley jobs                                                                                                                                                       | Soft metro rents YoY; not a thick cash-flow print            |
| **Phoenix, AZ**           | Gilbert, Chandler                         | App     | Gilbert ~$573k / ~4.3% gross; Chandler ~$524k / ~4.3% gross; strong schools / tech corridor                                                                                                                                         | Prestige premium compresses day-one yield                    |
| **Cleveland, OH**         | Lakewood, Parma, Cleveland Heights        | Bal     | Inner-ring suburbs; published screens ~$195k–$235k with stronger tenant tenure than deep city deals                                                                                                                                 | Taxes still bite; lower gross than city C-class              |
| **Cleveland, OH**         | Maple Heights / Garfield Heights          | CF      | Inner-ring value screens ~$110k–$150k in investor guides                                                                                                                                                                            | Block selection matters                                      |
| **Columbus, OH**          | Hilliard, Westerville                     | Bal/App | Suburb screens ~$385k–$415k; Intel-adjacent demand                                                                                                                                                                                  | Thinner yield than Cleveland                                 |
| **Columbus, OH**          | New Albany                                | App     | Premium suburb screens ~$525k+                                                                                                                                                                                                      | Growth premium, not cash-flow first                          |
| **Indianapolis, IN**      | Noblesville, Greenwood                    | Bal/CF  | Noblesville often cited as best Hamilton County entry; Greenwood cheaper south-side workforce demand                                                                                                                                | Rising concessions metro-wide                                |
| **Indianapolis, IN**      | Fishers, Carmel                           | App     | Hamilton County premium rents / schools; Carmel median home ~$475k in 2026 local guides                                                                                                                                             | Higher entry; thinner day-one cash flow                      |
| **Kansas City, MO**       | Independence, MO                          | CF      | 3BR buy box often ~$170k–$220k; rents ~$1,100–$1,400; ~6%–8% cap screens ([Alpine KC 2026](https://www.alpinekansascity.com/2026/03/13/is-independence-missouri-still-one-of-the-best-cash-flow-markets-in-the-kansas-city-metro/)) | Neighborhood variance inside Independence                    |
| **Kansas City, MO**       | Overland Park / Lee’s Summit              | App     | Much higher entry (~$350k–$450k screens)                                                                                                                                                                                            | Yield thinner than Independence                              |
| **Dallas–Fort Worth, TX** | Frisco, McKinney, Plano                   | App/Bal | North Collin growth / schools corridor; McKinney often the balanced pick                                                                                                                                                            | Tax + insurance; not Midwest-style yields                    |
| **Dallas–Fort Worth, TX** | Forney, Mansfield                         | CF/Bal  | Edge / south-side value plays for better rent-to-price                                                                                                                                                                              | Confirm insurance and new supply                             |
| **Houston, TX**           | Katy, Cypress, Spring / Klein             | Bal     | Family-suburb screens; guides often ~$300k–$420k with ~6%–8% gross ranges                                                                                                                                                           | Flood / insurance underwriting first                         |
| **Houston, TX**           | Pearland / Friendswood                    | App/Bal | Established schools / tenure                                                                                                                                                                                                        | Higher entry than Spring corridor                            |
| **Atlanta, GA**           | (metro still softer on yield)             | Bal     | Prefer job-pocket suburbs near strong employers; Athens remains the standout job-growth sibling                                                                                                                                     | Concessions; avoid treating all Atlanta suburbs as cash-flow |
| **Seattle, WA**           | Spokane (alt metro) over Eastside suburbs | Watch   | Eastside / Seattle proper remain expensive + rent-capped statewide                                                                                                                                                                  | Prefer Spokane value screen vs Bellevue/Redmond for income   |


**How to use this table:** pick the **parent metro** from Sections 3–5, then shortlist suburbs by angle (CF vs App) before ZIP underwriting. Suburb yields above are mostly **gross / typical-value screens**, not cash-on-cash.

### Appreciation leaders (first-quarter 2026, Federal Housing Finance Agency)
[↑ Back to Index](#index)



| Rank | Metro                            | Year-over-year |
| ---- | -------------------------------- | -------------- |
| 1    | Peoria, Illinois                 | 9.03%          |
| 2    | Syracuse, New York               | 8.96%          |
| 3    | Pensacola, Florida               | 8.71%          |
| 4    | Bridgeport–Stamford, Connecticut | 8.35%          |
| 5    | Billings, Montana                | 8.12%          |
| 6    | Jefferson City, Missouri         | 7.96%          |
| 7    | Lancaster, Pennsylvania          | 7.60%          |
| 8    | Anchorage, Alaska                | 7.58%          |
| 9    | Janesville–Beloit, Wisconsin     | 7.58%          |
| 10   | Reading, Pennsylvania            | 7.57%          |


One-year appreciation is backward-looking. Austin, Texas statewide, Colorado, and several pandemic-boom markets are still digesting elevated supply / prices.

### Job-market leaders (May 2026 payroll changes)
[↑ Back to Index](#index)



| Rank | Metro                                    | Evidence            |
| ---- | ---------------------------------------- | ------------------- |
| 1    | Las Vegas, Nevada                        | +24,500 jobs; +2.1% |
| 2    | Salt Lake City, Utah                     | +17,800; +2.1%      |
| 3    | San Jose, California                     | +17,600; +1.5%      |
| 4    | Raleigh, North Carolina                  | +16,700; +2.2%      |
| 5    | Greenville, South Carolina               | +10,600; +2.2%      |
| 6    | Fresno, California                       | +9,100; +2.0%       |
| 7    | Fayetteville–Springdale–Rogers, Arkansas | +7,700; +2.5%       |
| 8    | Athens, Georgia                          | +3,200; +3.0%       |


**Weakest confirmed large metros:** Washington–Arlington–Alexandria (−100,500; −3.0%) and Portland–Vancouver–Hillsboro (−35,000; −2.8%).

### Best balanced city shortlist
[↑ Back to Index](#index)


1. Cleveland — yield, owner-friendly law, improving jobs, price strength; excellent duplex/triplex market
2. Indianapolis — scalable management and consistent rent demand
3. Kansas City — diversified economy and balanced acquisition costs
4. Milwaukee — rent growth plus strong appreciation
5. Cincinnati — affordable relative to metro size
6. Pittsburgh — high yield and institutional employment base
7. St. Louis — good rent-to-price with careful neighborhood underwriting
8. Columbus — lower yield than Cleveland, stronger growth profile
9. Northwest Arkansas — strongest smaller-metro growth thesis
10. Birmingham — cash-flow leader with favorable law and low taxes
11. Memphis — high-income strategy requiring strong management
12. Raleigh — strong jobs, weaker immediate cash flow
13. Greenville, South Carolina — jobs and migration; moderate entry
14. Houston — scale and population growth; taxes and insurance matter
15. Philadelphia — large-market liquidity and strong gross-rent potential

---



## 6. All-state deep dives
[↑ Back to Index](#index)


Deep dives for **all 50 states + D.C.** in actionable-rank order. Same field labels throughout: Scores, Prices, Entry capital, Top industries, Demographics / income, Top suburbs, Best fit, Risks, Confidence. [↑ Index](#index) · [A–Z](#az-actionable-rank-index)

### Ohio
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 8 / Cash flow 9 / Appreciation 8 / Owner law 9 / Tenant law 2  

**Prices:** State median **$262,900** / typical **$251,502**. Cleveland metro median **$274,179**; Cincinnati **$324,030**; Columbus **$368,895** (Redfin June 2026).  
**Entry capital:** **25% down** (investor default). On state median **$262,900**: cash to close ≈ **$74k** (25% + ~3% closing); recommended shock liquid ≈ **$11k** (6 mo PITI screen); **total recommended liquid ≈ $84k**. Metro screens: Cleveland median **$274,179** → cash to close ~**$77k**, total liquid ~**$88k**; Columbus median **$368,895** → cash to close ~**$103k**, total liquid ~**$118k**; Cincinnati median **$324,030** → cash to close ~**$91k**, total liquid ~**$104k**. Suburb note: Maple Heights / Garfield Heights CF screens need less cash than New Albany / Hilliard appreciation corridors.  
**Top industries:** Trade / logistics; education & health; government; manufacturing. Cleveland leans health + manufacturing; Columbus adds government / education / tech (Intel-adjacent).  
**Demographics / income:** NH White 76% · Black 12% · Hisp 4% · Asian 3%. State median HH income **$81k** (CPS 2024); mean HH income `unavailable`. Cleveland metro ~~NH White mid-60s% / Black ~19% / Hisp ~6%; Columbus metro more White + growing Asian share. Cleveland city itself is majority-Black (~~46% Black alone). Cleveland / Columbus metro ACS median incomes not in top-25 table — use state **$81k** as screen.  
**Top suburbs:** Cleveland — Lakewood / Parma / Cleveland Heights (balanced tenure) and Maple Heights / Garfield Heights (cash-flow value); Columbus — Hilliard / Westerville (balanced) and New Albany (appreciation / Intel-adjacent).  

Unemployment fell from 4.6% to 3.6% year over year — the largest state decline in the June release. Cleveland’s June median sale price was about $274,179; typical rent about $1,461. Cleveland, Dayton, Toledo, and Akron show up repeatedly in high-yield research; Columbus is the growth / white-collar sibling. Statewide appreciation about +3.2%; Cleveland metro stronger. Property taxes are moderate-to-elevated (~1.4%), but insurance is generally more manageable than Gulf Coast markets. Duplex and triplex inventory is a real advantage here.

**Best fit:** Cleveland income (single-family or 2–4 unit); Columbus growth; Cincinnati balance.  
**Risks:** old systems, inspections, uneven neighborhoods.  
**Confidence:** High.

### Indiana
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 8 / Cash flow 9 / Appreciation 8 / Owner law 9 / Tenant law 2  

**Prices:** State median **$273,200** / typical **$262,265**. Indianapolis metro median **$324,030** (Redfin June 2026); Fort Wayne / South Bend metro medians `unavailable` in the top-50 print.  
**Entry capital:** **25% down** (investor default). On state median **$273,200**: cash to close ≈ **$76k** (25% + ~3% closing); recommended shock liquid ≈ **$10k** (6 mo PITI screen); **total recommended liquid ≈ $87k**. Metro screens: Indianapolis median **$324,030** → cash to close ~**$91k**, total liquid ~**$103k**. Suburb note: Noblesville / Greenwood entry usually below Carmel / Fishers school-suburb prices.  
**Top industries:** Trade / logistics; manufacturing; education & health; government. Indianapolis also has professional services + life-sciences growth.  
**Demographics / income:** NH White 75% · Black 9% · Hisp 8% · Asian 2%. State median HH income **$77k** (CPS 2024); mean HH income `unavailable`. Indianapolis metro ~NH White ~68–71% / Black ~15% / Hisp ~7–8% / Asian ~4%.  
**Top suburbs:** Noblesville and Greenwood for better entry / workforce demand; Fishers and Carmel for schools / appreciation (Carmel median home ~$475k in 2026 local guides).  

Unemployment 3.3%; statewide appreciation about +3.6%. Indianapolis typical rent about $1,553; gross yield screens near 8%. Rent-control preemption supports remote ownership. Effective property tax is relatively manageable (~0.8%). Bloomington’s payroll drop shows the state is not uniform. Concessions rose in Indianapolis — do not underwrite asking rent blindly.

**Best fit:** Indianapolis turnkey single-family; Fort Wayne value; selected duplexes where rents stack.  
**Risks:** concessions; slower wage growth.  
**Confidence:** High.

### Arkansas
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 9 / Cash flow 8 / Appreciation 8 / Owner law 9 / Tenant law 2  

**Prices:** State median **$270,300** / typical **$228,662**. Little Rock and Northwest Arkansas city medians `unavailable` in Redfin’s top-50 June table — use state pair + local MLS.  
**Entry capital:** **25% down** (investor default). On state median **$270,300**: cash to close ≈ **$76k** (25% + ~3% closing); recommended shock liquid ≈ **$10k** (6 mo PITI screen); **total recommended liquid ≈ $86k**.  

**Top industries:** Trade / logistics; education & health; government; professional services. Northwest Arkansas adds corporate / retail HQ demand.  

**Demographics / income:** NH White 69% · Black 15% · Hisp 9% · Asian 2%. State median HH income **$65k** (CPS 2024); mean HH income `unavailable`. State majority NH White; Northwest Arkansas more White/Asian growth; Little Rock / Delta Black share much higher than state average.  

Fayetteville–Springdale–Rogers added about 7,700 jobs (+2.5%). Statewide prices remain affordable; appreciation about +3.4%. Property taxes are low (~0.56%). Little Rock is the income screen; Northwest Arkansas is the growth screen.

**Best fit:** barbell of Northwest Arkansas single-family growth and Little Rock income / small multifamily.  
**Risks:** fast Northwest Arkansas repricing.  
**Confidence:** High.

### Iowa
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 9 / Cash flow 8 / Appreciation 8 / Owner law 9 / Tenant law 2  

**Prices:** State median **$250,700** / typical **$241,255** (among the lowest statewide entry costs). Des Moines / Cedar Rapids metro medians `unavailable` in the top-50 print.  
**Entry capital:** **25% down** (investor default). On state median **$250,700**: cash to close ≈ **$70k** (25% + ~3% closing); recommended shock liquid ≈ **$10k** (6 mo PITI screen); **total recommended liquid ≈ $81k**.  

**Top industries:** Trade / logistics; education & health; government; manufacturing. Des Moines finance / insurance is the metro differentiator.  

**Demographics / income:** NH White 83% · Hisp 7% · Black 4% · Asian 2%. State median HH income **$85k** (CPS 2024); mean HH income `unavailable`. Majority NH White statewide; Des Moines / meatpacking corridors have higher Hispanic shares than the state average.  

Unemployment 3.2%; appreciation about +3.5%. Des Moines has the deepest management market. Ames lost about 4% of payrolls. Property taxes are somewhat elevated (~1.35%), so net yields need a tax haircut even when purchase prices look cheap.

**Best fit:** conservative long-term single-family hold.  
**Risks:** thin resale pools; local employer risk.  
**Confidence:** Medium.

### Missouri
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 8 / Cash flow 8 / Appreciation 8 / Owner law 8 / Tenant law 3  

**Prices:** State median **$281,400** / typical **$271,597**. Kansas City metro median **$363,910**; St. Louis **$309,075** (Redfin June 2026).  
**Entry capital:** **25% down** (investor default). On state median **$281,400**: cash to close ≈ **$79k** (25% + ~3% closing); recommended shock liquid ≈ **$11k** (6 mo PITI screen); **total recommended liquid ≈ $90k**.  
**Top industries:** Trade / logistics; education & health; government; professional services. Kansas City = logistics / finance; St. Louis = health / corporate.  
**Demographics / income:** NH White 76% · Black 11% · Hisp 5% · Asian 2%. State median HH income **$78k** (CPS 2024); mean HH income `unavailable`. St. Louis and Kansas City metros have higher Black shares than the statewide mix; Independence / Northland diverge from city cores. St. Louis metro ACS 2024 median **$82k**.  
**Top suburbs:** Independence, MO remains the clearest Kansas City cash-flow suburb screen (~$170k–$220k 3BR buy box in 2026 local investor writeups); Overland Park / Lee’s Summit are higher-entry appreciation / tenant-quality plays.  

Unemployment 3.7%; appreciation about +3.9%. Kansas City typical rent about $1,548; St. Louis about $1,451 with solid annual rent growth. Property taxes mid-pack (~0.9%). Good remote-investor depth in both major metros.

**Best fit:** Kansas City balanced hold; St. Louis value / cash flow.  
**Risks:** municipal fragmentation and neighborhood variance.  
**Confidence:** High.

### Wisconsin
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 6 / Cash flow 7 / Appreciation 9 / Owner law 9 / Tenant law 2  

**Prices:** State median **$338,200** / typical **$342,279**. Milwaukee metro median **$378,866** (Redfin June 2026); Madison metro median `unavailable` in the top-50 print.  
**Entry capital:** **25% down** (investor default). On state median **$338,200**: cash to close ≈ **$95k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $109k**.  

**Top industries:** Trade / logistics; education & health; manufacturing; government. Milwaukee manufacturing + health anchors.  

**Demographics / income:** NH White 79% · Hisp 8% · Black 6% · Asian 3%. State median HH income **$83k** (CPS 2024); mean HH income `unavailable`. Milwaukee metro has a much higher Black share than the statewide ~6%; Madison skews Whiter / higher-income.  

Unemployment 3.3%; statewide appreciation about +4.5%. Milwaukee typical rent about $1,538 (+3.9% year over year) with strong published gross yields. The cash-flow score is tempered by higher property taxes (~1.5%). Madison is more expensive and more stability-oriented.

**Best fit:** Milwaukee income (single-family or small multifamily); Madison stability.  
**Risks:** taxes, winter capex, older buildings.  
**Confidence:** High.

### Alabama
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 8 / Cash flow 8 / Appreciation 7 / Owner law 9 / Tenant law 2  

**Prices:** State median **$299,000** / typical **$241,517**. Birmingham / Huntsville metro medians `unavailable` in Redfin top-50 — note the wide median-vs-typical gap (sale mix skew).  
**Entry capital:** **25% down** (investor default). On state median **$299,000**: cash to close ≈ **$84k** (25% + ~3% closing); recommended shock liquid ≈ **$11k** (6 mo PITI screen); **total recommended liquid ≈ $95k**.  

**Top industries:** Government; trade / logistics; manufacturing; education & health. Huntsville adds aerospace / defense / tech.  

**Demographics / income:** NH White 63% · Black 26% · Hisp 5% · Asian 2%. State median HH income **$66k** (CPS 2024); mean HH income `unavailable`. Birmingham / Montgomery Black shares well above state average; Huntsville Whiter / higher-income tech corridor.  

Unemployment 3.2%; among the lowest property-tax states (~0.38%). Birmingham repeatedly ranks as a national yield leader; typical rent about $1,448, but concessions rose and rent growth was only about 1.2%. Huntsville is the jobs / technology sibling. Insurance is a bigger issue than taxes.

**Best fit:** Birmingham income; Huntsville growth.  
**Risks:** insurance, concessions, city operating quality.  
**Confidence:** High.

### Kentucky
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 9 / Cash flow 8 / Appreciation 9 / Owner law 8 / Tenant law 3  

**Prices:** State median **$277,200** / typical **$235,363**. Louisville / Lexington metro medians `unavailable` in the top-50 print.  
**Entry capital:** **25% down** (investor default). On state median **$277,200**: cash to close ≈ **$78k** (25% + ~3% closing); recommended shock liquid ≈ **$11k** (6 mo PITI screen); **total recommended liquid ≈ $88k**.  

**Top industries:** Trade / logistics; education & health; manufacturing; government. Auto / logistics corridors support Louisville demand.  

**Demographics / income:** NH White 81% · Black 8% · Hisp 5% · Asian 2%. State median HH income **$65k** (CPS 2024); mean HH income `unavailable`. Louisville Black share above state average; Lexington more White / university-driven.  

Statewide appreciation about +4.7% (top-tier). Entry costs remain low. Louisville is the main scale market for both single-family and 2–4 units; Lexington adds university / healthcare demand. Unemployment 4.7% holds down the jobs score. Property taxes are moderate (~0.8%).

**Best fit:** affordable appreciation plus moderate cash flow.  
**Risks:** softer labor reading; smaller management depth.  
**Confidence:** Medium.

### Pennsylvania
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 7 / Cash flow 8 / Appreciation 8 / Owner law 7 / Tenant law 4  

**Prices:** State median **$308,500** / typical **$294,099**. Pittsburgh metro median **$291,527**; Philadelphia **$337,988**; Montgomery County suburbs **$548,358** (Redfin June 2026).  
**Entry capital:** **25% down** (investor default). On state median **$308,500**: cash to close ≈ **$86k** (25% + ~3% closing); recommended shock liquid ≈ **$13k** (6 mo PITI screen); **total recommended liquid ≈ $99k**. Metro screens: Philadelphia median **$408,776** → cash to close ~**$114k**, total liquid ~**$131k**.  

**Top industries:** Education & health; trade / logistics; government; professional services. Pittsburgh health / education; Philadelphia broader services.  

**Demographics / income:** NH White 73% · Black 11% · Hisp 8% · Asian 4%. State median HH income **$80k** (CPS 2024); mean HH income `unavailable`. Philadelphia metro far more diverse than statewide; Pittsburgh Whiter; both have ACS metro median incomes near ~$91k (2024). Philadelphia metro ACS 2024 median **$91k**.  

Statewide appreciation about +3.8%. Pittsburgh and Philadelphia both appear in national yield top tens; Lancaster and Reading lead recent appreciation lists. Philadelphia has more regulation and tax friction than the statewide score implies — city overrides matter.

**Best fit:** Pittsburgh balance / duplexes; Philadelphia income with experienced management.  
**Risks:** old housing, transfer taxes, city compliance.  
**Confidence:** High.

### Tennessee
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 6 / Cash flow 8 / Appreciation 7 / Owner law 9 / Tenant law 2  

**Prices:** State median **$392,100** / typical **$338,769**. Nashville metro median **$498,507** (Redfin June 2026); Memphis investor-screen ~**$165,000** (not a metro-wide Redfin print).  
**Entry capital:** **25% down** (investor default). On state median **$392,100**: cash to close ≈ **$110k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $124k**.  

**Top industries:** Trade / logistics; education & health; professional services; government. Memphis logistics; Nashville health / corporate / leisure.  

**Demographics / income:** NH White 71% · Black 16% · Hisp 7% · Asian 2%. State median HH income **$76k** (CPS 2024); mean HH income `unavailable`. Memphis Black share far above state; Nashville more diverse / higher-income than statewide median. Memphis / Nashville diverge sharply on race mix and income from statewide averages.  

Unemployment 3.5%; no state income tax on wages helps after-tax rental income. Memphis combines typical rent about $1,441 with high published yields and strong duplex / fourplex fit. Nashville is a higher-priced growth market with concessions and new supply. Property taxes are relatively low (~0.6%).

**Best fit:** Memphis cash flow (single-family or 2–4 unit); Nashville / Knoxville growth.  
**Risks:** Memphis operations; Nashville oversupply.  
**Confidence:** High.

### Nebraska
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 7 / Cash flow 7 / Appreciation 8 / Owner law 7 / Tenant law 3  

**Prices:** State median **$306,700** / typical **$284,464**. Omaha metro median `unavailable` in Redfin top-50.  
**Entry capital:** **25% down** (investor default). On state median **$306,700**: cash to close ≈ **$86k** (25% + ~3% closing); recommended shock liquid ≈ **$13k** (6 mo PITI screen); **total recommended liquid ≈ $99k**.  

**Top industries:** Trade / logistics; education & health; government; professional / finance (Omaha insurance).  

**Demographics / income:** NH White 76% · Hisp 12% · Black 5% · Asian 3%. State median HH income **$86k** (CPS 2024); mean HH income `unavailable`. Omaha / Lincoln drive income; Hispanic share rising in meatpacking and logistics corridors.  

Unemployment 2.9%; appreciation about +3.9%. Omaha diversifies insurance, logistics, finance, and healthcare. Yields are less spectacular than Ohio / Indiana but often more stable. Hail / storm insurance can still matter.

**Best fit:** conservative metro hold.  
**Confidence:** Medium.

### North Dakota
[↑ Back to Index](#index)


**Scores:** Jobs 10 / Price 7 / Cash flow 6 / Appreciation 9 / Owner law 8 / Tenant law 3  

**Prices:** State median **$310,500** / typical **$293,556**. Fargo metro median `unavailable` in Redfin top-50.  
**Entry capital:** **25% down** (investor default). On state median **$310,500**: cash to close ≈ **$87k** (25% + ~3% closing); recommended shock liquid ≈ **$12k** (6 mo PITI screen); **total recommended liquid ≈ $99k**.  

**Top industries:** Trade / logistics; government; education & health; energy-adjacent. Energy concentration outside Fargo.  

**Demographics / income:** NH White 82% · Native 5% · Hisp 4% · Black 3%. State median HH income **$88k** (CPS 2024); mean HH income `unavailable`. Fargo Whiter / higher-income; western energy counties and reservations diverge sharply.  

Unemployment 2.3%; appreciation about +4.0%. Fargo is the most diversified rental market. Strong raw economics, weaker scale / climate / liquidity — hence lower actionable rank than the raw composite.

**Best fit:** low-vacancy long hold.  
**Confidence:** Medium.

### Michigan
[↑ Back to Index](#index)


**Scores:** Jobs 4 / Price 8 / Cash flow 8 / Appreciation 8 / Owner law 8 / Tenant law 3  

**Prices:** State median **$269,700** / typical **$269,972**. Detroit city investor-screen ~**$85,000** (not metro-wide median); Grand Rapids metro median `unavailable` in top-50.  
**Entry capital:** **25% down** (investor default). On state median **$269,700**: cash to close ≈ **$76k** (25% + ~3% closing); recommended shock liquid ≈ **$11k** (6 mo PITI screen); **total recommended liquid ≈ $87k**.  

**Top industries:** Trade / logistics; education & health; manufacturing; professional services. Detroit still carries auto concentration risk.  

**Demographics / income:** NH White 72% · Black 13% · Hisp 6% · Asian 3%. State median HH income **$79k** (CPS 2024); mean HH income `unavailable`. Detroit metro ~Black 22% / NH White mid-60s%; Detroit city much higher Black share. Metro median HH income ACS 2024 **$76,403**.  

Detroit leads printed gross yields, but statewide unemployment is 5.0%. Grand Rapids is the lower-yield, higher-stability alternative. Detroit’s ~19% headline yield should never be applied to a typical renovated single-family home without address-level verification. Small multifamily can work in stronger suburbs.

**Best fit:** experienced value-add operators.  
**Confidence:** High on direction; Medium on achievable net yield.

### West Virginia
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 10 / Cash flow 8 / Appreciation 8 / Owner law 9 / Tenant law 2  

**Prices:** State median **$253,300** / typical **$182,704** (large median-vs-typical gap). Charleston / Huntington metro medians `unavailable` in top-50.  
**Entry capital:** **25% down** (investor default). On state median **$253,300**: cash to close ≈ **$71k** (25% + ~3% closing); recommended shock liquid ≈ **$9k** (6 mo PITI screen); **total recommended liquid ≈ $80k**.  

**Top industries:** Government; trade / logistics; education & health; mining-adjacent. Limited private diversification.  

**Demographics / income:** NH White 89% · Black 4% · Hisp 2% · Asian 1%. State median HH income **$63k** (CPS 2024); mean HH income `unavailable`. Overwhelmingly NH White statewide; limited metro scale.  

Extremely low entry prices, favorable owner law, appreciation about +4.0%, low property taxes. Charleston / Huntington are the main rental screens. Scale and exit liquidity keep it out of the top actionable tier.

**Best fit:** small-scale high-yield buying with local management.  
**Confidence:** Medium.

### Kansas
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 8 / Cash flow 7 / Appreciation 7 / Owner law 8 / Tenant law 3  

**Prices:** State median **$302,300** / typical **$252,794**. Wichita metro median `unavailable` in top-50.  
**Entry capital:** **25% down** (investor default). On state median **$302,300**: cash to close ≈ **$85k** (25% + ~3% closing); recommended shock liquid ≈ **$12k** (6 mo PITI screen); **total recommended liquid ≈ $97k**.  

**Top industries:** Trade / logistics; government; education & health; manufacturing (Wichita aviation pocket).  

**Demographics / income:** NH White 72% · Hisp 13% · Black 6% · Asian 3%. State median HH income **$88k** (CPS 2024); mean HH income `unavailable`. Wichita / Kansas City–KS side more diverse than rural Kansas; Hispanic share elevated in southwest counties.  

Affordable and landlord-workable, but hail / tornado insurance can erase thin deals. Wichita is the value market; Kansas City–Kansas side benefits from the broader metro.

**Best fit:** steady cash flow with bindable insurance quotes first.  
**Confidence:** Medium.


### Georgia
[↑ Back to Index](#index)


**Scores:** Jobs 9 / Price 6 / Cash flow 7 / Appreciation 5 / Owner law 9 / Tenant law 2  

**Prices:** State median **$373,700** / typical **$335,358**. Atlanta metro median **$408,776**.  
**Entry capital:** **25% down** (investor default). On state median **$373,700**: cash to close ≈ **$105k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $119k**. Metro screens: Atlanta median **$408,776** → cash to close ~**$114k**, total liquid ~**$130k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Atlanta logistics / film / corporate services  
**Demographics / income:** NH White 50% · Black 31% · Hisp 10% · Asian 4%. State median HH income **$81k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Atlanta — suburbs vs intown diverge sharply; screen for concessions. Athens is the job-growth satellite.  

Athens job growth and Atlanta migration are positives, but Atlanta yields and concessions are weaker than Midwest alternatives. Owner law is excellent.

**Best fit:** Athens / selected Atlanta suburbs for growth; Midwest still better for day-one cash flow.  
**Risks:** Atlanta concessions; inland vs coastal divergence.  
**Confidence:** High.

### Mississippi
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 10 / Cash flow 6 / Appreciation 7 / Owner law 9 / Tenant law 2  

**Prices:** State median **$265,200** / typical **$198,428**. Jackson investor-screen ~**$88,000**.  
**Entry capital:** **25% down** (investor default). On state median **$265,200**: cash to close ≈ **$74k** (25% + ~3% closing); recommended shock liquid ≈ **$16k** (9 mo PITI screen); **total recommended liquid ≈ $90k**.  
**Top industries:** Trade / logistics; government; education & health; manufacturing. Lower diversification; weaker wage base  
**Demographics / income:** NH White 55% · Black 36% · Hisp 4% · Asian 1%. State median HH income **$56k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Jackson is the main high-yield screen; Gulfport / Hattiesburg secondary. Neighborhood and insurance diligence required.  

Huge gross-yield potential on paper; insurance and liquidity justify a conservative cash-flow score. Jackson is the main screen.

**Best fit:** Jackson high-yield single-family / small multifamily with strong local PM.  
**Risks:** Insurance; ops intensity; exit liquidity.  
**Confidence:** Medium.

### South Carolina
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 6 / Cash flow 6 / Appreciation 6 / Owner law 9 / Tenant law 2  

**Prices:** State median **$397,600** / typical **$309,323**. Coastal metros need insurance stress tests.  
**Entry capital:** **25% down** (investor default). On state median **$397,600**: cash to close ≈ **$111k** (25% + ~3% closing); recommended shock liquid ≈ **$22k** (9 mo PITI screen); **total recommended liquid ≈ $134k**.  
**Top industries:** Trade / logistics; education & health; manufacturing; government. Auto / manufacturing + ports  
**Demographics / income:** NH White 62% · Black 25% · Hisp 7% · Asian 2%. State median HH income **$77k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Greenville (jobs / migration); Columbia (value); Charleston coastal (insurance / flood).  

Greenville is a top job-growth market; coastal areas need wind / flood insurance stress tests before any yield looks real.

**Best fit:** Greenville growth single-family; avoid uninsured coastal yield chasing.  
**Risks:** Wind / flood insurance; coastal HOA costs.  
**Confidence:** High.

### Oklahoma
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 9 / Cash flow 6 / Appreciation 5 / Owner law 9 / Tenant law 2  

**Prices:** State median **$256,700** / typical **$225,437**. Oklahoma City / Tulsa are the primary screens.  
**Entry capital:** **25% down** (investor default). On state median **$256,700**: cash to close ≈ **$72k** (25% + ~3% closing); recommended shock liquid ≈ **$16k** (9 mo PITI screen); **total recommended liquid ≈ $88k**.  
**Top industries:** Trade / logistics; government; education & health; energy-adjacent. Energy concentration risk  
**Demographics / income:** NH White 61% · Hisp 12% · Native 8% · Black 7% · Multiracial 9%. State median HH income **$65k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Oklahoma City and Tulsa; hail / tornado insurance can erase thin deals.  

Excellent law and price, but unemployment rising to 4.2%, flat prices, and hail / tornado insurance justify the cash-flow haircut.

**Best fit:** OKC / Tulsa value buys only after bindable hail quotes.  
**Risks:** Insurance; soft prices; job softness.  
**Confidence:** High.

### North Carolina
[↑ Back to Index](#index)


**Scores:** Jobs 9 / Price 6 / Cash flow 6 / Appreciation 5 / Owner law 8 / Tenant law 3  

**Prices:** State median **$381,700** / typical **$340,430**. Charlotte metro median **$428,716**; Raleigh thinner day-one cash flow.  
**Entry capital:** **25% down** (investor default). On state median **$381,700**: cash to close ≈ **$107k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $121k**. Metro screens: Charlotte median **$428,716** → cash to close ~**$120k**, total liquid ~**$136k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Research Triangle tech / finance; Charlotte banking  
**Demographics / income:** NH White 60% · Black 20% · Hisp 11% · Asian 3%. State median HH income **$67k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Raleigh / Cary (jobs, thinner cash flow); Charlotte banking suburbs; Greensboro value screen.  

Raleigh’s +2.2% job growth is excellent; Charlotte / Raleigh prices mean thinner day-one cash flow than Midwest leaders.

**Best fit:** Raleigh growth with lower leverage; Greensboro value screens.  
**Risks:** Thin day-one yields in Triangle / Charlotte.  
**Confidence:** High.

### South Dakota
[↑ Back to Index](#index)


**Scores:** Jobs 10 / Price 6 / Cash flow 6 / Appreciation 7 / Owner law 8 / Tenant law 3  

**Prices:** State median **$318,500** / typical **$325,618**. Sioux Falls / Rapid City; scale is the constraint.  
**Entry capital:** **25% down** (investor default). On state median **$318,500**: cash to close ≈ **$89k** (25% + ~3% closing); recommended shock liquid ≈ **$13k** (6 mo PITI screen); **total recommended liquid ≈ $102k**.  
**Top industries:** Trade / logistics; education & health; government; financial / leisure. Small scale; finance niches in Sioux Falls  
**Demographics / income:** NH White 80% · Native 8% · Hisp 4% · Black 2%. State median HH income **$80k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Sioux Falls primary; Rapid City secondary. Limited scale / exit liquidity.  

2.0% unemployment is excellent; market scale and exit liquidity are the constraints, not jobs.

**Best fit:** Sioux Falls long-term hold; keep expectations on scale.  
**Risks:** Thin buyer pool; limited inventory.  
**Confidence:** Medium.

### Illinois
[↑ Back to Index](#index)


**Scores:** Jobs 4 / Price 7 / Cash flow 6 / Appreciation 10 / Owner law 6 / Tenant law 6  

**Prices:** State median **$314,200** / typical **$298,871**. Chicago metro median **$408,776**; outside Chicago more workable.  
**Entry capital:** **25% down** (investor default). On state median **$314,200**: cash to close ≈ **$88k** (25% + ~3% closing); recommended shock liquid ≈ **$21k** (9 mo PITI screen); **total recommended liquid ≈ $109k**. Metro screens: Chicago median **$408,776** → cash to close ~**$114k**, total liquid ~**$141k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Chicago finance / professional services dominate metro mix  
**Demographics / income:** NH White 58% · Hisp 18% · Black 14% · Asian 6%. State median HH income **$84k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Outside Chicago preferred for landlord ops; Peoria appreciated strongly; Chicago city rules need local counsel.  

Leads the nation in recent statewide appreciation; Chicago’s city ordinances and taxes require local expertise. Outside Chicago, the baseline is more workable.

**Best fit:** Secondary metros / suburbs for appreciation + income; Chicago only with local expertise.  
**Risks:** City ordinances; taxes; Chicago-specific rules.  
**Confidence:** High.

### Texas
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 7 / Cash flow 5 / Appreciation 3 / Owner law 9 / Tenant law 2  

**Prices:** State median **$341,800** / typical **$302,999**. Houston **$345,665**, Dallas **$413,761**, Austin **$448,657**, San Antonio **$328,985**.  
**Entry capital:** **25% down** (investor default). On state median **$341,800**: cash to close ≈ **$96k** (25% + ~3% closing); recommended shock liquid ≈ **$23k** (9 mo PITI screen); **total recommended liquid ≈ $118k**. Metro screens: Houston median **$345,665** → cash to close ~**$97k**, total liquid ~**$120k**; Dallas median **$413,761** → cash to close ~**$116k**, total liquid ~**$143k**; Austin median **$448,657** → cash to close ~**$126k**, total liquid ~**$155k**; San Antonio median **$328,985** → cash to close ~**$92k**, total liquid ~**$114k**. Suburb note: Forney / Mansfield / Katy-type CF suburbs usually need less total liquid than Frisco / McKinney / Plano appreciation suburbs.  
**Top industries:** Trade / logistics; professional services; education & health; government. Energy still signature in Houston; DFW more corporate / logistics  
**Demographics / income:** NH White 40% · Hisp 39% · Black 12% · Asian 5%. State median HH income **$81k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** DFW — Frisco / McKinney / Plano (appreciation) and Forney / Mansfield (better rent-to-price); Houston — Katy / Cypress / Spring–Klein (balanced).  

Houston and Dallas–Fort Worth still grow population, but statewide prices are soft, property taxes are high (~1.6%), and Gulf / hail insurance matters. Austin remains a buyer’s market, not a clean appreciation call.

**Best fit:** Houston / DFW workforce suburbs; stress tax + insurance.  
**Risks:** Property tax; insurance; Austin soft thesis.  
**Confidence:** High.

### Virginia
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 4 / Cash flow 5 / Appreciation 7 / Owner law 8 / Tenant law 3  

**Prices:** State median **$462,400** / typical **$419,920**. Virginia Beach metro median **$398,806**; Richmond / Hampton Roads preferred over D.C.-only thesis.  
**Entry capital:** **25% down** (investor default). On state median **$462,400**: cash to close ≈ **$129k** (25% + ~3% closing); recommended shock liquid ≈ **$17k** (6 mo PITI screen); **total recommended liquid ≈ $147k**. Metro screens: Virginia Beach median **$398,806** → cash to close ~**$112k**, total liquid ~**$127k**.  
**Top industries:** Professional services; government; education & health; trade / logistics. Federal / defense / cyber concentration (Northern Virginia)  
**Demographics / income:** NH White 59% · Black 18% · Hisp 11% · Asian 7%. State median HH income **$98k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Richmond and Hampton Roads / Virginia Beach over a pure Northern Virginia / D.C. thesis in 2026.  

Richmond and Hampton Roads beat a D.C.-dependent thesis in 2026 given federal payroll risk in Northern Virginia.

**Best fit:** Richmond / Hampton Roads balanced; caution on NoVA federal exposure.  
**Risks:** Federal payroll risk; higher entry than Midwest.  
**Confidence:** High.

### New Mexico
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 6 / Cash flow 6 / Appreciation 7 / Owner law 8 / Tenant law 3  

**Prices:** State median **$378,300** / typical **$321,186**. Albuquerque is the primary balanced market.  
**Entry capital:** **25% down** (investor default). On state median **$378,300**: cash to close ≈ **$106k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $120k**.  
**Top industries:** Government; trade / logistics; education & health; professional / leisure. Federal / labs / tourism mix  
**Demographics / income:** Hisp 48% · NH White 37% · Native 9% · Black 2%. State median HH income **$64k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Albuquerque primary; Santa Fe lifestyle / higher entry; Las Cruces secondary.  

Albuquerque is the primary balanced market; federal / labs / tourism mix supports demand without coastal prices.

**Best fit:** Albuquerque balanced single-family.  
**Risks:** Thin liquidity outside Albuquerque; income levels.  
**Confidence:** Medium.

### Minnesota
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 6 / Cash flow 5 / Appreciation 7 / Owner law 6 / Tenant law 6  

**Prices:** State median **$354,500** / typical **$356,887**. Minneapolis metro median **$408,776**.  
**Entry capital:** **25% down** (investor default). On state median **$354,500**: cash to close ≈ **$99k** (25% + ~3% closing); recommended shock liquid ≈ **$14k** (6 mo PITI screen); **total recommended liquid ≈ $113k**. Metro screens: Minneapolis median **$408,776** → cash to close ~**$114k**, total liquid ~**$130k**.  
**Top industries:** Education & health; trade / logistics; professional services; government. Diversified Twin Cities corporate base  
**Demographics / income:** NH White 76% · Black 7% · Asian 5% · Hisp 6%. State median HH income **$92k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Twin Cities suburbs for liquidity; Duluth / Rochester smaller screens; watch local ordinances.  

Stable Twin Cities demand; modest yields and some local ordinance risk keep it mid-pack.

**Best fit:** Twin Cities turnkey with modest yield expectations.  
**Risks:** Local ordinances; thin yields.  
**Confidence:** High.

### Louisiana
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 9 / Cash flow 4 / Appreciation 6 / Owner law 9 / Tenant law 2  

**Prices:** State median **$260,300** / typical **$217,968**. New Orleans / Baton Rouge; insurance drag is material.  
**Entry capital:** **25% down** (investor default). On state median **$260,300**: cash to close ≈ **$73k** (25% + ~3% closing); recommended shock liquid ≈ **$16k** (9 mo PITI screen); **total recommended liquid ≈ $89k**.  
**Top industries:** Trade / logistics; education & health; government; leisure / energy-adjacent. Energy / petrochem concentration on Gulf  
**Demographics / income:** NH White 56% · Black 31% · Hisp 7% · Asian 2%. State median HH income **$61k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Baton Rouge often cleaner ops than New Orleans for remote owners; Gulf insurance is the deal-breaker screen.  

Cheap and landlord-friendly on statute, but insurance and weak long-term appreciation are material haircuts.

**Best fit:** Selected inland / Baton Rouge value only with insurance quotes.  
**Risks:** Catastrophe insurance; weak appreciation.  
**Confidence:** Medium.

### Alaska
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 5 / Cash flow 5 / Appreciation 10 / Owner law 8 / Tenant law 3  

**Prices:** State median **$399,900** / typical **$400,659**. Anchorage / Fairbanks; logistics raise operating cost.  
**Entry capital:** **25% down** (investor default). On state median **$399,900**: cash to close ≈ **$112k** (25% + ~3% closing); recommended shock liquid ≈ **$15k** (6 mo PITI screen); **total recommended liquid ≈ $127k**.  
**Top industries:** Government; trade / logistics; education & health; leisure. Government share elevated  
**Demographics / income:** NH White 58% · Native 15% · Multiracial 10% · Hisp 7% · Asian 6%. State median HH income **$91k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Anchorage primary; Fairbanks secondary. Extreme logistics / seasonal ops.  

Strong appreciation prints, but expensive logistics and small scale limit remote-investor practicality.

**Best fit:** Anchorage only for locals / specialists.  
**Risks:** Logistics; climate; small scale.  
**Confidence:** Medium.

### Vermont
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 5 / Cash flow 4 / Appreciation 9 / Owner law 4 / Tenant law 8  

**Prices:** State median **$438,400** / typical **$402,017**. Burlington is the main screen; small statewide scale.  
**Entry capital:** **25% down** (investor default). On state median **$438,400**: cash to close ≈ **$123k** (25% + ~3% closing); recommended shock liquid ≈ **$18k** (6 mo PITI screen); **total recommended liquid ≈ $141k**.  
**Top industries:** Education & health; trade / logistics; government; leisure. Small / seasonal leisure exposure  
**Demographics / income:** NH White 89% · Hisp 2% · Asian 2% · Black 1%. State median HH income **$85k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Burlington metro only meaningful screen; statewide inventory thin.  

Tight labor and supply support demand; high entry prices and tenant protections compress income returns.

**Best fit:** Burlington specialty / low leverage.  
**Risks:** Tenant rules; high entry; tiny scale.  
**Confidence:** Medium.

### Maine
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 5 / Cash flow 4 / Appreciation 7 / Owner law 5 / Tenant law 7  

**Prices:** State median **$390,400** / typical **$424,107**. Portland / Bangor; tenant protections compress returns.  
**Entry capital:** **25% down** (investor default). On state median **$390,400**: cash to close ≈ **$109k** (25% + ~3% closing); recommended shock liquid ≈ **$15k** (6 mo PITI screen); **total recommended liquid ≈ $124k**.  
**Top industries:** Education & health; trade / logistics; government; leisure. Health care + tourism seasonality  
**Demographics / income:** NH White 90% · Hisp 2% · Black 2% · Asian 1%. State median HH income **$91k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Portland metro; Bangor value. Tenant-leaning rules and high entry vs Midwest.  

Similar New England pattern: solid demand, high entry, tenant-leaning friction vs Midwest cash-flow states.

**Best fit:** Portland metro low-leverage hold.  
**Risks:** Tenant protections; high entry.  
**Confidence:** Medium.

### Idaho
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 4 / Cash flow 4 / Appreciation 7 / Owner law 10 / Tenant law 1  

**Prices:** State median **$476,300** / typical **$482,199**. Boise / Idaho Falls / Coeur d’Alene.  
**Entry capital:** **25% down** (investor default). On state median **$476,300**: cash to close ≈ **$133k** (25% + ~3% closing); recommended shock liquid ≈ **$17k** (6 mo PITI screen); **total recommended liquid ≈ $151k**.  
**Top industries:** Trade / logistics; government; education & health; professional / manufacturing. Boise tech / services growing; still smaller base  
**Demographics / income:** NH White 79% · Hisp 13% · Asian 1% · Native 1%. State median HH income **$82k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Boise metro primary; Idaho Falls / Coeur d’Alene secondary. Prices limit income returns.  

Best-in-class owner law and solid Boise demand; current prices limit income returns.

**Best fit:** Boise quality long-term; accept thin cash flow.  
**Risks:** High prices vs rents.  
**Confidence:** High.

### Florida
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 5 / Cash flow 4 / Appreciation 4 / Owner law 9 / Tenant law 2  

**Prices:** State median **$416,800** / typical **$378,126**. Tampa **$391,328**, Orlando **$413,761**, Miami **$576,124**, Jacksonville **$394,215**.  
**Entry capital:** **25% down** (investor default). On state median **$416,800**: cash to close ≈ **$117k** (25% + ~3% closing); recommended shock liquid ≈ **$25k** (9 mo PITI screen); **total recommended liquid ≈ $142k**. Metro screens: Tampa median **$391,328** → cash to close ~**$110k**, total liquid ~**$133k**; Orlando median **$413,761** → cash to close ~**$116k**, total liquid ~**$141k**; Miami median **$576,124** → cash to close ~**$161k**, total liquid ~**$195k**; Jacksonville median **$394,215** → cash to close ~**$110k**, total liquid ~**$134k**.  
**Top industries:** Trade / logistics; professional services; education & health; leisure / hospitality. Leisure / tourism seasonality is a real vacancy risk  
**Demographics / income:** NH White 52% · Hisp 26% · Black 15% · Asian 3%. State median HH income **$76k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Tampa / Jacksonville often cleaner than Miami for income screens; get bindable insurance quotes before offering.  

Strong owner law and migration do not erase insurance, association fees, and soft-rent risk. Bindable quotes before offering.

**Best fit:** Inland / Jacksonville / Tampa only after insurance binds.  
**Risks:** Insurance; concessions; HOA.  
**Confidence:** High.

### Wyoming
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 5 / Cash flow 6 / Appreciation 4 / Owner law 9 / Tenant law 2  

**Prices:** State median **$440,300** / typical **$372,526**. Cheyenne / Casper; small markets.  
**Entry capital:** **25% down** (investor default). On state median **$440,300**: cash to close ≈ **$123k** (25% + ~3% closing); recommended shock liquid ≈ **$16k** (6 mo PITI screen); **total recommended liquid ≈ $139k**.  
**Top industries:** Government; trade / logistics; education & health; mining / energy. Energy / mining concentration; very small scale  
**Demographics / income:** NH White 81% · Hisp 10% · Native 2% · Black 1%. State median HH income **$79k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Cheyenne / Casper only; very small markets.  

Favorable law and jobs, but very small markets and limited liquidity.

**Best fit:** Small-scale Cheyenne / Casper only.  
**Risks:** Liquidity; energy cyclicality.  
**Confidence:** Medium.

### Utah
[↑ Back to Index](#index)


**Scores:** Jobs 9 / Price 3 / Cash flow 4 / Appreciation 4 / Owner law 10 / Tenant law 1  

**Prices:** State median **$575,300** / typical **$541,692**. Salt Lake City / Provo / Ogden.  
**Entry capital:** **25% down** (investor default). On state median **$575,300**: cash to close ≈ **$161k** (25% + ~3% closing); recommended shock liquid ≈ **$20k** (6 mo PITI screen); **total recommended liquid ≈ $182k**.  
**Top industries:** Trade / logistics; professional services; education & health; government. Salt Lake tech / professional services growth  
**Demographics / income:** NH White 75% · Hisp 15% · Asian 2% · Pacific Isl. 1%. State median HH income **$104k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Salt Lake / Provo / Ogden corridor; strong demand, thin yields at current prices.  

Salt Lake corridor jobs are excellent; entry cost and thin yields make this an appreciation / quality screen, not a cash-flow leader.

**Best fit:** Salt Lake corridor quality / jobs; not income-first.  
**Risks:** High entry; thin yields.  
**Confidence:** High.

### Montana
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 4 / Cash flow 4 / Appreciation 5 / Owner law 9 / Tenant law 2  

**Prices:** State median **$505,600** / typical **$476,115**. Billings / Missoula / Bozeman; lifestyle metros pricey.  
**Entry capital:** **25% down** (investor default). On state median **$505,600**: cash to close ≈ **$142k** (25% + ~3% closing); recommended shock liquid ≈ **$19k** (6 mo PITI screen); **total recommended liquid ≈ $160k**.  
**Top industries:** Trade / logistics; government; education & health; leisure. Thin private base outside Billings / Bozeman  
**Demographics / income:** NH White 83% · Native 6% · Hisp 4% · Multiracial 5%. State median HH income **$82k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Billings value vs Missoula / Bozeman lifestyle premiums.  

Favorable law; lifestyle metros (Missoula / Bozeman) are expensive relative to rents.

**Best fit:** Billings value over Bozeman lifestyle premiums.  
**Risks:** High lifestyle prices; small markets.  
**Confidence:** Medium.

### Nevada
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 4 / Cash flow 5 / Appreciation 5 / Owner law 8 / Tenant law 3  

**Prices:** State median **$468,900** / typical **$448,215**. Las Vegas metro median **$453,642**; Reno secondary.  
**Entry capital:** **25% down** (investor default). On state median **$468,900**: cash to close ≈ **$131k** (25% + ~3% closing); recommended shock liquid ≈ **$17k** (6 mo PITI screen); **total recommended liquid ≈ $148k**. Metro screens: Las Vegas median **$453,642** → cash to close ~**$127k**, total liquid ~**$143k**.  
**Top industries:** Leisure / hospitality; trade / logistics; professional services; government. Tourism / gaming concentration (Las Vegas)  
**Demographics / income:** NH White 46% · Hisp 29% · Black 9% · Asian 9%. State median HH income **$81k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Las Vegas valley suburbs; Reno secondary. Tourism cyclicality.  

Las Vegas jobs are strong; tourism / gaming cyclicality remains the vacancy risk.

**Best fit:** Las Vegas with tourism vacancy stress tests.  
**Risks:** Tourism cyclicality.  
**Confidence:** High.

### Connecticut
[↑ Back to Index](#index)


**Scores:** Jobs 4 / Price 4 / Cash flow 6 / Appreciation 9 / Owner law 5 / Tenant law 7  

**Prices:** State median **$445,100** / typical **$455,424**. Hartford / Bridgeport / New Haven.  
**Entry capital:** **25% down** (investor default). On state median **$445,100**: cash to close ≈ **$125k** (25% + ~3% closing); recommended shock liquid ≈ **$19k** (6 mo PITI screen); **total recommended liquid ≈ $143k**.  
**Top industries:** Education & health; trade / logistics; government; professional services. Health / insurance / finance tilt in metros  
**Demographics / income:** NH White 63% · Hisp 17% · Black 10% · Asian 5%. State median HH income **$99k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Hartford cash-flow tilt; Bridgeport–Stamford appreciation corridor.  

Hartford can cash flow and appreciation has been strong; unemployment deterioration is a warning flag.

**Best fit:** Hartford income screens; watch jobs.  
**Risks:** Unemployment deterioration; tenant rules.  
**Confidence:** High.

### Delaware
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 5 / Cash flow 5 / Appreciation 6 / Owner law 8 / Tenant law 3  

**Prices:** State median **$366,200** / typical **$412,252**. Wilmington is the only scalable screen.  
**Entry capital:** **25% down** (investor default). On state median **$366,200**: cash to close ≈ **$103k** (25% + ~3% closing); recommended shock liquid ≈ **$13k** (6 mo PITI screen); **total recommended liquid ≈ $116k**.  
**Top industries:** Trade / logistics; education & health; government; professional / finance. Finance / corporate services overweighted vs size  
**Demographics / income:** NH White 59% · Black 22% · Hisp 11% · Asian 4%. State median HH income **$86k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Wilmington / New Castle County; Dover smaller.  

Balanced but small; Wilmington is the only scalable screen.

**Best fit:** Wilmington small-portfolio only.  
**Risks:** Scale; limited screens.  
**Confidence:** Medium.

### Arizona
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 4 / Cash flow 5 / Appreciation 5 / Owner law 9 / Tenant law 2  

**Prices:** State median **$452,500** / typical **$422,822**. Phoenix metro median **$463,612**; Tucson secondary.  
**Entry capital:** **25% down** (investor default). On state median **$452,500**: cash to close ≈ **$127k** (25% + ~3% closing); recommended shock liquid ≈ **$16k** (6 mo PITI screen); **total recommended liquid ≈ $143k**. Metro screens: Phoenix metro median **$463,612** → cash to close ~**$130k**, total liquid ~**$147k**. Suburb note: West Valley CF suburbs often price below Phoenix metro median (lower cash-to-close); Gilbert / Chandler higher entry + thinner yield.  
**Top industries:** Trade / logistics; education & health; professional services; government. Broad Sun Belt mix; not single-employer  
**Demographics / income:** NH White 53% · Hisp 31% · Black 4% · Native 4% · Asian 3%. State median HH income **$85k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** West Valley CF — Buckeye / Surprise / Avondale; East Valley — Mesa / Tempe (balanced), Gilbert / Chandler (appreciation / schools).  

Owner-friendly, but Phoenix rent growth was soft and concessions elevated — underwrite achieved rent.

**Best fit:** West Valley cash-flow tilt; East Valley schools / appreciation.  
**Risks:** Soft rents; concessions.  
**Confidence:** High.

### Maryland
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 4 / Cash flow 6 / Appreciation 5 / Owner law 5 / Tenant law 7  

**Prices:** State median **$446,900** / typical **$436,104**. Baltimore metro median **$438,686**.  
**Entry capital:** **25% down** (investor default). On state median **$446,900**: cash to close ≈ **$125k** (25% + ~3% closing); recommended shock liquid ≈ **$17k** (6 mo PITI screen); **total recommended liquid ≈ $142k**. Metro screens: Baltimore median **$438,686** → cash to close ~**$123k**, total liquid ~**$140k**.  
**Top industries:** Education & health; government; professional services; trade / logistics. Federal / cyber / biotech spillover from D.C.  
**Demographics / income:** NH White 47% · Black 29% · Hisp 12% · Asian 7%. State median HH income **$110k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Baltimore income screens; Montgomery / Prince George’s higher entry and local friction.  

Baltimore income is plausible; local stabilization and operating friction must be priced. High statewide incomes.

**Best fit:** Baltimore income with local-rule pricing.  
**Risks:** Stabilization / ops friction; high taxes in places.  
**Confidence:** High.

### New Hampshire
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 3 / Cash flow 3 / Appreciation 8 / Owner law 5 / Tenant law 7  

**Prices:** State median **$500,200** / typical **$522,944**. Manchester–Nashua; Boston spillover.  
**Entry capital:** **25% down** (investor default). On state median **$500,200**: cash to close ≈ **$140k** (25% + ~3% closing); recommended shock liquid ≈ **$20k** (6 mo PITI screen); **total recommended liquid ≈ $161k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Boston spillover professional / tech  
**Demographics / income:** NH White 87% · Hisp 4% · Asian 3% · Black 1%. State median HH income **$112k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Manchester–Nashua; Boston spillover appreciation more than day-one yield.  

Strong incomes and Boston spillover; prices and tenant rules leave thin day-one yields for income-first buyers.

**Best fit:** Manchester–Nashua appreciation / quality.  
**Risks:** Thin yields; tenant-leaning friction.  
**Confidence:** Medium.

### New York
[↑ Back to Index](#index)


**Scores:** Jobs 5 / Price 3 / Cash flow 4 / Appreciation 9 / Owner law 1 / Tenant law 10  

**Prices:** State median **$595,500** / typical **$525,947**. New York City metro median **$843,474** (upstate far lower).  
**Entry capital:** **25% down** (investor default). On state median **$595,500**: cash to close ≈ **$167k** (25% + ~3% closing); recommended shock liquid ≈ **$35k** (9 mo PITI screen); **total recommended liquid ≈ $202k**. Metro screens: New York City metro median **$843,474** → cash to close ~**$236k**, total liquid ~**$286k**.  
**Top industries:** Education & health; trade / logistics; professional services; government. NYC finance / professional services; upstate more health / gov / education  
**Demographics / income:** NH White 52% · Hisp 20% · Black 14% · Asian 9%. State median HH income **$87k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Upstate (Buffalo / Rochester / Syracuse) far more investable than NYC; Good Cause opt-ins vary by city.  

Upstate cities are far more investable than New York City, though Good Cause has expanded to several opt-in cities.

**Best fit:** Upstate cash flow / value; avoid NYC unless specialist.  
**Risks:** Good Cause opt-ins; NYC regulation.  
**Confidence:** High.

### New Jersey
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 3 / Cash flow 2 / Appreciation 9 / Owner law 3 / Tenant law 9  

**Prices:** State median **$545,300** / typical **$584,681**. Newark metro median **$697,245**.  
**Entry capital:** **25% down** (investor default). On state median **$545,300**: cash to close ≈ **$153k** (25% + ~3% closing); recommended shock liquid ≈ **$36k** (9 mo PITI screen); **total recommended liquid ≈ $189k**. Metro screens: Newark metro median **$697,245** → cash to close ~**$195k**, total liquid ~**$241k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Pharma / logistics / NYC spillover  
**Demographics / income:** NH White 52% · Hisp 22% · Black 12% · Asian 10%. State median HH income **$104k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Newark / Camden / New Brunswick corridor; taxes and Anti-Eviction Act dominate underwriting.  

Strong appreciation and demand, but taxes (~2.23% effective) and Anti-Eviction rules require lower leverage and more reserves.

**Best fit:** Lower leverage, higher reserves; demand is not the problem.  
**Risks:** Taxes; Anti-Eviction Act.  
**Confidence:** High.

### Rhode Island
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 3 / Cash flow 4 / Appreciation 4 / Owner law 7 / Tenant law 4  

**Prices:** State median **$535,100** / typical **$517,078**. Providence metro median **$547,361**.  
**Entry capital:** **25% down** (investor default). On state median **$535,100**: cash to close ≈ **$150k** (25% + ~3% closing); recommended shock liquid ≈ **$21k** (6 mo PITI screen); **total recommended liquid ≈ $171k**. Metro screens: Providence median **$547,361** → cash to close ~**$153k**, total liquid ~**$175k**.  
**Top industries:** Education & health; trade / logistics; government; professional services. Small base; health / education anchors  
**Demographics / income:** NH White 69% · Hisp 17% · Black 5% · Asian 4%. State median HH income **$92k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Providence metro; small statewide scale.  

Durable small-state demand; yields generally too thin for income-first investors.

**Best fit:** Providence low-leverage specialty.  
**Risks:** Thin yields; small scale.  
**Confidence:** Medium.

### Massachusetts
[↑ Back to Index](#index)


**Scores:** Jobs 6 / Price 2 / Cash flow 2 / Appreciation 7 / Owner law 6 / Tenant law 6  

**Prices:** State median **$645,400** / typical **$672,867**. Boston metro median **$797,612**; Worcester / Springfield secondary.  
**Entry capital:** **25% down** (investor default). On state median **$645,400**: cash to close ≈ **$181k** (25% + ~3% closing); recommended shock liquid ≈ **$24k** (6 mo PITI screen); **total recommended liquid ≈ $205k**. Metro screens: Boston median **$797,612** → cash to close ~**$223k**, total liquid ~**$253k**.  
**Top industries:** Education & health; professional services; trade / logistics; government. Boston education / biotech / professional services  
**Demographics / income:** NH White 68% · Hisp 13% · Asian 7% · Black 7%. State median HH income **$114k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Worcester / Springfield for any income attempt; Boston proper too expensive for cash-flow-first.  

Durable Boston-metro demand; yields generally too thin for income-first investors outside secondary cities.

**Best fit:** Secondary cities only for income attempts; Boston is appreciation / specialty.  
**Risks:** Extreme entry; regulation.  
**Confidence:** High.

### Hawaii
[↑ Back to Index](#index)


**Scores:** Jobs 8 / Price 1 / Cash flow 2 / Appreciation 7 / Owner law 7 / Tenant law 4  

**Prices:** State median **$773,400** / typical **$836,741**. Honolulu; extreme entry cost.  
**Entry capital:** **25% down** (investor default). On state median **$773,400**: cash to close ≈ **$217k** (25% + ~3% closing); recommended shock liquid ≈ **$39k** (9 mo PITI screen); **total recommended liquid ≈ $256k**.  
**Top industries:** Government; leisure / hospitality; trade / logistics; education & health. Tourism + military/government concentration  
**Demographics / income:** Asian 37% · Multiracial 20% · NH White 22% · Pacific Isl. 10% · Hisp 10%. State median HH income **$98k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Honolulu Oahu primary; neighbor islands even thinner liquidity for mainland investors.  

Low unemployment cannot overcome extreme entry cost for normal cash-flow investing.

**Best fit:** Not a standard cash-flow market.  
**Risks:** Extreme prices; tourism / military mix.  
**Confidence:** Medium.

### Colorado
[↑ Back to Index](#index)


**Scores:** Jobs 7 / Price 3 / Cash flow 3 / Appreciation 2 / Owner law 7 / Tenant law 5  

**Prices:** State median **$604,600** / typical **$543,435**. Denver metro median **$607,070**.  
**Entry capital:** **25% down** (investor default). On state median **$604,600**: cash to close ≈ **$169k** (25% + ~3% closing); recommended shock liquid ≈ **$22k** (6 mo PITI screen); **total recommended liquid ≈ $191k**. Metro screens: Denver median **$607,070** → cash to close ~**$170k**, total liquid ~**$192k**.  
**Top industries:** Trade / logistics; professional services; government; education & health. Diversified; Front Range professional services strong  
**Demographics / income:** NH White 65% · Hisp 22% · Black 4% · Asian 3%. State median HH income **$106k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Denver metro soft YoY; Colorado Springs / Front Range secondary screens.  

Statewide prices down about 2.4% year over year; high entry cost and for-cause changes make 2026 a watch market.

**Best fit:** Watch / selectively buy after price digestion.  
**Risks:** Soft prices; for-cause; high entry.  
**Confidence:** High.

### Oregon
[↑ Back to Index](#index)


**Scores:** Jobs 3 / Price 3 / Cash flow 3 / Appreciation 5 / Owner law 3 / Tenant law 9  

**Prices:** State median **$508,100** / typical **$504,432**. Portland metro median **$568,298**.  
**Entry capital:** **25% down** (investor default). On state median **$508,100**: cash to close ≈ **$142k** (25% + ~3% closing); recommended shock liquid ≈ **$28k** (9 mo PITI screen); **total recommended liquid ≈ $171k**. Metro screens: Portland median **$568,298** → cash to close ~**$159k**, total liquid ~**$191k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Portland tech / trade; state jobs soft recently  
**Demographics / income:** NH White 72% · Hisp 14% · Asian 5% · Black 2%. State median HH income **$90k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Portland weak near-term (jobs + statewide rent stabilization); Salem / Eugene secondary.  

Portland job losses and statewide rent stabilization weaken the near-term case.

**Best fit:** Wait / specialist only while Portland jobs and rent rules weigh.  
**Risks:** Rent stabilization; job losses.  
**Confidence:** High.

### Washington
[↑ Back to Index](#index)


**Scores:** Jobs 4 / Price 2 / Cash flow 3 / Appreciation 4 / Owner law 3 / Tenant law 9  

**Prices:** State median **$644,300** / typical **$603,303**. Seattle metro median **$827,522**; Spokane may be better value.  
**Entry capital:** **25% down** (investor default). On state median **$644,300**: cash to close ≈ **$180k** (25% + ~3% closing); recommended shock liquid ≈ **$36k** (9 mo PITI screen); **total recommended liquid ≈ $216k**. Metro screens: Seattle median **$827,522** → cash to close ~**$232k**, total liquid ~**$277k**.  
**Top industries:** Trade / logistics; education & health; professional services; government. Seattle tech / trade concentration; aerospace legacy  
**Demographics / income:** NH White 64% · Hisp 14% · Asian 9% · Black 4%. State median HH income **$98k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Spokane often the better value screen than Seattle / Tacoma under statewide rent caps.  

Statewide rent cap, weak Seattle pricing, elevated unemployment; Spokane may be the better value screen.

**Best fit:** Spokane value over Seattle; model statewide rent caps.  
**Risks:** Rent cap; Seattle softness; unemployment.  
**Confidence:** High.

### California
[↑ Back to Index](#index)


**Scores:** Jobs 4 / Price 1 / Cash flow 2 / Appreciation 4 / Owner law 3 / Tenant law 9  

**Prices:** State median **$854,000** / typical **$775,549**. Los Angeles **$947,164**, San Francisco **$1,724,835**, San Diego **$952,149**, Sacramento **$598,209**.  
**Entry capital:** **25% down** (investor default). On state median **$854,000**: cash to close ≈ **$239k** (25% + ~3% closing); recommended shock liquid ≈ **$46k** (9 mo PITI screen); **total recommended liquid ≈ $286k**. Metro screens: Los Angeles median **$947,164** → cash to close ~**$265k**, total liquid ~**$317k**; San Francisco median **$1,724,835** → cash to close ~**$483k**, total liquid ~**$575k**; San Diego median **$952,149** → cash to close ~**$267k**, total liquid ~**$318k**; Sacramento median **$598,209** → cash to close ~**$167k**, total liquid ~**$201k**.  
**Top industries:** Education & health; trade / logistics; professional services; government. Large & diversified; tech concentrated in metros  
**Demographics / income:** Hisp 39% · NH White 35% · Asian 15% · Black 5%. State median HH income **$101k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** Inland Empire / Sacramento / Central Valley for any cash-flow attempt; coastal metros specialist-only.  

Inland markets can work; coastal prices and statewide / local tenant rules make cash flow difficult for standard leverage.

**Best fit:** Inland value screens only; coastal specialist.  
**Risks:** Statewide / local tenant rules; extreme coastal prices.  
**Confidence:** High.

### District of Columbia
[↑ Back to Index](#index)


**Scores:** Jobs 2 / Price 2 / Cash flow 3 / Appreciation 3 / Owner law 1 / Tenant law 10  

**Prices:** State median **$676,500** / typical **$579,332**. Metro median **$623,134**.  
**Entry capital:** **25% down** (investor default). On state median **$676,500**: cash to close ≈ **$189k** (25% + ~3% closing); recommended shock liquid ≈ **$36k** (9 mo PITI screen); **total recommended liquid ≈ $225k**. Metro screens: D.C. metro median **$623,134** → cash to close ~**$174k**, total liquid ~**$208k**.  
**Top industries:** Professional services; government; education & health. High federal / professional concentration — cyclical with federal payrolls  
**Demographics / income:** Black 41% · NH White 38% · Hisp 11% · Asian 5%. State median HH income **$105k** (CPS 2024); mean HH income `unavailable`.  
**Top suburbs:** District proper vs Maryland / Virginia suburbs — TOPA / rent stabilization make D.C. specialist-only.  

TOPA / rent stabilization plus the largest confirmed metro job loss make this specialist-only.

**Best fit:** Specialist only (TOPA / rent stabilization).  
**Risks:** Federal job loss; TOPA; rent rules.  
**Confidence:** High.

---

## 7. Legal environment — verified 2026 highlights
[↑ Back to Index](#index)


- **Washington:** Rent stabilization law in effect since May 7, 2025. 2026 residential maximum increase **9.683%**, with 90 days’ notice and no increase in the first 12 months ([Washington Attorney General](https://www.atg.wa.gov/landlord-tenant)).
- **Oregon:** 2026 maximum **9.5%** for most covered older units; only one increase per 12 months ([Oregon Department of Administrative Services](https://www.oregon.gov/das/oea/pages/rent-stabilization.aspx)).
- **California:** Statewide rent cap of 5% + inflation, maximum 10%. Limits effective August 2026–July 2027 range roughly 8.1%–8.8% by region; local caps can be lower ([California Department of Justice](https://oag.ca.gov/rentcaps)).
- **New York:** Good Cause is mandatory in New York City and applies in opt-in municipalities. Increases above 5% + inflation, capped at 10%, are presumptively unreasonable for covered units ([New York Homes and Community Renewal](https://hcr.ny.gov/good-cause-eviction)).
- **Chicago / Cook County:** Illinois preempts rent control, but Chicago Fair Notice requires 60 or 120 days depending on tenure; Cook County ordinance caps deposits at 1.5 months and creates private remedies. City rules override the softer statewide rent-control preemption story.

Always verify licensing, registration, inspection, deposit, notice, and building-age exemptions for the exact city and property type.

---



## 8. Insurance and property-tax overlays
[↑ Back to Index](#index)




### Property tax (effective rate direction)
[↑ Back to Index](#index)


- **Highest drag:** New Jersey (~~2.23%), Illinois (~~2.07%), Connecticut, New Hampshire, Vermont, Texas (~1.6%), Wisconsin, Nebraska, New York, Ohio.
- **Lowest drag:** Hawaii, Alabama (~0.38%), Colorado, Nevada, Louisiana, South Carolina, West Virginia, Arkansas, Delaware.

Low tax rates help Alabama / Arkansas / Tennessee / South Carolina cash flow. High tax rates can quietly erase Wisconsin / Illinois / New Jersey / Texas deals that look fine on rent ÷ price alone.

### Insurance / catastrophe
[↑ Back to Index](#index)


- National landlord policies often **$800–$3,000/year**.
- Commonly **$2,200–$4,600+** in Florida, Louisiana, Texas, Oklahoma, Mississippi, and parts of the hail belt (Kansas, Nebraska, Arkansas).
- Treat Florida coastal, Louisiana, Texas Gulf, and Oklahoma as **insurance-first underwriting markets**. Do not rely on national average insurance assumptions.

---



## 9. Practical acquisition workflow
[↑ Back to Index](#index)


1. Choose a strategy: income now, balanced hold, or appreciation.
2. Choose property type: single-family, 2–4 unit, or both.
3. Shortlist 3–5 metros — not a whole state.
4. Pull current ZIP-level sale and executed-rent comps (like-for-like).
5. Get property-tax history and a **bindable insurance quote** before finalizing the offer.
6. Model vacancy, management, repairs, capital expenses, leasing, utilities, legal cost, and concessions.
7. Use the standard financing case (25% down; investor rate band ~7.0%–8.5% unless you have a live quote). Confirm **cash to close + shock reserves** from §4e / the state’s **Entry capital:** line before offering.
8. Stress: rate +1%, rent −5%, insurance +50%, and six months of nonpayment / vacancy.
9. Verify local licensing, inspection, deposit, notice, rent-cap, and just-cause rules.
10. Buy only if the **address-level** case still works.

---



## 10. Methodology and sources
[↑ Back to Index](#index)




### Confirmation of live research
[↑ Back to Index](#index)


This report used active web search / browsing on July 25, 2026. Scores are comparative screens on top of cited figures; regional judgment is labeled where exact metro duplex/fourplex medians were incomplete.

- **Pipeline live fetch:** `data/meta.json` analysis_run_at **2026-07-26T06:22:24+00:00**; census_api_key_present=False; tabular fields regenerated from overwritten `data/` (no cache-as-current).



### Financing and expense assumptions
[↑ Back to Index](#index)



| Item                           | Default used                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------- |
| Down payment                   | 25%                                                                                   |
| Closing / acquisition costs    | ~3% of purchase (screen)                                                              |
| Cash to close (screen)         | Down + closing ≈ **28%** of median buy-box price                                      |
| Shock liquid (screen)          | **6 months** PITI default; **9 months** in high-insurance / high-tax / soft-rent / heavy-regulation states |
| Total recommended liquid       | Cash to close + shock liquid                                                          |
| PITI rate assumption           | **7.5%** midpoint of ~7.0%–8.5% investor band; 30-year amortizing on 75% LTV          |
| Loan type                      | Investor / cash-flow–qualified rental loan                                            |
| Interest rate band             | About 7.0%–8.5% for typical July 2026 files; stronger files can be lower              |
| Vacancy                        | 5–8% (higher if concessions are elevated)                                             |
| Operating expenses before debt | About 35–50% of gross rent; higher in high-tax / high-insurance / older-stock markets |
| Gross yield                    | Annual rent ÷ price (prefer median purchase price; screen only)                       |
| Preferred rent input           | Achieved / signed lease rent; otherwise asking rent labeled                           |




### Primary sources
[↑ Back to Index](#index)


- [Bureau of Labor Statistics — state unemployment, June 2026](https://www.bls.gov/news.release/laus.htm)
- [BLS — industry employment by state (May 2026 chart)](https://www.bls.gov/charts/state-employment-and-unemployment/industry-employment-by-state.htm)
- [FRED / Census — median household income by state, 2024 CPS ASEC](https://fred.stlouisfed.org/release/tables?eid=259462&rid=249)
- [Census ACS brief — household income in states and metros, 2024 (ACSBR-025)](https://www2.census.gov/library/publications/2025/demo/acsbr-025.pdf)
- [2020 Census race/ethnicity by state (PL 94-171 via Wikipedia compilation)](https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_race_and_ethnicity)
- [BLS — Cleveland MSA economy at a glance](https://www.bls.gov/eag/eag.oh_cleveland_msa.htm)
- [BLS Midwest — Indianapolis area economic summary](https://www.bls.gov/regions/midwest/summary/BLSSummary_Indianapolis.pdf)
- [Bureau of Labor Statistics — metro employment, May 2026](https://www.bls.gov/news.release/metro.nr0.htm)
- [Federal Housing Finance Agency — house price index, first-quarter 2026](https://www.fhfa.gov/reports/house-price-index/2026/Q1)
- [Federal Housing Finance Agency — state and metro summary tables](https://www.fhfa.gov/data/hpi/summary-tables)
- [U.S. Census Bureau — Vintage 2025 population estimates](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html)
- [Zillow May 2026 Rent Report](https://www.zillow.com/research/may-2026-rent-report-36461/)
- [Redfin June 2026 housing report](https://www.redfin.com/news/home-prices-record-high-june-2026/)
- [Forbes Advisor — median home prices by state (Redfin May 2026)](https://www.forbes.com/advisor/mortgages/real-estate/median-home-prices-by-state/)
- [World Population Review — median home price by state 2026](https://worldpopulationreview.com/state-rankings/median-home-price-by-state)
- [Keeping Up With Inflation — average/typical home values by state (Zillow June 2026)](https://keepingupwithinflation.com/statistics/home-prices-by-state/)
- [Phoenix metro suburb yields — Lux AZ (Mar 2026 ZHVI/ZORI)](https://luxazrentals.com/phoenix-metro-cap-rates-2026/) 
- [Independence, MO cash-flow suburb screen — Alpine KC 2026](https://www.alpinekansascity.com/2026/03/13/is-independence-missouri-still-one-of-the-best-cash-flow-markets-in-the-kansas-city-metro/)
- [DFW suburbs for rentals 2026 — Flat Fee Landlord](https://flatfeelandlord.com/blog/best-dfw-suburbs-rental-property-investment-2026)
- [Hamilton County (Indy) suburb guide 2026 — Leaseway](https://www.leasewayindy.com/blog/hamilton-county-rental-market-guide-2026)
- [Resideline 2026 cash-flow study](https://resideline.com/blog/highest-cash-flow-markets-2026)
- [Property tax rate compilations (Tax Foundation–based 2026 rankings)](https://www.financewonk.com/references/property-taxes-by-state)
- [2026 landlord insurance cost summaries](https://richeyinsurance.com/landlord-insurance-statistics/)
- [July 2026 investor loan rate sheets / comparisons](https://dscrfinder.com/blog/current-dscr-loan-rates)
- [Duplex / fourplex market guides and investor-loan comparisons](https://www.noradarealestate.com/blog/best-cities-to-buy-a-duplex-triplex-for-rental-income-2026/)
- Official legal pages for Washington, Oregon, California, New York, Chicago / Cook County (linked in Section 8)



### Caveats / data gaps
[↑ Back to Index](#index)


- Race/ethnicity uses **2020 Census** shares (NH racial categories + Hispanic any race). ACS updates will shift percentages modestly; re-pull for address-level work.
- **Mean household income** by state (ACS S1901/S1902) is marked `unavailable` because the Census data API now requires a key and the full mean table was not downloadable in this pass — do not treat median as mean.
- CPS ASEC state medians (FRED) and ACS 1-year metro medians are different surveys; do not mix them in one ratio without labeling.
- Entry capital and shock reserves are **screens** (25% down, ~3% closing, 7.5% PI, tax/insurance overlays, 6–9 months PITI) — not lender commitments or bindable insurance quotes. Recompute with live quotes and the exact address.
- Industry rankings use CES supersectors (trade/transportation/utilities, education & health, government, etc.). Automated pulls of the full BLS table were blocked; rankings combine the May 2026 BLS industry chart extracts with standard CES state profiles — treat exact ordering of close sectors as directional.
- Exact duplex / fourplex median prices are thinner than single-family data in many metros; those recommendations lean on multiple secondary guides plus like-for-like yield logic.
- Suburb prices / yields are often from local investor or property-management writeups layered on Zillow typical values — treat as screens, then pull MLS comps.
- Asking-rent indexes are not achieved rents.
- Redfin sale medians and Zillow typical values are different measures; both are shown as columns in the Section 4 ranking matrix. True mean (average) closed-sale prices by metro are often `unavailable` in public summaries — labeled honestly rather than invented.
- North Dakota and Wyoming state medians use the same May 2026 Redfin-based series via World Population Review because the Forbes table omitted those two rows.
- Insurance quotes are ZIP- and roof-specific; state ranges are directional only.
- Metro payroll estimates are preliminary and can revise.
- At mid-2026 investor rates, many 5–6% gross-yield markets will not produce positive leveraged cash flow after tax and insurance.



### A–Z actionable-rank index
[↑ Back to Index](#index)


Actionable rank by postal abbreviation (1 = highest). **Every** state links to its [§6 deep dive](#6-all-state-deep-dives). Companion tables [4a](#4a-scores-actionable-order)–[4d](#4d-demographics--income-same-order) use the same rank order. [↑ Index](#index)

| | | | | |
|---|---|---|---|---|
| [AK](#alaska) 28 | [AL](#alabama) 7 | [AR](#arkansas) 3 | [AZ](#arizona) 39 | [CA](#california) 50 |
| [CO](#colorado) 47 | [CT](#connecticut) 37 | [DC](#district-of-columbia) 51 | [DE](#delaware) 38 | [FL](#florida) 32 |
| [GA](#georgia) 16 | [HI](#hawaii) 46 | [IA](#iowa) 4 | [ID](#idaho) 31 | [IL](#illinois) 22 |
| [IN](#indiana) 2 | [KS](#kansas) 15 | [KY](#kentucky) 8 | [LA](#louisiana) 27 | [MA](#massachusetts) 45 |
| [MD](#maryland) 40 | [ME](#maine) 30 | [MI](#michigan) 13 | [MN](#minnesota) 26 | [MO](#missouri) 5 |
| [MS](#mississippi) 17 | [MT](#montana) 35 | [NC](#north-carolina) 20 | [ND](#north-dakota) 12 | [NE](#nebraska) 11 |
| [NH](#new-hampshire) 41 | [NJ](#new-jersey) 43 | [NM](#new-mexico) 25 | [NV](#nevada) 36 | [NY](#new-york) 42 |
| [OH](#ohio) 1 | [OK](#oklahoma) 19 | [OR](#oregon) 48 | [PA](#pennsylvania) 9 | [RI](#rhode-island) 44 |
| [SC](#south-carolina) 18 | [SD](#south-dakota) 21 | [TN](#tennessee) 10 | [TX](#texas) 23 | [UT](#utah) 34 |
| [VA](#virginia) 24 | [VT](#vermont) 29 | [WA](#washington) 49 | [WI](#wisconsin) 6 | [WV](#west-virginia) 14 |
| [WY](#wyoming) 33 |  |  |  |  |

---

*End of base report (prices, suburbs, top industries, demographics, and income integrated into rankings / cities / deep dives). Re-pull live comps, tax bills, and bindable insurance quotes before deploying capital. Future dated runs should keep this section structure.*