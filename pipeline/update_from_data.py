"""
Propagate live data/ into report sections beyond companion tables 4b–4d.

Updates:
  - Deep-dive **Prices:** state median / typical from Redfin
  - Deep-dive **Entry capital:** + §4e from new medians (same financing screen)
  - Narrative unemployment + FHFA YoY where patterned
  - §1 What changed + §2 national snapshot bullets

Usage:
  python -m pipeline.update_from_data
  (also invoked at end of pipeline.build_report)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from pipeline import config

DOWN = 0.25
CLOSING = 0.03
RATE = 0.075
N_MONTHS = 360

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
INS = {
    "Florida": 3800, "Louisiana": 3600, "Texas": 3200, "Oklahoma": 3000, "Mississippi": 3000,
    "South Carolina": 2800, "Alabama": 2200, "Georgia": 2000, "North Carolina": 2000,
    "California": 2200, "Colorado": 2000, "Arizona": 1800, "Nevada": 1800,
}
INS_DEFAULT = 1500
SHOCK_MO = {
    "Florida": 9, "Louisiana": 9, "Texas": 9, "Oklahoma": 9, "Mississippi": 9,
    "South Carolina": 9, "New Jersey": 9, "California": 9, "Washington": 9, "Oregon": 9,
    "Hawaii": 9, "District of Columbia": 9, "New York": 9, "Illinois": 9,
}

# Keep prior metro price screens for entry-capital notes (not in state_prices.json yet)
METRO_PRICES: dict[str, list[tuple[str, int]]] = {
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
    "California": [
        ("Los Angeles", 947164),
        ("San Francisco", 1724835),
        ("San Diego", 952149),
        ("Sacramento", 598209),
    ],
    "New York": [("New York City metro", 843474)],
    "Massachusetts": [("Boston", 797612)],
    "Pennsylvania": [("Philadelphia", 337988), ("Pittsburgh", 291527)],
    "Minnesota": [("Minneapolis", 408776)],
    "Maryland": [("Baltimore", 438686)],
    "Virginia": [("Virginia Beach", 398806)],
    "Oregon": [("Portland", 568298)],
    "District of Columbia": [("D.C. metro", 623134)],
    "New Jersey": [("Newark metro", 697245)],
    "Rhode Island": [("Providence", 547361)],
    "Michigan": [("Detroit city screen", 85000)],
    "Wisconsin": [("Milwaukee", 378866)],
    "Tennessee": [("Nashville", 498507)],
}
SUBURB_NOTES = {
    "Arizona": "West Valley CF suburbs often price below Phoenix metro median (lower cash-to-close); Gilbert / Chandler higher entry + thinner yield.",
    "Texas": "Forney / Mansfield / Katy-type CF suburbs usually need less total liquid than Frisco / McKinney / Plano appreciation suburbs.",
    "Ohio": "Maple Heights / Garfield Heights CF screens need less cash than New Albany / Hilliard appreciation corridors.",
    "Indiana": "Noblesville / Greenwood entry usually below Carmel / Fishers school-suburb prices.",
}


def _load(name: str) -> dict[str, Any]:
    path = config.DATA_FILES.get(name)
    if not path or not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


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
        return f"${v / 1000:.0f}k"
    return f"${v:,}"


def fmt_full(n: int) -> str:
    return f"${n:,}"


def capital(price: float, state: str) -> dict[str, Any]:
    tax = TAX.get(state, 0.010)
    ins = INS.get(state, INS_DEFAULT)
    months = SHOCK_MO.get(state, 6)
    cash_close = price * (DOWN + CLOSING)
    loan = price * (1 - DOWN)
    pi = pmt(loan)
    piti = pi + (tax * price) / 12 + ins / 12
    shock = months * piti
    return {
        "down_pct": 25,
        "months": months,
        "cash_close": cash_close,
        "shock": shock,
        "total": cash_close + shock,
    }


def parse_order(report: str) -> list[tuple[str, str]]:
    a_start = report.index("### 4a. Scores")
    a_end = report.index("### 4b. Prices")
    order: list[tuple[str, str]] = []
    for line in report[a_start:a_end].splitlines():
        if not line.startswith("|") or "State" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2 or not parts[0].isdigit():
            continue
        state = parts[1].split(" — ")[0].strip()
        order.append((parts[0], state))
    return order


def patch_deep_dive_prices(report: str, prices: dict) -> str:
    states = prices.get("states") or {}
    as_of = prices.get("as_of") or "Redfin"
    if not states:
        return report

    pattern = re.compile(
        r"(### ([A-Za-z .]+)\n(?:\[↑ Back to Index\]\(#index\)\n+)?\*\*Scores:\*\*[^\n]+\n+\*\*Prices:\*\* )"
        r"State median \*\*\$[0-9,]+\*\* / typical (?:\*\*\$[0-9,]+\*\*|`unavailable`)"
        r"([^\n]*)",
        re.MULTILINE,
    )

    def repl(m: re.Match[str]) -> str:
        prefix, state, rest = m.group(1), m.group(2).strip(), m.group(3) or ""
        row = states.get(state)
        if not row or not row.get("median_sale_price"):
            return m.group(0)
        med = int(row["median_sale_price"])
        typ = row.get("typical_home_value")
        if typ:
            mid = (
                f"State median **{fmt_full(med)}** / typical **{fmt_full(int(typ))}**"
                f" (Redfin All Residential, {as_of})"
            )
        else:
            mid = (
                f"State median **{fmt_full(med)}** / typical `unavailable`"
                f" (Redfin All Residential median, {as_of})"
            )
        # Preserve metro clause after first period if present
        if "." in rest:
            # drop old leading measure labels before first period? keep from first period
            metro = rest[rest.index(".") :]
            # avoid duplicating "(Redfin..." if rest already had period-only metros
            if metro.startswith(".") and "Redfin" in metro[:40]:
                # strip old parenthetical before metros if any
                pass
            return f"{prefix}{mid}{metro}"
        if rest.strip():
            return f"{prefix}{mid}. {rest.strip().lstrip('. ')}"
        return f"{prefix}{mid}."

    out, n = pattern.subn(repl, report)
    print(f"patched {n} deep-dive Prices lines from Redfin")
    return out


def build_entry_line(state: str, price: int) -> str:
    c = capital(price, state)
    parts = [
        f"**Entry capital:** **{c['down_pct']}% down** (investor default). "
        f"On state median **{fmt_full(price)}**: cash to close ≈ **{fmt_k(c['cash_close'])}** "
        f"(25% + about 3% closing); recommended shock liquid ≈ **{fmt_k(c['shock'])}** "
        f"({c['months']} mo PITI screen); **total recommended liquid ≈ {fmt_k(c['total'])}**."
    ]
    metro_bits = []
    for name, mp in METRO_PRICES.get(state, []):
        mc = capital(mp, state)
        metro_bits.append(
            f"{name} median **{fmt_full(mp)}** → cash to close about **{fmt_k(mc['cash_close'])}**, "
            f"total liquid about **{fmt_k(mc['total'])}**"
        )
    if metro_bits:
        parts.append(" Metro screens: " + "; ".join(metro_bits) + ".")
    if state in SUBURB_NOTES:
        parts.append(f" Suburb note: {SUBURB_NOTES[state]}")
    return "".join(parts)


def rebuild_entry_capital(report: str, order: list[tuple[str, str]], prices: dict) -> str:
    states = prices.get("states") or {}
    # Prefer Redfin; fall back to parsing existing Prices if missing (e.g. D.C.)
    medians: dict[str, int] = {}
    for _, state in order:
        row = states.get(state) or {}
        if row.get("median_sale_price"):
            medians[state] = int(row["median_sale_price"])
    # Fallback parse for missing (DC)
    for m in re.finditer(
        r"### ([^\n]+)\n(?:\[↑ Back to Index\]\(#index\)\n+)?"
        r"\*\*Scores:\*\*[^\n]+\n+\*\*Prices:\*\* State median \*\*\$([0-9,]+)\*\*",
        report,
    ):
        state = m.group(1).strip()
        if state not in medians:
            medians[state] = int(m.group(2).replace(",", ""))

    lines = [
        "### 4e. Entry capital & shock reserves (same order)",
        "",
        "**Screen framing (not a lender quote):** Investor default **25% down** + about **3% closing** "
        "⇒ cash to close ≈ **28%** of buy-box **median** (Redfin All Residential this run when available). "
        "Loan priced at **7.5%** midpoint of the July 2026 about 7.0%–8.5% investor band, 30-year amortizing. "
        "Shock liquid = **6 months** (or **9** in high-insurance / high-tax / soft-rent / heavy-regulation states) "
        "of estimated PITI. **Total recommended liquid** = cash to close + shock. "
        "Metro/suburb variants in deep dives.",
        "",
        "| # | State | Down | Cash to close | Shock liquid | Total liquid |",
        "|---:|---|---:|---:|---:|---:|",
    ]
    for num, state in order:
        price = medians.get(state)
        if not price:
            lines.append(f"| {num} | {state} | 25% | `unavailable` | `unavailable` | `unavailable` |")
            continue
        c = capital(price, state)
        lines.append(
            f"| {num} | {state} | {c['down_pct']}% | {fmt_k(c['cash_close'])} | "
            f"{fmt_k(c['shock'])} ({c['months']} mo) | {fmt_k(c['total'])} |"
        )
    lines.append("")
    section_4e = "\n".join(lines) + "\n"

    if "### 4e. Entry capital" in report:
        start = report.index("### 4e. Entry capital")
        end = report.index("\n### Notes on score changes", start)
        report = report[:start] + section_4e + report[end:]
    else:
        end = report.index("\n### Notes on score changes")
        report = report[:end] + "\n" + section_4e + report[end:]

    # Replace each deep-dive Entry capital line
    dive_start = report.index("## 6. All-state deep dives")
    dive_end = report.index("## 7. Legal environment")
    head, dive, tail = report[:dive_start], report[dive_start:dive_end], report[dive_end:]
    dive = re.sub(r"\*\*Entry capital:\*\*[^\n]*\n?", "", dive)

    n = 0
    for state in medians:
        price = medians[state]
        line = build_entry_line(state, price)
        pattern = (
            rf"(### {re.escape(state)}\n(?:\[↑ Back to Index\]\(#index\)\n+)?"
            rf"\*\*Scores:\*\*[^\n]+\n+\*\*Prices:\*\*[^\n]+\n)"
        )
        dive2, count = re.subn(pattern, rf"\1{line}\n", dive, count=1)
        if count == 1:
            dive = dive2
            n += 1
        else:
            print(f"WARNING: could not insert Entry capital for {state}")
    print(f"rebuilt §4e and {n} deep-dive Entry capital lines")
    return head + dive + tail


def patch_narrative_jobs_appr(report: str, jobs: dict, fhfa: dict) -> str:
    """Refresh common 'Unemployment X%; ... appreciation about +Y%' lead sentences."""
    job_states = jobs.get("states") or {}
    fhfa_states = fhfa.get("states") or {}
    if not job_states and not fhfa_states:
        return report

    dive_start = report.index("## 6. All-state deep dives")
    dive_end = report.index("## 7. Legal environment")
    head, dive, tail = report[:dive_start], report[dive_start:dive_end], report[dive_end:]

    heading_re = re.compile(r"^### ([A-Za-z .]+)\s*$", re.MULTILINE)
    headings = [(m.start(), m.group(1).strip()) for m in heading_re.finditer(dive)]

    def state_at(pos: int) -> str | None:
        name = None
        for start, label in headings:
            if start > pos:
                break
            name = label
        return name

    # Pattern A: "Unemployment 3.3%; statewide appreciation about +3.6%."
    pat_a = re.compile(
        r"Unemployment (\d+\.\d+)%; statewide appreciation about \+[0-9.]+%\."
    )
    # Pattern B: "Unemployment fell from X% to Y% ... Statewide appreciation about +Z%;"
    pat_b = re.compile(
        r"Unemployment fell from \d+\.\d+% to \d+\.\d+%[^.]*\.\s*"
        r"([\s\S]*?)Statewide appreciation about \+[0-9.]+%;"
    )

    out: list[str] = []
    last = 0
    n = 0
    for m in pat_a.finditer(dive):
        state = state_at(m.start())
        if not state:
            continue
        ur = (job_states.get(state) or {}).get("unemployment_rate")
        yoy = (fhfa_states.get(state) or {}).get("yoy_pct")
        if ur is None and yoy is None:
            continue
        ur_txt = f"{ur:.1f}" if ur is not None else m.group(1)
        yoy_txt = f"{yoy:+.1f}%" if yoy is not None else m.group(0).split("about ")[-1].rstrip(".")
        if not yoy_txt.startswith("+") and not yoy_txt.startswith("-") and yoy is not None:
            yoy_txt = f"{yoy:+.1f}%"
        replacement = f"Unemployment {ur_txt}% (BLS LAUS); statewide appreciation {yoy_txt} (FHFA PO HPI)."
        out.append(dive[last : m.start()])
        out.append(replacement)
        last = m.end()
        n += 1
    dive = "".join(out) + dive[last:] if out else dive

    n_box = [0]

    def repl_b(m: re.Match[str]) -> str:
        state = state_at(m.start())
        if not state:
            return m.group(0)
        ur = (job_states.get(state) or {}).get("unemployment_rate")
        yoy = (fhfa_states.get(state) or {}).get("yoy_pct")
        mid = m.group(1)
        if ur is None or yoy is None:
            return m.group(0)
        n_box[0] += 1
        return (
            f"Unemployment {ur:.1f}% (BLS LAUS, latest). {mid}"
            f"Statewide appreciation {yoy:+.1f}% (FHFA PO HPI);"
        )

    dive, n_b = pat_b.subn(repl_b, dive)
    print(f"patched {n + n_b + n_box[0]} deep-dive unemployment/appreciation narrative leads")
    return head + dive + tail


def patch_what_changed(report: str) -> str:
    rows = {
        "**Demographics & income**": (
            "| **Demographics & income** | Live **Census ACS** race + mean HH income; "
            "**FRED/CPS** median HH income; BEA per-capita personal income in `data/bea.json` |"
        ),
        "**Top job industries**": (
            "| **Top job industries** | Live **BLS CES SAE** supersector shares every refresh (API) |"
        ),
        "**Prices in context**": (
            "| **Prices in context** | Live **Redfin** state medians + **FHFA** YoY in §4b; "
            "deep-dive Prices/Entry capital rebuilt from same medians |"
        ),
    }
    for key, new_row in rows.items():
        report = re.sub(
            rf"\| {re.escape(key)} \|[^\n]+\|",
            new_row,
            report,
            count=1,
        )
    # Ensure a live-fetch row exists
    if "| **Live APIs this run** |" not in report:
        report = report.replace(
            "| **Durable pipeline** |",
            "| **Live APIs this run** | Census + FRED + BLS + BEA keys; no-key FHFA HPI + Redfin state tracker |\n"
            "| **Durable pipeline** |",
            1,
        )
    return report


def patch_national_snapshot(report: str, jobs: dict, fhfa: dict, prices: dict, income: dict, bea: dict) -> str:
    job_states = jobs.get("states") or {}
    if job_states:
        urs = [(s, d["unemployment_rate"]) for s, d in job_states.items() if "unemployment_rate" in d]
        if urs:
            lo_s, lo_v = min(urs, key=lambda x: x[1])
            hi_s, hi_v = max(urs, key=lambda x: x[1])
            as_of = next(iter(job_states.values())).get("as_of", "latest")
            # Approximate US rate as mean of states (directional) — better: leave national if unknown
            us_approx = sum(v for _, v in urs) / len(urs)
            bullet = (
                f"- State unemployment (BLS LAUS, {as_of}): lowest **{lo_s} {lo_v:.1f}%**, "
                f"highest **{hi_s} {hi_v:.1f}%**; unweighted state mean about **{us_approx:.1f}%** "
                f"([Bureau of Labor Statistics](https://www.bls.gov/news.release/laus.htm))."
            )
            report = re.sub(
                r"- U\.S\. unemployment was[^\n]+",
                bullet,
                report,
                count=1,
            )
            report = re.sub(
                r"- State unemployment \(BLS LAUS[^\n]+",
                bullet,
                report,
                count=1,
            )

    fhfa_states = fhfa.get("states") or {}
    if fhfa_states:
        yoys = [d["yoy_pct"] for d in fhfa_states.values() if d.get("yoy_pct") is not None]
        if yoys:
            as_of = next(iter(fhfa_states.values())).get("as_of", "latest")
            bullet = (
                f"- FHFA purchase-only HPI YoY ({as_of}): state range "
                f"**{min(yoys):+.1f}%** to **{max(yoys):+.1f}%**; "
                f"median state about **{sorted(yoys)[len(yoys)//2]:+.1f}%** "
                f"([FHFA HPI](https://www.fhfa.gov/data/hpi/datasets))."
            )
            if "- FHFA purchase-only HPI YoY" in report:
                report = re.sub(r"- FHFA purchase-only HPI YoY[^\n]+", bullet, report, count=1)
            else:
                report = report.replace(
                    "- National house prices rose",
                    bullet + "\n- National house prices rose",
                    1,
                )

    if prices.get("states"):
        as_of = prices.get("as_of", "latest")
        meds = [d["median_sale_price"] for d in prices["states"].values() if d.get("median_sale_price")]
        if meds:
            bullet = (
                f"- **State prices (live):** Redfin All Residential medians as of **{as_of}** "
                f"in §4b / deep dives (state median range about "
                f"**${min(meds)/1000:.0f}k–${max(meds)/1000:.0f}k**). "
                "Typical column uses Redfin median list when present."
            )
            report = re.sub(
                r"- \*\*State prices are in the ranking matrix:\*\*[^\n]+",
                bullet,
                report,
                count=1,
            )
            report = re.sub(
                r"- \*\*State prices \(live\):\*\*[^\n]+",
                bullet,
                report,
                count=1,
            )

    means = income.get("mean_household_income") or {}
    if means and income.get("mean_status") not in (None, "unavailable"):
        bullet = (
            "- **Demographics & income tabulated:** §4d lists race/ethnicity (ACS), "
            "median HH income (CPS/FRED), and **mean HH income (ACS S1901)** for every state + D.C."
        )
        report = re.sub(
            r"- \*\*Demographics & income tabulated:\*\*[^\n]+",
            bullet,
            report,
            count=1,
        )

    pc = bea.get("per_capita_personal_income") or {}
    if pc:
        vals = list(pc.values())
        bullet = (
            f"- **BEA per-capita personal income ({bea.get('year', 'latest')}):** "
            f"state range about **${min(vals)/1000:.0f}k–${max(vals)/1000:.0f}k** "
            f"(stored in `data/bea.json`; demand-capacity context, not a ranking filter)."
        )
        if "- **BEA per-capita personal income" in report:
            report = re.sub(r"- \*\*BEA per-capita personal income[^\n]+", bullet, report, count=1)
        else:
            report = report.replace(
                "- **Demographics & income tabulated:**",
                bullet + "\n- **Demographics & income tabulated:**",
                1,
            )
    return report


def update_report(report: str | None = None) -> str:
    report = report if report is not None else config.REPORT_PATH.read_text(encoding="utf-8")
    order = parse_order(report)
    prices = _load("state_prices")
    jobs = _load("jobs")
    fhfa = _load("fhfa")
    income = _load("income")
    bea = _load("bea")

    report = patch_deep_dive_prices(report, prices)
    report = rebuild_entry_capital(report, order, prices)
    report = patch_narrative_jobs_appr(report, jobs, fhfa)
    report = patch_what_changed(report)
    report = patch_national_snapshot(report, jobs, fhfa, prices, income, bea)
    return report


def main() -> int:
    if str(config.ROOT) not in sys.path:
        sys.path.insert(0, str(config.ROOT))
    report = update_report()
    config.REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"updated {config.REPORT_PATH.name} from live data/ (prices, capital, narratives, snapshot)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
