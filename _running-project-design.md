# Running Project — Chapter Map & Options

*Step 1 + Step 2 of the running-project exercise generator. Step 3 (per-chapter LLM Exercise blocks appended to each chapter file) waits until you pick a project.*

---

## Numbering note

File numbers and the book's internal chapter numbers are offset by two for chapters in Part I, by two through Part III, and there is no internal number on the Introduction. The map below keys to **file number** because that's how the chapter files are named on disk and how you referenced "up to chapter 17." Internal book chapter is in parens.

- **File 01** — Introduction (no internal number, narrative only; no exercise)
- **File 02** — Chapter 00, Claude Basics
- **Files 03–06** — Book Chapters 1–4 (Part I, The Decision Layer)
- **Files 07–15** — Book Chapters 5–13 (Part II, The Chart Taxonomy)
- **Files 16–17** — Book Chapters 14–15 (Part III, Integration and Production)

Total chapters receiving an LLM Exercise: **16** (file 02 through file 17).

---

## Chapter Map

### File 01 — Introduction *(no internal chapter number)*
The Chibok/FiveThirtyEight case: a chart can be technically competent and factually misleading. Establishes graphicacy as the book's central skill. Names the brutalist posture: clear-eyed about what charts do, hide, and risk. *No LLM exercise — narrative chapter.*

### File 02 — Chapter 00: Claude Basics for D3 Visualization
**Core concepts:** Four-move prompt structure (show / say / constrain / verify); three D3 failure modes (API hallucination, chart-type mismatch, channel mismatch); the CLAUDE.md + DESIGN.md split.
**New capabilities:** Pick the right Claude surface (Code / chat / Project / Cowork) for a D3 task; write a four-move prompt that returns usable D3 on the first attempt; run the three-layer verification stack on any generated chart; produce starting CLAUDE.md and DESIGN.md files.
**Key vocabulary:** Four-move structure, API hallucination, instruction budget, CLAUDE.md, DESIGN.md, verification stack.
**Working examples:** AI capability scores across 8 cognitive domains (vague-vs-specific prompt comparison).

### File 03 — Chapter 1: Marks and Channels
**Core concepts:** Bertin-Cleveland-Munzner framework; magnitude vs. identity channels; Stevens' power law for perceptual accuracy; expressiveness and effectiveness.
**New capabilities:** Decompose any chart spec into mark + channels; rank channels by perceptual strength for the task at hand; match data type to appropriate visual encoding; specify a chart precisely enough for Claude Code to generate it cleanly.
**Key vocabulary:** Mark, channel, position, length, area, hue, luminance, magnitude vs. identity, Cleveland & McGill ranking.
**Working examples:** Minard 1812, Snow 1854 cholera, Nightingale 1858, HAI AI capability box plot.

### File 04 — Chapter 2: Chart Selection as Design Decision
**Core concepts:** Cairo's four-step framework; FT Visual Vocabulary's eight functional categories; chart choice as ethical decision; the "compared with what?" test.
**New capabilities:** Navigate from a vague dataset to a specific chart via communication goal + functional category; apply Cairo's ethical frame before designing; recognize familiarity-bias, aesthetic-first, and software-default failures.
**Key vocabulary:** Eight functional categories (comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial), Cairo's decision tree, "show the data."
**Working examples:** 14-slice humanitarian funding pie (failure) → sorted horizontal bar (fix); three charts from same dataset answering different questions.

### File 05 — Chapter 3: Reading a Dataset
**Core concepts:** Five data types (categorical, ordinal, quantitative, temporal, geographic); analyst's question vs. reader's question; "compared with what?" applied pre-chart; three honest moves when data has gaps.
**New capabilities:** Identify data types in any dataset; distinguish reader from analyst; flag incomplete chart specs; recognize data gaps and choose between better data, reframed question, or acknowledged gap.
**Key vocabulary:** Data types, granularity, aggregation, analyst question, reader question, FiveThirtyEight Nigeria case.
**Working examples:** Humanitarian funding (5 sectors × 3 years); UNHCR refugee statistics.

