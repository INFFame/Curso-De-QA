# Clase que representa la página de login
class LoginPage:
    # Constructor de la clase
    def __init__(self, page):
        # Asignar la página de Playwright a un atributo de la clase
        self.page = page
        # Definir los selectores de los elementos de la página
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.agregar_producto_button = page.get_by_role("button", name="Add to cart").nth(0)
    
    # Método para realizar login    
    def login(self, username, password):
        # Rellenar los campos de usuario y contraseña y hacer clic en el botón de login
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        