# Choropleth

*Choropleth Map — GDP per Capita*

![Choropleth](../images/29-choropleth.jpg)

## The perceptual mechanism

A choropleth map exploits **colour saturation and lightness** as an encoding channel for a continuous quantitative variable across pre-defined geographic regions. The viewer's visual system performs an effortless pre-attentive scan — dark regions read as high, light regions as low — without requiring them to decode any axis or scale. This makes geographic concentration, clustering, and outliers immediately visible at a glance.

The critical perceptual dependency: this only works when the colour ramp is **perceptually uniform** — equal data steps must produce equal apparent colour steps. Non-uniform ramps (naive RGB interpolation) create false visual boundaries in the middle of a continuous range.

## Why it was chosen for this data

The data structure is a **one-to-one mapping of a normalized continuous variable to geographic regions** (countries). The message is about geographic variation — where in the world is the value high, where is it low, and what spatial clusters emerge? That question is fundamentally spatial, so the encoding must be spatial. A bar chart of 150+ countries would require sorting to be readable and would destroy the geographic signal entirely.

A **logarithmic scale** is applied by default because GDP per capita spans three orders of magnitude ($200–$130,000). On a linear scale, most of the world compresses into the bottom 10% of the ramp and the entire map appears nearly uniform. The log scale restores perceptual resolution across the full income range.

## What the alternative would break

The next-best alternative for this message is a **bubble map** (proportional symbol map) — circles sized by value, centred on each country. It would be more accurate for precise comparison (area encodes magnitude, which is more readable than hue), but it fails for small countries (circles overlap in Western Europe, the Caribbean, Southeast Asia) and it cannot show the continuous geographic gradient that makes a choropleth visually compelling. The choropleth wins here because the message is about *pattern across space* , not precise comparison of individual countries.

A **nine-slice pie chart or stacked bar** would be a categorical error — this data is not compositional and does not sum to a meaningful whole.

## The one design decision worth knowing

The colour ramp interpolates from **#F5EBE0 (pale parchment) to #3B1A07 (deep espresso)** — both pulled from the walnut end of the hai palette. This is a single-hue sequential ramp, which is perceptually honest: there is one direction of change (low → high), so there should be one direction of colour change. Diverging ramps (two hues meeting at a midpoint) are reserved for data with a meaningful zero or threshold — not for a one-directional continuous variable like income.

## Framework reference

> // Framework — FT Visual Vocabulary FT Visual Vocabulary category: Location — "Where things are, geographic patterns and distributions." Abela quadrant: Comparison (comparing a single metric across many geographic units). Tufte principle applied: the map is the data; no redundant ink outside the colour encoding and necessary reference labels.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained choropleth in D3 v7. Two files:

1. `choropleth.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Choropleth" and the slide subtitle is "Choropleth Map — GDP per Capita".

2. `choropleth/data.json` — the data file the chart loads via `d3.json("./choropleth/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- World countries with a normalized continuous variable (GDP per capita, USD). Each entry maps an ISO 3166-1 alpha-3 country code to a numeric value. Replace 'value' with your real normalized metric — population density, literacy rate, HDI, etc. Never encode raw totals; always normalize per area, per capita, or as a rate.
  - `id`: string — ISO 3166-1 alpha-3 country code (e.g. 'USA', 'DEU')
  - `name`: string — display name for tooltip
  - `value`: number — normalized metric value (here: GDP per capita USD, 2023 estimate)
  - `region`: string — continental region for optional filter

Encoding: use the perceptually honest channel for this chart type (choropleth). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
