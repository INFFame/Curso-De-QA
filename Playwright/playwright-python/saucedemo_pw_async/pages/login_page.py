from pages.base_page import BasePage

class LoginPage(BasePage):
    # Localizadores
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    
    async def navegar(self):
        await self.page.goto("https://www.saucedemo.com/")
        
    async def login(self, username, password):
        await self.page.fill(self.username_input, username)
        await self.page.fill(self.password_input, password)
        await self.page.click(self.login_button)