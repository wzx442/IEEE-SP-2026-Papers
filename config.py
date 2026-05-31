"""
IEEE S&P 2026 Paper Scraper - Configuration
"""

import os


def _load_dotenv(path: str = ".env"):
    """Minimal .env loader — no extra dependencies needed."""
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip()
            if key not in os.environ:
                os.environ[key] = val


_load_dotenv()

# --- DeepSeek API ---
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "sk")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-v4-flash"

# --- IEEE CSDL GraphQL API ---
GRAPHQL_URL = "https://www.computer.org/csdl/api/v1/graphql"
PROCEEDING_ID = "2bojuokAJK8"
PROCEEDINGS_URL = "https://www.computer.org/csdl/proceedings/sp/2026/2bojuokAJK8"

# --- Fetcher ---
REQUEST_TIMEOUT = 30
RETRY_TIMES = 3
RETRY_DELAY = 2

# --- Caching ---
DATA_DIR = "data"
PAPERS_JSON = "data/papers.json"
CLASSIFIED_JSON = "data/classified.json"

# --- Output ---
OUTPUT_DIR = "output"
OUTPUT_MD = "output/SP2026.md"

# --- Classification ---
CLASSIFY_BATCH_SIZE = 15
BATCH_DELAY = 1.0
