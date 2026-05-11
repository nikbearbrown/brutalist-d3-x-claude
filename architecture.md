# Brutalist d3 x Claude — Learning Architecture

**Author:** Nik Bear Brown
*Phase 2 output from Tic TOC. Updated to reflect full theoretical pantry.*

---

## Learning Outcomes

*3–5 outcomes per chapter. At least one at Apply level or above. All assessable.*

### Chapter 1 — Marks and Channels
1. (Remember) Identify the six primary visual channels in Munzner's taxonomy (position x/y, size/area, color hue, color luminance, shape, orientation) and classify each as magnitude or identity channel.
2. (Understand) Explain why position is the most perceptually accurate channel for quantitative data, citing the Cleveland & McGill (1986) accuracy ranking and the Heer & Bostock (2010) replication.
3. (Apply) Given a dataset with specified attribute types (categorical, ordered, quantitative), assign appropriate channels to each attribute and justify each choice using the expressiveness and effectiveness principles.
4. (Analyze) Diagnose a given visualization for channel-attribute mismatches — e.g., encoding a categorical variable with luminance, or scaling a bubble chart by radius rather than area — and specify the correction with perceptual grounding.

### Chapter 2 — Chart Selection as Design Decision
1. (Understand) Classify any chart request into one of eight functional categories (comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial) using the FT Visual Vocabulary framework.
2. (Apply) Use Cairo's four-step decision framework (key message → data structure → functional category → specific form) to select a chart type for a specified dataset and communication goal.
3. (Evaluate) Given two candidate chart types for the same data, justify the selection of one over the other using perceptual, historical, and ethical criteria — including Cairo's argument that an ineffective chart choice is a moral failure, not just an aesthetic one.
4. (Analyze) Identify the adoption failure mode in a poorly chosen chart and specify the correct alternative, citing the specific perceptual mechanism the poor choice violates.

### Chapter 3 — Reading a Dataset
1. (Apply) Given a raw dataset, identify the data types present (categorical, ordinal, quantitative, temporal, geographic) and the relationships available to visualize.
2. (Analyze) Formulate the communication question a visualization should answer — distinguishing the analyst's question from the reader's question — applying Cairo's "compared with what?" principle.
3. (Evaluate) Assess whether a proposed chart type answers the communication question or a different question the author found interesting (the FiveThirtyEight Nigeria kidnapping failure mode).

### Chapter 4 — Working with Claude Code
1. (Apply) Write a Claude Code prompt that specifies chart type, data structure, encoding decisions (channel-to-attribute mappings from Chapter 1), and design constraints precisely enough to produce a usable D3 output.
2. (Analyze) Evaluate a Claude Code–generated D3 visualization against the design specifications in the prompt, identifying gaps using the marks-and-channels vocabulary from Chapter 1.
3. (Create) Iterate on a Claude Code output through at least two revision cycles, each targeting a specific design failure identified by applying Chapters 1–3 frameworks. Apply the MBTA project lesson: "nothing beat iterating on working code."

### Chapter 5 — Comparison Charts
1. (Apply) Build a bar chart, grouped bar chart, and stacked bar chart for the same dataset using Claude Code; explain when each is appropriate using the Few/Evergreen design checklist criteria.
2. (Analyze) Diagnose a truncated-axis bar chart for proportional ink violations, citing the bioRxiv finding that >88% of biological research articles contain this error.
3. (Evaluate) Justify the choice between horizontal and vertical bar orientation for a given label structure and category count, using Gestalt proximity and continuity principles.

