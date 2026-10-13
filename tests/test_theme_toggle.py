import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ThemeToggleTest(unittest.TestCase):
    def test_theme_is_initialized_before_the_stylesheet(self):
        head = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")

        self.assertIn('localStorage.getItem("preferred-theme")', head)
        self.assertIn('(prefers-color-scheme: dark)', head)
        self.assertIn('setAttribute("data-theme", theme)', head)
        self.assertLess(
            head.index('setAttribute("data-theme", theme)'),
            head.index('rel="stylesheet"'),
        )

    def test_masthead_has_an_accessible_icon_toggle(self):
        masthead = (ROOT / "_includes" / "masthead.html").read_text(
            encoding="utf-8"
        )

        self.assertIn("data-theme-toggle", masthead)
        self.assertIn('aria-label="Switch to dark mode"', masthead)
        self.assertIn("fa-moon", masthead)
        self.assertIn("fa-sun", masthead)
        self.assertIn("data-theme-toggle-label", masthead)

    def test_theme_choice_is_persisted_and_localized(self):
        scripts = (ROOT / "_includes" / "scripts.html").read_text(
            encoding="utf-8"
        )

        self.assertIn('localStorage.setItem(storageKey, theme)', scripts)
        self.assertIn('meta[name="theme-color"]', scripts)
        self.assertIn('"切换至深色模式"', scripts)
        self.assertIn('"切换至浅色模式"', scripts)
        self.assertIn('systemTheme.addEventListener("change"', scripts)

    def test_dark_palette_covers_primary_surfaces(self):
        styles = (ROOT / "assets" / "css" / "main.scss").read_text(
            encoding="utf-8"
        )

        self.assertIn('html[data-theme="dark"]', styles)
        self.assertIn("--theme-bg: #111418", styles)
        self.assertIn(".lang-switcher", styles)
        self.assertIn(".research-focus-item", styles)
        self.assertIn(".author__wechat-panel", styles)
        self.assertIn(".greedy-nav .hidden-links", styles)

    def test_desktop_sidebar_links_remain_unframed(self):
        styles = (ROOT / "assets" / "css" / "main.scss").read_text(
            encoding="utf-8"
        )

        self.assertIn(
            """@include breakpoint($large) {
    .author__urls {
        border: 0;
        background: transparent;
        box-shadow: none;
    }
}""",
            styles,
        )


if __name__ == "__main__":
    unittest.main()
