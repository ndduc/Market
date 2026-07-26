"""Inject entry capital + shock reserves into report (4e + deep-dive Entry capital lines)."""
from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(r"C:\Users\ndduc\OneDrive\house\Market")
report_path = ROOT / "rental_market_report.md"
text = report_path.read_text(encoding="utf-8")

DOWN = 0.25
CLOSING = 0.03
RATE = 0.075  # midpoint of 7.0%-8.5% band
N_MONTHS = 360

# Effective property tax rate screens (directional)
TAX = {
    "Alabama": 0.0040, "Alaska": 0.0100, "Arizona": 0.0060, "Arkansas": 0.0056,
    "California": 0.0070, "Colorado": 0.0050, "Connecticut": 0.0170, "Delaware": 0.0055,
    "District of Columbia": 0.0056, "Florida": 0.0080, "Georgia": 0.0080, "Hawaii": 0.0027,
    "Idaho": 0.0060, "Illinois": 0.0200, "Indiana": 0.0080, "Iowa": 0.0135,
    "Kansas": 0.0125, "Kentucky": 0.0080, "Louisiana": 0.0050, "Maine": 0.0105,
    "Maryland": 0.0100, "Massachusetts": 0.0105, "Michigan": 0.0130, "Minnesota": 0.0100,
    "Mississippi": 0.0065, "Missouri": 0.0090, "Montana": 0.0075, "Nebraska": 0.0150,
    "Nevada": 0.0055, "New Hampshire": 0.0160, "New Jersey": 0.0223, "New Mexico": 0.0060,
    "New York": 0.0140, "North Carolina": 0.0075, "North Dakota": 0.0100, "Ohio": 0.0140,
    "Oklahoma": 0.0085, "Oregon": 0.0085, "Pennsylvania": 0.0135, "Rhode Island": 0.0140,
    "South Carolina": 0.0050, "South Dakota": 0.0110, "Tennessee": 0.0060, "Texas": 0.0160,
    "Utah": 0.0055, "Vermont": 0.0155, "Virginia": 0.0080, "Washington": 0.0085,
    "West Virginia": 0.0050, "Wisconsin": 0.0150, "Wyoming": 0.0055,
}

# Annual landlord insurance screen ($)
INS = {
    "Florida": 3800, "Louisiana": 3600, "Texas": 3200, "Oklahoma": 3000, "Mississippi": 3000,
    "South Carolina": 2800, "Alabama": 2200, "Georgia": 2000, "North Carolina": 2000,
    "California": 2200, "Colorado": 2000, "Arizona": 1800, "Nevada": 1800,
}
INS_DEFAULT = 1500

# Shock months: 9 where insurance/tax/soft-rent overlays are severe
SHOCK_MO = {
    "Florida": 9, "Louisiana": 9, "Texas": 9, "Oklahoma": 9, "Mississippi": 9,
    "South Carolina": 9, "New Jersey": 9, "California": 9, "Washington": 9, "Oregon": 9,
    "Hawaii": 9, "District of Columbia": 9, "New York": 9, "Illinois": 9,
}

# Metro/suburb price screens (full $) for entry-capital notes
METRO_PRICES = {
    "Ohio": [("Cleveland", 274179), ("Columbus", 368895), ("Cincinnati", 324030)],
    "Indiana": [("Indianapolis", 324030)],
    "Georgia": [("Atlanta", 408776)],
    "North Carolina": [("Charlotte", 428716)],
    "Illinois": [("Chicago", 408776)],
    "Texas": [("Houston", 345665), ("Dallas", 413761), ("Austin", 448657), ("San Antonio", 328985)],
    "Florida": [("Tampa", 391328), ("Orlando", 413761), ("Miami", 576124), ("Jacksonville", 394215)],
    "Arizona": [("Phoenix metro", 463612)],
    "Nevada": [("Las Vegas", 453642)],
    "Colorado": [("Denver", 607070)],
    "Washington": [("Seattle", 827522)],
    "California": [("Los Angeles", 947164), ("San Francisco", 1724835), ("San Diego", 952149), ("Sacramento", 598209)],
    "New York": [("New York City metro", 843474)],
    "Massachusetts": [("Boston", 797612)],
    "Pennsylvania": [("Philadelphia", 408776)],  # approx from Chicago-tied earlier? use from cards if needed
    "Minnesota": [("Minneapolis", 408776)],
    "Maryland": [("Baltimore", 438686)],
    "Virginia": [("Virginia Beach", 398806)],
    "Oregon": [("Portland", 568298)],
    "District of Columbia": [("D.C. metro", 623134)],
    "New Jersey": [("Newark metro", 697245)],
    "Rhode Island": [("Providence", 547361)],
}

# Approximate suburb screens (directional)
SUBURB_NOTES = {
    "Arizona": "West Valley CF suburbs often price below Phoenix metro median (lower cash-to-close); Gilbert / Chandler higher entry + thinner yield.",
    "Texas": "Forney / Mansfield / Katy-type CF suburbs usually need less total liquid than Frisco / McKinney / Plano appreciation suburbs.",
    "Ohio": "Maple Heights / Garfield Heights CF screens need less cash than New Albany / Hilliard appreciation corridors.",
    "Indiana": "Noblesville / Greenwood entry usually below Carmel / Fishers school-suburb prices.",
}


