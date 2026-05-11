# Chapter 2 — Chart Selection as Design Decision
*The Wrong Chart Feels Familiar; the Right One Takes Work.*

## Three suggested titles

- Chart Selection as Design Decision
- Cairo's Frame: Why Chart Choice Is a Moral Decision
- The FT Visual Vocabulary as Navigation, Not Law

---

## Chapter overview

By the end of this chapter you will be able to choose the right chart type for a given dataset and communication goal — using a four-step decision framework grounded in Cairo's ethical frame and the FT Visual Vocabulary. You will know the eight functional categories that any chart request resolves to, the perceptual and ethical reasoning that supports the choice, and the failure modes that produce charts which look fine and read wrong. You will leave with the vocabulary to commit to a chart type before any Claude Code prompt is written — turning Chapter 4's workflow into a reliable pipeline rather than a guessing game.

---

## Learning objectives

1. **(Understand)** Classify any chart request into one of eight functional categories — comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial — using the FT Visual Vocabulary as the framework.
2. **(Apply)** Use Cairo's four-step decision framework (key message → data structure → functional category → specific form) to select a chart type for a specified dataset and communication goal.
3. **(Evaluate)** Given two candidate chart types for the same data, justify the selection of one over the other using perceptual, historical, and ethical criteria — including Cairo's argument that an ineffective chart choice is a moral failure, not just an aesthetic one.
4. **(Analyze)** Identify the failure mode in a poorly chosen chart and specify the correct alternative, citing the specific perceptual mechanism the poor choice violates.

---

## Opening case — the 14-slice pie chart from a humanitarian report

A 2022 humanitarian report from a major NGO included a pie chart titled "Allocation of Emergency Response Funds, FY2021." The chart had fourteen slices. Each slice represented one funding category — food security, water and sanitation, shelter, health, protection, education, livelihoods, logistics, coordination, security, communications, transport, monitoring, and a residual "other." The slices ranged from 21% (food security) to under 1% (communications, transport, monitoring).

You can read the chart for thirty seconds and not be able to rank the categories from largest to smallest. The five smallest slices (each under 3%) compress into indistinguishable slivers along one edge. The two next-smallest slices (around 4–5%) look identical. The middle three slices (around 8–12%) are also nearly impossible to rank by angle.

This chart is not a stylistic failure. It is a failure of chart choice. The communication question — "how were the funds allocated, and which categories received the most?" — is a comparison question. The data attribute being shown (funding amount per category) is quantitative. The most important task the chart needs to support is *ranking* — the reader needs to be able to see which categories received the most and which received the least.

Pie charts encode magnitude as **angle**. Angle is fourth in the Cleveland & McGill perceptual ranking (Chapter 1), behind position-along-a-common-scale, position-along-non-aligned-scales, and length. For a comparison-and-ranking task, a chart that uses angle is using one of the worst available channels. Past five or six slices, the angle differences become too small to perceive reliably.

The right chart for the same data is a horizontal bar chart, sorted by funding amount descending. The same fourteen categories, the same percentages, but encoded on **position-from-baseline** — the highest-accuracy magnitude channel. The reader can rank the categories at a glance. Food security at 21% is unambiguously twice the size of shelter at 10.5%. The smallest categories are still small but distinguishable.

The pie chart was not a casual choice. The report was produced by a competent organization with experienced designers. The fourteen-slice pie chart appeared because pie charts are *familiar* — they are what people reach for when they have parts-of-a-whole data and want a chart. Familiarity is not a design criterion. It is a cognitive shortcut that produces predictable failures.

This chapter is about how to make chart choices that are not cognitive shortcuts. The framework is Cairo's four-step decision tree, the navigation tool is the FT Visual Vocabulary, and the criterion at every step is whether the chart honestly answers the communication question. A chart that misleads the reader is not just a bad chart — Cairo's argument is that it is a *moral* failure. The chapter walks the framework and applies the Cairo frame to specific examples.

---

## Theoretical grounding — Cairo, FT Visual Vocabulary, Friendly's history, Tufte's "show the data"

This chapter introduces four theoretical sources, each at the moment the reader has a problem the source solves.

**Alberto Cairo's ethical frame.** Cairo's argument, set out in *The Truthful Art* (2016) and refined in *How Charts Lie* (2019), is rule-utilitarian. When a designer chooses a chart type that produces a misleading visual reading of the data, the designer has not just made a stylistic mistake. They have impeded the reader's understanding. Choosing an ineffective chart "just because she likes it, while ignoring evidence that may lead her to choose a more appropriate one" is, in Cairo's terms, *morally wrong*. This is not overclaiming. Cairo's argument is careful and specific: the designer has a professional responsibility to the reader, and abdicating that responsibility for aesthetic preference is a moral choice with consequences.

The frame applies throughout this book. It is introduced here because chart selection is the first decision where the designer's choices have the largest moral weight. A poorly executed chart of the right form can usually be fixed with iteration. A well-executed chart of the wrong form has communicated something other than what the data supports — and "fixing" it requires going back to the chart-type choice, not the implementation.

**The Financial Times Visual Vocabulary.** The FT's data journalism team produced an internal taxonomy that organizes chart types into eight functional categories: comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial. (Some versions split or merge slightly — adding *deviation* as a separate category, or merging *flow* into *spatial*. The eight-category version is the standard.) The vocabulary is a navigation tool: it lets a designer locate the right region of the chart taxonomy before drilling down to a specific form.

