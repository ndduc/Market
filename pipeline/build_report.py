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


def parse_order_from_4a(report: str) -> list[tuple[str, str]]:
    a_start = report.index("### 4a. Scores")
    a_end = report.index("### 4b. Prices")
    order: list[tuple[str, str]] = []
    for line in report[a_start:a_end].splitlines():
        if not line.startswith("|") or "State" in line or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        num, state_label = parts[0], parts[1]
        state = state_label.split(" — ")[0].strip()
        order.append((num, state))
    return order


def patch_methodology(report: str, meta: dict) -> str:
    stamp = meta.get("analysis_run_at") or datetime.now(timezone.utc).isoformat()
    note = (
        f"- **Pipeline live fetch:** `data/meta.json` analysis_run_at **{stamp}**; "
        f"census_api_key_present={meta.get('census_api_key_present')}; "
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

    n_med = len(income.get("median_household_income") or {})
    if n_med < 40:
        print(
            f"ERROR: refusing to overwrite §4d - only {n_med} median incomes in data/income.json. "
            "Re-run a successful live fetch (or recovery) so the report is not wiped to unavailable."
        )
        return 2

    section_4d = build_4d(order, income, demo)
    report = _replace_section(
        report,
        "### 4d. Demographics & income (same order)",
        "\n### Notes on score changes",
        section_4d,
    )
    report = patch_methodology(report, meta)

    # Touch what-changed if pipeline row missing
    if "**Durable pipeline**" not in report and "| **Demographics & income** |" in report:
        report = report.replace(
            "| **Demographics & income** |",
            "| **Durable pipeline** | Full refreshes must **live-fetch → overwrite `data/` → build** (no disposable `_add_*.py` patch scripts) |\n"
            "| **Demographics & income** |",
            1,
        )

    report_path.write_text(report, encoding="utf-8")
    print(f"updated {report_path.name} companion §4d from live data/")
    print("Narrative scores / top-10 still require analyst/AI judgment pass after fetch.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
