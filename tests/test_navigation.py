import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def setup(page: Page):
    # Navigate to base URL before each test
    page.goto("http://localhost:1313")


def test_home_page(page: Page):
    """Test the home page structure and content."""
    # Check if we're on the home page
    expect(page).to_have_url("http://localhost:1313/")

    # Verify header is present
    header = page.locator("header")
    expect(header).to_be_visible()

    # Verify the two-column layout
    columns = page.locator(".container > div")
    expect(columns).to_have_count(2)

    # Verify column content - just check that they exist and are visible
    left_column = page.locator(".container > div:first-child")
    right_column = page.locator(".container > div:last-child")
    expect(left_column).to_be_visible()
    expect(right_column).to_be_visible()


def test_lessons_page(page: Page):
    """Test the lessons listing page."""
    # Navigate to lessons page
    page.goto("http://localhost:1313/lessons")

    # Verify URL (with trailing slash)
    expect(page).to_have_url("http://localhost:1313/lessons/")

    # Basic structure checks
    container = page.locator(".container")
    expect(container).to_be_visible()

    # Verify layout
    columns = page.locator(".container > div")
    expect(columns).to_have_count(2)


def test_first_lesson_page(page: Page):
    """Test the first lesson page structure and content."""
    # Navigate to first lesson
    page.goto("http://localhost:1313/lessons/first")

    # Verify URL (with trailing slash)
    expect(page).to_have_url("http://localhost:1313/lessons/first/")

    # Verify the three-column layout specific to single pages
    columns = page.locator(".container > div")
    expect(columns).to_have_count(3)

    # Check for table of contents - using more specific selector
    toc = page.locator("#TableOfContents")
    expect(toc).to_be_visible()

    # Verify content area
    content = page.locator(".prose")
    expect(content).to_be_visible()

    # Verify sidebar visibility on desktop
    left_sidebar = page.locator(".container > div:first-child")
    classes = left_sidebar.get_attribute("class")
    assert classes is not None
    assert "hidden" in classes, "Sidebar should have 'hidden' class"
    assert "xl:block" in classes, "Sidebar should have 'xl:block' class"


def test_navigation_flow(page: Page):
    """Test navigation between pages using links."""
    # Start at home page
    page.goto("http://localhost:1313")

    # Navigate to lessons page and verify (with trailing slash)
    page.click("text=Lessons")
    expect(page).to_have_url("http://localhost:1313/lessons/")

    # Navigate to first lesson (with trailing slash)
    page.click("text=Python Lesson")  # Assuming the link text contains "First"
    expect(page).to_have_url("http://localhost:1313/lessons/first/")

    # Navigate back home using header link
    page.locator("header a").click()
    expect(page).to_have_url("http://localhost:1313/")
