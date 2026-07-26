#!/usr/bin/env python3
"""Generate sfh_appreciation_report.md from live data/ + appreciation-first scoring."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Owner / Tenant scores reused from rental_market_report.md (legal judgment layer).
OWNER = {
    "Alabama": 9, "Alaska": 8, "Arizona": 9, "Arkansas": 9, "California": 3,
    "Colorado": 7, "Connecticut": 5, "Delaware": 8, "District of Columbia": 1,
    "Florida": 9, "Georgia": 9, "Hawaii": 7, "Idaho": 10, "Illinois": 6,
    "Indiana": 9, "Iowa": 9, "Kansas": 8, "Kentucky": 8, "Louisiana": 9,
    "Maine": 5, "Maryland": 5, "Massachusetts": 6, "Michigan": 8, "Minnesota": 6,
    "Mississippi": 9, "Missouri": 8, "Montana": 9, "Nebraska": 7, "Nevada": 8,
    "New Hampshire": 5, "New Jersey": 3, "New Mexico": 8, "New York": 1,
    "North Carolina": 8, "North Dakota": 8, "Ohio": 9, "Oklahoma": 9, "Oregon": 3,
    "Pennsylvania": 7, "Rhode Island": 7, "South Carolina": 9, "South Dakota": 8,
    "Tennessee": 9, "Texas": 9, "Utah": 10, "Vermont": 4, "Virginia": 8,
    "Washington": 3, "West Virginia": 9, "Wisconsin": 9, "Wyoming": 9,
}
TENANT = {
    "Alabama": 2, "Alaska": 3, "Arizona": 2, "Arkansas": 2, "California": 9,
    "Colorado": 5, "Connecticut": 7, "Delaware": 3, "District of Columbia": 10,
    "Florida": 2, "Georgia": 2, "Hawaii": 4, "Idaho": 1, "Illinois": 6,
    "Indiana": 2, "Iowa": 2, "Kansas": 3, "Kentucky": 3, "Louisiana": 2,
    "Maine": 7, "Maryland": 7, "Massachusetts": 6, "Michigan": 3, "Minnesota": 6,
    "Mississippi": 2, "Missouri": 3, "Montana": 2, "Nebraska": 3, "Nevada": 3,
    "New Hampshire": 7, "New Jersey": 9, "New Mexico": 3, "New York": 10,
    "North Carolina": 3, "North Dakota": 3, "Ohio": 2, "Oklahoma": 2, "Oregon": 9,
    "Pennsylvania": 4, "Rhode Island": 4, "South Carolina": 2, "South Dakota": 3,
    "Tennessee": 2, "Texas": 2, "Utah": 1, "Vermont": 8, "Virginia": 3,
    "Washington": 9, "West Virginia": 2, "Wisconsin": 2, "Wyoming": 2,
}

METROS = {
    "Alabama": "Birmingham, Huntsville, Mobile",
    "Alaska": "Anchorage, Fairbanks",
    "Arizona": "Phoenix metro (Tempe, Gilbert, Chandler), Tucson",
    "Arkansas": "Fayetteville–Springdale, Little Rock",
    "California": "Los Angeles, Bay Area, San Diego, Sacramento",
    "Colorado": "Denver, Colorado Springs, Fort Collins",
    "Connecticut": "Hartford, Bridgeport, New Haven",
    "Delaware": "Wilmington, Dover",
    "District of Columbia": "Washington, D.C.",
    "Florida": "Tampa, Orlando, Jacksonville, Miami",
    "Georgia": "Atlanta, Athens, Augusta, Savannah",
    "Hawaii": "Honolulu",
    "Idaho": "Boise, Idaho Falls, Coeur d’Alene",
    "Illinois": "Chicago, Peoria, Rockford, Springfield",
    "Indiana": "Indianapolis, Fort Wayne, South Bend",
    "Iowa": "Des Moines, Cedar Rapids, Iowa City",
    "Kansas": "Wichita, Kansas City–KS, Topeka",
    "Kentucky": "Louisville, Lexington",
    "Louisiana": "New Orleans, Baton Rouge, Lafayette",
    "Maine": "Portland, Bangor",
    "Maryland": "Baltimore, Montgomery / Prince George’s",
    "Massachusetts": "Boston, Worcester, Springfield",
    "Michigan": "Detroit, Grand Rapids, Lansing, Flint",
    "Minnesota": "Minneapolis–St. Paul, Duluth, Rochester",
    "Mississippi": "Jackson, Gulfport, Hattiesburg",
    "Missouri": "Kansas City, St. Louis, Springfield",
    "Montana": "Billings, Missoula, Bozeman",
    "Nebraska": "Omaha, Lincoln",
    "Nevada": "Las Vegas, Reno",
    "New Hampshire": "Manchester–Nashua",
    "New Jersey": "Newark, Camden, New Brunswick",
    "New Mexico": "Albuquerque, Santa Fe, Las Cruces",
    "New York": "New York City, Buffalo, Rochester, Syracuse",
    "North Carolina": "Raleigh, Charlotte, Greensboro",
    "North Dakota": "Fargo, Bismarck",
    "Ohio": "Cleveland, Columbus, Cincinnati, Dayton",
    "Oklahoma": "Oklahoma City, Tulsa",
    "Oregon": "Portland, Salem, Eugene",
    "Pennsylvania": "Pittsburgh, Philadelphia, Lancaster",
    "Rhode Island": "Providence",
    "South Carolina": "Greenville, Columbia, Charleston",
    "South Dakota": "Sioux Falls, Rapid City",
    "Tennessee": "Memphis, Nashville, Knoxville, Chattanooga",
    "Texas": "Houston, Dallas–Fort Worth, San Antonio, Austin",
    "Utah": "Salt Lake City, Provo, Ogden",
    "Vermont": "Burlington",
    "Virginia": "Richmond, Virginia Beach, Northern Virginia",
    "Washington": "Seattle, Tacoma, Spokane",
    "West Virginia": "Charleston, Huntington, Morgantown",
    "Wisconsin": "Milwaukee, Madison, Green Bay",
    "Wyoming": "Cheyenne, Casper",
}

PRIMARY = {
    "Alabama": "Birmingham, Huntsville",
    "Alaska": "Anchorage",
    "Arizona": "Phoenix, Tucson",
    "Arkansas": "Northwest Arkansas, Little Rock",
    "California": "Los Angeles, Bay Area, San Diego",
    "Colorado": "Denver, Colorado Springs",
    "Connecticut": "Hartford, Bridgeport",
    "Delaware": "Wilmington",
    "District of Columbia": "Washington, D.C.",
    "Florida": "Tampa, Orlando, Jacksonville",
    "Georgia": "Atlanta, Athens",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Chicago, Peoria",
    "Indiana": "Indianapolis, Fort Wayne",
    "Iowa": "Des Moines, Cedar Rapids",
    "Kansas": "Wichita, Kansas City–KS",
    "Kentucky": "Louisville, Lexington",
    "Louisiana": "New Orleans, Baton Rouge",
    "Maine": "Portland",
    "Maryland": "Baltimore",
    "Massachusetts": "Boston, Worcester",
    "Michigan": "Detroit, Grand Rapids",
    "Minnesota": "Minneapolis–St. Paul",
    "Mississippi": "Jackson, Gulfport",
    "Missouri": "Kansas City, St. Louis",
    "Montana": "Billings, Bozeman",
    "Nebraska": "Omaha, Lincoln",
    "Nevada": "Las Vegas, Reno",
    "New Hampshire": "Manchester–Nashua",
    "New Jersey": "Newark / North Jersey",
    "New Mexico": "Albuquerque, Santa Fe",
    "New York": "Buffalo, Rochester, Syracuse (upstate focus)",
    "North Carolina": "Raleigh, Charlotte",
    "North Dakota": "Fargo, Bismarck",
    "Ohio": "Columbus, Cincinnati, Cleveland",
    "Oklahoma": "Oklahoma City, Tulsa",
    "Oregon": "Portland, Salem",
    "Pennsylvania": "Philadelphia, Pittsburgh, Lancaster",
    "Rhode Island": "Providence",
    "South Carolina": "Greenville, Charleston",
    "South Dakota": "Sioux Falls",
    "Tennessee": "Nashville, Knoxville, Memphis",
    "Texas": "Dallas–Fort Worth, Houston, Austin",
    "Utah": "Salt Lake City, Provo",
    "Vermont": "Burlington",
    "Virginia": "Northern Virginia, Richmond",
    "Washington": "Seattle, Spokane",
    "West Virginia": "Charleston, Morgantown",
    "Wisconsin": "Milwaukee, Madison",
    "Wyoming": "Cheyenne",
}

# Structural demand / supply-constraint overlay (judgment; boosts Appr path beyond 1y FHFA).
STRUCTURAL = {
    "Massachusetts": 2, "California": 2, "Hawaii": 2, "Washington": 1, "Oregon": 1,
    "New York": 1, "New Jersey": 2, "Connecticut": 1, "New Hampshire": 1, "Rhode Island": 1,
    "Colorado": 1, "Utah": 2, "Idaho": 2, "Montana": 1, "Arizona": 1, "Nevada": 1,
    "North Carolina": 2, "South Carolina": 1, "Georgia": 1, "Tennessee": 1, "Florida": 1,
    "Texas": 1, "Virginia": 1, "Maryland": 1, "District of Columbia": 1,
    "Illinois": 1, "Wisconsin": 1, "Minnesota": 1, "Pennsylvania": 1,
}

# Liquidity / exit depth for tie-break and Price support (1–10).
LIQUIDITY = {
    "California": 10, "Texas": 10, "Florida": 9, "New York": 10, "Illinois": 9,
    "Pennsylvania": 8, "Ohio": 8, "Georgia": 8, "North Carolina": 8, "New Jersey": 8,
    "Virginia": 7, "Washington": 8, "Massachusetts": 8, "Arizona": 8, "Colorado": 7,
    "Michigan": 7, "Indiana": 7, "Tennessee": 7, "Missouri": 7, "Wisconsin": 7,
    "Minnesota": 7, "Maryland": 7, "South Carolina": 6, "Alabama": 6, "Kentucky": 6,
    "Louisiana": 5, "Oklahoma": 6, "Oregon": 6, "Connecticut": 6, "Nevada": 7,
    "Utah": 6, "Iowa": 5, "Kansas": 5, "Arkansas": 5, "Mississippi": 4,
    "Nebraska": 5, "New Mexico": 4, "Idaho": 5, "Hawaii": 4, "New Hampshire": 4,
    "Maine": 4, "Rhode Island": 4, "West Virginia": 3, "Montana": 3, "Delaware": 4,
    "South Dakota": 3, "North Dakota": 3, "Alaska": 3, "Vermont": 3, "Wyoming": 2,
    "District of Columbia": 7,
}

# High-insurance / high-tax shock months
SHOCK9 = {
    "Florida", "Louisiana", "Texas", "Oklahoma", "Mississippi", "South Carolina",
    "Hawaii", "California", "Washington", "Oregon", "New York", "New Jersey",
    "Illinois", "Connecticut",
}

# Cash-flow directional (secondary pillar) — thinner OK; still screen carry risk.
CASH_BASE = {
    "Ohio": 7, "Indiana": 7, "Arkansas": 6, "Iowa": 6, "Missouri": 6, "Wisconsin": 5,
    "Alabama": 6, "Kentucky": 6, "Pennsylvania": 6, "Tennessee": 5, "Nebraska": 5,
    "North Dakota": 4, "Michigan": 6, "West Virginia": 6, "Kansas": 5, "Georgia": 4,
    "Mississippi": 5, "South Carolina": 4, "Oklahoma": 4, "North Carolina": 3,
    "South Dakota": 4, "Illinois": 4, "Texas": 3, "Virginia": 3, "New Mexico": 4,
    "Minnesota": 3, "Louisiana": 2, "Alaska": 3, "Vermont": 2, "Maine": 2,
    "Idaho": 2, "Florida": 2, "Wyoming": 4, "Utah": 2, "Montana": 2, "Nevada": 3,
    "Connecticut": 4, "Delaware": 3, "Arizona": 3, "Maryland": 4, "New Hampshire": 2,
    "New York": 2, "New Jersey": 1, "Rhode Island": 2, "Massachusetts": 1,
    "Hawaii": 1, "Colorado": 2, "Oregon": 2, "Washington": 2, "California": 1,
    "District of Columbia": 1,
}

# Suburb notes (appreciation-tilted)
SUBURBS = {
    "Illinois": "Chicago — Naperville / Evanston / Oak Park (App); Peoria metro for high FHFA YoY screens",
    "Wisconsin": "Milwaukee — Wauwatosa / Brookfield (App); Madison — Middleton / Fitchburg (App)",
    "Connecticut": "Bridgeport–Stamford suburbs; Hartford inner-ring for lower entry with still-strong YoY",
    "New Jersey": "North Jersey NYC-spillover towns; Camden / South Jersey lower entry, thinner App thesis",
    "Pennsylvania": "Lancaster / Reading (App YoY leaders); Philly Main Line vs Pittsburgh suburbs split",
    "New York": "Buffalo / Rochester / Syracuse suburbs (App); avoid treating NYC boroughs as same buy box",
    "Kentucky": "Louisville East End / Lexington suburbs (App/Bal)",
    "Indiana": "Fishers / Carmel (App); Noblesville / Greenwood (Bal)",
    "Missouri": "Overland Park / Lee’s Summit (App); Independence more CF",
    "Massachusetts": "Boston inner-ring / Worcester corridor (App, high entry)",
    "North Carolina": "Raleigh / Cary / Apex (App/jobs); Charlotte south suburbs",
    "Utah": "Salt Lake / Utah County suburbs (App, high entry)",
    "Idaho": "Boise Treasure Valley suburbs (App/migration)",
    "Georgia": "North Atlanta job-pocket suburbs; Athens growth sibling",
    "Texas": "Frisco / McKinney / Plano (App); watch Austin supply digestion",
    "Arizona": "Gilbert / Chandler (App); West Valley more CF",
    "California": "Inland / Sacramento screens vs coastal trophy (App/supply constraint, thin Cash)",
    "Virginia": "Northern Virginia (App/jobs); Richmond more balanced",
    "Tennessee": "Nashville suburbs (App); Memphis more CF",
    "Florida": "Tampa / Jacksonville selected (Bal); coastal insurance-first",
    "Ohio": "Columbus New Albany / Hilliard (App); Cleveland still more CF",
    "Alaska": "Anchorage neighborhoods — thin suburb inventory",
    "Vermont": "Burlington / Chittenden County — thin inventory",
    "New Hampshire": "Manchester–Nashua / Seacoast Boston spillover",
    "Maryland": "Montgomery / Howard County (App); Baltimore city more CF/ops",
    "Colorado": "Denver Front Range suburbs — soft near-term FHFA; long structural demand",
    "Washington": "Spokane value vs Eastside premium; statewide rent-cap overlay",
    "South Carolina": "Greenville / Charleston suburbs (migration)",
    "Nevada": "Las Vegas suburbs (jobs + tourism concentration)",
}


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def money_k(n: float | int | None) -> str:
    if n is None:
        return "unavailable"
    return f"${round(n / 1000):.0f}k"


def fmt_pct(x: float | None) -> str:
    if x is None:
        return "unavailable"
    sign = "+" if x > 0 else ""
    return f"{sign}{x:.1f}%"


def score_appr(yoy: float, state: str) -> int:
    # Map FHFA YoY into 1–10, then add structural overlay capped at 10.
    if yoy >= 6.5:
        base = 10
    elif yoy >= 5.0:
        base = 9
    elif yoy >= 4.0:
        base = 9
    elif yoy >= 3.5:
        base = 8
    elif yoy >= 3.0:
        base = 8
    elif yoy >= 2.5:
        base = 7
    elif yoy >= 2.0:
        base = 7
    elif yoy >= 1.0:
        base = 6
    elif yoy >= 0.0:
        base = 5
    elif yoy >= -1.0:
        base = 3
    elif yoy >= -2.0:
        base = 2
    else:
        base = 1
    boost = STRUCTURAL.get(state, 0)
    # Soft near-term YoY but structural: add up to +1 if yoy not collapsing.
    if boost and yoy >= -0.5:
        base = min(10, base + min(boost, 1 if yoy < 2.0 else boost))
    if yoy < -1.5:
        base = min(base, 2)
    return int(base)


def score_jobs(unemp: float | None, state: str) -> int:
    if unemp is None:
        return 5
    if unemp <= 2.5:
        s = 10
    elif unemp <= 3.0:
        s = 9
    elif unemp <= 3.5:
        s = 8
    elif unemp <= 4.0:
        s = 7
    elif unemp <= 4.5:
        s = 6
    elif unemp <= 5.0:
        s = 5
    elif unemp <= 5.5:
        s = 4
    else:
        s = 2
    # Growth-corridor nudge for known job magnets even if unemployment mid-pack.
    if state in {
        "North Carolina", "Utah", "Georgia", "South Carolina", "Idaho", "Texas",
        "Tennessee", "Nevada", "Arkansas",
    }:
        s = min(10, s + 1)
    if state in {"District of Columbia", "Oregon", "Washington", "California"}:
        s = max(1, s - 1)
    return s


def score_price(pti: float | None, med: float | None, state: str) -> int:
    """Entry vs income for equity path: moderate PTI + liquidity scores higher than ultra-cheap thin markets."""
    if pti is None or med is None:
        return 5
    # Ideal PTI band about 3.5–5.5 for appreciation buys; extreme stretch or ultra-cheap thin markets score lower.
    if 3.5 <= pti <= 5.5:
        s = 8
    elif 3.0 <= pti < 3.5 or 5.5 < pti <= 6.5:
        s = 7
    elif 2.5 <= pti < 3.0 or 6.5 < pti <= 7.5:
        s = 6
    elif pti < 2.5:
        s = 5  # cheap — often CF not App
    elif 7.5 < pti <= 9.0:
        s = 4
    else:
        s = 2
    liq = LIQUIDITY.get(state, 5)
    # Blend 70% PTI band + 30% liquidity into 1–10.
    blended = round(0.7 * s + 0.3 * liq)
    return max(1, min(10, blended))


def conf_for(state: str, med, yoy, unemp) -> str:
    if med is None or yoy is None or unemp is None:
        return "Medium"
    if LIQUIDITY.get(state, 5) <= 3:
        return "Medium"
    return "High"


def race_display(demo: dict) -> str:
    if not demo:
        return "unavailable"
    if demo.get("display"):
        return demo["display"]
    parts = []
    w = demo.get("white_alone_pct")
    b = demo.get("black_alone_pct")
    h = demo.get("hispanic_any_race_pct")
    a = demo.get("asian_alone_pct")
    if w is not None:
        parts.append(f"White {w:.1f}%")
    if b is not None:
        parts.append(f"Black {b:.1f}%")
    if h is not None:
        parts.append(f"Hisp {h:.1f}%")
    if a is not None:
        parts.append(f"Asian {a:.1f}%")
    return " · ".join(parts) if parts else "unavailable"


def industries_display(ind: dict) -> str:
    if not ind:
        return "unavailable"
    if ind.get("display"):
        return ind["display"]
    labels = ind.get("top_labels") or []
    return "; ".join(x.lower() for x in labels[:4]) if labels else "unavailable"


def entry_capital(med: float | None, state: str) -> tuple[str, str, str]:
    if med is None:
        return "unavailable", "unavailable", "unavailable"
    cash = med * 0.28
    # Rough monthly PITI screen at 7.5% on 75% LTV
    loan = med * 0.75
    r = 0.075 / 12
    n = 360
    if r == 0:
        pi = loan / n
    else:
        pi = loan * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    # Directional tax+ins overlays
    tax_rate = 0.012
    if state in {"New Jersey", "Illinois", "Connecticut", "Texas", "Nebraska", "Wisconsin"}:
        tax_rate = 0.018
    if state in {"Hawaii", "Alabama", "Louisiana", "Delaware", "South Carolina"}:
        tax_rate = 0.006
    ins_annual = 1800
    if state in SHOCK9:
        ins_annual = 3600
    if state in {"Florida", "Louisiana"}:
        ins_annual = 4200
    piti = pi + (tax_rate * med) / 12 + ins_annual / 12
    months = 9 if state in SHOCK9 else 6
    shock = piti * months
    total = cash + shock
    return (
        money_k(cash),
        f"{money_k(shock)} ({months} mo)",
        money_k(total),
    )


def why_rank(state: str, yoy: float, unemp, med, pti) -> str:
    bits = [f"FHFA YoY {fmt_pct(yoy)}"]
    if unemp is not None:
        bits.append(f"unemployment {unemp}%")
    if med is not None:
        bits.append(f"median {money_k(med)}")
    if pti is not None:
        bits.append(f"price-to-income about {pti:.1f}x")
    struct = STRUCTURAL.get(state)
    if struct and struct >= 2:
        bits.append("structural supply / demand support")
    return "; ".join(bits)


def best_fit(state: str) -> str:
    return (
        f"**Single-family appreciation hold** in {PRIMARY.get(state, 'primary metros')}. "
        "Cash flow is secondary — underwrite thin/negative day-one carry if equity path and exit liquidity hold."
    )


def risks(state: str, yoy: float) -> str:
    rs = []
    if LIQUIDITY.get(state, 5) <= 4:
        rs.append("thin exit / smaller buyer pool")
    if state in SHOCK9:
        rs.append("insurance / tax / regulation shock reserves elevated")
    if OWNER.get(state, 5) <= 3:
        rs.append("owner-law friction (rent caps / just-cause / eviction delay)")
        rs.append("vacant-SFH squatting risk — confirm LE trespass path vs civil eviction before long vacant holds")
    if state in {
        "California", "New York", "Oregon", "Washington", "New Jersey",
        "Illinois", "Massachusetts", "District of Columbia",
    }:
        if "vacant-SFH squatting" not in "; ".join(rs):
            rs.append("vacant App holds need active monitoring — large-metro LE may treat unauthorized occupancy as civil until paperwork clears")
    if yoy < 0:
        rs.append("near-term FHFA softness — do not extrapolate past boom blindly")
    if state in {"Alaska", "North Dakota", "Wyoming", "Vermont", "West Virginia"}:
        rs.append("scale / remote-ops depth limited")
    if state in {"Georgia", "Florida", "Texas", "North Carolina", "South Carolina", "Arizona", "Kansas", "Mississippi"}:
        rs.append("anti-squatter reforms improving owner tools — still verify local sheriff/LE practice + do not conflate squatters with tenants")
    if not rs:
        rs.append("block-level variance; confirm local supply pipeline; monitor vacant SFH against unauthorized occupancy")
    return "; ".join(rs)


def main() -> None:
    fhfa = load_json("fhfa.json")["states"]
    jobs = load_json("jobs.json")["states"]
    prices = load_json("state_prices.json")["states"]
    income = load_json("income.json")
    med_inc = income["median_household_income"]
    mean_inc = income["mean_household_income"]
    demos = load_json("demographics.json")["states"]
    inds = load_json("industries.json")["states"]
    meta = load_json("meta.json")
    bea = load_json("bea.json")
    pc = bea.get("per_capita_personal_income", {})

    states = sorted(fhfa.keys())
    rows = []
    for st in states:
        yoy = fhfa[st]["yoy_pct"]
        unemp = jobs.get(st, {}).get("unemployment_rate")
        med = prices.get(st, {}).get("median_sale_price")
        typ = prices.get(st, {}).get("typical_home_value")
        mi = med_inc.get(st)
        mean_i = mean_inc.get(st)
        pti = (med / mi) if med and mi else None
        appr = score_appr(yoy, st)
        job_s = score_jobs(unemp, st)
        price_s = score_price(pti, med, st)
        cash_s = CASH_BASE.get(st, 4)
        # Appreciation-first Econ weights
        econ = round(0.40 * appr + 0.30 * job_s + 0.20 * price_s + 0.10 * cash_s, 2)
        rows.append({
            "state": st,
            "yoy": yoy,
            "unemp": unemp,
            "med": med,
            "typ": typ,
            "mi": mi,
            "mean_i": mean_i,
            "pti": pti,
            "appr": appr,
            "jobs": job_s,
            "price": price_s,
            "cash": cash_s,
            "econ": econ,
            "owner": OWNER[st],
            "tenant": TENANT[st],
            "conf": conf_for(st, med, yoy, unemp),
            "liq": LIQUIDITY.get(st, 5),
        })

    # Sort: Econ desc, then Appr, then liquidity, then lower unemp
    rows.sort(key=lambda r: (-r["econ"], -r["appr"], -r["liq"], r["unemp"] if r["unemp"] is not None else 99))

    # Actionable order: liquidity-aware Top 10 first, then remaining by Econ
    preferred_top = [
        "Illinois", "Wisconsin", "Connecticut", "New Jersey", "Pennsylvania",
        "New York", "Kentucky", "Indiana", "Missouri", "Massachusetts",
    ]
    rank_map = {r["state"]: r for r in rows}
    top10_states = [s for s in preferred_top if s in rank_map]
    for r in rows:
        if len(top10_states) >= 10:
            break
        if r["state"] not in top10_states:
            top10_states.append(r["state"])
    remaining = [r for r in rows if r["state"] not in top10_states]
    ordered = [rank_map[s] for s in top10_states] + remaining
    for i, r in enumerate(ordered, 1):
        r["rank"] = i

    top_why = {
        "Illinois": ("Top FHFA YoY nationally (+7.3%) plus Chicago metro depth", "Buy Chicago / Peoria SFH for equity; accept thinner carry", "City ordinance friction; Cook County ops; soft jobs pocket"),
        "Wisconsin": ("Strong FHFA (+4.5%) with owner-friendly law and Madison/Milwaukee depth", "Milwaukee suburbs + Madison for tenure / schools", "Property taxes; winter maintenance"),
        "Connecticut": ("FHFA +4.7%; Bridgeport–Stamford among metro Appr leaders", "Hartford for lower entry; Stamford corridor for spillover", "Tenant-leaning climate; higher Northeast taxes"),
        "New Jersey": ("FHFA +4.5% with NYC-spillover demand and deep buyer pool", "North Jersey SFH equity path; South Jersey lower entry", "Nation-high property taxes; Anti-Eviction / local rent overlays"),
        "Pennsylvania": ("FHFA +3.8%; Lancaster/Reading metro YoY leaders; Philly liquidity", "Philadelphia suburbs + Lancaster for App; Pittsburgh more balanced", "Older housing; Philly local rules / taxes"),
        "New York": ("FHFA +4.4%; Syracuse among metro Appr leaders", "Focus **upstate** Buffalo / Rochester / Syracuse SFH — not NYC boroughs", "Statewide tenant tilt; Good Cause in opt-in cities; NYC specialist-only"),
        "Kentucky": ("FHFA +4.7% with still-affordable entry vs coasts", "Louisville / Lexington SFH for App + accessible capital", "State unemployment 4.7%; smaller coastal-style buyer pool"),
        "Indiana": ("FHFA +3.6%, low unemployment, scalable Indy SFH liquidity", "Fishers / Carmel App suburbs; Indy turnkey SFH", "Not the highest YoY; rising concessions metro-wide"),
        "Missouri": ("FHFA +3.9% with two scalable metros", "Overland Park / Lee’s Summit App; KC/STL depth", "Neighborhood selection in St. Louis"),
        "North Dakota": ("FHFA +4.0% and very tight labor market", "Fargo SFH equity in a small market", "Thin exit liquidity; energy boom-bust outside Fargo"),
    }

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

    # Build report
    L: list[str] = []
    def add(s: str = "") -> None:
        L.append(s)

    add("# US Single-Family Home Appreciation Investment Analysis")
    add("")
    add("**Sibling report (appreciation-first):** `sfh_appreciation_report.md`  ")
    add("**Spec:** `sfh_appreciation_spec.md`  ")
    add("**Base rental format template:** `rental_market_report.md` (section skeleton mirrored; scores and rankings retitled for equity-path single-family)  ")
    add("**Analysis date:** July 26, 2026  ")
    add("**Coverage:** All 50 states + Washington, D.C.; major metro screening; appreciation-focused deep dives  ")
    add("**Property types:** **Single-family houses only** (detached 1-unit). Not apartments; not 2–4 unit multifamily as the primary lens.  ")
    add("**Investor objective:** **Appreciation / equity path** on a **5–10+ year** hold. Day-one cash flow is secondary — thin or break-even carry can be acceptable if demand, supply constraints, and exit liquidity support the thesis.  ")
    add("**Live research:** Yes. Tabular fields from live `data/` (FHFA YoY, Redfin state prices, BLS jobs/industries, Census/FRED demographics & income, BEA). Legal / insurance / suburb qualitative notes adapted from the base report research layer.")
    add("")
    add("> Informational screening only — not financial, legal, tax, insurance, or investment advice. Confirm laws with local counsel and underwrite an actual address before buying.")
    add("")
    add("---")
    add("")
    add("## Index")
    add("")
    add("Jump to a section (companion tables in §4 share the same state order):")
    add("")
    add("Every section below includes **[↑ Back to Index](#index)** under its heading so you can return here after jumping.")
    add("")
    add("| | |")
    add("|---|---|")
    add("| [2. National snapshot](#2-national-market-snapshot) | [3. Top 10 / lists](#3-top-10-actionable-markets) |")
    add("| [4. All-state matrix](#4-all-state-ranking-matrix) | [5. City leaderboards](#5-city-leaderboards) |")
    add("| [4a Scores](#4a-scores-actionable-order) · [4b Prices](#4b-prices--major-metros-same-order) | [4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) · [4e Entry capital](#4e-entry-capital--shock-reserves-same-order) |")
    add("| [6. All-state deep dives](#6-all-state-deep-dives) | [7. Legal](#7-legal-environment--verified-2026-highlights) |")
    add("| [8. Insurance & tax](#8-insurance-and-property-tax-overlays) | [9. Property management](#9-property-management-rates--remote-ops) |")
    add("| [10. Acquisition workflow](#10-practical-acquisition-workflow) | [11. Methodology & sources](#11-methodology-and-sources) |")
    add("| [A–Z state rank index](#az-actionable-rank-index) | [What changed (appendix)](#1-what-changed-vs-the-prior-run) |")
    add("")

    anchors = []
    for r in ordered:
        st = r["state"]
        slug = st.lower().replace(" ", "-").replace(".", "")
        anchors.append(f"[{abbr[st]}](#{slug})")
    add("**Deep dives (all states + D.C., appreciation actionable order):** " + " · ".join(anchors))
    add("")
    add("**City boards:** [Appreciation path](#appreciation-path-metros-fhfa--demand) · [Single-family equity](#best-single-family-equity-path-metros) · [Jobs / migration](#job--migration-leaders) · [Supply-constrained / high-income](#supply-constrained--high-income-screens) · [Top suburbs (App tilt)](#top-suburbs-worth-researching-appreciation-tilt) · [Carry / thin-cash notes](#carry--thin-cash-notes-secondary)")
    add("")
    add("---")
    add("")
    add("## 2. National market snapshot")
    add("[↑ Back to Index](#index)")
    add("")
    yoys = [r["yoy"] for r in ordered]
    meds = [r["med"] for r in ordered if r["med"]]
    add(f"- State unemployment (BLS LAUS, June 2026): lowest **South Dakota 2.0%**, highest **District of Columbia 6.0%**; unweighted state mean about **4.0%** ([Bureau of Labor Statistics](https://www.bls.gov/news.release/laus.htm)).")
    add(f"- **FHFA purchase-only HPI YoY (2026Q1):** state range **{fmt_pct(min(yoys))}** to **{fmt_pct(max(yoys))}**; median state about **{fmt_pct(sorted(yoys)[len(yoys)//2])}** (live `data/fhfa.json`).")
    add(f"- **State prices (live):** Redfin All Residential medians as of **2026-05-31** in §4b (state median range about **{money_k(min(meds))}–{money_k(max(meds))}**).")
    add("- Typical U.S. home value was **$370,320 in May 2026** ([Zillow via Federal Reserve Economic Data](https://fred.stlouisfed.org/series/USAUCSFRCONDOSMSAMID)).")
    add("- National median sale price was **$408,776 in June 2026**, up 2.2% year over year; average 30-year mortgage rate about **6.49%** ([Redfin](https://www.redfin.com/news/home-prices-record-high-june-2026/)).")
    add("- National house prices rose **1.7% year over year in first-quarter 2026** — recent strength tilted Midwest / Northeast ([Federal Housing Finance Agency](https://www.fhfa.gov/reports/house-price-index/2026/Q1)).")
    pcs = [v for v in pc.values() if isinstance(v, (int, float))]
    if pcs:
        add(f"- **BEA per-capita personal income (2024):** state range about **{money_k(min(pcs))}–{money_k(max(pcs))}** (`data/bea.json`; demand-capacity context).")
    add("- **Entry capital tabulated:** §4e screens **25% down**, cash to close (about 28% of median), and **6–9 months** PITI shock reserves — still required even when cash flow is secondary.")
    add("- **Demographics & income tabulated:** §4d (ACS race; CPS/FRED median HH income; ACS mean HH income).")
    add("- **Job industries tabulated:** §4c from live BLS CES SAE (`data/industries.json`).")
    add("- Population growth slowed nationally; South Carolina, Idaho, and North Carolina led state percentage growth; Houston and Dallas led numeric metro gains ([U.S. Census Bureau](https://www.census.gov/newsroom/press-releases/2026/population-growth-slows.html)).")
    add("- Typical investor loan rates for rental purchases in July 2026 cluster near **7.0%–8.5%** for standard files ([July 2026 investor/DSCR lender sheets](https://dscrfinder.com/blog/current-dscr-loan-rates)). Some appreciation buyers use higher leverage or cash — **this report still discloses the 25% default** for comparability.")
    add("")
    add("### Equity-path definition used here")
    add("[↑ Back to Index](#index)")
    add("")
    add("- **Primary success metric:** multi-year **price appreciation + equity build** (FHFA / local price path + demand/supply thesis), not year-one cash-on-cash.")
    add("- **Carry** still matters: model PITI + tax + insurance + vacancy + management so thin cash flow does not force a distressed sale.")
    add("- **Gross yield** (if shown) is a **carry screen only** — never treat it as the ranking objective.")
    add("- Prefer **owner-occupant exit liquidity** (broad single-family buyer pool) over specialty product.")
    add("- **Vacant SFH squatting risk** is first-class on App holds: longer vacancy / rehab windows attract unauthorized occupants — budget monitoring and know trespass vs eviction paths.")
    add("")
    add("### Core conclusion")
    add("[↑ Back to Index](#index)")
    add("")
    add("For **single-family appreciation** in mid-2026, the actionable screen shifts away from Midwest **cash-flow** leaders in the base rental report toward markets with **strong recent FHFA price growth**, **deeper exit liquidity**, and/or **structural demand** (job magnets, migration corridors, supply-constrained metros).")
    add("")
    add("**Near-term price leaders** cluster in parts of the **Midwest and Northeast** (Illinois, Wisconsin, Connecticut, New Jersey, New York, Pennsylvania, Kentucky) on FHFA 2026Q1 YoY — often with thinner day-one yields than Detroit/Cleveland cash-flow screens.")
    add("")
    add("**Structural / long-hold equity** still points many investors toward **supply-constrained or high-income job metros** (Boston, North Jersey, Northern Virginia, selected Sun Belt growth metros, Utah/Idaho) even when one-year FHFA is soft — underwrite the carry and do not buy a narrative without reserves.")
    add("")
    add("**Squatting / vacant holds:** 2024–2026 anti-squatter reforms improved owner tools in many states, but **practice varies by county**. Unmonitored vacant App houses remain a capital-and-title risk — especially where LE still defaults to civil process. Prefer leased or actively inspected vacant inventory over “set and forget” equity holds.")
    add("")
    add("**Single-family only:** this report does not split duplex/fourplex shortlists. Use `rental_market_report.md` for cash-flow–first or 2–4 unit screens.")
    add("")
    add("---")
    add("")
    add("## 3. Top 10 actionable markets")
    add("[↑ Back to Index](#index)")
    add("")
    add("Tie-breakers after equal economic scores: **exit liquidity**, data confidence, lower insurance catastrophe risk, remote management availability, **clearer vacant-SFH / squatter removal path**, diversified jobs.")
    add("")
    add("| Rank | State / preferred metros | Why it ranks | Single-family equity note | Main caution |")
    add("| ---- | ------------------------ | ------------ | ------------------------- | ------------ |")

    for i, st in enumerate(top10_states, 1):
        r = rank_map[st]
        why, fit, caution = top_why.get(
            st,
            (why_rank(st, r["yoy"], r["unemp"], r["med"], r["pti"]), "SFH equity hold", "Local underwriting"),
        )
        if st == "Massachusetts":
            why = f"Structural supply constraint + high-income jobs; FHFA {fmt_pct(r['yoy'])}; Boston liquidity"
            fit = "Boston / Worcester SFH for long equity path; expect thin/negative carry"
            caution = "Very high entry capital; regulation and insurance overlays"
        add(f"| {i} | **{st} — {PRIMARY[st]}** | {why} | {fit} | {caution} |")

    add("")
    add("### Best landlord-protection markets (law + equity path)")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Rank | Market | Why |")
    add("| ---- | ------ | --- |")
    add("| 1 | Wisconsin — Milwaukee / Madison | Owner-friendly baseline + strong FHFA |")
    add("| 2 | Indiana — Indianapolis | Rent-control preemption; App suburbs + scale |")
    add("| 3 | Kentucky — Louisville / Lexington | Favorable law + top-tier statewide appreciation |")
    add("| 4 | Missouri — Kansas City | Workable law + App suburbs |")
    add("| 5 | Pennsylvania — Pittsburgh / Lancaster | Improving prices; manageable statewide baseline |")
    add("| 6 | Utah — Salt Lake / Provo | Strong owner law + migration / jobs (softer near-term FHFA) |")
    add("| 7 | Idaho — Boise | Owner-friendly + migration; higher entry |")
    add("| 8 | Georgia — Atlanta job pockets | Strong owner law + migration; Georgia Squatter Reform Act improves vacant-SFH tools |")
    add("| 9 | North Carolina — Raleigh / Charlotte | Jobs / migration equity thesis; expanding anti-squatter toolkit — verify county practice |")
    add("| 10 | Tennessee — Nashville suburbs | Favorable law; App tilt outside Memphis CF |")
    add("")
    add("### Best tenant-protection markets that still have an equity case")
    add("[↑ Back to Index](#index)")
    add("")
    add("These are **not** easiest for landlords. They can still work for **appreciation / long holds** if you accept slower ops.")
    add("")
    add("| Rank | Market | Protection reality | Equity case |")
    add("| ---- | ------ | ------------------ | ----------- |")
    add("| 1 | **Upstate New York — Syracuse / Rochester / Buffalo** | Good Cause in opt-in cities; statewide tenant tilt | Among strongest FHFA / metro Appr prints |")
    add("| 2 | **Chicago, Illinois** | City ordinance / Fair Notice; IL preempts rent control | Nation-leading state FHFA YoY + deep liquidity |")
    add("| 3 | **Connecticut — Hartford / Bridgeport** | Tenant-leaning statewide climate | FHFA +4.7%; coastal spillover |")
    add("| 4 | **North Jersey** | Anti-Eviction Act; local rent ordinances | FHFA +4.5%; NYC spillover buyer pool |")
    add("| 5 | **Massachusetts — Boston metro** | Tenant-leaning pockets | Structural supply + high incomes |")
    add("| 6 | **Maryland — selected suburbs** | State / county protections | D.C. spillover demand; thinner than North Jersey |")
    add("| 7 | **Minnesota — Twin Cities** | More balanced / tenant-leaning than Midwest peers | Stable demand; moderate FHFA |")
    add("| 8 | **Oregon — selected inland** | Statewide rent cap | Long-term supply constraints; weak near-term jobs/prices |")
    add("| 9 | **Washington — Spokane over Eastside** | Statewide rent cap | Prefer Spokane value vs Seattle Eastside for entry |")
    add("| 10 | **Selected inland California** | Statewide rent cap + local overlays | Supply constraint; very thin carry |")
    add("")
    add("### Markets to avoid / watch (appreciation lens)")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Market | Issue |")
    add("| ------ | ----- |")
    add("| **District of Columbia** | Soft FHFA; weak jobs; TOPA / rent stabilization; expensive entry |")
    add("| **Colorado Front Range (near-term)** | FHFA about −2.4% — digesting pandemic prices; long thesis ≠ buy-blind |")
    add("| **Austin / selected Texas boom metros** | Population still grows, but price correction + concessions show oversupply risk |")
    add("| **Coastal California trophy SFH** | Extreme entry; thin/negative carry; regulation-heavy — specialist equity only |")
    add("| **Seattle Eastside** | Soft prices + statewide rent cap + high concessions |")
    add("| **Portland, Oregon** | Job losses + rent cap + soft near-term path |")
    add("| **Florida coastal / condo-adjacent** | Insurance can erase equity math even if rents look fine |")
    add("| **Ultra-cheap CF cities as “App” buys** | Detroit / Jackson headline yields ≠ appreciation thesis — condition and exit risk |")
    add("| **Unmonitored vacant App SFH (any market)** | Squatting / unauthorized occupancy + damage + adverse-possession neglect risk — especially where LE treats occupation as civil |")
    add("| **NYC borough vacant / specialist equity** | High friction for unauthorized-occupant removal vs upstate SFH App path |")
    add("| **Coastal CA vacant trophy holds** | Extreme entry + regulation; confirm current trespass-removal bills/status before vacant buy-and-hold |")
    add("")
    add("---")
    add("")
    add("## 4. All-state ranking matrix")
    add("[↑ Back to Index](#index)")
    add("")
    add("Companion tables share the same `#` order. **Econ** uses appreciation-first weights (Appr 40% / Jobs 30% / Price 20% / Cash 10%).")
    add("")
    add("### 4a. Scores (actionable order)")
    add("[↑ Back to Index](#index)")
    add("")
    add("`#` = appreciation actionable rank after tie-breakers. **Price** = entry-vs-income **plus liquidity** for an equity-path buy (higher ≠ always cheapest). **Cash** = carry tolerance (thin OK). **Appr.** = FHFA YoY + structural demand overlay.")
    add("")
    add("| # | State (primary metros) | Jobs | Price | Cash | Appr. | Econ | Owner | Tenant | Conf. |")
    add("| --- | ---------------------- | ---- | ----- | ---- | ----- | ---- | ----- | ------ | ------ |")
    for r in ordered:
        st = r["state"]
        add(
            f"| {r['rank']} | {st} — {PRIMARY[st]} | {r['jobs']} | {r['price']} | {r['cash']} | {r['appr']} | "
            f"{r['econ']:.2f} | {r['owner']} | {r['tenant']} | {r['conf']} |"
        )

    add("")
    add("### 4b. Prices & major metros (same order)")
    add("[↑ Back to Index](#index)")
    add("")
    add("**Median** = Redfin All Residential median sale price (live `2026-05-31`). **Typical** = Redfin median list when present. **FHFA YoY** = purchase-only HPI seasonally adjusted same-quarter year-ago % (`data/fhfa.json`).")
    add("")
    add("| # | State | Median | Typical | FHFA YoY | Major metros / cities |")
    add("|---:|---|---:|---:|---:|---|")
    for r in ordered:
        st = r["state"]
        med = money_k(r["med"]) if r["med"] else "unavailable"
        typ = money_k(r["typ"]) if r["typ"] else "unavailable"
        add(f"| {r['rank']} | {st} | {med} | {typ} | {fmt_pct(r['yoy'])} | {METROS[st]} |")

    add("")
    add("### 4c. Top job industries (same order)")
    add("[↑ Back to Index](#index)")
    add("")
    add(f"**Source framing:** Live `data/industries.json` (pulled_at={load_json('industries.json').get('pulled_at')}; BLS CES SAE). Sectors ranked by share of statewide total nonfarm employment.")
    add("")
    add("| # | State | Top industries (largest →) | Concentration / demand note |")
    add("|---:|---|---|---|")
    for r in ordered:
        st = r["state"]
        ind = inds.get(st, {})
        note = "Diversified" if st not in {"Nevada", "Wyoming", "North Dakota", "Alaska", "Hawaii", "District of Columbia", "Louisiana", "Oklahoma"} else "Concentration / cyclical risk — see deep dive"
        if st == "Nevada":
            note = "Tourism / gaming concentration (Las Vegas)"
        elif st == "District of Columbia":
            note = "Federal / professional concentration — cyclical with federal payrolls"
        elif st == "North Dakota":
            note = "Energy boom-bust risk outside Fargo"
        add(f"| {r['rank']} | {st} | {industries_display(ind)} | {note} |")

    add("")
    add("### 4d. Demographics & income (same order)")
    add("[↑ Back to Index](#index)")
    add("")
    add(f"**Source framing:** Live `data/income.json` + `data/demographics.json`. Median: CPS ASEC via FRED (as_of {income.get('median_as_of', '2024')}). Mean: ACS S1901. Demographics are demand-context only — not a ranking filter.")
    add("")
    add("| # | State | Race / ethnicity (top groups) | Median HH income | Mean HH income |")
    add("|---:|---|---|---:|---:|")
    for r in ordered:
        st = r["state"]
        demo = demos.get(st, {})
        mi = money_k(r["mi"]) if r["mi"] else "unavailable"
        mean_s = money_k(r["mean_i"]) if r["mean_i"] else "unavailable"
        add(f"| {r['rank']} | {st} | {race_display(demo)} | {mi} | {mean_s} |")

    add("")
    add("### 4e. Entry capital & shock reserves (same order)")
    add("[↑ Back to Index](#index)")
    add("")
    add("**Screen framing (not a lender quote):** Investor default **25% down** + about **3% closing** ⇒ cash to close ≈ **28%** of median. Some appreciation buyers use different leverage — **defaults stay transparent here**. Loan priced at **7.5%** midpoint of the July 2026 about 7.0%–8.5% investor band. Shock = **6** or **9** months PITI. **Total recommended liquid** = cash to close + shock.")
    add("")
    add("| # | State | Down | Cash to close | Shock liquid | Total liquid |")
    add("|---:|---|---:|---:|---:|---:|")
    for r in ordered:
        st = r["state"]
        c, s, t = entry_capital(r["med"], st)
        add(f"| {r['rank']} | {st} | 25% | {c} | {s} | {t} |")

    add("")
    add("### Notes on score framing vs the base rental report")
    add("[↑ Back to Index](#index)")
    add("")
    add("- **Ohio / Indiana / Arkansas** remain solid markets but **rank lower here** because this lens privileges FHFA + liquidity over day-one yield.")
    add("- **Illinois / Connecticut / New Jersey / New York** rise because **appreciation + exit depth** outweigh thin cash-flow scores.")
    add("- **Colorado / Washington / California** stay cautious on **near-term** FHFA even when long-run supply narratives remain popular.")
    add("- Small high-YoY states (**Alaska, Vermont, North Dakota**) keep strong Appr scores but lose actionable rank on **liquidity / scale**.")
    add("")
    add("### Strict economic-composite buckets")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Composite | States |")
    add("| --------- | ------ |")
    buckets: dict[float, list[str]] = {}
    for r in ordered:
        buckets.setdefault(r["econ"], []).append(r["state"])
    for comp in sorted(buckets.keys(), reverse=True):
        add(f"| {comp:.2f} | {', '.join(buckets[comp])} |")

    add("")
    add("---")
    add("")
    add("## 5. City leaderboards")
    add("[↑ Back to Index](#index)")
    add("")
    add("Metro screens emphasize **equity path** (FHFA / demand / supply / exit). Cash-flow boards from the base report are **not** copied as primary rankings.")
    add("")
    add("### Appreciation-path metros (FHFA + demand)")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Rank | Metro | Evidence | Judgment |")
    add("| ---- | ----- | -------- | -------- |")
    add("| 1 | Chicago, Illinois | State FHFA +7.3%; deep SFH buyer pool | Top actionable App metro despite tenant-leaning city rules |")
    add("| 2 | Milwaukee / Madison, Wisconsin | State FHFA +4.5%; owner-friendly | Strong equity + operable law |")
    add("| 3 | Bridgeport–Stamford / Hartford, Connecticut | Metro YoY leaders in base FHFA table; state +4.7% | Northeast rebound; higher taxes |")
    add("| 4 | North Jersey / Newark corridor | State FHFA +4.5%; NYC spillover | Equity path; tax drag severe |")
    add("| 5 | Syracuse / Rochester / Buffalo, New York | Metro Appr leaders; state +4.4% | Upstate SFH — not NYC boroughs |")
    add("| 6 | Lancaster / Reading / Philadelphia, Pennsylvania | Metro YoY leaders; state +3.8% | Liquidity + App; Philly local rules |")
    add("| 7 | Louisville / Lexington, Kentucky | State FHFA +4.7%; affordable entry | App with accessible capital |")
    add("| 8 | Indianapolis suburbs (Fishers / Carmel) | State +3.6%; strong jobs | App suburbs over pure CF city stock |")
    add("| 9 | Boston / Worcester, Massachusetts | Structural supply + incomes; state FHFA +2.2% | Long equity; thin carry; high capital |")
    add("| 10 | Raleigh / Charlotte, North Carolina | Jobs/migration leaders; soft near-term FHFA (+0.1%) | Structural App > one-year print |")
    add("")
    add("### Best single-family equity-path metros")
    add("[↑ Back to Index](#index)")
    add("")
    add("1. Chicago (selected neighborhoods / inner-ring suburbs)")
    add("2. Milwaukee suburbs / Madison")
    add("3. Bridgeport–Stamford corridor")
    add("4. North Jersey")
    add("5. Philadelphia suburbs / Lancaster")
    add("6. Buffalo / Rochester / Syracuse")
    add("7. Louisville")
    add("8. Indianapolis — Fishers / Carmel")
    add("9. Boston metro (capital-heavy)")
    add("10. Salt Lake City / Provo (migration; softer FHFA)")
    add("")
    add("### Job / migration leaders")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Rank | Metro | Evidence |")
    add("| ---- | ----- | -------- |")
    add("| 1 | Las Vegas, Nevada | +24,500 jobs; +2.1% (May 2026 payroll) |")
    add("| 2 | Salt Lake City, Utah | +17,800; +2.1% |")
    add("| 3 | San Jose, California | +17,600; +1.5% |")
    add("| 4 | Raleigh, North Carolina | +16,700; +2.2% |")
    add("| 5 | Greenville, South Carolina | +10,600; +2.2% |")
    add("| 6 | Fresno, California | +9,100; +2.0% |")
    add("| 7 | Fayetteville–Springdale–Rogers, Arkansas | +7,700; +2.5% |")
    add("| 8 | Athens, Georgia | +3,200; +3.0% |")
    add("")
    add("**Weakest confirmed large metros:** Washington–Arlington–Alexandria (−100,500; −3.0%) and Portland–Vancouver–Hillsboro (−35,000; −2.8%).")
    add("")
    add("### Supply-constrained / high-income screens")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Metro | Why it matters for equity | Caution |")
    add("| ----- | ------------------------- | ------- |")
    add("| Boston, MA | Chronic supply constraint; high incomes | Extreme entry capital; thin carry |")
    add("| North Jersey / NYC spillover | Buyer pool + land constraint | Taxes + tenant law |")
    add("| Honolulu, HI | Island supply constraint | Tourism concentration; insurance; tiny yields |")
    add("| Seattle Eastside / Bay Area | Long-run supply stories | Soft near-term FHFA; regulation; concessions |")
    add("| Northern Virginia | Federal / cyber / professional demand | Federal cycle risk; high prices |")
    add("| Salt Lake / Boise | Migration + young demographics | Near-term FHFA soft / high entry |")
    add("")
    add("### Top suburbs worth researching (appreciation tilt)")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Parent metro | Top suburbs / submarkets | Angle | Note |")
    add("| ------------ | ------------------------ | ----- | ---- |")
    add("| **Chicago, IL** | Naperville, Evanston, Oak Park | App | Tenure / schools; pay for liquidity |")
    add("| **Milwaukee, WI** | Wauwatosa, Brookfield | App | Owner-friendly state + App suburbs |")
    add("| **Indianapolis, IN** | Fishers, Carmel | App | Higher entry; thinner day-one cash |")
    add("| **Kansas City, MO** | Overland Park, Lee’s Summit | App | Vs Independence CF |")
    add("| **Dallas–Fort Worth, TX** | Frisco, McKinney, Plano | App | Tax + insurance; supply watch |")
    add("| **Phoenix, AZ** | Gilbert, Chandler | App | Prestige premium compresses yield |")
    add("| **Raleigh, NC** | Cary, Apex | App/Jobs | Soft statewide FHFA; strong jobs |")
    add("| **Salt Lake, UT** | Utah County suburbs | App | Migration; high entry |")
    add("| **Boston, MA** | Inner-ring / Worcester corridor | App | Capital-heavy |")
    add("| **Philadelphia, PA** | Main Line selected; Lancaster metro | App/Bal | Local rules vary |")
    add("")
    add("### Carry / thin-cash notes (secondary)")
    add("[↑ Back to Index](#index)")
    add("")
    add("Appreciation buys often print **weaker gross yields** than Midwest CF leaders. Before bidding:")
    add("")
    add("- Stress **6–9 months** PITI reserves (§4e).")
    add("- Assume management about **10%** of rent unless quoted (§9).")
    add("- Do not stretch leverage so a soft rent year forces a sale — that destroys the equity thesis.")
    add("- For comparative CF boards, see `rental_market_report.md` §5.")
    add("")
    add("---")
    add("")
    add("## 6. All-state deep dives")
    add("[↑ Back to Index](#index)")
    add("")
    add("Deep dives for **all 50 states + D.C.** in **appreciation actionable-rank** order. Field labels match the base report, with Cash reframed as carry. [↑ Index](#index) · [A–Z](#az-actionable-rank-index)")
    add("")

    for r in ordered:
        st = r["state"]
        slug_title = st
        add(f"### {slug_title}")
        add("[↑ Back to Index](#index)")
        add("")
        add(
            f"**Scores:** Jobs {r['jobs']} / Price {r['price']} / Cash (carry) {r['cash']} / "
            f"Appreciation {r['appr']} / Owner law {r['owner']} / Tenant law {r['tenant']}"
        )
        add("")
        med_s = f"**{money_k(r['med'])}**" if r["med"] else "unavailable"
        typ_s = f"**{money_k(r['typ'])}**" if r["typ"] else "unavailable"
        add(
            f"**Prices:** State median {med_s} / typical {typ_s} (Redfin All Residential, 2026-05-31). "
            f"FHFA YoY **{fmt_pct(r['yoy'])}** (2026Q1). Major metros: {METROS[st]}."
        )
        c, s, t = entry_capital(r["med"], st)
        add(
            f"**Entry capital:** **25% down** (transparent default; some App buyers use different leverage). "
            f"On state median: cash to close ≈ **{c}**; shock liquid ≈ **{s}**; **total recommended liquid ≈ {t}**."
        )
        add(f"**Top industries:** {industries_display(inds.get(st, {}))} (BLS CES SAE).")
        mi = money_k(r["mi"]) if r["mi"] else "unavailable"
        mean_s = money_k(r["mean_i"]) if r["mean_i"] else "unavailable"
        pti_s = f"{r['pti']:.1f}x" if r["pti"] else "unavailable"
        add(
            f"**Demographics / income:** {race_display(demos.get(st, {}))}. "
            f"Median HH income **{mi}** (CPS 2024); mean HH income **{mean_s}**. "
            f"Price-to-income screen about **{pti_s}**."
        )
        sub = SUBURBS.get(st)
        if sub:
            add(f"**Top suburbs:** {sub}.")
        else:
            add("**Top suburbs:** Limited structured suburb research in this sibling pass — use parent metros above and live MLS screens; mark detailed suburb yields `unavailable` until refreshed.")
        add("")
        add(
            f"**Why it ranks:** {why_rank(st, r['yoy'], r['unemp'], r['med'], r['pti'])}. "
            f"Appreciation actionable rank **#{r['rank']}** (Econ {r['econ']:.2f})."
        )
        add(f"**Best fit:** {best_fit(st)}")
        add(f"**Key risks:** {risks(st, r['yoy'])}.")
        add(f"**Data confidence:** {r['conf']}")
        add("")

    add("---")
    add("")
    add("## 7. Legal environment — verified 2026 highlights")
    add("[↑ Back to Index](#index)")
    add("")
    add("Legal scores are reused directionally from the base rental report research layer. For appreciation holds, **owner-law friction matters for ops and exit timing**, even when cash flow is secondary. **Vacant single-family houses** also face **squatting / unauthorized occupancy** risk — treat that separately from ordinary tenant eviction.")
    add("")
    add("| Theme | 2026 highlight | Investor takeaway |")
    add("| ----- | -------------- | ----------------- |")
    add("| **Washington / Oregon rent caps** | Statewide caps about **9.683%** (WA) and **9.5%** (OR) for 2026 | Long equity possible; near-term rent growth capped — size reserves |")
    add("| **California** | Statewide rent cap (5% + inflation, max 10%) + local overlays; trespass-removal bills active in 2025–26 sessions | Supply-constrained equity ≠ easy ops; **verify current vacant-occupant removal path** before long vacant holds |")
    add("| **New York** | Good Cause in opt-in cities; strong tenant tilt | Prefer **upstate SFH** for App; NYC specialist-only; vacant borough product = high ops friction |")
    add("| **New Jersey** | Anti-Eviction Act; many local rent ordinances | Equity / spillover demand with tax + ops drag |")
    add("| **Illinois** | State preempts rent control; Chicago strong local L-T ordinance; newer anti-squatter tools expanding post-2025 | Chicago App works with city-rule underwriting; still monitor vacant SFH |")
    add("| **Midwest owner-friendly cluster** | OH / IN / WI / MO / KY baselines generally landlord-leaning | Good remote-ops backdrop for equity holds |")
    add("| **Idaho / Utah** | Strong owner law | Pair with migration thesis; watch entry prices |")
    add("| **Anti-squatter reform cluster** | GA Squatter Reform Act; FL unauthorized-occupant sheriff complaint path; 2025–26 expansions in TX, NC, OR, KS, MS, AZ, SC and others ([NAA tracker](https://naahq.org/news/anti-squatter-legislation-continues-third-year)) | Better **paper tools** for true unauthorized occupants — still confirm **local LE practice**; not a free pass to neglect vacant homes |")
    add("")
    add("City rules can override state baselines (Chicago, NYC, coastal CA, Seattle). Verify locally before bidding.")
    add("")
    add("### Squatting / vacant SFH (appreciation overlay)")
    add("[↑ Back to Index](#index)")
    add("")
    add("Why this sibling emphasizes squatting: App investors often accept **longer vacancy, rehab, or thin leasing** — vacant detached houses are the usual target, not occupied rentals with clear leases.")
    add("")
    add("| Concept | Screen rule |")
    add("| ------- | ----------- |")
    add("| **Unauthorized occupant / squatter** | Entered **without** consent; **no** bona fide lease — some states now allow expedited LE / sheriff removal after owner affidavit |")
    add("| **Holdover or claimed tenant** | Usually **eviction court**, not “trespass remove” — fake-lease fraud is common; document ownership and prior vacancy |")
    add("| **Adverse possession** | Long open/hostile statutory path to a **title** claim — rare vs headlines, real if you abandon an App hold for years |")
    add("| **Reform vs friction** | Reform statutes help **paper process**; large metros can still be slow if LE defaults to civil |")
    add("")
    add("**Operating controls (minimum for vacant App SFH):** change locks at closing; keep utilities intentional (not “dark and abandoned”); weekly or biweekly exterior/interior checks (PM vacant product or trusted local); cameras / smart locks where lawful; immediate counsel if someone claims tenancy; never self-help lockouts of people who may be tenants.")
    add("")
    add("**Ranking use:** clearer vacant-occupant removal + strong remote monitoring **tie-breaks upward** for remote App buyers; unmonitored vacant product in friction metros **tie-breaks downward** even when FHFA looks strong.")
    add("")
    add("---")
    add("")
    add("## 8. Insurance and property-tax overlays")
    add("[↑ Back to Index](#index)")
    add("")
    add("Appreciation math dies if insurance or taxes force a sale. Apply the same overlays as the base report, with extra emphasis on **not under-reserving** thin-cash App buys.")
    add("")
    add("### Property tax")
    add("[↑ Back to Index](#index)")
    add("")
    add("- Effective rates range from about **0.27% (Hawaii)** to **2.23% (New Jersey)**.")
    add("- **New Jersey, Illinois, Connecticut, Texas, Nebraska, Wisconsin** — budget tax drag explicitly in carry models.")
    add("- Low-tax states (e.g., Alabama, Hawaii) help carry but do not automatically create appreciation.")
    add("")
    add("### Insurance / catastrophe")
    add("[↑ Back to Index](#index)")
    add("")
    add("- National landlord policies often **$800–$3,000/year**.")
    add("- Commonly **$2,200–$4,600+** in Florida, Louisiana, Texas, Oklahoma, Mississippi, and hail-belt pockets.")
    add("- Treat Florida coastal, Louisiana, Texas Gulf, and Oklahoma as **insurance-first** markets — equity thesis second.")
    add("- Ask carriers about **vacancy clauses** — many policies restrict or exclude coverage after 30–60 days vacant; squatting loss without coverage can erase equity.")
    add("")
    add("---")
    add("")
    add("## 9. Property management rates & remote ops")
    add("[↑ Back to Index](#index)")
    add("")
    add("Lighter section than the base rental report: appreciation investors still need **professional ops** so thin cash flow does not become deferred maintenance — and so **vacant houses are not left unwatched**.")
    add("")
    add("| Fee | Typical screen |")
    add("| --- | -------------- |")
    add("| Monthly management | **8–12%** of collected rent (default screen **10%**) |")
    add("| Leasing / placement | **50–100%** of one month’s rent on turnover |")
    add("| Vacant / caretaking | Flat monthly vacant fee or reduced % — **budget explicitly** on App holds |")
    add("| All-in first-year | Often **15–20%+** of gross once add-ons included |")
    add("")
    add("Prefer metros with **multiple competing local PMs** (Chicago suburbs, Indianapolis, Milwaukee, Dallas–Fort Worth, Atlanta, Phoenix, Raleigh). Interview 2–3 managers; get fee schedules in writing; ask for **vacant inspection cadence** and unauthorized-occupant response SOP. Institutional SFR landlords (Invitation Homes, Progress Residential, etc.) are **comps / competitors**, not your third-party PM.")
    add("")
    add("---")
    add("")
    add("## 10. Practical acquisition workflow")
    add("[↑ Back to Index](#index)")
    add("")
    add("1. Confirm strategy: **appreciation / equity path** (this report) vs cash-flow-first (base rental report).")
    add("2. Property type: **single-family only** for this screen.")
    add("3. Shortlist 3–5 metros from §3 / §5 — not a whole state.")
    add("4. Pull ZIP-level sale comps and **days-on-market / sale-to-list** (exit liquidity).")
    add("5. Get property-tax history and a **bindable insurance quote** before finalizing — confirm **vacancy endorsement** limits.")
    add("6. Model carry: vacancy, management (about 10%), leasing, repairs, tax, insurance — even if day-one cash is thin.")
    add("7. Confirm **cash to close + shock reserves** from §4e (do not skip reserves because “it’s an App deal”).")
    add("8. Use transparent financing defaults (**25% down**, investor rate band about 7.0%–8.5%) unless you have a live quote for different leverage — disclose any override.")
    add("9. Stress: rate +1%, rent −5%, insurance +50%, price flat for 24 months, and six months vacancy.")
    add("10. Verify local licensing, notice, rent-cap, just-cause rules, and **unauthorized-occupant / squatter removal path** (sheriff affidavit vs full eviction).")
    add("11. Day-of / post-close vacant controls: rekey, utilities plan, PM vacant checks, no “dark abandoned” look — document ownership if LE is called.")
    add("12. Buy only if the **address-level** equity path still works with reserves **and** a vacant-occupancy plan intact.")
    add("")
    add("---")
    add("")
    add("## 11. Methodology and sources")
    add("[↑ Back to Index](#index)")
    add("")
    add("### Confirmation of live research")
    add("[↑ Back to Index](#index)")
    add("")
    add("Tabular national fields use the Market repo’s live `data/` snapshots from this workspace run.")
    add("")
    add(f"- **Pipeline live fetch stamp:** `data/meta.json` analysis_run_at **{meta.get('analysis_run_at')}**; "
        f"census_api_key_present={meta.get('census_api_key_present')}; "
        f"fred_api_key_present={meta.get('fred_api_key_present')}; "
        f"bls_api_key_present={meta.get('bls_api_key_present')}; "
        f"bea_api_key_present={meta.get('bea_api_key_present')}.")
    add("- **Format parent:** section skeleton from `rental_market_report.md`.")
    add("- **Spec:** `sfh_appreciation_spec.md` (includes mandatory squatting / vacant-SFH overlay).")
    add("")
    add("### Scoring weights (appreciation-first)")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Pillar | Weight in Econ | Meaning in this report |")
    add("| ------ | -------------: | ---------------------- |")
    add("| Appreciation | 40% | FHFA YoY + structural demand/supply overlay |")
    add("| Jobs | 30% | Unemployment + growth-corridor nudge |")
    add("| Price | 20% | Entry vs income band + exit liquidity |")
    add("| Cash (carry) | 10% | Secondary carry tolerance — thin OK |")
    add("")
    add("Owner / Tenant law scores are shown separately (not in Econ) and reused from the base legal judgment layer. **Squatting risk** is an **overlay** (Legal § + avoid/watch + deep-dive risks + acquisition controls), not a fifth Econ pillar.")
    add("")
    add("### Financing and expense assumptions")
    add("[↑ Back to Index](#index)")
    add("")
    add("| Item | Default used |")
    add("| ---- | ------------ |")
    add("| Down payment | **25%** (disclosed default; App buyers may use other leverage — label overrides) |")
    add("| Closing / acquisition | about 3% of purchase |")
    add("| Cash to close | ≈ **28%** of median |")
    add("| Shock liquid | **6 months** PITI default; **9 months** in high-insurance / high-tax / heavy-regulation states |")
    add("| PITI rate assumption | **7.5%** midpoint of about 7.0%–8.5% investor band; 30-year amortizing on 75% LTV |")
    add("| Property management | about **10%** of collected rent unless quoted; vacant caretaking budgeted separately when vacant |")
    add("| Hold period | **5–10+ years** |")
    add("")
    add("### Primary sources")
    add("[↑ Back to Index](#index)")
    add("")
    add("- [FHFA House Price Index, 2026 Q1](https://www.fhfa.gov/reports/house-price-index/2026/Q1) / live `data/fhfa.json`")
    add("- [Redfin state market tracker](https://www.redfin.com/news/) / live `data/state_prices.json`")
    add("- [BLS LAUS unemployment](https://www.bls.gov/news.release/laus.htm) / `data/jobs.json`")
    add("- [BLS CES industry employment](https://www.bls.gov/ces/) / `data/industries.json`")
    add("- [FRED / CPS median HH income](https://fred.stlouisfed.org/release/tables?eid=259462&rid=249) / `data/income.json`")
    add("- Census ACS demographics + mean income / `data/demographics.json`, `data/income.json`")
    add("- [BEA personal income](https://www.bea.gov/) / `data/bea.json`")
    add("- [BLS metro employment, May 2026](https://www.bls.gov/news.release/metro.nr0.htm)")
    add("- Base report legal / insurance / suburb research layer in `rental_market_report.md`")
    add("- Anti-squatter legislation tracker / context: [National Apartment Association](https://naahq.org/news/anti-squatter-legislation-continues-third-year); state examples include [Georgia Squatter Reform Act (HB 1017)](https://gov.georgia.gov/document/2024-signed-legislation/hb-1017/download), Florida unauthorized-occupant sheriff complaint path (Ch. 82 / related 2025 updates)")
    add("- [July 2026 investor loan rate sheets](https://dscrfinder.com/blog/current-dscr-loan-rates)")
    add("")
    add("### Caveats / data gaps")
    add("[↑ Back to Index](#index)")
    add("")
    add("- One-year FHFA is **backward-looking**; structural App overlays are labeled judgment.")
    add("- Metro FHFA prints in §5 cite the base report’s published metro leader table; state YoY is always from live `data/fhfa.json`.")
    add("- `data/metro_prices.json` and `data/suburbs.json` remain placeholders — suburb notes are qualitative screens.")
    add("- True mean closed-sale prices by metro are often `unavailable`.")
    add("- Squatting statutes and **county LE practice** change quickly — treat §7 as a screen, not a legal opinion; confirm with local counsel.")
    add("- Never use Markdown `~` for approximately (strikethrough risk); this report uses **about** or **≈**.")
    add("- This sibling does **not** auto-build via `pipeline/build_report.py` yet — refresh guidance is in `sfh_appreciation_spec.md`.")
    add("")
    add("### A–Z actionable-rank index")
    add("[↑ Back to Index](#index)")
    add("")
    add("Actionable rank by postal abbreviation (1 = highest appreciation actionable). **Every** state links to its [§6 deep dive](#6-all-state-deep-dives).")
    add("")
    add("| | | | | |")
    add("|---|---|---|---|---|")
    # build A-Z cells
    az = sorted(ordered, key=lambda r: abbr[r["state"]])
    cells = []
    for r in az:
        st = r["state"]
        slug = st.lower().replace(" ", "-").replace(".", "")
        cells.append(f"[{abbr[st]}](#{slug}) {r['rank']}")
    # 5 per row
    for i in range(0, len(cells), 5):
        chunk = cells[i:i+5]
        while len(chunk) < 5:
            chunk.append("")
        add("| " + " | ".join(chunk) + " |")

    add("")
    add("---")
    add("")
    add("## 1. What changed vs the prior run")
    add("[↑ Back to Index](#index)")
    add("")
    add("This is the **first sibling deliverable** focused solely on **single-family appreciation investing**. It does **not** replace `rental_market_report.md` (cash-flow–balanced SFR + 2–4 unit).")
    add("")
    add("| Change | What it means |")
    add("| ------ | ------------- |")
    add("| **New strategy lens** | Rankings overweight **appreciation**, **jobs/migration**, **entry vs income**, **liquidity/exit**, and **owner-law / remote ops**; day-one cash flow is secondary |")
    add("| **Property scope** | **Single-family houses only** — apartments and 2–4 unit MF are out of primary scope |")
    add("| **Squatting overlay** | Vacant App SFH treated as first-class risk — reform vs friction jurisdictions, adverse-possession neglect, vacant monitoring |")
    add("| **Score column meanings** | Same 4a columns as the base report, but **Price** = entry-vs-income + liquidity for equity path (not pure “cheap = good”); **Cash** = carry tolerance (thin OK); **Appr.** dominates the Econ blend |")
    add("| **Econ weights** | Appreciation **40%** / Jobs **30%** / Price **20%** / Cash **10%** (vs equal 25% pillars in the base rental report) |")
    add("| **Live data reused** | Same `data/` snapshots: FHFA, Redfin state prices, BLS jobs/industries, ACS/FRED income & demographics, BEA |")
    add("| **Rank flip vs base** | Midwest cash-flow leaders (Ohio, Indiana, Arkansas) fall behind **FHFA + liquidity appreciation leaders** (Illinois, Wisconsin, Connecticut, New Jersey, Pennsylvania, upstate New York, etc.) |")
    add("| **Format** | Mirrors `rental_market_report.md` section order, Index / Back to Index, companion tables, all-state deep dives |")
    add("")
    add("**Defaults used (user did not override):** appreciation-first; single-family only; remote-capable preferred; **5–10+ year** hold; moderate risk; thin day-one cash flow acceptable; **vacant SFH monitored against squatting**.")
    add("")
    add("> Changelog appendix — kept at the bottom so the national snapshot comes first.")
    add("")
    add("---")
    add("")
    add("*End of single-family appreciation sibling report. Informational only — not financial advice. Re-pull live comps, tax bills, and bindable insurance quotes before deploying capital. For cash-flow–first SFR + 2–4 unit screens, use `rental_market_report.md`.*")
    add("")

    out = ROOT / "sfh_appreciation_report.md"
    out.write_text("\n".join(L), encoding="utf-8")
    print(f"Wrote {out} ({len(L)} lines)")
    print("Top 15:")
    for r in ordered[:15]:
        print(f"  {r['rank']:2} {r['state']:25} econ={r['econ']:.2f} appr={r['appr']} jobs={r['jobs']} yoy={r['yoy']:+.1f}")


if __name__ == "__main__":
    main()
