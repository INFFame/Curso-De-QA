// Prueba para testear agregar 1 producto al carrito usando datos desde testData.js

const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { ProductPage } = require('../pages/ProductPage');
const { CartPage } = require('../pages/CartPage');
const { credentials, products } = require('./data/testData');

test('Agregar 1 producto al carrito en saucedemo', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const cartPage = new CartPage(page);

  // Paso 1: Login
  await loginPage.navigate();
  await loginPage.login(credentials.username, credentials.password);

  // Paso 2: Agregar solo el primer producto
  await productPage.addProductToCartByButton(products.list[0]);

  // Paso 3: Ir al carrito
  await productPage.goToCart();

  // Paso 4: Verificar producto en el carrito
  const items = await cartPage.getCartItems();
  expect(items).toContain(products.list[0]); // Verifica que el primer producto esté en el carrito

});
