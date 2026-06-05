# Research: Chapter 05 — Comparison Charts
## Brutalist d3 x Claude

**Chapter one-line:** Bar, column, grouped, stacked, and radial charts depend on honest quantitative comparison.
**Research date:** 2026-06-01

---

## 1. Primary Sources

1. Cleveland and McGill, "Graphical Perception," 1984.
2. Tufte, *The Visual Display of Quantitative Information*.
3. Stephen Few, *Show Me the Numbers*.
4. Cairo, *The Truthful Art*.
5. Munzner, *Visualization Analysis and Design*.
6. D3 scale/axis/shape docs. Source: https://d3js.org/what-is-d3
7. FT Visual Vocabulary, comparison category.
8. Kelleher and Wagener, "Ten guidelines for effective data visualization."
9. Evergreen and Emery chart design checklist.
10. Heer and Bostock graphical perception replication.

## 2. Core Concept — State of the Field

Comparison charts should prioritize position and length on a common scale. Zero baseline is required for bar charts because bar area/length visually represents magnitude.

Stacked bars are useful for totals and rough composition but weak for comparing non-baseline components. Radial bars add perceptual cost and need strong justification.

## 3. Application Domain Examples

1. Horizontal bar for long category labels.
2. Grouped bar for subgroup comparison.
3. Stacked bar for total plus composition.
4. Bullet graph for target-versus-actual.
5. Radial bar only for cyclic structure, not ordinary ranking.

## 4. Book's Thesis Connection

Claude can produce any comparison chart, including misleading ones. The reader must specify scale, baseline, sort order, and comparison intent.

## 5. AI Wayback Machine — Candidate Figures

1. William Playfair — early bar/line charts.
2. William Cleveland — comparison accuracy.
3. Stephen Few — bullet graph and practical business charts.
4. Florence Nightingale — public comparison for action.

## 6. Pedagogical Delivery Research

Use a truncated baseline failure first. Readers should see why "looks more dramatic" is a truth problem.

## 7. Representation and Display Research

Checklist:

- Common scale?
- Zero baseline for bars?
- Sort order intentional?
- Labels readable?
- Grouping not overloaded?
- Color used for identity, not decoration?

## 8. Open Questions and Research Gaps

1. Include biological/medical zero-baseline misuse example if sourced.
2. Clarify when a dot plot beats a bar chart.
3. Add D3 prompt examples for horizontal and grouped bars.

