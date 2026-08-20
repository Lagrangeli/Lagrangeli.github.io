import argparse
import json
import os
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Optional


DATA_PATHS = (
    Path("results/gs_data.json"),
    Path("_data/scholar.json"),
    Path("google_scholar_crawler/results/gs_data.json"),
)
BADGE_PATHS = (
    Path("results/gs_data_shieldsio.json"),
    Path("google_scholar_crawler/results/gs_data_shieldsio.json"),
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def parse_serpapi_total(payload: object) -> int:
    if not isinstance(payload, dict):
        raise ValueError("SerpAPI response is invalid")
    if payload.get("error"):
        raise ValueError(f"SerpAPI error: {payload['error']}")

    metadata = payload.get("search_metadata")
    if not isinstance(metadata, dict) or metadata.get("status") != "Success":
        raise ValueError("SerpAPI search did not succeed")

    cited_by = payload.get("cited_by")
    table = cited_by.get("table") if isinstance(cited_by, dict) else None
    if not isinstance(table, list):
        raise ValueError("SerpAPI response has no citation table")

    for row in table:
        if not isinstance(row, dict):
            continue
        citations = row.get("citations")
        value = citations.get("all") if isinstance(citations, dict) else None
        if value is not None:
            if type(value) is not int or value < 0:
                raise ValueError("citation total must be a non-negative integer")
            return value

    raise ValueError("SerpAPI response has no total citation value")


def fetch_serpapi_total(api_key: str, scholar_id: str) -> int:
    params = urllib.parse.urlencode(
        {
            "engine": "google_scholar_author",
            "author_id": scholar_id,
            "hl": "en",
            "num": "100",
            "api_key": api_key,
        }
    )
    request = urllib.request.Request(
        f"https://serpapi.com/search.json?{params}",
        headers={"User-Agent": "Lagrangeli.github.io citation updater"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return parse_serpapi_total(payload)


def update_total(root: Path, total: int, now: Optional[str] = None) -> bool:
    if type(total) is not int or total < 0:
        raise ValueError("total citations must be a non-negative integer")

    data_payloads = {
        relative_path: read_json(root / relative_path) for relative_path in DATA_PATHS
    }
    badge_payloads = {
        relative_path: read_json(root / relative_path) for relative_path in BADGE_PATHS
    }
    stored_total = max(
        int(payload.get("citedby", 0)) for payload in data_payloads.values()
    )

    if total < stored_total:
        raise ValueError(
            f"fetched total {total} is lower than stored total {stored_total}"
        )
    if total == stored_total:
        return False

    timestamp = now or datetime.utcnow().isoformat(sep=" ")
    for relative_path, payload in data_payloads.items():
        payload["citedby"] = total
        payload["fetch_strategy"] = "google-scholar-fetcher"
        payload["citation_value_source"] = "google-scholar-fetcher"
        payload["updated"] = timestamp
        payload.pop("last_fetch_error", None)
        write_json(root / relative_path, payload)

    for relative_path, payload in badge_payloads.items():
        payload["message"] = str(total)
        write_json(root / relative_path, payload)

    return True


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Update the homepage Google Scholar citation total."
    )
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--scholar-id", default="r9f4mLMAAAAJ")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise ValueError("SERPAPI_API_KEY is not set")
    total = fetch_serpapi_total(api_key, args.scholar_id)
    changed = update_total(args.root, total)
    if changed:
        print(f"updated total citations to {total}")
    else:
        print(f"total citations unchanged at {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
