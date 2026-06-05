# Research: Chapter 07 — Distribution Charts
## Brutalist d3 x Claude

**Chapter one-line:** Distribution charts reveal shape, spread, outliers, and uncertainty, but binning and summaries can hide the story.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Cleveland and McGill, "Graphical Perception," 1984.
2. Tufte, *The Visual Display of Quantitative Information*.
3. Tukey, *Exploratory Data Analysis*.
4. Munzner, *Visualization Analysis and Design*.
5. Cairo, *The Truthful Art*.
6. D3 histogram/bin, scale, axis, and shape docs. Source: https://d3js.org/
7. Observable Plot docs for histograms, density, and marks. Source: https://observablehq.com/plot/
8. Kelleher and Wagener, "Ten guidelines for effective data visualization."
9. Evergreen and Emery data visualization checklist.
10. Heer and Bostock graphical perception replication.

## 2. Core Concept — State of the Field

Distribution charts answer questions about shape rather than single values. Histograms depend on bin width; box plots summarize robustly but hide multimodality; violin and density plots show shape but introduce smoothing assumptions.

The chapter should treat binning, smoothing, and summary statistics as design decisions that can change the argument a chart appears to make.

## 3. Application Domain Examples

1. Histogram for values across a population.
2. Box plot for comparing groups with medians and quartiles.
3. Violin plot for group distributions where shape matters.
4. Ridgeline plot for repeated distributions over time or categories.
5. Dot/strip plot for small samples where every observation should remain visible.

## 4. Book's Thesis Connection

Claude can generate distribution charts quickly, but the reader must inspect whether the chosen bin width, smoothing, and summary form preserve the pattern the data actually supports.

## 5. AI Wayback Machine — Candidate Figures

1. John Tukey — box plot and exploratory data analysis.
2. William Cleveland — distribution and visual perception.
3. Florence Nightingale — distributions used for reform arguments.
4. John Snow — spatial distribution as evidence.

## 6. Pedagogical Delivery Research

Use one dataset where a wide bin hides bimodality and a narrower bin reveals it. Then compare histogram, box plot, and violin plot so readers see what each form compresses.

## 7. Representation and Display Research

Checklist:

- Bin width disclosed and tested?
- Sample size visible?
- Outliers handled honestly?
- Smoothing assumptions clear?
- Group comparisons share scales?
- Summary statistics not substituting for the distribution?

## 8. Open Questions and Research Gaps

1. Add a sourced failure case where binning changes interpretation.
2. Include a small-sample warning for violin/density plots.
3. Write a Claude prompt pattern for "show me three bin widths before finalizing."
