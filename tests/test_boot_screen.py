"""Tests — boot screen removed regression coverage."""
from playwright.sync_api import expect

from tests.pages.portfolio_page import PortfolioPage


class TestBootScreenRemoval:
    """Verify the site loads directly into the main content without an intro overlay."""

    def test_boot_screen_overlay_is_absent(self, portfolio_local: PortfolioPage) -> None:
        """The old #bootScreen element must no longer exist in the DOM."""
        expect(portfolio_local._page.locator("#bootScreen")).to_have_count(0)

    def test_main_content_is_visible_immediately(self, portfolio_local: PortfolioPage) -> None:
        """Navigation and hero content should be visible right after the page opens."""
        expect(portfolio_local.nav.nav).to_be_visible()
        expect(portfolio_local.hero.section).to_be_visible()

    def test_hero_terminal_links_are_available_without_dismiss(
        self, portfolio_local: PortfolioPage
    ) -> None:
        """Hero links must be usable without any boot-screen interaction."""
        expect(portfolio_local._page.locator(".hero-terminal a[href='#projects']")).to_be_visible()
        expect(portfolio_local._page.locator(".hero-terminal a[href='#contact']")).to_be_visible()

