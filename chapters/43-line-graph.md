# Line Graph

*The gap was 22 points in 2016 — it is 67 in 2024*

![Line Graph](../images/43-line-graph.jpg)

## What this chart is

A line graph encodes quantitative values as *position along the y-axis* — the most accurate perceptual channel in Cleveland and McGill's hierarchy — and connects successive points with a line that implies continuity. The line itself is not a data encoding; it is a **visual metaphor** for the path a value took between measurements. An upward slope means increase; a downward slope means decrease; diverging lines mean a growing gap. These readings are pre-attentive — the direction is understood before any axis is read. That metaphor only works when the x-axis is genuinely continuous (time, distance, sequence), never when it is categorical.

## Why it was chosen here

The data has a continuous time axis (annual, 2016–2024) and three series whose *divergence* is the message. A line graph is uniquely suited to divergence stories: the visual distance between lines at any x-position directly encodes the gap. In 2016 the three lines start close together; by 2024 the space between them is dramatically wider. No other chart form renders that expanding space as immediately. The y-axis is anchored at 0 — not the data minimum — because the message is about absolute levels and **how far the bottom sits from the top** , not about slope alone.

## What grouped bars would break

A grouped bar chart of this data requires 9 year-groups × 3 bars = 27 bars. Each year-group reads as a *comparison at a moment* rather than a *trajectory over time* . The viewer must mentally connect the high-income bars across all nine groups to perceive the trend — work the line chart does automatically. More critically, the growing gap between series **cannot be seen** in grouped bars without computing differences. The "gap" annotation that appears via the toggle on slide 1 would be the only way to surface it — and in a bar chart, that annotation has no geometric backing.

## Framework reference & the one decision worth knowing

**The one decision worth knowing:** lines animate in order from highest final value to lowest — high-income first, low-income last. This is not alphabetical. It creates a deliberate reveal: the viewer sees the leading line establish a ceiling, then watches the gap widen as subsequent lines draw in below. The ordering is an editorial argument that the *distance* matters, not just the levels.

## Framework reference

> // FT Visual Vocabulary + Tufte FT Visual Vocabulary: Change over time — Trend .
            Abela quadrant: Comparison (items over time, many
            periods). Tufte: the line graph has among the best data-ink ratios
            of any chart form — every pixel of line is a data encoding. Gridlines
            are kept light and sparse; they are references, not decoration.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained line graph in D3 v7. Two files:

1. `line-graph.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Line Graph" and the slide subtitle is "The gap was 22 points in 2016 — it is 67 in 2024".

2. `line-graph/data.json` — the data file the chart loads via `d3.json("./line-graph/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Multi-series time data. Each series has an id, display label, line style, and an array of {year, value} objects. All series should share the same year domain.
  - `title`: string — chart headline
  - `unit`: string — y-axis label / tooltip unit descriptor
  - `yDomain`: [number, number] — explicit y-axis domain. Use [0, max] for honest baselines; truncate only for rate-of-change stories.
  - `series[].id`: string — unique identifier
  - `series[].label`: string — full display name for legend and tooltip
  - `series[].shortLabel`: string — abbreviated name for end-of-line label
  - `series[].style`: string — 'solid' | 'dashed' | 'dotted'
  - `series[].values[]`: array of {year: number, value: number}

Encoding: use the perceptually honest channel for this chart type (line graph). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