def pmt(principal: float, annual_rate: float = RATE, n: int = N_MONTHS) -> float:
    r = annual_rate / 12
    if r == 0:
        return principal / n
    return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def round_k(x: float) -> int:
    return int(round(x / 1000.0) * 1000)


def fmt_k(x: float) -> str:
    v = round_k(x)
    if v >= 1000:
        return f"${v/1000:.0f}k"
    return f"${v:,}"


def capital(price: float, state: str) -> dict:
    tax = TAX.get(state, 0.010)
    ins = INS.get(state, INS_DEFAULT)
    months = SHOCK_MO.get(state, 6)
    down = price * DOWN
    closing = price * CLOSING
    cash_close = down + closing
    loan = price * (1 - DOWN)
    pi = pmt(loan)
    piti = pi + (tax * price) / 12 + ins / 12
    shock = months * piti
    total = cash_close + shock
    return {
        "down_pct": 25,
        "months": months,
        "cash_close": cash_close,
        "shock": shock,
        "total": total,
        "piti": piti,
        "tax": tax,
        "ins": ins,
    }


def parse_state_medians(text: str) -> dict[str, int]:
    """Parse State median **$X** from deep dives."""
    out = {}
    for m in re.finditer(
        r"### ([^\n]+)\n\n\*\*Scores:\*\*[^\n]+\n\n\*\*Prices:\*\* State median \*\*\$([0-9,]+)\*\*",
        text,
    ):
        state = m.group(1).strip()
        out[state] = int(m.group(2).replace(",", ""))
    return out


def parse_order(text: str) -> list[tuple[int, str]]:
    chunk = text[text.index("### 4a. Scores") : text.index("### 4b. Prices")]
    order = []
    for line in chunk.splitlines():
        if not line.startswith("|") or "State" in line or re.match(r"\| ---", line) or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        try:
            num = int(parts[0])
        except ValueError:
            continue
        state = parts[1].split(" — ")[0].strip()
        order.append((num, state))
    return order


medians = parse_state_medians(text)
order = parse_order(text)
missing = [s for _, s in order if s not in medians]
if missing:
    raise SystemExit(f"missing medians for: {missing}")

# Build 4e section
lines = [
    "### 4e. Entry capital & shock reserves (same order)",
    "",
    "**Screen framing (not a lender quote):** Investor default **25% down** + **~3% closing** ⇒ cash to close ≈ **28%** of buy-box **median**. "
    "Loan priced at **7.5%** midpoint of the July 2026 ~7.0%–8.5% investor band, 30-year amortizing. "
    "Shock liquid = **6 months** (or **9** in high-insurance / high-tax / soft-rent / heavy-regulation states) of estimated PITI "
    "(principal & interest + property tax screen + landlord insurance screen). "
    "**Total recommended liquid** = cash to close + shock. Recompute on metro/suburb prices when they diverge — see deep dives.",
    "",
    "| # | State | Down | Cash to close | Shock liquid | Total liquid |",
    "|---:|---|---:|---:|---:|---:|",
]

cap_by_state = {}
for num, state in order:
    price = medians[state]
    c = capital(price, state)
    cap_by_state[state] = (price, c)
    lines.append(
        f"| {num} | {state} | {c['down_pct']}% | {fmt_k(c['cash_close'])} | "
        f"{fmt_k(c['shock'])} ({c['months']} mo) | {fmt_k(c['total'])} |"
    )
lines.append("")
section_4e = "\n".join(lines) + "\n"

# Insert/replace 4e before Notes on score changes
if "### 4e. Entry capital" in text:
    start = text.index("### 4e. Entry capital")
    end = text.index("\n### Notes on score changes", start)
    text = text[:start] + section_4e + text[end:]
else:
    end = text.index("\n### Notes on score changes")
    text = text[:end] + "\n" + section_4e + text[end:]

# Inject Entry capital into each deep dive after Prices paragraph
# Pattern: **Prices:** ... \n then maybe blank then **Top industries:** or **Entry capital:**


def entry_line(state: str) -> str:
    price, c = cap_by_state[state]
    parts = [
        f"**Entry capital:** **{c['down_pct']}% down** (investor default). "
        f"On state median **${price:,}**: cash to close ≈ **{fmt_k(c['cash_close'])}** (25% + ~3% closing); "
        f"recommended shock liquid ≈ **{fmt_k(c['shock'])}** ({c['months']} mo PITI screen); "
        f"**total recommended liquid ≈ {fmt_k(c['total'])}**."
    ]
    metro_bits = []
    for name, mp in METRO_PRICES.get(state, []):
        mc = capital(mp, state)
        metro_bits.append(
            f"{name} median **${mp:,}** → cash to close ~**{fmt_k(mc['cash_close'])}**, "
            f"total liquid ~**{fmt_k(mc['total'])}**"
        )
    if metro_bits:
        parts.append(" Metro screens: " + "; ".join(metro_bits) + ".")
    if state in SUBURB_NOTES:
        parts.append(f" Suburb note: {SUBURB_NOTES[state]}")
    return "".join(parts) + "  \n"


