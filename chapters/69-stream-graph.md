# Stream Graph

*Music Genre Dominance — Streaming Volume 2000–2023*

![Stream Graph](../images/69-stream-graph.jpg)

## What this chart is

A stream graph is a stacked area chart where the baseline is not fixed at zero but is instead computed by a symmetric wiggle algorithm that minimises the average slope of all layer edges simultaneously. This produces the characteristic river-like silhouette: streams swell where values peak and contract where they decline, with the central axis itself oscillating to distribute visual weight symmetrically around the horizontal midpoint. The perceptual mechanism is shape and area: the viewer reads the relative thickness of each stream as its proportional magnitude at any point in time, and the organic curvature makes temporal trends more intuitively readable than the jagged edges of a zero-baseline stacked area chart. The chart is explicitly optimised for pattern detection, not precision reading — exact values require the interactive tooltip layer.

## Why it was chosen here

The dataset is seven music genres measured across 24 years, and the message is about long-run trends and the transition of dominance — not precise annual values. The stream graph excels precisely at this use case: a large volume of temporal categorical data where the interesting signal is the rise and fall of relative magnitudes rather than exact numbers. The symmetric wiggle baseline suppresses visual bias toward any particular layer — in a zero-baseline stacked area chart, the bottom layer always appears visually stable while upper layers appear to fluctuate wildly, an artefact of the stacking rather than the data. The wiggle baseline distributes this distortion across all layers equally. The normalised mode (percentage expand) allows proportional reading when relative share is the question.

## What the alternative would break

A stacked area chart with a zero baseline would communicate the same data but introduce two artefacts: visual instability for upper layers caused by the cumulative stack (not the data), and a misleading implied absolute baseline that suggests quantities can be read against an axis — which they cannot without vertical gridlines. A line chart for each genre would allow precise reading of individual trends but makes cross-category comparison and total-volume reading impossible. The catalogue's caution is correct: small categories are visually suppressed in a stream graph. This implementation mitigates the suppression issue by providing click-to-isolate, which expands any layer to the full viewport height for isolated reading.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary category: Change Over Time — "Show change in value of one or more variables, here multiple categories stacked with a symmetric baseline." Tufte caution: the stream graph sacrifices readability of exact values for aesthetic engagement and pattern salience — an intentional trade. The one design decision worth knowing: layer ordering matters critically. Layers are sorted by variance (most variable in the middle, most stable at edges) — this keeps the visually dominant central layers informative while stable layers form calm borders, preventing the common failure of burying the most interesting data under stable layers at the top or bottom.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained stream graph in D3 v7. Two files:

1. `stream-graph.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Stream Graph" and the slide subtitle is "Music Genre Dominance — Streaming Volume 2000–2023".

2. `stream-graph/data.json` — the data file the chart loads via `d3.json("./stream-graph/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Stream graph data: time-series values for multiple categories. Values are a relative index (0–100 scale). Years and series values must be parallel arrays of the same length.
  - `years`: number[] — x-axis time points (integers, in order)
  - `series[].id`: string — unique key, must match COLORS lookup in JS
  - `series[].label`: string — display name in legend and tooltip
  - `series[].values`: number[] — one value per year, parallel to years array. Can be absolute counts or a normalised index. Stream graph does not require values to sum to a constant per time point.

Encoding: use the perceptually honest channel for this chart type (stream graph). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Joseph Fourier** proved in 1822 that any periodic function could be decomposed into a sum of stacked sinusoids — and that the sum, drawn on paper as overlapping waveforms, was a more legible record of the underlying components than the raw signal. Strip away the trigonometry and you have the stream-graph: many categorical waveforms stacked, the total flowing through a baseline-free curve, the structure visible only after the decomposition is plotted.

![Joseph Fourier, circa 1820. AI-generated portrait based on a public domain engraving.](../images/joseph-fourier.jpg)
*Joseph Fourier, circa 1820. AI-generated portrait based on a public domain engraving (Wikimedia Commons).*

**Run this:**

```
Who was Joseph Fourier, and how does his Fourier-series decomposition connect to the stream-graph form we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Joseph Fourier series"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how a Fourier decomposition of monthly retail sales would look as a stream graph — and what gets lost when you collapse the harmonic components into stacked layers.
- Ask it to compare Fourier's 1822 *Théorie analytique de la chaleur* with the 2008 NYT stream-graph of box-office data (Lee Byron) — what makes both "the same chart."

What changes? What gets better? What gets worse?
