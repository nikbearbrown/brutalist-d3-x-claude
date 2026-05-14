# Stem Leaf

*Section B clusters in the 70s and 80s — Section A spreads wider with more extreme values on both ends*

![Stem Leaf](../images/68-stem-leaf.jpg)

## What this chart is

A Stem and Leaf Plot organises a dataset by its place values. Each value is split into a *stem* (the leading digit or digits, typically representing the tens place) and a *leaf* (the trailing digit, representing the ones place). Stems are arranged in ascending order in a central column; leaves extend horizontally from their corresponding stem.

The defining property is **losslessness** : every original data value is preserved in full and can be reconstructed exactly by combining its stem and leaf. A score of 74 appears as leaf "4" next to stem "7". No aggregation, no binning, no smoothing — the raw data is the chart. This makes the stemplot the only distribution chart that doubles as a complete data reference.

// Example: dataset (2, 4, 11, 17, 20, 23) 0 | 2  4 1 | 1  7 2 | 0  3 stem = tens digit · leaf = ones digit

## Back-to-back stemplots

When two datasets share the same stem values, they can be displayed back-to-back: one dataset's leaves extend to the left, the other's to the right. The stems occupy the shared central column. This allows direct visual comparison of two distributions at every stem level simultaneously — the viewer reads one dataset's shape from right to left and the other from left to right, and the asymmetry between them is immediately visible.

The back-to-back stemplot is the simplest multi-dataset comparison tool that preserves every data value. A side-by-side box plot compresses each dataset to five numbers; back-to-back histograms bin the data; the back-to-back stemplot shows everything.

// Back-to-back: Group A | Stem | Group B 9  4  2 | 6 | 1  5  8 8  5  3  1 | 7 | 2  4  6 7  2 | 8 | 0  3  3  9 Group A leaves read right-to-left

## Why it was chosen here

The message compares two class sections' exam score distributions. The dataset is small enough (25–30 values per section) that every data point can be displayed without overcluttering — this is the stemplot's optimal range. Binning the data into a histogram would lose the exact scores; a box plot would reduce each section to five numbers and hide the clustering pattern in the 70s and 80s.

The back-to-back mode is specifically chosen because the two sections share the same stem structure (60s, 70s, 80s, 90s) and a direct row-by-row comparison — "how many students scored in the 70s in Section A versus Section B?" — is the core question. The shared stem column makes this comparison structurally explicit.

## Size limits and when not to use it

The stemplot has hard practical limits in both directions. With fewer than 10–15 values, most stem rows contain 0–1 leaves; the "distribution" is too sparse to have a shape, and a simple sorted list is more useful. With more than 50–80 values per dataset, stem rows become crowded with 10+ leaves, the display wraps, and the visual distribution signal is lost in a wall of digits.

Within its range, the stemplot excels for exploratory data analysis, classroom settings, and any context where the analyst needs to see the actual values — not a smoothed representation of them. Outside that range, a histogram (more data) or a dot plot / table (less data) is the appropriate substitute.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained stem leaf in D3 v7. Two files:

1. `stem-leaf.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Stem Leaf" and the slide subtitle is "Section B clusters in the 70s and 80s — Section A spreads wider with more extreme values on both ends".

2. `stem-leaf/data.json` — the data file the chart loads via `d3.json("./stem-leaf/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Exam scores (0–100) for two fictional class sections. Section A has a wider spread with more extreme values on both ends. Section B clusters tightly in the 70s and 80s. Both sections have 28 students. The back-to-back stemplot reveals these distributional differences at every stem level simultaneously.
  - `section_a`: array of integers — raw exam scores for Section A. Values are integers 0–100. Optimal range for stemplot display: 20–50 values.
  - `section_b`: array of integers — raw exam scores for Section B. Same scale as section_a for meaningful back-to-back comparison.

Encoding: use the perceptually honest channel for this chart type (stem leaf). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Arthur Lyon Bowley** was a British statistician who in 1901 produced *Elements of Statistics* — the first English-language statistics textbook to systematically use simple visual displays (including a precursor to stem-and-leaf and dot displays) to teach inferential reasoning.

![Arthur Lyon Bowley, circa 1920. AI-generated portrait based on a public domain photograph.](../images/arthur-lyon-bowley.jpg)
*Arthur Lyon Bowley, circa 1920. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Arthur Lyon Bowley, and how does his early statistical-graphics work connect to the stem-and-leaf display we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Arthur Lyon Bowley"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to compare Bowley's 1901 dot displays with Tukey's 1977 stem-and-leaf plot — what's the design lineage?
- Ask it about Bowley's pioneering work on the sampling theory of survey statistics.

What changes? What gets better? What gets worse?
