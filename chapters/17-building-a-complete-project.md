# Chapter 15 — Building a Complete Project
*From Raw Data to Published Chart in One Pipeline.*

## Three suggested titles

- Building a Complete Project: From Raw Data to Published Output
- The MBTA Process Model Applied End-to-End
- The Final Exam: A Visualization Project from Scratch

---

## Chapter overview

By the end of this chapter you will have built a complete D3 visualization project from raw dataset to published output, walking the entire pipeline this book has taught: data audit (Chapter 3), chart selection (Chapter 2), channel decomposition (Chapter 1), Claude Code workflow (Chapter 4), chart-family-specific design rules (Chapters 5–13), and design audit (Chapter 14). The chapter is structured around the MBTA project model (Barry & Card, 2014): start with the question, prototype on working code, iterate to publishable. The project is the test the book asks you to pass.

---

## Learning objectives

1. **(Create)** Given a raw dataset, produce a complete visualization following the MBTA project process model: define the communication question → prototype multiple forms → select and build with Claude Code → apply the Chapter 14 audit → iterate → publish.
2. **(Evaluate)** Assess the final output against the communication question identified at the start and specify any gap between the chart and the question it was supposed to answer — applying Cairo's "the purpose of the graphic is to answer the question" criterion.

---

## Opening case — the MBTA project's three guiding questions

Mike Barry and Brian Card began their MBTA visualization project with three questions:

1. "When and where are the trains crowded or delayed?"
2. "How do snowstorms affect the system?"
3. "How congested is my route?"

Every design decision in the project traces back to one of these questions. Where the data didn't support a question, they reframed. Where multiple chart types could have answered a question, they prototyped to compare. Where the prototype revealed something the question hadn't anticipated, they updated the question.

This is the model. The project starts with the question, not the data. The data audit (Chapter 3) follows the question, not the other way around. The chart selection (Chapter 2) follows the audit. The build (Chapter 4) follows the selection. Each step builds on the previous. Skipping any one of them produces work that breaks at later steps.

This chapter walks the model end-to-end on a humanitarian data project. The dataset is real (UNHCR forced displacement figures); the questions are reader-focused; the workflow follows everything Part I and Part II of this book have taught. By the end, you will have produced a complete visualization project that you could publish — and you will have a `PROJECT.md` documenting every decision.

---

## Theoretical grounding — the MBTA process model, Cairo's "purpose answers question," the full Brutalist phase model

This chapter applies the entire framework of the book.

**The MBTA process model (Barry & Card, 2014).** From their published reflection: "Mockups and prototypes helped us formulate ideas, but nothing beat iterating on working code." The full process, generalized:

1. Define the communication questions before touching data or charts.
2. Explore the data to find what it actually supports.
3. Prototype multiple forms — "nothing beats iterating on working code."
4. Select the form that answers the reader's question most directly.
5. Build with Claude Code, iterate.
6. Apply the design audit (Chapter 14).
7. Publish with annotations.

**Cairo's "the purpose of the graphic is to answer the question."** The design's success criterion is whether the chart answers the question identified at the start. A chart that is technically clean, perceptually accurate, well-annotated, and visually polished — but which doesn't answer the communication question — is a failed chart. The design audit (Chapter 14) tests for technical and perceptual quality; the project's final evaluation tests for whether the question is answered.

**The full Brutalist phase model.** This chapter is the first chapter that walks all five phases together:

- **Phase A — AUDIT.** Data audit (Chapter 3). What types are present? What relationships does the data support? What is the analyst's question vs. the reader's question?
- **Phase B — SCHEMA.** Define `CLAUDE.md` (the project's coding constitution), `DESIGN.md` (the project's visual constitution — palette, typography, spacing, dark-mode behavior, responsive breakpoints), and `PROJECT.md` (the project state). All three populated before generation. The `CLAUDE.md`/`DESIGN.md` split, introduced in Chapter 00, exists because the LLM instruction budget cannot reliably hold both coding and visual rules in a single file. Sessions that do not involve visual decisions load only `CLAUDE.md`; sessions that do load both.
- **Phase C — GENERATE.** Claude Code produces the visualization. One chart at a time. Each chart's prompt follows the four-move structure (Chapter 4).
- **Phase D — VERIFY.** Run the chart. Apply the Chapter 14 audit. Iterate to publishable.
- **Phase E — HANDOFF.** Publish with annotations, accessibility metadata, source documentation, methodology notes.

