import ast
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def generated_cv_titles():
    source = (ROOT / "scripts" / "generate_bilingual_cv.py").read_text(
        encoding="utf-8"
    )
    module = ast.parse(source)
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "PUBLICATIONS"
            for target in node.targets
        ):
            return [item["title"] for item in ast.literal_eval(node.value)]
    raise AssertionError("PUBLICATIONS was not found in the CV generator")


def homepage_publication_titles():
    about = (ROOT / "_pages" / "about.md").read_text(encoding="utf-8")
    titles = []
    in_publications = False
    for line in about.splitlines():
        if line.startswith("<span class='anchor' id='-publications'"):
            in_publications = True
            continue
        if line.startswith("<span class='anchor' id='-honors-and-awards'"):
            break
        if not in_publications or not line.startswith("- <img"):
            continue

        match = re.search(r"<strong>(.*?)</strong></a><br>", line)
        if not match:
            match = re.search(r"\[\*\*(.*?)\*\*\]\(", line)
        if not match:
            match = re.search(r"\*\*(.*?)\*\*", line)
        if match:
            titles.append(match.group(1))
    return titles


class CvPublicationSyncTest(unittest.TestCase):
    def test_cv_generator_contains_every_homepage_publication(self):
        self.assertEqual(
            [],
            [
                title
                for title in homepage_publication_titles()
                if title not in generated_cv_titles()
            ],
        )


if __name__ == "__main__":
    unittest.main()
