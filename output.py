"""
IEEE S&P 2026 Markdown Output Generator
========================================
Generates organized markdown from classified papers.
"""

import os
from collections import Counter


def generate_markdown(papers: list[dict], output_path: str) -> str:
    """
    Generate markdown from classified papers grouped by broad_category.
    """
    grouped: dict[str, list[dict]] = {}
    for p in papers:
        cat = p.get("broad_category", "Other")
        grouped.setdefault(cat, []).append(p)

    sorted_cats = sorted(grouped.keys(), key=lambda c: (-len(grouped[c]), c))

    lines = []
    lines.append("# IEEE S&P 2026 Accepted Papers")
    lines.append("")
    lines.append(f"> **Total papers: {len(papers)}** | ")
    lines.append(f"> Categories: {len(sorted_cats)} | ")
    lines.append(f"> Generated from [IEEE S&P 2026 Proceedings]"
                 f"(https://www.computer.org/csdl/proceedings/sp/2026/2bojuokAJK8)")
    lines.append("")
    lines.append(f"> Classification performed by DeepSeek AI; ")
    lines.append(f"> please excuse any errors.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of Contents
    lines.append("## Table of Contents")
    lines.append("")
    for cat in sorted_cats:
        count = len(grouped[cat])
        anchor = cat.lower().replace(" ", "-").replace("/", "").replace("&", "").replace("'", "")
        lines.append(f"- [{cat} ({count})](#{anchor})")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Each category
    for cat in sorted_cats:
        cat_papers = grouped[cat]
        lines.append(f"## {cat}")
        lines.append("")
        lines.append(f"*{len(cat_papers)} papers*")
        lines.append("")
        lines.append("| Paper | Sub-area |")
        lines.append("|-------|----------|")

        cat_papers.sort(key=lambda p: (p.get("sub_area", ""), p.get("title", "")))

        for p in cat_papers:
            title = p.get("title", "Unknown")
            url = p.get("url", "")
            sub_area = p.get("sub_area", "—")

            title_escaped = title.replace("|", "\\|")
            if url:
                title_md = f"[{title_escaped}]({url})"
            else:
                title_md = title_escaped

            lines.append(f"| {title_md} | {sub_area} |")

        lines.append("")
        lines.append("---")
        lines.append("")

    # Statistics
    lines.append("## Statistics")
    lines.append("")
    lines.append("| Category | Paper Count |")
    lines.append("|-----------|-------------|")
    for cat in sorted_cats:
        lines.append(f"| {cat} | {len(grouped[cat])} |")
    lines.append(f"| **Total** | **{len(papers)}** |")
    lines.append("")

    # Sub-area details
    lines.append("## Sub-Area Distribution")
    lines.append("")
    sub_counter = Counter(p.get("sub_area", "N/A") for p in papers if p.get("sub_area"))
    lines.append("| Sub-area | Count |")
    lines.append("|----------|-------|")
    for area, count in sub_counter.most_common():
        lines.append(f"| {area} | {count} |")
    lines.append("")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    content = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[INFO] Markdown written to: {output_path}")
    return output_path


if __name__ == "__main__":
    sample = [
        {"pid": "1", "broad_category": "Machine Learning and Security",
         "title": "Privacy-Preserving Federated Learning",
         "url": "https://doi.org/10.1109/SP63933.2026.00001",
         "sub_area": "Federated Learning"},
        {"pid": "2", "broad_category": "LLMs and AI Safety",
         "title": "SoK: Evaluating Jailbreak Guardrails for LLMs",
         "url": "https://doi.org/10.1109/SP63933.2026.00076",
         "sub_area": "LLM Jailbreaking"},
    ]
    generate_markdown(sample, "output/test_SP2026.md")
    print("Test output generated.")
