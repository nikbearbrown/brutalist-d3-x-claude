# Sankey Diagram

*Global Energy Flow — Source to End Use, Width = Exajoules*

![Sankey Diagram](../images/62-sankey-diagram.jpg)

## What this chart is

A Sankey diagram encodes directed flows between nodes using ribbons whose width is strictly proportional to the flow quantity. Nodes are rectangles (or points) arranged in columns representing stages of a process; ribbons connect source nodes to target nodes and can split or merge at each stage. The perceptual mechanism is area: the viewer's eye integrates ribbon width over length, making proportional flow comparisons automatic — a ribbon that is twice as wide carries twice the quantity, and this is legible without reading any number. The layout preserves flow conservation at each node: the sum of incoming ribbon widths equals the sum of outgoing widths (minus any losses explicitly encoded), which allows mass-balance verification at a glance.

## Why it was chosen here

The dataset is a directed multi-stage flow system — energy moving from primary sources through conversion stages to end uses with explicit losses — and the message is about where quantity is concentrated and where it is dissipated. No other chart type encodes this simultaneously. A stacked bar chart at each stage could show totals but cannot show which source flows to which end use. A chord diagram would show bilateral relationships but imposes a circular layout that loses the left-to-right process directionality. A flow map would require geographic coordinates. The Sankey is the only format that allows the viewer to trace a specific flow path — from coal through electricity generation to industry — as a continuous visual thread from left to right.

## What the alternative would break

An alluvial diagram is the closest structural relative. The distinction is subtle but important: alluvial diagrams show how categorical composition changes across time or grouping variables — the flows represent reclassifications of the same population. Sankey diagrams show physical or financial flows where quantity is transferred, not just reclassified, and losses are permitted (total output at a node can be less than total input, encoding inefficiency or waste). Using an alluvial diagram for energy flow would incorrectly imply conservation at every node, hiding the conversion losses that are often the key finding. Parallel sets are the third confusion — they show conditional probabilities across ordered categorical dimensions, with no implied physical transfer.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary category: Flow — "Show the volume or intensity of movement between two or more states or conditions." Tufte principle: the Sankey is data-ink efficient when the flow quantity is the message — every pixel of ribbon width encodes a real quantity. The one design decision worth knowing: node horizontal position is fixed by stage column, but vertical position within a column is determined by the layout algorithm minimising link crossings. This implementation uses d3-sankey's default iterative relaxation — it trades some vertical compactness for reduced visual clutter from crossing ribbons.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained sankey diagram in D3 v7. Two files:

1. `sankey-diagram.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Sankey Diagram" and the slide subtitle is "Global Energy Flow — Source to End Use, Width = Exajoules".

2. `sankey-diagram/data.json` — the data file the chart loads via `d3.json("./sankey-diagram/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Sankey diagram data: nodes represent stages or entities in a flow system; links represent directed flows between them. Values are in exajoules (EJ). Replace with real flow data in the same unit.
  - `nodes[].id`: string — unique key, must match link source/target
  - `nodes[].label`: string — display name on the diagram
  - `nodes[].col`: number — column index (0 = leftmost stage, 1 = middle, 2 = rightmost). Controls horizontal position.
  - `links[].source`: string — node id of the flow origin
  - `links[].target`: string — node id of the flow destination
  - `links[].value`: number — flow quantity (must be positive; unit matches dataset)

Encoding: use the perceptually honest channel for this chart type (sankey diagram). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
