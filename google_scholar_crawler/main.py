import json
import os
from datetime import datetime
from typing import Optional

from scholarly import ProxyGenerator, scholarly


def write_json(path: str, payload: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False)


def read_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as infile:
        return json.load(infile)


def fetch_author(scholar_id: str) -> dict:
    errors = []

    try:
        author = scholarly.search_author_id(scholar_id)
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
        author["fetch_strategy"] = "direct"
        return author
    except Exception as exc:  # pragma: no cover - network-dependent
        errors.append(f"direct: {exc}")

    try:
        proxy = ProxyGenerator()
        if proxy.FreeProxies():
            scholarly.use_proxy(proxy)
            author = scholarly.search_author_id(scholar_id)
            scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
            author["fetch_strategy"] = "free-proxies"
            return author
        errors.append("free-proxies: no proxy available")
    except Exception as exc:  # pragma: no cover - network-dependent
        errors.append(f"free-proxies: {exc}")

    raise RuntimeError("Failed to fetch Google Scholar profile. " + " | ".join(errors))


def to_int(value) -> Optional[int]:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def apply_floor(author: dict, previous_author: dict, manual_floor: dict) -> dict:
    citedby_candidates = [
        ("scraped", to_int(author.get("citedby"))),
        ("previous", to_int(previous_author.get("citedby"))),
        ("manual_floor", to_int(manual_floor.get("citedby"))),
        ("env_floor", to_int(os.environ.get("SCHOLAR_CITATION_FLOOR"))),
    ]
    citedby_candidates = [(source, value) for source, value in citedby_candidates if value is not None]
    best_source, best_citedby = max(citedby_candidates, key=lambda item: item[1])
    author["citedby"] = best_citedby

    citedby5y_candidates = [
        ("scraped", to_int(author.get("citedby5y"))),
        ("previous", to_int(previous_author.get("citedby5y"))),
        ("manual_floor", to_int(manual_floor.get("citedby5y")) or to_int(manual_floor.get("citedby"))),
        ("env_floor", to_int(os.environ.get("SCHOLAR_CITATION_FLOOR"))),
    ]
    citedby5y_candidates = [(source, value) for source, value in citedby5y_candidates if value is not None]
    if citedby5y_candidates:
        _, best_citedby5y = max(citedby5y_candidates, key=lambda item: item[1])
        author["citedby5y"] = best_citedby5y

    author["citation_value_source"] = best_source
    return author


scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "r9f4mLMAAAAJ")
previous_author = read_json("../results/gs_data.json")
manual_floor = read_json("manual_citation_floor.json")
author: dict = fetch_author(scholar_id)
author = apply_floor(author, previous_author, manual_floor)

author["updated"] = str(datetime.now())
author["publications"] = {
    publication["author_pub_id"]: publication
    for publication in author.get("publications", [])
    if publication.get("author_pub_id")
}
print(
    json.dumps(
        {
            "name": author.get("name"),
            "citedby": author.get("citedby"),
            "fetch_strategy": author.get("fetch_strategy"),
            "citation_value_source": author.get("citation_value_source"),
        },
        indent=2,
    )
)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author.get("citedby", 0)),
}

# Keep all consumer paths in sync:
# - google_scholar_crawler/results/* for script-local usage
# - ../results/* for website runtime usage
# - ../_data/scholar.json for data-file usage
write_json("results/gs_data.json", author)
write_json("results/gs_data_shieldsio.json", shieldio_data)
write_json("../results/gs_data.json", author)
write_json("../results/gs_data_shieldsio.json", shieldio_data)
write_json("../_data/scholar.json", author)