The book's preceding 14 chapters were the inputs to this chapter. Chapter 15 is the integration.

---

## Concept 1 — Phase A: defining the questions and reading the data

The project starts with the question, not the data.

### The chosen project: humanitarian forced displacement, 2020–2024

The dataset: UNHCR forced displacement figures by country, 2020–2024. Each row: country of origin, country of asylum (or internal displacement), year, count. The dataset has roughly 5,000 rows.

### Step 1.1 — Frame the questions

Before opening the data, write the communication questions. Three reader-focused questions for a public-policy audience:

1. "Which countries of origin are producing the most refugees? How has this changed across 2020-2024?"
2. "Which countries are receiving the most refugees? Where are people going?"
3. "What proportion of forced displacement is internal (within country) vs. international (across borders)?"

These are the MBTA-style questions: specific, audience-focused, answerable by visualization. Each will produce a chart (or set of charts).

### Step 1.2 — Apply the Chapter 3 data audit

For each question, walk the audit:

- **Data types:** Country of origin (categorical, 100+ countries). Country of asylum (categorical). Year (temporal). Count (quantitative). Type of displacement (categorical: refugee, asylum-seeker, internally displaced).
- **Analyst's question vs. reader's question:** The dataset suggests many analyst questions (where do refugees flow? what countries are stable as origins? what is the temporal trajectory?). The three reader-focused questions above narrow the analyst space.
- **"Compared with what?":** Q1 compares countries to each other across years. Q2 compares destination countries. Q3 compares two categories (internal vs. international).
- **Relationships supported:** comparison (countries on a quantitative scale), change over time (year axis), part-to-whole (international vs. internal), spatial (origin and destination geography), flow (origin → destination).

Each question maps to a different chart family.

### Step 1.3 — Identify gaps

The data does not directly answer "which routes are most used by refugees?" — origin-destination pair counts are present, but the chart family (flow map, Chapter 12) requires geographic projection. The dataset doesn't contain geographic coordinates; we'd need to join with a country-coordinates lookup. The honest move: acknowledge the gap and proceed with the three questions above.

This is the Phase A output. It defines the project scope.

---

## Concept 2 — Phase B: schema (`CLAUDE.md`, `DESIGN.md`, and `PROJECT.md`)

Before generating any charts, build the project's three schema files: `CLAUDE.md` (coding constitution, loads every session), `DESIGN.md` (visual constitution, loads when visual decisions are in scope), and `PROJECT.md` (project state, the per-project audit document). Chapter 00 explains why `CLAUDE.md` and `DESIGN.md` are separate files — the LLM instruction budget cannot reliably hold both coding and visual rules in a single document. This chapter applies that separation to a real project.

### `CLAUDE.md` — the project's coding constitution

`CLAUDE.md` loads at the start of every Claude Code session in this project. It contains coding rules — D3 version, file structure, encoding requirements, accessibility implementation, the chart-family-specific rules that govern *how the code gets written*. Visual rules (palette, typography, responsive behavior) live in `DESIGN.md` and load only when the session involves visual decisions.

