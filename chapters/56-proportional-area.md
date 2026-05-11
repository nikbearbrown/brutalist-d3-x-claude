# Proportional Area

*North America + East Asia hold 62% of global AI for Good investment*

![Proportional Area](../images/56-proportional-area.jpg)

## What this chart is

A Proportional Area Chart encodes quantitative values as the *area* of geometric shapes — most commonly circles, but any closed shape works. The perceptual mechanism is **area estimation** : the eye reads the space inside the shape and compares it across items. Area estimation is less precise than position on a common axis (the bar chart's mechanism), which makes proportional area charts better suited to *presentational* contexts — conveying the scale of differences at a glance — than to *analytical* ones, where readers need to extract specific values. Value labels inside or beside circles are required; the chart alone cannot support accurate reading.

## Why it was chosen here

The data spans **43:1** from the largest to the smallest value ($8,420M to $195M). A bar chart would render this honestly but the smallest bars would be barely visible without a log scale, which introduces its own perceptual problems. A proportional area chart handles extreme ratios naturally: the eye tolerates wide size variation between circles and still perceives the relative scale. The circular form also avoids implying a ranking or sequence — these are independent regions, not ordered categories. The packed layout groups them naturally without imposing a spatial hierarchy that doesn't exist in the data.

## The encoding error — and how to spot it

// the common mistake If you set radius ∝ value instead of area ∝ value , area grows as value².
            North America ($8,420M) is 43× larger than Oceania ($195M).
            With correct area encoding: visually 43× larger area .
            With radius encoding: visually 1,849× larger area .
            The error amplifies differences by a factor equal to the value ratio.
            Hit the radius error toggle on slide 1 and watch the
            small circles become nearly invisible.

D3's fix: use `d3.scaleSqrt()` or pass the raw value to `hierarchy.sum()` and let `d3.pack()` compute `r = sqrt(value)` internally. Never map value directly to radius.

## Framework reference & the one decision worth knowing

**The one decision worth knowing:** circle color uses the same sequential scale as the size (darker = larger value). This is *double encoding* — both area and colour encode the same variable. That's usually redundant and inefficient; here it is deliberate. Double encoding reinforces the size hierarchy for viewers who find area estimation difficult, and it makes the smallest circles (which are almost invisible by area) still perceptible by hue contrast.

## Framework reference

> // FT Visual Vocabulary + Tufte FT Visual Vocabulary: Magnitude — Size comparison .
            Abela quadrant: Comparison — comparing the relative
            magnitude of items without a continuous axis. Tufte: proportional area
            charts sacrifice data-ink ratio precision for gestalt comprehension;
            acceptable only when the scale of difference is the message, not the
            precise values.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained proportional area in D3 v7. Two files:

1. `proportional-area.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Proportional Area" and the slide subtitle is "North America + East Asia hold 62% of global AI for Good investment".

2. `proportional-area/data.json` — the data file the chart loads via `d3.json("./proportional-area/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Flat dataset for proportional area (bubble) chart. Each item gets a circle whose AREA is proportional to its value. D3 pack layout positions and sizes circles automatically. The radius-error toggle demonstrates what happens when radius (not area) is used — a common and serious implementation mistake.
  - `title`: string — chart headline
  - `unit`: string — display unit for values
  - `items[].id`: string — unique identifier
  - `items[].label`: string — display label (keep concise for in-circle text)
  - `items[].short`: string — abbreviated label for small circles
  - `items[].value`: number — positive value; circle AREA will be proportional to this

Encoding: use the perceptually honest channel for this chart type (proportional area). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).
