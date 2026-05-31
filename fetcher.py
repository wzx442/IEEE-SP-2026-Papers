"""
IEEE S&P 2026 Paper Fetcher
============================
Fetches all papers from the IEEE Computer Society Digital Library
via the public GraphQL API. No browser or Playwright needed.

API endpoint: https://www.computer.org/csdl/api/v1/graphql
"""

import json
import os
import time
import requests
from tqdm import tqdm

import config

GRAPHQL_QUERY = """
query ($proceedingId: String!, $limitResults: Int, $skipResults: Int) {
  articlesByProceeding: articlesByProceedingWithPagination(
    proceedingId: $proceedingId
    limit: $limitResults
    skip: $skipResults
  ) {
    totalResults
    articleResults {
      id
      doi
      title
      abstract
      sectionTitle
      authors {
        fullName
        __typename
      }
      pubType
      pages
      year
      __typename
    }
    __typename
  }
}
"""


def fetch_papers(force: bool = False) -> list[dict]:
    """
    Fetch all papers from the IEEE CSDL GraphQL API.
    Returns list of paper dicts.
    """
    cache = load_cache(config.PAPERS_JSON)

    if not force and cache.get("papers") and len(cache["papers"]) >= 150:
        print(f"[INFO] Loaded {len(cache['papers'])} papers from cache. "
              f"Use --force to re-fetch.")
        return cache["papers"]

    print(f"[INFO] Fetching papers from IEEE CSDL GraphQL API...")

    # Fetch all papers in one call (199 < 500 limit)
    variables = {
        "proceedingId": config.PROCEEDING_ID,
        "limitResults": 500,
        "skipResults": 0,
    }

    for attempt in range(config.RETRY_TIMES):
        try:
            resp = requests.post(
                config.GRAPHQL_URL,
                json={"query": GRAPHQL_QUERY, "variables": variables},
                headers={"Content-Type": "application/json"},
                timeout=config.REQUEST_TIMEOUT,
            )
            resp.raise_for_status()
            data = resp.json()

            if "errors" in data:
                print(f"[ERROR] GraphQL errors: {data['errors']}")
                return []

            articles = data["data"]["articlesByProceeding"]
            total = articles["totalResults"]
            raw = articles["articleResults"]

            print(f"[INFO] Fetched {len(raw)} / {total} papers.")

            # Transform to our standard format
            papers = []
            for a in raw:
                authors = [auth.get("fullName", "") for auth in a.get("authors", []) if auth.get("fullName")]
                doi = a.get("doi", "")
                papers.append({
                    "pid": a.get("id", doi.split("/")[-1] if doi else ""),
                    "doi": doi,
                    "url": f"https://doi.org/{doi}" if doi else "",
                    "title": a.get("title", ""),
                    "abstract": a.get("abstract", ""),
                    "authors": ", ".join(authors),
                    "section": a.get("sectionTitle") or "",
                    "pub_type": a.get("pubType", ""),
                    "pages": a.get("pages", ""),
                })

            # Save cache
            save_cache(config.PAPERS_JSON, {"papers": papers, "total": total})
            return papers

        except requests.RequestException as e:
            if attempt < config.RETRY_TIMES - 1:
                print(f"  [RETRY] Request failed: {e}")
                time.sleep(config.RETRY_DELAY * (attempt + 1))
            else:
                print(f"[ERROR] Failed after {config.RETRY_TIMES} attempts: {e}")
                return []

    return []


# ── Cache helpers ──

def load_cache(path: str) -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_cache(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    papers = fetch_papers()
    print(f"\nTotal: {len(papers)} papers")
    print(f"\nFirst paper: {json.dumps(papers[0], ensure_ascii=False, indent=2)}")