The FT Visual Vocabulary is in this book's pantry (`pantry/Visual-vocabulary.txt`). Read it; print it; pin it to a wall. It is the working reference for Chapter 2 and recurs throughout Part II. The vocabulary is *navigation*, not *law*. It tells you where to look. The choice of specific form within a category — which kind of comparison chart, which kind of distribution chart — depends on the perceptual and ethical considerations the rest of this chapter walks.

**Michael Friendly's history of data visualization.** Every chart type in the standard taxonomy has an origin story. Playfair invented the bar chart and line graph (1786) to argue about British trade policy. Florence Nightingale invented the polar area chart (1858) to argue about preventable deaths in the Crimean War. Charles Joseph Minard invented the flow map (1869) for Napoleon's Russian campaign. John Snow invented the dot map (1854) to find the source of London's cholera outbreak. Baron Charles Dupin invented the choropleth (1826) to map French illiteracy. Ben Shneiderman invented the treemap (1991) to visualize disk usage with nested directories.

Each chart type was a *solution to a specific communication problem*. Knowing the original problem clarifies when the chart works. The choropleth was made for ratio data on bounded geographic units (illiteracy *rate* per French department, not absolute illiterate count). Use it for absolute counts and you produce the area-size distortion that Chapter 12 will name. The bar chart was made for comparison of independent categories (Playfair was comparing trade values across years and regions). Use it for parts of an unrelated whole and you import a comparison frame the data doesn't support.

Friendly's history (`pantry/Handbook of Data Visualization 2008 Friendly.txt`) is the comprehensive reference. The point for this chapter: chart selection is intellectual history, not menu navigation. Every chart type carries its origin's design intent forward, and using a chart against its original intent is the most common path to a chart that fails.

**Tufte's basic principle: "show the data."** This is the precondition for any chart-selection question. Before you choose a chart type, the chart has to *show* the underlying data — not summary statistics that hide the distribution, not a visual that obscures the values. Tufte's principle is introduced here because Chapter 5's bar-chart-of-means failure (showing only the mean of a bimodal distribution, hiding the bimodality) is a chart-selection failure: the wrong form was chosen, not just the wrong design within the right form. Tufte's principle returns in Chapter 14 as the foundation of the design audit.

---

## Concept 1 — The eight functional categories (FT Visual Vocabulary)

The first move in any chart-selection question is to identify the *functional category*. The FT Visual Vocabulary names eight, each defined by what the chart is trying to *show*. A chart request that doesn't fit any category is usually a chart request that hasn't been properly framed yet.

