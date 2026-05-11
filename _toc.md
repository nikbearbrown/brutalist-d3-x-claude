# Table of Contents — Brutalist d3 x Claude

*Drafted: 2026-05-08. Status: full first-pass draft; revision pending.*

---

## Front matter

- [Front matter (copyright, dedication, preface)](chapters/00-frontmatter.md) — *includes the Brutalist-system-applied-to-D3 preface*
- [Introduction](chapters/01-introduction.md) — *FiveThirtyEight Nigeria case + book overview*
- [Chapter 00 — Claude Basics for D3 Visualization](chapters/01a-chapter-00.md) — *four-move prompt structure, three D3-specific failure modes, three-layer verification*

## Planning documents (project-internal)

- [Book metadata](book.md)
- [Outline](outline.md)
- [Vision (Tic TOC Phase 1)](vision.md)
- [Architecture (Tic TOC Phase 2)](architecture.md)
- [Chapter specs (Tic TOC Phase 3)](chapters-spec.md)
- [Risks (Tic TOC Phase 4)](risks.md)
- [Run notes](_notes.md)

---

## Part I — The Decision Layer

- [Chapter 1 — Marks and Channels](chapters/02-chapter-01.md) — *Bertin → Cleveland & McGill → Munzner; Stevens' power law*
- [Chapter 2 — Chart Selection as Design Decision](chapters/03-chapter-02.md) — *Cairo's ethical frame; FT Visual Vocabulary; four-step framework*
- [Chapter 3 — Reading a Dataset](chapters/04-chapter-03.md) — *Data type identification; analyst vs. reader question; "compared with what?"*
- [Chapter 4 — Working with Claude Code](chapters/05-chapter-04.md) — *MBTA iteration model; Evergreen/Emery audit subset; full pipeline*

## Part II — The Chart Taxonomy

- [Chapter 5 — Comparison Charts](chapters/06-chapter-05.md) — *Bar, column, multiset, stacked, radial; zero-baseline rule; Few-resolved stance*
- [Chapter 6 — Time Series and Temporal Charts](chapters/07-chapter-06.md) — *Line, area, stacked area, stream graph, spiral, Gantt; Marey diagram*
- [Chapter 7 — Distribution Charts](chapters/08-chapter-07.md) — *Histogram, box plot, violin, density, stem-and-leaf; Tukey, graphicacy*
- [Chapter 8 — Relationship and Correlation Charts](chapters/09-chapter-08.md) — *Scatterplot, bubble, parallel coordinates, heatmap; Stevens' law on bubble area*
- [Chapter 9 — Part-to-Whole Charts](chapters/10-chapter-09.md) — *Pie, donut, waffle, Marimekko, Nightingale rose; five-slice rule*
- [Chapter 10 — Hierarchy Charts](chapters/11-chapter-10.md) — *Treemap, sunburst, circle packing, tree diagram; squarification*
- [Chapter 11 — Flow and Network Charts](chapters/12-chapter-11.md) — *Sankey, alluvial, chord, arc, force-directed; hairball mitigation*
- [Chapter 12 — Spatial and Geographic Charts](chapters/13-chapter-12.md) — *Choropleth, dot density, bubble map, connection map; Dupin and Snow*
- [Chapter 13 — Specialized and Financial Charts](chapters/14-chapter-13.md) — *Candlestick, Kagi, P&F, bullet graph, radar*

## Part III — Integration and Production

- [Chapter 14 — Design Principles in Practice](chapters/15-chapter-14.md) — *Tufte/Few/Cairo synthesis; Evergreen/Emery 22-point checklist*
- [Chapter 15 — Building a Complete Project](chapters/16-chapter-15.md) — *MBTA process model end-to-end; UNHCR worked example*

## Back matter

- [Back matter (acknowledgments, author bio, Chart Type Reference, references, colophon)](chapters/99-back-matter.md)

---

## Build pipeline

This book uses the existing Kindle/EPUB build pipeline:

```bash
./build.sh
```

Output goes to `output/` (gitignored). Upload `output/brutalist-d3-x-claude.epub` to KDP.

The chapter files are ordered by filename for the build:
- `00-frontmatter.md`
- `01-introduction.md`
- `01a-chapter-00.md` (Claude Basics)
- `02-chapter-01.md` through `16-chapter-15.md`
- `99-back-matter.md`

---

## Companion files

- `_project-guide.md` (TBD — running project for course-context use; pending Step 3 of the curriculum enrichment generator)
- `pantry/` — working D3 examples and theoretical reference documents
- `data/` — example datasets (forthcoming with Chapter 15's worked example)
- `styles/` — Kindle CSS overrides