### File 06 — Chapter 4: Working with Claude Code
**Core concepts:** MBTA "iterate on working code" model; three D3-specific failure modes deep-dive; four-move prompt applied; three-layer verification stack; instruction budget and the CLAUDE.md / DESIGN.md split.
**New capabilities:** Build four-move prompts that produce working D3 first-try; diagnose and fix the three failure modes; apply MBTA iteration discipline; keep CLAUDE.md and DESIGN.md separate by instruction-budget logic.
**Key vocabulary:** MBTA model, four-move, API hallucination, chart-type mismatch, channel mismatch, verification stack, instruction budget.
**Working examples:** HAI humanitarian funding (5 sectors); vague-vs-specific prompt comparison.

### File 07 — Chapter 5: Comparison Charts
**Core concepts:** Zero-baseline rule grounded in area-as-channel theory; Cleveland & McGill position-from-baseline accuracy; multiset vs. stacked vs. small-multiples; Weissgerber's 88% finding; the five-bar limit for radial.
**New capabilities:** Pick bar vs. column by label length and category count; specify zero-baseline as a requirement; choose multiset / stacked / small-multiples by communication structure; diagnose and fix truncated-axis distortion.
**Key vocabulary:** Bar, column, multiset, stacked, radial, zero-baseline, proportional ink, Gestalt proximity, Few's redundancy criterion.
**Working examples:** AI capability bar chart (8 domains, 0–100); humanitarian funding by sector (5 sectors); sorted box plot.

### File 08 — Chapter 6: Time Series and Temporal Charts
**Core concepts:** Gestalt continuity for x-axis time; zero-baseline exception (line uses point position, not bar length); Kelleher's area-chart baseline lesson; multi-series legibility threshold (5 lines max); irregular-interval honesty.
**New capabilities:** Pick line / area / stacked area / stream graph by channel type and baseline requirement; specify temporal axis to respect Gestalt; build multi-series with legibility limits; handle irregular intervals.
**Key vocabulary:** Line chart, area chart, stacked area, stream graph, spiral plot, Gantt, timeline, Marey diagram.
**Working examples:** AI capability over 8 years (3 metrics); humanitarian funding stacked area (5 sectors, 36 months); MBTA transit data.

### File 09 — Chapter 7: Distribution Charts
**Core concepts:** Bin-width problem (Sturges / Scott / Freedman-Diaconis); Tukey's five-number summary; violin reveals multimodality; Cairo's graphicacy as audience constraint; Heer & Bostock histogram perception finding.
**New capabilities:** Pick histogram / box plot / violin / density by sample size, bimodality suspicion, and audience graphicacy; diagnose bin-width sensitivity; test for real bimodality across bin widths.
**Key vocabulary:** Histogram, bin width, box plot, IQR fence, outlier, violin plot, KDE, bandwidth, graphicacy.
**Working examples:** HAI household income box plot (5 zones with outlier cluster); distribution chart comparison for bimodal detection.

### File 10 — Chapter 8: Relationship and Correlation Charts
**Core concepts:** Cairo's "correlation is not causation" as moral responsibility; Stevens applied to bubble radius vs. area; Munzner on parallel-coordinates axis-order dependence; overplotting mitigation.
**New capabilities:** Build scatterplots with OLS trend line and the mandatory caveat annotation; specify bubble area encoding with d3.scaleSqrt; diagnose and fix overplotting (alpha, jitter, hexbin); handle parallel-coordinates axis-order trap.
**Key vocabulary:** Scatterplot, OLS, Pearson's r, bubble chart, radius-vs-area, overplotting, alpha, jittering, hexbin, parallel coordinates, heatmap.
**Working examples:** Education vs. life expectancy (50 countries, r annotation); GDP / life expectancy / population bubble with toggle.

