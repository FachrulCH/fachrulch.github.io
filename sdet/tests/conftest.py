import pytest
from pathlib import Path
from playwright.sync_api import Page


@pytest.fixture(scope="session")
def challenge_url():
    """Return the file:// URL for the SDET challenge page."""
    html_path = Path(__file__).parent.parent / "sdet-challenge.html"
    return f"file://{html_path.resolve()}"


@pytest.fixture()
def page(page: Page, challenge_url: str):
    """Navigate to the challenge page before each test."""
    page.goto(challenge_url)
    page.wait_for_load_state("domcontentloaded")
    return page
