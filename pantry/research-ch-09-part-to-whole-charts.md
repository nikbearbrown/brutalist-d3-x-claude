# Research: Chapter 09 — Part-to-Whole Charts
## Brutalist d3 x Claude

**Chapter one-line:** Part-to-whole charts trade exact comparison for composition, and each form has a perceptual cost.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Cleveland and McGill, "Graphical Perception," 1984.
2. Bertin, *Semiology of Graphics*.
3. Cairo, *The Truthful Art*.
4. Tufte, *The Visual Display of Quantitative Information*.
5. Stephen Few, *Show Me the Numbers*.
6. D3 shape, arc, pie, and stack docs. Source: https://d3js.org/
7. Friendly, history of data visualization.
8. Florence Nightingale polar area diagrams.
9. Heer and Bostock graphical perception replication.
10. FT Visual Vocabulary.

## 2. Core Concept — State of the Field

Part-to-whole charts rely on angle, area, or stacked length. These channels are weaker than position on a common scale, so the author must justify why composition is the question.

Pie and donut charts can be honest with few categories and large differences. Waffle charts provide countable equal-area units. Marimekko and rose charts add expressive power but increase perceptual burden.

## 3. Application Domain Examples

1. Pie chart for a few large, simple proportions.
2. Donut chart when center annotation adds value.
3. Waffle chart for countable proportions.
4. Marimekko for two-dimensional composition.
5. Nightingale rose for advocacy with explicit distortion disclosure.

## 4. Book's Thesis Connection

Claude will happily produce beautiful part-to-whole charts. The reader must decide whether the chart asks for composition or whether a bar chart would communicate the comparison more truthfully.

## 5. AI Wayback Machine — Candidate Figures

1. Florence Nightingale — polar area chart and sanitary reform.
2. Jacques Bertin — area as visual variable.
3. Cleveland and McGill — angle versus length accuracy.
4. Stephen Few — practical critique of pie charts.

## 6. Pedagogical Delivery Research

Use a 14-slice pie as the failure case, then rebuild it as a sorted bar chart and a five-slice grouped pie with "other."

## 7. Representation and Display Research

Checklist:

- Composition is the real question?
- Slice count limited?
- Parts sum to a meaningful whole?
- Labels direct and readable?
- Area distortions disclosed?
- Color palette not doing unnecessary work?

## 8. Open Questions and Research Gaps

1. Source a defensible five-slice rule explanation.
2. Add guidance for "other" categories.
3. Include a Claude prompt that rejects pie charts when category count is too high.
