from playwright.sync_api import Page, expect
import pytest
# playwright codegen --device="iPhone 13" saucedemo.com

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {**playwright.devices["iPhone 13"]}

def test_example(page: Page) -> None:
    print('Starting sync Playwright...')
    page.goto("https://www.saucedemo.com/")
    page.pause()
    # page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    # page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")



# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args, playwright):
#     return {"viewport": {"width": 500, "height": 500}}

def test_example2(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"login-button\"]").click()
    page.locator("[data-test=\"login-credentials\"]").click()
    page.locator("[data-test=\"login-password\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_have_text("Epic sadface: Username is required")
