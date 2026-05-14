# Bubble Chart

*Education Correlates With Longevity —But Population Scale Varies Dramatically*

![Bubble Chart](../images/24-bubble-chart.jpg)

## What this chart is

A bubble chart is a **trivariate scatter plot** : it places data points on a Cartesian grid using position (x, y) to encode two quantitative variables, then encodes a third variable through circle area. The perceptual mechanism exploited is **position along a common axis** — the most accurate channel in Cleveland and McGill's encoding hierarchy — supplemented by **area** , which is less accurate but allows a third quantitative dimension without adding a spatial axis. Color and stroke pattern layer in a fourth variable: categorical region membership.

## Why it was chosen

The data contains three quantitative variables (education, life expectancy, population) and one categorical variable (region) — a structure that cannot be represented by any two-variable chart without discarding information. A scatter plot loses population. A bar chart loses the correlation structure entirely. A bubble chart is the **minimum-distortion solution** for this data shape. The message — that education and longevity correlate, but that population scale differs enormously across regions — requires simultaneously visible x/y correlation and visible size variation. This chart delivers both.

## What the alternative would break

The nearest alternative, a **grouped bar chart** , could show either education or life expectancy by country but cannot encode population size except through supplementary labeling. More critically, it destroys the **correlation structure** : the viewer sees regional averages or individual bars — not the relationship between the two variables. Countries where education is high but life expectancy lags (or vice versa) become invisible. A **stacked area chart** fails for different reasons: stacking requires values that sum to a meaningful total — this data has no such property.

## The hard limits

Bubble charts fail at **scale** : beyond 30–40 bubbles, occlusion from overlapping circles degrades legibility. This implementation addresses overlap with semi-transparent fills ( `fill-opacity: 0.75` ) and renders largest bubbles first so smaller ones remain visible above them. The second hard limit — and the most common implementation error — is encoding size by radius rather than area. Encoding by radius causes exponential visual distortion: a circle twice the radius appears four times as large. This chart uses `d3.scaleSqrt()` , mapping population values to radius such that **area scales linearly with the data** .

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained bubble chart in D3 v7. Two files:

1. `bubble-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Bubble Chart" and the slide subtitle is "Education Correlates With Longevity —But Population Scale Varies Dramatically".

2. `bubble-chart/data.json` — the data file the chart loads via `d3.json("./bubble-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Global human development indicators by country, 2024 estimates. Fictional placeholder — realistic values derived from public HDI data. Proves the visualization renders before real data is substituted.
  - `id`: string — ISO 3166-1 alpha-3 country code (used as bubble label for large populations)
  - `country`: string — full country name for tooltip display
  - `region`: string — world region: Africa | Americas | Asia | Europe | Oceania
  - `education`: number — Education Index (HDI component), scale 0–1
  - `lifeExpectancy`: number — average life expectancy at birth, years
  - `population`: number — estimated population in millions
  - `gdpPerCapita`: number — GDP per capita, current USD

Encoding: use the perceptually honest channel for this chart type (bubble chart). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **W. E. B. Du Bois** designed a series of data visualizations — including proportional bubbles, circular flow diagrams, and color-coded maps — for the 1900 Paris Exposition's *Exhibit of American Negroes*. They are among the most visually inventive infographics of any era.

![W. E. B. Du Bois, circa 1900. AI-generated portrait based on a public domain photograph.](../images/w-e-b-du-bois.jpg)
*W. E. B. Du Bois, circa 1900. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was W. E. B. Du Bois, and how does his 1900 Paris Exposition data visualization work connect to the bubble chart we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"W. E. B. Du Bois"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to describe one specific Du Bois plate from the 1900 Exposition — what data, what encoding, what argument.
- Ask it to compare Du Bois's hand-drawn statistical art with the modern automated chart-generation pipelines.

What changes? What gets better? What gets worse?
