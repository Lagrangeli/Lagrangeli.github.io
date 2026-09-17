import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CvScholarSyncTest(unittest.TestCase):
    def test_generated_pdfs_link_scholar_without_metrics(self):
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
            self.assertIn("Google Scholar", result.stdout, pdf_name)
            self.assertNotIn("citations", result.stdout, pdf_name)
            self.assertNotIn("h-index", result.stdout, pdf_name)
            self.assertNotIn("i10-index", result.stdout, pdf_name)


if __name__ == "__main__":
    unittest.main()