```markdown
# CLAUDE.md — Forced Displacement Visualization Project

## D3 version
- D3 v7. No mixing with v6 or earlier.
- CDN: https://cdn.jsdelivr.net/npm/d3@7

## File structure
- One self-contained HTML file per chart.
- Inline CSS (component scoped).
- Inline D3 (script tag).
- One companion JSON file per chart at `{slug}/data.json`.

## Required encoding rules
- Bar charts: zero baseline non-negotiable.
- Bubble charts: d3.scaleSqrt for radius (area-not-radius — Stevens' law).
- Choropleths: d3.geoEqualEarth or d3.geoAlbersUsa (equal-area projection).
- Sankey diagrams: d3.sankey() with sankeyJustify alignment.

## Naming conventions
- SVG IDs: chart-{type}-{n} pattern.
- CSS classes: BEM-light (.chart, .chart__bar, .chart__bar--highlighted).

## Accessibility
- Every SVG: role="img", aria-label.
- Every encoded element: <title> child for screen-reader.
- Keyboard focus on interactive elements.
- Color-blind safety: verify with simulator before publishing.

## Four-move prompt template
Every chart prompt follows show / say / constrain / verify (Chapter 00).

## Forbidden without explicit instruction
- Do not modify existing charts in this project.
- Do not substitute one chart type for another (e.g., bar → pie).
- Do not invent encoding decisions; specify them in the prompt.
```

### `DESIGN.md` — the project's visual constitution

`DESIGN.md` loads when a session involves visual decisions. It contains palette, typography, spacing, dark-mode behavior, and responsive breakpoints — the rules that govern *how the result looks*. Sessions about scales, joins, transitions, axis ticks do not load this file; loading it on every session would consume ~50 instruction slots on rules that don't apply.

```markdown
# DESIGN.md — Forced Displacement Visualization Project

## Color palette
- Primary: #8B0000 (dark red, accent for emphasis)
- Secondary: #6B6B5E (mid gray, default)
- Light: #9B957F (pale tan, low values)
- Background light: #FFFFFF
- Background dark: #0D0D0D

## Sequential color scale
- d3.scaleSequential with d3.interpolateRgb from "#9B957F" to "#8B0000"

## Categorical color scale
- d3.scaleOrdinal with #8B0000, #5C3317, #6B6B5E, #4A4A4A, #9B957F

## Typography
- Family: 'Inter', -apple-system, sans-serif
- Title: 16px regular
- Subtitle: 12px regular, fill #9B957F
- Axis labels: 11px regular
- Annotations: 11px regular

## Spacing scale (8px base)
- 0, 4, 8, 16, 24, 32, 48, 64, 96
- Default chart margins: top 60, right 40, bottom 60, left 60

## Dark mode
- prefers-color-scheme media query.
- Light/dark palette pair maintained for every chart.
- Walnut accents stay visible in both modes; cream becomes near-black.

## Responsive
- Window resize triggers redraw.
- Mobile breakpoint at 600px (consider mobile-specific layout).
- Below 400px: drop legend, increase tooltip use.

## Component rules
- Cards: 1px border, no shadow, 0 corner radius.
- Axis: tick density adapts to viewport width.
- Annotations: leader lines walnut at 0.75 stroke-width.
```

### `PROJECT.md` — the project state

```markdown
# PROJECT.md — Forced Displacement Visualization Project

## Designer layer

### Communication questions

1. Which countries of origin are producing the most refugees? How has
   this changed across 2020-2024?
2. Which countries are receiving the most refugees?
3. What proportion of forced displacement is internal vs. international?

### Audience

Public-policy readers (think tank, government, journalism). High but
not specialized graphicacy. Decisions about where to focus aid efforts
or where to advocate for refugee protection.

### Tone

Informational, with explicit acknowledgment of uncertainty in some
counts. Not advocacy.

### Constraints

- No specific chart type can be assumed. Choose based on what answers
  each question.
- Each chart should stand alone (the project may publish each
  separately).
- Sequence the charts to build context: country origin → destination
  → composition.

## Technical layer

### Dataset

UNHCR forced displacement figures, 2020-2024. Source: UNHCR Global
Trends report. ~5,000 rows. Columns: country_of_origin, country_of_asylum,
year, type (refugee/asylum-seeker/internally-displaced), count.

### Generation log

[Updated as charts are built.]
```

The `PROJECT.md` is now ready for Phase C.

---

## Concept 3 — Phase C: generating the charts

Walk through generating each of the three charts.

### Chart 1: Top countries of origin, change over time

**Question:** Which countries of origin are producing the most refugees? How has this changed across 2020-2024?

