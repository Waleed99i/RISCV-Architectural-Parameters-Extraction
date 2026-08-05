#!/usr/bin/env python3
"""
report_generator.py

Generate benchmark markdown reports automatically.

Produces:

benchmark/
├── hallucination_summary.md
├── model_comparison.md
├── prompt_comparison.md
└── leaderboard.md

Sources:

audits/
comparisons/
prompts/

Ground truth is NOT required.
"""

from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent

AUDITS_DIR = ROOT / "audits"
PROMPTS_DIR = ROOT / "prompts"
COMPARISONS_DIR = ROOT / "comparisons"
BENCHMARK_DIR = ROOT / "benchmark"

BENCHMARK_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# Utilities
# ---------------------------------------------------------

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ---------------------------------------------------------
# Hallucination Parser
# ---------------------------------------------------------

def parse_hallucination_report(md_file):
    """
    Returns

    {
        model,
        spec,
        supported,
        hallucinations,
        total,
        hallucination_rate
    }
    """

    text = read(md_file)

    model = "Unknown"
    spec = "Unknown"

    m = re.search(r"\*\*Model:\*\*\s*(.+)", text)
    if m:
        model = m.group(1).strip()

    s = re.search(r"\*\*Specification:\*\*\s*(.+)", text)
    if s:
        spec = s.group(1).strip()

    supported = len(re.findall(r"\|\s*PASS\s*\|", text))
    hallucinations = len(re.findall(r"\|\s*FAIL\s*\|", text))

    total = supported + hallucinations

    rate = 0.0
    if total:
        rate = hallucinations / total

    return {
        "model": model,
        "spec": spec,
        "supported": supported,
        "hallucinations": hallucinations,
        "total": total,
        "hallucination_rate": rate,
    }


# ---------------------------------------------------------
# Collect every audit report
# ---------------------------------------------------------

def collect_audits():

    reports = []

    for spec_dir in AUDITS_DIR.iterdir():

        if not spec_dir.is_dir():
            continue

        for model_dir in spec_dir.iterdir():

            if not model_dir.is_dir():
                continue

            report = model_dir / "hallucination_report.md"

            if report.exists():
                reports.append(parse_hallucination_report(report))

    return reports

# ---------------------------------------------------------
# Hallucination Summary Generator
# ---------------------------------------------------------

def generate_hallucination_summary():

    reports = collect_audits()

    if not reports:
        write(
            BENCHMARK_DIR / "hallucination_summary.md",
            "# Hallucination Summary\n\nNo audit reports found.\n",
        )
        return

    md = "# Hallucination Summary\n\n"

    md += (
        "| Model | Specification | Supported | Hallucinations "
        "| Hallucination Rate |\n"
    )
    md += "|---|---:|---:|---:|---:|\n"

    overall = defaultdict(
        lambda: {
            "supported": 0,
            "hallucinations": 0,
            "total": 0,
        }
    )

    for r in reports:

        md += (
            f"| {r['model']} "
            f"| {r['spec']} "
            f"| {r['supported']} "
            f"| {r['hallucinations']} "
            f"| {r['hallucination_rate']:.2%} |\n"
        )

        overall[r["model"]]["supported"] += r["supported"]
        overall[r["model"]]["hallucinations"] += r["hallucinations"]
        overall[r["model"]]["total"] += r["total"]

    md += "\n---\n\n"
    md += "## Overall By Model\n\n"

    md += "| Model | Supported | Hallucinations | Rate |\n"
    md += "|---|---:|---:|---:|\n"

    best_model = None
    best_rate = 999

    for model, stats in sorted(overall.items()):

        total = stats["total"]

        if total:
            rate = stats["hallucinations"] / total
        else:
            rate = 0

        md += (
            f"| {model} "
            f"| {stats['supported']} "
            f"| {stats['hallucinations']} "
            f"| {rate:.2%} |\n"
        )

        if rate < best_rate:
            best_rate = rate
            best_model = model

    md += "\n"

    if best_model:
        md += (
            f"**Best Hallucination Performance:** "
            f"{best_model} ({best_rate:.2%})\n"
        )

    write(
        BENCHMARK_DIR / "hallucination_summary.md",
        md,
    )

# ---------------------------------------------------------
# Prompt Comparison Generator
# ---------------------------------------------------------

