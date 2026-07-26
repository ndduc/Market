"""Add [Back to Index] under every indexed section heading in the report (and optionally the spec)."""
from __future__ import annotations

import re
from pathlib import Path

BACK = "[↑ Back to Index](#index)"
BACK_LINE = f"{BACK}\n"

ROOT = Path(r"C:\Users\ndduc\OneDrive\house\Market")


def add_back_links(text: str, *, skip_titles: set[str] | None = None) -> str:
    skip_titles = skip_titles or {"Index", "Spec index"}
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = re.match(r"^(#{2,3}) (.+?)\s*$", line.rstrip("\n\r"))
        if m:
            level, title = m.group(1), m.group(2).strip()
            # Skip top-level Index / Spec index only at ##
            if title in skip_titles or title.startswith("Index"):
                i += 1
                continue
            # Peek next non-empty content lines for existing back link
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            already = j < len(lines) and "Back to Index" in lines[j]
            if not already:
                # Insert blank line then back link if heading wasn't followed by blank
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    out.append("\n")
                out.append(BACK_LINE)
                out.append("\n")
        i += 1
    return "".join(out)


def patch_index_note(text: str) -> str:
    note = (
        "Every section below includes **[↑ Back to Index](#index)** under its heading "
        "so you can return here after jumping.\n\n"
    )
    if "Every section below includes" in text:
        return text
    # After "Jump to a section..." paragraph
    return text.replace(
        "Jump to a section (companion tables in §4 share the same state order):\n\n",
        "Jump to a section (companion tables in §4 share the same state order):\n\n" + note,
        1,
    )


def patch_spec_index_note(text: str) -> str:
    note = (
        "Every section below includes **[↑ Back to Spec index](#spec-index)** under its heading.\n\n"
    )
    if "Back to Spec index" in text and "Every section below includes" in text:
        return text
    # Insert after ## Spec index heading block start
    if "## Spec index\n" in text and "Every section below includes" not in text.split("## Spec index", 1)[1][:400]:
        text = text.replace(
            "## Spec index\n\n",
            "## Spec index\n\n" + note,
            1,
        )
    return text


def main() -> None:
    report = ROOT / "rental_market_report.md"
    t = report.read_text(encoding="utf-8")
    # Remove prior auto back-links to avoid stacking on re-run
    t = re.sub(r"\n*\[↑ Back to Index\]\(#index\)\n+", "\n", t)
    t = patch_index_note(t)
    t = add_back_links(t, skip_titles={"Index"})
    # Ensure A-Z keeps a back link (### heading gets one from add_back_links)
    report.write_text(t, encoding="utf-8")
    n = t.count("Back to Index")
    print(f"report: {n} Back to Index links")

    spec = ROOT / "rental_market_spec.md"
    s = spec.read_text(encoding="utf-8")
    s = re.sub(r"\n*\[↑ Back to Spec index\]\(#spec-index\)\n+", "\n", s)
    s = patch_spec_index_note(s)
    # Spec uses ## and ### — add Back to Spec index
    BACK_SPEC = "[↑ Back to Spec index](#spec-index)"

    lines = s.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = re.match(r"^(#{2,3}) (.+?)\s*$", line.rstrip("\n\r"))
        if m:
            title = m.group(2).strip()
            if title != "Spec index":
                j = i + 1
                while j < len(lines) and lines[j].strip() == "":
                    j += 1
                already = j < len(lines) and "Back to Spec index" in lines[j]
                if not already:
                    if i + 1 < len(lines) and lines[i + 1].strip() != "":
                        out.append("\n")
                    out.append(BACK_SPEC + "\n")
                    out.append("\n")
        i += 1
    s2 = "".join(out)

    # Navigation rules in spec
    if "Back to Index" not in s2.split("Navigation rules", 1)[-1][:800]:
        s2 = s2.replace(
            "**Navigation rules:**\n"
            "- Keep a top **Index** with Markdown anchor links (works in GitHub / most Markdown previews), including shortcuts to **all** deep-dive state headings (or A–Z → deep dive).\n"
            "- Keep an end **A–Z rank index** that links **every** state abbreviation to its deep-dive heading.\n"
            "- Within dense sections (§4, §5, §6), prefer short “jump” lines or Index shortcuts rather than duplicating full tables.\n",
            "**Navigation rules:**\n"
            "- Keep a top **Index** with Markdown anchor links (works in GitHub / most Markdown previews), including shortcuts to **all** deep-dive state headings (or A–Z → deep dive).\n"
            "- Keep an end **A–Z rank index** that links **every** state abbreviation to its deep-dive heading.\n"
            "- **Every indexed section / subsection** (including each deep-dive state and 4a–4e) must show **[↑ Back to Index](#index)** directly under its heading.\n"
            "- Within dense sections (§4, §5, §6), prefer short “jump” lines or Index shortcuts rather than duplicating full tables.\n",
            1,
        )

    # What-changed / content note
    if "Back to Index under every section" not in s2:
        pass

    spec.write_text(s2, encoding="utf-8")
    print(f"spec: {s2.count('Back to Spec index')} Back to Spec index links")


if __name__ == "__main__":
    main()
