import asyncio
from pageObjects.SearchPage import SearchPage
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        search_page = SearchPage(page)
        await search_page.navigate()
        await search_page.search("Colo Colo campeón")
        await page.screenshot(path="search_results.png")
        print(await page.title())
        await browser.close()
        
asyncio.run(main())