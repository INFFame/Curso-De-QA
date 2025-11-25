class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator('input#sb_form_q')

    async def navigate(self):
        await self.page.goto("https://bing.com")

    async def search(self, text):
        await self.search_term_input.fill(text)
        await self.search_term_input.press("Enter")