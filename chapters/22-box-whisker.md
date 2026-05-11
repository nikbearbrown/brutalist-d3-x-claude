# Box and Whisker Plot

*Five Numbers, One Glyph — Tukey's Distribution Sketch*

![Box and Whisker Plot](../images/22-box-whisker.jpg)

## What this chart is

A box and whisker plot is the chart John Tukey introduced in *Exploratory Data Analysis* (1977) to summarise a univariate distribution as a single compact glyph. The glyph carries five numbers: the minimum (or lower fence), the first quartile (Q1), the median, the third quartile (Q3), and the maximum (or upper fence). The box spans Q1 to Q3 — the interquartile range, IQR — and contains the middle 50% of observations. A line drawn across the box at the median tells the viewer where the center is and, by its offset within the box, how skewed the distribution is. Whiskers extend from the box ends to the most extreme observations within 1.5 × IQR; observations beyond that fence are plotted individually as outlier points.

The "box plot" name and the "box and whisker plot" name refer to the same chart. The longer name is Tukey's; the shorter is the abbreviation that took over in the 1990s. Both describe a glyph whose ink is, almost entirely, statistical signal.

## How to read this chart

Read the median line first. Its position tells you the center and, by its offset within the box, the direction and degree of skew: a median pushed toward the bottom of the box indicates a right-skewed distribution; pushed toward the top, left-skewed; centered, roughly symmetric. Read the box width second. A wide box means high variance in the middle 50%; a narrow box means tight clustering. Read the whisker lengths third. Asymmetric whiskers reveal tail asymmetry that the box itself cannot show. Read the outlier dots last. Each dot beyond a whisker is a value the 1.5 × IQR fence has flagged as worth a separate glance — it does not mean the value is "wrong," only that it sits in the distribution's tail.

When several boxes appear side by side on a shared axis, the comparison reads at a glance: differences in median position become differences in line height; differences in spread become differences in box and whisker length; differences in outlier behavior become differences in dot patterns above and below.

## Why the 1.5 × IQR rule

Tukey set the whisker length at 1.5 × IQR by deliberate calibration. Under a normal distribution, the rule flags roughly 0.7% of observations as potential outliers — small enough that a typical sample produces few flagged points, large enough that genuinely anomalous values are not absorbed into the whisker silently. The rule is robust: because IQR uses the middle 50% of the data, it is insensitive to the outliers it is trying to detect. A rule based on standard deviations would not be — outliers contaminate the standard deviation, which then masks the very anomalies the rule is meant to flag.

The rule is a heuristic, not a probabilistic threshold. Some implementations expose a multiplier setting; some make the boundary `min(max-value, Q3 + 1.5 × IQR)` rather than `Q3 + 1.5 × IQR` exactly. The convention to follow in published charts is Tukey's original: 1.5 × IQR, fences clipped to the actual data extreme inside that bound, points beyond rendered individually.

## What the alternative would break

A bar chart of group means with error bars — the substitute most commonly chosen by audiences trained on parametric statistics — assumes the distribution is roughly symmetric and approximately normal. The moment one group is skewed, the error bar either crosses zero (when zero is not a realistic value) or implies symmetric tails that do not exist in the data. The viewer reads the chart as if the groups differ in average; the real story is in skew or tail behavior the encoding has erased.

A scatter of all individual points reveals everything the box plot summarises but collapses into overplotting at sample sizes above ~40 unless jittered, and even jittered scatter requires the viewer to estimate quartiles by eye. A violin plot adds a kernel density curve to the box plot and reveals multimodality the box plot hides — at the cost of requiring more sample (KDE bandwidth choices need observations) and more reader literacy. Use the box plot when the audience needs five numbers, fast; use the violin when the distribution shape itself is the story.

## Framework reference

> // FRAMEWORK FT Visual Vocabulary category: **Distribution** — "Show the range of values in a dataset and how they are distributed." Abela quadrant: Distribution (single variable, multiple groups, comparison of shape). Tufte principle: the box plot is data-ink near 1.0 — every pixel of every glyph encodes a quantile, the median, a fence, or an outlier. The one design decision worth knowing: 1.5 × IQR for the whisker fence, set by Tukey in 1977, is the convention the chart's interpretive grammar depends on. Changing it silently breaks the reader's ability to compare across charts.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained box-and-whisker plot in D3 v7. Two files:

1. `box-whisker.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover that shows the five-number summary and outlier values. The page title is "Box and Whisker Plot" and the slide subtitle is "Five Numbers, One Glyph — Tukey's Distribution Sketch".

2. `box-whisker/data.json` — the data file the chart loads via `d3.json("./box-whisker/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Three to six groups of continuous measurements, n=60–120 each, themed for an audience that cares about realistic distribution shapes (e.g., test scores by class, response times by region, salaries by role). Compute Q1, median, Q3, lower and upper whisker (using Tukey's 1.5 × IQR rule), and outlier values at render time from the raw arrays.
  - `group`: string — category label, drives the band axis
  - `values`: number[] — raw measurements per group

Encoding: position along a common scale for the value axis. Box drawn between Q1 and Q3 with a median line; whiskers drawn to the most extreme value within 1.5 × IQR of the box; outliers plotted as individual points beyond. Annotate the chart with a one-line in-chart subtitle. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
