# Density Plot

*Crisis Type Determines Response Delay —Conflict Shows Bimodal Pattern, Displacement Skews Right*

![Density Plot](../images/32-density-plot.jpg)

## What this chart is

A density plot (formally a **Kernel Density Estimate** , or KDE) visualises the distribution of a continuous variable by placing a smooth kernel function over each data point and summing the result across the range. The perceptual mechanism exploited is **position along a common scale** — the curve's height at any x-value encodes the probability density there. Peaks reveal where values concentrate. Troughs reveal gaps. Shape — symmetric, skewed, bimodal — is the primary message. This implementation uses the **Epanechnikov kernel** , the theoretically optimal kernel for minimising mean integrated squared error.

## Why it was chosen

The data is three sets of continuous observations — response times in days — where the *shape* of each distribution is the message, not individual values. The conflict distribution is bimodal: fast-strike responses and protracted negotiations produce two distinct clusters. A histogram would either smooth that bimodality away (too few bins) or introduce false peaks from bin boundary placement (too many bins). A density plot eliminates the bin count decision entirely by using a **continuous kernel** , producing a shape that is stable under reasonable bandwidth choices.

## What the histogram would break

A histogram's shape changes with bin width and bin origin — two parameters with no principled optimal value. The same data can appear unimodal at 5 bins and bimodal at 15. For the conflict distribution here, the bimodal structure at days 2–3 and days 12–15 would be visible with narrow bins but destroyed with wide ones. The density plot makes the bimodal pattern **structurally stable** : the two peaks survive across a wide range of bandwidths, so the viewer can trust that shape reflects data rather than a parameter choice they weren't told about.

## Bandwidth — the one real parameter

The density plot trades the histogram's bin-width problem for a **bandwidth** (smoothing window) problem — but the tradeoff is better. Bandwidth affects smoothness, not shape topology. The **bw − / bw +** buttons on slide 1 let you tune bandwidth in real time. The optimal bandwidth for this dataset is 2.5 (set in `data.json` ). Increasing it to 5.0 would merge the conflict bimodal peaks. Decreasing to 1.0 would fragment the natural disaster distribution into false peaks.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained density plot in D3 v7. Two files:

1. `density-plot.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Density Plot" and the slide subtitle is "Crisis Type Determines Response Delay —Conflict Shows Bimodal Pattern, Displacement Skews Right".

2. `density-plot/data.json` — the data file the chart loads via `d3.json("./density-plot/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Simulated humanitarian aid response times (days from crisis onset to first aid delivery) across three crisis types. Fictional placeholder — realistic distributional shapes derived from sector literature. Proves KDE renders before real data is substituted.
  - `label`: string — crisis category name, used in legend and tooltip
  - `fill`: string — hex color, mapped to hai palette roles (p2/p3/p5)
  - `strokeDash`: string — SVG stroke-dasharray for redundant encoding. 'none' = solid
  - `values`: array of numbers — observed response times in days. KDE is computed from these at runtime.

Encoding: use the perceptually honest channel for this chart type (density plot). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