**Selection:** Comparison + change over time. Two natural forms:
- *Bar chart with trend lines* (sparkline-style) per country.
- *Multi-series line chart* with the top 10 countries as lines.
- *Heatmap* with countries on y-axis, years on x-axis, color encoding count.

The reader-focused choice: the question implies ranking *and* trajectory. A bar chart of cumulative 2020-2024 totals shows ranking; line chart shows trajectory; heatmap shows both. Build the heatmap first.

**Channel decomposition:**
- Marks: rectangles (cells in a heatmap grid).
- y-position: country (categorical, sorted by 2024 count descending).
- x-position: year (temporal, 2020-2024).
- Color luminance: count (sequential pale-to-dark).

**Claude Code prompt:**

```
**Show what I have:**
Refugee counts by country of origin, 2020-2024. Top 15 countries by
2024 totals. Sample: [paste 15 rows × 5 years].

**Say what I want:**
Heatmap in D3 v7. Single self-contained HTML file. Responsive.

**Constrain it:**
- Marks: rectangles (cells).
- y-position: country (sorted by 2024 count descending).
- x-position: year (2020 to 2024).
- Color luminance: count, d3.scaleSequential with d3.interpolateRgb
  from "#9B957F" to "#8B0000".
- Cell labels: count (in millions if appropriate; in thousands
  otherwise).
- y-axis labels: country names, no rotation.
- x-axis: years labeled at top.
- Subtitle: "Refugee Counts by Country of Origin, 2020-2024 (millions)".
- Legend: color scale at bottom-right.
- Margins: top 60, right 80, bottom 40, left 200.
- Dark mode support per CLAUDE.md.

**Verify:**
Restate channel decomposition.
```

Iterate per Chapter 4.

### Chart 2: Top destination countries

**Question:** Which countries are receiving the most refugees?

**Selection:** Comparison. The reader needs ranking. Bar chart with horizontal orientation (long country names).

**Channel decomposition:**
- Marks: rectangles, one per destination country.
- y-position: country (sorted by 2024 totals descending).
- x-position from zero baseline: refugee count (quantitative).
- Color luminance: redundant encoding of count.

The Claude Code prompt follows Chapter 5's pattern. Generate, audit, iterate.

### Chart 3: Internal vs. international displacement, 2024

**Question:** What proportion is internal vs. international?

**Selection:** Part-to-whole. Two categories. Stacked bar (single bar) is the cleanest form for two-category proportions.

**Channel decomposition:**
- Marks: two rectangles in a single bar.
- x-position: type (internal vs. international).
- Length-of-segment: count.
- Color hue: type identity.

Claude Code prompt follows Chapter 9's pattern.

---

## Concept 4 — Phase D: applying the Chapter 14 audit

Each chart goes through the 22-point checklist. Failures get follow-up prompts; iterations land at publishable.

For chart 1 (heatmap), common audit failures:
- Cell labels too small at the deployment size. Fix: increase font, or add only on hover.
- Color luminance scale doesn't match the dataset's range. Fix: explicit color domain.
- y-axis country labels overlap. Fix: increase left margin, or filter to top 10 instead of top 15.

For chart 2 (bar chart), common failures match Chapter 5's: zero baseline, sort order, label rotation. Verify each.

For chart 3 (stacked bar), verify the two segments add to the total and the colors match the project palette.

Document the iterations in `PROJECT.md`'s Generation Log.

---

## Concept 5 — Phase E: handoff

The project is publishable when the audit passes. The handoff includes:

### Per chart

- Final HTML file with inline CSS and D3.
- Annotation: source ("Source: UNHCR Global Trends 2024").
- Annotation: methodology note ("Counts are point-in-time totals as of December 31 of each year; some counts include estimates").
- Annotation: data quality note ("Data quality varies by country; some figures are estimates").
- Accessibility metadata (ARIA, screen-reader summaries).

### Project-level

- The `PROJECT.md` documenting every decision.
- The `CLAUDE.md` for any future iteration.
- A README explaining how to re-run the prompts (and what data is required).
- License notes (UNHCR data is publicly available; cite per their terms).

