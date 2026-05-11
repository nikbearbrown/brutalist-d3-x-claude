# Dot Map

*Library density clusters in the Northeast and Great Lakes — the interior West is sparse*

![Dot Map](../images/34-dot-map.jpg)

## What this chart is

A Dot Map encodes the geographic location of discrete events or objects as equally-sized points plotted over a geographic base layer. It exploits the viewer's perceptual ability to detect visual density — clusters of points register immediately as regions of high concentration, sparse areas as low concentration. This is a preattentive task: the pattern emerges before conscious counting begins.

Two variants exist. In a *one-to-one* map, each dot represents a single real-world object — one library, one hospital, one crime incident. In a *one-to-many* map, each dot represents a unit count (e.g., 1 dot = 100 residents). This implementation is one-to-one: every dot is a confirmed branch location with a name and coordinates.

## Why it was chosen here

The message is about spatial distribution and clustering — where things are, and whether they concentrate. No aggregation is applied: each point is a real facility at a real coordinate. Aggregating to county or state would mask the intra-regional variation that is the actual story (a state with one dense urban cluster and vast rural emptiness looks identical to a state with uniform coverage).

The dot map preserves the original spatial resolution of the data while making density patterns immediately visible through point clustering. It is the correct chart when the story is *where* , not *how many* in aggregate — that distinction is the design decision.

## What the rejected alternative breaks

A **Choropleth Map** — the most common alternative — aggregates values by administrative unit (state, county) and encodes them as fill colour. For this data, it would collapse every library in Massachusetts into a single state-level count, hiding the fact that Boston has dozens of branches within a few square miles while rural western Massachusetts has almost none. The choropleth answers "how many per state?" The dot map answers "where exactly?"

A **Bubble Map** would aggregate counts by city or county centroid, losing the precise location information and misrepresenting the data as a comparison of totals rather than a distribution of individual points. When you have real coordinates for individual events, using them is always more honest than throwing them away to draw circles.

## What dot maps cannot tell you

Dot maps do not encode quantity at a point — a dot cluster of twelve libraries and a dot cluster of forty look similar unless you zoom in and count. They are not suitable for retrieving precise counts or comparing exact values between regions. They also suffer from overplotting at dense scales: when many points share near-identical coordinates, they merge visually and the underlying count is lost.

This implementation mitigates overplotting with a small dot radius, semi-transparency on the SVG layer, and zoom — the viewer can drill into any dense cluster to separate individual points. But the limitation is structural: if the message requires exact counts, the dot map hands off to a bar chart or table.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained dot map in D3 v7. Two files:

1. `dot-map.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Dot Map" and the slide subtitle is "Library density clusters in the Northeast and Great Lakes — the interior West is sparse".

2. `dot-map/data.json` — the data file the chart loads via `d3.json("./dot-map/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Public library branch locations across the United States. Each record is one branch facility. 120 placeholder entries spanning all four US census regions, weighted toward Northeast and Midwest density to reflect the message.
  - `name`: string — branch name (shown in tooltip and stat bar)
  - `city`: string — city name
  - `state`: string — two-letter US state abbreviation (used for region filter)
  - `lat`: number — decimal latitude (WGS84, used for d3.geoAlbersUsa projection)
  - `lon`: number — decimal longitude (WGS84, must be negative for continental US)

Encoding: use the perceptually honest channel for this chart type (dot map). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