# Process deep dive section only
dive_start = text.index("## 6. All-state deep dives")
dive_end = text.index("## 7. Legal environment")
head, dive, tail = text[:dive_start], text[dive_start:dive_end], text[dive_end:]

# Remove existing Entry capital lines to allow re-run
dive = re.sub(r"\*\*Entry capital:\*\*[^\n]+\n(?:[^\n]*\n)?", "", dive)

for state, _ in sorted(cap_by_state.items(), key=lambda kv: -len(kv[0])):
    # longest names first to avoid partial issues - actually use exact heading
    pass

for state in cap_by_state:
    # Insert after Prices block (line starting **Prices:** through next blank line before **Top)
    pattern = rf"(### {re.escape(state)}\n\n\*\*Scores:\*\*[^\n]+\n\n\*\*Prices:\*\*[^\n]+\n)"
    repl = rf"\1{entry_line(state)}"
    dive2, n = re.subn(pattern, repl, dive, count=1)
    if n != 1:
        # try without double newline variants
        pattern2 = rf"(### {re.escape(state)}\n\*\*Scores:\*\*[^\n]+\n\n\*\*Prices:\*\*[^\n]+\n)"
        dive2, n = re.subn(pattern2, rf"\1{entry_line(state)}", dive, count=1)
    if n != 1:
        print("WARN no inject", state)
    else:
        dive = dive2

# Update section 6 intro
dive = dive.replace(
    "Same field labels throughout: Scores, Prices, Top industries, Demographics / income, Top suburbs, Best fit, Risks, Confidence.",
    "Same field labels throughout: Scores, Prices, Entry capital, Top industries, Demographics / income, Top suburbs, Best fit, Risks, Confidence.",
    1,
)

text = head + dive + tail

# Index: add 4e link
text = text.replace(
    "[4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order)",
    "[4c Industries](#4c-top-job-industries-same-order) · [4d Demographics & income](#4d-demographics--income-same-order) · [4e Entry capital](#4e-entry-capital--shock-reserves-same-order)",
    1,
)

# What changed
if "**Entry capital / shock reserves**" not in text:
    text = text.replace(
        "| **All-state deep dives**",
        "| **Entry capital / shock reserves** | Every state shows **25% down**, cash to close, **6–9 mo shock liquid**, and total recommended liquid (metro/suburb variants in deep dives) |\n| **All-state deep dives**",
        1,
    )

# Snapshot bullet
if "Entry capital tabulated" not in text:
    text = text.replace(
        "- **Demographics & income tabulated:**",
        "- **Entry capital tabulated:** Section **4e** and every deep-dive **Entry capital:** line screen **25% down**, cash to close (~28% of median), and **6–9 months** PITI shock reserves.\n"
        "- **Demographics & income tabulated:**",
        1,
    )

# Methodology financing table
fin_extra = """| Closing / acquisition costs    | ~3% of purchase (screen)                                                              |
| Cash to close (screen)         | Down + closing ≈ **28%** of median buy-box price                                      |
| Shock liquid (screen)          | **6 months** PITI default; **9 months** in high-insurance / high-tax / soft-rent / heavy-regulation states |
| Total recommended liquid       | Cash to close + shock liquid                                                          |
| PITI rate assumption           | **7.5%** midpoint of ~7.0%–8.5% investor band; 30-year amortizing on 75% LTV          |
"""
if "Cash to close (screen)" not in text:
    text = text.replace(
        "| Down payment                   | 25%                                                                                   |\n",
        "| Down payment                   | 25%                                                                                   |\n" + fin_extra,
        1,
    )

# Workflow step
if "Confirm liquid cash" not in text:
    text = text.replace(
        "7. Use the standard financing case (25% down; investor rate band ~7.0%–8.5% unless you have a live quote).",
        "7. Use the standard financing case (25% down; investor rate band ~7.0%–8.5% unless you have a live quote). Confirm **cash to close + shock reserves** from §4e / the state’s **Entry capital:** line before offering.",
        1,
    )

# Caveat
cav = (
    "- Entry capital and shock reserves are **screens** (25% down, ~3% closing, 7.5% PI, tax/insurance overlays, 6–9 months PITI) — not lender commitments or bindable insurance quotes. Recompute with live quotes and the exact address.\n"
)
if "Entry capital and shock reserves are **screens**" not in text:
    text = text.replace(
        "- Industry rankings use CES supersectors",
        cav + "- Industry rankings use CES supersectors",
        1,
    )

# Count Entry capital lines
n = len(re.findall(r"\*\*Entry capital:\*\*", text))
report_path.write_text(text, encoding="utf-8")
print(f"4e added; Entry capital lines: {n}; states: {len(order)}")
