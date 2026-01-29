export async function tomarScreenshot(test: any, page: any, name: string){
    await test.info().attach(name, {
        body: await page.screenshot({ fullPage: true }),
        contentType: 'image/png'
    });
}