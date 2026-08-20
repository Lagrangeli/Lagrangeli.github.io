import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CvScholarSyncTest(unittest.TestCase):
    def test_generated_pdfs_use_homepage_scholar_metrics(self):
        scholar = json.loads((ROOT / "_data" / "scholar.json").read_text(encoding="utf-8"))
        expected = (
            f"{scholar['citedby']} citations, h-index {scholar['hindex']}, "
            f"i10-index {scholar['i10index']}"
        )

        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_bilingual_cv.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        for pdf_name in ("Zhenyang LI - CV - phd.pdf", "Zhenyang LI - CV - phd - zh.pdf"):
            result = subprocess.run(
                ["pdftotext", str(ROOT / pdf_name), "-"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn(expected, result.stdout, pdf_name)


if __name__ == "__main__":
    unittest.main()
