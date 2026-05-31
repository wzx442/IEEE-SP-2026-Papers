#!/usr/bin/env python3
"""
IEEE S&P 2026 Paper Fetcher & Classifier
=========================================
Fetches papers from IEEE CSDL GraphQL API, classifies them
using DeepSeek AI, and generates organized Markdown output.

No browser or manual interaction needed — pure API pipeline.

Usage:
  python main.py                  # Full pipeline
  python main.py --fetch-only     # Only fetch from API
  python main.py --classify-only  # Only classify (from cache)
  python main.py --output-only    # Only generate MD (from cache)
  python main.py --force          # Force re-fetch and re-classify
"""

import argparse
import sys

import config
from fetcher import fetch_papers, load_cache
from classifier import classify_all_papers
from output import generate_markdown


def main():
    parser = argparse.ArgumentParser(
        description="IEEE S&P 2026 Paper Fetcher & Classifier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py                  # Full pipeline
  python main.py --fetch-only     # Just fetch from API
  python main.py --classify-only  # Classify from cache
  python main.py --output-only    # Generate MD from cached results
  python main.py --force          # Re-do everything
        """,
    )
    parser.add_argument("--fetch-only", action="store_true")
    parser.add_argument("--classify-only", action="store_true")
    parser.add_argument("--output-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    do_fetch = not (args.classify_only or args.output_only)
    do_classify = not (args.fetch_only or args.output_only)
    do_output = not (args.fetch_only or args.classify_only)

    if args.fetch_only:
        do_fetch, do_classify, do_output = True, False, False
    elif args.classify_only:
        do_fetch, do_classify, do_output = False, True, False
    elif args.output_only:
        do_fetch, do_classify, do_output = False, False, True

    print("=" * 60)
    print("  IEEE S&P 2026 Paper Fetcher & Classifier")
    print(f"  Mode: {'Fetch' if do_fetch else ''}"
          f"{' + Classify' if do_classify else ''}"
          f"{' + Output' if do_output else ''}")
    print("=" * 60)

    # ── Step 1: Fetch ──
    papers = []
    if do_fetch:
        print("\n[STEP 1/3] Fetching papers from IEEE CSDL GraphQL API...")
        papers = fetch_papers(force=args.force)
    else:
        cache = load_cache(config.PAPERS_JSON)
        papers = cache.get("papers", [])
        if not papers:
            print("[ERROR] No cached papers found. Run with --fetch-only first.")
            sys.exit(1)
        print(f"\n[INFO] Loaded {len(papers)} papers from cache.")

    if not papers:
        print("[ERROR] No papers to process.")
        sys.exit(1)

    # Ensure all papers have a pid
    for p in papers:
        if "pid" not in p or not p["pid"]:
            p["pid"] = p.get("doi", "").split("/")[-1] or str(hash(p["title"]) & 0xffff)

    # ── Step 2: Classify ──
    if do_classify:
        print(f"\n[STEP 2/3] Classifying {len(papers)} papers...")
        papers = classify_all_papers(papers, force=args.force)

    # ── Step 3: Output ──
    if do_output:
        print(f"\n[STEP 3/3] Generating markdown...")
        generate_markdown(papers, config.OUTPUT_MD)

    print("\n" + "=" * 60)
    print("  Done!")
    print(f"  Output: {config.OUTPUT_MD}")
    print("=" * 60)


if __name__ == "__main__":
    main()
