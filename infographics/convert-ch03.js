const puppeteer = require('puppeteer');
const path = require('path');

const infographicsDir = __dirname;
const imagesDir = path.join(__dirname, '..', 'images');

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const htmlPath = path.join(infographicsDir, 'ch03-fig-05-channel-taxonomy.html');
  const outPath = path.join(imagesDir, '03-marks-and-channels-fig-05.jpg');

  console.log('Processing ch03-fig-05-channel-taxonomy.html -> 03-marks-and-channels-fig-05.jpg');

  const page = await browser.newPage();
  await page.setViewport({ width: 1600, height: 900 });

  const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
  await page.goto(fileUrl, { waitUntil: 'networkidle0', timeout: 30000 });
  await page.waitForSelector('svg', { timeout: 10000 });
  await new Promise(r => setTimeout(r, 2000));

  await page.screenshot({
    path: outPath,
    type: 'jpeg',
    quality: 92,
    clip: { x: 0, y: 0, width: 1600, height: 900 }
  });

  console.log('  Saved:', outPath);
  await page.close();
  await browser.close();
  console.log('Done.');
})();
