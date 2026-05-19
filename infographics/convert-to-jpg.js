const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

const files = [
  { html: 'fig-01-prompt-comparison.html', out: '02-claude-basics-for-d3-visualization-fig-01.jpg' },
  { html: 'fig-02-instruction-budget.html', out: '02-claude-basics-for-d3-visualization-fig-02.jpg' },
  { html: 'fig-03-four-move-prompt.html', out: '02-claude-basics-for-d3-visualization-fig-03.jpg' },
  { html: 'fig-04-verification-stack.html', out: '02-claude-basics-for-d3-visualization-fig-04.jpg' },
  { html: 'fig-05-workflow.html', out: '02-claude-basics-for-d3-visualization-fig-05.jpg' },
];

const infographicsDir = __dirname;
const imagesDir = path.join(__dirname, '..', 'images');

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

    // Wait for D3 to render and fonts to load
    await page.waitForSelector('svg', { timeout: 10000 });
    await new Promise(r => setTimeout(r, 2000));

    await page.screenshot({
      path: outPath,
      type: 'jpeg',
      quality: 92,
      clip: { x: 0, y: 0, width: 1600, height: 900 }
    });

    console.log(`  Saved: ${outPath}`);
    await page.close();
  }

  await browser.close();
  console.log('\nDone. All 5 infographics converted to JPG.');
})();