### File 11 — Chapter 9: Part-to-Whole Charts
**Core concepts:** Five-slice rule grounded in angle perception; Bertin area encoding; Cairo's rhetorical-vs-analytical Nightingale distinction; Few's clarity criterion for pie / waffle / bar choice.
**New capabilities:** Apply five-slice rule decisively; diagnose when comparison dominates part-to-whole frame; redesign over-sliced pies as bars; choose pie / donut / waffle / stacked bar / Marimekko.
**Key vocabulary:** Pie chart, five-slice rule, donut, waffle, Marimekko, Nightingale rose, polar area, area-squared distortion.
**Working examples:** Humanitarian funding pie (passes five-slice rule); same data as bar comparison; alluvial across 3 years.

### File 12 — Chapter 10: Hierarchy Charts
**Core concepts:** Treemap squarification; sunburst depth limit (5); circle packing for irregular branching; tree diagram for exact structure; Shneiderman's treemap origin.
**New capabilities:** Pick treemap / sunburst / circle packing / tree diagram by question type (proportions, depth, irregular branching, structure); specify depth limits and layout algorithms; handle deep hierarchies via zoom or form switch.
**Key vocabulary:** Treemap, squarify, treemapBinary / Dice / Slice, sunburst, circle packing, dendrogram, node-link tree.
**Working examples:** Humanitarian R&D treemap (4 sectors × 3–5 sub-categories, 2 levels); sunburst depth comparison; circle packing with irregular depth.

### File 13 — Chapter 11: Flow and Network Charts
**Core concepts:** Bertin's width-as-channel for flow magnitude; Gestalt connection; Sankey origins (Captain Sankey 1898); hairball problem and mitigations; flow magnitude vs. connection existence distinction.
**New capabilities:** Pick Sankey / alluvial / chord / arc / force-directed by whether question is flow magnitude or connection existence; specify d3.sankey() layout with node ordering; mitigate hairball via filter / cluster / form switch.
**Key vocabulary:** Sankey, alluvial, chord (ribbon vs. non-ribbon), arc diagram, force-directed, hairball, community detection.
**Working examples:** Energy-flow Sankey; humanitarian aid 3-column donor-implementer-recipient; MBTA train network force-directed.

### File 14 — Chapter 12: Spatial and Geographic Charts
**Core concepts:** Area-size distortion in choropleths; Cairo's ratio-vs-absolute rule; Dupin's 1826 choropleth (rates, equal-area regions); Snow 1854 dot map as canonical alternative.
**New capabilities:** Pick choropleth / dot density / bubble map / connection or flow map by data type (rate vs. absolute, geographic scale); diagnose area-size distortion and apply mitigations; specify equal-area projections (Albers, Equal Earth, Mollweide).
**Key vocabulary:** Choropleth, area distortion, dot density, bubble map, connection map, flow map, equal-area projection, ratio-vs-absolute.
**Working examples:** GDP-per-capita choropleth (large-country distortion); US uninsured-rate choropleth; food-assistance bubble map; UNHCR refugee flows.

### File 15 — Chapter 13: Specialized and Financial Charts
**Core concepts:** Domain conventions (candlestick OHLC, Kagi, Point & Figure) earn complexity for specific audiences; Few's bullet graph replaces gauge (position beats angle); radial-encoding distortion.
**New capabilities:** Build candlestick / OHLC with position-as-magnitude; understand time-independent charts (Kagi, P&F) and when trend-reversal detection matters; specify Few-style bullet dashboards; diagnose radar-chart axis-order trap.
**Key vocabulary:** Candlestick, OHLC, Kagi, Point & Figure, bullet graph, radar / spider, polar area, time-independent.
**Working examples:** Financial candlestick; Kagi price movement; bullet graph dashboard (revenue vs. target, customer satisfaction, uptime).

### File 16 — Chapter 14: Design Principles in Practice
**Core concepts:** Tufte / Few / Cairo synthesis; proportional ink and data-ink ratio; Gestalt principles; Evergreen-Emery 22-point checklist; color types (categorical, sequential, diverging); chartjunk debate resolved by Few's clarity criterion.
**New capabilities:** Run the 22-point audit on any chart; resolve chartjunk debate per chart using clarity criterion; fix proportional-ink violations; choose color palettes by channel type with color-blind safety; build annotation strategy.
**Key vocabulary:** Proportional ink, data-ink ratio, chartjunk, functional redundancy, Gestalt (proximity / similarity / enclosure / continuity / figure-ground), 22-point checklist.
**Working examples:** Flawed quarterly-sales bar (14 checklist failures); fully redesigned version; multi-chart project consistency.

