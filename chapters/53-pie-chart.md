# Pie Chart

*Pie Chart*

![Pie Chart](../images/53-pie-chart.jpg)

## The perceptual mechanism

A pie chart encodes quantitative values as **arc length and central angle** within a circle that represents 100% of the total. The viewer's visual system judges proportion by angle — the size of the "pie slice" — which is a weaker perceptual channel than position on a common axis (used by bar charts) but stronger than area alone. The key perceptual advantage of a pie chart is that it **communicates the whole simultaneously** : the reader can instantly see that one slice is "about a third" or "just under half" in relation to the complete circle, without needing to mentally sum a column of bars.

This part-to-whole relationship is what the pie chart is uniquely good at communicating, and it is the only circumstance where it should be used.

## The hard constraints — and why they exist

**No more than five slices.** Human angle discrimination degrades sharply below ~15°. At six or more slices, multiple segments become visually indistinguishable without reading the labels — at which point the chart is doing no perceptual work, and a sorted horizontal bar chart would be faster to read. This implementation enforces the five-slice limit by collapsing excess segments into "Other."

**Values must sum to a meaningful whole.** A pie chart is categorically wrong for data that does not constitute 100% of something. Survey responses that allow multiple answers, non-exhaustive category lists, and continuous measurements are all incorrect uses. The viewer's implicit assumption — "these slices account for everything" — must be true.

**Avoid multiple pies for comparison.** Comparing two pie charts side-by-side requires the viewer to mentally hold two sets of angles and compare them — a task humans perform badly. Two grouped bar charts with shared axes are dramatically easier to compare accurately.

## Why it was chosen for this data

The data structure is a **complete, exhaustive composition of five or fewer categories that sum to 100%** . The message is a single-distribution story: one category dominates, and the chart communicates that dominance at a glance. The reader needs to walk away with one proportion lodged in memory — not to compare seven categories precisely. That is the pie chart's job description.

## What the alternative would break

A **100% stacked bar chart** would allow more categories, enable multi-period comparison (one bar per time period), and be more accurate for precise proportion reading. It is the correct upgrade when either of these needs arise. A **donut chart** (togglable above) is perceptually equivalent to a pie chart but opens the centre for a summary statistic — useful when one number (total, selected %, dominant category) needs emphasis alongside the distribution.

## The one design decision worth knowing

Direct **arc labels** — percentage values placed on or adjacent to each slice — are strongly preferred over a detached legend. A legend requires the eye to travel off the chart, match a colour swatch, and return. A direct label eliminates that round-trip. The downside is that very small slices (under ~10°) cannot carry a readable label without a leader line — this implementation uses centroid-positioned labels and suppresses them on slices below 5% to prevent collision.

## Framework reference

> // Framework — FT Visual Vocabulary FT Visual Vocabulary category: Part-to-whole — "How a single entity is made up of its components." Abela quadrant: Composition (static, few periods). Tufte principle applied: the circle perimeter is data (100% of the whole); every arc is data (each category's share). The only non-data ink is the thin white stroke separating slices — necessary for figure–ground separation, not decoration.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained pie chart in D3 v7. Two files:

1. `pie-chart.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Pie Chart" and the slide subtitle is "Pie Chart".

2. `pie-chart/data.json` — the data file the chart loads via `d3.json("./pie-chart/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Proportional composition data for a pie chart. Maximum 5 slices — if your dataset has more categories, either consolidate smaller ones into an 'Other' bucket or switch to a 100% stacked bar chart. Values do not need to sum to 100; the chart normalises them. Provide raw counts or percentages — either works.
  - `label`: string — category name (keep short, ≤20 chars)
  - `value`: number — raw count or percentage share
  - `note`: string (optional) — annotation shown in tooltip

Encoding: use the perceptually honest channel for this chart type (pie chart). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Émile Cheysson** was a 19th-century French engineer and statistician who pioneered the use of pie charts and proportional area diagrams in public administration — making the form a workhorse of European government statistics decades after Playfair invented it.

![Émile Cheysson, circa 1880. AI-generated portrait based on a public domain photograph.](../images/emile-cheysson.jpg)
*Émile Cheysson, circa 1880. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Émile Cheysson, and how does his statistical-graphics work connect to the pie chart we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Émile Cheysson"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to recreate one of Cheysson's 1870s administrative pie charts in modern D3 — what changes about clarity?
- Ask it about the long-running debate over whether the pie chart is ever actually the right choice.

What changes? What gets better? What gets worse?
