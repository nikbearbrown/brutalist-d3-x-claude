# Sunburst

*Sunburst Diagram*

![Sunburst](../images/70-sunburst.jpg)

## The perceptual mechanism

A sunburst diagram encodes a **hierarchy as a series of concentric rings** . The centre circle is the root node. Each ring outward represents one level deeper in the hierarchy. Within each ring, arcs are sliced proportionally to a numeric value — arc angle and arc length encode magnitude. The viewer's visual system simultaneously reads **containment** (which node belongs to which parent, conveyed by angular alignment) and **proportion** (how much each node contributes to its parent, conveyed by arc angle).

This dual encoding — hierarchy structure plus proportional composition — is the sunburst's unique capability. No other chart type conveys both in a single view without requiring the reader to cross-reference between two separate charts.

## Two modes: equal and proportional

When arcs are divided **equally** under a parent, the chart emphasises hierarchy structure — every child node gets equal visual weight regardless of its value. This is useful when the branching pattern itself is the message. When arcs are **proportional to a value** (as implemented here), the chart emphasises composition — each node's arc angle represents its share of the parent's total. The choice between these modes is a design decision that depends on whether structural equality or magnitude comparison is the message.

## Why it was chosen for this data

The data structure is a **three-level hierarchy with numeric leaf values** : industry → company → product line → revenue. The message is compositional at every level simultaneously: which industry dominates, which company dominates within each industry, and which product line drives each company. A treemap would answer the same question but loses the explicit parent–child ring structure that makes the hierarchy legible. A pie chart can only show one level. The sunburst shows all levels at once with a single glance.

## What the alternative would break

A **treemap** — the nearest alternative — packs all leaf nodes into rectangular area without showing the intermediate branch levels as visible elements. It is better for precise area comparison of leaf nodes; worse for communicating the hierarchical grouping structure. A **nested pie chart** (multiple concentric pies) is perceptually equivalent but harder to implement cleanly because it requires manual ring sizing. The sunburst's continuous angle encoding makes parent–child proportional relationships clearer than separate concentric pies.

The sunburst performs poorly when the hierarchy is very deep (more than four rings), when many nodes at one level have very small values (thin slivers become unreadable), or when the message is precise comparison rather than structural overview. In those cases, a hierarchical bar chart or treemap is more appropriate.

## The one design decision worth knowing

The **click-to-zoom** interaction is not a navigation convenience — it is an analytical necessity. A sunburst with four or more levels and many nodes becomes visually dense at full scale. Zooming into a branch re-partitions the full angular space to show only that subtree's children, making small arcs readable. The **breadcrumb trail** above the chart preserves the viewer's positional context within the hierarchy — without it, zoom interactions disorient the reader. These two elements are inseparable.

## Framework reference

> // Framework — FT Visual Vocabulary FT Visual Vocabulary category: Part-to-whole — "How a single entity is made up of its components." Abela quadrant: Composition (hierarchical, accumulating over levels). Tufte principle: the rings are data (hierarchy levels); the arcs are data (proportional values); the angular alignment of parent and children arcs is data (containment relationship). The only non-data ink is the thin white stroke separating arcs — necessary for figure–ground separation between adjacent slices.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained sunburst in D3 v7. Two files:

1. `sunburst.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Sunburst" and the slide subtitle is "Sunburst Diagram".

2. `sunburst/data.json` — the data file the chart loads via `d3.json("./sunburst/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Hierarchical data for a sunburst diagram. Structure is a nested tree: each node has a name, an optional value (leaf nodes), and optional children (branch nodes). The root node is the centre circle. Each ring outward is one level deeper. Values on leaf nodes drive arc angles; branch node values are summed from children automatically. Do not provide values on branch nodes — the chart computes them.
  - `name`: string — label for this node
  - `value`: number (leaf nodes only) — magnitude that drives arc angle
  - `children`: array (branch nodes only) — child nodes at the next ring level

Encoding: use the perceptually honest channel for this chart type (sunburst). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
