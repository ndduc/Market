"""Expand report: deep dives for all remaining states; drop §7 cards; renumber."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"C:\Users\ndduc\OneDrive\house\Market")
report_path = ROOT / "rental_market_report.md"
text = report_path.read_text(encoding="utf-8")

# Exact prices from cards / 4b (full dollars when known from cards)
EXACT_PRICES = {
    "Georgia": ("$373,700", "$335,358", "Atlanta metro median **$408,776**."),
    "Mississippi": ("$265,200", "$198,428", "Jackson investor-screen ~**$88,000**."),
    "South Carolina": ("$397,600", "$309,323", "Coastal metros need insurance stress tests."),
    "Oklahoma": ("$256,700", "$225,437", "Oklahoma City / Tulsa are the primary screens."),
    "North Carolina": ("$381,700", "$340,430", "Charlotte metro median **$428,716**; Raleigh thinner day-one cash flow."),
    "South Dakota": ("$318,500", "$325,618", "Sioux Falls / Rapid City; scale is the constraint."),
    "Illinois": ("$314,200", "$298,871", "Chicago metro median **$408,776**; outside Chicago more workable."),
    "Texas": (
        "$341,800",
        "$302,999",
        "Houston **$345,665**, Dallas **$413,761**, Austin **$448,657**, San Antonio **$328,985**.",
    ),
    "Virginia": ("$462,400", "$419,920", "Virginia Beach metro median **$398,806**; Richmond / Hampton Roads preferred over D.C.-only thesis."),
    "New Mexico": ("$378,300", "$321,186", "Albuquerque is the primary balanced market."),
    "Louisiana": ("$260,300", "$217,968", "New Orleans / Baton Rouge; insurance drag is material."),
    "Minnesota": ("$354,500", "$356,887", "Minneapolis metro median **$408,776**."),
    "Alaska": ("$399,900", "$400,659", "Anchorage / Fairbanks; logistics raise operating cost."),
    "Vermont": ("$438,400", "$402,017", "Burlington is the main screen; small statewide scale."),
    "Maine": ("$390,400", "$424,107", "Portland / Bangor; tenant protections compress returns."),
    "New Hampshire": ("$500,200", "$522,944", "Manchester–Nashua; Boston spillover."),
    "Idaho": ("$476,300", "$482,199", "Boise / Idaho Falls / Coeur d’Alene."),
    "Utah": ("$575,300", "$541,692", "Salt Lake City / Provo / Ogden."),
    "Florida": (
        "$416,800",
        "$378,126",
        "Tampa **$391,328**, Orlando **$413,761**, Miami **$576,124**, Jacksonville **$394,215**.",
    ),
    "Wyoming": ("$440,300", "$372,526", "Cheyenne / Casper; small markets."),
    "Montana": ("$505,600", "$476,115", "Billings / Missoula / Bozeman; lifestyle metros pricey."),
    "Nevada": ("$468,900", "$448,215", "Las Vegas metro median **$453,642**; Reno secondary."),
    "Arizona": ("$452,500", "$422,822", "Phoenix metro median **$463,612**; Tucson secondary."),
    "Connecticut": ("$445,100", "$455,424", "Hartford / Bridgeport / New Haven."),
    "Delaware": ("$366,200", "$412,252", "Wilmington is the only scalable screen."),
    "Maryland": ("$446,900", "$436,104", "Baltimore metro median **$438,686**."),
    "New York": ("$595,500", "$525,947", "New York City metro median **$843,474** (upstate far lower)."),
    "New Jersey": ("$545,300", "$584,681", "Newark metro median **$697,245**."),
    "Rhode Island": ("$535,100", "$517,078", "Providence metro median **$547,361**."),
    "Massachusetts": ("$645,400", "$672,867", "Boston metro median **$797,612**; Worcester / Springfield secondary."),
    "Colorado": ("$604,600", "$543,435", "Denver metro median **$607,070**."),
    "Oregon": ("$508,100", "$504,432", "Portland metro median **$568,298**."),
    "Hawaii": ("$773,400", "$836,741", "Honolulu; extreme entry cost."),
    "Washington": ("$644,300", "$603,303", "Seattle metro median **$827,522**; Spokane may be better value."),
    "California": (
        "$854,000",
        "$775,549",
        "Los Angeles **$947,164**, San Francisco **$1,724,835**, San Diego **$952,149**, Sacramento **$598,209**.",
    ),
    "District of Columbia": ("$676,500", "$579,332", "Metro median **$623,134**."),
}

SUBURBS = {
    "Georgia": "Atlanta — suburbs vs intown diverge sharply; screen for concessions. Athens is the job-growth satellite.",
    "Mississippi": "Jackson is the main high-yield screen; Gulfport / Hattiesburg secondary. Neighborhood and insurance diligence required.",
    "South Carolina": "Greenville (jobs / migration); Columbia (value); Charleston coastal (insurance / flood).",
    "Oklahoma": "Oklahoma City and Tulsa; hail / tornado insurance can erase thin deals.",
    "North Carolina": "Raleigh / Cary (jobs, thinner cash flow); Charlotte banking suburbs; Greensboro value screen.",
    "South Dakota": "Sioux Falls primary; Rapid City secondary. Limited scale / exit liquidity.",
    "Illinois": "Outside Chicago preferred for landlord ops; Peoria appreciated strongly; Chicago city rules need local counsel.",
    "Texas": "DFW — Frisco / McKinney / Plano (appreciation) and Forney / Mansfield (better rent-to-price); Houston — Katy / Cypress / Spring–Klein (balanced).",
    "Virginia": "Richmond and Hampton Roads / Virginia Beach over a pure Northern Virginia / D.C. thesis in 2026.",
    "New Mexico": "Albuquerque primary; Santa Fe lifestyle / higher entry; Las Cruces secondary.",
    "Louisiana": "Baton Rouge often cleaner ops than New Orleans for remote owners; Gulf insurance is the deal-breaker screen.",
    "Minnesota": "Twin Cities suburbs for liquidity; Duluth / Rochester smaller screens; watch local ordinances.",
    "Alaska": "Anchorage primary; Fairbanks secondary. Extreme logistics / seasonal ops.",
    "Vermont": "Burlington metro only meaningful screen; statewide inventory thin.",
    "Maine": "Portland metro; Bangor value. Tenant-leaning rules and high entry vs Midwest.",
    "New Hampshire": "Manchester–Nashua; Boston spillover appreciation more than day-one yield.",
    "Idaho": "Boise metro primary; Idaho Falls / Coeur d’Alene secondary. Prices limit income returns.",
    "Utah": "Salt Lake / Provo / Ogden corridor; strong demand, thin yields at current prices.",
    "Florida": "Tampa / Jacksonville often cleaner than Miami for income screens; get bindable insurance quotes before offering.",
    "Wyoming": "Cheyenne / Casper only; very small markets.",
    "Montana": "Billings value vs Missoula / Bozeman lifestyle premiums.",
    "Nevada": "Las Vegas valley suburbs; Reno secondary. Tourism cyclicality.",
    "Arizona": "West Valley CF — Buckeye / Surprise / Avondale; East Valley — Mesa / Tempe (balanced), Gilbert / Chandler (appreciation / schools).",
    "Connecticut": "Hartford cash-flow tilt; Bridgeport–Stamford appreciation corridor.",
    "Delaware": "Wilmington / New Castle County; Dover smaller.",
    "Maryland": "Baltimore income screens; Montgomery / Prince George’s higher entry and local friction.",
    "New York": "Upstate (Buffalo / Rochester / Syracuse) far more investable than NYC; Good Cause opt-ins vary by city.",
    "New Jersey": "Newark / Camden / New Brunswick corridor; taxes and Anti-Eviction Act dominate underwriting.",
    "Rhode Island": "Providence metro; small statewide scale.",
    "Massachusetts": "Worcester / Springfield for any income attempt; Boston proper too expensive for cash-flow-first.",
    "Colorado": "Denver metro soft YoY; Colorado Springs / Front Range secondary screens.",
    "Oregon": "Portland weak near-term (jobs + statewide rent stabilization); Salem / Eugene secondary.",
    "Hawaii": "Honolulu Oahu primary; neighbor islands even thinner liquidity for mainland investors.",
    "Washington": "Spokane often the better value screen than Seattle / Tacoma under statewide rent caps.",
    "California": "Inland Empire / Sacramento / Central Valley for any cash-flow attempt; coastal metros specialist-only.",
    "District of Columbia": "District proper vs Maryland / Virginia suburbs — TOPA / rent stabilization make D.C. specialist-only.",
}

NARRATIVE = {
    "Georgia": "Athens job growth and Atlanta migration are positives, but Atlanta yields and concessions are weaker than Midwest alternatives. Owner law is excellent.",
    "Mississippi": "Huge gross-yield potential on paper; insurance and liquidity justify a conservative cash-flow score. Jackson is the main screen.",
    "South Carolina": "Greenville is a top job-growth market; coastal areas need wind / flood insurance stress tests before any yield looks real.",
    "Oklahoma": "Excellent law and price, but unemployment rising to 4.2%, flat prices, and hail / tornado insurance justify the cash-flow haircut.",
    "North Carolina": "Raleigh’s +2.2% job growth is excellent; Charlotte / Raleigh prices mean thinner day-one cash flow than Midwest leaders.",
    "South Dakota": "2.0% unemployment is excellent; market scale and exit liquidity are the constraints, not jobs.",
    "Illinois": "Leads the nation in recent statewide appreciation; Chicago’s city ordinances and taxes require local expertise. Outside Chicago, the baseline is more workable.",
    "Texas": "Houston and Dallas–Fort Worth still grow population, but statewide prices are soft, property taxes are high (~1.6%), and Gulf / hail insurance matters. Austin remains a buyer’s market, not a clean appreciation call.",
    "Virginia": "Richmond and Hampton Roads beat a D.C.-dependent thesis in 2026 given federal payroll risk in Northern Virginia.",
    "New Mexico": "Albuquerque is the primary balanced market; federal / labs / tourism mix supports demand without coastal prices.",
    "Louisiana": "Cheap and landlord-friendly on statute, but insurance and weak long-term appreciation are material haircuts.",
    "Minnesota": "Stable Twin Cities demand; modest yields and some local ordinance risk keep it mid-pack.",
    "Alaska": "Strong appreciation prints, but expensive logistics and small scale limit remote-investor practicality.",
    "Vermont": "Tight labor and supply support demand; high entry prices and tenant protections compress income returns.",
    "Maine": "Similar New England pattern: solid demand, high entry, tenant-leaning friction vs Midwest cash-flow states.",
    "New Hampshire": "Strong incomes and Boston spillover; prices and tenant rules leave thin day-one yields for income-first buyers.",
    "Idaho": "Best-in-class owner law and solid Boise demand; current prices limit income returns.",
    "Utah": "Salt Lake corridor jobs are excellent; entry cost and thin yields make this an appreciation / quality screen, not a cash-flow leader.",
    "Florida": "Strong owner law and migration do not erase insurance, association fees, and soft-rent risk. Bindable quotes before offering.",
    "Wyoming": "Favorable law and jobs, but very small markets and limited liquidity.",
    "Montana": "Favorable law; lifestyle metros (Missoula / Bozeman) are expensive relative to rents.",
    "Nevada": "Las Vegas jobs are strong; tourism / gaming cyclicality remains the vacancy risk.",
    "Arizona": "Owner-friendly, but Phoenix rent growth was soft and concessions elevated — underwrite achieved rent.",
    "Connecticut": "Hartford can cash flow and appreciation has been strong; unemployment deterioration is a warning flag.",
    "Delaware": "Balanced but small; Wilmington is the only scalable screen.",
    "Maryland": "Baltimore income is plausible; local stabilization and operating friction must be priced. High statewide incomes.",
    "New York": "Upstate cities are far more investable than New York City, though Good Cause has expanded to several opt-in cities.",
    "New Jersey": "Strong appreciation and demand, but taxes (~2.23% effective) and Anti-Eviction rules require lower leverage and more reserves.",
    "Rhode Island": "Durable small-state demand; yields generally too thin for income-first investors.",
    "Massachusetts": "Durable Boston-metro demand; yields generally too thin for income-first investors outside secondary cities.",
    "Colorado": "Statewide prices down about 2.4% year over year; high entry cost and for-cause changes make 2026 a watch market.",
    "Oregon": "Portland job losses and statewide rent stabilization weaken the near-term case.",
    "Hawaii": "Low unemployment cannot overcome extreme entry cost for normal cash-flow investing.",
    "Washington": "Statewide rent cap, weak Seattle pricing, elevated unemployment; Spokane may be the better value screen.",
    "California": "Inland markets can work; coastal prices and statewide / local tenant rules make cash flow difficult for standard leverage.",
    "District of Columbia": "TOPA / rent stabilization plus the largest confirmed metro job loss make this specialist-only.",
}

BEST = {
    "Georgia": ("Athens / selected Atlanta suburbs for growth; Midwest still better for day-one cash flow.", "Atlanta concessions; inland vs coastal divergence.", "High"),
    "Mississippi": ("Jackson high-yield single-family / small multifamily with strong local PM.", "Insurance; ops intensity; exit liquidity.", "Medium"),
    "South Carolina": ("Greenville growth single-family; avoid uninsured coastal yield chasing.", "Wind / flood insurance; coastal HOA costs.", "High"),
    "Oklahoma": ("OKC / Tulsa value buys only after bindable hail quotes.", "Insurance; soft prices; job softness.", "High"),
    "North Carolina": ("Raleigh growth with lower leverage; Greensboro value screens.", "Thin day-one yields in Triangle / Charlotte.", "High"),
    "South Dakota": ("Sioux Falls long-term hold; keep expectations on scale.", "Thin buyer pool; limited inventory.", "Medium"),
    "Illinois": ("Secondary metros / suburbs for appreciation + income; Chicago only with local expertise.", "City ordinances; taxes; Chicago-specific rules.", "High"),
    "Texas": ("Houston / DFW workforce suburbs; stress tax + insurance.", "Property tax; insurance; Austin soft thesis.", "High"),
    "Virginia": ("Richmond / Hampton Roads balanced; caution on NoVA federal exposure.", "Federal payroll risk; higher entry than Midwest.", "High"),
    "New Mexico": ("Albuquerque balanced single-family.", "Thin liquidity outside Albuquerque; income levels.", "Medium"),
    "Louisiana": ("Selected inland / Baton Rouge value only with insurance quotes.", "Catastrophe insurance; weak appreciation.", "Medium"),
    "Minnesota": ("Twin Cities turnkey with modest yield expectations.", "Local ordinances; thin yields.", "High"),
    "Alaska": ("Anchorage only for locals / specialists.", "Logistics; climate; small scale.", "Medium"),
    "Vermont": ("Burlington specialty / low leverage.", "Tenant rules; high entry; tiny scale.", "Medium"),
    "Maine": ("Portland metro low-leverage hold.", "Tenant protections; high entry.", "Medium"),
    "New Hampshire": ("Manchester–Nashua appreciation / quality.", "Thin yields; tenant-leaning friction.", "Medium"),
    "Idaho": ("Boise quality long-term; accept thin cash flow.", "High prices vs rents.", "High"),
    "Utah": ("Salt Lake corridor quality / jobs; not income-first.", "High entry; thin yields.", "High"),
    "Florida": ("Inland / Jacksonville / Tampa only after insurance binds.", "Insurance; concessions; HOA.", "High"),
    "Wyoming": ("Small-scale Cheyenne / Casper only.", "Liquidity; energy cyclicality.", "Medium"),
    "Montana": ("Billings value over Bozeman lifestyle premiums.", "High lifestyle prices; small markets.", "Medium"),
    "Nevada": ("Las Vegas with tourism vacancy stress tests.", "Tourism cyclicality.", "High"),
    "Arizona": ("West Valley cash-flow tilt; East Valley schools / appreciation.", "Soft rents; concessions.", "High"),
    "Connecticut": ("Hartford income screens; watch jobs.", "Unemployment deterioration; tenant rules.", "High"),
    "Delaware": ("Wilmington small-portfolio only.", "Scale; limited screens.", "Medium"),
    "Maryland": ("Baltimore income with local-rule pricing.", "Stabilization / ops friction; high taxes in places.", "High"),
    "New York": ("Upstate cash flow / value; avoid NYC unless specialist.", "Good Cause opt-ins; NYC regulation.", "High"),
    "New Jersey": ("Lower leverage, higher reserves; demand is not the problem.", "Taxes; Anti-Eviction Act.", "High"),
    "Rhode Island": ("Providence low-leverage specialty.", "Thin yields; small scale.", "Medium"),
    "Massachusetts": ("Secondary cities only for income attempts; Boston is appreciation / specialty.", "Extreme entry; regulation.", "High"),
    "Colorado": ("Watch / selectively buy after price digestion.", "Soft prices; for-cause; high entry.", "High"),
    "Oregon": ("Wait / specialist only while Portland jobs and rent rules weigh.", "Rent stabilization; job losses.", "High"),
    "Hawaii": ("Not a standard cash-flow market.", "Extreme prices; tourism / military mix.", "Medium"),
    "Washington": ("Spokane value over Seattle; model statewide rent caps.", "Rent cap; Seattle softness; unemployment.", "High"),
    "California": ("Inland value screens only; coastal specialist.", "Statewide / local tenant rules; extreme coastal prices.", "High"),
    "District of Columbia": ("Specialist only (TOPA / rent stabilization).", "Federal job loss; TOPA; rent rules.", "High"),
}

# Parse 4a / 4c / 4d for remaining states
def parse_table(section_start: str, section_end: str):
    chunk = text[text.index(section_start) : text.index(section_end)]
    rows = {}
    for line in chunk.splitlines():
        if not line.startswith("|") or "State" in line or line.startswith("|---") or re.match(r"\| ---", line):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 3:
            continue
        try:
            num = int(parts[0])
        except ValueError:
            continue
        state = parts[1].split(" — ")[0].strip()
        rows[state] = (num, parts)
    return rows


scores = parse_table("### 4a. Scores", "### 4b. Prices")
industries = parse_table("### 4c. Top job industries", "### 4d. Demographics")
demos = parse_table("### 4d. Demographics", "### Notes on score changes")

already = {
    "Ohio", "Indiana", "Arkansas", "Iowa", "Missouri", "Wisconsin", "Alabama",
    "Kentucky", "Pennsylvania", "Tennessee", "Nebraska", "North Dakota", "Michigan",
    "West Virginia", "Kansas",
}

# Order remaining by actionable rank
remaining = sorted(
    [s for s in scores if s not in already],
    key=lambda s: scores[s][0],
)

blocks = []
for state in remaining:
    num, sp = scores[state]
    jobs, price, cash, appr = sp[2], sp[3], sp[4], sp[5]
    owner, tenant, conf = sp[7], sp[8], sp[9]
    ind = industries[state][1][2]
    conc = industries[state][1][3]
    race = demos[state][1][2]
    med_inc = demos[state][1][3]
    mean_inc = demos[state][1][4]
    med, typ, price_note = EXACT_PRICES[state]
    suburb = SUBURBS[state]
    narr = NARRATIVE[state]
    best, risks, conf_line = BEST[state]
    # prefer 4a conf if present
    conf_out = conf if conf else conf_line

    blocks.append(
        f"""### {state}

