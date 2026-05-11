# Tally Chart

*Accuracy failures lead at 31 — safety incidents, at 8, may be the most under-reported*

![Tally Chart](../images/71-tally-chart.jpg)

## What this chart is

A Tally Chart is simultaneously a *data collection method* and a *visual display* . The tally mark numeral system — four vertical strokes crossed by a diagonal — groups counts in fives, making totals readable at a glance without arithmetic. Historically made with pen and paper, the form conveys something that no bar chart can: the **process of counting** . Each mark is a discrete event. The chart does not abstract the data into a continuous scale; it preserves the unit nature of what was counted. The animation here restores that accumulative process — marks appear as they would be drawn, one incident at a time.

## Why it was chosen here

The data is a count of discrete events (reported incidents) across a small number of categories with relatively modest counts (8–31 per category). A bar chart would be more precise, and a dot plot would be more elegant. But the tally form makes an argument that precision does not: these are *individually countable events* , not a measured quantity. Every mark is an incident that was filed by a real person. The form grounds the data in its origin — a manual counting process — which is appropriate when the act of counting is itself part of the story. When counts exceed ~60 per category, the form breaks down and a histogram is correct.

## What a histogram would do differently

A histogram bins continuous values into intervals and shows their frequency as bars. A tally chart counts discrete events in categorical rows. They look similar when complete — the Data Visualisation Catalogue notes that "the final result is similar to a histogram" — but they are conceptually different. The histogram's x-axis is a continuous scale; the tally chart's rows are independent categories. You **cannot** use a tally chart for continuous data (temperature, time-to-resolution) without first binning it, at which point a histogram is the correct form. The tally chart's limitation is also its strength: it only works for countable, discrete data.

## Framework reference & the one decision worth knowing

**The one decision worth knowing:** phantom group boxes (faint rectangles) are drawn *before* the marks animate in. This mirrors the pre-printed form structure of a physical tally sheet, where blank boxes exist before any data is recorded. The boxes also make the group-of-5 structure legible from the first frame — the viewer understands the encoding before a single mark appears.

## Framework reference

> // FT Visual Vocabulary + Tufte FT Visual Vocabulary: Distribution — Frequency (closest match; tally charts predate most formal charting frameworks).
            Abela quadrant: Comparison — comparing discrete
            frequency counts across categories. Tufte: tally charts achieve
            near-perfect data-ink ratio — every mark is one data point .

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained tally chart in D3 v7. Two files:

1. `tally-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Tally Chart" and the slide subtitle is "Accuracy failures lead at 31 — safety incidents, at 8, may be the most under-reported".

2. `tally-chart/data.json` — the data file the chart loads via `d3.json("./tally-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Frequency dataset. Each category gets a row of tally marks — groups of 5 (four vertical marks slashed by a diagonal). The chart resembles a histogram once marks are totalled. Best for discrete counts of 5–60; above that, a histogram is clearer.
  - `title`: string — chart headline
  - `unit`: string — what each tally mark represents
  - `period`: string — time period or context label
  - `categories[].id`: string — unique identifier
  - `categories[].label`: string — row label (displayed on left axis)
  - `categories[].count`: number — integer count (each unit becomes one tally mark)

Encoding: use the perceptually honest channel for this chart type (tally chart). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
