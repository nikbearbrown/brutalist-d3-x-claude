# Run Summary — 2026-05-08

## Brutalist d3 x Claude — Full Draft Completed

This document summarizes the run for review. For full detail, see `_notes.md`.

---

## What was completed

A full first-pass draft of *Brutalist d3 x Claude* — 19 documents, approximately 130,000 words.

**Front matter and book-level documents:**
- Front matter: copyright, dedication, **and a substantial preface positioning the book as the D3 renderer module of the Brutalist system** (per user instruction). The preface walks the Brutalist phase model, labor separation, supervisory capacities, and two-governing-files structure as they apply to D3 specifically.
- Introduction: opens with the Cairo/FiveThirtyEight Nigeria kidnapping case (per the spec); states the book's argument that the design layer is the hard layer; maps the chapters.
- Chapter 00 — Claude Basics for D3 Visualization. Four-move prompt structure; three D3-specific failure modes (API hallucination, chart-type mismatch, channel mismatch); three-layer verification stack.

**Part I — The Decision Layer (4 chapters):**
- Ch 1 — Marks and Channels. Bertin → Cleveland & McGill → Munzner spine. Stevens' power law as mechanism. Bertin's specific cases (Minard, Snow, Nightingale).
- Ch 2 — Chart Selection as Design Decision. Cairo's four-step framework. FT Visual Vocabulary's eight functional categories. Three failure modes (familiarity bias, aesthetic-first, software-default).
- Ch 3 — Reading a Dataset. Data type identification. Analyst-vs-reader question. "Compared with what?" check.
- Ch 4 — Working with Claude Code. MBTA iteration model. Evergreen/Emery audit subset. Full pipeline integrating Chs 1, 2, 3.

**Part II — The Chart Taxonomy (9 chapters):**
- Ch 5 — Comparison Charts. Bar, column, multiset, stacked, radial. Few-resolved stance on zero baseline.
- Ch 6 — Time Series. Line, area, stacked area, stream, spiral, Gantt. Marey diagram. Zero baseline differentially applied (areas vs. lines).
- Ch 7 — Distribution. Histogram, box plot, violin, density, stem-and-leaf. Tukey, Cairo's graphicacy.
- Ch 8 — Relationship. Scatterplot, bubble, parallel coordinates, heatmap. Stevens' power law on bubble area; correlation-is-not-causation as Cairo-class moral requirement.
- Ch 9 — Part-to-Whole. Pie, donut, waffle, Marimekko, Nightingale rose. Five-slice rule; Cleveland & McGill on angle.
- Ch 10 — Hierarchy. Treemap, sunburst, circle packing, tree diagram. Squarification. Depth limits.
- Ch 11 — Flow/Network. Sankey, alluvial, chord, arc, force-directed. Width-as-channel; hairball mitigation.
- Ch 12 — Spatial. Choropleth, dot density, bubble map, connection map. Dupin 1826; Snow 1854; ratio-vs-absolute.
- Ch 13 — Specialized. Candlestick, Kagi, P&F, bullet graph, radar. Few's argument for bullet graphs replacing gauges.

**Part III — Integration and Production (2 chapters):**
- Ch 14 — Design Principles in Practice. Tufte/Few/Cairo synthesis. Evergreen/Emery 22-point checklist applied in full. Chartjunk debate explicitly resolved with Few's position.
- Ch 15 — Building a Complete Project. MBTA process model walked end-to-end on a UNHCR humanitarian dataset. Brutalist phases A through E.

**Back matter:** Acknowledgments, About the Author, Chart Type Reference one-pager, full references, colophon.

---

## Voice and method

The voice is course-textbook, scene-anchored, code-aware. Each chapter follows the 12-section anatomy from the updated `chapters-spec.md`:

