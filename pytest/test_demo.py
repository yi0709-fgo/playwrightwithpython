from playwright.sync_api import Page
import pytest

@pytest.mark.only_browser("chromium")
def test_page_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

@pytest.mark.only_browser("chromium")
def test_inventory_h3(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."

# def test_wrong_match(page: Page):
#     page.goto("https://www.saucedemo.com/")
#     assert page.inner_text("h3") == "Epic sadface: Username and password do not match any user in this service"