### Chapter 6 — Time Series and Temporal Charts
1. (Apply) Select and build a line chart, area chart, or stream graph for a specified temporal dataset, justifying the choice against the marks-and-channels framework.
2. (Analyze) Identify the design failure in an area chart with a non-zero baseline, explaining the perceptual distortion in terms of area as a channel (Kelleher's worked example: temperature area chart with non-zero baseline).
3. (Evaluate) Assess whether a spiral plot is more or less effective than a standard line chart for a given cyclic dataset, citing the specific perceptual trade-off between trend visibility and seasonal pattern visibility.

### Chapter 7 — Distribution Charts
1. (Understand) Explain what information a violin plot reveals that a box plot hides (multimodality, distribution shape) and vice versa (precise quartile values, outlier identification), using kernel density estimation as the mechanism.
2. (Apply) Build a box plot and violin plot for the same distribution dataset; identify which features of each distribution are visible in each form.
3. (Analyze) Diagnose a histogram where bin width obscures bimodality; specify the corrected bin width with reasoning.
4. (Evaluate) Select the most appropriate distribution chart for a specified audience graphicacy level and analytical goal, applying Cairo's concept that more complex forms require more graphicacy to decode.

### Chapter 8 — Relationship and Correlation Charts
1. (Apply) Build a scatterplot with OLS trend line and annotate it with the appropriate correlation-is-not-causation caveat — applying Cairo's ethical frame that omitting this caveat is a moral failure, not just a style choice.
2. (Analyze) Identify overplotting in a scatterplot and specify at least two mitigation strategies (jittering, alpha transparency, 2D binning) with their trade-offs.
3. (Evaluate) Assess whether a bubble chart's third variable encoding uses area or radius, correct it if it uses radius, and explain the Stevens psychophysical power law mechanism behind why area scaling is required.

### Chapter 9 — Part-to-Whole Charts
1. (Apply) Build a pie chart that passes the five-slice rule; rebuild an over-sliced pie chart as a bar chart and justify the redesign using the Cleveland & McGill angle-vs-length accuracy comparison.
2. (Analyze) Explain the perceptual distortion produced by a Nightingale rose chart's outer-ring amplification, tracing the mechanism to the area-encoding problem Bertin's framework predicts.
3. (Evaluate) Select the most appropriate part-to-whole chart for a given dataset size and audience graphicacy level, using Few's clarity-first position rather than Tufte's minimalism-first position.

### Chapter 10 — Hierarchy Charts
1. (Apply) Build a treemap and sunburst from the same hierarchical dataset; identify what each form reveals that the other hides (proportion vs. depth).
2. (Analyze) Diagnose a sunburst with more than five hierarchy levels, explain why outer rings compress into illegible slivers, and specify the redesign.
3. (Evaluate) Justify the choice between treemap and circle packing for a dataset with irregular hierarchy depth, citing the specific perceptual mechanism each exploits.

### Chapter 11 — Flow and Network Charts
1. (Apply) Build a Sankey diagram where flow width is proportional to quantity; verify that the proportionality holds at both the widest and narrowest flows (Tufte's proportional ink principle).
2. (Analyze) Diagnose a chord diagram that has become unreadable due to too many entities and propose a structural redesign, distinguishing between cases where ribbon width carries quantitative meaning vs. cases where existence is all that matters.
3. (Evaluate) Assess whether a force-directed graph or a Sankey diagram better serves a specified flow communication goal, using the Gestalt law of connection to justify the choice.

### Chapter 12 — Spatial and Geographic Charts
1. (Apply) Build a choropleth map and a bubble map for the same geographic dataset; identify the perceptual difference between encoding ratios (choropleth) vs. absolute values (bubble map).
2. (Analyze) Diagnose the area-size distortion in a choropleth, explaining why large-area units dominate perceptually regardless of their data value — the specific mechanism Friendly's history traces to Dupin's 1826 choropleth invention.
3. (Evaluate) Select between choropleth and dot density map for a given spatial dataset, applying Cairo's "compared with what?" criterion to population-based vs. absolute geographic data.

### Chapter 13 — Specialized and Financial Charts
1. (Understand) Explain why Kagi and Point & Figure charts are time-independent and identify the specific class of analytical question (trend reversal detection, support/resistance identification) for which this matters.
2. (Apply) Build a bullet graph as a dashboard component; explain why Few argued it replaces a gauge chart using the Cleveland & McGill accuracy hierarchy (position > angle).
3. (Analyze) Diagnose the outer-ring distortion in a radial bar chart — tracing the mechanism to the area-encoding problem in Bertin's framework — and explain why the same data in a standard bar chart is more perceptually honest.

### Chapter 14 — Design Principles in Practice
1. (Apply) Audit a completed visualization using the Evergreen/Emery checklist (text, arrangement, color, lines, overall) and the Tufte data-ink ratio heuristic; produce a written critique with specific corrections.
2. (Evaluate) Apply Few's critique of Tufte to determine whether a specific visual element is genuine chartjunk or a functional embellishment that serves the communication goal.
3. (Create) Redesign a flawed visualization applying all four principles (proportional ink, data-ink ratio, color accessibility, annotation strategy); document each change with the perceptual mechanism it serves.

### Chapter 15 — Building a Complete Project
1. (Create) Given a raw dataset, produce a complete visualization following the MBTA project process model: define the communication question → prototype multiple forms → select and build with Claude Code → apply the Chapter 14 audit → iterate → publish.
2. (Evaluate) Assess the final output against the communication question identified at the start and specify any gap between the chart and the question it was supposed to answer — applying Cairo's "the purpose of the graphic is to answer the question" criterion.

---

## Outcome Map

| Chapter | Highest Bloom's Level | Assessable? | Maps to course need? |
|---|---|---|---|
| 1 — Marks & Channels | Analyze | Yes | Theoretical foundation for all subsequent chapters |
| 2 — Chart Selection | Evaluate | Yes | Core professional skill; Cairo ethical frame introduced |
| 3 — Reading a Dataset | Evaluate | Yes | Pre-implementation decision; Cairo "compared with what?" |
| 4 — Claude Code | Create | Yes | Implementation workflow; MBTA iteration model |
| 5 — Comparison | Evaluate | Yes | Most common chart family; proportional ink grounded |
| 6 — Time Series | Evaluate | Yes | Temporal data ubiquitous; zero-baseline grounded in channels |
| 7 — Distribution | Evaluate | Yes | Statistical literacy; graphicacy-level sensitivity |
| 8 — Relationship | Evaluate | Yes | Correlation/causation literacy; Cairo ethical annotation |
| 9 — Part-to-Whole | Evaluate | Yes | Pie chart literacy; Cleveland & McGill angle-vs-length |
| 10 — Hierarchy | Evaluate | Yes | Proportion vs. depth trade-off |
| 11 — Flow/Network | Evaluate | Yes | Width-as-channel vs. existence-as-channel distinction |
| 12 — Spatial | Evaluate | Yes | Area-size distortion; ratio vs. absolute value rule |
| 13 — Specialized | Analyze | Yes | Domain conventions; Few's position-vs-angle criterion |
| 14 — Design Principles | Create | Yes | Tufte/Few debate resolved; audit framework synthesized |
| 15 — Complete Project | Create | Yes | Full MBTA-model project; Cairo criterion applied |

---

## Sequencing Model and Justification

**Primary model:** Concrete → Abstract, modified with Simple → Complex within Part II.

**Justification against learner profile:** The primary reader has low graphicacy (Cairo's term) and needs concrete examples before theory. Following Merrill's First Principles, Chapter 1 opens with a live failure — two scatterplots encoding the same data differently — before introducing the Bertin/Cleveland/Munzner theoretical framework. Within Part II, functional categories sequence from most familiar (bar charts in Chapter 5) to most specialized (financial charts in Chapter 13).

**Historical sequencing note:** The Friendly history establishes that every chart type has an origin story tied to a specific communication problem. This is woven into Chapter 2, not presented as a separate history chapter. The historical frame is: every chart in the taxonomy is a solution — knowing the problem it was designed to solve is part of knowing when to use it.

**Most likely breakdown chapter:** Chapter 4 (Claude Code workflow). This is the pivot from theory to practice, and it depends on the reader accepting the book's core premise — that they do not need JavaScript fluency. The MBTA project model (iterate on working code, not mockups) is the chapter's organizing principle.

**Transition chapter:** Chapter 4 is the explicit pivot from design vocabulary (Chapters 1–3) to implementation (Chapters 5–15). Transition condition: the student can formulate a precise chart specification (chart type, channel-to-attribute mappings, data structure) before attempting to prompt Claude Code.

---

## Three-Act Learning Arc

**Act One — Establish (Chapters 1–4)**
*What problem does this act establish?* The gap between "I have data" and "I have a visualization that honestly answers my question" — and the specific skills (graphicacy, channel theory, chart selection judgment) required to close it.
- Opening hook: Cairo's FiveThirtyEight Nigeria kidnapping case. Technically produced, factually misleading. The cost of low graphicacy in a professional context.
- Inciting question (Chapter 1): Why do some visualizations mislead even when the data is correct? The Bertin/Cleveland/Munzner answer: because the wrong channel was used for the wrong attribute type.
- Inciting question (Chapter 2): Why does chart selection matter morally, not just aesthetically? The Cairo answer.
- What the student knows at the end of Act One: The marks-and-channels grammar; chart selection as an ethical and perceptual decision; how to read a dataset before choosing a form; how to direct Claude Code with precision.

**Act Two — Build (Chapters 5–13)**
*What does this act provide?* The complete chart taxonomy — every major form, its origin story (Friendly), its use case, its failure modes, its design rules, its D3 implementation via Claude Code.
- Hardest conceptual moment: Chapter 11 (flow/network) — the distinction between Sankey, chord, and arc diagram depends on whether flow width carries quantitative meaning, which requires fluent channel theory from Chapter 1.
- What the student can DO at the end of Act Two: Identify any chart type from the major taxonomy, justify a selection using the Bertin/Cleveland/Cairo/Few framework, build it with Claude Code, and audit the output for design failures.

**Act Three — Apply (Chapters 14–15)**
*Where does the student put it all together?* Chapter 14 synthesizes Tufte, Few, Cairo, and the Gestalt/preattentive literature into a single audit framework. Chapter 15 is a complete MBTA-model project from raw data to published output, with no scaffolding.
- Final deliverable: A complete visualization built on a real dataset, annotated with design justifications at every decision point, audited against the Chapter 14 framework.

**Arc statement:** "This book takes the reader from low graphicacy and no D3 capability to production-ready visualization judgment grounded in the Bertin–Cleveland–Munzner tradition, by first establishing the marks-and-channels grammar and Cairo's ethical frame, then building fluency across the full chart taxonomy through MBTA-model iteration with Claude Code, then synthesizing all principles into a complete project audit."

---

## Prerequisite Dependency Map

| Chapter | Depends On |
|---|---|
| 1 — Marks & Channels | None — opener |
| 2 — Chart Selection | Chapter 1 (channel vocabulary required for selection criteria; Bertin → Cleveland → Munzner lineage established) |
| 3 — Reading a Dataset | Chapter 2 (functional categories required to frame the communication question) |
| 4 — Claude Code | Chapters 1–3 (design vocabulary required to evaluate Claude Code output; Cairo criterion required to identify failures) |
| 5 — Comparison | Chapter 4 (implementation workflow); Chapter 1 (zero-baseline rule from area-as-channel theory) |
| 6 — Time Series | Chapter 5 (bar charts as baseline comparison; area chart as extension of line chart) |
| 7 — Distribution | Chapter 1 (position encoding for quartiles); Chapter 3 (data type identification — continuous vs. discrete) |
| 8 — Relationship | Chapter 7 (scatterplot as joint distribution of two variables); Chapter 1 (area vs. radius encoding — Stevens' power law) |
| 9 — Part-to-Whole | Chapter 5 (bar chart as the alternative — must know it before the redesign argument); Chapter 1 (angle vs. length accuracy from Cleveland & McGill) |
| 10 — Hierarchy | Chapter 9 (part-to-whole area encoding is the prerequisite for treemap area encoding) |
| 11 — Flow/Network | Chapter 1 (width as a channel); Chapter 9 (proportional flow from part-to-whole logic) |
| 12 — Spatial | Chapter 5 (choropleth as bar chart in geographic form); Chapter 1 (color luminance encoding for sequential data) |
| 13 — Specialized | Chapters 5–6 (financial charts are comparison + time-series variants); Chapter 1 (position vs. angle accuracy for bullet graph justification) |
| 14 — Design Principles | All of Chapters 1–13; Tufte/Few/Cairo/Gestalt sources synthesized |
| 15 — Complete Project | All chapters; MBTA project model as the process template |

**Broken sequences:** None. Every chapter depends only on chapters that appear earlier.

**Load-bearing chapters:** Chapter 1 (marks and channels — prerequisite for everything); Chapter 4 (Claude Code workflow — prerequisite for all implementation chapters); Chapter 5 (bar charts — referenced as the baseline alternative in Chapters 6, 9, 12).

---

## Front-Loading Decisions

- JavaScript prerequisite is NOT SAFE but intentionally excluded — Chapter 4 must demonstrate the Claude Code workflow convincingly enough that JS fluency is not missed. The MBTA case (built entirely in D3 by two students who knew JavaScript) is the before-image; the book's approach is the after-image.
- Basic statistics (quartile, median) is PROBABLY SAFE — embedded explanation at first use in Chapter 7. Cairo's point about graphicacy applies: assume lower prior knowledge than expected.
- The Bertin/Cleveland/Munzner theoretical tradition is NOT SAFE to assume — Chapter 1 builds it from scratch using Kelleher's video as the accessible entry point.
- No Chapter 0 foundations chapter needed. Chapter 4 serves as the minimal onboarding chapter for the implementation layer. The theoretical foundations are Part I's job, not a prerequisites chapter.
