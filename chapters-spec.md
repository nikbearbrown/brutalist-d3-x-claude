# Brutalist d3 x Claude — Chapter Specifications

**Author:** Nik Bear Brown
*Phase 3 output from Tic TOC. Updated to reflect full theoretical pantry.*

---

## Chapter Anatomy Template

Every chapter follows this structure:

1. Chapter overview (1 paragraph — "what you'll be able to do")
2. Learning objectives (3–5, Bloom's level explicit)
3. Opening case: a real visualization failure or success that creates the need-to-know
4. Theoretical grounding: the relevant source (Bertin, Cleveland, Cairo, Few, Gestalt, Friendly) introduced at the moment it's needed
5. Core content sections (4–6), each: concept → perceptual mechanism → example → application
6. Mid-chapter checkpoint (one question or short exercise)
7. Extended worked example from the Humanitarians AI D3 example set
8. Chapter summary: capabilities gained, not topics covered
9. Key terms (plain language, non-circular)
10. Discussion questions (3–5, at least one cross-chapter synthesis)
11. Exercises (3–5, at least one requiring production via Claude Code)
12. Further reading (3–5 sources, one-sentence annotation each)

**Theory integration rule:** Theoretical sources are introduced when the student has a problem that theory solves — not before. Bertin appears in Chapter 1 because the student needs a vocabulary for the channel failures they can already see. Cairo appears in Chapter 2 because the student needs an ethical frame for the chart-choice failures they've already diagnosed. Few appears in Chapter 14 because the student needs a resolution to the Tufte vs. Holmes debate they can now evaluate. Theory follows evidence.

---

## Chapter Specifications

---

### Introduction

**One-line:** The API curve is solved. Here is the problem that remains.

**Opening:** The Cairo/FiveThirtyEight Nigeria kidnapping case. A technically competent visualization — bar graphs, animated maps — that was wrong in a consequential way. The data showed news stories about kidnappings, not kidnappings. The result? "Validate your own data. It's not true just because it's on a goddamn map." (Erin Simpson, Twitter, 2014.) This is what low graphicacy costs.

**Core content blocks:**
1. What D3 has always been: two separate problems — the implementation problem and the design problem
2. What Claude Code changed: which of those problems is now delegated
3. What graphicacy is (Cairo's term) and why it's the competency this book builds
4. How to use this book: Part I builds the grammar, Part II builds the taxonomy, Part III applies both

**Bridge:** Raises the question the reader now has — "If Claude Code writes the D3, what do I actually need to know?" Chapter 1 answers with the Bertin/Cleveland/Munzner framework.

---

### Chapter 1 — Marks and Channels

**One-line:** The grammar beneath every chart — the Bertin/Cleveland/Munzner tradition that grounds every design decision in this book.

**Opening case:** Two scatterplots encoding identical data. The first uses position (x/y) for both quantitative variables. The second uses position for one variable and color luminance for the other. One is immediately readable; the other requires effort. Why? The perceptual mechanism behind the difference is the chapter's subject.

**Theoretical sources this chapter introduces:**
- Bertin (1967, *Sémiologie Graphique*): the original taxonomy of visual variables. "The informational invariant" and "information components" in Bertin's vocabulary map to dependent and independent variables in statistical learning — a translation the chapter makes explicit.
- Cleveland & McGill (1986): the accuracy ranking — position > length > angle > area > luminance > hue — grounded in psychophysical research. The Stevens power law (perception of length is linear; perception of area is not) explains why bar charts are more accurate than bubble charts.
- Heer & Bostock (2010): the replication and extension confirming the ranking and extending it to pie charts, circle packing, and treemaps.
- Munzner (2014): the synthesis — magnitude channels (position, length, area, luminance, saturation) vs. identity channels (hue, shape, texture) — and the expressiveness principle (match channel type to attribute type) and effectiveness principle (encode important attributes with high-ranked channels).

**Core content blocks:**
1. Marks: points, lines, areas — what each implies about data continuity and what the choice signals to the reader
2. Channels: the six primary visual variables from Bertin's taxonomy
3. The accuracy ranking: why position is king, with Stevens' power law as the mechanism
4. Magnitude vs. identity channels: which channels encode quantitative data honestly and which encode categorical data honestly
5. The expressiveness and effectiveness principles: Munzner's synthesis as the actionable framework
6. Bertin's specific cases: Napoleon's Russian campaign, Minard's flow map, Snow's cholera dot map — each analyzed as a marks-and-channels decision, not just a historical artifact

**Worked example:** The Humanitarians AI box plot — walk through every channel decision: position (y-axis for income), color hue (group identity), position-x (categorical separation). Show the Claude Code prompt that specified these decisions and the output it produced.

**Bridge:** Marks and channels are the alphabet. Chart types are the words. Chapter 2 is the dictionary — and the grammar for when each word is the right choice.

**Key sources:** Kelleher marks-and-channels video (pedagogical entry point); Bertin *Sémiologie Graphique*; Cleveland & McGill 1986; Heer & Bostock 2010; Munzner *Visualization Analysis and Design* 2014; Nik Bear Brown Bertin notes (in pantry).

---

### Chapter 2 — Chart Selection as Design Decision

**One-line:** Chart selection is an ethical decision with perceptual consequences — Cairo's framework for making it right.

**Opening case:** The FiveThirtyEight Nigeria kidnapping case (from Cairo's "Ethical Infographics"). Not a chart-type failure — a data-choice failure that a chart type obscured. The lesson: "A common problem with tables and graphs is the excessive presence of visual content that isn't information" (Cairo). The chapter's job is to give the student a decision framework rigorous enough to catch this class of failure before publication.

**Theoretical sources this chapter introduces:**
- Cairo (rule utilitarian ethics): choosing an ineffective chart is morally wrong because it impedes understanding. "When a designer chooses a graphic form to represent data just because she likes it, while ignoring evidence that may lead her to choose a more appropriate one, her act is morally wrong." This is not overclaiming — Cairo's argument is careful and specific.
- FT Visual Vocabulary: the eight functional categories as a first-pass filter. This is navigation, not law.
- Data Visualisation Catalogue: the reference tool for finding alternative forms within a functional category.
- Friendly (history): every chart type in the taxonomy has an origin story tied to a specific communication problem. Knowing the problem it was designed to solve is part of knowing when to use it.
- Tufte's basic principle (introduced here, not in Chapter 14): "show the data" — the first test any chart must pass before design decisions are relevant.

**Core content blocks:**
1. The eight functional categories — what each is actually for (the Friendly origin story for each)
2. The FT Visual Vocabulary as a navigation tool, not a rulebook
3. Cairo's four-step decision framework: key message → data structure → functional category → specific form
4. Common selection failures: chart chosen by familiarity, aesthetics, or software defaults
5. The "compared with what?" question (Cairo) as the mandatory check before finalizing any chart choice
6. When rules break down: legitimate cases for non-standard forms and how to defend them

**Worked example:** Take one humanitarian dataset (funding allocation by sector). Walk the four-step framework. Show two candidate chart types that technically work. Apply the Cairo ethical test. Build both with Claude Code and compare what each communicates honestly.

**Bridge:** The framework tells you which functional category. Within a category, you still need to know what the specific forms do. Chapters 5–13 cover each category in depth.

---

### Chapter 3 — Reading a Dataset

**One-line:** Before touching D3 — identify what type of data you have and what question your reader needs to answer.

**Opening case:** An analyst wants to "visualize refugee flows." What does that actually mean? Flow by origin country to destination? Flow over time? Flow relative to population? Each is a different dataset, a different chart type, and a different communication question. The work before the work — which the MBTA team calls "understanding what information would be interesting to people and then narrowing down our focus based on the data that we could gather."

**Theoretical sources:**
- Cairo: the analyst's question vs. the reader's question are often different. The chart must answer the reader's question, not the analyst's question about the data.
- Friendly's "quantitative comparisons" principle (from the Snow analysis): always ask "compared with what?" before choosing a form. The answer determines the chart type.
- FT Visual Vocabulary data types: categorical, temporal, relational, or hierarchical — the prior decision before functional category.

**Core content blocks:**
1. Data type identification: categorical, ordinal, quantitative, temporal, geographic — and the chart families each enables
2. The analyst's question vs. the reader's question: these are often different and the chart must answer the reader's
3. The "compared with what?" test: identifying the comparison the chart must make explicit
4. Identifying the relationship: comparison, trend, distribution, correlation, composition, spatial pattern, flow
5. When your dataset doesn't answer your question: honest treatment of data gaps

**Worked example:** The Humanitarians AI choropleth dataset (GDP per capita). Walk through: what data types are present, what relationships are available, what question the reader needs to answer, which relationships serve that question. Apply the "compared with what?" test to identify whether a ratio or absolute value is needed.

---

### Chapter 4 — Working with Claude Code

**One-line:** How to turn a chart specification into a working D3 visualization — and how to iterate on the output the way the MBTA team iterated on working code.

**Opening case:** The MBTA project's central lesson: "nothing beat iterating on working code." Two Claude Code prompts for the same bar chart: one vague ("make a bar chart of funding by sector"), one precise (specifying data structure, channel-to-attribute mappings from Chapter 1, zero-baseline requirement, color encoding for sector identity). Show both outputs. The difference is design vocabulary from Chapters 1–3 — not D3 knowledge.

**Theoretical sources:**
- MBTA project (Barry & Card): the iteration model — prototype → evaluate → revise. The "levels of abstraction" framework (Bret Victor) for moving between a map and its data encoding.
- MBTA project: "avoiding administrative debris" — Claude Code prompts should specify what to build, not describe UI widgets. The Marey diagram as an "information-rich interface for controlling the visualization."
- Few's design checklist (Evergreen/Emery): the evaluation criteria Claude Code output is measured against. Not Tufte's minimalism commandments — Few's "does this support the message?" test.

**Core content blocks:**
1. The Claude Code + D3 pipeline: environment setup (Observable, CodePen, local), how D3 loads via CDN
2. Prompt anatomy: chart type, data structure, channel-to-attribute mappings, design constraints — drawn from the Chapter 1 vocabulary
3. Evaluating output using Few's criteria: text hierarchy, arrangement, color, lines, overall — the Evergreen/Emery checklist as the evaluation instrument
4. Iteration workflow: how to give correction prompts that converge. The MBTA model: one concern per iteration, working code as the base
5. What Claude Code cannot decide: the design judgments that require Chapters 1–3 vocabulary
6. Common failure modes in generated D3: truncated axes, radius-instead-of-area encoding, missing zero baseline — each named as a channel theory violation

**Worked example:** Full pipeline walkthrough using a humanitarian dataset. Apply Chapter 3 (read the dataset). Apply Chapter 2 (select the chart with Cairo's framework). Apply Chapter 1 (specify channel-to-attribute mappings). Write the Claude Code prompt. Show the output. Run the Evergreen/Emery checklist. Iterate once. Final output with channel-theory annotation.

---

### Chapter 5 — Comparison Charts

**One-line:** Bar, column, multiset, stacked, radial — when each is right, when each misleads, and why the zero baseline is not a stylistic preference.

**Opening case:** The "AI adoption by sector" horizontal bar chart from Humanitarians AI. Walk through every design decision: horizontal orientation (long sector labels → Gestalt continuity), zero baseline (area as channel — proportional ink rule), HAI color palette (hue for categorical encoding, one hue per group).

**Theoretical sources:**
- Cleveland & McGill: bar charts are the most accurate method for quantitative comparison because position along a common scale is the highest-accuracy channel.
- Tufte's proportional ink principle: the area of the bars must be proportional to the data values. Zero baseline is not a stylistic choice — it's required by the channel.
- bioRxiv (2024): >88% of biological research articles contain bar graphs that violate the zero-baseline rule. The violation is systematic, not idiosyncratic.
- Gestalt proximity: horizontal vs. vertical bar orientation — proximity of labels to values determines reading order.

**Core content blocks:**
1. Bar/column dichotomy: label length and category count as the structural decision variables (not aesthetic preference)
2. Multiset (grouped) vs. stacked: when you need both total and component vs. when you need only proportion
3. The zero-baseline rule: the bioRxiv evidence, the area-as-channel mechanism, why truncated axes are a moral failure in Cairo's frame
4. Radial bar charts: when they work (cyclic/seasonal data), when they mislead (comparison of magnitudes), the perceptual cost of curved length — the Cleveland & McGill accuracy ranking applied
5. The >15-category problem: when bar charts fail and what replaces them

**Worked example:** The AI adoption by sector example from the HAI pantry. Full Claude Code prompt specifying all channel decisions. Audit using Evergreen/Emery checklist. Identify and correct one failure in the generated output.

---

### Chapter 6 — Time Series and Temporal Charts

**One-line:** Line, area, stream graph, spiral, Gantt — and why the non-zero area baseline is always wrong, even when the software defaults to it.

**Opening case:** The AI capability gap line chart from HAI — three series, diverging trend, 2016–2024. Why a line chart and not a stacked area? The channel answer: line position encodes individual values accurately; stacked area encodes the sum accurately but makes individual non-baseline series unreadable. The choice depends on whether the reader's question is about individual trends or cumulative total.

**Theoretical sources:**
- Kelleher video: the area chart with non-zero baseline worked example — temperature over time. "This is actually misleading because the area doesn't have a zero baseline." The mechanism: area as a channel requires a zero reference.
- MBTA project: the Marey diagram as a time series that doubles as an interaction interface — "an information-rich interface" that avoids administrative debris.
- Gestalt continuity: time should always run left-to-right. Temporal axis breaks (skipping periods) violate continuity and mislead trend perception.

**Core content blocks:**
1. Line charts: the continuous data requirement, the don't-skip-intervals rule, multi-series legibility limits (Gestalt similarity — when colors fail to distinguish)
2. Area charts: the zero-baseline requirement as a channel theory constraint, not a style rule — cumulative volume vs. individual values
3. Stacked area and stream graph: when the flowing shape encodes something the stacked bar cannot — the organic form as signal, not noise
4. Spiral plots: cyclic data, the Archimedean layout, when seasonal pattern matters more than absolute trend
5. Gantt and timeline: task duration vs. milestone events, the MBTA timetable as a real-world worked example

**Worked example:** The HAI stacked area chart (humanitarian funding 2022–2024) and the spiral plot (monthly aid delivery seasonality). Build each with Claude Code. Compare what each reveals vs. hides.

---

### Chapter 7 — Distribution Charts

**One-line:** What a violin plot reveals that a box plot hides — and the graphicacy cost of each form.

**Opening case:** The HAI box and whisker plot — five residential zones, Suburban shows upper outliers suggesting an affluent subpopulation. The box plot reveals their existence; it cannot reveal whether they form a separate cluster or a continuous tail. A violin plot answers the follow-up question. The choice between forms depends on the reader's question and their graphicacy level.

**Theoretical sources:**
- Tukey (1977): the box plot's five-number summary and the 1.5×IQR fence rule for outliers. Every design decision in the standard box plot traces to this paper.
- Cairo (graphicacy): violin plots are more information-dense but require more graphicacy to read. Chapter 7 is where the Cairo concept of audience graphicacy becomes a practical design constraint, not just a theoretical one.
- Heer & Bostock (2010): extending accuracy research — histograms and bar charts show that bin choices affect perceived distribution shape, exactly the failure mode this chapter names.

**Core content blocks:**
1. Histograms: the bin-width problem — how bin size can hide bimodality or create false peaks (the mechanism, not just the rule)
2. Box and whisker: Tukey's five-number summary, the 1.5×IQR fence, what skew looks like in a box, what multimodality looks like (invisible)
3. Violin plots: kernel density estimation as the mechanism, the bimodality reveal, when sample size is too small for a reliable violin (n < 40 as a rough threshold)
4. Density plots: the Epanechnikov kernel, smooth distribution comparison, the lack of precise summary statistics
5. Stem-and-leaf: small datasets (n < 50), preserving raw values, the back-to-back form for comparison

**Worked example:** The HAI box plot and the KDE + mixture visualization. Build both with Claude Code. Annotate which features of the distribution each form reveals and which each hides.

---

### Chapter 8 — Relationship and Correlation Charts

**One-line:** Scatterplots, bubble charts, heatmaps, parallel coordinates — and the annotation that belongs on all of them.

**Opening case:** The HAI scatterplot (education index vs. life expectancy) with OLS trend line and Pearson r readout. Strong positive correlation. Cairo's question: what would it take to claim causation? The annotation "correlation is not causation" is not boilerplate — it's a Cairo-class ethical requirement. Omitting it when the visual pattern is compelling is a moral failure in Cairo's frame.

**Theoretical sources:**
- Cairo ("Ethical Infographics"): the El País independence poll case — 45.3% vs. 44.5% with a margin of error of ±2.95. The story said Catalonia "swings toward No." The correct statement: the difference is within sampling error. Uncertainty visualization is an ethical obligation, not an enhancement.
- Stevens' psychophysical power law: area perception is non-linear. Bubble charts scaled by radius rather than area violate this — the visual difference appears larger than the actual difference. This is the mechanism behind the radius-not-area failure.
- Munzner: parallel coordinates as a channel-theory workaround for high-dimensional data — each axis is position, the highest-accuracy magnitude channel, but axis order creates strong visual patterns that may not reflect the data.

**Core content blocks:**
1. Scatterplots: position encoding for two quantitative variables, OLS trend line, overplotting mitigation
2. Bubble charts: area (not radius) as the third channel — Stevens' power law as the mechanism, the HAI proportional area chart with radius-error toggle as the worked example
3. Connected scatter: tracking a relationship over time, when the path matters as much as the points
4. Parallel coordinates: multivariate comparison, axis order dependence, brushing interaction
5. Heatmaps: two categorical variables + quantitative intensity, color scale choice for sequential vs. diverging data

**Worked example:** The HAI scatterplot (education index, life expectancy, population) and the parallel coordinates plot (humanitarian AI programs across 7 dimensions). Build both with Claude Code. Include the correlation-is-not-causation annotation as a non-negotiable design element.

---

### Chapter 9 — Part-to-Whole Charts

**One-line:** Pie, donut, waffle, Marimekko, Nightingale rose — the perceptual mechanisms behind their limitations and the conditions under which each is honest.

**Opening case:** The HAI pie chart with the five-slice enforcement rule documented in the code. Why five? Cleveland & McGill: humans perceive angle with significantly less accuracy than length. Past five slices, angle differences are too small for reliable perception. This is not Tufte's aesthetic preference — it's a perceptual accuracy finding.

**Theoretical sources:**
- Cleveland & McGill (1986): angle vs. length accuracy — the mechanism behind the pie chart's limitation.
- Bertin (from HAI pantry notes): pie charts use area as the encoding channel — but humans perceive area non-linearly. The donut chart's center space is perceptual real estate, not decoration.
- Cairo: the Nightingale rose chart case — Florence Nightingale used it to argue for sanitary reform. The outer-ring amplification distortion was a known limitation she accepted because the visual argument was compelling. Cairo's position: this is defensible in advocacy contexts; in analytical contexts it requires explicit disclosure.

**Core content blocks:**
1. Pie charts: the five-slice rule as a perceptual accuracy threshold, not an aesthetic preference; when they are honest (significant proportional differences, few categories)
2. Donut charts: the same perceptual limitations as pie; the center space as a secondary encoding opportunity
3. Waffle charts: equal-area cells, why they're more accurate than pie for proportional comparison, the dot-matrix counting mechanism
4. Marimekko: two dimensions simultaneously, the variable-width stacked bar, when the "birds-eye view" earns its complexity cost
5. Nightingale rose: the outer-ring amplification distortion as a known design trade-off, the Bertin area-encoding mechanism, the Cairo disclosure requirement

**Worked example:** The HAI donut chart and Nightingale rose — build both with Claude Code, including the distortion-acknowledgment toggle from the HAI implementation. This toggle is the Cairo ethical frame made interactive.

---

### Chapter 10 — Hierarchy Charts

**One-line:** Treemap, sunburst, circle packing, tree diagram — when to show proportion vs. depth vs. exact structure.

**Opening case:** The HAI circle packing chart (AI applications in humanitarian domains). Why circle packing and not a treemap? The hierarchy has irregular depth — some branches go 3 levels, some 2. Circle packing handles this more gracefully because the nested circles can accommodate irregular branching without distorting the area encoding. This is a Bertin-class channel decision, not an aesthetic preference.

**Theoretical sources:**
- Bertin: area encoding as the channel for treemap and circle packing. The squarification algorithm (Bruls, Huizing, van Wijk 1999) maximizes aspect ratio to make area comparison more accurate.
- Gestalt figure/ground: sunburst diagrams create strong center/periphery figure-ground relationships. Outer rings compress as hierarchy deepens — a predictable Gestalt failure mode.
- Friendly (history): treemaps were invented by Ben Shneiderman in 1991 for a specific problem — visualizing disk usage with nested directories. Knowing this problem clarifies when treemaps work and when they don't.

**Core content blocks:**
1. Treemaps: squarified algorithm, area encoding, the three-level depth limit, zoomable interaction for deep hierarchies
2. Sunburst diagrams: concentric rings, radial encoding, when depth matters more than proportion, the five-level legibility limit
3. Circle packing: nested circles, irregular hierarchy depth, the space-inefficiency trade-off vs. treemap
4. Tree diagrams and dendrograms: node-link structure, collapsible interaction, when exact structure matters more than proportion

**Worked example:** The HAI treemap (global R&D by sector) and sunburst (hierarchical composition). Build both with Claude Code. Annotate which structural features each form reveals vs. hides.

---

### Chapter 11 — Flow and Network Charts

**One-line:** Sankey, alluvial, chord, arc diagram, force-directed — when width carries quantitative meaning and when it doesn't.

**Opening case:** The HAI Sankey (global energy flow). Flow width is proportional to energy quantity in exajoules — this is area-as-channel in Bertin's framework. What breaks if all flows have the same width? The chart becomes a topology diagram (does a connection exist?) rather than a flow diagram (how much flows?). The distinction between these two questions determines the chart type.

**Theoretical sources:**
- Bertin: width as a channel — width can encode quantitative variables (Sankey) or simply indicate connection existence (non-ribbon chord, arc diagram). The choice between these is a channel-theory decision.
- Gestalt connection: connected elements are perceived as belonging to the same group. Force-directed graphs exploit this — but when connection density is high, the visual becomes a "hairball" where the Gestalt law fails.
- Cairo: Sankey diagrams were invented for energy flow analysis. Alluvial diagrams were invented for tracking categorical shifts over time (voter flows, student outcomes). Knowing the original problem clarifies the use case.

**Core content blocks:**
1. Sankey diagrams: proportional flow width (width as quantitative channel), left-to-right organization, energy/budget/funnel use cases
2. Alluvial diagrams: Sankey across time, categorical shift applications, the distinction from Sankey
3. Chord diagrams: circular organization, inter-entity flow, ribbon width as quantitative channel vs. non-ribbon for existence only
4. Non-ribbon chord and arc diagrams: existence-as-channel, biological gene interaction networks, co-occurrence matrices
5. Force-directed graphs: network topology, the cluster-and-outlier question, the hairball failure mode and mitigation strategies

**Worked example:** The HAI non-ribbon chord (humanitarian coordination network) and force-directed (humanitarian AI ecosystem). Build both with Claude Code. Annotate the channel-theory decision that determines which form is correct for which question.

---

### Chapter 12 — Spatial and Geographic Charts

**One-line:** Choropleth, dot map, bubble map, connection map — and the area-size distortion that haunts all of them.

**Opening case:** The HAI choropleth (GDP per capita). The United States and Russia dominate visually despite having middling per-capita GDP values. Large geographic area amplifies perceived importance regardless of data value — the choropleth's fundamental limitation. Friendly's history: Baron Charles Dupin invented the choropleth in 1826 to map French illiteracy. The area-size distortion was recognized almost immediately.

**Theoretical sources:**
- Friendly (history): Dupin's 1826 choropleth as origin; Snow's 1854 dot map as the demonstration that dot maps can reveal what choropleths hide (the Broad Street pump cluster was invisible in any aggregated geographic view).
- Tufte (Snow analysis): Snow's map succeeded because it made quantitative comparisons explicit — the brewery workers with no cholera, the workhouse with far fewer deaths than expected. The "compared with what?" question, answered spatially.
- Cairo: ratio vs. absolute value rule — choropleths should show rates (inhabitants per km², illness per capita), not absolute counts. Absolute counts require bubble maps where area is proportional to value.

**Core content blocks:**
1. Choropleth maps: color encoding for ratios, the area-size distortion mechanism, the ratio-not-absolute-counts rule
2. Dot density maps: one dot per N units, why they're more honest for density data, the Snow dot map as the canonical case
3. Bubble maps: proportional symbol (area not radius), the overlap problem for dense geographic distributions
4. Connection maps and flow maps: great-circle routes, flow volume encoding, when the "spaghetti" failure mode occurs

**Worked example:** The HAI choropleth (GDP per capita) and bubble map (US food assistance by state). Build both with Claude Code. Include the ratio-vs-absolute annotation as a non-negotiable design element.

---

### Chapter 13 — Specialized and Financial Charts

**One-line:** Candlestick, Kagi, Point & Figure, bullet graph, radar — when domain conventions encode information that standard charts cannot.

**Opening case:** The HAI candlestick chart (Chicago wheat futures). Why not a line chart? The OHLC encoding — open, high, low, close — in a single glyph encodes four quantitative values simultaneously using position (the most accurate channel from Cleveland & McGill) for all four. The convention is not arbitrary; it's perceptually efficient for the specific question traders need to answer.

**Theoretical sources:**
- Cleveland & McGill: position as the highest-accuracy magnitude channel. Bullet graphs replace gauge charts because position along a common scale (bullet) is more accurate than angle (gauge). This is not a stylistic preference — it's a measurable accuracy difference.
- Bertin: radar charts encode multivariate data using angle and length in a circular layout. Angle is less accurate than position (Cleveland & McGill). The axis-order dependence (changing axis order changes the visual shape) is a direct consequence of using angle as the encoding channel.
- Cairo: time-independent charts (Kagi, Point & Figure) are domain conventions that serve a specific analytical question (trend reversal detection, support/resistance identification). They're not better than time-series charts; they're better for a specific question.

**Core content blocks:**
1. Candlestick and OHLC: four-value encoding using position (the highest-accuracy channel), body/wick distinction, when this form is overkill
2. Kagi and Point & Figure: time-independent charts, filtering out noise, support/resistance identification — the specific question these forms were built for
3. Bullet graphs: Few's position-vs-angle argument for replacing gauge charts; primary measure + target + qualitative band in one perceptually efficient display
4. Radar/spider charts: the axis-order dependence problem as a Bertin-class channel failure; when the shape carries meaning (performance profiling) and when it misleads
5. Nightingale rose revisited: cross-reference from Chapter 9 with the domain-convention framing

**Worked example:** The HAI Kagi chart and bullet graph. Build both with Claude Code. Annotate the Cleveland & McGill accuracy reasoning behind the bullet graph's design.

---

### Chapter 14 — Design Principles in Practice

**One-line:** The Tufte/Few/Cairo synthesis — a single audit framework that resolves the chartjunk debate and applies it to Claude Code output.

**Opening case:** A real visualization from a published report with multiple design failures. Walk the audit: proportional ink violation (truncated axis — the bioRxiv finding), data-ink clutter (unnecessary gridlines — Tufte's chartjunk category), accessibility failure (red/green without secondary cues — the color-blindness simulator test), annotation gap (no callout for the key finding — Cairo's "the chart must answer the question" criterion). Name each failure with its theoretical grounding, not just its appearance.

**The Tufte/Few/Cairo resolution (central to this chapter):**

Tufte: maximize data-ink ratio. Remove everything that isn't data.
Holmes: embellishments that support the message can increase recall without decreasing comprehension.
Few: the Bateman/Holmes chartjunk study showed embellishments don't reduce comprehension; Tufte's data-ink ratio is a heuristic, not a law. "Clarity over minimization."

The book's position (explicitly stated in this chapter): Few's framework is correct for the use cases this book covers. The evaluation criterion is "does this visual element support the communication goal?" If yes, it may stay. If no, it must go. This is a judgment call, not a rule — and the preceding 13 chapters have built the judgment required to make it.

**Theoretical sources (synthesis):**
- Tufte: data-ink ratio, chartjunk, proportional ink. The foundational rules, introduced as heuristics.
- Few: the Bateman/Holmes study analysis, "clarity over minimization," the redesigned plain charts that demonstrate good simplicity vs. Tufte's sometimes counterproductive extreme minimalism.
- Cairo: graphicacy as the audience variable — the same chart may be appropriate for experts and misleading for general audiences. The uncertainty visualization obligation.
- Gestalt: preattentive attributes and laws of grouping as the mechanism behind all design rules — proximity, similarity, enclosure, continuity, figure/ground.
- Evergreen/Emery: the 22-point data visualization checklist as the audit instrument.

**Core content blocks:**
1. Proportional ink: Tufte's principle, the bioRxiv evidence, the zero-baseline and area-not-radius rules — and the specific channel-theory mechanism behind each
2. Data-ink ratio: Tufte's heuristic, Few's refinement, the chartjunk debate resolution — "does this support the message?" as the criterion
3. Color for data: categorical (hue), sequential (luminance), diverging (two-hue), the five-color palette limit, color-blind simulation as the Cairo-class accessibility check
4. Annotation strategy: when to annotate, Cairo's "the chart must answer the question" test applied to callouts, direct labeling vs. legend trade-off

**Worked example:** Take a flawed visualization. Run the Evergreen/Emery checklist. Apply the Tufte/Few resolution for each flagged item. Produce the redesigned version with Claude Code. Document each change with the theoretical principle it serves (Tufte? Few? Cairo? Gestalt?).

---

### Chapter 15 — Building a Complete Project

**One-line:** From raw dataset to published D3 visualization — the MBTA project model applied from start to finish.

**Opening case:** The MBTA project's three guiding questions: "When and where are the trains crowded or delayed? How do snowstorms affect the system? How congested is my route?" Every design decision in the project traces back to one of these questions. The lesson: start with the question, not the data.

**The MBTA process model (this chapter's organizing principle):**
1. Define the communication questions (plural) before touching data or charts
2. Explore the data to find what it actually supports
3. Prototype multiple forms — "mockups and prototypes helped us formulate ideas but nothing beat iterating on working code"
4. Select the form that answers the reader's question most directly
5. Build with Claude Code, iterate
6. Apply the Chapter 14 audit
7. Publish with annotations

**Theoretical sources:**
- MBTA project (Barry & Card): the complete process model, the levels of abstraction framework, avoiding administrative debris, integrating words/numbers/graphics
- Cairo: "the purpose of journalism is to increase knowledge while minimizing harm" — applied to the publication decision: publish the chart that answers the question honestly, not the chart that looks most impressive
- Friendly: the full visualization lineage — this chapter is where the student produces something that joins that lineage

**Core content blocks:**
1. Phase 1 — Questions: define the communication questions before touching data
2. Phase 2 — Data: what format, what cleaning, what Claude Code can do in data prep
3. Phase 3 — Selection: the Chapter 2–3 framework applied to a real dataset with multiple candidate chart types
4. Phase 4 — Build: Claude Code prompt with full channel-theory specification, initial review, first iteration
5. Phase 5 — Audit: Chapter 14 Evergreen/Emery checklist applied to the output, specific corrections with theoretical grounding
6. Phase 6 — Publish: embed options, responsiveness, accessibility final check, the Cairo disclosure obligations

**Worked example:** This chapter IS the worked example. A humanitarian dataset (UNHCR forced displacement). Every step is the content.

---

## Case Study Strategy

**Domain coverage (from the HAI pantry):**
- Humanitarian/development data: choropleth, flow map, bubble map, Sankey, chord, network — appears in at least one example per chapter
- Financial markets: candlestick, Kagi, Point & Figure, OHLC — confined to Chapter 13
- Public policy/social science: bar charts, population pyramid, scatterplot, stacked area
- Environmental/energy: stream graph, treemap, spiral plot
- Health/epidemiological: box plot, violin plot, histogram, dot map (Snow case)

**Failure mode cases (required — at least one per Part):**
- Introduction: FiveThirtyEight Nigeria kidnapping (Cairo) — proxy variable, no context
- Chapter 1: luminance-for-categorical encoding failure (Kelleher video worked example)
- Chapter 5: truncated axis bar chart (bioRxiv finding — >88% of biology articles)
- Chapter 7: histogram with bin-width that hides bimodality
- Chapter 8: bubble chart scaled by radius not area (Stevens' power law violation)
- Chapter 9: 14-slice pie chart (Cleveland & McGill angle accuracy limit exceeded)
- Chapter 12: choropleth of absolute values across geographies of different size (Dupin's original limitation)
- Chapter 14: the Challenger O-ring charts (Tufte's analysis) — the ultimate failure-mode case: correct data, wrong display, fatal decision

**The Challenger case (Chapter 14 supplementary):**
Tufte's analysis of the Challenger launch decision charts is the strongest possible case for the Chapter 14 thesis. The engineers had the correct data; the display failed to show the causal relationship between temperature and O-ring damage; seven people died. The lesson: "displays of evidence implicitly but powerfully define the scope of the relevant." The Chapter 14 audit framework is the tool that would have caught this failure.

---

## Contested Claims Audit

| Claim | Status | Treatment |
|---|---|---|
| "Pie charts should generally be avoided" | Disputed | Chapter 9 presents the Cleveland & McGill angle-accuracy evidence and the five-slice rule, not a blanket prohibition. Few's position: pie charts are wrong in specific conditions. |
| "Tufte's rules are laws" | Settled (against) | Chapter 14 explicitly presents Few's critique: the Bateman/Holmes study, the redesigned plain charts, the "clarity over minimization" resolution. |
| "Bar charts must start at zero" | Settled | The zero-baseline rule is presented as a channel-theory requirement (area as a channel requires a zero reference), not a stylistic rule. |
| "Color luminance cannot encode categorical data" | Settled | Chapter 1 presents this from Munzner's taxonomy with the Bertin mechanism. |
| "AI tools hallucinate structural details" | Settled in practice | Chapter 4 names this as the Verification Gap. The Evergreen/Emery checklist is the audit instrument. |
| "Radar charts are always misleading" | Emerging consensus against | Chapter 13 presents the axis-order problem (a Bertin-class channel failure), not a general prohibition. |

---

## Aging Risk Audit

| Chapter | Aging risk | Stable core | Current-state content | Mitigation |
|---|---|---|---|---|
| 4 — Claude Code | HIGH | The MBTA iteration model; the Evergreen/Emery evaluation criteria; the Chapter 1 channel-theory vocabulary for prompts | Specific Claude Code interface and API | Frame workflow around principles, not menus. Date the chapter explicitly. |
| 13 — Specialized Charts | MEDIUM | Candlestick, Kagi, P&F as permanent domain conventions; the Cleveland & McGill position-vs-angle argument for bullet graphs | Any software-specific implementation | Channel-theory grounding makes the content durable; implementation via Claude Code abstracts the tool. |
| 1 — Marks & Channels | LOW | Bertin (1967), Cleveland & McGill (1986), Munzner (2014) — all foundational | None | No aging risk — the theoretical foundations are stable. |
| 5–12 — Taxonomy | LOW | Chart types are stable conventions; Friendly's origin stories are historical | D3 version-specific API calls | Claude Code abstracts D3 version; chart logic and channel theory are stable. |
| 14 — Design Principles | LOW | Tufte/Few/Cairo resolution; Gestalt principles; Evergreen/Emery checklist | None | The theoretical synthesis is stable. |