**Scores:** Jobs {jobs} / Price {price} / Cash flow {cash} / Appreciation {appr} / Owner law {owner} / Tenant law {tenant}  

**Prices:** State median **{med}** / typical **{typ}**. {price_note}  
**Top industries:** {ind}. {conc}  
**Demographics / income:** {race}. State median HH income **{med_inc}** (CPS 2024); mean HH income {mean_inc}.  
**Top suburbs:** {suburb}  

{narr}

**Best fit:** {best}  
**Risks:** {risks}  
**Confidence:** {conf_out}.
"""
    )

new_dives = "\n".join(blocks)

# Insert before --- ## 7
marker = "\n---\n\n\n\n## 7. Remaining-state decision cards"
if marker not in text:
    marker = "\n## 7. Remaining-state decision cards"
    idx = text.index(marker)
else:
    idx = text.index(marker)

# Find end of section 7 (start of legal)
legal = text.index("## 8. Legal environment")
# Keep Kansas ending: find last deep dive end - actually insert after Kansas section which ends just before --- ## 7
# Replace from --- ## 7 through just before ## 8 with new dives + renumbered legal heading prep

# Change section 6 title
text = text.replace("## 6. Top-state deep dives", "## 6. All-state deep dives", 1)

before = text[:idx].rstrip() + "\n\n"
# Remove section 7 entirely; renumber 8-11 -> 7-10
after = text[legal:]
after = after.replace("## 8. Legal environment", "## 7. Legal environment", 1)
after = after.replace("## 9. Insurance and property-tax overlays", "## 8. Insurance and property-tax overlays", 1)
after = after.replace("## 10. Practical acquisition workflow", "## 9. Practical acquisition workflow", 1)
after = after.replace("## 11. Methodology and sources", "## 10. Methodology and sources", 1)

text2 = before + "\n" + new_dives + "\n---\n\n" + after

# Update Index
old_index = """## Index