### File 17 — Chapter 15: Building a Complete Project
**Core concepts:** End-to-end MBTA process (question → audit → prototype → select → build → audit → publish); Brutalist phase model (Audit → Schema → Generate → Verify → Handoff); the three schema files (CLAUDE.md, DESIGN.md, PROJECT.md) as a working system.
**New capabilities:** Execute a full visualization project from raw data to published output; maintain three schema files across a project; iterate through Claude Code build/audit cycles; evaluate output against the original communication question; produce publishable work with annotations and source documentation.
**Key vocabulary:** MBTA model, five-phase Brutalist cycle, CLAUDE.md, DESIGN.md, PROJECT.md, phase checkpoints, publication readiness.
**Working examples:** UNHCR forced displacement 2020–2024 — three reader-focused questions, three chart family forms (heatmap, bar, stacked composition).

---

## Project Options

Four candidates. Each builds something real, lets the student adapt by domain, and respects the labor separation: **the student decides; Claude generates.** Pick one and I'll generate the 16 LLM Exercise blocks.

---

### Project Option 1: The Domain Pantry

**What it is:** The student picks one domain (their company, their thesis topic, a public dataset they care about) and builds one publishable chart per chapter using that domain's data. By the end, they have a 16-chart pantry that mirrors the book's HAI pantry — but in their domain, with their data, justified by their judgment.

**Final deliverable:** A directory of 16 single-file HTML/SVG charts (one per chapter), each with a paired JSON dataset and a `README.md` explaining which question that chart answers, which channels it uses, and why this form earned the slot. Plus an `index.html` that catalogs the pantry like the book's pantry.

**Why it fits this book:** The book is built on a pantry of working examples. The student leaves with their own pantry, in their domain. The labor separation is enforced chart-by-chart: the student names the question and the encoding; Claude renders.

**Adaptability:** A finance student builds the pantry on equity returns, sector exposure, factor loadings. A branding student builds it on campaign performance, channel mix, sentiment over time. A data journalist builds it on a single beat (housing, climate, elections). A bioinformatics student builds it on expression data, pathways, cohort distributions. Every chart type still earns a slot — what the slot holds depends on the student.

**Tool path:** Claude Code as primary (one file per chart). Claude chat for the audit step before each build. A Claude Project to hold the accumulating CLAUDE.md and DESIGN.md across sessions.

---

### Project Option 2: The Single Question

**What it is:** The student picks one consequential, specific question in their domain at the start of the book and refuses to drop it. Each chapter adds one chart that views the question through that chapter's lens. The final deliverable is the same question seen 16 different ways — most viewings will be wrong-shaped (a pie chart of a temporal question is part of the lesson) and the student documents *why* each form earned or failed the question.

**Final deliverable:** A single `data-story.md` plus 16 charts: one per chapter, each annotated with "this form answers the question this way" or "this form fails the question because X." Plus a concluding chapter-by-chapter table mapping each form to its fit. The deliverable is a written reading of one question, illustrated by the full chart taxonomy.

**Why it fits this book:** The book teaches that chart selection is a design decision. This project forces that decision sixteen times against one fixed question. The brutalist refusal behavior is built into the project: most chapters will produce a chart the student must reject as wrong-shaped, and the rejection is the assignment.

**Adaptability:** Finance: *Did our portfolio outperform the benchmark in 2024 because of skill or factor exposure?* Branding: *Did the rebrand change customer perception in the segments we cared about?* Journalism: *Is housing in this city getting more expensive, or is the income distribution shifting?* Bioinformatics: *Does this drug's response differ across patient subgroups, or are we seeing noise?* The question stays; the encoding sequence is the book.

**Tool path:** Claude Code primary. A Claude Project highly recommended — the question, the dataset, and the running list of "earned" vs. "rejected" forms persist across sessions.

---

