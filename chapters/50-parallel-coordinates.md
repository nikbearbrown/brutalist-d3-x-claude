# Parallel Coordinates

*Health programs lead on efficiency —emergency response moves fastest but costs most*

![Parallel Coordinates](../images/50-parallel-coordinates.jpg)

## What this chart is

A parallel coordinates plot represents each observation as a polyline that crosses multiple vertical axes. Each axis encodes one variable; the position where a line crosses an axis encodes that variable's value. The perceptual mechanism is *pattern detection through line slope and clustering* — lines that run parallel between two adjacent axes indicate positive correlation; lines that cross indicate negative correlation or inverse relationship.

It is the only chart type that can display seven or more quantitative variables simultaneously without collapsing into a matrix of 21 separate scatter plots. The trade-off: individual values are harder to read than on a bar or scatter chart, and the chart becomes cluttered above ~50–80 observations without interaction.

## Why it was chosen here

The data structure is 28 records × 7 numerical dimensions — the canonical parallel coordinates use case. The message is multivariate: no single axis tells the story. The pattern worth finding is how program type creates characteristic "signatures" — consistent shapes across all seven axes that reveal trade-offs (emergency programs sacrifice efficiency for speed; health programs achieve high efficiency but serve fewer beneficiaries).

A scatter plot matrix would need 21 panels to show the same variable pairs. A radar chart would collapse all 28 records onto one overlay. Neither surfaces the line-pattern trade-offs that parallel coordinates reveal naturally.

## Brushing — the essential fix

Without brushing, parallel coordinates are visually overwhelming at 28 lines. With brushing, the viewer can isolate the subset of interest — "show me only programs with efficiency above 80% and AI accuracy above 90%" — and let the remaining lines fade to near-invisible. Brushing is not optional decoration on this chart type. It is the primary analytical mechanism.

Multi-axis brushing uses *intersection* logic: a line is highlighted only if it falls within every active brush range simultaneously. This makes the chart a multivariate filter, not just a visual overview.

## Axis order and correlation

Adjacent axes reveal correlations more clearly than non-adjacent ones. Dragging the "Funding ($M)" axis next to "Beneficiaries (k)" will make the positive correlation between them immediately visible as lines running roughly parallel. Moving "Response (days)" adjacent to "Efficiency (%)" reveals the trade-off: slower response correlates with higher efficiency — planned programs outperform emergency deployments on cost-effectiveness.

This is the key design parameter. There is no universal optimal axis order — the right order depends on which relationship the viewer is investigating. Axis reordering is therefore an analytical tool, not an aesthetic preference.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained parallel coordinates in D3 v7. Two files:

1. `parallel-coordinates.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Parallel Coordinates" and the slide subtitle is "Health programs lead on efficiency —emergency response moves fastest but costs most".

2. `parallel-coordinates/data.json` — the data file the chart loads via `d3.json("./parallel-coordinates/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- 28 humanitarian AI programs measured across 7 numerical dimensions. Each record is one line in the parallel coordinates plot. The 'type' field determines line color.
  - `dimensions[].id`: string — key matching data record fields
  - `dimensions[].label`: string — axis header label
  - `dimensions[].desc`: string — description shown in tooltip
  - `dimensions[].inverted`: boolean — true if lower values are better (annotated on axis)
  - `data[].id`: string — unique record identifier
  - `data[].name`: string — program name shown in tooltip
  - `data[].type`: string — category determining line color
  - `data[].{dimId}`: number — value for each dimension

Encoding: use the perceptually honest channel for this chart type (parallel coordinates). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