Jump to a section (companion tables in §4 share the same state order):

| | |
|---|---|
| [1. What changed](#1-what-changed-vs-the-prior-run) | [2. National snapshot](#2-national-market-snapshot) |
| [3. Top 10 / lists](#3-top-10-actionable-markets) | [4. All-state matrix](#4-all-state-ranking-matrix) |
| [4a Scores](#4a-scores-actionable-order) · [4b Prices](#4b-prices--major-metros-same-order) | [4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) |
| [5. City leaderboards](#5-city-leaderboards) | [6. Top-state deep dives](#6-top-state-deep-dives) |
| [7. Remaining-state cards](#7-remaining-state-decision-cards) | [8. Legal](#8-legal-environment--verified-2026-highlights) |
| [9. Insurance & tax](#9-insurance-and-property-tax-overlays) | [10. Acquisition workflow](#10-practical-acquisition-workflow) |
| [11. Methodology & sources](#11-methodology-and-sources) | [A–Z state rank index](#az-actionable-rank-index) |

**Deep dives:** [OH](#ohio) · [IN](#indiana) · [AR](#arkansas) · [IA](#iowa) · [MO](#missouri) · [WI](#wisconsin) · [AL](#alabama) · [KY](#kentucky) · [PA](#pennsylvania) · [TN](#tennessee) · [NE](#nebraska) · [ND](#north-dakota) · [MI](#michigan) · [WV](#west-virginia) · [KS](#kansas)

**City boards:** [Cash flow](#cash-flow-potential-gross-yield-is-a-screen) · [Single-family](#best-for-single-family-houses) · [2–4 unit](#best-for-24-unit-multifamily-homes) · [Top suburbs](#top-suburbs-worth-researching-live-2026-screen) · [Appreciation](#appreciation-leaders-first-quarter-2026-federal-housing-finance-agency) · [Jobs](#job-market-leaders-may-2026-payroll-changes)
"""

# Build full deep dive link list in actionable order
all_states_ordered = sorted(scores.keys(), key=lambda s: scores[s][0])
abbr = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "District of Columbia": "DC",
    "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA",
    "Maine": "ME", "Maryland": "MD", "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
    "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR",
    "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT", "Virginia": "VA",
    "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY",
}

def slug(state: str) -> str:
    return state.lower().replace(" ", "-").replace(".", "")

dive_links = " · ".join(f"[{abbr[s]}](#{slug(s)})" for s in all_states_ordered)

new_index = f"""## Index

Jump to a section (companion tables in §4 share the same state order):

| | |
|---|---|
| [1. What changed](#1-what-changed-vs-the-prior-run) | [2. National snapshot](#2-national-market-snapshot) |
| [3. Top 10 / lists](#3-top-10-actionable-markets) | [4. All-state matrix](#4-all-state-ranking-matrix) |
| [4a Scores](#4a-scores-actionable-order) · [4b Prices](#4b-prices--major-metros-same-order) | [4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) |
| [5. City leaderboards](#5-city-leaderboards) | [6. All-state deep dives](#6-all-state-deep-dives) |
| [7. Legal](#7-legal-environment--verified-2026-highlights) | [8. Insurance & tax](#8-insurance-and-property-tax-overlays) |
| [9. Acquisition workflow](#9-practical-acquisition-workflow) | [10. Methodology & sources](#10-methodology-and-sources) |
| [A–Z state rank index](#az-actionable-rank-index) | |

**Deep dives (all states + D.C., actionable order):** {dive_links}

**City boards:** [Cash flow](#cash-flow-potential-gross-yield-is-a-screen) · [Single-family](#best-for-single-family-houses) · [2–4 unit](#best-for-24-unit-multifamily-homes) · [Top suburbs](#top-suburbs-worth-researching-live-2026-screen) · [Appreciation](#appreciation-leaders-first-quarter-2026-federal-housing-finance-agency) · [Jobs](#job-market-leaders-may-2026-payroll-changes)
"""

# Flexible replace of index block
idx_start = text2.index("## Index\n")
idx_end = text2.index("\n---\n\n## 1. What changed")
text2 = text2[:idx_start] + new_index + text2[idx_end:]

# Update A-Z to link every state
az_rows = []
items = [(abbr[s], scores[s][0], s) for s in all_states_ordered]
# rebuild as 5-col table in alpha order by abbr
items_alpha = sorted(items, key=lambda x: x[0])
cells = [f"[{a}](#{slug(s)}) {n}" for a, n, s in items_alpha]
# pad to multiple of 5
while len(cells) % 5:
    cells.append("")
az_lines = ["| | | | | |", "|---|---|---|---|---|"]
for i in range(0, len(cells), 5):
    az_lines.append("| " + " | ".join(cells[i : i + 5]) + " |")

az_block = (
    "### A–Z actionable-rank index\n\n"
    "Actionable rank by postal abbreviation (1 = highest). **Every** state links to its [§6 deep dive](#6-all-state-deep-dives). "
    "Companion tables [4a](#4a-scores-actionable-order)–[4d](#4d-demographics--income-same-order) use the same rank order. [↑ Index](#index)\n\n"
    + "\n".join(az_lines)
    + "\n"
)

az_start = text2.index("### A–Z actionable-rank index")
az_end = text2.index("\n---\n\n*End of base report")
text2 = text2[:az_start] + az_block + text2[az_end:]

# Section 6 intro blurb
text2 = text2.replace(
    "## 6. All-state deep dives\n\n\n\n",
    "## 6. All-state deep dives\n\n"
    "Deep dives for **all 50 states + D.C.** in actionable-rank order. "
    "Same field labels throughout: Scores, Prices, Top industries, Demographics / income, Top suburbs, Best fit, Risks, Confidence. "
    "[↑ Index](#index) · [A–Z](#az-actionable-rank-index)\n\n",
    1,
)

# What changed row
if "**All-state deep dives**" not in text2:
    text2 = text2.replace(
        "| **Index / navigation**",
        "| **All-state deep dives** | **Every state + D.C.** has a full §6 deep dive (no remaining-state bullet cards) |\n| **Index / navigation**",
        1,
    )

# Fix legal heading anchor note in body if any leftover §7 cards reference
assert "## 7. Remaining-state" not in text2
assert "### Georgia\n" in text2
assert "### California\n" in text2
assert "### District of Columbia\n" in text2
assert len(remaining) == 36, len(remaining)

report_path.write_text(text2, encoding="utf-8")
print(f"added {len(remaining)} deep dives; total states with ### headings check")
print("remaining sample", remaining[:5], "...", remaining[-3:])
