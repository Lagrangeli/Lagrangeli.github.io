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


def parse_metric(table: list, names: tuple[str, ...]) -> tuple[int, Optional[int]]:
    for row in table:
        if not isinstance(row, dict):
            continue
        for name in names:
            value = row.get(name)
            if not isinstance(value, dict):
                continue
            total = value.get("all")
            recent = next(
                (item for key, item in value.items() if key != "all"), None
            )
            if type(total) is not int or total < 0:
                raise ValueError(f"{names[0]} must be a non-negative integer")
            if recent is not None and (type(recent) is not int or recent < 0):
                raise ValueError(
                    f"recent {names[0]} must be a non-negative integer"
                )
            return total, recent
    raise ValueError(f"SerpAPI response has no {names[0]} value")


def parse_serpapi_metrics(payload: object) -> dict[str, int]:
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

    citedby, citedby5y = parse_metric(table, ("citations",))
    hindex, hindex5y = parse_metric(table, ("h_index", "hindex", "indice_h"))
    i10index, i10index5y = parse_metric(
        table, ("i10_index", "i10index", "indice_i10")
    )
    metrics = {
        "citedby": citedby,
        "hindex": hindex,
        "i10index": i10index,
    }
    for key, value in (
        ("citedby5y", citedby5y),
        ("hindex5y", hindex5y),
        ("i10index5y", i10index5y),
    ):
        if value is not None:
            metrics[key] = value
    return metrics


def fetch_serpapi_metrics(api_key: str, scholar_id: str) -> dict[str, int]:
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
    return parse_serpapi_metrics(payload)


def update_metrics(
    root: Path, metrics: dict[str, int], now: Optional[str] = None
) -> bool:
    required = {"citedby", "hindex", "i10index"}
    missing = required - metrics.keys()
    if missing:
        raise ValueError(f"missing Scholar metrics: {', '.join(sorted(missing))}")
    for key, value in metrics.items():
        if type(value) is not int or value < 0:
            raise ValueError(f"{key} must be a non-negative integer")

    data_payloads = {
        relative_path: read_json(root / relative_path) for relative_path in DATA_PATHS
    }
    badge_payloads = {
        relative_path: read_json(root / relative_path) for relative_path in BADGE_PATHS
    }
    for key in required:
        stored_value = max(
            int(payload.get(key, 0)) for payload in data_payloads.values()
        )
        if metrics[key] < stored_value:
            raise ValueError(
                f"fetched {key} {metrics[key]} is lower than stored value {stored_value}"
            )

    changed = any(
        payload.get(key) != value
        for payload in data_payloads.values()
        for key, value in metrics.items()
    )
    if not changed:
        return False

    timestamp = now or datetime.utcnow().isoformat(sep=" ")
    for relative_path, payload in data_payloads.items():
        payload.update(metrics)
        payload["fetch_strategy"] = "google-scholar-fetcher"
        payload["citation_value_source"] = "google-scholar-fetcher"
        payload["updated"] = timestamp
        payload.pop("last_fetch_error", None)
        write_json(root / relative_path, payload)

    for relative_path, payload in badge_payloads.items():
        payload["message"] = str(metrics["citedby"])
        write_json(root / relative_path, payload)

    return True


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Update the homepage Google Scholar citation and index metrics."
    )
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--scholar-id", default="r9f4mLMAAAAJ")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise ValueError("SERPAPI_API_KEY is not set")
    metrics = fetch_serpapi_metrics(api_key, args.scholar_id)
    changed = update_metrics(args.root, metrics)
    summary = (
        f'{metrics["citedby"]} citations, h-index {metrics["hindex"]}, '
        f'i10-index {metrics["i10index"]}'
    )
    if changed:
        print(f"updated Scholar metrics to {summary}")
    else:
        print(f"Scholar metrics unchanged at {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