### Project Option 3: The Brutalist Infrastructure

**What it is:** The student leaves the book with a **reusable brutalist project skeleton** for D3 visualization work — not a portfolio of charts, but the infrastructure that produces portfolios. Each chapter contributes one rule to a growing `CLAUDE.md` and one rule to a growing `DESIGN.md`, plus one PROJECT.md case study where that rule earned its place. By the end, the student has a personal D3 stack — coding constitution, design constitution, and ~16 case-studied PROJECT.md files demonstrating each rule in action.

**Final deliverable:** Three durable files (`CLAUDE.md`, `DESIGN.md`, `PROJECT-index.md`) plus 16 case-study `PROJECT.md` files, each showing one chart, the rule it embodies, and the prompt that produced it. The infrastructure is reusable across any future D3 project the student starts.

**Why it fits this book:** The book's deepest commitment is the schema layer — that you do not generate against vibes, you generate against named conventions. This project IS the schema layer. The student finishes the book with the working brutalist artifact the book argues for, not just charts the book argues are correct.

**Adaptability:** A finance team uses the same `CLAUDE.md` and `DESIGN.md` to govern all their reporting charts. A journalism organization uses them as the in-house style guide enforceable at the prompt level. A research group locks them into their lab's analysis pipeline. The domain shows up only in the case-study `PROJECT.md` files; the constitutions are stack-specific, not domain-specific.

**Tool path:** Claude Code primary (writes the constitutional files, generates the case-study charts). Cowork for the multi-file orchestration. A Claude Project to hold the accumulating constitutions in active context for every session.

---

### Project Option 4: The Audit Resume

**What it is:** The student becomes a chart critic across 16 chapters. Each chapter, they find one **published chart in the wild** that fails in the specific way that chapter teaches against (Chapter 5: a truncated y-axis; Chapter 9: a 14-slice pie; Chapter 12: a choropleth distorted by area; etc.). They audit it using the chapter's framework, then direct Claude Code to produce a corrected version. Final deliverable is a portfolio of 16 audits + redesigns — a critic's CV.

**Final deliverable:** A `_audit-portfolio/` directory with 16 numbered case files. Each contains: a screenshot or link to the failing original, a written audit using the chapter's specific frame, the corrected redesign as a working D3 chart, and a "what changed and why" annotation. Plus an index page that organizes the audits by failure type and severity.

**Why it fits this book:** The book treats chart choice as an ethical decision and graphicacy as a professional skill. This project teaches the skill in its diagnostic form: not "can I build it?" but "can I see what's wrong?" The brutalist refusal is built in — the student must refuse the original chart's argument before redesigning.

**Adaptability:** A finance student audits research-house charts, equity reports, central bank publications. A branding student audits agency case studies and brand performance dashboards. A data journalist audits competing newsrooms' charts. A bioinformatics student audits figures in published papers (a publish-or-perish-rich source). A policy analyst audits government statistics dashboards.

**Tool path:** Claude chat for the audit dialogue (it's discussion-shaped). Claude Code for the redesign. Cowork helpful for fetching and saving the source artifacts.

---

## How to pick

**Pick Option 1 (The Domain Pantry)** if the student needs a tangible portfolio at the end — interview-ready chart work. Highest volume of artifacts. Most concrete.

**Pick Option 2 (The Single Question)** if the student is doing this for one specific question they need to answer and want to see how the form choice changes the answer. Most rigorous on the labor-separation lesson.

**Pick Option 3 (The Brutalist Infrastructure)** if the student is going to keep doing D3 work after the book and wants reusable infrastructure. Highest ROI on durability. Most on-brand with the brutalist commitment.

**Pick Option 4 (The Audit Resume)** if the student is a critic or journalist by inclination and wants the diagnostic-eye skill more than the production skill. Most differentiated from a normal textbook exercise set.

---

## Pause

Pick one. I'll generate the 16 LLM Exercise blocks (file 02 through file 17) and append each to its chapter file. File 01 (Introduction) gets no exercise — it's narrative.

If none of these fit, name the shape you want and I'll propose a fifth.
