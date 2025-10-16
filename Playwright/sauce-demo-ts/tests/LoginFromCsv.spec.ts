import { test, expect } from '@playwright/test';
import readUsersCsv from './utils/csvReader';
import * as path from 'path';

const csvPath = path.join(__dirname, 'data', 'users.csv');
const users = readUsersCsv(csvPath);

test.describe('Login desde CSV', () => {
  for (const user of users) {
    test(`Login para ${user.username}`, async ({ page }) => {
      await page.goto('');
      await expect(page).toHaveURL('https://www.saucedemo.com/');

      await page.locator('[data-test="username"]').fill(user.username);
      await expect(page.locator('[data-test="username"]')).toHaveValue(user.username);

      await page.locator('[data-test="password"]').fill(user.password);
      await expect(page.locator('[data-test="password"]')).toHaveValue(user.password);

      await page.locator('[data-test="login-button"]').click();

      // Comprobación simple: si el usuario es 'locked_out_user' la app muestra un error
      if (user.username === 'locked_out_user') {
        await expect(page.locator('[data-test="error"]')).toBeVisible();
      } else {
        await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
      }
    });
  }
});
