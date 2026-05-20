# Brutalist d3 x Claude

**Author:** Nik Bear Brown
**Publisher:** Bear Brown, LLC
**Status:** Draft (17 chapter files in place; final pass pending)
**Started:** 2026-05-07
**Series:** Brutalist — [brutalist.art](https://www.brutalist.art/)
**Sister volumes:** *Brutalist After Effects x Claude*, *Brutalist Blender x Claude*, *Brutalist Remotion x Claude* (additional renderer modules in development)

---

## What this book is

A textbook that teaches data visualization through D3 by treating the design layer — not the syntax — as the hard layer worth a student's time. Claude Code generates conformant D3 v7 faster than any developer can write it. The implementation barrier is dissolved. What remains is the work that was always harder and is now decisive: reading a dataset, choosing a chart that serves the question, justifying every channel, and refusing the forms that distort the data the reader will eventually trust.

The book teaches that work. It uses the Humanitarians AI pantry — sixty-plus working visualizations covering the full chart taxonomy — as its laboratory. Each chapter pairs the conceptual framework with a working example the student can inspect, modify, and rebuild. Claude Code writes the D3. The student directs it.

The byline is Nik Bear Brown. The audience is graduate students, data journalists, researchers, and analysts who work with data, need to communicate it visually, and have bounced off the D3 API before. After this book they will not be JavaScript developers. They will be people who can specify a chart precisely enough that Claude Code produces a publishable one, and who can read their own data well enough to know when the chart they specified is wrong.

---

## The Brutalist commitment

This book is one application of a renderer-agnostic system for AI-assisted production. Other volumes in the series apply the same framework to After Effects, Blender, Remotion, and beyond. The framework's name is **Brutalist**. Its guiding principle is one sentence:

> **Maximally informed and minimally autonomous by design.**

The framework was built to solve a specific problem. AI code generation is fast and capable. It also runs ahead of human intent, loses track of what it has done, crosses boundaries it should not cross, and acts on new information without asking first. Brutalist is the counter-architecture. The same six principles govern every book in the series; this book teaches them in the D3 layer.

### 1. Intent Layer

Before any code is written, the human specifies — in plain language, never in technical language — what the chart should do, what the reader should understand, what is at stake. Populated by the human. Never overwritten by the AI.

### 2. Schema Layer

A separate technical document defines conventions for the active stack — for this book, that means D3 v7: naming standards, scale vocabulary, color rules, axis conventions, accessibility requirements, the explicit list of what Claude must not improvise. The AI generates against the schema. It does not invent outside it.

### 3. Phase Gate

Generation cannot begin until both the intent layer and the schema layer are populated. The phases run in order:

- **Audit** — map what exists before touching anything
- **Schema** — build the governing documents; populate both layers
- **Generate** — produce output against the schema, one chart at a time
- **Verify** — human reviews every chart before the next is built
- **Handoff** — lock the output, document all manual work, prepare the package

No phase is skipped. No phase is abbreviated under deadline pressure.

### 4. Labor Separation

The boundary between what the AI does and what the human does is explicit and defended. Claude generates D3 code. The human runs it, watches it, and decides whether it is accepted. Claude surfaces information. The human decides what to do with it. Creative judgment, chart selection, and the call on whether a chart actually answers the question — these live permanently in the human layer. The system will not accept them being delegated down.

### 5. Refusal Behavior

Brutalist says **no**. When the human asks Claude to make a judgment call that belongs in the human layer — pick the chart type, choose the palette, decide whether to log-scale — the system declines and explains why. It does not flag and proceed. It stops. That is what gives the labor separation teeth: it is not a guideline a hurried user can override.

### 6. Current Knowledge, Deferred Action

The system reads current documentation, deprecation notices, and breaking changes. When it finds something relevant, it does not act. It surfaces what it found, explains why it matters, and asks permission. New information is a trigger to *inform*, not to *execute*. This posture — *mother may I?* — applies to every external input, including updates Claude is confident are correct.

---

## What this book is not

- **Not a JavaScript tutorial.** The student is not expected to leave fluent in D3 syntax.
- **Not a button-clicking assistant.** Mechanics of UI are not narrated.
- **Not a celebration of AI capability.** Claude is the syntax-generator the reader directs. The reader does the work that matters.
- **Not autonomous.** Nothing in the workflow described here lets the AI ship a chart without the human deciding it ships.
- **Not a substitute for graphicacy.** The book teaches the skill. It does not pretend the tool replaces it.

---

## Governing files for this stack

### `CLAUDE.md` — The Coding Constitution

One per stack. For this book the stack is **D3 v7 + Claude Code + a single-file HTML/SVG output**. The constitution accumulates across the book, chapter by chapter, into a working document. It contains:

- D3 v7 conventions (scales, axes, joins, transitions, layouts) with examples drawn from production references
- Naming standards for marks, channels, datasets, and the project's pantry slots
- The explicit list of what Claude must not touch without instruction
- Code patterns extracted from the working examples in `pantry/`
- The verification stack the reader runs on every generated chart

### `DESIGN.md` — The Visual Constitution

Loaded on-demand rather than every session. Contains:

- The mark-and-channel ranking with the perceptual mechanism that justifies it
- Color rules by channel type (categorical, sequential, diverging) and accessibility constraints
- Annotation strategy and the proportional-ink commitment
- Failure modes for each chart family and the design rule that prevents each one
- The 22-point design audit checklist applied at handoff

### `PROJECT.md` — The Project State

One per project the reader builds. Populated in two layers, both required before any chart is generated:

**Designer / intent layer** — populated by the reader through guided interrogation

- What this chart, dashboard, or report should mean
- What the reader of the final artifact should understand
- The communication question being answered, and the question being refused
- Where dynamic data or media inserts go and why
- Open creative questions

**Technical layer** — populated by audit of the project's current state

- Current chart inventory: built, pending, locked
- Generation log: what was run, accepted, rejected, and why
- Open technical questions

A `PROJECT.md` with only one layer is incomplete. Phase Gate holds the line.

---

## What's in the book

Three parts. Sixteen teachable chapters plus an introduction. Files are numbered on disk; the book's internal chapter numbering starts at zero for the Claude Basics setup chapter and at one for the Decision Layer.

### Part I — The Decision Layer

Builds the conceptual vocabulary. The student leaves Part I able to read a dataset, name the question, pick the chart family, and write a Claude Code prompt that produces a usable D3 chart on the first attempt.

| File | Internal | Title |
|------|----------|-------|
| `01-introduction.md` | — | Introduction — graphicacy, the Chibok case, the brutalist posture |
| `02-claude-basics-for-d3-visualization.md` | Ch. 0 | Claude Basics for D3 Visualization |
| `03-marks-and-channels.md` | Ch. 1 | Marks and Channels |
| `04-chart-selection-as-design-decision.md` | Ch. 2 | Chart Selection as a Design Decision |
| `05-reading-a-dataset.md` | Ch. 3 | Reading a Dataset |
| `06-working-with-claude-code.md` | Ch. 4 | Working with Claude Code |

### Part II — The Chart Taxonomy

A structured tour of every major chart family. Each chapter walks the working examples in `pantry/`, names the design rules grounded in their perceptual mechanism, identifies the failure modes, and produces a Claude Code prompt template the reader adapts. The student leaves Part II with literacy across all sixty-plus chart forms — knowing what each is for and when it fails.

| File | Internal | Title |
|------|----------|-------|
| `07-comparison-charts.md` | Ch. 5 | Comparison Charts (Bars and Columns) |
| `08-time-series-and-temporal-charts.md` | Ch. 6 | Time Series and Temporal Charts |
| `09-distribution-charts.md` | Ch. 7 | Distribution Charts |
| `10-relationship-and-correlation-charts.md` | Ch. 8 | Relationship and Correlation Charts |
| `11-part-to-whole-charts.md` | Ch. 9 | Part-to-Whole Charts |
| `12-hierarchy-charts.md` | Ch. 10 | Hierarchy Charts |
| `13-flow-and-network-charts.md` | Ch. 11 | Flow and Network Charts |
| `14-spatial-and-geographic-charts.md` | Ch. 12 | Spatial and Geographic Charts |
| `15-specialized-and-financial-charts.md` | Ch. 13 | Specialized and Financial Charts |

### Part III — Integration and Production

Synthesizes. Chapter 14 is the design-audit framework — Tufte, Few, and Cairo applied through the Evergreen-Emery checklist, with the chartjunk debate resolved by Few's clarity criterion. Chapter 15 walks a complete visualization project from raw data to published output, following the MBTA process model and the Brutalist phase gate.

| File | Internal | Title |
|------|----------|-------|
| `16-design-principles-in-practice.md` | Ch. 14 | Design Principles in Practice |
| `17-building-a-complete-project.md` | Ch. 15 | Building a Complete Project |

The reader leaves Chapter 15 holding three durable artifacts: a `CLAUDE.md` and `DESIGN.md` accumulated across the book, plus a `PROJECT.md` portfolio that demonstrates the practice on real data.

---

## Repository structure

```
brutalist-d3-x-claude/
├── README.md               ← this file
├── book.md                 ← pitch, argument, audience, voice notes (planning)
├── outline.md              ← chapter-level TOC (planning)
├── vision.md               ← Tic TOC Phase 1
├── architecture.md         ← Tic TOC Phase 2
├── chapters-spec.md        ← Tic TOC Phase 3
├── risks.md                ← Tic TOC Phase 4
├── style/                  ← per-book voice anchor (brutalist posture)
│   ├── brutalist-voice.md
│   └── brutalist-manifesto-source.md
├── pantry/                 ← working visualizations: 60+ chart examples + data
│   └── visualization/      ← one folder per chart type (HTML + data.json)
├── chapters/
│   ├── 00-frontmatter.md   ← copyright, dedication, preface
│   ├── 01-introduction.md
│   ├── 02-claude-basics-for-d3-visualization.md
│   ├── 03-marks-and-channels.md
│   ├── 04-chart-selection-as-design-decision.md
│   ├── 05-reading-a-dataset.md
│   ├── 06-working-with-claude-code.md
│   ├── 07-comparison-charts.md
│   ├── 08-time-series-and-temporal-charts.md
│   ├── 09-distribution-charts.md
│   ├── 10-relationship-and-correlation-charts.md
│   ├── 11-part-to-whole-charts.md
│   ├── 12-hierarchy-charts.md
│   ├── 13-flow-and-network-charts.md
│   ├── 14-spatial-and-geographic-charts.md
│   ├── 15-specialized-and-financial-charts.md
│   ├── 16-design-principles-in-practice.md
│   ├── 17-building-a-complete-project.md
│   └── 99-back-matter.md
├── styles/
│   ├── kindle.css          ← shared base; do not edit per book
│   └── kindle-book.css     ← book-specific overrides
├── output/                 ← built artifacts (gitignored)
├── build.sh                ← EPUB build pipeline
└── graphs.sh               ← figure-processing pass
```

---

## Planning documents

| File | Purpose |
|------|---------|
| `book.md` | One-sentence pitch, the argument, the gap, the reader, high-level outline, voice anchor reference. |
| `outline.md` | Chapter-level TOC — kept in sync with `chapters/`. |
| `vision.md` | Tic TOC Phase 1 — book concept, learner profile, thesis, field positioning. |
| `architecture.md` | Tic TOC Phase 2 — learning outcomes, sequencing, three-act arc, prerequisites. |
| `chapters-spec.md` | Tic TOC Phase 3 — per-chapter specs, cases, contested claims, coverage gaps. |
| `risks.md` | Tic TOC Phase 4 — comparable texts, features, out of scope, adoption risks. |
| `style/brutalist-voice.md` | Per-book voice anchor. Overrides root `style/` on conflict. |
| `style/brutalist-manifesto-source.md` | Verbatim Brutalist project description. Source of truth for voice. |
| `pantry/` | Working visualization examples — one per chart family, with paired data. The laboratory the book runs on. |

Planning files are not compiled into the EPUB.

The four Tic TOC files are templated with `[NEEDS HUMAN INPUT]` markers and a `*Phase N output from Tic TOC*` header signature. Run Tic TOC's `/scaffold silent` to fill them from `book.md`, `outline.md`, `pantry/`, and `chapters/`. Or build them section-by-section through the interactive phase commands (`/i1` → `/m4`).

---

## Chapter status

| File | Title | Status |
|------|-------|--------|
| `00-frontmatter.md` | Front Matter | ☐ |
| `01-introduction.md` | Introduction | ☑ drafted |
| `02-claude-basics-for-d3-visualization.md` | Chapter 0 — Claude Basics | ☑ drafted |
| `03-marks-and-channels.md` | Chapter 1 — Marks and Channels | ☑ drafted |
| `04-chart-selection-as-design-decision.md` | Chapter 2 — Chart Selection | ☑ drafted |
| `05-reading-a-dataset.md` | Chapter 3 — Reading a Dataset | ☑ drafted |
| `06-working-with-claude-code.md` | Chapter 4 — Working with Claude Code | ☑ drafted |
| `07-comparison-charts.md` | Chapter 5 — Comparison Charts | ☑ drafted |
| `08-time-series-and-temporal-charts.md` | Chapter 6 — Time Series | ☑ drafted |
| `09-distribution-charts.md` | Chapter 7 — Distribution Charts | ☑ drafted |
| `10-relationship-and-correlation-charts.md` | Chapter 8 — Relationship Charts | ☑ drafted |
| `11-part-to-whole-charts.md` | Chapter 9 — Part-to-Whole | ☑ drafted |
| `12-hierarchy-charts.md` | Chapter 10 — Hierarchy | ☑ drafted |
| `13-flow-and-network-charts.md` | Chapter 11 — Flow and Network | ☑ drafted |
| `14-spatial-and-geographic-charts.md` | Chapter 12 — Spatial and Geographic | ☑ drafted |
| `15-specialized-and-financial-charts.md` | Chapter 13 — Specialized and Financial | ☑ drafted |
| `16-design-principles-in-practice.md` | Chapter 14 — Design Principles in Practice | ☑ drafted |
| `17-building-a-complete-project.md` | Chapter 15 — Building a Complete Project | ☑ drafted |
| `99-back-matter.md` | Back Matter | ☐ |

End-of-chapter LLM Exercises (running-project blocks) are appended in a separate pass governed by `_running-project-design.md`.

---

## Build

```bash
./build.sh
```

Output lands in `output/` (gitignored). The pipeline compiles markdown chapters into a single EPUB suitable for KDP submission.

## Figures

```bash
./graphs.sh
```

Processes `<!-- → [TYPE: description] -->` comments across every chapter:

- Tabular figures → classed markdown tables (`.infographic-table`, `.comparison-table`, `.data-table`)
- Non-tabular figures → placeholder images in `images/`, ready to replace
- CSS log appended to `styles/kindle-book.css` on each run

Review `chapters/*-updated.md`, then promote:

```bash
for f in chapters/*-updated.md; do mv "$f" "${f/-updated/}"; done
```

## Styles

| File | Purpose |
|------|---------|
| `styles/kindle.css` | Shared base — typography, figure table classes. Do not edit per book. |
| `styles/kindle-book.css` | Book-specific overrides. Edit freely. `graphs.sh` appends its log here. |

## Publish

Upload `output/brutalist-d3-x-claude.epub` to [KDP](https://kdp.amazon.com).

---

## Why this exists

Most AI-assisted production workflows fail in the same ways. The AI generates before intent is clear. It loses track of what it has already produced. It crosses into decisions that belong to the human. It applies new information without asking. Output accumulates faster than the human can verify. The project becomes unauditable.

This book is one application of the architecture built against every one of those failure modes — deliberately, structurally, and without exceptions carved out for speed or convenience.

The result is a workflow where the human spends time on what is irreducibly human: judgment, direction, verification, decision. Claude handles what it is actually good at: D3 generation, pattern application, information retrieval — within a schema, on request, one chart at a time.

That boundary, held firmly, is the whole idea.

---

## Who This Book Is For

reader's roadmap)

This file is a stub. Sections 1–10 and 12–13 are placeholders for a later pass.
Section 11 (A note about AI) is substantive and written.

A good model for the full version: Pearl's "The Mind Over Data" introduction,
Molnar's Interpretable ML introduction. Both are argument-first and tell the
reader exactly what to expect from each chapter.
-->

# Introduction

<!-- [1] COLD OPEN
     A specific named scene with real stakes.
     No "this book will...", no throat-clearing.

---

## How to Read It

<!-- TODO: populate from chapter content -->

---

## Table of Contents

| Chapter | Title | File |
|---------|-------|------|
| Intro | Introduction | [chapters/00-introduction.md](chapters/00-introduction.md) |
| Intro | Introduction | [chapters/01-introduction.md](chapters/01-introduction.md) |
| 2 | Chapter 02 — Claude Basics for D3 Visualization | [chapters/02-claude-basics-for-d3-visualization-updated.md](chapters/02-claude-basics-for-d3-visualization-updated.md) |
| 2 | Chapter 02 — Claude Basics for D3 Visualization | [chapters/02-claude-basics-for-d3-visualization.md](chapters/02-claude-basics-for-d3-visualization.md) |
| 3 | Chapter 3 — Marks and Channels | [chapters/03-marks-and-channels.md](chapters/03-marks-and-channels.md) |
| 4 | Chapter 4 — Chart Selection as Design Decision | [chapters/04-chart-selection-as-design-decision.md](chapters/04-chart-selection-as-design-decision.md) |
| 5 | Chapter 05 — Reading a Dataset | [chapters/05-reading-a-dataset.md](chapters/05-reading-a-dataset.md) |
| 6 | Chapter 6 — Working with Claude Code | [chapters/06-working-with-claude-code.md](chapters/06-working-with-claude-code.md) |
| 7 | Chapter 07 — Comparison Charts | [chapters/07-comparison-charts.md](chapters/07-comparison-charts.md) |
| 8 | Chapter 8 — Time Series and Temporal Charts | [chapters/08-time-series-and-temporal-charts.md](chapters/08-time-series-and-temporal-charts.md) |
| 9 | Chapter 09 — Distribution Charts | [chapters/09-distribution-charts.md](chapters/09-distribution-charts.md) |
| 10 | Chapter 10 — Relationship and Correlation Charts | [chapters/10-relationship-and-correlation-charts.md](chapters/10-relationship-and-correlation-charts.md) |
| 11 | Chapter 11 — Part-to-Whole Charts | [chapters/11-part-to-whole-charts.md](chapters/11-part-to-whole-charts.md) |
| 12 | Chapter 12 — Hierarchy Charts | [chapters/12-hierarchy-charts.md](chapters/12-hierarchy-charts.md) |
| 13 | Chapter 13 — Flow and Network Charts | [chapters/13-flow-and-network-charts.md](chapters/13-flow-and-network-charts.md) |
| 14 | Chapter 14 — Spatial and Geographic Charts | [chapters/14-spatial-and-geographic-charts.md](chapters/14-spatial-and-geographic-charts.md) |
| 15 | Chapter 15 — Specialized and Financial Charts | [chapters/15-specialized-and-financial-charts.md](chapters/15-specialized-and-financial-charts.md) |
| 16 | Chapter 16 — Design Principles in Practice | [chapters/16-design-principles-in-practice.md](chapters/16-design-principles-in-practice.md) |
| 17 | Chapter 17 — Building a Complete Project | [chapters/17-building-a-complete-project.md](chapters/17-building-a-complete-project.md) |
| 18 | Part II — Examples | [chapters/18-arc-diagram.md](chapters/18-arc-diagram.md) |
| 18 | Chapter 16 — The Brutalist Claude Project | [chapters/18-brutalist-claude-project.md](chapters/18-brutalist-claude-project.md) |
| 19 | Area Graph | [chapters/19-area-graph.md](chapters/19-area-graph.md) |
| 20 | Bar Chart | [chapters/20-bar-chart.md](chapters/20-bar-chart.md) |
| 21 | Box Plot | [chapters/21-box-plot.md](chapters/21-box-plot.md) |
| 22 | Box and Whisker Plot | [chapters/22-box-whisker.md](chapters/22-box-whisker.md) |
| 23 | Brainstorm | [chapters/23-brainstorm.md](chapters/23-brainstorm.md) |
| 24 | Bubble Chart | [chapters/24-bubble-chart.md](chapters/24-bubble-chart.md) |
| 25 | Bubble Map | [chapters/25-bubble-map.md](chapters/25-bubble-map.md) |
| 26 | Bullet Graph | [chapters/26-bullet-graph.md](chapters/26-bullet-graph.md) |
| 27 | Candlestick Chart | [chapters/27-candlestick-chart.md](chapters/27-candlestick-chart.md) |
| 28 | Chord Diagram | [chapters/28-chord-diagram.md](chapters/28-chord-diagram.md) |
| 29 | Choropleth | [chapters/29-choropleth.md](chapters/29-choropleth.md) |
| 30 | Circle Packing | [chapters/30-circle-packing.md](chapters/30-circle-packing.md) |
| 31 | Connection Map | [chapters/31-connection-map.md](chapters/31-connection-map.md) |
| 32 | Density Plot | [chapters/32-density-plot.md](chapters/32-density-plot.md) |
| 33 | Donut Chart | [chapters/33-donut-chart.md](chapters/33-donut-chart.md) |
| 34 | Dot Map | [chapters/34-dot-map.md](chapters/34-dot-map.md) |
| 35 | Dot Matrix | [chapters/35-dot-matrix.md](chapters/35-dot-matrix.md) |
| 36 | Error Bars | [chapters/36-error-bars.md](chapters/36-error-bars.md) |
| 37 | Flow Map | [chapters/37-flow-map.md](chapters/37-flow-map.md) |
| 38 | Gantt Chart | [chapters/38-gantt-chart.md](chapters/38-gantt-chart.md) |
| 39 | Heatmap | [chapters/39-heatmap.md](chapters/39-heatmap.md) |
| 40 | Histogram | [chapters/40-histogram.md](chapters/40-histogram.md) |
| 41 | Illustration Diagram | [chapters/41-illustration-diagram.md](chapters/41-illustration-diagram.md) |
| 42 | Kagi Chart | [chapters/42-kagi-chart.md](chapters/42-kagi-chart.md) |
| 43 | Line Graph | [chapters/43-line-graph.md](chapters/43-line-graph.md) |
| 44 | Marimekko Chart | [chapters/44-marimekko-chart.md](chapters/44-marimekko-chart.md) |
| 45 | Multimodal Distribution | [chapters/45-multimodal-distribution.md](chapters/45-multimodal-distribution.md) |
| 46 | Multiset Bar | [chapters/46-multiset-bar.md](chapters/46-multiset-bar.md) |
| 47 | Network Diagram | [chapters/47-network-diagram.md](chapters/47-network-diagram.md) |
| 48 | Nightingale | [chapters/48-nightingale.md](chapters/48-nightingale.md) |
| 49 | OHLC Chart | [chapters/49-ohlc-chart.md](chapters/49-ohlc-chart.md) |
| 50 | Parallel Coordinates | [chapters/50-parallel-coordinates.md](chapters/50-parallel-coordinates.md) |
| 51 | Parallel Sets | [chapters/51-parallel-sets.md](chapters/51-parallel-sets.md) |
| 52 | Pictogram Chart | [chapters/52-pictogram-chart.md](chapters/52-pictogram-chart.md) |
| 53 | Pie Chart | [chapters/53-pie-chart.md](chapters/53-pie-chart.md) |
| 54 | Point Figure | [chapters/54-point-figure.md](chapters/54-point-figure.md) |
| 55 | Population Pyramid | [chapters/55-population-pyramid.md](chapters/55-population-pyramid.md) |
| 56 | Proportional Area | [chapters/56-proportional-area.md](chapters/56-proportional-area.md) |
| 57 | Radar Chart | [chapters/57-radar-chart.md](chapters/57-radar-chart.md) |
| 58 | Radial Bar | [chapters/58-radial-bar.md](chapters/58-radial-bar.md) |
| 59 | Radial Bar Chart | [chapters/59-radial-bar-chart.md](chapters/59-radial-bar-chart.md) |
| 60 | Radial Column | [chapters/60-radial-column.md](chapters/60-radial-column.md) |
| 61 | Radial Column Chart | [chapters/61-radial-column-chart.md](chapters/61-radial-column-chart.md) |
| 62 | Sankey Diagram | [chapters/62-sankey-diagram.md](chapters/62-sankey-diagram.md) |
| 63 | Scatterplot | [chapters/63-scatterplot.md](chapters/63-scatterplot.md) |
| 64 | Span Chart | [chapters/64-span-chart.md](chapters/64-span-chart.md) |
| 65 | Spiral Plot | [chapters/65-spiral-plot.md](chapters/65-spiral-plot.md) |
| 66 | Stacked Area | [chapters/66-stacked-area.md](chapters/66-stacked-area.md) |
| 67 | Stacked Bar | [chapters/67-stacked-bar.md](chapters/67-stacked-bar.md) |
| 68 | Stem Leaf | [chapters/68-stem-leaf.md](chapters/68-stem-leaf.md) |
| 69 | Stream Graph | [chapters/69-stream-graph.md](chapters/69-stream-graph.md) |
| 70 | Sunburst | [chapters/70-sunburst.md](chapters/70-sunburst.md) |
| 71 | Tally Chart | [chapters/71-tally-chart.md](chapters/71-tally-chart.md) |
| 72 | Timeline | [chapters/72-timeline.md](chapters/72-timeline.md) |
| 73 | Timetable | [chapters/73-timetable.md](chapters/73-timetable.md) |
| 74 | Tree Diagram | [chapters/74-tree-diagram.md](chapters/74-tree-diagram.md) |
| 75 | Treemap | [chapters/75-treemap.md](chapters/75-treemap.md) |
| 76 | Venn Diagram | [chapters/76-venn-diagram.md](chapters/76-venn-diagram.md) |
| 77 | Violin Plot | [chapters/77-violin-plot.md](chapters/77-violin-plot.md) |
| 78 | Word Cloud | [chapters/78-word-cloud.md](chapters/78-word-cloud.md) |

---

## Signature Simulations

| Chapter | Topic | Simulation |
|---------|-------|------------|
| 18 | Part II | AI Wayback Machine |
| 19 | Area Graph | AI Wayback Machine |
| 20 | Bar Chart | AI Wayback Machine |
| 21 | Box Plot | AI Wayback Machine |
| 22 | Box and Whisker Plot | AI Wayback Machine |
| 23 | Brainstorm | AI Wayback Machine |
| 24 | Bubble Chart | AI Wayback Machine |
| 25 | Bubble Map | AI Wayback Machine |
| 26 | Bullet Graph | AI Wayback Machine |
| 27 | Candlestick Chart | AI Wayback Machine |
| 28 | Chord Diagram | AI Wayback Machine |
| 29 | Choropleth | AI Wayback Machine |
| 30 | Circle Packing | AI Wayback Machine |
| 31 | Connection Map | AI Wayback Machine |
| 32 | Density Plot | AI Wayback Machine |
| 33 | Donut Chart | AI Wayback Machine |
| 34 | Dot Map | AI Wayback Machine |
| 35 | Dot Matrix | AI Wayback Machine |
| 36 | Error Bars | AI Wayback Machine |
| 37 | Flow Map | AI Wayback Machine |
| 38 | Gantt Chart | AI Wayback Machine |
| 39 | Heatmap | AI Wayback Machine |
| 40 | Histogram | AI Wayback Machine |
| 41 | Illustration Diagram | AI Wayback Machine |
| 42 | Kagi Chart | AI Wayback Machine |
| 43 | Line Graph | AI Wayback Machine |
| 44 | Marimekko Chart | AI Wayback Machine |
| 45 | Multimodal Distribution | AI Wayback Machine |
| 46 | Multiset Bar | AI Wayback Machine |
| 47 | Network Diagram | AI Wayback Machine |
| 48 | Nightingale | AI Wayback Machine |
| 49 | OHLC Chart | AI Wayback Machine |
| 50 | Parallel Coordinates | AI Wayback Machine |
| 51 | Parallel Sets | AI Wayback Machine |
| 52 | Pictogram Chart | AI Wayback Machine |
| 53 | Pie Chart | AI Wayback Machine |
| 54 | Point Figure | AI Wayback Machine |
| 55 | Population Pyramid | AI Wayback Machine |
| 56 | Proportional Area | AI Wayback Machine |
| 57 | Radar Chart | AI Wayback Machine |
| 58 | Radial Bar | AI Wayback Machine |
| 59 | Radial Bar Chart | AI Wayback Machine |
| 60 | Radial Column | AI Wayback Machine |
| 61 | Radial Column Chart | AI Wayback Machine |
| 62 | Sankey Diagram | AI Wayback Machine |
| 63 | Scatterplot | AI Wayback Machine |
| 64 | Span Chart | AI Wayback Machine |
| 65 | Spiral Plot | AI Wayback Machine |
| 66 | Stacked Area | AI Wayback Machine |
| 67 | Stacked Bar | AI Wayback Machine |
| 68 | Stem Leaf | AI Wayback Machine |
| 69 | Stream Graph | AI Wayback Machine |
| 70 | Sunburst | AI Wayback Machine |
| 71 | Tally Chart | AI Wayback Machine |
| 72 | Timeline | AI Wayback Machine |
| 73 | Timetable | AI Wayback Machine |
| 74 | Tree Diagram | AI Wayback Machine |
| 75 | Treemap | AI Wayback Machine |
| 76 | Venn Diagram | AI Wayback Machine |
| 77 | Violin Plot | AI Wayback Machine |
| 78 | Word Cloud | AI Wayback Machine |

---

## About the Author

**Nik Bear Brown** teaches data science, AI, and visualization at Northeastern University. His work spans machine learning, generative AI, data visualization, and the design of AI-assisted production pipelines. He is the author of the *with LLMs* textbook series and the architect of the **Brutalist** system for AI-assisted creative production — the renderer-agnostic framework whose D3 module is this book and whose other modules include *Brutalist After Effects x Claude*, *Brutalist Blender x Claude*, and *Brutalist Remotion x Claude*. The framework lives at [brutalist.art](https://www.brutalist.art/).

He works in Boston and writes occasionally at his website. He is on most of the major social-media platforms under variations of his name.

---

## Copyright

Copyright © 2026 Nik Bear Brown. All rights reserved.

Published by Bear Brown, LLC.

No part of this publication may be reproduced, distributed, or transmitted in any form or by any means without the prior written permission of the publisher, except in the case of brief quotations in critical reviews and certain other noncommercial uses permitted by copyright law.

The visualizations referenced in this book are drawn from the Humanitarians AI D3 example set, used with permission. The pantry of working examples is available alongside the book as a companion repository.

ISBN: [pending]

First edition: 2026

