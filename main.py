import asyncio
from playwright.async_api import async_playwright


async def run_automation():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto("https://example.com", timeout=30000)
            print(f"Page title: {await page.title()}")

            await page.screenshot(path="screenshot.png")
            print("Screenshot saved: screenshot.png")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(run_automation())