### The publication

The three charts can be published as:
- A single article with all three charts embedded.
- A dashboard where a user navigates between them.
- A series of social-media-friendly individual charts.

The choice depends on the publication context. The charts themselves are independent; the project is the integrated set.

---

## Mid-chapter checkpoint

Pick a real dataset of your own. Frame three reader-focused questions. Walk through Phase A (data audit) for each. The questions should be specific enough that, once answered, the audience would have something useful.

You should be able to do this in 15 minutes.

---

## Extended worked example — the project as `PROJECT.md` evolves

Show what the final `PROJECT.md` looks like at the end of the project.

```markdown
# PROJECT.md — Forced Displacement Visualization Project

## Designer layer (final)

### Communication questions
[Same as initial spec.]

### Audience
[Same as initial spec.]

## Technical layer (updated)

### Generation log

#### Chart 1 — Heatmap of countries of origin
- Initial prompt: 2024-XX-XX (paste prompt).
- First output: chart-01-heatmap-v1.html. Audit failures:
  - Cell labels too small.
  - Color domain didn't match data range.
- Iteration 1 (2024-XX-XX): increased font; specified color domain
  [0, 8000000].
- Final: chart-01-heatmap-v2.html. All 22 audit items pass.

#### Chart 2 — Bar chart of destination countries
- Initial prompt: 2024-XX-XX.
- First output: chart-02-bar-v1.html. Audit failures:
  - Sort order alphabetical, not by value.
  - Color was monotone gray (no luminance encoding).
- Iteration 1 (2024-XX-XX): specified sort order; specified color
  luminance encoding.
- Final: chart-02-bar-v2.html. All 22 audit items pass.

#### Chart 3 — Stacked bar of internal vs. international
- Initial prompt: 2024-XX-XX.
- First output: chart-03-stack-v1.html. Audit passed on first attempt.

### Files in repository

- charts/chart-01-heatmap.html
- charts/chart-02-bar.html
- charts/chart-03-stack.html
- data/unhcr-2020-2024.csv
- README.md
- PROJECT.md (this file)
- CLAUDE.md
```

This is what a finished `PROJECT.md` looks like. Every decision documented, every iteration logged, every file findable.

---

## Chapter summary

You can now do five things you could not do before this chapter.

You can produce a complete visualization project end to end, walking the entire pipeline this book has taught: data audit → chart selection → channel decomposition → Claude Code workflow → chart-family-specific design rules → design audit → publication.

You can apply the MBTA project process model to your own work: start with the question, prototype on working code, iterate to publishable, document every decision in `PROJECT.md`.

You can build the project's `CLAUDE.md` (coding constitution) and `PROJECT.md` (state) and use them as the persistent context that travels with the project.

You can apply Cairo's success criterion at every stage: does this chart answer the communication question? If not, iterate. The chart's purpose is to answer the question; everything else is decoration.

You have completed the book. The next thing to do is build a real project of your own.

---

## Key terms

- **The MBTA process model.** Question → data audit → prototype → select → build → audit → publish. The full pipeline.
- **`CLAUDE.md`.** The project's coding constitution. D3 version, palette, accessibility, naming conventions.
- **`PROJECT.md`.** The project state. Designer layer (intent) + technical layer (state, log).
- **Phase A — AUDIT.** Data and question audit. Before generating anything.
- **Phase B — SCHEMA.** `CLAUDE.md` + `PROJECT.md` populated.
- **Phase C — GENERATE.** Claude Code produces charts.
- **Phase D — VERIFY.** Charter audit per Chapter 14.
- **Phase E — HANDOFF.** Publication with annotations and metadata.

---

## Discussion questions

