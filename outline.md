# Brutalist d3 x Claude — Outline

**Author:** Nik Bear Brown

---

## Front Matter

- **Copyright**
- **Dedication** *(optional)*
- **Preface** — The API curve is solved. The design problem isn't.

---

## Introduction

Why D3 visualization has always been two problems — the programming problem and the design problem — and why Claude Code changes which one you need to solve yourself.

---

## Part I — The Decision Layer

1. **Marks and Channels** — The grammar beneath every chart: how visual variables encode data, which encodings are perceptually accurate, and why position is king.

2. **Chart Selection as Design Decision** — The FT Visual Vocabulary and Data Visualisation Catalogue as navigation tools; the four-step decision framework; functional categories as a selection heuristic.

3. **Reading a Dataset** — Before touching D3: identifying what type of data you have, what relationship you want to show, and what question your reader needs to answer.

4. **Working with Claude Code** — Setting up the Claude Code + D3 pipeline; how to prompt for a visualization; how to evaluate and iterate on output; what Claude Code cannot decide for you.

---

## Part II — The Chart Taxonomy

5. **Comparison Charts** — Bar, column, multiset, stacked, radial; when each works and when each misleads; the zero-baseline rule; the label-length heuristic.

6. **Time Series and Temporal Charts** — Line, area, stacked area, stream graph; Gantt and timeline; spiral plots for cyclic data; the don't-skip-intervals rule.

7. **Distribution Charts** — Histogram, stem-and-leaf, box and whisker, violin, density/KDE; why box plots hide what violin plots reveal; when each earns its place.

8. **Relationship and Correlation Charts** — Scatterplot, bubble chart, connected scatter, parallel coordinates, heatmap; error bars and uncertainty; the correlation-is-not-causation annotation.

9. **Part-to-Whole Charts** — Pie, donut, waffle, pictogram, Marimekko; why pie charts earn their criticism; the five-slice rule; Nightingale rose and its honest distortion.

10. **Hierarchy Charts** — Treemap, sunburst, circle packing, tree diagram, dendrogram; squarified algorithms; when to show depth vs. proportion.

11. **Flow and Network Charts** — Sankey, alluvial, chord, arc diagram; force-directed networks; when width carries meaning and when it carries noise.

12. **Spatial and Geographic Charts** — Choropleth, dot map, bubble map, connection map, flow map; the area-size distortion problem; when to use ratio vs. absolute values.

13. **Specialized and Financial Charts** — Candlestick, OHLC, Kagi, Point & Figure; bullet graph; radar/spider; polar area; time-independent charts.

---

## Part III — Integration and Production

14. **Design Principles in Practice** — Proportional ink, data-ink ratio, color for categorical vs. quantitative, accessibility and color-blind palettes, annotation strategy.

15. **Building a Complete Project** — From raw data to published output: data cleaning, chart selection, Claude Code implementation, embed and responsiveness. A worked humanitarian data case.

---

## Back Matter

- **Acknowledgments**
- **About the Author**
- **Chart Type Reference** — one-page decision guide
- **References**

---

## Notes on Order

Part I before Part II because mark-and-channel theory is the prereq for evaluating any specific chart form. Chapters 5–13 in Part II are roughly ordered by pedagogical accessibility: bar charts are the most familiar starting point; spatial and financial charts require more context. Chapters within Part II can be taught in any order after Chapter 5, making the book modular for instructors who want to assign specific chart families to match course data.

Chapter 4 (Claude Code workflow) is positioned at the end of Part I because students need the design vocabulary from Chapters 1–3 before they can meaningfully evaluate Claude Code output.
