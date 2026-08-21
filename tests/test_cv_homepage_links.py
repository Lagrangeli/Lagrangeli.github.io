import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT_PAGE = ROOT / "_pages" / "about.md"


class CvHomepageLinksTest(unittest.TestCase):
    def test_homepage_uses_current_bilingual_cv_pdfs(self):
        about = ABOUT_PAGE.read_text(encoding="utf-8")

        self.assertIn(
            'href="/assets/pdf/Zhenyang_Li_CV_202608.pdf"',
            about,
        )
        self.assertIn(
            'href="/assets/pdf/Zhenyang_Li_CV_ZH_202608.pdf"',
            about,
        )
        self.assertNotIn("Zhenyang_Li_CV_20260603_fast.pdf", about)
        self.assertNotIn("Zhenyang_Li_CV_ZH_20260603_fast.pdf", about)


if __name__ == "__main__":
    unittest.main()
