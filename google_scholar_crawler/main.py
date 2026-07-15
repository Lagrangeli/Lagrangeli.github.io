import json
import os
import re
import urllib.request
import urllib.parse
from datetime import datetime
from typing import Any, Optional

try:
    from scholarly import ProxyGenerator, scholarly
except ImportError:  # pragma: no cover - local fallback path
    ProxyGenerator = None
    scholarly = None


def write_json(path: str, payload: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False)


def read_json(path: str) -> dict:
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as infile:
        return json.load(infile)


def first_non_all_metric(metric: dict) -> Optional[int]:
    for key, value in metric.items():
        if key != "all":
            parsed = to_int(value)
            if parsed is not None:
                return parsed
    return None


def extract_serpapi_metric(table: list, metric_names: list[str]) -> tuple[Optional[int], Optional[int]]:
    for row in table:
        if not isinstance(row, dict):
            continue
        for metric_name in metric_names:
            metric = row.get(metric_name)
            if isinstance(metric, dict):
                return to_int(metric.get("all")), first_non_all_metric(metric)
            parsed = to_int(metric)
            if parsed is not None:
                return parsed, None
    return None, None


def update_publications_from_serpapi(author: dict, articles: list) -> None:
    publications = normalize_publications(author.get("publications", {}))
    for article in articles:
        if not isinstance(article, dict):
            continue

        citation_id = article.get("citation_id")
        if not citation_id:
            continue

        publication = publications.get(citation_id, {"container_type": "Publication"})
        publication["source"] = "SERPAPI_AUTHOR_ARTICLE"
        publication["filled"] = False
        publication["author_pub_id"] = citation_id

        bib = publication.get("bib", {})
        if article.get("title"):
            bib["title"] = article["title"]
        if article.get("year"):
            bib["pub_year"] = str(article["year"])
        if article.get("publication"):
            bib["citation"] = article["publication"]
        if article.get("authors"):
            bib["author"] = article["authors"]
        publication["bib"] = bib

        cited_by = article.get("cited_by")
        if isinstance(cited_by, dict):
            num_citations = to_int(cited_by.get("value"))
            if num_citations is not None:
                publication["num_citations"] = num_citations
            if cited_by.get("link"):
                publication["citedby_url"] = cited_by["link"]

        publications[citation_id] = publication

    author["publications"] = publications


def fetch_serpapi_author(scholar_id: str, previous_author: dict) -> dict:
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise RuntimeError("SERPAPI_API_KEY is not set")

    params = urllib.parse.urlencode(
        {
            "engine": "google_scholar_author",
            "author_id": scholar_id,
            "hl": "en",
            "num": "100",
            "api_key": api_key,
        }
    )
    url = f"https://serpapi.com/search.json?{params}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Lagrangeli.github.io Scholar updater"},
    )

    with urllib.request.urlopen(request, timeout=45) as response:
        payload = json.loads(response.read().decode("utf-8", errors="replace"))

    if payload.get("error"):
        raise RuntimeError(f"SerpAPI error: {payload['error']}")

    metadata = payload.get("search_metadata", {})
    if metadata.get("status") and metadata.get("status") != "Success":
        raise RuntimeError(f"SerpAPI status: {metadata.get('status')}")

    cited_by = payload.get("cited_by") or {}
    table = cited_by.get("table") or []
    citedby, citedby5y = extract_serpapi_metric(table, ["citations"])
    hindex, hindex5y = extract_serpapi_metric(table, ["h_index", "hindex", "indice_h"])
    i10index, i10index5y = extract_serpapi_metric(table, ["i10_index", "i10index", "indice_i10"])

    if citedby is None:
        raise RuntimeError("SerpAPI response did not include citation totals")

    author = previous_author.copy() if previous_author else {"scholar_id": scholar_id}
    author_profile = payload.get("author") or {}
    if author_profile.get("name"):
        author["name"] = author_profile["name"]
    if author_profile.get("affiliations"):
        author["affiliation"] = author_profile["affiliations"]
    if author_profile.get("thumbnail"):
        author["url_picture"] = author_profile["thumbnail"]

    author["scholar_id"] = author.get("scholar_id", scholar_id)
    author["citedby"] = citedby
    if citedby5y is not None:
        author["citedby5y"] = citedby5y
    if hindex is not None:
        author["hindex"] = hindex
    if hindex5y is not None:
        author["hindex5y"] = hindex5y
    if i10index is not None:
        author["i10index"] = i10index
    if i10index5y is not None:
        author["i10index5y"] = i10index5y

    if isinstance(cited_by.get("graph"), list):
        author["cites_per_year"] = {
            str(item.get("year")): to_int(item.get("citations")) or 0
            for item in cited_by["graph"]
            if isinstance(item, dict) and item.get("year")
        }

    articles = payload.get("articles")
    if isinstance(articles, list):
        update_publications_from_serpapi(author, articles)

    author["fetch_strategy"] = "serpapi"
    author.pop("last_fetch_error", None)
    return author