1. Three suggested titles
2. Chapter overview (1 paragraph)
3. Learning objectives (3-5, Bloom's level explicit)
4. Opening case (real visualization failure or success)
5. Theoretical grounding (sources introduced when needed)
6. Core content sections (4-6, each: concept → mechanism → example → application)
7. Mid-chapter checkpoint
8. Extended worked example from the Humanitarians AI pantry
9. Chapter summary (capabilities gained)
10. Key terms
11. Discussion questions (3-5, at least one cross-chapter synthesis)
12. Exercises (warm-up / application / synthesis / challenge)
13. LLM Exercise (Claude Code task)
14. Further reading
15. Tags

Most chapters opened with real or pantry-grounded examples (the FiveThirtyEight Nigeria case for the Introduction; two scatterplots of GDP/life expectancy for Ch 1; the 14-slice pie chart from a humanitarian report for Ch 2; the AI capability bar chart for Ch 5; the AI capability gap line chart for Ch 6; Snow's cholera dot map and Dupin's choropleth as historical anchors for Ch 12). The Bertin → Cleveland & McGill → Munzner lineage is named consistently across Part I and recurs in Part II. The Few > Tufte position is held throughout. Cairo's ethical frame appears at Ch 2, Ch 8 (correlation-is-not-causation), Ch 9 (Nightingale), Ch 12 (ratio-vs-absolute), Ch 14 (full synthesis).

---

## Brutalist framing

The user's explicit request was that the front matter explain that this is the Brutalist system applied to D3. The preface does exactly that:

- Opens by naming Brutalist and its origins in After Effects.
- Names the renderer-agnostic core (designer interrogation, phase model, labor separation, supervisory capacities, two-governing-files).
- Maps the five Brutalist phases to D3 (Phase A audit = data audit; Phase B schema = `CLAUDE.md` + `PROJECT.md`; Phase C generate = Claude Code workflow; Phase D verify = Evergreen/Emery audit; Phase E handoff = publishing).
- Maps the five supervisory capacities (PA, PF, TO, IJ, EI) to chart-design work.
- Names the labor separation (Claude Code: syntax and computation; human: design judgment).
- Establishes the two-governing-files structure for the book's pedagogy.
- Names the renderer-agnostic origin and what makes D3 specifically the right renderer for this book.

Chapter 15 then walks the full Brutalist phase model end-to-end on a real project, completing the framework's instantiation in book form.

---

## What was NOT done (intentionally or due to scope)

1. **Step 3 of the curriculum enrichment generator (running project menu) was not produced.** Chapter 15 effectively serves as the running project; a formal 3-5-option menu was not generated. If a course-context running project is needed later, the instructor can either use Ch 15's UNHCR humanitarian project as-is or substitute domain-specific data.

2. **LLM Exercises are project-agnostic.** Each chapter has an LLM Exercise at the chapter end with `[TBD — selected after Chapter 00]` as a placeholder. If a running project is later locked, these need retuning with project-specific prompt blocks (the same retuning pattern used for the prior three books in the session).

3. **Primary-source verification pass not done.** Every chapter contains specific citations (Bertin, Cleveland & McGill, Tufte, Cairo, Few, Munzner, Stevens, Heer & Bostock, etc.). None has been independently verified. A revision pass should apply `[verify]` flags. Most-citation-dense chapters: Ch 1 and Ch 14.

4. **Build pipeline not tested.** The Kindle/EPUB build (`build.sh`, `metadata.yaml`, styles) exists but has not been run against the new chapter files. Filename ordering follows the convention; should compile cleanly but should be tested.

5. **The Brutalist documentation is not separately included.** The preface refers to Brutalist as a system; if the book is published, the Brutalist documentation should be findable (companion website, separate publication, or open-source repository).

---

## Recommended next steps

1. **Read the Brutalist preface against the source documentation.** Confirm the framing is accurate to the system as the user has it.
2. **Spot-check 2–3 chapters for primary-source verification.** Ch 1 (most citation-dense) and Ch 14 (most synthesis-heavy) are good candidates.
3. **Run `./build.sh` on the chapters** to confirm the EPUB compiles. The chapter file ordering (numeric prefix) should produce the right reading order.
4. **Decide whether to formalize a running project** or rely on Chapter 15's capstone. If formalize, the prior three books' Project Guide structure is the template.
5. **Consider whether Chapter 00's `01a-chapter-00.md` filename** is right for the build pipeline. The "01a" prefix sorts between the introduction (01) and Chapter 1 (02), which is the intended reading order. The `build.sh` should respect this; verify.
6. **Decide on a license for publication.** The book references Humanitarians AI examples (used with permission, per the acknowledgments); the book itself is under Bear Brown, LLC copyright per the front matter.

---

## Files for review

[Front matter](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/00-frontmatter.md)

[Introduction](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/01-introduction.md)

[Chapter 00 — Claude Basics](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/01a-chapter-00.md)

[Chapter 1 — Marks and Channels (rewritten)](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/02-chapter-01.md)

[Chapter 5 — Comparison Charts (rewritten)](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/06-chapter-05.md)

[Chapter 14 — Design Principles in Practice](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/15-chapter-14.md)

[Chapter 15 — Building a Complete Project](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/16-chapter-15.md)

[Back matter](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/chapters/99-back-matter.md)

[Run notes](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/_notes.md)

[Table of contents](computer:///Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/_toc.md)
