import argparse
import json
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


def calculate_total(records: object) -> int:
    if not isinstance(records, list) or not records:
        raise ValueError("publication list is empty or invalid")

    total = 0
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("publication record is invalid")
        value = record.get("citations", 0)
        if type(value) is not int or value < 0:
            raise ValueError("citation value must be a non-negative integer")
        total += value
    return total


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
    parser.add_argument("record_file", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    total = calculate_total(read_json(args.record_file))
    changed = update_total(args.root, total)
    if changed:
        print(f"updated total citations to {total}")
    else:
        print(f"total citations unchanged at {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