def generate_prompt_comparison():

    md = "# Prompt Comparison\n\n"

    prompt_dirs = sorted(
        [
            p for p in PROMPTS_DIR.iterdir()
            if p.is_dir()
        ],
        key=lambda x: x.name,
    )

    if not prompt_dirs:
        write(
            BENCHMARK_DIR / "prompt_comparison.md",
            "# Prompt Comparison\n\nNo prompts found.\n",
        )
        return

    md += "| Prompt | README Found | System Prompt | User Prompt | Schema |\n"
    md += "|---|---:|---:|---:|---:|\n"

    summaries = []

    for p in prompt_dirs:

        readme = p / "README.md"
        system = p / "system_prompt.md"
        user = p / "user_prompt.md"
        schema = p / "expected_output_schema.yaml"

        md += (
            f"| {p.name} "
            f"| {'✅' if readme.exists() else '❌'} "
            f"| {'✅' if system.exists() else '❌'} "
            f"| {'✅' if user.exists() else '❌'} "
            f"| {'✅' if schema.exists() else '❌'} |\n"
        )

        if readme.exists():

            text = read(readme)

            # first non-empty paragraph
            lines = [
                l.strip()
                for l in text.splitlines()
                if l.strip()
                and not l.startswith("#")
            ]

            summary = ""

            if lines:
                summary = lines[0]

            summaries.append(
                (
                    p.name,
                    summary,
                )
            )

    md += "\n---\n\n"
    md += "## Prompt Summaries\n\n"

    for version, summary in summaries:

        md += f"### {version}\n\n"

        if summary:
            md += summary + "\n\n"
        else:
            md += "_No summary available._\n\n"

    md += "---\n\n"

    latest = prompt_dirs[-1].name

    md += (
        f"Current latest prompt version: **{latest}**\n\n"
    )

    md += (
        "After running benchmark.py and evaluate.py, "
        "replace this section with actual benchmark metrics "
        "(Precision, Recall, F1, Hallucination Rate, etc.).\n"
    )

    write(
        BENCHMARK_DIR / "prompt_comparison.md",
        md,
    )

# ---------------------------------------------------------
# Model Comparison Generator
# ---------------------------------------------------------

def generate_model_comparison():

    md = "# Model Comparison\n\n"

    comparison_files = sorted(
        COMPARISONS_DIR.glob("*.md")
    )

    if not comparison_files:

        write(
            BENCHMARK_DIR / "model_comparison.md",
            "# Model Comparison\n\nNo comparison files found.\n",
        )
        return

    md += (
        "This report summarizes all comparison reports "
        "generated under the `comparisons/` directory.\n\n"
    )

    for file in comparison_files:

        text = read(file)

        md += f"## {file.stem}\n\n"

        lines = [
            line.rstrip()
            for line in text.splitlines()
            if line.strip()
        ]

        # Keep first ~60 meaningful lines to avoid copying entire file
        preview = lines[:60]

        md += "```text\n"
        md += "\n".join(preview)
        md += "\n```\n\n"

    md += "---\n\n"

    md += (
        "## Overall Observation\n\n"
        "- Comparison files were successfully discovered.\n"
        "- Review the individual comparison reports above.\n"
        "- After evaluation metrics are available "
        "(Precision, Recall, F1, etc.), this section can be "
        "extended with automatic ranking of models.\n"
    )

    write(
        BENCHMARK_DIR / "model_comparison.md",
        md,
    )

# ---------------------------------------------------------
# Leaderboard Generator
# ---------------------------------------------------------

def generate_leaderboard():

    reports = collect_audits()

    md = "# Benchmark Leaderboard\n\n"

    if not reports:
        write(
            BENCHMARK_DIR / "leaderboard.md",
            "# Benchmark Leaderboard\n\nNo benchmark data available.\n",
        )
        return

    overall = defaultdict(
        lambda: {
            "supported": 0,
            "hallucinations": 0,
            "total": 0,
        }
    )

    for r in reports:

        overall[r["model"]]["supported"] += r["supported"]
        overall[r["model"]]["hallucinations"] += r["hallucinations"]
        overall[r["model"]]["total"] += r["total"]

    leaderboard = []

    for model, stats in overall.items():

        total = stats["total"]

        if total == 0:
            score = 0
            hallucination_rate = 0
        else:
            hallucination_rate = (
                stats["hallucinations"] / total
            )
            score = stats["supported"] / total

        leaderboard.append(
            (
                model,
                score,
                hallucination_rate,
                stats["supported"],
                stats["hallucinations"],
            )
        )

    leaderboard.sort(
        key=lambda x: (
            -x[1],   # higher score first
            x[2],    # lower hallucination first
            x[0],
        )
    )

    md += "| Rank | Model | Score | Supported | Hallucinations | Hallucination Rate |\n"
    md += "|---:|---|---:|---:|---:|---:|\n"

    for rank, row in enumerate(leaderboard, start=1):

        model, score, rate, sup, hall = row

        md += (
            f"| {rank} "
            f"| {model} "
            f"| {score:.2%} "
            f"| {sup} "
            f"| {hall} "
            f"| {rate:.2%} |\n"
        )

    md += "\n---\n\n"

    md += (
        "Ranking currently uses **supported evidence ratio** "
        "and **hallucination rate**.\n\n"
        "After `evaluate.py` is available, this leaderboard "
        "can automatically include:\n\n"
        "- Precision\n"
        "- Recall\n"
        "- F1 Score\n"
        "- Constraint Accuracy\n"
        "- Hallucination Rate\n"
        "- Average Confidence\n"
    )

    write(
        BENCHMARK_DIR / "leaderboard.md",
        md,
    )


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    print("Generating benchmark reports...")

    generate_hallucination_summary()
    generate_prompt_comparison()
    generate_model_comparison()
    generate_leaderboard()

    print("\nDone.\n")

    print("Generated:")

    print("  benchmark/hallucination_summary.md")
    print("  benchmark/prompt_comparison.md")
    print("  benchmark/model_comparison.md")
    print("  benchmark/leaderboard.md")


if __name__ == "__main__":
    main()