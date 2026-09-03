import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from google_scholar_crawler.update_total import parse_serpapi_metrics, update_metrics


ROOT = Path(__file__).resolve().parents[1]
DATA_PATHS = (
    Path("results/gs_data.json"),
    Path("_data/scholar.json"),
    Path("google_scholar_crawler/results/gs_data.json"),
)
BADGE_PATHS = (
    Path("results/gs_data_shieldsio.json"),
    Path("google_scholar_crawler/results/gs_data_shieldsio.json"),
)
ALL_PATHS = DATA_PATHS + BADGE_PATHS


class ScholarTotalUpdateTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

        scholar_payload = {
            "citedby": 229,
            "citedby5y": 205,
            "hindex": 8,
            "hindex5y": 8,
            "i10index": 8,
            "i10index5y": 8,
            "publications": {"paper-id": {"num_citations": 12}},
            "fetch_strategy": "previous-cache",
            "citation_value_source": "manual_floor",
            "last_fetch_error": "temporary failure",
            "updated": "2026-08-20 10:00:00",
        }
        for relative_path in DATA_PATHS:
            self.write_json(relative_path, scholar_payload)
        for relative_path in BADGE_PATHS:
            self.write_json(
                relative_path,
                {"schemaVersion": 1, "label": "citations", "message": "229"},
            )

    def write_json(self, relative_path, payload):
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload), encoding="utf-8")

    def read_json(self, relative_path):
        return json.loads((self.root / relative_path).read_text(encoding="utf-8"))

    def snapshot_files(self):
        return {
            relative_path: (self.root / relative_path).read_bytes()
            for relative_path in ALL_PATHS
        }

    def test_parses_and_synchronizes_metrics(self):
        response = {
            "search_metadata": {"status": "Success"},
            "cited_by": {
                "table": [
                    {"citations": {"all": 231, "since_2021": 210}},
                    {"h_index": {"all": 10, "since_2021": 10}},
                    {"i10_index": {"all": 9, "since_2021": 9}},
                ]
            },
        }
        metrics = parse_serpapi_metrics(response)

        self.assertEqual(
            {
                "citedby": 231,
                "citedby5y": 210,
                "hindex": 10,
                "hindex5y": 10,
                "i10index": 9,
                "i10index5y": 9,
            },
            metrics,
        )
        self.assertTrue(
            update_metrics(self.root, metrics, now="2026-08-20 12:00:00")
        )

        for relative_path in DATA_PATHS:
            payload = self.read_json(relative_path)
            self.assertEqual(231, payload["citedby"])
            self.assertEqual(210, payload["citedby5y"])
            self.assertEqual(10, payload["hindex"])
            self.assertEqual(10, payload["hindex5y"])
            self.assertEqual(9, payload["i10index"])
            self.assertEqual(9, payload["i10index5y"])
            self.assertEqual(
                {"paper-id": {"num_citations": 12}}, payload["publications"]
            )
            self.assertEqual("google-scholar-fetcher", payload["fetch_strategy"])
            self.assertEqual(
                "google-scholar-fetcher", payload["citation_value_source"]
            )
            self.assertEqual("2026-08-20 12:00:00", payload["updated"])
            self.assertNotIn("last_fetch_error", payload)

        for relative_path in BADGE_PATHS:
            self.assertEqual("231", self.read_json(relative_path)["message"])

    def test_rejects_failed_or_malformed_serpapi_responses(self):
        invalid_responses = (
            {"error": "invalid API key"},
            {"search_metadata": {"status": "Error"}},
            {"search_metadata": {"status": "Success"}, "cited_by": {"table": []}},
            {
                "search_metadata": {"status": "Success"},
                "cited_by": {"table": [{"citations": {"all": -1}}]},
            },
            {
                "search_metadata": {"status": "Success"},
                "cited_by": {"table": [{"citations": {"all": "231"}}]},
            },
        )
        for response in invalid_responses:
            with self.subTest(response=response):
                with self.assertRaises(ValueError):
                    parse_serpapi_metrics(response)

    def test_rejects_lower_total_without_changing_files(self):
        before = self.snapshot_files()

        with self.assertRaisesRegex(ValueError, "lower than stored value"):
            update_metrics(
                self.root,
                {"citedby": 228, "hindex": 8, "i10index": 8},
            )

        self.assertEqual(before, self.snapshot_files())

    def test_unchanged_metrics_do_not_rewrite_files(self):
        before = self.snapshot_files()

        self.assertFalse(
            update_metrics(
                self.root,
                {
                    "citedby": 229,
                    "citedby5y": 205,
                    "hindex": 8,
                    "hindex5y": 8,
                    "i10index": 8,
                    "i10index5y": 8,
                },
            )
        )

        self.assertEqual(before, self.snapshot_files())

    def test_updates_indices_when_total_is_unchanged(self):
        self.assertTrue(
            update_metrics(
                self.root,
                {
                    "citedby": 229,
                    "citedby5y": 205,
                    "hindex": 10,
                    "hindex5y": 10,
                    "i10index": 10,
                    "i10index5y": 10,
                },
                now="2026-08-20 12:00:00",
            )
        )
        for relative_path in DATA_PATHS:
            payload = self.read_json(relative_path)
            self.assertEqual(229, payload["citedby"])
            self.assertEqual(10, payload["hindex"])
            self.assertEqual(10, payload["i10index"])

    def test_cli_returns_nonzero_without_serpapi_key(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "google_scholar_crawler" / "update_total.py"),
                "--root",
                str(self.root),
            ],
            capture_output=True,
            text=True,
            env={"PATH": str(Path(sys.executable).parent)},
        )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("SERPAPI_API_KEY", result.stderr)


if __name__ == "__main__":
    unittest.main()
