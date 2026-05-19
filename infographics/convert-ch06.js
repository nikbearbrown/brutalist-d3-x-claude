const puppeteer = require('puppeteer');
const path = require('path');

const infographicsDir = __dirname;
const imagesDir = path.join(__dirname, '..', 'images');

const files = [
  { html: 'ch06-fig-01-vague-vs-fourmove.html', out: '06-working-with-claude-code-fig-01.jpg' },
  { html: 'ch06-fig-02-annotated-prompt.html', out: '06-working-with-claude-code-fig-02.jpg' },
  { html: 'ch06-fig-03-iteration-loop.html', out: '06-working-with-claude-code-fig-03.jpg' },
  { html: 'ch06-fig-04-pipeline.html', out: '06-working-with-claude-code-fig-04.jpg' },
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
