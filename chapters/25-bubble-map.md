# Bubble Map

*California and Texas Absorb Nearly Half of All Household Aid Disbursements*

![Bubble Map](../images/25-bubble-map.jpg)

## What this chart is

A proportional symbol map encodes a quantitative variable as the area of a circle placed at a geographic centroid. The active perceptual channel is 2D size estimation — viewers compare circle footprints to judge relative magnitude. Because the symbol is anchored to a point rather than filling the administrative polygon, the encoding decouples visual weight from geographic area entirely. Wyoming and Rhode Island receive equally legible circles regardless of how much land each occupies.

This chart type belongs to the FT Visual Vocabulary's Spatial category, specifically proportional symbol. Its task is singular and non-negotiable: show magnitude at place. It implies no rate, no density, no administrative share — only absolute counts at geographic locations.

## Why it was chosen here

The message is about absolute reach — how many households were served, not how many per capita or per square mile. That distinction immediately disqualifies the choropleth: choropleth shading implies proportion relative to the polygon's area, which forces viewers to mentally normalize every shade against state population or geography. That cognitive burden belongs to the chart, not the viewer. The bubble map carries it by encoding raw count directly in circle area, leaving the viewer free to compare size.

The primary flaw of bubble maps — overlap in high-density regions — is addressed in three layers here. Partial fill opacity (0.48) ensures overlapping bubbles remain visually distinguishable. A contrasting stroke at 0.82 opacity preserves circle boundaries even under overlap. And a "top 5 states" filter dims all non-highlighted bubbles when the full field feels crowded, surfacing the headline states without removing geographic context.

## What a choropleth would break

A choropleth of raw household counts would make Montana appear data-rich — large, mid-tone polygon — when its absolute count is among the lowest in the dataset. Texas's dominance would be undercut by the visual mass of vast, sparsely-populated Western states. The choropleth's failure mode here is area conflation: polygon darkness reads as magnitude, but polygon size is geographically determined, not data-determined. The message — California and Texas absorb nearly half of all disbursements — becomes nearly unreadable without normalization to per-capita rates, which changes the question entirely.

// design decision — sqrt radius scaling Circle radius is set via d3.scaleSqrt() , which maps sqrt(value) to a pixel range. This is non-negotiable for proportional symbol maps. Because perceived area scales with r² , naive linear radius encoding would make the largest bubble appear quadratically dominant and collapse small values into near-invisibility. The square-root mapping ensures a state with twice the households receives a circle with twice the area — which is what the FT Visual Vocabulary and Flannery (1956) both require for honest proportional symbol encoding.

## Framework reference

> // framework — FT Visual Vocabulary The FT Visual Vocabulary separates proportional symbols from choropleths on exactly this axis: use a choropleth for rates and ratios bounded by administrative units; use a proportional symbol for totals and absolute counts at a centroid. The operative test — does the polygon's area carry information about the variable? If no, remove it from the encoding channel and place a symbol at the centroid instead.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained bubble map in D3 v7. Two files:

1. `bubble-map.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Bubble Map" and the slide subtitle is "California and Texas Absorb Nearly Half of All Household Aid Disbursements".

2. `bubble-map/data.json` — the data file the chart loads via `d3.json("./bubble-map/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- FY 2024 simulated food assistance reach by U.S. state. Placeholder — replace with real program records.
  - `fips`: string, 2-digit zero-padded FIPS code — must match us-atlas state IDs exactly
  - `state`: string, full state name
  - `abbr`: string, 2-letter postal abbreviation
  - `value`: number, households reached by food assistance programs (bubble area encodes this field)
  - `program`: string, primary program delivery channel
  - `yoy_pct`: number, year-over-year change as a percentage, positive = growth
  - `region`: string, HHS administrative region label

Encoding: use the perceptually honest channel for this chart type (bubble map). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