1. The MBTA project's reflection lesson — "nothing beat iterating on working code" — predates Claude Code. Why does it apply more strongly now?
2. The book's argument is that the design layer is the hard layer and that Claude Code has dissolved the implementation barrier. Do the three charts you would have built before reading this book differ from the three you would build now?
3. Cairo's "purpose is to answer the question" criterion is the project's success criterion. What would it look like to fail this criterion while passing the Chapter 14 audit? When does a chart pass technical audit and still fail the question?
4. The Brutalist phase model (A through E) gives a process. Where in your professional workflow do you currently skip phases? What is the cost?
5. *Closing the book.* The book's thesis: D3 visualization has been two problems; Claude Code solved one; the design problem remains and is teachable. After working through the book, where does the thesis land for you?

---

## Exercises

### Warm-up

**Exercise 15.1** — *Frame three questions.* Take a dataset you work with. Frame three reader-focused communication questions following the MBTA model.

**Exercise 15.2** — *Build a CLAUDE.md.* Draft a `CLAUDE.md` for your domain. Include D3 version, palette, accessibility standards, naming conventions.

**Exercise 15.3** — *Phase A audit.* Apply the data audit (Chapter 3) to a project you're considering. Identify gaps.

### Application

**Exercise 15.4** — *Walk the full pipeline.* Take a real dataset. Walk all five Brutalist phases. Build the project. Document in `PROJECT.md`.

**Exercise 15.5** — *Iteration log.* For one chart in your project, keep a complete iteration log. Note each follow-up prompt and the failure it targeted.

**Exercise 15.6** — *Audit your project.* Apply the 22-point Chapter 14 audit to every chart in your project.

### Synthesis

**Exercise 15.7** — *Publication preparation.* Take a project you've built. Write the publication-ready annotations (source, methodology, data quality notes, accessibility metadata). Test on a screen reader.

**Exercise 15.8** — *Project handoff to a colleague.* Hand your project to a colleague. Watch them try to re-run the prompts and rebuild the charts. Identify what's missing in the handoff documentation.

### Challenge

**Exercise 15.9** — *Multi-chart project.* Build a project with 5+ related charts. Apply consistent visual language (same palette, same typography, same chart-family conventions). Document the visual language in `CLAUDE.md`.

**Exercise 15.10** — *Replicate the MBTA project.* Following Barry & Card's structure, build a small replication of one of the MBTA visualizations (or an analogous transit/transportation system in your area). Walk the full process.

---

## LLM Exercise — Chapter 15: The Final Project

```
I am working on the final project for Brutalist d3 x Claude.
The dataset is [DESCRIBE]. The audience is [DESCRIBE].

Walk me through the full Brutalist process:

1. Frame three reader-focused communication questions.
2. Apply the data audit (data types, analyst-vs-reader, "compared with
   what?", relationships supported).
3. For each question, recommend a chart type and channel decomposition.
4. Help me draft the project's CLAUDE.md (D3 version, palette,
   accessibility, conventions).
5. For each chart, write a four-move Claude Code prompt.
6. After each chart is built, walk me through the 22-point audit.
7. Document the project in PROJECT.md.

The output of this exercise is a complete project: three charts, a
CLAUDE.md, a PROJECT.md, and a publication-ready artifact.
```

**This is the final exercise of the book.** Doing it is the test the book asks you to pass.

---

## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter walks the full Brutalist pipeline end-to-end on the UNHCR humanitarian dataset; the focal figures are the deliverables of each phase.

For chart-type references the chapter mentions in passing, see Part II directly: [Heatmap](39-heatmap.md), [Bar Chart](20-bar-chart.md), [Stacked Bar](67-stacked-bar.md), [Sankey Diagram](62-sankey-diagram.md), [Line Graph](43-line-graph.md), [Choropleth](29-choropleth.md), [Bubble Chart](24-bubble-chart.md), [Flow Map](37-flow-map.md). Each Part II chapter has its own prompt.

### Figure 15.1 — Phase A: data audit visualization

The chapter's Phase A deliverable. A summary visualization of the dataset structure: which attributes are categorical, ordered, quantitative, temporal, spatial; which combinations support which chart types. The figure is the channel-decomposition audit document made visible.

