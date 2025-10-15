import { defineConfig } from '@playwright/test';
export default defineConfig({
    use: {
        baseURL: 'https://www.saucedemo.com',
        headless: true,
        trace: 'on',
    },
    testDir: './tests',
    reporter: [['html', { outputFolder: 'playwright-report', open: 'never' }]],
});