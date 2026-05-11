# Nightingale

*Summer peaks — July leads at 74, February trails at 27*

![Nightingale](../images/48-nightingale.jpg)

## What this chart is

A Nightingale Rose (Coxcomb, Polar Area Diagram) is a *radial bar chart* where segments occupy equal angular slices and values are encoded as petal **radius** . Each ring from the centre represents a scale increment. The chart is drawn on a polar coordinate grid, which means values that are numerically similar appear in a circular spatial arrangement — useful when the data is genuinely cyclic (months in a year, hours in a day). The visual metaphor is a flower: larger values bloom outward; smaller values stay compact near the centre. Florence Nightingale used this form in 1858 to show causes of army deaths in the Crimean War — almost certainly the most consequential data visualisation in history.

## The deliberate flaw — area distortion as rhetoric

This chart has a **known and serious flaw** : petal area grows as *r²* , not *r* . A petal with value 74 has nearly *seven times* the area of a petal with value 27, even though the values differ by less than 3×. The area-correct toggle on slide 1 applies a square-root radius scale, which makes area proportional to value — correcting the distortion. Compare them. The corrected version is more honest. Nightingale almost certainly knew this. She chose the uncorrected form because the exaggerated visual contrast between preventable and battle deaths was *rhetorically necessary* to motivate army reform. The flaw was the argument.

## When to use it — and when not to

Use a Nightingale Rose when the data is *genuinely cyclic* (months, quarters, compass bearings, hours) and the circular metaphor adds interpretive meaning that a bar chart cannot. Do not use it when your goal is precise comparison — the area distortion makes accurate reading nearly impossible without the values printed inside. Never use it for non-cyclic data: the circular arrangement implies a loop that doesn't exist. The correct alternative for most use cases is a **bar chart** : it encodes values as position on a common axis — the most accurate perceptual channel — with no area penalty.

## Framework reference & the one decision worth knowing

**The one decision worth knowing:** petals animate clockwise from January at 12 o'clock — not from the highest value, and not alphabetically. Cyclic data has a natural reading order (the calendar), and preserving that order is more important than dramatic reveal. Starting at 12 o'clock mirrors how we read clocks and compasses, making the monthly pattern immediately legible without a legend.

## Framework reference

> // FT Visual Vocabulary + Abela FT Visual Vocabulary: Part-to-whole / Cyclic Comparison .
            Abela quadrant: Comparison — comparing values across
            categories arranged in a cycle. Tufte would flag this chart's area
            distortion as a data-ink violation: non-data ink (the exaggerated outer
            area) is actively misleading, not merely decorative.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained nightingale in D3 v7. Two files:

1. `nightingale.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Nightingale" and the slide subtitle is "Summer peaks — July leads at 74, February trails at 27".

2. `nightingale/data.json` — the data file the chart loads via `d3.json("./nightingale/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Cyclic categorical data — typically 12 months or similar equal-interval periods. Each segment gets an equal angular slice; value encodes the petal radius (and thus area, which grows as r²). Best for cyclic patterns where the circular metaphor adds interpretive meaning.
  - `title`: string — chart headline
  - `unit`: string — what each value represents
  - `segments[].label`: string — category or period label (keep short, displayed radially)
  - `segments[].value`: number — positive value encoded as petal radius

Encoding: use the perceptually honest channel for this chart type (nightingale). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