```
Generate a dataset-structure audit visualization in D3 v7. Two files:

1. `chapter-15-fig-01.html` — full HTML with inline CSS and inline D3 v7. A multi-panel layout showing the dataset structure: a small data table preview, a column-type-classification chart, and a chart-type-feasibility matrix. Page subtitle: "Phase A deliverable — what the data has, what it supports."

2. `chapter-15-fig-01/data.json` — the dataset metadata.

Data shape:
- `columns`: array of `{name, type (categorical|ordered|quantitative|temporal|spatial), n_unique, sample_values}`.
- `rows_count`: total row count.
- `chart_feasibility`: matrix of column-pair-to-chart-type viability.

{DATA NEEDED} — The UNHCR refugee statistics dataset (https://www.unhcr.org/refugee-statistics/) or any structured humanitarian dataset with multiple column types. The audit visualization is structural; the specific dataset choice can be adjusted.

Panel 1 — column-type bar chart: counts of categorical / ordered / quantitative / temporal / spatial columns.
Panel 2 — chart-type-feasibility matrix: rows = column pairs, columns = chart types, cell color = viable (walnut), marginal (light gray), infeasible (white). The reader sees which charts the dataset can support.
Panel 3 — small preview table: 5 rows × all columns, with type-color borders.

Caption beneath: "The Phase A deliverable is not a pretty chart — it is a documented audit. The reader of this document is the future self designing the chart."

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 15.2 — Phase B: schema document rendered as a chart

The chapter's Phase B deliverable. The `PROJECT.md` schema document for the worked-example chart, rendered as a structured visualization: chart type, data structure, channel decomposition, design constraints, color palette, sort order, accessibility decisions. The figure makes the schema concrete.

```
Generate a schema-document visualization in D3 v7. Two files:

1. `chapter-15-fig-02.html` — full HTML with inline CSS and inline D3 v7. A structured layout rendering the PROJECT.md content as labeled panels. Page subtitle: "Phase B deliverable — the schema as the chart's blueprint."

2. `chapter-15-fig-02/data.json` — the schema content.

Data shape:
- `chart_type`: string.
- `data_structure`: object describing rows/columns.
- `channels`: array of `{channel_name, attribute, type, justification}`.
- `design_constraints`: array of strings.
- `color_palette`: array of hex codes with usage notes.
- `accessibility`: array of strings.

{DATA NEEDED} — The PROJECT.md content for whichever chart is being built in the chapter's worked example. If the chapter uses a heatmap of refugee count by origin × destination, the schema is built for that.

Render each schema element as a labeled panel:
- "Chart type" — large label, brief description.
- "Data structure" — table of columns with their types.
- "Channels" — list of channel-attribute mappings with justifications.
- "Design constraints" — bulleted list.
- "Color palette" — swatches with usage labels.
- "Accessibility" — bulleted list.

The figure should look like a one-page reference document, not a decorative chart.

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 15.3 — Phase C: the final chart deliverable

The chapter's Phase C deliverable — the actual chart the project produces. A heatmap (or whichever chart the worked-example schema specifies) of UNHCR refugee data, rendered to publication standard with all design decisions from Phases A and B applied. The figure is the project's output.

See [Heatmap](39-heatmap.md) in Part II for the canonical reference.

```
Generate the final project chart in D3 v7 — a heatmap of refugee origin-destination counts. Two files:

1. `chapter-15-fig-03.html` — full HTML with inline CSS and inline D3 v7. A heatmap with origin countries on one axis, destination countries on the other, color luminance encoding count. Responsive on resize. Page subtitle: "Phase C deliverable — the chart Phases A and B specified."

2. `chapter-15-fig-03/data.json` — the dataset.

Data shape:
- `origin_destinations`: array of `{origin, destination, count}` for the top-N origin-destination pairs.

{DATA NEEDED} — UNHCR refugee statistics, country-of-origin × country-of-asylum top pairs by count. https://www.unhcr.org/refugee-statistics/.

Encoding:
- Rows: origin countries, sorted by total outflow.
- Columns: destination countries, sorted by total inflow.
- Cell color luminance: count (sequential walnut palette).
- Direct value labels in cells where count exceeds a readability threshold; tooltip otherwise.
- Subtitle: "Top refugee origin–destination pairs, [year]. Color encodes count."

Apply all design decisions from the chapter's worked-example schema: zero baseline (cell color from light-cream-zero to dark-walnut-max), categorical sort by row/column total, accessible color contrast, direct labels where space permits, alt text for screen readers.

Style: warm monochrome — black, dark walnut, blood-red. Editorial register.

Provide both files as separate code blocks.
```

