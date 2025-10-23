import { type Locator, type Page } from '@playwright/test';

export class LoginPage {
    // Elementos de la página de login
    readonly page: Page; // Referencia a la página
    readonly username: Locator; // Localizador nombre de usuario
    readonly password: Locator; // Localizador contraseña

    constructor(page: Page) {
        this.page = page; // Inicializar la referencia a la página
        this.username = page.locator('[data-test="username"]'); // Inicializar el localizador nombre de usuario
        this.password = page.locator('[data-test="password"]'); // Inicializar el localizador contraseña
    }

    async login(username: string, password: string) {
        await this.username.fill(username); // Ingresar el nombre de usuario con metodo fill
        await this.password.fill(password); // Ingresar la contraseña con metodo fill
    }

}
