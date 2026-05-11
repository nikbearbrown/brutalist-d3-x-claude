# Radial Column Chart

*Concentric Value Rings, Radial Bars — A Polar Variant of the Column Chart*

![Radial Column Chart](../images/61-radial-column-chart.jpg)

## What this chart is

A radial column chart maps a standard column chart onto a polar coordinate system. Each category occupies an angular slice; the column extends outward along a radial axis from a central baseline. The value scale is encoded as concentric rings — the innermost ring represents the lowest value (often zero), each successive ring outward represents a higher value, and the column's radial length encodes the value of its category.

The form is mechanically identical to the radial bar chart in this book. The naming convention separates them: a *column* chart in linear form has bars running vertically (value on y), and a *bar* chart has bars running horizontally (value on x). When either is bent into polar coordinates, the bars run radially. Some references reserve "radial column" for the polar version of a column chart and "radial bar" for a different polar form (concentric arcs encoding value by arc length rather than radius). The pantry treats them as siblings; this chapter and the radial bar chapter cover the same encoding from two angles.

The construction in D3: an angular scale (`d3.scaleBand` over `[0, 2π]`) places each category. A radial scale (`d3.scaleLinear`) maps values to radial extent. Each column is a `d3.arc` with fixed inner radius, data-driven outer radius, and small `padAngle`. The chart's "value rings" are circles drawn at sensible scale intervals, providing the only quantitative reference the reader has — there is no straight axis line.

## How to read this chart

Read the silhouette first. The outer edge of all the columns, taken together, forms a shape — a smooth arc, a spiky pattern, a partial half-circle. That silhouette is the gestalt of the data. Symmetric silhouettes indicate uniform values; spiky silhouettes reveal outliers; arc-shaped silhouettes reveal a single mode that rises and falls across the categorical axis.

Read the rings second. Each concentric ring marks a value on the radial scale; the column endpoint between two rings tells you the value within that interval. This is harder than reading a number off a linear y-axis — the rings are curves, the interpolation is mental, and rings at different radii have different physical lengths even though they represent the same value range.

Read individual columns last. A tooltip giving the exact value on hover is the honest substitute for what a linear column chart provides automatically.

## When this form is justified

Two conditions must hold. First, the data must be cyclical: months, hours, compass directions, days of the week — categories whose end and beginning are adjacent in the world. The polar form expresses that adjacency; the linear form cannot. Second, the communication goal must be pattern recognition or visual memory rather than precise value comparison. The radial form's silhouette is memorable; the linear form's bars are precise. If a viewer needs to argue "May was 23% higher than April," the linear form is the right chart. If a viewer needs to register "summer is the broad arc and winter is the trough," the radial form makes that pattern visible at a glance.

When neither condition holds, the radial column chart is decoration with a perceptual cost. Stephen Few and the Data Visualisation Catalogue both come down hard on this: the linear bar chart is more accurate, and the radial form should not be used unless the circular structure of the data warrants it.

## What the alternative would break

A linear column chart of the same cyclic data places the first and last category at opposite ends of the x-axis. The seasonal-cycle wrap-around — December meets January — is broken visually; the eye reads December as far from January, when in the world they are adjacent. For genuinely cyclic data, this is information loss. For non-cyclic data, the linear form is informationally complete and perceptually superior, and the radial form adds nothing but visual interest at the cost of reading accuracy.

A small-multiples linear chart — twelve small bar charts arranged in a 4×3 grid showing monthly data across multiple years — preserves the linear axis precision and lets the reader compare year-over-year cycles without polar distortion. For analytical work this is the strongest alternative.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary: **Comparison — Categorical (cyclical variant)**. Tufte principle partially violated: the polar coordinate system introduces a non-data-ink distortion that scales as `r²` for area, even though the encoding ostensibly uses radial length only. Abela quadrant: Comparison (items, few periods, specialised for cyclic ordering). The one design decision worth knowing: the inner radius is not free. A small inner radius maximises radial range but also maximises the area distortion (small bars look much smaller than they are); a large inner radius compresses the value scale but reduces the perceptual amplification of large values. Tune the inner radius to match the communication goal.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained radial column chart in D3 v7. Two files:

1. `radial-column-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on columns, and include a tooltip on hover that shows the exact value. The page title is "Radial Column Chart" and the slide subtitle is "Concentric Value Rings, Radial Bars — A Polar Variant of the Column Chart".

2. `radial-column-chart/data.json` — the data file the chart loads via `d3.json("./radial-column-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- 8–12 categories with cyclical structure (months, hours, days of week, compass octants). Each entry has a category label and one quantitative value.
  - `category`: string — angular position label
  - `value`: number — radial length

Encoding: angular position by category; radial length by value, drawn from a fixed inner radius outward. Concentric value rings at sensible intervals. Use `d3.arc` per column. Provide a slider or fixed-default for inner radius (around 30% of outer) — the reader should be able to see the trade-off between range and distortion. Annotate the chart with a one-line in-chart subtitle.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
