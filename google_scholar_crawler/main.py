import json
import os
from datetime import datetime

from scholarly import scholarly


def write_json(path: str, payload: dict) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(payload, outfile, ensure_ascii=False)


scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "r9f4mLMAAAAJ")
author: dict = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])

author["updated"] = str(datetime.now())
author["publications"] = {
    publication["author_pub_id"]: publication
    for publication in author.get("publications", [])
    if publication.get("author_pub_id")
}
print(json.dumps({"name": author.get("name"), "citedby": author.get("citedby")}, indent=2))

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
