# Bullet Graph

*Most programs trail their targets —Community Trust is the lone outlier*

![Bullet Graph](../images/26-bullet-graph.jpg)

## What this chart is

The bullet graph, developed by Stephen Few in 2005, is a linear replacement for the radial gauges and speedometer dials that crowded early dashboards. It encodes a primary measure as a bar, layered over qualitative range bands and punctuated by a perpendicular target marker.

The perceptual mechanism it exploits is *position along a common axis* — the most accurate of all visual encoding channels for quantitative comparison. Radial gauges use angle, which is among the weakest channels. The bullet graph achieves the same task with roughly one-sixth the ink.

## Three comparisons in one row

**1.** Is the actual value in the poor, satisfactory, or good band? **2.** Did the actual value reach the target marker? **3.** How far into the band did it land — barely satisfactory, or deep into good?

A bar chart answers only the first. A grouped bar chart requires separate colors and a legend with no qualitative context. A gauge cannot show the target as a reference line — it degrades to a secondary number label, stripped of visual meaning.

## Why it was chosen here

The data structure is a named set of performance metrics, each with an actual value, a target, and a qualitative interpretation of the range. This is the canonical bullet graph use case: dashboard performance tracking where the viewer needs all three answers simultaneously.

Five bullet graphs in a vertical list share a common axis, enabling direct comparison of performance levels across programs — something five separate gauges cannot provide.

## What the alternative would break

A radial gauge encodes value as angle — the perceptually imprecise encoding channel. Five gauges consume five times the screen area and provide no shared reference axis for cross-metric comparison. The target marker cannot be clearly rendered as a positional reference in a radial design.

A stacked bar would imply that the metrics sum to a meaningful whole — they do not. A grouped bar would require five color-coded series with no qualitative context bands.

## The one design decision worth knowing

The range bands are encoded as gray intensities — not distinct hues — following Few's own specification. Using hues (red → yellow → green) for the bands would pull the viewer's eye to the background, inverting the visual hierarchy. The walnut bar and blood-red target line must dominate. The bands should answer only when interrogated. Gray intensities keep them subordinate while still legible as categorical zones.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained bullet graph in D3 v7. Two files:

1. `bullet-graph.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Bullet Graph" and the slide subtitle is "Most programs trail their targets —Community Trust is the lone outlier".

2. `bullet-graph/data.json` — the data file the chart loads via `d3.json("./bullet-graph/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Humanitarian program performance metrics for bullet graph visualization
  - `label`: string — metric name displayed as the row label
  - `unit`: string — unit appended to values, e.g. '%' or ' pts'
  - `value`: number — featured measure (actual performance this period)
  - `target`: number — comparative measure (target / goal marker line)
  - `ranges`: array [poor_end, sat_end, good_end] — cumulative thresholds for qualitative bands
  - `rangeLabels`: array of 3 strings — labels for each band: poor, satisfactory, good

Encoding: use the perceptually honest channel for this chart type (bullet graph). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
