# Brutalist d3 x Claude — Book and Series Summary

*Detailed summary of the book and its parent series, drawn from the current state of the manuscript at /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-d3-x-claude/.*

---

## Part 1: The Brutalist Series

### What Brutalist is

Brutalist is a renderer-agnostic framework for AI-assisted creative production. Its founding observation: when an AI assistant can generate code that produces a deterministic visual artifact faster than a human can write that code, the human's job stops being implementation and starts being supervision. The labor distribution that fact creates — *AI executes, human supervises* — is the architecture Brutalist names and operationalizes.

The framework lives at [brutalist.art](https://www.brutalist.art/). The series is published by Bear Brown, LLC under the byline of Nik Bear Brown. Each book in the series applies the framework to one renderer.

### The five phases

Brutalist names a single five-phase pipeline that every creative production passes through. Different renderers instantiate different mechanics, but the phases are the same:

1. **Audit.** Before generation, the supervisor interrogates the data, the problem framing, and the deployment context. Nothing is generated until the audit is complete. In data viz: read the dataset, identify attribute types, formulate the communication question. In motion graphics: dump the project, build the asset map, understand what exists.

2. **Schema.** The contract that names what the system will do, what it will not do, and how the boundary is enforced. Schema files are persistent — they outlive any single session. The book conventions name three: `CLAUDE.md` (coding rules), `DESIGN.md` (visual rules), `PROJECT.md` (per-project state).

3. **Generate.** The AI produces a candidate output. This is the phase current AI tools are most developed in and where supervision is most absent.

4. **Verify.** The candidate becomes a result only after verification against external referents — does it match the spec, does it pass perceptual audits, does it answer the question. The book teaches a three-layer verification stack: format check, fact check, behavior test.

5. **Handoff.** The verified result crosses a boundary into a context where someone is going to use it. The supervisor's authority to refuse the handoff is part of this phase, not separate from it.

### The five supervisory capacities

Five categories of cognitive work the human supervisor must do because the system cannot do them for itself:

- **Plausibility Auditing (PA)** — checking whether a result is plausible given everything else the supervisor knows, independent of the AI's stated confidence.
- **Problem Formulation (PF)** — asking whether the question the AI is answering is the question that needed to be answered.
- **Tool Orchestration (TO)** — choosing which tool to apply when, and recognizing when a tool is being asked to do work it was not designed for.
- **Interpretive Judgment (IJ)** — reading a result in context, recognizing when the language game the AI is playing has come unmoored from the language game the user is playing.
- **Executive Integration (EI)** — making decisions that no individual sub-discipline can make for the supervisor — whether to deploy, whether to roll back, whether to refuse.

The five names are constant across the entire series. A reader who learns them in one Brutalist book is fluent in the framework in every other.

### The governing files

The framework's persistent context lives in a small set of markdown files:

- **`CLAUDE.md`** — the coding constitution. Loads at the start of every session. Contains: version policy, naming conventions, accessibility standards, what the AI must not do without explicit instruction, the four-move prompt template.
- **`DESIGN.md`** — the visual constitution. Loads on demand, when visual decisions are in scope. Contains: color palette, typography stack, spacing scale, dark-mode behavior, responsive breakpoints, component rules.
- **`PROJECT.md`** — the project state. The per-project audit document with the channel decomposition, communication question, design constraints, iteration log.

The `CLAUDE.md` / `DESIGN.md` split is a consequence of the LLM **instruction budget**: Claude Code's own system prompt consumes ~50 of the ~150–200 instructions Claude can reliably hold in active attention. Loading both coding and visual rules in a single file exceeds the remaining budget; the later rules degrade silently. Two focused files keep both within budget.

### The renderer modules (the series)

Each book in the series applies the framework to one renderer:

| Book | Renderer | Status |
|---|---|---|
| *Brutalist After Effects x Claude* | Motion graphics, ExtendScript | The original module |
| *Brutalist d3 x Claude* | Data visualization in the browser | This book |
| *Brutalist Blender x Claude* | 3D modeling, materials, rendering (Python API) | In development |
| *Brutalist Remotion x Claude* | Programmatic video composition (React) | In development |
| Additional modules (planned) | SVG/GSAP, Rough.js, Three.js, p5.js | Planned |

Plus an adjacent book — *Computational Skepticism for AI* — which is the **AI-deployment-supervision module**: the same framework applied not to a chart or animation but to a deployed predictive or generative AI system. The five supervisory capacities map exactly; the fluency trap is the canonical Brutalist verify-phase failure mode.

---

## Part 2: Brutalist d3 x Claude — The Book

### Structural overview

```
Front matter
Introduction
Chapter 00 — Claude Basics for D3 Visualization
Part I — Concepts (15 chapters, 83,000 words)
Part II — Examples (61 alphabetical chart-type chapters)
Back matter (acknowledgments, author bio, chart-type one-pager,
              full references, glossary, index)
```

The book is approximately 145,000 words across 80 chapter files.

### Front matter — the Brutalist preface

The book opens by positioning itself as the D3 renderer module of the Brutalist system. The preface walks the five Brutalist phases as they apply to D3 — *Audit* becomes data audit and channel-map building; *Schema* becomes the three governing files; *Generate* becomes Claude Code writing D3; *Verify* becomes the Evergreen/Emery audit and the three-layer verification stack; *Handoff* becomes publication with annotation, source documentation, and accessibility metadata. Names the sister volumes and links the series at brutalist.art. Establishes the labor separation: Claude Code handles syntax and computation; the human handles design judgment, problem formulation, and executive integration.

### Introduction — the design layer is the hard layer

Opens with the FiveThirtyEight Nigeria kidnapping case (2014) — a chart whose technical execution was competent but whose underlying data was misread, supported by Erin Simpson's "validate your own data; it's not true just because it's on a goddamn map." Frames the book's central argument: the implementation barrier in D3 was real and is now mostly dissolved by Claude Code; what was always harder, and remains harder, is the *design layer* — which chart fits the data and the question, what the perceptual mechanisms say about which encodings are honest, when a design rule is a heuristic to follow and when it is a heuristic to break.

Names three foundational commitments:

1. **The design layer is the hard layer.** Implementation is delegable; design is not.
2. **Perceptual honesty is the criterion.** Cleveland & McGill's ranking, Stevens' power law, Cairo's "compared with what?" are the tools.
3. **Chart choice is an ethical decision** (Cairo). A chart that distorts the data is not a stylistic choice; it is a moral choice with consequences.

### Chapter 00 — Claude Basics for D3 Visualization

The book's working tools chapter. ~7,200 words.

Teaches:
- **Where Claude lives** — Claude Code, Claude.ai chat, Claude Projects, Cowork, Claude in Chrome — and which to use when.
- **The instruction budget** — Claude Code's system prompt eats ~50 instructions; the remaining ~100–150 must hold project context. The reason `CLAUDE.md` and `DESIGN.md` are separate files.
- **The four-move prompt structure** — show what you have, say what you want, constrain it, ask for verification. The single highest-leverage skill the chapter teaches.
- **Three D3-specific failure modes** — API hallucination (Claude Code uses syntax not in D3 v7), chart-type mismatch (Claude Code chooses a valid chart that doesn't answer the question), channel mismatch (Claude Code encodes a quantitative attribute on an identity channel).
- **Multi-LLM comparison** — used as a targeted strategic tool, not a default workflow. High-leverage for chart selection and accessibility decisions.
- **Three-layer verification stack** — sanity-check the format, check specific facts, test the work in a browser.

The chapter's deliverable: drafts of the reader's `CLAUDE.md` and `DESIGN.md` — two files that travel with them through the rest of the book.

### Part I — Concepts (Chapters 1–15)

**Chapter 1 — Marks and Channels.** *The Channels Your Eye Trusts and the Ones It Doesn't.* Bertin → Cleveland & McGill → Munzner spine. Marks (point, line, area, glyph). Channels (position, length, area, hue, luminance, shape, orientation). Stevens' power law as the perceptual mechanism behind the channel ranking. Munzner's expressiveness and effectiveness principles. Worked examples: Minard's flow map, Snow's cholera dot map, Nightingale's polar area chart — each as an explicit channel decomposition. Five focal-figure prompts, including the opening-case two-scatterplot pair.

**Chapter 2 — Chart Selection as Design Decision.** *The Wrong Chart Feels Familiar; the Right One Takes Work.* Cairo's four-step framework. The FT Visual Vocabulary's eight functional categories (Comparison, Composition, Distribution, Relationship, Hierarchy, Flow, Spatial, Change-over-time). Three failure modes: familiarity bias, aesthetic-first, software-default. The 14-slice pie chart from a humanitarian funding report as the central case. Four focal-figure prompts.

**Chapter 3 — Reading a Dataset.** *Read the Data Before You Reach for the Code.* Data type identification (categorical, ordered, quantitative, temporal, spatial). The analyst's question vs. the reader's question. Cairo's "compared with what?" check. The MBTA process model's pre-coding phase. Three focal-figure prompts.

**Chapter 4 — Working with Claude Code.** *You Decide, the Machine Renders, You Review.* Prompt anatomy applied to D3. The MBTA iteration model (Barry & Card 2014). The Evergreen/Emery audit subset for live iteration. The full pipeline integrating Chapters 1, 2, 3. Three focal-figure prompts.

**Chapters 5–13 — The Chart Taxonomy (family chapters).** Each chapter walks one chart family and the design rules that govern it.

- **Ch 5 — Comparison Charts.** *Length Along a Shared Baseline Is the Honest Channel.* Bar, column, multiset, stacked, radial. Few-resolved stance on the zero baseline.
- **Ch 6 — Time Series and Temporal Charts.** *What Changes, in What Direction, How Fast.* Line, area, stacked area, stream, spiral, Gantt. Marey diagram. Zero baseline differentially applied.
- **Ch 7 — Distribution Charts.** *Shape, Spread, and Skew — Beyond the Mean.* Histogram, box plot, violin, density, stem-and-leaf. Tukey, graphicacy.
- **Ch 8 — Relationship and Correlation Charts.** *Two Variables and the Question They Refuse to Settle.* Scatterplot, bubble, parallel coordinates, heatmap. Stevens' law on bubble area. Correlation-is-not-causation as Cairo-class moral requirement.
- **Ch 9 — Part-to-Whole Charts.** *When the Pieces Have to Add Up to One.* Pie, donut, waffle, Marimekko, Nightingale rose. Five-slice rule. Cleveland & McGill on angle.
- **Ch 10 — Hierarchy Charts.** *Containment as the Encoding.* Treemap, sunburst, circle packing, tree diagram. Squarification (Bruls–Huizing–van Wijk 2000). Depth limits.
- **Ch 11 — Flow and Network Charts.** *What Flows Where — and How Much.* Sankey, alluvial, chord, arc, force-directed. Width-as-channel. Hairball mitigation.
- **Ch 12 — Spatial and Geographic Charts.** *Position on the Earth Is the Story.* Choropleth, dot density, bubble map, connection map. Dupin 1826; Snow 1854. Ratio-vs-absolute.
- **Ch 13 — Specialized and Financial Charts.** *Conventions That Earn Their Strangeness.* Candlestick, Kagi, P&F, bullet graph, radar. Few's argument for bullet graphs replacing gauges.

Each family chapter has one focal-figure prompt that demonstrates the chapter's central argument and a Part II reference list of the chart types it covers.

**Chapter 14 — Design Principles in Practice.** *From Principle to Audit Checklist.* Tufte/Few/Cairo synthesis. Proportional ink. Data-ink ratio. Color (categorical, sequential, diverging). Annotation strategy. The Evergreen/Emery 22-point checklist applied in full. Chartjunk debate explicitly resolved with Few's position. Three focal-figure prompts: before/after audit, color-scale family, annotation Goldilocks.

**Chapter 15 — Building a Complete Project.** *From Raw Data to Published Chart in One Pipeline.* The MBTA process model end-to-end on a UNHCR humanitarian dataset. All five Brutalist phases walked. Five focal-figure prompts — one per phase — culminating in a publication-packaged chart with caption, source citation, methodology, accessibility statement.

### Part II — Examples (61 alphabetical chart-type chapters)

The reference parade. Each chapter is named `NN-{slug}.md` (slug from the pantry, alphabetical, NN from 18 to 78). Each chapter contains:

1. **Title** (chart name) and **slide-title tagline** (from the pantry's HTML page).
2. **Placeholder image** (black 700×420 JPG; user replaces with rendered chart later).
3. **Rich pedagogical prose** extracted from the corresponding pantry HTML page — *What this chart is, How to read it, Why it was chosen here, Strengths and limitations, About this example, Framework reference (FT Visual Vocabulary, Abela quadrant, Tufte principle).*
4. **A single Claude Code prompt** that, when pasted into Claude Code, produces a working D3 chart of that type plus a matching JSON data file.
5. **Reference to bearbrown.co** for the original code and data, copy-paste-ready.

The 61 chart types span the full taxonomy: arc-diagram, area-graph, bar-chart, box-plot, box-whisker, brainstorm, bubble-chart, bubble-map, bullet-graph, candlestick-chart, chord-diagram, choropleth, circle-packing, connection-map, density-plot, donut-chart, dot-map, dot-matrix, error-bars, flow-map, gantt-chart, heatmap, histogram, illustration-diagram, kagi-chart, line-graph, marimekko-chart, multimodal-distribution, multiset-bar, network-diagram, nightingale, ohlc-chart, parallel-coordinates, parallel-sets, pictogram-chart, pie-chart, point-figure, population-pyramid, proportional-area, radar-chart, radial-bar, radial-bar-chart, radial-column, radial-column-chart, sankey-diagram, scatterplot, span-chart, spiral-plot, stacked-area, stacked-bar, stem-leaf, stream-graph, sunburst, tally-chart, timeline, timetable, tree-diagram, treemap, venn-diagram, violin-plot, word-cloud.

Read alphabetically as a reference. The reader takes what they need and skips what they don't.

### Back matter

- **Acknowledgments** — Humanitarians AI team for the working D3 example set; Brutalist series predecessors.
- **About the Author** — Nik Bear Brown's positioning as architect of the Brutalist system.
- **Chart Type Reference** — a one-page decision guide.
- **Selected References** — Bertin, Cairo, Cleveland & McGill, Few, Heer & Bostock, Munzner, Stevens, Tufte, plus practical references (Murray, Wilke, Knaflic, Evergreen, Barry & Card, Kelleher).
- **Colophon** — voice ground truth, build pipeline, the use of Claude Code in production.

### Theoretical commitments held throughout

- **Few > Tufte** — the chartjunk debate resolved on the side of clarity over minimization.
- **Cairo's ethical frame** — chart choice as a moral requirement, not a stylistic preference.
- **Bertin → Cleveland & McGill → Munzner** — the perceptual lineage that grounds every channel decision.
- **Stevens' power law** — the mechanism behind the channel ranking and the radius-vs-area distortion.
- **MBTA process model** — the canonical iteration template for chart-building.
- **Evergreen/Emery 22-point checklist** — the audit instrument applied throughout.

### What the book teaches

A reader who completes the book can:

1. **Diagnose** any chart by naming its marks and channels, identifying any expressiveness or effectiveness violations, and predicting the perceptual error those violations produce.
2. **Specify** any chart precisely enough that Claude Code produces it on the first attempt. The four-move prompt structure is the discipline.
3. **Verify** any Claude-Code-generated chart with the three-layer stack: format check, fact check, behavior test.
4. **Audit** any chart against the Evergreen/Emery 22-point checklist and the design audit framework.
5. **Build** a complete visualization project from raw data through publication, walking all five Brutalist phases.
6. **Maintain** persistent project context in three files — `CLAUDE.md`, `DESIGN.md`, `PROJECT.md` — that grow with the reader's practice and outlive any single chart.

### What the book does not teach

- D3 v7 API reference. Scott Murray's *Interactive Data Visualization for the Web* (3rd ed., O'Reilly) covers this.
- Comprehensive visualization theory. Wilke's *Fundamentals of Data Visualization* and Munzner's *Visualization Analysis and Design* cover this.
- Brutalist as a system. Brutalist's framework documentation (at brutalist.art) covers this.
- Visual judgment in the abstract. The book is a scaffold; the reader builds the muscle by doing the exercises.

---

## Part 3: How the book and the series fit together

A reader can come to *Brutalist d3 x Claude* with no prior exposure to the framework — the book teaches what it needs as it goes. A reader who has worked through *Brutalist After Effects x Claude* will recognize the architecture immediately and only need to learn the D3-specific failure modes (chart-type mismatch, channel mismatch, API hallucination at the v7 level). A reader who finishes this book and moves to *Brutalist Blender x Claude* or *Brutalist Remotion x Claude* will find the same five phases, the same five supervisory capacities, the same three governing files — applied to renderers with different mechanics.

The framework is the spine. The renderers are the surface. The reader who learns one renderer well has learned a discipline portable across all of them.
