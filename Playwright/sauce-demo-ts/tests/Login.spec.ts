import { test, expect } from '@playwright/test';
import { LoginPage } from './Pages/LoginPage';


test.describe('Pruebas iterando usernames desde la página', () => {
    test('Obtener usernames listados en la página y probar login con cada uno', async ({ page }) => {
        await test.step('Ingresar a la pagina de Sauce Demo', async () => {
            const loginPage = new LoginPage(page);
            // Ir a la página de login
            await loginPage.gotoSauceDemo();
            await expect(page).toHaveURL('https://www.saucedemo.com/');
        });
        

        await test.step('Obtener usernames de la página', async () => {
            // Localizar el contenedor donde se muestran los "Accepted usernames"
            const usersLocator = page.locator('.login_credentials');
            await expect(usersLocator).toBeVisible();

            // Extraer texto y procesar usernames
            const text = await usersLocator.innerText();
            // Dividir el texto en líneas y filtrar usernames
            const usernames = text
                .split('\n') // divide por líneas
                .map(line => line.trim()) // elimina espacios en blanco
                .filter(line => /^[a-z0-9_]+$/i.test(line)); // filtra solo palabras tipo usernames

                
            // Iterar sobre cada username encontrado en la página
            for (const username of usernames) {
                await test.step(`Probar login con el username: ${username}`, async () => {
                    await test.step('Ingresar usuario y contraseña', async () => {
                        const loginPage = new LoginPage(page);
                        const demoPassword = 'secret_sauce';
                        // Ingresar usuario y verificar
                        await loginPage.login(username, demoPassword);
                        await expect(loginPage.username).toHaveValue(username);
                        await expect(loginPage.password).toHaveValue(demoPassword);
                    });
                    
                    await test.step('Hacer click en botón Login', async () => {
                        const loginPage = new LoginPage(page);
                        await test.info().attach('screenshot', { body: await page.screenshot(), contentType: 'image/png' });
                        // Hacer click en login y verificar resultado según usuario
                        await page.locator('[data-test="login-button"]').click();

                        // Verificar resultado del login
                        if (username === 'locked_out_user') {
                            // Usuario bloqueado debe mostrar error
                            await expect(page.locator('[data-test="error"]')).toBeVisible();
                            // Volver a la página de login para la siguiente iteración
                            await loginPage.gotoSauceDemo();
                            await expect(page).toHaveURL('https://www.saucedemo.com/');

                        } else {
                            // Para los demás usuarios, debemos llegar al inventario
                            await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
                            // Volver a la página de login para la siguiente iteración
                            await loginPage.gotoSauceDemo();
                            await expect(page).toHaveURL('https://www.saucedemo.com/');

                        }
                    })

                });
            }
        });

    });
});