**1. Comparison.** Show how independent values or categories differ in magnitude. Bar charts, column charts, slope graphs, dot plots, radial bars (with reservations from Chapter 5). The defining question: "how do these compare?" The HAI AI capability bar chart (Chapter 5's worked example) is a canonical comparison chart.

**2. Change over time.** Show how a value or set of values evolves across a continuous temporal dimension. Line charts, area charts, stream graphs, Gantt charts, spiral plots, candlesticks. The defining question: "how is this changing?" Time on the x-axis (almost always); the quantitative variable on the y-axis.

**3. Distribution.** Show how values are spread, including frequency, central tendency, and skew. Histograms, density plots (KDE), box and whisker plots, violin plots, stem-and-leaf, strip plots. The defining question: "what does the distribution of this variable look like?"

**4. Relationship (correlation).** Show how two or more variables relate to each other. Scatterplots, bubble charts, parallel coordinates, heatmaps, connected scatterplots. The defining question: "are these variables related, and how?"

**5. Part-to-whole.** Show how components contribute to a single total. Pie charts (with restrictions), donut charts, waffle charts, Marimekko (mosaic) charts, treemaps, stacked bars (single bar with sub-segments). The defining question: "what makes up this total?"

**6. Hierarchy.** Show nested or layered structure. Treemaps, sunburst diagrams, circle packing, dendrograms, tree diagrams, icicle plots. The defining question: "how is this organized into levels?"

**7. Flow.** Show movement, transition, or transformation between states. Sankey diagrams, alluvial diagrams, chord diagrams, arc diagrams, flow maps. The defining question: "how does this move from A to B?"

**8. Spatial.** Show patterns tied to geographic location. Choropleth maps, dot maps, bubble maps, connection maps, flow maps (overlapping with category 7), cartograms. The defining question: "where is this happening?"

Some chart types appear in multiple categories. A flow map is both spatial and flow. A heatmap can be relationship (two categorical variables + intensity) or distribution (a 2D density). The categories overlap because the underlying data sometimes does. The point is not exclusive classification; the point is that locating your dataset in a category narrows the chart-type space from "any of 60+ options" to "any of 5–10 options within this category."

### How to identify the right category

The category is a function of the *communication question*, not of the data alone. The same dataset can support different categories depending on what you are trying to show.

Take a dataset of monthly humanitarian funding across five sectors over three years. The data attributes: month (temporal), sector (categorical), funding amount (quantitative). Three different communication questions, three different categories:

- "How has total monthly funding changed over the three years?" → **change over time**. A line chart of monthly totals.
- "Which sector received the most funding overall?" → **comparison**. A bar chart of cumulative funding per sector.
- "How is each year's total split across sectors?" → **part-to-whole**. A stacked bar chart, one bar per year, segmented by sector.

Same data, three categories, three charts. The chart type follows the question, not the table. This is why Chapter 3 (Reading a Dataset) emphasizes formulating the communication question *before* choosing a chart type — and why a dataset arriving without a framed question is the first thing to fix.

> ### ↳ Dig Deeper — The functional categories applied to your domain
>
> **Prompt:**
>
> > List five datasets typical of [my domain — e.g., epidemiology, financial analytics, customer behavior, climate science]. For each, identify which of the eight functional categories it most naturally fits. Note any datasets that fit two or three categories — and for those, name the communication question that resolves the choice. Use the FT Visual Vocabulary as the navigation tool.
>
> **What to do with the output:** Save the mapping. The functional category is the entry point to every later chapter; this exercise builds the muscle memory of locating any dataset in the taxonomy quickly.

---

## Concept 2 — Cairo's four-step decision framework

Cairo's decision framework moves from the abstract to the concrete in four steps. Each step closes off a class of bad choices. By step 4, the chart type is named.

**Step 1: Key message.** What does the reader need to understand in 5 seconds? Write it as a single sentence. "Funding for food security is twice the next-largest category." "Refugee flows from Country X have shifted from Country Y to Country Z over five years." "Hospital admissions cluster in three age groups, not a smooth distribution." If you cannot write this sentence, you do not yet have a chart — you have a dataset and a hope.

**Step 2: Data structure.** What kind of data do you have? Categorical, ordinal, quantitative, temporal, geographic. How many variables? How many observations per category? Is there a hierarchy? Is there a flow between states? Step 2 is the descriptive audit Chapter 3 will walk in detail.

**Step 3: Functional category.** Given the message and the structure, which of the eight functional categories applies? This is the FT Visual Vocabulary lookup. If the message is comparative and the data is categorical with one quantitative variable, the category is comparison. If the message is about composition and the data sums to a meaningful total, the category is part-to-whole. The category narrows the chart space.

**Step 4: Specific form.** Within the category, which specific chart? Comparison gives you bar/column/multiset/stacked/radial. Part-to-whole gives you pie/donut/waffle/treemap/Marimekko. The choice depends on perceptual and design criteria the rest of Part II walks. For chart selection at this stage, the reasonable defaults are:

- Comparison → bar (long labels) or column (short labels), with sort by value.
- Change over time → line (multi-series) or area (single cumulative measure).
- Distribution → histogram (n > 50, single variable) or box plot (cross-group comparison).
- Relationship → scatterplot (two quantitative variables) or heatmap (two categorical + intensity).
- Part-to-whole → bar chart (single bar, segmented) or waffle chart (≤5 categories) before pie chart.
- Hierarchy → treemap (regular depth) or circle packing (irregular depth).
- Flow → Sankey (proportional flow) or chord (inter-entity).
- Spatial → choropleth (rate/ratio data) or bubble map (absolute values).

These defaults are not absolute. Specific forms get their full treatment in Chapters 5–13. The point of step 4 at this stage is to land on a candidate; the candidate gets refined through the design considerations of the relevant chapter.

### Worked example — the humanitarian funding dataset

Apply the four steps to the opening case.

**Step 1 — Key message.** "Of the fourteen funding categories, food security received the largest share at 21%, more than twice the next-largest category."

**Step 2 — Data structure.** Categorical variable (funding category, 14 values, no inherent order). Quantitative variable (funding amount, 0–100% as percentage). One observation per category.

**Step 3 — Functional category.** The data sums to 100% (it's a budget allocation). The natural category is part-to-whole. *But:* the message is comparative — the reader needs to rank categories by size. When part-to-whole and comparison overlap in the message, the comparison structure dominates if ranking is what the reader needs to do. The de facto category is **comparison**.

**Step 4 — Specific form.** Comparison + 14 categories + long-ish labels (8–17 characters) → horizontal bar chart, sorted by funding amount descending. The bar lengths use position-from-baseline (the highest-accuracy channel). The 14 categories fit comfortably as horizontal bars. Adding the percentage values as annotations supports precise reading where the bar length doesn't (the smallest categories are visible but their exact values matter).

The pie chart in the original report fails at step 3 — the message dominates over the part-to-whole frame, and the comparison structure should have led to a bar chart. Cairo's frame applies: the pie chart was chosen for familiarity, not for the message. The choice impeded the reader's understanding. The choice was, in Cairo's terms, morally wrong.

> ### ↳ Dig Deeper — Apply Cairo's four steps to a chart you produced
>
> **Prompt:**
>
> > Take a chart I produced recently and walk it backward through Cairo's four-step decision framework. Did I have a key message? Did I read my data structure? Did I correctly identify the functional category? Did I choose the right specific form within it? Where my chart fails one of these steps, name the failure and specify the redesign. Apply the Cairo ethical frame: was my choice driven by the message, by familiarity, or by the software's defaults?
>
> **What to do with the output:** Save the audit. The pattern reapplies to every chart you produce.

---

## Concept 3 — Common chart-selection failures

Three failure modes recur in chart selection. Each fails one of Cairo's four steps. Each has a specific corrective.

### Familiarity bias

The designer reaches for the chart they always use, regardless of whether it fits the question. Pie charts because pie charts are familiar. Bar charts because bar charts work. Line charts because line charts are what the dashboard tool offers.

The corrective is step 3: locate the dataset in the FT Visual Vocabulary. The familiar chart is sometimes still right — but if it is right, it is right because it fits the category, not because it is familiar. The 14-slice pie chart from the opening case is the familiarity-bias failure: pie charts are part-to-whole, but the message dominates and the right form is comparison.

### Aesthetic-first choice

The designer reaches for the chart that looks impressive — radial bars instead of linear, 3D perspective instead of flat, animated transitions instead of static. The aesthetic choice has nothing to do with whether the chart answers the question.

The corrective is step 1: write the key message. If the chart cannot serve the message because the aesthetic obscures the data, the aesthetic is wrong. Tufte's "show the data" principle applies: any visual element that does not serve the data is by default a candidate for removal. (This is the strict reading. Few's resolution from Chapter 5 — that embellishments which support the message can earn their place — applies; the test is whether the aesthetic *serves* or *obscures*.)

### Software-default choice

The designer accepts whatever the charting tool produces by default. PowerPoint's default chart, the Excel SmartArt template, the Tableau auto-suggestion, the BI dashboard template. Each of these has implicit choices baked in (truncated y-axes for emphasis, gradient fills for visual interest, default rainbow palettes for categorical encoding) that a real chart-selection process would override.

The corrective is to override the defaults consciously. The four-step framework is the override discipline. Do the steps before the chart is built; the chart will then differ from the default in specific, defensible ways.

### Cairo's ethical frame applied

Each failure mode has an ethical dimension in Cairo's reading. The familiarity-bias designer impedes understanding because they did not engage with the message. The aesthetic-first designer impedes understanding because they prioritized their preferences over the reader's needs. The software-default designer impedes understanding because they did not exercise judgment.

Cairo's frame is not "every bad chart is morally wrong." It is "when a designer chooses an ineffective chart while a more appropriate one is available, the choice is morally significant." The book adopts this frame. It does not produce moral panic about every imperfect chart. It produces *responsibility* — the designer's professional obligation to the reader is to make the chart-choice that the message and data support.

> ### ↳ Dig Deeper — When familiarity is right
>
> **Prompt:**
>
> > Argue both sides of the question: when is reaching for a familiar chart type (bar chart, line chart, pie chart) the right choice, and when is it the failure mode of familiarity bias? Cite Cairo's frame on both sides. Identify two or three contexts in which familiarity is the *correct* design criterion (audience graphicacy, time pressure, established convention) and the perceptual cost is worth paying.
>
> **What to do with the output:** Save the analysis. The chartjunk debate (Chapter 14) will revisit the same trade-off in design-element terms.

---

## Concept 4 — The "compared with what?" check

Cairo introduced "compared with what?" as a mandatory check before any chart is finalized. The phrase is borrowed from social science (Stanley Lieberson) and from W. Edwards Deming (the question every quality-control analyst should ask). For chart design, it means: every quantitative claim a chart makes must be set against a reference — explicit or implicit — that gives the claim meaning.

A bar chart of "Q4 revenue per region" makes a quantitative claim about each region. *Compared with what?* The other regions, comparing them to each other (within-chart comparison). Q3 revenue (year-on-quarter comparison). The same quarter last year (year-on-year comparison). The annual target (target comparison). Each of these is a different chart, because each is a different "compared with what" answer.

The check forces the designer to name the comparison the chart actually makes. A chart that fails the check makes a claim without a reference and produces a meaningless reading.

### Common failures of "compared with what?"

**Absolute counts where ratios are needed.** A choropleth of "absolute kidnappings per state" has no comparison built in — large states automatically have higher counts, and the visual color gradient tracks population, not crime rate. The fix: rate per capita (kidnappings per 100,000 residents), or kidnappings as a percentage change from the national average. The comparison is now explicit.

**Time series without baseline.** A line chart of "stock price over five years" makes a claim about price change, but compared with what? The market average (S&P 500 in the same period). The sector average. Inflation-adjusted. Each comparison reveals different information and is sometimes the right one.

**Cross-sectional comparison without controls.** A bar chart of "average income by region" makes a claim about income, but compared with what? Cost of living. Education levels. Industry composition. Without the right control, the chart shows differences that may be artifacts of the missing comparison.

The check is part of step 1 (key message). The key message is incomplete if it does not name the comparison. "Funding for food security is highest" is incomplete; "funding for food security is highest, more than twice the next-largest category" makes the comparison explicit. The chart then encodes the comparison the message demands.

---

## Mid-chapter checkpoint

Pick a chart you have produced or seen recently. Walk it through Cairo's four-step framework. (1) Can you write its key message in one sentence? (2) What data structure does it have? (3) Which functional category does the message fit? (4) Is the specific form within that category the best fit, or could a different form within the same category serve better?

Then apply the "compared with what?" check. Is the comparison the chart makes explicit? If you change the comparison frame (rate instead of count, year-on-year instead of within-period), does the chart change?

If the chart fails any step, sketch the redesign.

---

## Extended worked example — selecting a chart for the humanitarian funding dataset

The dataset: monthly humanitarian funding amounts across five sectors (food, shelter, water, health, protection) for one country across three years (2022–2024).

### Three communication questions, three charts

**Question 1: "How has total monthly funding changed across the three years?"**

- Step 1 — Key message: "Total monthly funding peaked in mid-2023 and has declined through 2024."
- Step 2 — Data structure: Aggregate the dataset to monthly totals. One quantitative variable (total funding) over time (36 months).
- Step 3 — Functional category: change over time.
- Step 4 — Specific form: line chart. Single line. Months on the x-axis (continuous), funding on the y-axis (quantitative, zero baseline if the variation is large enough; otherwise non-zero is acceptable for line charts because the channel is point position, not bar length).

**Question 2: "Which sector received the most funding cumulatively?"**

- Step 1 — Key message: "Food security received the largest share of cumulative funding (38%), more than the next two sectors combined."
- Step 2 — Data structure: Aggregate to total funding per sector (5 values).
- Step 3 — Functional category: comparison.
- Step 4 — Specific form: horizontal bar chart, sorted by cumulative funding descending. Sector names on the y-axis, funding on the x-axis (zero baseline).

**Question 3: "How does each year's total split across sectors?"**

- Step 1 — Key message: "Food security's share has grown from 32% in 2022 to 41% in 2024 at the expense of protection and water."
- Step 2 — Data structure: 5 sectors × 3 years = 15 values, with totals per year.
- Step 3 — Functional category: part-to-whole, with a temporal dimension.
- Step 4 — Specific form: stacked column chart, one column per year, segmented by sector. Or, equivalently, a 100% stacked column chart if the message is about *proportion* rather than absolute levels. The latter normalizes the totals to 100%, making proportions directly comparable across years.

The same dataset has produced three different charts because three different questions have been asked. None of the three charts is the "right chart for this data." All three are right for their respective questions; none is right for the others. The chart is the answer to the question.

### Where Claude Code enters

Once the chart type is named (the four steps complete), the chart specification follows the Chapter 1 framework: marks, channels, design constraints. The Claude Code prompt follows the Chapter 00 four-move structure. A worked prompt for Question 2:

```
**Show what I have:**
5 rows. Each row has `sector` (string) and `cumulative_funding`
(number, USD millions). Sample:
  Food Security, 380.2
  Shelter, 142.7
  Water, 98.4
  Health, 87.3
  Protection, 64.1

**Say what I want:**
Horizontal bar chart in D3 v7. Single HTML file with inline CSS and
inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: rectangles, one per sector.
- y-position: sector (categorical, sorted by cumulative_funding
  descending).
- x-position from zero baseline: cumulative_funding (quantitative).
  Zero baseline non-negotiable.
- Color luminance redundantly encoding cumulative_funding (sequential
  pale-to-dark).
- x-axis ticks at $0, $100M, $200M, $300M, $400M.
- Cumulative funding values labeled at the right of each bar.
- Subtitle: "FY2022-2024 Cumulative Humanitarian Funding by Sector
  (USD millions)".
- Margins: top 60, right 80, bottom 40, left 140 (left margin
  accommodates sector labels).
- Dark mode support via prefers-color-scheme.

**Verify:**
Before writing the code, restate the channel decomposition. Then write
D3 v7 with comments showing which line implements which channel. Flag
any decisions not specified.
```

The prompt is precise because the four steps were done first. Without the four steps, the prompt is "show this data as a chart" — and Claude Code will choose, often badly. The four-step framework is what turns chart selection into a designer skill rather than a generator's guess.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can locate any chart request in the FT Visual Vocabulary's eight functional categories — comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial — and use the location to narrow the chart-type space from "any of 60+" to "any of 5–10."

You can apply Cairo's four-step decision framework (key message → data structure → functional category → specific form) to land on a chart type that is defensible, not merely familiar. You know that step 1 (key message) is the load-bearing step; without it, the rest of the framework fails.

You can diagnose three common chart-selection failures — familiarity bias, aesthetic-first choice, software-default choice — and you know each is fixable by re-engaging the four-step framework rather than by retroactively fixing the chart.

You can apply Cairo's "compared with what?" check to ensure that every chart makes its comparison explicit. You know that absolute counts where ratios are needed, time series without baselines, and cross-sectional comparisons without controls are the recurring failures of this check.

The thing to watch for, going forward, is the temptation to skip the four steps. Most charts you produce will be variations of bar charts, line charts, or scatterplots — the forms are familiar. The four-step framework is most valuable on the charts you do not immediately know how to do, and on the charts you think you know how to do. Every later chapter applies the framework to its specific chart family; the discipline starts here.

---

## Key terms

- **Functional category.** One of eight (FT Visual Vocabulary): comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial. The first move in chart selection.
- **Cairo's four-step decision framework.** Key message → data structure → functional category → specific form. The decision tree this chapter teaches.
- **Cairo's ethical frame.** When a designer chooses an ineffective chart while a more appropriate one is available, the choice is morally significant — not just aesthetically.
- **"Compared with what?"** Cairo's mandatory check before finalizing any chart. Every quantitative claim must be set against an explicit reference.
- **Familiarity bias.** Reaching for a familiar chart type regardless of fit. The most common chart-selection failure.
- **The FT Visual Vocabulary.** The Financial Times' chart taxonomy, used here as the navigation tool. Available in the book's pantry as `Visual-vocabulary.txt`.
- **Friendly's history.** Michael Friendly's history of data visualization, used to ground every chart type in its origin and original communication problem. In the pantry as `Handbook of Data Visualization 2008 Friendly.txt`.
- **Tufte's "show the data" principle.** The first test any chart must pass: it must let the reader see the underlying values, not summary statistics that hide the distribution.

---

## Discussion questions

1. The 14-slice pie chart from the opening case was produced by a competent designer. Why? Apply the three failure modes from Concept 3 to predict which one drove the choice.
2. Cairo's "morally wrong" framing of bad chart choices is stronger than most contemporary writing on visualization. Make the case for and against the strength of this frame. Where does it land you?
3. The FT Visual Vocabulary names eight categories. Some chart types (heatmaps, flow maps, candlesticks) appear in multiple categories. Why do they overlap, and what does the overlap suggest about the limits of category-based chart selection?
4. Pick a published dashboard or report that uses many charts (corporate annual report, government statistical release). Audit five charts using the four-step framework. How many pass step 1 (key message) cleanly, and how many appear to have skipped it?
5. *Cross-chapter synthesis.* Chapter 14 will introduce the Tufte/Few/Cairo synthesis as the design-audit framework. Frame the relationship between this chapter's chart-selection framework and Chapter 14's design audit: where do they overlap, and where does each do work the other does not?

---

## Exercises

### Warm-up

**Exercise 2.1** — *Functional category lookup.* For each of the following datasets, name the most likely functional category from the FT Visual Vocabulary. Where multiple categories could apply, name the communication question that would resolve the choice.
- Monthly visitors to a website over two years.
- Distribution of household incomes in a single ZIP code.
- The relationship between hours studied and test score for 200 students.
- The breakdown of a city's annual budget into 9 departments.

**Exercise 2.2** — *Apply the four-step framework.* Walk a recent dataset of yours through the four steps. Write down each step's output: key message, data structure, functional category, specific form. Submit as a short markdown document.

**Exercise 2.3** — *"Compared with what?" diagnosis.* Find a chart in a recent newspaper or report that fails the "compared with what?" check (absolute counts, no baseline, missing control). Specify the redesign that fixes the failure.

### Application

**Exercise 2.4** — *Three charts from one dataset.* Take a dataset with at least three meaningful communication questions (the humanitarian funding example in this chapter is a model). Walk each question through the four-step framework. Produce three different chart specifications. Build the charts with Claude Code. Compare them.

**Exercise 2.5** — *Audit a dashboard.* Find a public dashboard (city open-data portal, public health dashboard, financial market visualization). Audit ten charts using the four-step framework. Categorize each by which step (if any) was skipped. Rank the dashboard's overall chart-selection discipline.

**Exercise 2.6** — *The familiarity-bias rewrite.* Find a pie chart with more than five slices (these are abundant in corporate reports). Apply Cairo's framework. Rewrite as a horizontal bar chart with sort by value. Build both with Claude Code. Compare reading speed and accuracy with two colleagues.

### Synthesis

**Exercise 2.7** — *Cairo's ethical frame applied.* Take a chart from a recent published report whose chart choice you suspect is wrong. Apply the four-step framework to identify what should have been chosen. Write a one-page "ethics audit" applying Cairo's frame: was the choice driven by the message, by familiarity, or by the software's defaults? What did the designer's choice impede in the reader's understanding?

**Exercise 2.8** — *FT Visual Vocabulary in your domain.* Take five datasets typical of your professional work. For each, identify the functional category and the recommended specific form. Build a one-page reference card you can pin to your wall. Cite the perceptual reasoning for each form choice.

### Challenge

**Exercise 2.9** — *Friendly's history applied.* Pick a chart type that you use frequently. Look up its origin (when invented, by whom, for what original communication problem). Compare your typical use to the original use. Where are you using the chart against its original intent? Where does the original intent illuminate why your chart sometimes fails?

**Exercise 2.10** — *Multi-LLM chart selection.* Submit the four-step framework prompt for a contestable dataset to Claude, ChatGPT, and Gemini. Compare the chart-type recommendations. Where do they agree? Where do they disagree? What does the disagreement reveal about which design decisions are genuinely contestable in your domain?

---

## LLM Exercise — Chapter 2: Chart Selection

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A chart-selection audit document that walks a real dataset through Cairo's four-step framework and produces a defensible chart-type recommendation. Plus the Claude Code prompt for the recommended chart.

**Tool:** Claude chat (for the audit) + Claude Code (for the build)

---

**The Prompt:**

```
I have a dataset of [DESCRIBE: rows, columns, types]. The communication
goal is [DESCRIBE: what the reader needs to understand in 5 seconds].

Walk me through Cairo's four-step chart-selection framework:

1. Key message: write the message as a single sentence. If I cannot
   write it, push back and ask for it before proceeding.

2. Data structure: name the data types, the number of variables and
   observations, any hierarchy, any temporal dimension.

3. Functional category: locate the dataset in the FT Visual Vocabulary's
   eight functional categories (comparison, change over time, distribution,
   relationship, part-to-whole, hierarchy, flow, spatial). Where multiple
   categories could apply, name the question that resolves the choice.

4. Specific form: recommend a specific chart type within the category.
   Cite the perceptual reasoning (Cleveland & McGill ranking from
   Chapter 1) and any chart-family-specific design considerations.

Then apply the "compared with what?" check: name the comparison the
chart will make explicit. If the comparison is missing, name it.

Then identify whether the recommendation is at risk of any of the three
failure modes from Chapter 2 — familiarity bias, aesthetic-first choice,
software-default choice. Audit yourself: am I recommending this chart
because the message demands it, or because it's familiar?

Save the audit as chapter-02-selection-audit.md. Then write a four-move
Claude Code prompt for the recommended chart, following the Chapter 00
prompt structure.
```

---

**What this produces:** A markdown audit document with Cairo's four steps walked through, the "compared with what?" check applied, and a four-move Claude Code prompt ready to run. Save as `chapter-02-selection-audit.md`.

**How to adapt this prompt:**
- *For your own domain:* Replace the dataset and communication goal.
- *For ChatGPT / Gemini:* Works as-is. Both will accept the four-step structure.
- *For a Claude Project:* Save Cairo's four-step framework and the FT Visual Vocabulary as system-prompt context; the per-chart audit becomes the user message.
- *For Cowork:* Use Cowork to read the dataset file directly, then run the audit; saves a paste step.

**Connection to previous chapters:** Builds on Chapter 1 (channel ranking grounds the perceptual reasoning at step 4). Chapter 00's four-move prompt structure is what the audit's final output is. Future chapters' LLM Exercises assume this audit has happened first.

**Preview of next chapter:** Chapter 3 zooms in on step 2 (data structure) and step 1 (key message). The pre-chart-type work — distinguishing the analyst's question from the reader's question, framing "compared with what?" against the actual data — is the focus.

---

## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. Where a figure also appears in Part II as a stand-alone reference chapter, the link is provided; the prompt below is tuned to the chart-selection pedagogy this chapter introduces.

For chart-type references the chapter mentions in passing, see Part II directly: [Bar Chart](20-bar-chart.md), [Pie Chart](53-pie-chart.md), [Line Graph](43-line-graph.md), [Treemap](75-treemap.md), [Choropleth](29-choropleth.md), [Heatmap](39-heatmap.md), [Sankey Diagram](62-sankey-diagram.md), [Stacked Bar](67-stacked-bar.md), [Donut Chart](33-donut-chart.md), [Bubble Map](25-bubble-map.md), [Marimekko Chart](44-marimekko-chart.md), [Chord Diagram](28-chord-diagram.md), [Circle Packing](30-circle-packing.md), [Nightingale](48-nightingale.md), [Candlestick Chart](27-candlestick-chart.md). Each Part II chapter has its own prompt.

### Figure 2.1 — The 14-slice pie chart and its bar-chart fix

The opening-case figure. Two panels side by side: a 14-slice pie chart from a humanitarian funding report (the failure case) and the same data redrawn as a sorted horizontal bar chart (the fix). The chapter's argument made visible — same data, perceptually different chart, dramatically different reading speed.

```
Generate a single HTML page in D3 v7 with two side-by-side panels. Two files:

1. `chapter-02-fig-01.html` — full HTML with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). Two SVG panels in a flex layout, responsive on resize. Page subtitle: "Same data, two encodings — angle vs. length."

2. `chapter-02-fig-01/data.json` — the dataset.

Data shape:
- 14 humanitarian-funding categories with one quantitative attribute each.
  - `category`: string — sector name (Food Security, Shelter, WASH, Protection, Health, Education, Logistics, etc.)
  - `value`: number — percentage of total funding (sums to 100)

{DATA NEEDED} — A real or representative humanitarian-funding breakdown by sector, 14 categories. Sources include OCHA Financial Tracking Service (FTS), UNHCR funding reports, or any published humanitarian appeal sector breakdown.

Left panel — pie chart (failure case):
- 14 slices, angle encodes value.
- Default rainbow color palette across the 14 slices.
- Tiny detached legend with 14 entries.
- This panel is intentionally hard to read; do not "fix" the encoding.

Right panel — sorted horizontal bar chart (fix):
- 14 bars, length encodes value, sorted descending.
- Single-hue walnut palette (no per-category color).
- Direct labels on each bar with the value.
- Same total chart area as the pie panel.

Both panels labeled with the channel decomposition in a small caption box. Annotate the page with the 5-second reading test: which panel can the reader rank top-3 sectors faster?

Style: warm monochrome — black, dark walnut, blood-red accents. Serif body, JetBrains Mono for labels.

Provide both files as separate code blocks.
```

### Figure 2.2 — The FT Visual Vocabulary 8-category matrix

A reference figure showing the eight functional categories from the Financial Times Visual Vocabulary (Comparison, Composition, Distribution, Relationship, Hierarchy, Flow, Spatial, Change-over-time) with one canonical chart per category. The figure is the navigation tool the chapter teaches.

```
Generate an 8-panel grid in D3 v7 showing one canonical chart per FT Visual Vocabulary functional category. Two files:

1. `chapter-02-fig-02.html` — full HTML with inline CSS and inline D3 v7. A 4×2 grid of small SVG panels, each ~200×150 px, each rendering one canonical chart of its category. Page subtitle: "FT Visual Vocabulary — eight functional categories."

2. `chapter-02-fig-02/data.json` — eight small datasets, one per panel.

Data shape (one per category):
- `comparison`: 6 bar values
- `composition`: 5 stacked-bar values summing to 100
- `distribution`: 80 simulated values for a histogram
- `relationship`: 30 (x,y) scatterplot points
- `hierarchy`: nested tree of 12 nodes for a small treemap
- `flow`: 4-node Sankey with 5 links
- `spatial`: 8 (lat, lon) points for a tiny world dot map
- `change_over_time`: 24 monthly line-chart values

{DATA NEEDED} — Themed humanitarian-data examples for each panel work well: comparison (sector funding), composition (refugee origin breakdown), distribution (response times), relationship (GDP vs. life expectancy), hierarchy (UN agency org chart), flow (aid corridor volumes), spatial (delivery hubs), change-over-time (monthly displacement).

Each panel:
- Title above (10pt, JetBrains Mono, uppercase).
- Mini chart with axes if appropriate; no decoration beyond the chart itself.
- Caption below naming the category.
- One example annotation per panel ("compares values across categories", "shows joint distribution", etc.).

Style: warm monochrome. Each chart uses the same walnut palette so the matrix reads as a unified reference, not eight different visual styles.

Provide both files as separate code blocks.
```

### Figure 2.3 — Three failure modes diagrammed

A three-panel illustration of the chapter's named failure modes: familiarity bias (defaulting to pie/bar), aesthetic-first selection (3D rendering or "look pretty" defaults), and software-default selection (whatever Excel produces). Each panel shows a real chart-selection failure followed by the correction.

```
Generate a 3-panel before/after illustration in D3 v7. Two files:

1. `chapter-02-fig-03.html` — full HTML with inline CSS and inline D3 v7. Three rows; each row has a "before" chart on the left and an "after" chart on the right. Page subtitle: "Three failure modes — familiarity bias, aesthetic-first, software-default."

2. `chapter-02-fig-03/data.json` — three datasets.

Data shape:
- `familiarity`: 8 categories with values; the "before" is a 3D pie, "after" is a sorted bar chart.
- `aesthetic`: 12 categories with values; the "before" is a radial bar (decorative), "after" is a sorted horizontal bar.
- `software_default`: a time series with 7 series; the "before" is a line chart with all 7 series at once (default Excel behavior), "after" is small multiples (one panel per series).

{DATA NEEDED} — Any three datasets that fit the three failure-mode patterns. The chapter's humanitarian-funding example serves the familiarity case; a 12-month delivery dataset serves the aesthetic case; a 7-series operational-metric dataset serves the software-default case.

Each row's caption names the failure mode and the perceptual mechanism that corrects it.

Style: warm monochrome. The "before" charts are intentionally compromised; do not improve them.

Provide both files as separate code blocks.
```

### Figure 2.4 — Cairo's four-step framework as a flow diagram

A single panel rendering Cairo's four-step decision framework as a labeled flow with branches: data attributes → communication question → chart-type candidates → channel decomposition. The figure is the chapter's framework made literal.

```
Generate a single-panel decision-flow diagram in D3 v7. Two files:

1. `chapter-02-fig-04.html` — full HTML with inline CSS and inline D3 v7. The panel is a labeled flow with 4 stages, each with branches. Page subtitle: "Cairo's four-step framework — what the data has, what the reader needs, which charts qualify, which channels carry the weight."

2. `chapter-02-fig-04/data.json` — the framework's 4 stages with branches.

Data shape:
- Four stages, each with name, description, and 3–5 branch options.
- Stage 1: "Data attributes" — branches: categorical / ordered / quantitative / spatial / temporal.
- Stage 2: "Communication question" — branches: comparison / composition / distribution / relationship / change-over-time / hierarchy / flow / spatial.
- Stage 3: "Candidate chart types" — branches: bar / line / pie / scatter / treemap / choropleth / sankey / etc.
- Stage 4: "Channel decomposition" — branches: position / length / area / hue / luminance.

The diagram is rendered as labeled boxes with arrows. Layout left-to-right; branches stack vertically within each stage. Use `d3.tree()` or manual placement; the geometry is not the teaching point — the labels and the flow are.

Style: warm monochrome. Boxes have walnut borders with light cream fill. Arrows blood-red where they show the worked example's path through the framework.

Provide both files as separate code blocks.
```

---

## Further reading

- **Cairo, Alberto. (2016).** *The Truthful Art: Data, Charts, and Maps for Communication.* New Riders. Read Chapters 1–3 for the ethical frame; Chapter 5 for chart selection in depth.
- **Cairo, Alberto. (2019).** *How Charts Lie: Getting Smarter About Visual Information.* W. W. Norton. The accessible companion to *The Truthful Art*. Chapter 2 ("Charts That Lie by Showing Too Little") is most relevant here.
- **The Financial Times Visual Vocabulary.** Available in the book's pantry (`pantry/Visual-vocabulary.txt`) and online at ft.com/visual-vocabulary. Print it. Pin it.
- **Friendly, Michael. (2008).** "A Brief History of Data Visualization." In *Handbook of Data Visualization*, edited by C. Chen, W. Härdle, and A. Unwin. Springer. The origin stories that ground chart-type choice.
- **Tufte, Edward R. (1983, 2nd ed. 2001).** *The Visual Display of Quantitative Information.* Chapter 1 establishes "show the data" as the foundational principle.
- **Few, Stephen.** *Show Me the Numbers: Designing Tables and Graphs to Enlighten.* The most rigorous practical chart-selection reference. Few's chapter on selecting the right chart is the deepest treatment of the four-step decision in book form.

---

## Tags

chart-selection, Cairo, ethical-frame, FT-visual-vocabulary, eight-functional-categories, four-step-framework, compared-with-what, Tufte-show-the-data, Friendly-history, familiarity-bias, aesthetic-first-choice, software-default, D3, Claude-Code, chart-taxonomy
