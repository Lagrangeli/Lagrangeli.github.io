import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_NAMES = (
    "Zhenyang LI - CV - phd.pdf",
    "Zhenyang LI - CV - phd - zh.pdf",
)


class CvPaginationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_bilingual_cv.py")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

    def test_first_page_continues_publication_list(self):
        expected_title = "Enhanced Velocity Field Modeling for Gaussian Video Reconstruction"
        for pdf_name in PDF_NAMES:
            result = subprocess.run(
                ["pdftotext", "-f", "1", "-l", "1", str(ROOT / pdf_name), "-"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertIn(expected_title, result.stdout, pdf_name)

    def test_generated_cvs_remain_two_pages(self):
        for pdf_name in PDF_NAMES:
            result = subprocess.run(
                ["qpdf", "--show-npages", str(ROOT / pdf_name)],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertEqual("2", result.stdout.strip(), pdf_name)


if __name__ == "__main__":
    unittest.main()
