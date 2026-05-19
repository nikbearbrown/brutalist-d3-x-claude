const puppeteer = require('puppeteer');
const path = require('path');

const infographicsDir = __dirname;
const imagesDir = path.join(__dirname, '..', 'images');

const files = [
  { html: 'ch05-fig-01-analyst-vs-reader.html', out: '05-reading-a-dataset-fig-01.jpg' },
  { html: 'ch05-fig-02-decision-tree.html', out: '05-reading-a-dataset-fig-02.jpg' },
  { html: 'ch05-fig-03-audit-flow.html', out: '05-reading-a-dataset-fig-03.jpg' },
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
