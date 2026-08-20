import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "update-google-scholar.yml"
EXPECTED_DATA_PATHS = {
    "results/gs_data.json",
    "_data/scholar.json",
    "google_scholar_crawler/results/gs_data.json",
    "results/gs_data_shieldsio.json",
    "google_scholar_crawler/results/gs_data_shieldsio.json",
}


class ScholarWorkflowTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = WORKFLOW.read_text(encoding="utf-8")

    def test_uses_daily_pinned_no_secret_fetcher(self):
        self.assertEqual(1, self.workflow.count("cron:"))
        self.assertIn("cron: '17 2 * * *'", self.workflow)
        self.assertIn("uses: actions/checkout@v4", self.workflow)
        self.assertIn(
            "uses: sxlllslgh/google-scholar-fetcher@"
            "4a30641f7dab085f01f99c38d38069d8aec2496f",
            self.workflow,
        )
        self.assertIn("google-scholar-id: r9f4mLMAAAAJ", self.workflow)
        self.assertIn("record-file: /tmp/scholar-record.json", self.workflow)
        self.assertIn(
            "run: python3 google_scholar_crawler/update_total.py "
            "/tmp/scholar-record.json --root .",
            self.workflow,
        )
        self.assertNotIn("SERPAPI_API_KEY", self.workflow)
        self.assertNotIn("pip install", self.workflow)

    def test_commit_step_stages_only_runtime_data_files(self):
        self.assertNotIn("git add -A", self.workflow)
        start = self.workflow.index("git add --")
        end = self.workflow.index("\n          if ", start)
        git_add_block = self.workflow[start:end]
        staged_paths = set(re.findall(r"[\w./-]+\.json", git_add_block))

        self.assertEqual(EXPECTED_DATA_PATHS, staged_paths)


if __name__ == "__main__":
    unittest.main()