def fetch_author(scholar_id: str) -> dict:
    errors = []

    if scholarly is None or ProxyGenerator is None:
        errors.append("scholarly: package not installed")
    elif os.environ.get("SCHOLAR_SKIP_SCHOLARLY") == "1":
        errors.append("direct/free-proxies: skipped by SCHOLAR_SKIP_SCHOLARLY")
    else:
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


def fetch_profile_page_counts(scholar_id: str) -> dict:
    url = f"https://scholar.google.com/citations?hl=en&user={scholar_id}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        page = response.read().decode("utf-8", errors="replace")

    def parse_row(label: str) -> tuple[Optional[int], Optional[int]]:
        row_match = re.search(
            rf">{re.escape(label)}</a>.*?"
            r'<td[^>]*class="gsc_rsb_std"[^>]*>([\d,]+)</td>.*?'
            r'<td[^>]*class="gsc_rsb_std"[^>]*>([\d,]+)</td>',
            page,
            flags=re.DOTALL,
        )
        if not row_match:
            return None, None
        return (
            int(row_match.group(1).replace(",", "")),
            int(row_match.group(2).replace(",", "")),
        )

    citedby, citedby5y = parse_row("Citations")
    hindex, hindex5y = parse_row("h-index")
    i10index, i10index5y = parse_row("i10-index")
    if citedby is not None:
        counts = {"citedby": citedby}
        if citedby5y is not None:
            counts["citedby5y"] = citedby5y
        if hindex is not None:
            counts["hindex"] = hindex
        if hindex5y is not None:
            counts["hindex5y"] = hindex5y
        if i10index is not None:
            counts["i10index"] = i10index
        if i10index5y is not None:
            counts["i10index5y"] = i10index5y
        return counts

    meta_match = re.search(r"Cited by\s+([\d,]+)", page)
    if meta_match:
        return {"citedby": int(meta_match.group(1).replace(",", ""))}

    raise RuntimeError("Could not parse citation counts from Google Scholar profile page")


def build_fallback_author(
    scholar_id: str,
    previous_author: dict,
    fetch_error: str,
    profile_error: Optional[str] = None,
) -> dict:
    author = previous_author.copy() if previous_author else {"scholar_id": scholar_id}
    author["scholar_id"] = author.get("scholar_id", scholar_id)
    author["fetch_strategy"] = "previous-cache"
    errors = [fetch_error]
    if profile_error:
        errors.append(profile_error)
    author["last_fetch_error"] = " | ".join(errors)
    return author


def fetch_author_with_fallback(scholar_id: str, previous_author: dict) -> dict:
    errors = []

    try:
        return fetch_serpapi_author(scholar_id, previous_author)
    except Exception as exc:  # pragma: no cover - network-dependent
        errors.append(f"serpapi: {exc}")

    try:
        return fetch_author(scholar_id)
    except Exception as exc:  # pragma: no cover - network-dependent
        errors.append(str(exc))

    try:
        counts = fetch_profile_page_counts(scholar_id)
        author = previous_author.copy() if previous_author else {"scholar_id": scholar_id}
        author.update(counts)
        author["scholar_id"] = author.get("scholar_id", scholar_id)
        author["fetch_strategy"] = "profile-page"
        author.pop("last_fetch_error", None)
        return author
    except Exception as exc:  # pragma: no cover - network-dependent
        return build_fallback_author(scholar_id, previous_author, " | ".join(errors), str(exc))


def to_int(value) -> Optional[int]:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def apply_floor(author: dict, previous_author: dict, manual_floor: dict) -> dict:
    author_source = author.get("fetch_strategy") or "scraped"
    citedby_candidates = [
        (author_source, to_int(author.get("citedby"))),
        ("previous", to_int(previous_author.get("citedby"))),
        ("manual_floor", to_int(manual_floor.get("citedby"))),
        ("env_floor", to_int(os.environ.get("SCHOLAR_CITATION_FLOOR"))),
    ]
    citedby_candidates = [(source, value) for source, value in citedby_candidates if value is not None]
    if citedby_candidates:
        best_source, best_citedby = max(citedby_candidates, key=lambda item: item[1])
        author["citedby"] = best_citedby
    else:
        best_source = "missing"
        author["citedby"] = 0

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


def normalize_publications(publications: Any) -> dict:
    if isinstance(publications, dict):
        return publications
    if not isinstance(publications, list):
        return {}
    return {
        publication["author_pub_id"]: publication
        for publication in publications
        if isinstance(publication, dict) and publication.get("author_pub_id")
    }


def main() -> None:
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "r9f4mLMAAAAJ")
    previous_author = read_json("../results/gs_data.json")
    manual_floor = read_json("manual_citation_floor.json")
    author: dict = fetch_author_with_fallback(scholar_id, previous_author)
    author = apply_floor(author, previous_author, manual_floor)

    author["updated"] = str(datetime.now())
    author["publications"] = normalize_publications(author.get("publications", []))
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


if __name__ == "__main__":
    main()
