class BasePage:
    def __init__(self, page):
        self.page = page
        
    async def screenshot(self, name):
        await self.page.screenshot(path=f"screenshots/{name}.png")