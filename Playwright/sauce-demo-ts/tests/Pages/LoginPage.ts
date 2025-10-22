import { type Locator, type Page } from '@playwright/test';

export class LoginPage {
    // Elementos de la página de login
    readonly page: Page; // Referencia a la página
    readonly username: Locator; // Localizador del campo de nombre de usuario
    readonly password: Locator; // Localizador del campo de contraseña

    constructor(page: Page) {
        this.page = page; // Inicializar la referencia a la página
        this.username = page.locator('[data-test="username"]'); // Inicializar el localizador del campo de nombre de usuario
        this.password = page.locator('[data-test="password"]'); // Inicializar el localizador del campo de contraseña
    }

    
    async gotoSauceDemo() {
        await this.page.goto('');
    }

    async login(username: string, password: string) {
        await this.username.fill(username);
        await this.password.fill(password);
    }

}