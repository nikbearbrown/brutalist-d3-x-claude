# Parallel Sets

*Higher education routes to higher income — but employment status reshapes the path*

![Parallel Sets](../images/51-parallel-sets.jpg)

## What this chart is

Parallel Sets encode the joint distribution of multiple categorical variables simultaneously. Each *dimension* is represented as a vertical axis; the categories within each dimension appear as proportional segments (blocks) on that axis. *Ribbons* connect adjacent dimensions: each ribbon represents the population subset that belongs to a specific category in dimension A *and* a specific category in dimension B. Ribbon width is proportional to that subset's count.

The key perceptual mechanism is width-along-a-common-baseline: the viewer reads the relative size of each ribbon as a proportion of the total at any given axis crossing. The flow direction is left-to-right, and at each axis the full width of all incoming ribbons equals the full width of the category block — the chart is mass-conserving.

## How it differs from a Sankey diagram

Both charts use proportional ribbon widths to show flow. The critical difference is structural. A **Sankey Diagram** shows flows between nodes in an arbitrary network — nodes can appear at any position, flows can cross and split in any direction, and the topology is defined by the data's actual directed graph. It is designed for process flows: energy systems, supply chains, user journeys with multiple possible paths.

A **Parallel Sets** chart imposes a strict rectangular axis structure. Every dimension occupies a vertical column; every category within a dimension occupies a proportional block on that column. Ribbons only connect adjacent columns — there are no backwards flows, no skipped dimensions. This structure enforces comparability: the viewer can scan vertically at any axis and read the marginal distribution of that dimension, then read ribbons horizontally to understand joint distributions.

## Why it was chosen here

The message involves the joint relationship between three categorical variables: Education, Employment Status, and Income. These are not process steps in a causal sequence — they are co-occurring attributes of a population. The question is distributional: "what proportion of the population occupies each combination of these three categories?"

A grouped bar chart could show one pairwise relationship at a time but would require six separate charts to cover all dimension pairs. A mosaic plot (Marimekko) could show two dimensions simultaneously. Parallel Sets handles three or more dimensions in a single view without losing the proportional encoding or introducing the dimension-ordering artefacts of a Parallel Coordinates Plot.

## What the rejected alternative breaks

A **Parallel Coordinates Plot** — the visually closest alternative — encodes each observation as a polyline crossing multiple continuous axes. It is designed for continuous data: each observation's exact value on each axis is plotted and connected. Applied to categorical data, all observations within a category collapse to the same line, producing overplotted bands that are indistinguishable from one another without transparency hacks. Parallel Sets solves this by encoding aggregated counts as ribbon widths rather than individual observations as lines.

A **Sankey Diagram** would work but implies directionality and process. Showing Education → Income as a Sankey implies that education *causes* income through a flow process. Parallel Sets makes no such implication — it shows co-occurrence, not process, and the rectangular axis structure signals correlation rather than causation.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained parallel sets in D3 v7. Two files:

1. `parallel-sets.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Parallel Sets" and the slide subtitle is "Higher education routes to higher income — but employment status reshapes the path".

2. `parallel-sets/data.json` — the data file the chart loads via `d3.json("./parallel-sets/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Joint categorical distribution of 1,200 survey respondents across three dimensions: Education level, Employment Status, and Income Bracket. Each flow record represents a unique combination of one category from each dimension and the count of respondents in that combination.
  - `dimensions`: array of strings — ordered dimension names, left to right on the chart
  - `categories`: object — maps each dimension name to an ordered array of its category labels (order determines top-to-bottom block order on each axis)
  - `flows`: array of flow records. Each record has: 'keys' (array of category labels, one per dimension, in the same order as 'dimensions') and 'value' (number of respondents in that combination)

Encoding: use the perceptually honest channel for this chart type (parallel sets). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **John B. Sparks** published the *Histomap of Evolution* (1932) and *Histomap of World History* (1931) — five-foot fold-out charts that ran from antiquity to the present, with each civilization rendered as a horizontal ribbon whose width tracked its relative power. Multiple categorical bands, time on one axis, magnitude in band-width, the whole thing readable as a single image: the parallel-sets form, drawn by hand on cardstock.

![John B. Sparks, circa 1933. AI-generated portrait based on a public domain photograph.](../images/john-b-sparks.jpg)
*John B. Sparks, circa 1933. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was John B. Sparks, and how do his Histomap ribbons connect to the parallel-sets form we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"John B. Sparks Histomap"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Sparks's 1931 ribbon charts handle the multi-category-over-time problem — and where the form breaks down at extreme scale.
- Ask it to compare Sparks's hand-drawn Histomap with a modern parallel-sets diagram of the Titanic survival data — what reading tasks each does well.

What changes? What gets better? What gets worse?
