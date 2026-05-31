"""
IEEE S&P 2026 Paper Classifier
===============================
Uses DeepSeek API to classify papers into two levels:
  1. Broad category (e.g. "LLMs and AI Safety")
  2. Sub-area (e.g. "LLM Jailbreaking")

Since IEEE CSDL does NOT provide session/track information,
both levels are assigned by the LLM.
"""

import json
import os
import time
from collections import Counter

import requests
from tqdm import tqdm

import config

CLASSIFICATION_SYSTEM_PROMPT = """You are an expert in computer security research classification.
You will classify papers from the IEEE Symposium on Security and Privacy (S&P) 2026.

For each paper, assign:
1. **broad_category** — one of the established categories below (create new only if absolutely necessary)
2. **sub_area** — the specific research sub-area (2-5 words, precise and consistent)

## Established Broad Categories (prefer these; keep consistent across batches):
- LLMs and AI Safety (jailbreaking, prompt injection, LLM privacy, LLM security, LLM watermarking, etc.)
- Machine Learning and Security (adversarial ML, federated learning, backdoor attacks, privacy-preserving ML, etc.)
- Cryptography and Privacy (applied crypto, ZKP, MPC, FHE, differential privacy, anonymous communication, etc.)
- Software Security (fuzzing, binary analysis, vulnerability detection, program analysis, exploitation, etc.)
- Systems Security (TEE, hardware security, OS security, side channels, cloud security, firmware, etc.)
- Network Security (TLS, DNS, DDoS, traffic analysis, protocol security, 5G, Wi-Fi, etc.)
- Web Security (browser security, web attacks, XSS, authentication, tracking, etc.)
- Blockchain and Distributed Systems (smart contracts, DeFi, consensus, MEV, etc.)
- IoT and Cyber-Physical Systems (automotive, drones, ICS, medical devices, etc.)
- Usable Security and Privacy (UX studies, security warnings, developer practices, measurement studies, etc.)
- Formal Methods and Verification (protocol verification, security proofs, model checking, etc.)
- Digital Forensics and Cybercrime (malware, fraud, abuse, threat intelligence, etc.)

## Sub-area Guidelines:
- Be specific and consistent (e.g., "Federated Learning" not "ML Privacy"; "LLM Jailbreaking" not "LLM Attacks")
- Use established terminology from the security community
- Maximum 5 words

## Output Format (JSON only, no markdown):
```json
{
  "classifications": [
    {"pid": "paper_id", "broad_category": "Category Name", "sub_area": "Specific Sub-area"}
  ]
}
```
"""


def classify_batch(papers_batch: list[dict]) -> list[dict]:
    """Send a batch to DeepSeek API. Returns classification list."""
    paper_texts = []
    for p in papers_batch:
        abstract = p.get("abstract", "")
        if len(abstract) > 900:
            abstract = abstract[:900] + "..."
        paper_texts.append(
            f"pid={p.get('pid', '')}\n"
            f"Title: {p['title']}\n"
            f"Abstract: {abstract}\n"
        )

    papers_block = "\n---\n".join(paper_texts)

    user_prompt = (
        f"Classify each of the following {len(papers_batch)} papers:\n\n"
        f"{papers_block}\n\n"
        f"Return JSON with 'classifications' array (pid, broad_category, sub_area for each)."
    )

    for attempt in range(config.RETRY_TIMES):
        try:
            resp = requests.post(
                f"{config.DEEPSEEK_BASE_URL}/chat/completions",
                headers={
                    "Authorization": f"Bearer {config.DEEPSEEK_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": config.DEEPSEEK_MODEL,
                    "messages": [
                        {"role": "system", "content": CLASSIFICATION_SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": 0.1,
                    "max_tokens": 4096,
                },
                timeout=120,
            )
            resp.raise_for_status()
            content = resp.json()["choices"][0]["message"]["content"].strip()

            # Strip markdown fences
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:]) if len(lines) > 1 else content
                if content.endswith("```"):
                    content = content[:-3].strip()
                if content.startswith("json"):
                    content = content[4:].strip()

            parsed = json.loads(content)
            return parsed.get("classifications", [])

        except (json.JSONDecodeError, KeyError) as e:
            if attempt < config.RETRY_TIMES - 1:
                time.sleep(config.RETRY_DELAY * (attempt + 1))
            else:
                print(f"  [ERROR] Parse failure: {e}")
                return []
        except requests.RequestException as e:
            if attempt < config.RETRY_TIMES - 1:
                time.sleep(config.RETRY_DELAY * (attempt + 1))
            else:
                print(f"  [ERROR] API failure: {e}")
                return []

    return []


def classify_all_papers(papers: list[dict], force: bool = False) -> list[dict]:
    """Classify all papers with DeepSeek API."""
    classified_map = {}
    if os.path.exists(config.CLASSIFIED_JSON):
        with open(config.CLASSIFIED_JSON, "r", encoding="utf-8") as f:
            classified_map = json.load(f).get("classifications", {})

    papers_needed = []
    for p in papers:
        pid = p.get("pid", "")
        if not force and pid in classified_map:
            p["broad_category"] = classified_map[pid].get("broad_category", "")
            p["sub_area"] = classified_map[pid].get("sub_area", "")
        else:
            papers_needed.append(p)

    if not papers_needed:
        print(f"[INFO] All {len(papers)} papers already classified. Use --force to redo.")
        return papers

    print(f"[INFO] Classifying {len(papers_needed)} papers "
          f"in batches of {config.CLASSIFY_BATCH_SIZE}...")

    batches = [
        papers_needed[i:i + config.CLASSIFY_BATCH_SIZE]
        for i in range(0, len(papers_needed), config.CLASSIFY_BATCH_SIZE)
    ]

    for batch in tqdm(batches, desc="Classifying"):
        results = classify_batch(batch)
        for r in results:
            pid = r.get("pid", "")
            classified_map[pid] = {
                "broad_category": r.get("broad_category", "Other"),
                "sub_area": r.get("sub_area", "General"),
            }
            for p in papers:
                if p.get("pid") == pid:
                    p["broad_category"] = r.get("broad_category", "Other")
                    p["sub_area"] = r.get("sub_area", "General")
                    break

        with open(config.CLASSIFIED_JSON, "w", encoding="utf-8") as f:
            json.dump({"classifications": classified_map}, f, ensure_ascii=False, indent=2)
        time.sleep(config.BATCH_DELAY)

    for p in papers:
        if "broad_category" not in p:
            p["broad_category"] = "Other"
        if "sub_area" not in p:
            p["sub_area"] = ""

    cat_counts = Counter(p.get("broad_category", "Other") for p in papers)
    print("\n[INFO] Classification distribution:")
    for cat, count in cat_counts.most_common():
        print(f"  {cat}: {count} papers")

    return papers


if __name__ == "__main__":
    from fetcher import load_cache
    papers = load_cache("data/papers.json").get("papers", [])
    test = papers[:3]
    results = classify_batch(test)
    for r in results:
        print(f"{r.get('pid', '?')}: {r.get('broad_category', '?')} / {r.get('sub_area', '?')}")
