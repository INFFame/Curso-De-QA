const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { ProductPage } = require('../pages/ProductPage');
const { CartPage } = require('../pages/CartPage');
const { credentials, products } = require('./testData');

test('Agregar productos al carrito en saucedemo', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const cartPage = new CartPage(page);

  // Paso 1: Login
  await loginPage.navigate();
  await loginPage.login(credentials.username, credentials.password);

});