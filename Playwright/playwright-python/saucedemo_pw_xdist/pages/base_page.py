class BasePage:
    def __init__(self, page):
        self.page = page
        
    def screenshot(self, name):
        self.page.screenshot(path=f"screenshots/{name}.png")