const puppeteer = require('puppeteer');
const path = require('path');

const infographicsDir = __dirname;
const imagesDir = path.join(__dirname, '..', 'images');

const files = [
  { html: 'ch08-fig-01-bar-vs-line-baseline.html', out: '08-time-series-and-temporal-charts-fig-01.jpg' },
  { html: 'ch08-fig-02-temporal-forms.html', out: '08-time-series-and-temporal-charts-fig-02.jpg' },
  { html: 'ch08-fig-03-area-baseline.html', out: '08-time-series-and-temporal-charts-fig-03.jpg' },
  { html: 'ch08-fig-04-missing-data.html', out: '08-time-series-and-temporal-charts-fig-04.jpg' },
  { html: 'ch08-fig-05-stacked-area-accuracy.html', out: '08-time-series-and-temporal-charts-fig-05.jpg' },
  { html: 'ch08-fig-06-line-vs-spiral.html', out: '08-time-series-and-temporal-charts-fig-06.jpg' },
];

(async () => {
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  for (const f of files) {
    const htmlPath = path.join(infographicsDir, f.html);
    const outPath = path.join(imagesDir, f.out);
    console.log(`Processing ${f.html} -> ${f.out}`);

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
  }

  await browser.close();
  console.log('Done.');
})();
