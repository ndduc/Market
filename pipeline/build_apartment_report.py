"""Build apartment_market_report.md from shared data/ + apartment scoring tables.

Format contract: same section order as rental_market_report.md (see apartment_market_spec.md).
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "apartment_market_report.md"

# Actionable apartment order (judgment): deep inventory + workable law + NOI realism.
# Scores are directional 1–10; Cash haircuts supply/concessions; Owner penalizes rent control harder.
STATES: list[dict] = [
    {"abbr": "OH", "name": "Ohio", "metros": "Cleveland, Columbus, Cincinnati",
     "jobs": 8, "price": 8, "cash": 9, "appr": 7, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "about $60k–$110k/door Class B/C garden (directional brokerage screens)",
     "deal_illust": "$4.5M (about 50 doors × $90k)", "cash_close": "$1.5M", "shock": "$180k", "total_liq": "$1.7M",
     "rent_screen": "asking / in-place often about $1,100–$1,500/unit in secondary metros",
     "occ": "generally stable Midwest occupancy; verify lease-up on new Class A",
     "conc": "lighter than Sun Belt Class A; still model 0.5–1 mo on competitive assets",
     "cap": "Class B/C often wider than coastal Class A (verify live print)",
     "submarkets": "Cleveland — near-east / west-side Class B/C value-add; Columbus — suburban garden corridors; Cincinnati — I-71 / northern KY spillover",
     "best": "Class B/C garden value-add and light renovations; Columbus for growth lease-up if basis works",
     "risks": "older systems; neighborhood variance; tax drag in some counties"},
    {"abbr": "IN", "name": "Indiana", "metros": "Indianapolis, Fort Wayne, South Bend",
     "jobs": 8, "price": 8, "cash": 9, "appr": 7, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "about $70k–$120k/door common Indy Class B screens",
     "deal_illust": "$5.0M (about 50 doors × $100k)", "cash_close": "$1.7M", "shock": "$190k", "total_liq": "$1.9M",
     "rent_screen": "Indy workforce rents often about $1,200–$1,600/unit",
     "occ": "stable with pockets of new supply", "conc": "rising in Indy Class A — do not underwrite asking",
     "cap": "Midwest Class B screens typically above coastal Class A",
     "submarkets": "Indy — east/south workforce Class B; north suburban Class A/B; Fort Wayne garden stock",
     "best": "Indianapolis Class B workforce; selected Fort Wayne gardens",
     "risks": "concessions on new product; Bloomington employer concentration"},
    {"abbr": "MO", "name": "Missouri", "metros": "Kansas City, St. Louis, Springfield",
     "jobs": 7, "price": 8, "cash": 8, "appr": 7, "owner": 8, "tenant": 3, "conf": "High",
     "shock_mo": 6, "door_screen": "about $65k–$115k/door Class B/C screens",
     "deal_illust": "$4.8M (about 50 doors × $95k)", "cash_close": "$1.6M", "shock": "$185k", "total_liq": "$1.8M",
     "rent_screen": "KC / STL Class B often about $1,100–$1,550/unit",
     "occ": "stable; submarket selection critical in STL", "conc": "moderate; heavier on new suburban Class A",
     "cap": "value-add Class C can print wide — ops risk priced in",
     "submarkets": "KC — Independence / eastern Jackson CF; JoCo KS side more tenant-quality; STL — carefully screened inner-ring Class B/C",
     "best": "KC balanced Class B; STL income with strong management",
     "risks": "STL neighborhood / crime variance; property taxes"},
    {"abbr": "AL", "name": "Alabama", "metros": "Birmingham, Huntsville, Mobile",
     "jobs": 8, "price": 8, "cash": 8, "appr": 6, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "about $55k–$100k/door Birmingham Class B/C screens",
     "deal_illust": "$4.0M (about 50 doors × $80k)", "cash_close": "$1.3M", "shock": "$170k", "total_liq": "$1.5M",
     "rent_screen": "Birmingham income product often about $900–$1,350/unit",
     "occ": "stable outside heavy new-delivery pockets", "conc": "watch Huntsville Class A lease-up",
     "cap": "Birmingham Class B/C often attractive going-in vs coasts",
     "submarkets": "Birmingham — eastern / southern Class B; Huntsville — growth Class A/B; Mobile — coastal insurance overlay",
     "best": "Birmingham Class B/C cash flow; Huntsville growth if basis and concessions work",
     "risks": "insurance (esp. Mobile); city operating variance"},
    {"abbr": "TN", "name": "Tennessee", "metros": "Memphis, Nashville, Knoxville, Chattanooga",
     "jobs": 8, "price": 7, "cash": 8, "appr": 6, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "Memphis often cheaper/door; Nashville much higher",
     "deal_illust": "$5.5M (illustrative mid-market 50-door)", "cash_close": "$1.8M", "shock": "$200k", "total_liq": "$2.0M",
     "rent_screen": "Memphis Class B/C lower; Nashville Class A/B higher with concession risk",
     "occ": "Memphis ops-intensive; Nashville supply-sensitive", "conc": "Nashville Class A still concession-prone",
     "cap": "Memphis wider; Nashville tighter / more competitive",
     "submarkets": "Memphis — east / southeast Class B/C; Nashville — suburban garden vs urban core; Knoxville secondary depth",
     "best": "Memphis income with strong ops; Nashville only with lease-up / basis discipline",
     "risks": "two-market state; Memphis crime/ops; Nashville oversupply pockets"},
    {"abbr": "PA", "name": "Pennsylvania", "metros": "Pittsburgh, Philadelphia, Lancaster",
     "jobs": 6, "price": 7, "cash": 8, "appr": 7, "owner": 7, "tenant": 4, "conf": "High",
     "shock_mo": 6, "door_screen": "Pittsburgh often cheaper/door than Philly",
     "deal_illust": "$6.0M (about 50 doors mid-market)", "cash_close": "$2.0M", "shock": "$220k", "total_liq": "$2.2M",
     "rent_screen": "Pittsburgh Class B often workable; Philly higher rent / higher tax",
     "occ": "generally stable older stock", "conc": "lighter than Sun Belt; competitive near new product",
     "cap": "Pittsburgh value-add wider; Philly institutional tighter",
     "submarkets": "Pittsburgh — east/south Class B/C; Philly — carefully screened Class B; suburbs for Class A",
     "best": "Pittsburgh Class B/C; Philly liquidity for larger sponsors",
     "risks": "older housing; Philly local taxes / rules"},
    {"abbr": "GA", "name": "Georgia", "metros": "Atlanta, Athens, Augusta, Savannah",
     "jobs": 9, "price": 6, "cash": 6, "appr": 5, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "Atlanta $/door spans wide by class and submarket",
     "deal_illust": "$7.5M (illustrative 50-door Atlanta Class B)", "cash_close": "$2.5M", "shock": "$250k", "total_liq": "$2.7M",
     "rent_screen": "Atlanta Class B often about $1,400–$1,900/unit — verify concessions",
     "occ": "recovering as deliveries slow; still submarket-specific", "conc": "still material on newer suburban Class A",
     "cap": "compressed vs Midwest value-add; better on true B/C",
     "submarkets": "Atlanta — south/east workforce Class B; north prestige Class A; Augusta / Savannah secondary",
     "best": "Atlanta Class B workforce with supply visibility; secondary metros for simpler basis",
     "risks": "delivery hangover; insurance in coastal Savannah"},
    {"abbr": "KY", "name": "Kentucky", "metros": "Louisville, Lexington",
     "jobs": 5, "price": 8, "cash": 8, "appr": 8, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Louisville Class B/C often affordable vs peers",
     "deal_illust": "$4.2M (about 50 doors × $85k)", "cash_close": "$1.4M", "shock": "$175k", "total_liq": "$1.6M",
     "rent_screen": "Louisville workforce rents often about $1,000–$1,450/unit",
     "occ": "stable secondary-market profile", "conc": "moderate",
     "cap": "often wider than coastal Class A",
     "submarkets": "Louisville — south/east Class B; Lexington — university-adjacent demand",
     "best": "Louisville Class B scale; Lexington smaller/stabler",
     "risks": "state unemployment softer; thinner institutional exits outside Louisville"},
    {"abbr": "WI", "name": "Wisconsin", "metros": "Milwaukee, Madison, Green Bay",
     "jobs": 8, "price": 6, "cash": 7, "appr": 8, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 6, "door_screen": "Milwaukee cheaper/door; Madison more expensive",
     "deal_illust": "$5.5M (illustrative 50-door)", "cash_close": "$1.8M", "shock": "$210k", "total_liq": "$2.0M",
     "rent_screen": "Milwaukee Class B income; Madison higher rents / tighter yields",
     "occ": "stable", "conc": "lighter Midwest pattern",
     "cap": "Milwaukee value-add wider; Madison tighter",
     "submarkets": "Milwaukee — near-south / west Class B/C; Madison — west side / suburban Class A/B",
     "best": "Milwaukee income; Madison stability / higher entry",
     "risks": "property taxes; winter OpEx"},
    {"abbr": "MI", "name": "Michigan", "metros": "Detroit, Grand Rapids, Lansing, Ann Arbor",
     "jobs": 4, "price": 8, "cash": 8, "appr": 7, "owner": 8, "tenant": 3, "conf": "High",
     "shock_mo": 9, "door_screen": "Detroit Class C can look very cheap/door — ops risk priced in",
     "deal_illust": "$3.5M (about 50 doors low-basis screen)", "cash_close": "$1.2M", "shock": "$220k", "total_liq": "$1.4M",
     "rent_screen": "Detroit Class C high printed gross; Grand Rapids more balanced",
     "occ": "Class C vacancy/collection risk; GR more stable", "conc": "varies sharply by class",
     "cap": "Detroit Class C very wide — not a free lunch",
     "submarkets": "Detroit — carefully screened Class B/C corridors; Grand Rapids garden Class B; Ann Arbor constrained/expensive",
     "best": "Grand Rapids balanced; Detroit only with institutional-grade ops",
     "risks": "auto concentration; Class C collections; exit liquidity"},
    {"abbr": "NC", "name": "North Carolina", "metros": "Charlotte, Raleigh, Greensboro, Durham",
     "jobs": 9, "price": 6, "cash": 5, "appr": 5, "owner": 8, "tenant": 3, "conf": "High",
     "shock_mo": 6, "door_screen": "Charlotte / Raleigh $/door elevated vs Midwest",
     "deal_illust": "$8.0M (illustrative 50-door Triangle / Charlotte)", "cash_close": "$2.7M", "shock": "$260k", "total_liq": "$2.9M",
     "rent_screen": "Class A/B rents higher; economic rent after concessions matters",
     "occ": "improving as deliveries slow; still supply-sensitive", "conc": "still common on new Class A",
     "cap": "tighter than Midwest value-add",
     "submarkets": "Charlotte — south/east suburban gardens; Raleigh–Durham — RTP-adjacent Class A/B; Greensboro value",
     "best": "Class B with clear supply visibility; avoid blind Class A lease-up",
     "risks": "delivery pipeline; basis risk after 2022–25 build wave"},
    {"abbr": "SC", "name": "South Carolina", "metros": "Greenville, Columbia, Charleston",
     "jobs": 8, "price": 6, "cash": 5, "appr": 5, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 9, "door_screen": "Greenville / Columbia cheaper than Charleston coastal",
     "deal_illust": "$6.5M (illustrative 50-door)", "cash_close": "$2.2M", "shock": "$280k", "total_liq": "$2.5M",
     "rent_screen": "inland Class B workable; Charleston higher / insurance",
     "occ": "mixed with new supply inland and coastal", "conc": "watch Class A lease-up",
     "cap": "inland wider than Charleston trophy",
     "submarkets": "Greenville — Upstate garden Class B; Columbia — workforce; Charleston — coastal insurance overlay",
     "best": "Greenville / Columbia Class B; Charleston only with insurance math",
     "risks": "coastal insurance; supply in growth corridors"},
    {"abbr": "AR", "name": "Arkansas", "metros": "Little Rock, Fayetteville–Springdale, Fort Smith",
     "jobs": 8, "price": 8, "cash": 7, "appr": 7, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Little Rock often affordable/door; NWA pricier",
     "deal_illust": "$4.0M (about 50 doors)", "cash_close": "$1.3M", "shock": "$160k", "total_liq": "$1.5M",
     "rent_screen": "Little Rock income; NWA higher growth rents",
     "occ": "stable secondary; thinner broker prints", "conc": "lighter than large Sun Belt",
     "cap": "often attractive vs coasts when deals trade",
     "submarkets": "Little Rock — central / west Class B; NWA — growth corridors with higher basis",
     "best": "Little Rock income gardens; NWA growth if basis not stretched",
     "risks": "thinner apartment liquidity than OH/IN/MO; NWA repricing"},
    {"abbr": "IL", "name": "Illinois", "metros": "Chicago, Peoria, Rockford, Springfield",
     "jobs": 4, "price": 6, "cash": 6, "appr": 8, "owner": 6, "tenant": 6, "conf": "High",
     "shock_mo": 9, "door_screen": "Chicago institutional $/door; downstate thinner",
     "deal_illust": "$9.0M (illustrative Chicago Class B)", "cash_close": "$3.0M", "shock": "$350k", "total_liq": "$3.4M",
     "rent_screen": "Chicago Class B high rent / high tax / ordinance ops",
     "occ": "class and neighborhood dependent", "conc": "competitive in soft pockets",
     "cap": "institutional Chicago tighter; Class C wider with ops haircut",
     "submarkets": "Chicago — north/northwest Class B; south/west value-add with heavy underwriting; suburbs for Class A",
     "best": "experienced Chicago sponsors; Peoria/Rockford only with local ops",
     "risks": "city ordinance / taxes; soft jobs; Cook County complexity"},
    {"abbr": "TX", "name": "Texas", "metros": "Houston, Dallas–Fort Worth, San Antonio, Austin",
     "jobs": 8, "price": 7, "cash": 4, "appr": 3, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 9, "door_screen": "huge dispersion by metro/class; Austin still elevated",
     "deal_illust": "$8.5M (illustrative 50-door DFW/Houston Class B)", "cash_close": "$2.8M", "shock": "$320k", "total_liq": "$3.1M",
     "rent_screen": "asking often soft after concessions in oversupplied submarkets",
     "occ": "improving nationally but TX submarkets still lease-up heavy", "conc": "still aggressive in many Class A corridors (months free)",
     "cap": "wider than 2021 peak; still competitive for quality B",
     "submarkets": "DFW — eastern / southern workforce Class B; Houston — energy-cycle aware; Austin — concession / basis caution; SA — relative value",
     "best": "scale + landlord law; prefer clear supply visibility and economic rents",
     "risks": "concessions; insurance (esp. coastal/hail); property taxes"},
    {"abbr": "IA", "name": "Iowa", "metros": "Des Moines, Cedar Rapids, Iowa City",
     "jobs": 8, "price": 8, "cash": 7, "appr": 7, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Des Moines deepest; statewide thin vs Ohio",
     "deal_illust": "$3.8M (about 40–50 doors)", "cash_close": "$1.3M", "shock": "$155k", "total_liq": "$1.4M",
     "rent_screen": "workforce rents; university overlays in Iowa City / Ames",
     "occ": "stable secondary", "conc": "generally lighter",
     "cap": "wider when deals trade; fewer prints",
     "submarkets": "Des Moines — suburban gardens; Cedar Rapids industrial demand; Iowa City student-labeled if used",
     "best": "Des Moines Class B hold; avoid thin tertiary without local PM",
     "risks": "thin exits; Ames employer risk; property taxes"},
    {"abbr": "OK", "name": "Oklahoma", "metros": "Oklahoma City, Tulsa",
     "jobs": 5, "price": 8, "cash": 6, "appr": 4, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 9, "door_screen": "OKC / Tulsa often affordable/door",
     "deal_illust": "$3.8M (about 50 doors)", "cash_close": "$1.3M", "shock": "$200k", "total_liq": "$1.5M",
     "rent_screen": "workforce Class B/C",
     "occ": "stable secondary", "conc": "moderate",
     "cap": "often wider — energy and insurance haircuts apply",
     "submarkets": "OKC — north/west Class B; Tulsa — river / south corridors",
     "best": "OKC / Tulsa Class B with insurance discipline",
     "risks": "energy cycle; hail/wind insurance; softer jobs"},
    {"abbr": "KS", "name": "Kansas", "metros": "Wichita, Kansas City–KS, Topeka",
     "jobs": 7, "price": 7, "cash": 6, "appr": 6, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Wichita / KCKS affordable vs coasts",
     "deal_illust": "$4.0M (about 50 doors)", "cash_close": "$1.3M", "shock": "$170k", "total_liq": "$1.5M",
     "rent_screen": "workforce Class B",
     "occ": "stable", "conc": "lighter",
     "cap": "secondary-market wider prints when available",
     "submarkets": "Wichita — aviation-tied demand; JoCo KS — KC metro quality side",
     "best": "KCKS Class B as part of KC thesis; Wichita with employer awareness",
     "risks": "aviation concentration; thinner institutional capital"},
    {"abbr": "NE", "name": "Nebraska", "metros": "Omaha, Lincoln",
     "jobs": 8, "price": 7, "cash": 6, "appr": 7, "owner": 7, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Omaha deepest statewide",
     "deal_illust": "$4.5M (about 50 doors)", "cash_close": "$1.5M", "shock": "$180k", "total_liq": "$1.7M",
     "rent_screen": "Omaha Class B workforce / insurance-employment demand",
     "occ": "stable", "conc": "lighter Midwest",
     "cap": "secondary wider",
     "submarkets": "Omaha — west / southwest gardens; Lincoln — university + state gov demand",
     "best": "Omaha Class B long hold",
     "risks": "thinner apartment scale than Midwest Big 3; exit pools"},
    {"abbr": "MS", "name": "Mississippi", "metros": "Jackson, Gulfport, Hattiesburg",
     "jobs": 7, "price": 9, "cash": 6, "appr": 6, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 9, "door_screen": "low entry/door — ops and insurance priced in",
     "deal_illust": "$3.0M (about 50 doors low-basis)", "cash_close": "$1.0M", "shock": "$200k", "total_liq": "$1.2M",
     "rent_screen": "low rents; collections and condition matter",
     "occ": "Class C sensitive", "conc": "varies",
     "cap": "wide — not automatically investable",
     "submarkets": "Jackson — carefully screened Class B/C; Gulfport — coastal insurance",
     "best": "only with strong local ops and insurance quotes",
     "risks": "insurance; wage base; Class C intensity; thin exits"},
    {"abbr": "VA", "name": "Virginia", "metros": "Richmond, Virginia Beach, Northern Virginia",
     "jobs": 7, "price": 4, "cash": 5, "appr": 6, "owner": 8, "tenant": 3, "conf": "High",
     "shock_mo": 6, "door_screen": "NoVA expensive; Richmond more approachable",
     "deal_illust": "$9.0M (illustrative 50-door Richmond/NoVA mix)", "cash_close": "$3.0M", "shock": "$280k", "total_liq": "$3.3M",
     "rent_screen": "NoVA high rent / high basis; Richmond better yield screens",
     "occ": "generally solid demand", "conc": "competitive Class A pockets",
     "cap": "NoVA tight; Richmond wider",
     "submarkets": "Richmond — suburban Class B; Hampton Roads — military demand + insurance; NoVA — federal/cyber Class A",
     "best": "Richmond Class B; NoVA for larger/stabilized sponsors",
     "risks": "expensive entry in NoVA; coastal insurance in Hampton Roads"},
    {"abbr": "MN", "name": "Minnesota", "metros": "Minneapolis–St. Paul, Duluth, Rochester",
     "jobs": 6, "price": 5, "cash": 5, "appr": 6, "owner": 6, "tenant": 6, "conf": "High",
     "shock_mo": 9, "door_screen": "Twin Cities institutional pricing",
     "deal_illust": "$8.0M (illustrative 50-door MSP)", "cash_close": "$2.7M", "shock": "$300k", "total_liq": "$3.0M",
     "rent_screen": "MSP Class B solid rents; regulation/ops awareness",
     "occ": "generally stable", "conc": "moderate",
     "cap": "institutional mid-pack",
     "submarkets": "MSP — first-ring Class B; suburbs Class A; Rochester — Mayo demand",
     "best": "experienced MSP sponsors; Rochester niche",
     "risks": "local tenant rules; winter OpEx; taxes"},
    {"abbr": "FL", "name": "Florida", "metros": "Tampa, Orlando, Jacksonville, Miami",
     "jobs": 6, "price": 5, "cash": 3, "appr": 3, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 12, "door_screen": "wide by metro; insurance can dominate underwriting",
     "deal_illust": "$9.5M (illustrative 50-door)", "cash_close": "$3.2M", "shock": "$450k", "total_liq": "$3.6M",
     "rent_screen": "headline rents high; net after insurance/concessions often weaker",
     "occ": "supply + insurance reshaping submarkets", "conc": "still common in overbuilt corridors",
     "cap": "buyer/seller gap; insurance-adjusted returns critical",
     "submarkets": "Tampa / Jax — relative inland preference; Orlando — tourism seasonality; Miami — coastal / condo-adjacent complexity",
     "best": "only with locked insurance and economic rents; prefer lower catastrophe exposure",
     "risks": "insurance; assessments; concessions; tourism vacancy"},
    {"abbr": "LA", "name": "Louisiana", "metros": "New Orleans, Baton Rouge, Lafayette",
     "jobs": 6, "price": 8, "cash": 3, "appr": 5, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 12, "door_screen": "cheap entry often offset by insurance",
     "deal_illust": "$3.5M (about 50 doors)", "cash_close": "$1.2M", "shock": "$280k", "total_liq": "$1.5M",
     "rent_screen": "moderate rents; net yields insurance-sensitive",
     "occ": "mixed", "conc": "varies",
     "cap": "wide — catastrophe haircut required",
     "submarkets": "Baton Rouge — relatively better insurance math than coastal NOLA in many cases; NOLA — specialist only",
     "best": "Baton Rouge with hard insurance quotes; NOLA specialist",
     "risks": "wind/flood insurance; energy cycle; ops"},
    {"abbr": "ND", "name": "North Dakota", "metros": "Fargo, Bismarck",
     "jobs": 10, "price": 6, "cash": 5, "appr": 8, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Fargo deepest; statewide thin institutional inventory",
     "deal_illust": "$3.5M (smaller community screen)", "cash_close": "$1.2M", "shock": "$150k", "total_liq": "$1.3M",
     "rent_screen": "secondary-market rents; energy towns more volatile",
     "occ": "Fargo stabler than energy boom towns", "conc": "usually lighter",
     "cap": "few prints — Conf. Medium",
     "submarkets": "Fargo — primary apartment depth; Bismarck — capital/energy mix",
     "best": "Fargo Class B hold for local/regional sponsors",
     "risks": "thin exits; energy volatility outside Fargo"},
    {"abbr": "SD", "name": "South Dakota", "metros": "Sioux Falls, Rapid City",
     "jobs": 10, "price": 6, "cash": 5, "appr": 6, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Sioux Falls deepest",
     "deal_illust": "$3.8M (smaller community screen)", "cash_close": "$1.3M", "shock": "$160k", "total_liq": "$1.4M",
     "rent_screen": "Sioux Falls workforce / finance niches",
     "occ": "stable small-metro", "conc": "lighter",
     "cap": "few prints",
     "submarkets": "Sioux Falls — primary; Rapid City — tourism overlay",
     "best": "Sioux Falls Class B for regional buyers",
     "risks": "thin apartment scale / exits"},
    {"abbr": "WV", "name": "West Virginia", "metros": "Charleston, Huntington, Morgantown",
     "jobs": 6, "price": 9, "cash": 6, "appr": 6, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 6, "door_screen": "very low entry — thin apartment liquidity",
     "deal_illust": "$2.5M (small community)", "cash_close": "$0.9M", "shock": "$140k", "total_liq": "$1.0M",
     "rent_screen": "low rents; scale limited",
     "occ": "secondary", "conc": "usually light",
     "cap": "wide when deals appear; few comps",
     "submarkets": "Charleston / Huntington — workforce; Morgantown — university-labeled demand",
     "best": "small local sponsors only; not institutional screen",
     "risks": "thin exits; weak scale; wage base"},
    {"abbr": "NM", "name": "New Mexico", "metros": "Albuquerque, Santa Fe, Las Cruces",
     "jobs": 5, "price": 6, "cash": 5, "appr": 6, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Albuquerque primary depth",
     "deal_illust": "$5.0M (illustrative 50-door ABQ)", "cash_close": "$1.7M", "shock": "$190k", "total_liq": "$1.9M",
     "rent_screen": "ABQ Class B; Santa Fe higher / thinner",
     "occ": "mixed", "conc": "moderate",
     "cap": "secondary prints",
     "submarkets": "ABQ — northeast / west Class B; Santa Fe — constrained/expensive; Las Cruces secondary",
     "best": "Albuquerque Class B",
     "risks": "softer jobs; thin institutional capital"},
    {"abbr": "NV", "name": "Nevada", "metros": "Las Vegas, Reno",
     "jobs": 7, "price": 4, "cash": 4, "appr": 4, "owner": 8, "tenant": 3, "conf": "High",
     "shock_mo": 9, "door_screen": "Las Vegas Class A/B still competitive on basis",
     "deal_illust": "$8.0M (illustrative 50-door Vegas)", "cash_close": "$2.7M", "shock": "$300k", "total_liq": "$3.0M",
     "rent_screen": "tourism-tied; economic rent after concessions",
     "occ": "supply-sensitive", "conc": "often material on new product",
     "cap": "mid; watch cycle",
     "submarkets": "Las Vegas — suburban gardens vs Strip-adjacent; Reno — smaller northern NV depth",
     "best": "only with supply visibility and tourism-cycle stress tests",
     "risks": "gaming/tourism concentration; concessions; water/long-term growth debates"},
    {"abbr": "AZ", "name": "Arizona", "metros": "Phoenix (incl. Tempe, Mesa, Chandler), Tucson",
     "jobs": 5, "price": 4, "cash": 4, "appr": 4, "owner": 9, "tenant": 2, "conf": "High",
     "shock_mo": 9, "door_screen": "Phoenix $/door still elevated vs Midwest value-add",
     "deal_illust": "$9.0M (illustrative 50-door Phoenix)", "cash_close": "$3.0M", "shock": "$320k", "total_liq": "$3.3M",
     "rent_screen": "asking soft in heavy-delivery East/West Valley pockets",
     "occ": "rebalancing; submarket picks matter", "conc": "still a primary underwriting risk on Class A",
     "cap": "wider than peak; not automatic bargains",
     "submarkets": "West Valley — yield/concession watch; East Valley — tenant quality / schools; Tucson — secondary relative value",
     "best": "selective Class B with clear lease-up endgame; avoid blind new Class A",
     "risks": "concessions; heat/insurance; jobs softer than prior boom"},
    {"abbr": "ID", "name": "Idaho", "metros": "Boise, Idaho Falls, Coeur d’Alene",
     "jobs": 8, "price": 3, "cash": 3, "appr": 6, "owner": 10, "tenant": 1, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Boise expensive/door for secondary scale",
     "deal_illust": "$7.0M (illustrative 40–50 doors Boise)", "cash_close": "$2.3M", "shock": "$240k", "total_liq": "$2.6M",
     "rent_screen": "high rents vs Midwest; yields thinner",
     "occ": "tight-ish historically; watch new supply", "conc": "emerging with deliveries",
     "cap": "tighter than Midwest",
     "submarkets": "Boise — suburban gardens; Coeur d’Alene — resort-adjacent premium",
     "best": "growth hold for sponsors OK with thinner cash flow",
     "risks": "high basis; thinner liquidity; wildfire/insurance pockets"},
    {"abbr": "UT", "name": "Utah", "metros": "Salt Lake City, Provo, Ogden",
     "jobs": 9, "price": 3, "cash": 3, "appr": 4, "owner": 10, "tenant": 1, "conf": "High",
     "shock_mo": 6, "door_screen": "Wasatch Front expensive vs cash-flow screens",
     "deal_illust": "$9.0M (illustrative 50-door SLC)", "cash_close": "$3.0M", "shock": "$280k", "total_liq": "$3.3M",
     "rent_screen": "strong demand rents; entry basis high",
     "occ": "generally solid demand", "conc": "watch new Class A",
     "cap": "tighter growth-market caps",
     "submarkets": "SLC — west/south Class B; Provo — tech/university demand; Ogden — relative value",
     "best": "growth / jobs thesis more than cash-flow thesis",
     "risks": "expensive entry; supply in hot corridors"},
    {"abbr": "MT", "name": "Montana", "metros": "Billings, Missoula, Bozeman",
     "jobs": 8, "price": 3, "cash": 3, "appr": 4, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Bozeman very expensive; Billings more approachable",
     "deal_illust": "$5.0M (smaller community)", "cash_close": "$1.7M", "shock": "$200k", "total_liq": "$1.9M",
     "rent_screen": "lifestyle markets high rent / high basis",
     "occ": "tight in lifestyle markets", "conc": "varies",
     "cap": "few prints; lifestyle premiums",
     "submarkets": "Billings — workforce; Missoula / Bozeman — lifestyle / constrained",
     "best": "Billings for more conventional screens; lifestyle metros specialist",
     "risks": "thin inventory; expensive Bozeman; wildfire"},
    {"abbr": "DE", "name": "Delaware", "metros": "Wilmington, Dover",
     "jobs": 5, "price": 5, "cash": 5, "appr": 5, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Wilmington / Philly spillover pricing",
     "deal_illust": "$6.0M (illustrative)", "cash_close": "$2.0M", "shock": "$220k", "total_liq": "$2.2M",
     "rent_screen": "mid-Atlantic Class B",
     "occ": "stable small-state", "conc": "moderate",
     "cap": "limited prints",
     "submarkets": "Wilmington — Philly spillover; Dover — smaller capital market",
     "best": "Wilmington Class B for regional sponsors",
     "risks": "thin statewide scale"},
    {"abbr": "CT", "name": "Connecticut", "metros": "Hartford, Bridgeport, New Haven",
     "jobs": 4, "price": 4, "cash": 5, "appr": 8, "owner": 5, "tenant": 7, "conf": "High",
     "shock_mo": 9, "door_screen": "higher Northeast basis; Hartford relatively better yield",
     "deal_illust": "$7.5M (illustrative)", "cash_close": "$2.5M", "shock": "$300k", "total_liq": "$2.8M",
     "rent_screen": "Hartford better yield screens than coastal NY peers",
     "occ": "mixed by metro", "conc": "competitive pockets",
     "cap": "Northeast mid",
     "submarkets": "Hartford — insurance employment Class B; New Haven — university overlay; Fairfield — expensive NY spillover",
     "best": "Hartford income/value vs coastal trophy",
     "risks": "tenant-leaning climate; taxes; soft jobs"},
    {"abbr": "MD", "name": "Maryland", "metros": "Baltimore, Montgomery / Prince George’s",
     "jobs": 5, "price": 4, "cash": 5, "appr": 4, "owner": 5, "tenant": 7, "conf": "High",
     "shock_mo": 9, "door_screen": "Baltimore cheaper/door; suburbs expensive",
     "deal_illust": "$7.0M (illustrative Baltimore Class B)", "cash_close": "$2.3M", "shock": "$280k", "total_liq": "$2.6M",
     "rent_screen": "Baltimore high printed gross possible; ops heavy",
     "occ": "class dependent", "conc": "varies",
     "cap": "Baltimore Class C wide with ops haircut",
     "submarkets": "Baltimore — carefully screened Class B/C; MoCo / PG — D.C. spillover regulation/price",
     "best": "Baltimore with strong management; suburbs for larger sponsors",
     "risks": "local stabilization / tenant rules; taxes; D.C. metro job spillover risk"},
    {"abbr": "WY", "name": "Wyoming", "metros": "Cheyenne, Casper",
     "jobs": 8, "price": 4, "cash": 5, "appr": 3, "owner": 9, "tenant": 2, "conf": "Medium",
     "shock_mo": 6, "door_screen": "very thin apartment inventory",
     "deal_illust": "$2.8M (small community)", "cash_close": "$1.0M", "shock": "$150k", "total_liq": "$1.1M",
     "rent_screen": "small-market rents; energy towns volatile",
     "occ": "thin data", "conc": "usually light",
     "cap": "scarce prints",
     "submarkets": "Cheyenne — primary small depth; Casper — energy cycle",
     "best": "local sponsors only",
     "risks": "scale; energy; exits"},
    {"abbr": "AK", "name": "Alaska", "metros": "Anchorage, Fairbanks",
     "jobs": 6, "price": 4, "cash": 4, "appr": 8, "owner": 8, "tenant": 3, "conf": "Medium",
     "shock_mo": 9, "door_screen": "Anchorage primary; high OpEx climate",
     "deal_illust": "$5.5M (illustrative)", "cash_close": "$1.8M", "shock": "$250k", "total_liq": "$2.1M",
     "rent_screen": "high rents offset by high costs",
     "occ": "small-market", "conc": "varies",
     "cap": "few prints",
     "submarkets": "Anchorage — primary; Fairbanks — interior/military/university mix",
     "best": "local/regional specialists",
     "risks": "climate OpEx; thin exits; logistics"},
    {"abbr": "ME", "name": "Maine", "metros": "Portland, Bangor",
     "jobs": 8, "price": 4, "cash": 3, "appr": 6, "owner": 5, "tenant": 7, "conf": "Medium",
     "shock_mo": 9, "door_screen": "Portland constrained / expensive",
     "deal_illust": "$6.0M (illustrative Portland-area)", "cash_close": "$2.0M", "shock": "$260k", "total_liq": "$2.3M",
     "rent_screen": "Portland high; Bangor thinner",
     "occ": "tight supply narrative in Portland", "conc": "less Sun-Belt-style",
     "cap": "lifestyle / constrained premiums",
     "submarkets": "Portland — local rent stabilization awareness; Bangor — smaller",
     "best": "Portland for long-hold constrained-supply thesis",
     "risks": "tenant rules; thin scale; high basis"},
    {"abbr": "VT", "name": "Vermont", "metros": "Burlington",
     "jobs": 8, "price": 4, "cash": 3, "appr": 7, "owner": 4, "tenant": 8, "conf": "Medium",
     "shock_mo": 9, "door_screen": "Burlington thin / expensive",
     "deal_illust": "$5.0M (small community)", "cash_close": "$1.7M", "shock": "$240k", "total_liq": "$1.9M",
     "rent_screen": "high relative rents; regulation risk",
     "occ": "tight small market", "conc": "limited",
     "cap": "scarce",
     "submarkets": "Burlington metro — primary statewide apartment depth",
     "best": "specialist / values-aligned long hold",
     "risks": "tenant protections; tiny inventory; exits"},
    {"abbr": "NH", "name": "New Hampshire", "metros": "Manchester–Nashua",
     "jobs": 8, "price": 3, "cash": 3, "appr": 7, "owner": 5, "tenant": 7, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Boston spillover pricing",
     "deal_illust": "$7.5M (illustrative)", "cash_close": "$2.5M", "shock": "$260k", "total_liq": "$2.8M",
     "rent_screen": "high rents / high basis",
     "occ": "generally solid labor markets", "conc": "moderate",
     "cap": "Northeast tighter",
     "submarkets": "Manchester–Nashua — Boston spillover workforce / professional",
     "best": "growth spillover more than deep cash flow",
     "risks": "expensive entry; tenant-leaning Northeast norms"},
    {"abbr": "CO", "name": "Colorado", "metros": "Denver, Colorado Springs, Fort Collins",
     "jobs": 7, "price": 3, "cash": 3, "appr": 2, "owner": 7, "tenant": 5, "conf": "High",
     "shock_mo": 9, "door_screen": "Denver still expensive after correction",
     "deal_illust": "$10.0M (illustrative 50-door Denver)", "cash_close": "$3.3M", "shock": "$350k", "total_liq": "$3.7M",
     "rent_screen": "economic rents after concessions critical",
     "occ": "supply hangover in places", "conc": "still a key risk on newer product",
     "cap": "expanded vs peak; not automatic deep value",
     "submarkets": "Denver — suburban gardens vs urban core; Springs — relative value; Fort Collins — university/lifestyle",
     "best": "selective basis with supply endgame; Springs relative value",
     "risks": "concessions; price correction; regulation pockets"},
    {"abbr": "RI", "name": "Rhode Island", "metros": "Providence",
     "jobs": 6, "price": 3, "cash": 3, "appr": 3, "owner": 7, "tenant": 4, "conf": "Medium",
     "shock_mo": 6, "door_screen": "Providence mid-Atlantic / New England basis",
     "deal_illust": "$6.5M (illustrative)", "cash_close": "$2.2M", "shock": "$230k", "total_liq": "$2.4M",
     "rent_screen": "Providence Class B",
     "occ": "small-state", "conc": "moderate",
     "cap": "limited prints",
     "submarkets": "Providence metro — primary statewide depth",
     "best": "regional sponsors; Boston spillover selective",
     "risks": "thin scale; Northeast costs"},
    {"abbr": "NY", "name": "New York", "metros": "New York City, Buffalo, Rochester, Syracuse",
     "jobs": 5, "price": 3, "cash": 4, "appr": 8, "owner": 1, "tenant": 10, "conf": "High",
     "shock_mo": 12, "door_screen": "NYC specialist; Upstate far cheaper/door",
     "deal_illust": "Upstate $4.5M screen; NYC institutional (separate)", "cash_close": "Upstate about $1.5M", "shock": "$280k", "total_liq": "Upstate about $1.8M",
     "rent_screen": "Upstate workable; NYC rent-regulated complexity",
     "occ": "Upstate stable; NYC class/regulation dependent", "conc": "competitive in soft pockets",
     "cap": "Upstate wider; NYC unique",
     "submarkets": "Buffalo / Rochester / Syracuse — Good Cause opt-in awareness; NYC — rent stabilization / specialist counsel required",
     "best": "Upstate Class B for non-specialists; NYC only with counsel and rent-roll expertise",
     "risks": "statewide tenant tilt; NYC regulation; taxes"},
    {"abbr": "NJ", "name": "New Jersey", "metros": "Newark, Camden, New Brunswick, Jersey City",
     "jobs": 6, "price": 3, "cash": 2, "appr": 8, "owner": 3, "tenant": 9, "conf": "High",
     "shock_mo": 12, "door_screen": "high basis; local rent ordinances common",
     "deal_illust": "$10.0M (illustrative)", "cash_close": "$3.3M", "shock": "$400k", "total_liq": "$3.7M",
     "rent_screen": "high rents offset by tax / regulation",
     "occ": "generally deep demand near NY", "conc": "varies",
     "cap": "compressed for quality; local rules dominate",
     "submarkets": "North Jersey — NY spillover; South Jersey — Philly spillover; always check local rent ordinances",
     "best": "experienced Northeast multifamily operators only",
     "risks": "rent ordinances; property taxes; Anti-Eviction Act ops"},
    {"abbr": "MA", "name": "Massachusetts", "metros": "Boston, Worcester, Springfield",
     "jobs": 6, "price": 2, "cash": 2, "appr": 6, "owner": 6, "tenant": 6, "conf": "High",
     "shock_mo": 9, "door_screen": "Boston trophy expensive; Worcester / Springfield relative",
     "deal_illust": "$12.0M (illustrative Boston-area)", "cash_close": "$4.0M", "shock": "$420k", "total_liq": "$4.4M",
     "rent_screen": "high rents / thin cash flow after basis",
     "occ": "generally strong demand in Boston", "conc": "competitive Class A",
     "cap": "tight in Boston",
     "submarkets": "Boston — urban Class A/B specialist; Worcester / Springfield — relative value Inland",
     "best": "institutional Boston; Inland for better entry screens",
     "risks": "extreme basis; regulation; taxes"},
    {"abbr": "HI", "name": "Hawaii", "metros": "Honolulu",
     "jobs": 8, "price": 1, "cash": 2, "appr": 6, "owner": 7, "tenant": 4, "conf": "Medium",
     "shock_mo": 9, "door_screen": "very expensive; thin conventional screens",
     "deal_illust": "specialty — $/door often extreme", "cash_close": "`unavailable` without live print", "shock": "high", "total_liq": "`unavailable`",
     "rent_screen": "high rents; tourism and shipping cost overlays",
     "occ": "island constrained", "conc": "varies",
     "cap": "specialty market",
     "submarkets": "Honolulu — primary statewide depth",
     "best": "local specialists only",
     "risks": "basis; insurance; tourism; logistics"},
    {"abbr": "OR", "name": "Oregon", "metros": "Portland, Salem, Eugene",
     "jobs": 3, "price": 3, "cash": 3, "appr": 4, "owner": 3, "tenant": 9, "conf": "High",
     "shock_mo": 12, "door_screen": "Portland expensive with rent-cap overlay",
     "deal_illust": "$8.5M (illustrative Portland)", "cash_close": "$2.8M", "shock": "$350k", "total_liq": "$3.2M",
     "rent_screen": "rent growth capped statewide (2026 cap about 9.5% — verify current)",
     "occ": "soft jobs weighing demand", "conc": "competitive",
     "cap": "not a cash-flow leader",
     "submarkets": "Portland — regulation-aware Class B; Salem / Eugene — smaller",
     "best": "long-hold constrained-supply specialists only",
     "risks": "rent cap; just cause; weak near-term jobs"},
    {"abbr": "WA", "name": "Washington", "metros": "Seattle, Tacoma, Spokane",
     "jobs": 4, "price": 2, "cash": 3, "appr": 3, "owner": 3, "tenant": 9, "conf": "High",
     "shock_mo": 12, "door_screen": "Seattle very expensive; Spokane relative",
     "deal_illust": "$11.0M (illustrative Seattle-area)", "cash_close": "$3.7M", "shock": "$400k", "total_liq": "$4.1M",
     "rent_screen": "high rents; statewide rent cap (verify current %)",
     "occ": "concessions in soft tech-tied pockets", "conc": "still material Seattle Class A",
     "cap": "tight for quality Seattle",
     "submarkets": "Seattle — specialist; Tacoma — relative; Spokane — Inland value",
     "best": "Spokane / Tacoma relative value; Seattle institutional only",
     "risks": "rent cap; concessions; soft prices/jobs in Seattle"},
    {"abbr": "CA", "name": "California", "metros": "Los Angeles, Bay Area, San Diego, Sacramento, Inland Empire",
     "jobs": 4, "price": 1, "cash": 2, "appr": 3, "owner": 3, "tenant": 9, "conf": "High",
     "shock_mo": 12, "door_screen": "coastal trophy extreme; Inland relatively better",
     "deal_illust": "Inland $9M+ screens; coastal institutional", "cash_close": "often $3M+ on mid-size", "shock": "$450k+", "total_liq": "high — live quote required",
     "rent_screen": "statewide rent cap (5%+CPI max 10%) + local overlays",
     "occ": "class/metro dependent", "conc": "common in soft coastal pockets",
     "cap": "compressed coastal; Inland wider but still regulated",
     "submarkets": "Inland Empire / Sacramento — relative entry; LA / Bay / SD — specialist rent-control underwriting",
     "best": "Inland / Sacramento for non-specialists; coastal only with counsel",
     "risks": "rent control; local overlays; taxes; insurance (wildfire)"},
    {"abbr": "DC", "name": "District of Columbia", "metros": "Washington, D.C.",
     "jobs": 2, "price": 2, "cash": 2, "appr": 2, "owner": 1, "tenant": 10, "conf": "High",
     "shock_mo": 12, "door_screen": "expensive; TOPA / rent stabilization critical",
     "deal_illust": "institutional / specialist", "cash_close": "high", "shock": "high", "total_liq": "`unavailable` without live deal",
     "rent_screen": "regulated rent rolls require specialist underwriting",
     "occ": "demand exists; jobs soft YoY", "conc": "competitive",
     "cap": "specialty",
     "submarkets": "D.C. proper — TOPA / rent stab; nearby MD/VA suburbs are separate state rows",
     "best": "specialist operators with counsel only",
     "risks": "TOPA; rent stabilization; job losses; high basis"},
]


def econ(s: dict) -> float:
    return round((s["jobs"] + s["price"] + s["cash"] + s["appr"]) / 4, 2)


def load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def demo_line(name: str, demo: dict, income: dict) -> str:
    d = demo["states"].get(name, {})
    med = income.get("median_household_income", {}).get(name)
    mean = income.get("mean_household_income", {}).get(name)
    med_s = f"${med // 1000}k" if isinstance(med, (int, float)) else "`unavailable`"
    mean_s = f"${mean // 1000}k" if isinstance(mean, (int, float)) else "`unavailable`"
    if not d:
        return f"Demographics `unavailable`. Median HH income {med_s}; mean HH income {mean_s}."
    return (
        f"White alone {d.get('white_alone_pct', '?')}% · Black {d.get('black_alone_pct', '?')}% · "
        f"Hisp {d.get('hispanic_any_race_pct', '?')}% · Asian {d.get('asian_alone_pct', '?')}%. "
        f"State median HH income **{med_s}** (CPS/FRED); mean HH income {mean_s} (ACS)."
    )


def industries_line(name: str, ind: dict) -> tuple[str, str]:
    st = ind["states"].get(name, {})
    top = st.get("top") or []
    labels = [t["label"].lower() for t in top[:4]]
    joined = "; ".join(labels) if labels else "`unavailable`"
    note = st.get("concentration_note") or "See BLS CES mix for renter-demand context."
    return joined, note


def ue_line(name: str, jobs: dict) -> str:
    st = jobs["states"].get(name, {})
    rate = st.get("unemployment_rate")
    as_of = st.get("as_of", "")
    if rate is None:
        return "Unemployment `unavailable`."
    return f"Unemployment **{rate}%** (BLS LAUS, {as_of})."


def slug(name: str) -> str:
    return name.lower().replace(" ", "-").replace(".", "")


def build() -> str:
    demo = load_json("demographics.json")
    income = load_json("income.json")
    ind = load_json("industries.json")
    jobs = load_json("jobs.json")

    for i, s in enumerate(STATES, 1):
        s["rank"] = i
        s["econ"] = econ(s)

    deep_links = " · ".join(f"[{s['abbr']}](#{slug(s['name'])})" for s in STATES)

    lines: list[str] = []
    a = lines.append

    a("# US Apartment (Multifamily) Market Analysis")
    a("")
    a("**Apartment report** (5+ unit conventional multifamily).  ")
    a("**Format template:** `rental_market_report.md` (same section order / Index / deep-dive fields).  ")
    a("**Spec:** `apartment_market_spec.md`  ")
    a("**Sibling (SFR / 2–4):** [`rental_market_report.md`](rental_market_report.md)  ")
    a("**Analysis date:** July 26, 2026  ")
    a("**Coverage:** All 50 states + Washington, D.C.; major apartment metros / submarkets  ")
    a("**Property types:** Conventional **apartments (5+ units)** — garden, mid-rise, high-rise; Class A / B / C. Not SFR or 2–4 unit primary rankings.  ")
    a("**Live research:** Yes. Shared `data/` for jobs, industries, demographics, income; live web research for national multifamily occupancy, concessions, deliveries, cap rates, and financing. Per-door prices often `unavailable` in public free sources — labeled honestly.")
    a("")
    a("> Informational screening only — not financial, legal, tax, insurance, or investment advice. Confirm laws with local counsel and underwrite an actual rent roll before buying.")
    a("")
    a("---")
    a("")
    a("## Index")
    a("")
    a("Jump to a section (companion tables in §4 share the same state order):")
    a("")
    a("Every section below includes **[↑ Back to Index](#index)** under its heading so you can return here after jumping.")
    a("")
    a("| | |")
    a("|---|---|")
    a("| [2. National snapshot](#2-national-market-snapshot) | [3. Top 10 / lists](#3-top-10-actionable-markets) |")
    a("| [4. All-state matrix](#4-all-state-ranking-matrix) | [5. City leaderboards](#5-city-leaderboards) |")
    a("| [4a Scores](#4a-scores-actionable-order) · [4b Apartment screens](#4b-apartment-screens--major-metros-same-order) | [4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) · [4e Entry capital](#4e-entry-capital--shock-reserves-same-order) |")
    a("| [6. All-state deep dives](#6-all-state-deep-dives) | [7. Legal](#7-legal-environment--verified-2026-highlights) |")
    a("| [8. Insurance & tax](#8-insurance-and-property-tax-overlays) | [9. Property management](#9-property-management-rates--remote-ops) |")
    a("| [10. Acquisition workflow](#10-practical-acquisition-workflow) | [11. Methodology & sources](#11-methodology-and-sources) |")
    a("| [A–Z state rank index](#az-actionable-rank-index) | [What changed (appendix)](#1-what-changed-vs-the-prior-run) |")
    a("")
    a(f"**Deep dives (all states + D.C., actionable order):** {deep_links}")
    a("")
    a("**City boards:** [Cash flow / NOI](#cash-flow--noi-screens) · [Class B/C value-add](#best-for-class-bc-value-add) · [Class A / growth](#best-for-class-a--growth-hold) · [Submarkets](#top-submarkets-worth-researching-live-2026-screen) · [Jobs](#job-market-leaders-context-for-renter-demand)")
    a("")
    a("---")
    a("")
    a("## 2. National market snapshot")
    a("[↑ Back to Index](#index)")
    a("")
    a("- **Multifamily rebalancing (mid-2026):** Demand has begun to outpace new supply on a trailing basis in major brokerage reads; national vacancy drifted lower in Q2 2026 while deliveries fell sharply from 2024 peaks ([Cushman & Wakefield Q2 2026 Multifamily MarketBeat](https://www.cushmanwakefield.com/en/united-states/news/2026/07/us-multifamily-marketbeat)).")
    a("- **Occupancy:** National occupancy remained resilient near about **95%** in early-2026 capital-markets reads, with wide metro dispersion ([Colliers U.S. Multifamily Capital Markets 2026 Q1](https://www.colliers.com/en/research/nrep-uscm-usmf-colliers-capital-markets-multifamily-report-2026-q1)).")
    a("- **Concessions:** Still a primary underwriting risk in oversupplied Sun Belt Class A corridors (months free / fee waivers); Midwest Class B/C generally lighter but not zero.")
    a("- **Cap rates:** Transactional / survey multifamily caps clustered about **5.0%–5.8%** nationally by class and deal size in 2026 lender/brokerage screens — verify live prints ([apartment lender cap-rate compilations](https://apartmentloanstore.com/glossary/cap-rate); Q1 2026 capital-markets notes around mid-5%s).")
    a("- **Pipeline:** Units under construction as a share of inventory fell toward multi-year lows in mid-2026 brokerage summaries — supportive for occupancy into 2027 if starts stay muted.")
    a("- **Jobs / demand context (shared data):** State unemployment (BLS LAUS, June 2026) spans about **2.0%–6.0%**; industries and incomes in §4c–4d.")
    a("- **Financing screen:** Agency / bank multifamily and DSCR-style debt still price off higher-for-longer rates; model **DSCR** and interest-rate stress, not only LTV. Exact coupons are lender- and sponsor-specific — treat public “about 5.5%–7%+” chatter as `verify live`.")
    a("- **PM screen:** Third-party multifamily often about **3–8% of EGI** or flat $/door; this report defaults about **5–6% of EGI** unless quoted — see §9.")
    a("- **Sibling residential context:** Redfin/FHFA house prices in the SFR report are **not** apartment comps; cited only as broad housing-cost context for renter vs owner affordability.")
    a("")
    a("### Yield definition used here")
    a("[↑ Back to Index](#index)")
    a("")
    a("- Prefer **cap rate** = NOI ÷ price (label trailing vs forward).")
    a("- **Gross yield** = annual rent ÷ price is a crude screen only.")
    a("- Prefer **economic occupancy** and **in-place rent after concessions**; label **asking** when that is all you have.")
    a("- Cash-flow scores haircut vacancy, concessions, tax, insurance, turnover, and PM about **5–6% of EGI**.")
    a("")
    a("### Core conclusion")
    a("[↑ Back to Index](#index)")
    a("")
    a("Best risk-adjusted **apartment** screens in this cut still favor **Midwest metros with deep 5+ unit inventory, workable landlord law, and lighter concession regimes** (Ohio, Indiana, Missouri, Alabama, Tennessee income product), plus selected Southeast markets where **supply visibility** is clear. Sun Belt scale (Texas, Georgia, Carolinas, Arizona, Florida) remains important for liquidity — but **near-term Cash scores** are haircut for concessions, insurance, and delivery hangover. Coastal and heavily regulated markets (California, Oregon, Washington, New York City, D.C., much of New Jersey) stay **specialist-only** for conventional apartment cash-flow buyers.")
    a("")
    a("**Class A vs Class B/C:**")
    a("")
    a("- **Class B/C (especially Midwest garden)** usually wins this screen on going-in yield and lower amenity competition — if you can staff ops and underwrite collections.")
    a("- **Class A** can win on liquidity, newer systems, and long-term rent growth **after** lease-up and concession burn-off — do not buy the offering-memorandum asking rent.")
    a("")
    a("---")
    a("")
    a("## 3. Top 10 actionable markets")
    a("[↑ Back to Index](#index)")
    a("")
    a("Tie-breakers: apartment inventory depth, professional management availability, insurance catastrophe risk, supply/concession clarity, diversified jobs.")
    a("")
    a("| Rank | State / preferred metros | Why it ranks | Class A vs B/C | Main caution |")
    a("| ---- | ------------------------ | ------------ | -------------- | ------------ |")
    for s in STATES[:10]:
        a(f"| {s['rank']} | **{s['name']} — {s['metros']}** | Econ {s['econ']}; Owner {s['owner']}; {s['best'].split(';')[0]} | See deep dive | {s['risks'].split(';')[0]} |")
    a("")
    a("### Best landlord-protection markets (law + apartment economics)")
    a("[↑ Back to Index](#index)")
    a("")
    a("| Rank | Market | Why |")
    a("| ---- | ------ | --- |")
    a("| 1 | Ohio — Cleveland / Columbus / Cincinnati | Owner-friendly baseline + deep apartment stock + income |")
    a("| 2 | Indiana — Indianapolis | Rent-control preemption + scalable Indy inventory |")
    a("| 3 | Alabama — Birmingham | Favorable law + low taxes + Class B/C yields |")
    a("| 4 | Missouri — Kansas City / St. Louis | Workable law + two apartment metros |")
    a("| 5 | Tennessee — Memphis (Nashville selective) | Favorable law; Memphis income if ops are strong |")
    a("| 6 | Georgia — Atlanta | Strong owner law + scale (supply/concession watch) |")
    a("| 7 | Wisconsin — Milwaukee | Owner-friendly + income product |")
    a("| 8 | Texas — DFW / Houston / San Antonio | Strong owner law + huge liquidity (Cash haircut for concessions) |")
    a("| 9 | South Carolina — Greenville / Columbia | Owner-friendly inland Class B |")
    a("| 10 | Oklahoma — OKC / Tulsa | Very favorable law + low entry; insurance/jobs limit rank |")
    a("")
    a("### Best tenant-protection markets that still have an investment case")
    a("[↑ Back to Index](#index)")
    a("")
    a("These are **not** easiest for landlords. Apartment portfolios feel rent caps / just cause / TOPA more than scattered SFR.")
    a("")
    a("| Rank | Market | Protection reality | Investment case |")
    a("| ---- | ------ | ------------------ | --------------- |")
    a("| 1 | Upstate New York — Buffalo / Rochester / Syracuse | Good Cause in opt-in cities; statewide tenant tilt | Cheaper doors than NYC; appreciation pockets |")
    a("| 2 | Chicago, Illinois | City ordinance / Fair Notice; IL preempts rent control | Deep institutional market; strong recent house-price context |")
    a("| 3 | Baltimore, Maryland | Local protections / stabilization in places | High printed income potential with heavy ops |")
    a("| 4 | Hartford, Connecticut | Tenant-leaning statewide climate | Better yield screens than coastal NY peers |")
    a("| 5 | Minneapolis–St. Paul, Minnesota | Local tenant rules matter | Diversified corporate demand |")
    a("| 6 | Portland, Maine | Local rent stabilization | Constrained supply / tight labor |")
    a("| 7 | Selected New Jersey secondary metros | Anti-Eviction Act + local rent ordinances | NY spillover demand; taxes severe |")
    a("| 8 | Portland, Oregon | Statewide rent cap; just cause | Long-term supply constraints; weak near-term jobs |")
    a("| 9 | Seattle, Washington | Statewide rent cap; just cause | High-income base; soft near-term apartment math |")
    a("| 10 | Inland California metros | Statewide + local overlays | Better entry than coast; still regulation-heavy |")
    a("")
    a("New York City, San Francisco, Los Angeles, and Washington, D.C. remain specialist-only for apartments.")
    a("")
    a("### Markets to avoid / watch")
    a("[↑ Back to Index](#index)")
    a("")
    a("| Market | Issue |")
    a("| ------ | ----- |")
    a("| **Washington, D.C.** | Soft jobs; TOPA; rent stabilization; expensive entry |")
    a("| **Portland, Oregon** | Job losses; statewide rent cap |")
    a("| **Coastal California Class A trophy** | Basis + rent control + insurance |")
    a("| **Seattle Class A lease-up** | Concessions + rent cap + soft prices |")
    a("| **Austin / heavy-delivery Sun Belt Class A** | Concession wars; basis risk |")
    a("| **Florida coastal** | Insurance can erase NOI |")
    a("| **Detroit / Jackson “too good to be true” Class C** | Collections, capex, and exits often dominate |")
    a("")
    a("---")
    a("")
    a("## 4. All-state ranking matrix")
    a("[↑ Back to Index](#index)")
    a("")
    a("Companion tables share the same `#` actionable order. **Price** = apartment entry affordability (higher = easier), not an SFR median. **Cash** = NOI realism after concessions/tax/insurance/PM.")
    a("")
    a("### 4a. Scores (actionable order)")
    a("[↑ Back to Index](#index)")
    a("")
    a("`#` = actionable rank after tie-breakers. Primary apartment metros shown next to each state.")
    a("")
    a("| # | State (primary metros) | Jobs | Price | Cash | Appr. | Econ | Owner | Tenant | Conf. |")
    a("| --- | ---------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ------ | ----- |")
    for s in STATES:
        a(
            f"| {s['rank']} | {s['name']} — {s['metros']} | {s['jobs']} | {s['price']} | {s['cash']} | {s['appr']} | "
            f"{s['econ']:.2f} | {s['owner']} | {s['tenant']} | {s['conf']} |"
        )
    a("")
    a("### 4b. Apartment screens & major metros (same order)")
    a("[↑ Back to Index](#index)")
    a("")
    a("**Rent / occ / concessions / cap** columns are directional screening notes from mid-2026 national research + state judgment — replace with CoStar/RealPage/broker OM before bidding. **$/door** often `unavailable` in free public sources.")
    a("")
    a("| # | State | $/door screen | Rent / occ / concessions | Cap-rate note | Major apartment metros |")
    a("|---:|---|---|---|---|---|")
    for s in STATES:
        a(
            f"| {s['rank']} | {s['name']} | {s['door_screen']} | {s['rent_screen']}; occ: {s['occ']}; conc: {s['conc']} | {s['cap']} | {s['metros']} |"
        )
    a("")
    a("### 4c. Top job industries (same order)")
    a("[↑ Back to Index](#index)")
    a("")
    a(f"**Source:** live `data/industries.json` ({ind.get('source', 'BLS CES SAE')}; pulled_at={ind.get('pulled_at', 'n/a')}). Demand context for renter employment — not an apartment rent print.")
    a("")
    a("| # | State | Top industries (largest →) | Concentration / renter note |")
    a("|---:|---|---|---|")
    for s in STATES:
        joined, note = industries_line(s["name"], ind)
        a(f"| {s['rank']} | {s['name']} | {joined} | {note} |")
    a("")
    a("### 4d. Demographics & income (same order)")
    a("[↑ Back to Index](#index)")
    a("")
    a("Demand-context only — **never** an exclusion ranking criterion. Race alone + Hispanic any race from shared ACS/Census extract; incomes from CPS/FRED median + ACS mean when present.")
    a("")
    a("| # | State | Race / ethnicity (alone + Hisp) | Median HH | Mean HH |")
    a("|---:|---|---|---:|---:|")
    for s in STATES:
        d = demo["states"].get(s["name"], {})
        med = income.get("median_household_income", {}).get(s["name"])
        mean = income.get("mean_household_income", {}).get(s["name"])
        med_s = f"${int(med)//1000}k" if isinstance(med, (int, float)) else "`unavailable`"
        mean_s = f"${int(mean)//1000}k" if isinstance(mean, (int, float)) else "`unavailable`"
        race = (
            f"White {d.get('white_alone_pct', '?')}% · Black {d.get('black_alone_pct', '?')}% · "
            f"Hisp {d.get('hispanic_any_race_pct', '?')}% · Asian {d.get('asian_alone_pct', '?')}%"
            if d else "`unavailable`"
        )
        a(f"| {s['rank']} | {s['name']} | {race} | {med_s} | {mean_s} |")
    a("")
    a("### 4e. Entry capital & shock reserves (same order)")
    a("[↑ Back to Index](#index)")
    a("")
    a("**Screen framing (not a lender quote):** Default **30% down** (midpoint of 25–35%) + about **3%** closing/acquisition costs on an **illustrative mid-size garden community**. Shock liquid = **6–12 months** of debt-service / operating screen (higher in insurance, concession, or heavy-regulation states). Replace with live $/door and rent roll. When cash figures are labeled illustrative, they are order-of-magnitude only.")
    a("")
    a("| # | State | Down | Illustrative deal | Cash to close | Shock liquid | Total liquid |")
    a("|---:|---|---:|---|---:|---:|---:|")
    for s in STATES:
        a(
            f"| {s['rank']} | {s['name']} | 30% | {s['deal_illust']} | {s['cash_close']} | {s['shock']} ({s['shock_mo']} mo) | {s['total_liq']} |"
        )
    a("")
    a("---")
    a("")
    a("## 5. City leaderboards")
    a("[↑ Back to Index](#index)")
    a("")
    a("Apartment-metro screens (not SFR city boards). Order is directional for this report’s Cash / law / depth blend.")
    a("")
    a("### Cash flow / NOI screens")
    a("[↑ Back to Index](#index)")
    a("")
    a("1. Cleveland — Class B/C garden income depth  ")
    a("2. Indianapolis — workforce Class B scale  ")
    a("3. Birmingham — yield + low tax  ")
    a("4. Memphis — high income if ops are strong  ")
    a("5. Kansas City — balanced Class B  ")
    a("6. St. Louis — income with neighborhood underwriting  ")
    a("7. Pittsburgh — older Class B/C stock  ")
    a("8. Cincinnati — I-71 corridor balance  ")
    a("9. Louisville — affordable Class B  ")
    a("10. Milwaukee — income + owner-friendly baseline  ")
    a("11. Oklahoma City — low entry / law (insurance watch)  ")
    a("12. Columbus — growth sibling to Cleveland income  ")
    a("")
    a("### Best for Class B/C value-add")
    a("[↑ Back to Index](#index)")
    a("")
    a("1. Cleveland / Akron corridors  ")
    a("2. Indianapolis east/south workforce  ")
    a("3. Birmingham  ")
    a("4. Memphis (ops-intensive)  ")
    a("5. Detroit carefully screened Class B (not blind Class C)  ")
    a("6. St. Louis screened inner-ring  ")
    a("7. Pittsburgh  ")
    a("8. Baltimore (regulation/ops awareness)  ")
    a("9. Kansas City eastern Jackson County  ")
    a("10. San Antonio / selected DFW workforce (concession-aware)  ")
    a("")
    a("### Best for Class A / growth hold")
    a("[↑ Back to Index](#index)")
    a("")
    a("1. Columbus  ")
    a("2. Nashville (only with lease-up discipline)  ")
    a("3. Atlanta (supply visibility required)  ")
    a("4. Charlotte / Raleigh (same)  ")
    a("5. Dallas–Fort Worth selective submarkets  ")
    a("6. Greenville, SC  ")
    a("7. Huntsville  ")
    a("8. Salt Lake City (jobs > cash flow)  ")
    a("9. Richmond  ")
    a("10. Tampa inland-leaning (insurance-aware)  ")
    a("")
    a("### Top submarkets worth researching (live 2026 screen)")
    a("[↑ Back to Index](#index)")
    a("")
    a("| Metro | Submarkets to open first | Angle |")
    a("| ----- | ------------------------- | ----- |")
    a("| Cleveland | Near-east / west-side Class B/C; selected first-ring | Value-add income |")
    a("| Indianapolis | East/south workforce; north suburban Class A/B | CF vs growth |")
    a("| Kansas City | Independence / eastern Jackson; JoCo KS | CF vs tenant quality |")
    a("| Atlanta | South/east Class B; north Class A | CF vs prestige |")
    a("| Dallas–Fort Worth | Eastern/southern workforce gardens | Concession-aware CF |")
    a("| Phoenix | West Valley vs East Valley | Yield vs schools/quality |")
    a("| Nashville | Suburban garden vs urban core | Lease-up risk |")
    a("| Chicago | North/northwest Class B; south/west value-add | Ordinance-aware |")
    a("")
    a("### Job market leaders (context for renter demand)")
    a("[↑ Back to Index](#index)")
    a("")
    a("Use §4c + BLS metro payrolls. Standouts for apartment demand screens in this cut: **Raleigh / Charlotte**, **Atlanta**, **Columbus**, **Nashville**, **Salt Lake**, **Indy**, **DFW / Houston** (scale), with **D.C. metro** and **Portland, OR** as caution flags on jobs.")
    a("")
    a("---")
    a("")
    a("## 6. All-state deep dives")
    a("[↑ Back to Index](#index)")
    a("")
    a("Deep dives for **all 50 states + D.C.** in actionable-rank order. Field labels: Scores, Prices (apartment screens), Entry capital, Top industries, Demographics / income, Top submarkets, Best fit, Risks, Confidence. [↑ Index](#index) · [A–Z](#az-actionable-rank-index)")
    a("")

    for s in STATES:
        joined, _note = industries_line(s["name"], ind)
        a(f"### {s['name']}")
        a("[↑ Back to Index](#index)")
        a("")
        a(
            f"**Scores:** Jobs {s['jobs']} / Price {s['price']} / Cash flow {s['cash']} / Appreciation {s['appr']} / "
            f"Owner law {s['owner']} / Tenant law {s['tenant']}"
        )
        a("")
        a(
            f"**Prices:** $/door screen — {s['door_screen']}. Rent — {s['rent_screen']}. "
            f"Occupancy — {s['occ']}. Concessions — {s['conc']}. Cap-rate note — {s['cap']}. "
            f"(Replace with rent roll / broker print; SFR house medians are not comps.)"
        )
        a(
            f"**Entry capital:** **30% down** screen on illustrative deal **{s['deal_illust']}**. "
            f"Cash to close about **{s['cash_close']}**; shock liquid about **{s['shock']}** ({s['shock_mo']} mo); "
            f"**total recommended liquid about {s['total_liq']}**. Live DSCR / agency quotes required."
        )
        a(f"**Top industries:** {joined} (BLS CES SAE via `data/industries.json`).")
        a(f"**Demographics / income:** {demo_line(s['name'], demo, income)}")
        a(f"**Top submarkets:** {s['submarkets']}")
        a("")
        a(f"{ue_line(s['name'], jobs)} Apartment inventory depth and professional management availability drive Confidence more than SFR screens in thin states.")
        a("")
        a(f"**Best fit:** {s['best']}  ")
        a(f"**Risks:** {s['risks']}  ")
        a(f"**Confidence:** {s['conf']}.")
        a("")

    a("---")
    a("")
    a("## 7. Legal environment — verified 2026 highlights")
    a("[↑ Back to Index](#index)")
    a("")
    a("Apartment portfolios are more exposed to **rent caps, just-cause eviction, registration, and transfer/TOPA** rules than scattered SFR. Highlights below are screening notes — confirm with counsel.")
    a("")
    a("| Topic | Apartment relevance |")
    a("| ----- | ------------------- |")
    a("| **Rent-control preemption states** (many Southern / Midwestern) | Supports remote / scaled apartment ops |")
    a("| **California** statewide cap (5% + inflation, max 10%) + local overlays | Binds renewals on covered units |")
    a("| **Oregon** statewide cap (about **9.5% for 2026** — verify) + just cause | Caps upside; underwrite renewals |")
    a("| **Washington** statewide cap (about **9.683% for 2026** — verify) + just cause | Same |")
    a("| **New York** Good Cause / rent stabilization | NYC and opt-in Upstate cities — specialist rent rolls |")
    a("| **New Jersey** Anti-Eviction Act + local rent ordinances | Local ordinance check is mandatory |")
    a("| **Washington, D.C.** TOPA + rent stabilization | Transfer friction can dominate deals |")
    a("| **Chicago / Cook County** | No statewide rent cap (IL preemption) but heavy ordinance / notice rules |")
    a("| **Minnesota / Maryland / Connecticut / Maine / Vermont** | Local or statewide tenant tilt — underwrite timelines |")
    a("")
    a("Always separate **state baseline** from **city/county** overlays.")
    a("")
    a("---")
    a("")
    a("## 8. Insurance and property tax overlays")
    a("[↑ Back to Index](#index)")
    a("")
    a("- **Effective property-tax rates** still span roughly about **0.27% (Hawaii)** to **2.23% (New Jersey)** in residential compilations — multifamily assessments can differ; pull the parcel card.")
    a("- **Catastrophe insurance** (wind, hail, flood, wildfire) is a first-class NOI line for apartments in Florida, Louisiana, coastal Texas, Oklahoma, Mississippi, coastal Carolinas, and parts of California.")
    a("- Model **insurance at quote**, not a national average, before locking Cash scores on Gulf / coastal deals.")
    a("- Higher-tax Northeast states need larger OpEx haircuts even when rents look strong.")
    a("")
    a("---")
    a("")
    a("## 9. Property management rates & remote ops")
    a("[↑ Back to Index](#index)")
    a("")
    a("Informational landscape for **conventional multifamily apartments** — not an endorsement. Get a written fee schedule for the exact asset class and unit count.")
    a("")
    a("### Typical fee stack (2026 apartment screens)")
    a("[↑ Back to Index](#index)")
    a("")
    a("| Fee | Typical screen | Notes |")
    a("|-----|----------------|-------|")
    a("| **Third-party management** | About **3–8% of EGI** or flat **$/door/mo** | Often lower % than SFR; larger communities negotiate down |")
    a("| **Default used in Cash scores** | About **5–6% of EGI** | Replace with live bid |")
    a("| **On-site payroll** | Manager / leasing / maintenance | Frequently owner-paid above the % fee on larger assets |")
    a("| **Leasing / concessions admin** | Often in-house | Still model turnover + concession burn |")
    a("| **Construction / rehab oversight** | Separate fee or flat | Value-add critical path |")
    a("")
    a("**All-in screen:** first-year load can still reach low-to-mid teens of gross when turnover, marketing, and payroll are included — underwrite the full chart of accounts.")
    a("")
    a("### Notable operators (scale landscape — verify locally)")
    a("[↑ Back to Index](#index)")
    a("")
    a("| Name | Role | Why it matters |")
    a("|------|------|----------------|")
    a("| **Greystar** | Large multifamily manager / operator | Institutional process benchmark |")
    a("| **Avenue5 Residential** | Large third-party multifamily manager | Multi-state third-party scale |")
    a("| **Asset Living / RPM Living / FPI / BH Management** | Large U.S. multifamily managers | Fee and staffing comps |")
    a("| **Regional Class B specialists** | Local/regional operators | Often the realistic path for 50–150 door Midwest deals |")
    a("")
    a("Institutional SFR landlords (Invitation Homes, Progress, AH4R) are **not** the default apartment third-party stack — see the sibling report for SFR context.")
    a("")
    a("---")
    a("")
    a("## 10. Practical acquisition workflow")
    a("[↑ Back to Index](#index)")
    a("")
    a("1. **Market screen** — use this report’s Top 10 / 4a order; open submarkets in §5–6.  ")
    a("2. **Broker / off-market** — multifamily brokers, agency seller lists, distressed refinance opportunities.  ")
    a("3. **Underwrite rent roll** — Trailing-12, concessions, bad debt, renewal premiums vs new leases.  ")
    a("4. **OpEx & insurance quotes** — taxes, insurance, payroll, turnover, capex reserve.  ")
    a("5. **Debt path** — agency, bank, life company, or bridge; stress DSCR and rates.  ")
    a("6. **Diligence** — PCA, environmental, survey, title, rent-control / TOPA counsel where applicable.  ")
    a("7. **Close & stabilize** — marketing plan, concession exit, and reserve policy.  ")
    a("")
    a("For SFR / 2–4 unit workflows, use the sibling report §10.")
    a("")
    a("---")
    a("")
    a("## 11. Methodology and sources")
    a("[↑ Back to Index](#index)")
    a("")
    a("### Scoring method")
    a("[↑ Back to Index](#index)")
    a("")
    a("- Pillars scored 1–10; **Econ** = average of Jobs, Price, Cash, Appreciation.")
    a("- Rankings are **apartment-specific** judgment using shared jobs/demo/income data plus mid-2026 multifamily market research (occupancy, concessions, deliveries, cap-rate bands).")
    a("- **Price** favors easier apartment entry and inventory depth — not Redfin house medians.")
    a("- **Cash** haircuts concessions, insurance, taxes, and PM about **5–6% of EGI**.")
    a("- Owner/Tenant law aligned with the sibling report but **weighted harder** for rent regulation on apartments.")
    a("- Thin apartment states lose rank even when SFR yields look strong in the sibling report.")
    a("")
    a("### Primary sources")
    a("[↑ Back to Index](#index)")
    a("")
    a("- Shared pipeline `data/` — BLS LAUS / CES, Census ACS demographics, FRED/CPS income, BEA (context)")
    a("- [Cushman & Wakefield — U.S. apartment market Q2 2026](https://www.cushmanwakefield.com/en/united-states/news/2026/07/us-multifamily-marketbeat)")
    a("- [Colliers — U.S. Multifamily Capital Markets 2026 Q1](https://www.colliers.com/en/research/nrep-uscm-usmf-colliers-capital-markets-multifamily-report-2026-q1)")
    a("- [Apartment loan / cap-rate compilations (2026)](https://apartmentloanstore.com/glossary/cap-rate)")
    a("- Sibling legal and insurance notes in [`rental_market_report.md`](rental_market_report.md) §§7–8")
    a("- Spec: [`apartment_market_spec.md`](apartment_market_spec.md)")
    a("")
    a("### Caveats / data gaps")
    a("[↑ Back to Index](#index)")
    a("")
    a("- Many **$/door**, metro **cap rates**, and **economic occupancy** prints are not free/public — marked directional or `unavailable` rather than invented.")
    a("- National brokerage vacancy/occupancy definitions differ (e.g. about 5% vacant vs about 95% occupied) — compare like-with-like.")
    a("- Illustrative 4e deal sizes are **screens**, not appraisals.")
    a("- Asking rents ≠ achieved rents; concessions can move NOI hundreds of bps.")
    a("- Demographics are context only.")
    a("")
    a("---")
    a("")
    a("### A–Z actionable-rank index")
    a("[↑ Back to Index](#index)")
    a("")
    a("Actionable rank by postal abbreviation (1 = highest). Every state links to its [§6 deep dive](#6-all-state-deep-dives).")
    a("")
    a("| | | | | |")
    a("|---|---|---|---|---|")
    # build A-Z grid 5 columns
    by_abbr = sorted(STATES, key=lambda x: x["abbr"])
    cells = [f"[{s['abbr']}](#{slug(s['name'])}) {s['rank']}" for s in by_abbr]
    while len(cells) % 5:
        cells.append("")
    for i in range(0, len(cells), 5):
        row = cells[i : i + 5]
        a("| " + " | ".join(row) + " |")
    a("")
    a("---")
    a("")
    a("## 1. What changed vs the prior run")
    a("[↑ Back to Index](#index)")
    a("")
    a("First full apartment report in this workspace (sibling of the SFR / 2–4 base report).")
    a("")
    a("| Change | What it means |")
    a("|--------|----------------|")
    a("| **New apartment scope** | Rankings and deep dives target **5+ unit** conventional apartments only |")
    a("| **Format reuse** | Same Index, §1–11 order, 4a–4e companions, all-state deep dives, A–Z as `rental_market_report.md` |")
    a("| **National MF context** | Mid-2026 rebalancing: occupancy improving as deliveries slow; concessions still matter in Sun Belt Class A; national cap-rate band about mid-5%s (brokerage / lender screens) |")
    a("| **Shared demand data** | Jobs, industries, demographics, income from live `data/` pulls (same parent pipeline) |")
    a("| **Apartment pricing honesty** | Many $/door and metro cap prints marked `unavailable` or directional — not invented from Redfin house medians |")
    a("| **PM defaults** | Multifamily third-party screen about **5–6% of EGI** (not SFR 10%) |")
    a("| **Entry capital** | Illustrative **30% down** on mid-size garden screens + 6–12 mo reserves |")
    a("")
    a("**Defaults used:** balanced strategy; professional multifamily management; 5–10+ year hold; moderate risk; remote OK with third-party or platform ops.")
    a("")
    a("> Changelog appendix — kept at the bottom so the national snapshot comes first.")
    a("")
    a("---")
    a("")
    a("*End of apartment market report. Sibling SFR / 2–4 analysis: [`rental_market_report.md`](rental_market_report.md).*")
    a("")
    return "\n".join(lines)


if __name__ == "__main__":
    text = build()
    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT} ({len(text):,} chars, {text.count(chr(10))+1} lines)")
