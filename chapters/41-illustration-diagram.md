# Illustration Diagram

*The Human Heart — Anatomy & Blood Flow Direction*

![Illustration Diagram](../images/41-illustration-diagram.jpg)

## What this chart type is

An Illustration Diagram is a graphic that pairs a visual representation of an object, system, or concept with structured annotations — labels, callouts, leader lines, legends, and sometimes enlarged cross-sections. It is not a statistical chart: no data is plotted on axes. Its purpose is explanatory rather than comparative. The perceptual mechanism it exploits is spatial correspondence: a label attached to a specific location on the image inherits the visual context of that location, allowing complex multi-part systems to be understood simultaneously rather than sequentially. The viewer builds a mental model by mapping text to position, which is faster and more durable than reading a list of descriptions.

## Why it was chosen here

The human heart is a canonical subject for illustration diagrams: it has discrete named structures, directional flow logic, and meaningful spatial relationships between parts that cannot be communicated through any tabular or statistical format. A written list of chambers and valves conveys the same facts but severs their spatial relationships — the reader cannot infer that the left ventricle wall is thicker because it pumps against higher systemic pressure without seeing the cross-section. The illustration diagram makes that inference automatic. The interactive callout layer adds depth-on-demand: the primary visual is uncluttered, and detail is surfaced only when a specific structure is selected, preventing cognitive overload.

## What the alternative would break

A flowchart could represent the sequence of blood flow — right atrium to right ventricle to pulmonary artery and so on — but it would lose all spatial information about where each chamber sits relative to the others. A viewer reading a flowchart of cardiac circulation cannot develop intuition about why the pulmonary and systemic circuits are physically separate, or how the septum prevents mixing. A table of structure names and descriptions preserves the vocabulary but destroys the geometry. The illustration diagram is the only format that allows spatial reasoning about a complex physical object, which is why it is the dominant format in medical education, engineering documentation, and technical journalism.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary category: Concepts / How things work — "Show mechanisms, processes, and objects where spatial arrangement carries the meaning." The one design decision worth knowing: callout dots are placed at the anatomical boundary of each structure, not at its centroid — boundary placement mimics how a real dissection label is pinned, and tells the viewer precisely which edge or wall is being named rather than gesturing at a region.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained illustration diagram in D3 v7. Two files:

1. `illustration-diagram.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Illustration Diagram" and the slide subtitle is "The Human Heart — Anatomy & Blood Flow Direction".

2. `illustration-diagram/data.json` — the data file the chart loads via `d3.json("./illustration-diagram/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Annotation data for an illustration diagram. Each entry defines a callout dot position, its label, and explanatory body text. Positions are expressed as fractions (0–1) of the SVG viewBox dimensions.
  - `id`: string — unique identifier, used to link dot to info panel
  - `label`: string — short structure name shown as the callout label
  - `cx`: number (0–1) — horizontal position of callout dot as fraction of viewBox width
  - `cy`: number (0–1) — vertical position of callout dot as fraction of viewBox height
  - `lx`: number (0–1) — horizontal anchor of the leader-line label
  - `ly`: number (0–1) — vertical anchor of the leader-line label
  - `side`: string — 'left' or 'right': which side of lx the label text extends toward
  - `color`: string — hex color for this callout (use palette role colors)
  - `body`: string — 1–3 sentence explanation shown in the info panel on click

Encoding: use the perceptually honest channel for this chart type (illustration diagram). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