### Figure 15.4 — Phase D: the audit checklist applied

The chapter's Phase D deliverable. The Evergreen/Emery 22-point checklist applied to the project's chart, with each item marked pass/fail/partial. The figure makes the verification phase concrete.

```
Generate a checklist-audit visualization in D3 v7. Two files:

1. `chapter-15-fig-04.html` — full HTML with inline CSS and inline D3 v7. A 22-row checklist with status indicators for each item. Page subtitle: "Phase D deliverable — the 22-point Evergreen/Emery audit applied."

2. `chapter-15-fig-04/data.json` — the audit results.

Data shape:
- `audit`: array of 22 entries, each `{item_number, item_text, status (pass|fail|partial), notes}`.

{DATA NEEDED} — The Evergreen/Emery checklist itself (published in Stephanie Evergreen's *Effective Data Visualization*; many free summaries online). For the per-item status, the audit is performed by the reader against the chart from Figure 15.3.

Render as a structured checklist:
- Each row: item number, item text, status indicator (filled circle for pass, half-filled for partial, empty for fail), brief notes.
- Group items by category (Text, Arrangement, Color, Lines, Overall).
- Summary at top: "X of 22 pass, Y partial, Z fail."

Style: warm monochrome. The status indicators are the only graphical elements; everything else is text.

Provide both files as separate code blocks.
```

### Figure 15.5 — Phase E: the published artifact

The chapter's Phase E deliverable. The chart from Figure 15.3, packaged for publication: with caption, source citation, methodology note, accessibility statement, and link to the underlying data. The figure makes the handoff concrete.

```
Generate the publication-packaged chart in D3 v7. Two files:

1. `chapter-15-fig-05.html` — full HTML with inline CSS and inline D3 v7. The chart from Figure 15.3 wrapped in a publication container with caption, source, methodology, and accessibility statement. Page subtitle: "Phase E deliverable — the chart, packaged for the reader who is not in the room."

2. `chapter-15-fig-05/data.json` — same data as Figure 15.3.

Layout:
- The chart from Figure 15.3, full width.
- Title above: "Top refugee origin–destination pairs, [year]."
- Subtitle below title: a one-sentence claim the chart makes.
- Caption below the chart: 2–3 sentences explaining what the reader should take away.
- Source line: "Data: UNHCR Refugee Statistics, [date]. URL: https://www.unhcr.org/refugee-statistics/"
- Methodology line: "Methodology: Top-N pairs by absolute count. Sort: row and column totals descending. Color: sequential luminance, cream-to-walnut, 5 quantile bins."
- Accessibility statement: "Alt text and SVG `<title>`/`<desc>` provided. Color contrast meets WCAG AA. Tooltip values readable by screen reader."

Style: warm monochrome. Editorial register, suitable for publication on a humanitarian-organization website or in a print report.

Provide both files as separate code blocks.
```

---

## Further reading

- **Barry, Mike, and Brian Card. (2014).** "Visualizing MBTA Data." Read the full project report.
- **Cairo, Alberto. (2016).** *The Truthful Art* and (2019) *How Charts Lie*. The ethical frame from start to finish.
- **The Brutalist system documentation** (forthcoming or in your own configuration). The architecture this book inherits.
- **The book's pantry** — the full reference set you have used throughout.

---

## Tags

complete-project, MBTA-process-model, Brutalist-phase-model, CLAUDE.md, PROJECT.md, audit, publication, handoff, Cairo-purpose-answers-question, end-to-end-pipeline, D3, Claude-Code
