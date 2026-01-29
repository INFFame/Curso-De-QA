import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { ProductsPage } from '../pages/ProductsPage';
import { tomarScreenshot } from '../utils/screenshot';


test.describe('Tests de login en SauceDemo', () => {
    test('Login exitoso en SauceDemo', async ({ page }) => {
        const login = new LoginPage(page);
        const products = new ProductsPage(page);
        
        await page.goto('/');

        await tomarScreenshot(test, page, 'pantalla-inicial');
        
        await test.step('Realizar login', async () => {
           await login.login(process.env.USER!, process.env.PASSWORD!); 
        });

        await tomarScreenshot(test, page, 'pantalla-products');

        await test.step('Validar pantalla Products', async () => {
            await products.isLoaded();
            await expect(products.productsTitle).toBeVisible();
        });

    });
    
});
