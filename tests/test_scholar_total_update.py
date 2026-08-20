import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from google_scholar_crawler.update_total import calculate_total, update_total


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
            "hindex": 8,
            "i10index": 8,
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

    def test_calculates_and_synchronizes_higher_total(self):
        records = [{"citations": 120}, {"citations": 111}, {}]
        total = calculate_total(records)

        self.assertEqual(231, total)
        self.assertTrue(update_total(self.root, total, now="2026-08-20 12:00:00"))

        for relative_path in DATA_PATHS:
            payload = self.read_json(relative_path)
            self.assertEqual(231, payload["citedby"])
            self.assertEqual(8, payload["hindex"])
            self.assertEqual(8, payload["i10index"])
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

    def test_rejects_empty_or_malformed_publication_records(self):
        with self.assertRaisesRegex(ValueError, "publication list is empty"):
            calculate_total([])

        invalid_records = (
            [{"citations": -1}],
            [{"citations": "12"}],
            {"citations": 12},
            ["not-a-publication"],
        )
        for records in invalid_records:
            with self.subTest(records=records):
                with self.assertRaises(ValueError):
                    calculate_total(records)

    def test_rejects_lower_total_without_changing_files(self):
        before = self.snapshot_files()

        with self.assertRaisesRegex(ValueError, "lower than stored total"):
            update_total(self.root, 228)

        self.assertEqual(before, self.snapshot_files())

    def test_unchanged_total_does_not_rewrite_files(self):
        before = self.snapshot_files()

        self.assertFalse(update_total(self.root, 229))

        self.assertEqual(before, self.snapshot_files())

    def test_cli_returns_nonzero_for_malformed_record_file(self):
        record_file = self.root / "records.json"
        record_file.write_text('[{"citations": "invalid"}]', encoding="utf-8")

        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "google_scholar_crawler" / "update_total.py"),
                str(record_file),
                "--root",
                str(self.root),
            ],
            capture_output=True,
            text=True,
        )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("citation value must be a non-negative integer", result.stderr)


if __name__ == "__main__":
    unittest.main()
