from pages.base_page import BasePage

class LoginPage(BasePage):
    # Localizadores
    username_input = "#user-name"
    password_input = "#password"
    login_button = "#login-button"
    
    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")
        
    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)