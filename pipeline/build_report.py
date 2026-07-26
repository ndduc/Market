"""
Build companion tables into rental_market_report.md from data/ JSON.

Does NOT invent statistics. Only renders fields present in this run's data/.
Requires a prior live fetch (pipeline.fetch_all) on the same refresh.

Usage:
  python -m pipeline.build_report
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pipeline import config


def _load(name: str) -> dict[str, Any]:
    path = config.DATA_FILES[name]
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _fmt_income(n: Any) -> str:
    try:
        v = int(n)
    except (TypeError, ValueError):
        return "`unavailable`"
    return f"${v/1000:.0f}k"


def _replace_section(report: str, heading: str, next_heading: str, new_body: str) -> str:
    """Replace from heading through (not including) next_heading."""
    start = report.find(heading)
    if start < 0:
        # insert before next_heading
        nxt = report.find(next_heading)
        if nxt < 0:
            return report + "\n" + new_body
        return report[:nxt] + new_body + report[nxt:]
    end = report.find(next_heading, start + len(heading))
    if end < 0:
        return report[:start] + new_body
    return report[:start] + new_body + report[end:]


def build_4d(order: list[tuple[str, str]], income: dict, demo: dict) -> str:
    medians = income.get("median_household_income") or {}
    if len(medians) < 40:
        medians = {
            k: v
            for k, v in (income.get("census_acs_median_alt") or {}).items()
            if k != "Puerto Rico"
        }
    means = income.get("mean_household_income") or {}
    mean_status = income.get("mean_status", "unavailable")
    races = demo.get("states") or {}

    lines = [
        "### 4d. Demographics & income (same order)",
        "",
        "**Source framing:** Built from this run’s live `data/income.json` and `data/demographics.json` "
        f"(pulled_at income={income.get('pulled_at', 'n/a')}, demographics={demo.get('pulled_at', 'n/a')}). "
        f"Median source: {income.get('median_source', 'see data/sources.json')}. "
        f"Mean status: **{mean_status}**. "
        "Race rows use live ACS/`display` fields when present; otherwise `unavailable` "
        "(spec: no silent stale reuse). "
        "Demographics are tenant-pool / demand context only - not a ranking filter.",
        "",
        "| # | State | Race / ethnicity (top groups) | Median HH income | Mean HH income |",
        "|---:|---|---|---:|---|",
    ]
    for num, state in order:
        med = _fmt_income(medians.get(state)) if state in medians else "`unavailable`"
        if state in means and means[state] is not None:
            mean = _fmt_income(means[state])
        else:
            mean = "`unavailable`"
        r = races.get(state)
        if isinstance(r, dict) and r.get("display"):
            race_line = r["display"]
        elif isinstance(r, dict) and r.get("white_alone_pct") is not None:
            race_line = (
                f"White {r.get('white_alone_pct')}% · Black {r.get('black_alone_pct')}% · "
                f"Hisp {r.get('hispanic_any_race_pct')}% · Asian {r.get('asian_alone_pct')}%"
            )
        else:
            race_line = "`unavailable`"
        lines.append(f"| {num} | {state} | {race_line} | {med} | {mean} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def _demo_income_prefix(state: str, income: dict, demo: dict) -> str | None:
    medians = income.get("median_household_income") or {}
    if state not in medians:
        alt = income.get("census_acs_median_alt") or {}
        if state not in alt:
            return None
        med = alt[state]
    else:
        med = medians[state]
    means = income.get("mean_household_income") or {}
    if state in means and means[state] is not None:
        mean_txt = _fmt_income(means[state])
    else:
        mean_txt = "`unavailable`"
    as_of = income.get("median_as_of") or "ACS"
    r = (demo.get("states") or {}).get(state) or {}
    if r.get("display"):
        race_line = r["display"]
    elif r.get("white_alone_pct") is not None:
        race_line = (
            f"White alone {r.get('white_alone_pct')}% · Black {r.get('black_alone_pct')}% · "
            f"Hisp {r.get('hispanic_any_race_pct')}% · Asian {r.get('asian_alone_pct')}%"
        )
    else:
        race_line = "`unavailable`"
    return (
        f"**Demographics / income:** {race_line}. "
        f"State median HH income **{_fmt_income(med)}** ({as_of}); "
        f"mean HH income {mean_txt}."
    )


def patch_deep_dive_demographics(report: str, income: dict, demo: dict) -> str:
    """Refresh state-level race/income lead-in on every deep dive; keep metro narrative after."""
    # Match **Demographics / income:** ... through mean HH income ... .
    pattern = re.compile(
        r"(\*\*Demographics / income:\*\*.*?mean HH income (?:`unavailable`|\$[\d.]+k)\.)",
        re.DOTALL,
    )
    # Find which state section each match belongs to by scanning headings before it
    heading_re = re.compile(r"^### ([A-Za-z .]+)\s*$", re.MULTILINE)
    headings = [(m.start(), m.group(1).strip()) for m in heading_re.finditer(report)]

    def state_at(pos: int) -> str | None:
        name = None
        for start, label in headings:
            if start > pos:
                break
            name = label
        return name

    out = []
    last = 0
    n = 0
    for m in pattern.finditer(report):
        state = state_at(m.start())
        if not state:
            continue
        # Skip non-state headings that might match ### pattern
        replacement = _demo_income_prefix(state, income, demo)
        if not replacement:
            continue
        out.append(report[last : m.start()])
        out.append(replacement)
        last = m.end()
        n += 1
    out.append(report[last:])
    print(f"patched {n} deep-dive Demographics / income lead-ins")
    return "".join(out)


def _fmt_price(n: Any) -> str:
    try:
        v = int(n)
    except (TypeError, ValueError):
        return "`unavailable`"
    if v >= 1000:
        return f"${v/1000:.0f}k"
    return f"${v}"


def build_4b(order: list[tuple[str, str]], prices: dict, prior_metros: dict[str, str], fhfa: dict) -> str:
    states = prices.get("states") or {}
    fhfa_states = fhfa.get("states") or {}
    as_of = prices.get("as_of") or "n/a"
    lines = [
        "### 4b. Prices & major metros (same order)",
        "",
        f"**Median** = Redfin All Residential median sale price (live `{as_of}`). "
        "**Typical** = Redfin median list price when present in the tracker, else `unavailable` "
        "(do not invent Zillow ZHVI here). "
        "**FHFA YoY** = purchase-only House Price Index seasonally adjusted, same-quarter year-ago % "
        f"(source file as of this run). Major metros column preserved from prior research.",
        "",
        "| # | State | Median | Typical | FHFA YoY | Major metros / cities |",
        "|---:|---|---:|---:|---:|---|",
    ]
    for num, state in order:
        row = states.get(state) or {}
        med = _fmt_price(row.get("median_sale_price")) if row.get("median_sale_price") else "`unavailable`"
        typ = (
            _fmt_price(row.get("typical_home_value"))
            if row.get("typical_home_value")
            else "`unavailable`"
        )
        yoy = fhfa_states.get(state, {}).get("yoy_pct")
        yoy_txt = f"{yoy:+.1f}%" if isinstance(yoy, (int, float)) else "`unavailable`"
        metros = prior_metros.get(state) or "`unavailable`"
        lines.append(f"| {num} | {state} | {med} | {typ} | {yoy_txt} | {metros} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def parse_4b_metros(report: str) -> dict[str, str]:
    try:
        start = report.index("### 4b. Prices")
        end = report.index("### 4c. Top job industries")
    except ValueError:
        return {}
    metros: dict[str, str] = {}
    for line in report[start:end].splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4 or not parts[0].isdigit():
            continue
        # old: # State Median Typical Metros
        # new may already have FHFA column
        state = parts[1]
        metros[state] = parts[-1]
    return metros


def build_4c(order: list[tuple[str, str]], industries: dict, prior_notes: dict[str, str]) -> str:
    states = industries.get("states") or {}
    lines = [
        "### 4c. Top job industries (same order)",
        "",
        "**Source framing:** Built from this run’s live `data/industries.json` "
        f"(pulled_at={industries.get('pulled_at', 'n/a')}; "
        f"source={industries.get('source', 'BLS CES SAE')}). "
        "Sectors are CES supersectors ranked by share of statewide total nonfarm employment "
        "(largest →). Exact headcount shares revise with each BLS release.",
        "",
        "| # | State | Top industries (largest →) | Concentration / renter note |",
        "|---:|---|---|---|",
    ]
    for num, state in order:
        row = states.get(state) or {}
        top = row.get("top") or []
        if top:
            ind_txt = "; ".join((t.get("label") or "").lower() for t in top)
            lead = top[0]
            note = prior_notes.get(state) or (
                f"Largest share: {lead.get('label')} (~{lead.get('share_pct')}% of nonfarm); "
                f"as of {row.get('as_of', 'n/a')}"
            )
        else:
            ind_txt = "`unavailable`"
            note = prior_notes.get(state) or "`unavailable` this run"
        lines.append(f"| {num} | {state} | {ind_txt} | {note} |")
    lines.append("")
    return "\n".join(lines) + "\n"


def parse_4c_notes(report: str) -> dict[str, str]:
    """Preserve prior concentration notes when rebuilding industries."""
    try:
        start = report.index("### 4c. Top job industries")
        end = report.index("### 4d. Demographics")
    except ValueError:
        return {}
    notes: dict[str, str] = {}
    for line in report[start:end].splitlines():
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 4 or not parts[0].isdigit():
            continue
        notes[parts[1]] = parts[3]
    return notes


def patch_deep_dive_industries(report: str, industries: dict) -> str:
    states = industries.get("states") or {}
    if not states:
        return report
    pattern = re.compile(r"(\*\*Top industries:\*\*[^\n]*)")
    heading_re = re.compile(r"^### ([A-Za-z .]+)\s*$", re.MULTILINE)
    headings = [(m.start(), m.group(1).strip()) for m in heading_re.finditer(report)]

    def state_at(pos: int) -> str | None:
        name = None
        for start, label in headings:
            if start > pos:
                break
            name = label
        return name

    out = []
    last = 0
    n = 0
    for m in pattern.finditer(report):
        state = state_at(m.start())
        row = states.get(state or "")
        if not row or not row.get("display"):
            continue
        as_of = row.get("as_of") or "BLS CES"
        replacement = f"**Top industries:** {row['display']} (BLS CES SAE {as_of})."
        out.append(report[last : m.start()])
        out.append(replacement)
        last = m.end()
        n += 1
    out.append(report[last:])
    print(f"patched {n} deep-dive Top industries lines")
    return "".join(out)


def parse_order_from_4a(report: str) -> list[tuple[str, str]]:
    a_start = report.index("### 4a. Scores")
    a_end = report.index("### 4b. Prices")
    order: list[tuple[str, str]] = []
    for line in report[a_start:a_end].splitlines():
        if not line.startswith("|") or "State" in line:
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        num, state_label = parts[0], parts[1]
        if not num.isdigit() or set(state_label) <= {"-", "—", " "}:
            continue
        state = state_label.split(" — ")[0].strip()
        order.append((num, state))
    return order


def patch_methodology(report: str, meta: dict) -> str:
    stamp = meta.get("analysis_run_at") or datetime.now(timezone.utc).isoformat()
    note = (
        f"- **Pipeline live fetch:** `data/meta.json` analysis_run_at **{stamp}**; "
        f"census_api_key_present={meta.get('census_api_key_present')}; "
        f"fred_api_key_present={meta.get('fred_api_key_present')}; "
        f"bls_api_key_present={meta.get('bls_api_key_present')}; "
        f"bea_api_key_present={meta.get('bea_api_key_present')}; "
        "tabular fields regenerated from overwritten `data/` (no cache-as-current).\n"
    )
    marker = "### Confirmation of live research"
    if marker not in report:
        return report
    # Insert after the confirmation paragraph
    idx = report.index(marker)
    # find end of first paragraph after heading
    para_end = report.find("\n\n", idx)
    if para_end < 0:
        return report
    insert_at = para_end + 2
    if "Pipeline live fetch:" in report:
        report = re.sub(
            r"- \*\*Pipeline live fetch:\*\*.*\n",
            note,
            report,
            count=1,
        )
        return report
    return report[:insert_at] + note + report[insert_at:]


def main() -> int:
    if str(config.ROOT) not in sys.path:
        sys.path.insert(0, str(config.ROOT))

    meta = _load("meta")
    if not meta:
        print("ERROR: data/meta.json missing - run `python -m pipeline.fetch_all` first (live every time).")
        return 1
    if not meta.get("live_fetch_required", True):
        print("WARNING: meta missing live_fetch_required flag")

    report_path = config.REPORT_PATH
    if not report_path.exists():
        print(f"ERROR: missing {report_path}")
        return 1

    report = report_path.read_text(encoding="utf-8")
    order = parse_order_from_4a(report)
    income = _load("income")
    demo = _load("demographics")
    industries = _load("industries")
    prices = _load("state_prices")
    fhfa = _load("fhfa")

    medians = income.get("median_household_income") or {}
    if len(medians) < 40:
        medians = {
            k: v
            for k, v in (income.get("census_acs_median_alt") or {}).items()
            if k != "Puerto Rico"
        }
        income = {**income, "median_household_income": medians}
    n_med = len(medians)
    if n_med < 40:
        print(
            f"ERROR: refusing to overwrite §4d - only {n_med} median incomes in data/income.json. "
            "Re-run a successful live fetch (or recovery) so the report is not wiped to unavailable."
        )
        return 2

    n_price = len(prices.get("states") or {})
    if n_price >= 40:
        prior_metros = parse_4b_metros(report)
        section_4b = build_4b(order, prices, prior_metros, fhfa)
        report = _replace_section(
            report,
            "### 4b. Prices & major metros (same order)",
            "\n### 4c. Top job industries (same order)",
            section_4b,
        )
    else:
        print(f"WARNING: skipping §4b rebuild - only {n_price} price rows in data/state_prices.json")

    n_ind = len(industries.get("states") or {})
    if n_ind >= 40:
        prior_notes = parse_4c_notes(report)
        section_4c = build_4c(order, industries, prior_notes)
        report = _replace_section(
            report,
            "### 4c. Top job industries (same order)",
            "\n### 4d. Demographics & income (same order)",
            section_4c,
        )
        report = patch_deep_dive_industries(report, industries)
    else:
        print(f"WARNING: skipping §4c rebuild - only {n_ind} industry rows in data/industries.json")

    section_4d = build_4d(order, income, demo)
    report = _replace_section(
        report,
        "### 4d. Demographics & income (same order)",
        "\n### Notes on score changes",
        section_4d,
    )
    report = patch_deep_dive_demographics(report, income, demo)
    report = patch_methodology(report, meta)

    # Propagate prices / entry capital / narratives / snapshot from data/
    try:
        from pipeline.update_from_data import update_report

        report = update_report(report)
    except Exception as exc:  # noqa: BLE001 - keep companion tables even if expand fails
        print(f"WARNING: update_from_data failed: {exc}")

    # Touch what-changed if pipeline row missing
    if "**Durable pipeline**" not in report and "| **Demographics & income** |" in report:
        report = report.replace(
            "| **Demographics & income** |",
            "| **Durable pipeline** | Full refreshes must **live-fetch → overwrite `data/` → build** (no disposable `_add_*.py` patch scripts) |\n"
            "| **Demographics & income** |",
            1,
        )

    report_path.write_text(report, encoding="utf-8")
    print(f"updated {report_path.name} companion tables from live data/")
    print("Narrative scores / top-10 still require analyst/AI judgment pass after fetch.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
