# Radial Bar

*Aid Deliveries Peak in November and January Around Winter Emergencies — June Access Constraints Create the Annual Trough at 188K MT*

![Radial Bar](../images/58-radial-bar.jpg)

## What this chart is

A radial bar chart is a bar chart plotted on polar coordinates. Each category occupies an angular band; the bar's radial length encodes the value. The viewer reads the same information as a regular bar chart — bar length — but in a circular arrangement. The angular axis replaces the categorical x-axis, and the radial axis replaces the value y-axis.

In D3 terms: the angular scale is `d3.scaleBand()` with a range of `[0, 2π]` ; the radial scale is `d3.scaleLinear()` mapping values to the bar height in pixels (from `innerRadius` to `outerRadius` ). Each bar is a `d3.arc()` with fixed `innerRadius` and a data-driven `outerRadius` .

## The distortion — why this chart misleads

The outer arc of a taller bar is not just *further from the center* — it is literally *longer in pixels* than the outer arc of a shorter bar, even accounting for proportion. This is because **arc length = radius × angle** . Two bars with the same angular width but different heights have different outer arc lengths. The November bar (318K MT) has an outer arc roughly 1.69× longer than the June bar (188K MT) — but the ratio of their values is only 1.69× anyway. The distortion doesn't change the ratio, but it does change the perceived area: area scales with `r²` , not `r` , so the November bar appears to dominate the field of view far more than its 1.69× value ratio would justify.

The bar closest to the outer edge gets a disproportionate visual footprint compared to its neighbours. In a 12-bar radial chart, a bar at 170px radius has an outer arc about 3.3× as long as a bar at the same angular width starting at the same inner radius but only 52px tall. A viewer reading the chart via perceived arc length rather than radial extent will systematically overestimate the largest values.

// distortion warning This chart is analytically inferior to a regular bar chart for precise value comparison. Use it when the circular form has semantic meaning (cyclical data like months, hours, directions) and when aesthetic communication is as important as precise reading. Always pair it with exact values in tooltips and scale rings for estimation. Do not use it to compare non-cyclical data where the circular arrangement is purely decorative.

## When it is justified — and why it was used here

Monthly data has a genuine cyclic structure. January follows December — the wrap-around is not an arbitrary visual choice but a property of the data itself. Plotting monthly aid deliveries on a polar axis makes the winter peak visible as a continuous arc (Nov–Jan), which a regular bar chart would split into two ends of the x-axis with a gap in between. The viewer can immediately see that the high-delivery cluster is contiguous, not separated. This is information the bar chart form suppresses.

The second justification is communication context. This chart appeared in a slide deck, not a data-analysis tool. For an audience reading quickly, the circular form makes the seasonal pattern memorable in a way that a horizontal bar chart at the same size does not. The Catalogue is correct that a bar chart is analytically superior; the radial form was chosen because the communication goal was pattern recognition, not precise value reading. The tooltip provides exact values for viewers who need them.

## What a regular bar chart would do better

A horizontal bar chart of the same 12 months, sorted by value, would allow precise comparison using the most accurate perceptual mechanism available: length along a common scale. The November–June difference (130K MT) would be immediately readable by comparing bar endpoints against the x-axis. No arc-length distortion. No area amplification. Any analyst who needs to argue a 41% seasonal swing would use the bar chart, not the radial form, in a technical context.

// design decision — January at 12 o'clock, not angular index 0 The angular scale starts at 0 radians with January, which in D3's arc convention places it at 12 o'clock (top). This matches how most people read a clock face — January at the top reads intuitively as "the start." An alternative would be to start the scale at −π/2 and map January to the left (9 o'clock, matching a standard Cartesian x-axis). The 12 o'clock convention was chosen because the audience's mental model of "year as clock" makes the seasonal pattern (winter peaks at top and left, summer trough at bottom-right) immediately spatially resonant.

## Framework reference

> // framework — FT Visual Vocabulary + Data Visualisation Catalogue Both the FT Visual Vocabulary and the Data Visualisation Catalogue classify radial bar charts as aesthetic-first tools. The Catalogue states directly: "Since our visual systems are better at interpreting straight lines, a regular Bar Chart is a better choice for comparing values. The main reason to use a Radial Bar Chart instead is aesthetic." This is the correct framing. The chart is aesthetically motivated; the bar chart is analytically correct. When you choose the radial form, own the tradeoff.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained radial bar in D3 v7. Two files:

1. `radial-bar.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Radial Bar" and the slide subtitle is "Aid Deliveries Peak in November and January Around Winter Emergencies — June Access Constraints Create the Annual Trough at 188K MT".

2. `radial-bar/data.json` — the data file the chart loads via `d3.json("./radial-bar/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Monthly humanitarian aid delivery volume, FY 2024 (simulated). Twelve categories mapped to angular positions on a polar axis. Replace with any single-series categorical dataset where the circular layout has semantic meaning (months, compass directions, hours of day). Avoid using a radial bar chart for datasets where the circular wrap-around carries no meaning — a regular bar chart will be more honest.
  - `data[].month`: string, category label — mapped to angular band
  - `data[].value`: number, quantity — encoded as bar length (radial extent) from innerRadius
  - `data[].note`: string, annotation shown in tooltip

Encoding: use the perceptually honest channel for this chart type (radial bar). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
