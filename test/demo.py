import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def run_playwright():
    print('Starting async Playwright...')
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://google.com")
        print(await page.title())
        await page.screenshot(path="example1.png")
        await browser.close()

print('Starting sync Playwright...')
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    print(page.title())
    page.screenshot(path="example.png")
    browser.close()

asyncio.run(run_playwright())
