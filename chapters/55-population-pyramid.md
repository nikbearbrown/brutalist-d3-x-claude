# Population Pyramid

*Age & Sex Distribution — Two Population Profiles Side by Side*

![Population Pyramid](../images/55-population-pyramid.jpg)

## What this chart is

A population pyramid is two back-to-back horizontal bar charts sharing a common categorical y-axis of age bands. Female bars extend leftward; male bars extend rightward. The x-axis encodes either absolute count or percentage of total population. The overall silhouette — the outline formed by all bar ends — is the primary signal: a wide base tapering to a narrow top indicates high fertility and high mortality (expansive, developing); a near-uniform column indicates stable fertility and mortality (stationary, developed); a narrow base widening in middle age then tapering indicates an ageing population with declining fertility (constrictive). This silhouette reading is the key perceptual advantage over a table: demographic structure becomes a shape, not a number.

## Why it was chosen here

The data is a bivariate categorical distribution — age band crossed with sex — and the message is about demographic structure, not a specific value comparison. A grouped bar chart could show the same numbers but would lose the bilateral symmetry convention that allows immediate sex-ratio reading at each age band. A stacked bar chart across age bands would collapse the male/female distinction. The back-to-back layout exploits the viewer's bilateral symmetry detection: any horizontal imbalance between left and right bars is immediately visible as a sex-ratio anomaly — war cohort gaps, female longevity advantage in older bands, and selective migration effects are all apparent before any number is read. No other chart type makes this comparison as effortless.

## What the alternative would break

A standard histogram for each sex in separate panels would work but requires the viewer to mentally align two separate scales. The back-to-back layout enforces shared axes, which is precisely what makes silhouette comparison possible. An area chart of population over age for each sex would show the distribution shape but lose the discreteness of age-band counts, which matters for policy planning (pension age thresholds, school cohort sizing). A line chart across age bands would imply continuity between categorical bins — age bands are ordered but not continuous in the same way that years are, and bar encoding correctly communicates that each band is a distinct count.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary category: Distribution — "Show the range and concentration of values in a dataset, here bivariate (age × sex)." Abela quadrant: Distribution / Comparison (comparing two distributions across the same ordered categories). The one design decision worth knowing: the x-axis is mirrored — female values are positive numbers plotted leftward using a reversed scale, not negative numbers. This keeps the axis labels positive and avoids the cognitive double-negation of reading "negative population." D3 implements this with two separate linear scales sharing the same domain [0, maxVal], with the female scale's range reversed.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained population pyramid in D3 v7. Two files:

1. `population-pyramid.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Population Pyramid" and the slide subtitle is "Age & Sex Distribution — Two Population Profiles Side by Side".

2. `population-pyramid/data.json` — the data file the chart loads via `d3.json("./population-pyramid/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Population pyramid data for four countries. Each dataset contains age bands with female and male counts in thousands. Replace with real census data.
  - `datasets[key].label`: string — displayed as chart subtitle
  - `datasets[key].shape`: string — shape classification: Expansive, Constrictive, Stationary, Transitional, Inverted
  - `datasets[key].shapeNote`: string — one-line interpretation of the shape (shown as badge tooltip)
  - `datasets[key].data[].band`: string — age band label (ordered youngest to oldest)
  - `datasets[key].data[].female`: number — female population count (thousands)
  - `datasets[key].data[].male`: number — male population count (thousands)

Encoding: use the perceptually honest channel for this chart type (population pyramid). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
