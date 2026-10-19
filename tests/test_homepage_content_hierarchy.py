import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HomepageContentHierarchyTest(unittest.TestCase):
    def setUp(self):
        self.about = (ROOT / "_pages" / "about.md").read_text(encoding="utf-8")
        self.styles = (ROOT / "assets" / "css" / "main.scss").read_text(
            encoding="utf-8"
        )

    def test_sidebar_uses_compact_research_tagline(self):
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        profile = (ROOT / "_includes" / "author-profile.html").read_text(
            encoding="utf-8"
        )
        sidebar_styles = (ROOT / "_sass" / "_sidebar.scss").read_text(
            encoding="utf-8"
        )

        self.assertIn(
            'tagline          : "3D/4D Vision · World Models · Graphics · Multimodal AI"',
            config,
        )
        self.assertIn("{{ author.tagline }}", profile)
        self.assertNotIn("{{ site.description }}", profile)
        self.assertIn("white-space: normal", sidebar_styles)
        self.assertIn("overflow-wrap: anywhere", sidebar_styles)

    def test_about_has_bilingual_research_positioning(self):
        self.assertIn("I study how to reconstruct, generate, render, and simulate", self.about)
        self.assertIn("我致力于动态 3D/4D 世界的重建、生成、渲染与仿真", self.about)
        self.assertEqual(self.about.count('class="research-focus-links"'), 8)

    def test_news_is_scannable_and_earlier_items_are_collapsed(self):
        news = self.about.split("🔥 News", 1)[1].split("📝 Publications", 1)[0]

        self.assertEqual(news.count('class="news-more"'), 2)
        self.assertLess(
            news.index("EventTracer</strong></a> is accepted"),
            news.index("ConsistNav</strong></a> is released"),
        )
        self.assertLess(
            news.index("ConsistNav</strong></a> is released"),
            news.index("PatternGSL</strong></a> is accepted"),
        )

    def test_core_publications_have_short_takeaways(self):
        self.assertEqual(self.about.count('class="publication-summary"'), 5)
        self.assertIn(".publication-summary", self.styles)
        self.assertIn(".news-more summary", self.styles)

    def test_erf_gs_uses_official_ieee_xplore_page(self):
        ieee_url = "https://ieeexplore.ieee.org/document/11733892"

        self.assertEqual(self.about.count(ieee_url), 6)
        self.assertIn(f"[IEEE Xplore]({ieee_url})", self.about)
        self.assertIn("[arXiv](https://arxiv.org/abs/2608.08531)", self.about)

    def test_research_focus_includes_requested_representative_works(self):
        representative_urls = {
            "MASIV": "https://arxiv.org/abs/2508.01112",
            "Editable NeRF": "https://arxiv.org/abs/2405.07306",
            "Temporal Attention": "https://proceedings.neurips.cc/paper_files/paper/2022/file/5820ad65b1c27411417ae8b59433e580-Paper-Conference.pdf",
        }

        for label, url in representative_urls.items():
            with self.subTest(work=label):
                self.assertEqual(self.about.count(url), 3)
                self.assertEqual(self.about.count(f">{label}</a>"), 2)


if __name__ == "__main__":
    unittest.main()
