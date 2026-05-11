# Chapter 5 — Comparison Charts
*Length Along a Shared Baseline Is the Honest Channel.*

## Three suggested titles

- Comparison Charts: Bar, Column, Multiset, Stacked, Radial
- Why Bar Charts Win — and When the Zero-Baseline Rule Is a Moral Decision
- The Workhorse of the Taxonomy

---

## Chapter overview

By the end of this chapter you will be able to build the entire family of comparison charts — bar, column, multiset (grouped), stacked, radial — and you will know when each is right and when each misleads. You will know why position-along-a-common-baseline is the highest-accuracy channel for quantitative comparison (Cleveland & McGill 1986), why the zero-baseline rule is grounded in area-as-channel theory (and why violating it is a moral failure in Cairo's frame, not just an aesthetic one), and how to specify a comparison chart precisely enough for Claude Code to produce a perceptually honest output on the first attempt.

---

## Learning objectives

1. **(Apply)** Build a bar chart, multiset (grouped) bar chart, and stacked bar chart for the same dataset using Claude Code; explain when each is appropriate using the Few/Evergreen design checklist criteria.
2. **(Analyze)** Diagnose a truncated-axis bar chart for proportional ink violations, citing the Weissgerber et al. *PLOS Biology* (2015) finding that more than 88% of biological research articles contain a bar-graph error of this class.
3. **(Evaluate)** Justify the choice between horizontal and vertical bar orientation for a given label structure and category count, using Gestalt proximity and continuity as the perceptual mechanism behind the choice.

---

## Opening case — the AI adoption bar chart from the Humanitarians AI pantry

Open `pantry/visualization/bar-chart.html` in a browser. Eight cognitive domains line up along the x-axis: Pattern Recognition, Language, Memory Retrieval, Causal Reasoning, Moral Judgment, Creativity, Embodied Teaching, Empathy. Each has a column rising to its score on the y-axis (0–100). Memory Retrieval at 96 is the tallest. Embodied Teaching at 35 is the shortest. Color luminance reinforces the ranking — pale tan at the low end, deep red at the high. The y-axis starts at 0 and ticks at 25, 50, 75, 100. The x-axis labels rotate -30° to fit the long domain names.

You can read the entire ranking in less than a second. You can also tell, without reading the values, that Memory Retrieval and Pattern Recognition are nearly tied, that Causal Reasoning at 62 and Creativity at 71 separate clearly, and that there's a substantial gap between the strongest cognitive domain (96) and the weakest (35).

Walk through every design decision the chart makes, and what each decision is doing for the reader.

**Vertical column orientation.** The category names are 12–17 characters. They could fit horizontally with rotation, which is what the chart does (-30°), or they could go on the y-axis as horizontal bars. Both are defensible; the chart picks vertical because eight categories at vertical-with-rotated-labels reads cleanly within a dashboard tile and the cultural convention for "bar chart" is vertical. Gestalt continuity is at work: the eye reads horizontally across the rotated labels and vertically up each column, two perpendicular reading paths that don't interfere.

**Zero baseline.** The y-axis starts at 0. The bars are area marks, and area is a magnitude channel — *the visual area of the bar is the data signal*. If the baseline started at, say, 30 (where the lowest value sits), the bars would no longer represent the score. They would represent the score minus 30. The reader's perceptual machinery, calibrated to "longer bar = larger value," would now produce a wrong reading.

**Color luminance as redundant encoding.** The score is encoded twice — once on bar height (position-from-baseline, the highest-accuracy channel from Cleveland & McGill 1986) and once on color luminance (a magnitude channel ranked sixth). The redundancy is intentional. Position carries the information; luminance reinforces the ranking and supports color-blind readers and casual scanning. This is *not* chartjunk in Tufte's sense — it is functional redundancy in Few's sense, an embellishment that supports the message without distorting it. Few's position on the chartjunk debate (`pantry/the_chartjunk_debate.txt`): the criterion is "does this support the message?" not "does this minimize ink?"

**Sort by value descending.** The categories have no inherent order (the eight cognitive domains are not on any natural scale). The chart sorts them by score so the reader gets a ranking the data does not impose. This is a Munzner effectiveness move: when an order is meaningful and the data does not impose one, derive an order from the most important attribute.

Each design decision is doing visible work for the reader. None is decorative. The chart took perhaps 70 lines of D3 to build; what makes it good is not the code but the channel decomposition the code implements. You can describe the channel decomposition in a hundred words. Claude Code can then write the seventy lines.

---

## Theoretical grounding — the sources that ground each design rule in this chapter

**Cleveland & McGill (1986).** Bar charts are the most accurate form for quantitative comparison because they use position-along-a-common-scale, the highest-ranked channel. Subsequent replications (Heer & Bostock 2010) confirm this for the contemporary D3 era. Every "prefer bars" claim in this chapter rests on the empirical ranking, not on aesthetic preference.

**Tufte's proportional ink principle (1983, refined since).** The visual area of a chart element must be proportional to the data value it represents. Bar charts use area as a magnitude channel; truncating the y-axis violates the proportionality. Tufte's principle is the *heuristic*. The empirical evidence that supports it comes from psychophysical work on how the eye perceives area (Stevens' power law, introduced in Chapter 1).

**Weissgerber, Milic, Winham, and Garovic (2015).** "Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm." *PLOS Biology* 13(4). The paper analyzed over 700 biology research articles and found that more than 88% contained at least one bar graph error. The most common errors: hiding the underlying distribution (a bar chart of mean values when the data is bimodal or skewed), using bar charts for paired data (where a paired-difference plot would show the relationship), and yes — truncated y-axes. The Weissgerber finding is the empirical basis for treating the zero-baseline rule as a non-trivial discipline rather than a stylistic flourish.

**Pandey, Rall, Satterthwaite, Nov, and Bertini (2015).** "How Deceptive Are Deceptive Visualizations?" *CHI '15.* Controlled experiments on truncated y-axes and other distortions. Subjects were shown either honest charts or distorted versions and asked to rate the magnitude of differences. The truncated charts produced systematically inflated subjective ratings — readers rated small differences as large when the y-axis was truncated. The mechanism that Tufte's principle predicts is the mechanism the experiments observed.

**Stephen Few's chartjunk-debate analysis (`pantry/the_chartjunk_debate.txt`).** Tufte's data-ink ratio is a heuristic, not a commandment. The Bateman et al. (2010) chartjunk study showed that embellishments don't reduce comprehension and may aid recall — Tufte's strict minimalism is therefore not the right reading of his own evidence. Few's resolution: clarity is the criterion, not minimization. The book adopts this resolution. The zero-baseline rule for bar charts is non-negotiable not because Tufte said so, but because the *perceptual mechanism* (area as channel; Stevens' power law for area perception) makes truncation produce distortion.

**Cairo's ethical frame (`pantry/Cairo Ethical Infographics.txt`).** When a designer chooses an encoding that produces a perceptual distortion, they are not just making an aesthetic choice — they are impeding the reader's understanding. Cairo's argument is rule-utilitarian: the designer's professional responsibility is to the reader. A truncated bar chart in a corporate slide is a bad design choice. A truncated bar chart in a research paper is a moral failure. The same rule, different stakes.

**The Evergreen / Emery 22-point design checklist (`pantry/EvergreenDataVizChecklist.txt`).** Stephanie Evergreen and Ann Emery's audit instrument synthesizes Tufte, Few, and Cairo into a workable list. Every bar chart in this chapter is evaluated against the checklist. Chapter 14 walks the full checklist; this chapter applies the comparison-chart subset (text legibility, accurate axes, sort order, color choice).

**Gestalt proximity and continuity** as the mechanism for the bar-vs-column orientation choice. When labels are long, horizontal bars place the label adjacent to its data (proximity), and the reader's eye flows from label to value without rotation (continuity). Vertical columns with rotated labels break both — proximity is violated by the rotation, and continuity is violated by the diagonal reading path.

---

## Concept 1 — The bar/column dichotomy, decided by structure not preference

A **bar chart** has horizontal bars; the categorical axis is on the y-axis (left side) and the quantitative axis on the x-axis (bottom). A **column chart** has vertical bars; categorical on x-axis (bottom), quantitative on y-axis (left).

These are not interchangeable stylistic choices. The choice is decided by two structural variables: **label length** and **category count**.

### Label length (the proximity/continuity argument)

If your category names are long, use **horizontal bars**. The horizontal bar chart places its category labels along the y-axis on the left. The label sits directly to the left of its bar. Gestalt proximity puts label and value next to each other; Gestalt continuity allows the eye to read horizontally from label to bar tip without changing direction. The reader can read each label without rotating their head.

If you use vertical (column) bars and the labels are long, you have three bad options:

- *Truncate the labels to fit.* You lose information.
- *Rotate the labels at -30° to -45°.* You slow the reader by ~200ms per label, multiplied by N labels. The pantry's bar-chart.html accepts this slowdown because the labels (12–17 characters) are short enough to remain readable when rotated and the vertical orientation is the dashboard convention.
- *Wrap the labels onto two or three lines.* You eat vertical space and the chart compresses.

The label-length threshold is roughly: **if your longest label exceeds 10–12 characters, default to horizontal bars.**

### Category count

For many categories (more than 15–20), default to horizontal and consider whether a single chart is the right form. Vertical columns at 20+ categories produce label crowding even with rotation. Horizontal bars at 20+ categories produce a tall scrolling chart that fails the "read in 5 seconds" test for executive contexts.

At 25+ categories you are usually past the point where one bar chart is the right form. Options:

- **Sort by value and show the top N.** Show the top 15 with a separate "all others" or "remaining 84 in appendix" callout.
- **Group categories into a higher-level taxonomy** (8 sub-categories grouped into 3 super-categories) and show the higher level.
- **Switch to a different chart family** — a treemap for large hierarchies (Chapter 10), a bullet graph for dashboard tiles (Chapter 13), or small multiples (later in this chapter).

### The default

Moderate label lengths (10 characters or less), 4–10 categories, comparison frame: **vertical columns**. Vertical is the cultural default. Horizontal is the deviation, justified by long labels or many categories.

Long labels, 12+ categories: **horizontal bars**. The horizontal orientation costs nothing in perceptual accuracy (position is position) and saves the reader the cognitive cost of tilted labels.

> ### ↳ Dig Deeper — The bar/column choice in journalism vs. dashboards
>
> **Prompt:**
>
> > Walk me through orientation choices in three contexts: Financial Times graphics, modern executive dashboards (Tableau / Power BI defaults), and academic research posters. Where do they default to horizontal bars even with short labels? When do they default to vertical despite long labels? What does this tell us about how Gestalt proximity gets traded against cultural expectation?
>
> **What to do with the output:** Compare the LLM's claims against actual published charts from those contexts in the past year. Note where convention overrides the proximity argument and ask whether the override is defensible.

---

## Concept 2 — The zero-baseline rule, grounded in area-as-channel theory

The y-axis (or x-axis on a horizontal bar) of any bar or column chart must start at zero. This is the single most important non-negotiable rule in the comparison family.

### The mechanism

Bar charts use length-from-baseline as the magnitude channel. Length is interpreted by the reader as area — the visual area of the bar swept from the baseline up. Stevens' power law (Chapter 1) tells us perceived length is approximately linear with actual length (exponent ≈ 1.0). The reader's perception is calibrated to "longer bar = larger value" — and the calibration assumes the baseline is at zero. Move the baseline up, and the proportionality breaks.

A concrete example. Three values: 12.4%, 12.8%, 13.2%. The actual difference between A and C is 0.8 percentage points — a 6% relative difference. Plot these on a y-axis from 0 to 14: the bars look almost identical, varying by perhaps 6% of bar height, faithfully reflecting the data. Plot the same values on a y-axis from 12 to 14: the C bar looks roughly *three times* the height of the A bar. The reader, applying linear length-perception, reads "C is roughly three times A" — when the data says "C is roughly 1.06 times A."

This is not aesthetic preference. It is a measurable perceptual distortion. Pandey et al. (2015) tested it experimentally — readers shown truncated charts rated the magnitude of differences much higher than readers shown the same data on un-truncated charts.

Tufte called the principle behind this **proportional ink**: the visual area of a chart element must be proportional to the data value it represents. The principle is a heuristic. The mechanism is Stevens' power law applied to area-as-channel.

### The Weissgerber finding

The Weissgerber et al. (2015) *PLOS Biology* paper analyzed 703 biology research articles. More than 88% contained at least one bar graph error. Truncated y-axes were a substantial fraction of the violations, alongside hiding distributions and using bars for paired data.

This is not an academic curiosity. The same papers that made claims like "the experimental group had higher levels of X" relied on bar charts that visually exaggerated those differences. The published claim and the visual signal disagreed. Readers relied on the visual signal.

The Weissgerber finding is why this chapter treats the zero-baseline rule as a non-trivial discipline. The violation is not rare. It is systematic, and it shapes scientific conclusions. Cairo's frame applies: a researcher who publishes a truncated bar chart is not just making a stylistic choice; they are making a moral choice with consequences for reader understanding.

### The exception that isn't

Defenders of truncated y-axes sometimes argue: "I need to show the variation, and the zero baseline hides it." This argument has the structure of "I need to show the difference, but the data is honest about how small the difference is, so I will use the chart to make it look bigger."

There is a legitimate move here. It is not "truncate the bars." The legitimate move is one of:

- **Use a different chart type.** A point estimate with error bars (Chapter 8) does not have the bar-length channel; the y-axis can be zoomed without lying about magnitude because the channel is point position, not area-from-baseline.
- **Use a difference chart.** Plot the *change* from a baseline rather than the absolute values. A bar chart of "percentage point change from Q3" can have a zero baseline (zero change is meaningful as zero) while still emphasizing small-but-real differences.
- **Annotate explicitly.** If the values are 12.4%, 12.8%, 13.2%, write the values on the bars. The reader does not need a stretched y-axis to see the difference; they can read the numbers. The bars then serve as ranking; the numbers as precision.

The truncated y-axis is never the right answer. There is always a legitimate alternative. Use it.

### The exception that is

There is one genuine exception: **time-series line charts** (Chapter 6) do not require a zero baseline because the channel is point position, not bar length. A line chart of stock prices showing $200 to $250 is not a proportional-ink violation — the channel does not encode magnitude as length-from-axis.

This is why financial charts often look scarier than they should: people transferring intuition from time-series line charts to bar comparisons truncate the bar baseline and get the wrong perceptual outcome. The rule depends on the channel. Bar charts use length-from-axis (zero baseline required). Line charts use point position (zero baseline optional, often misleading).

### Where Few refines Tufte

Tufte's strict minimalism extends the proportional ink principle to a broader claim: "minimize non-data ink." Few's analysis of the Bateman/Holmes chartjunk study (`pantry/the_chartjunk_debate.txt`) showed this stronger claim is not supported by experimental evidence. Embellishments that support the message can aid recall without reducing comprehension. The right test is "does this visual element support the message?" — not "is it data ink?"

For bar charts specifically: the zero baseline is not optional, because the violation directly distorts the magnitude channel. Color luminance reinforcing the bar height (as in the pantry's bar-chart.html) is *not* a violation — it is functional redundancy that aids accessibility and casual scanning. Light grid lines at axis ticks are *not* a violation — they help the reader read off precise values when needed. The Tufte purist would remove the gridlines. The Few-resolved position keeps them, because they serve the reader without distorting the data.

This is the book's position throughout. The rules are heuristics grounded in perceptual mechanism. Apply the rule when the mechanism applies; relax the rule when the mechanism doesn't.

> ### ↳ Dig Deeper — Auditing the zero-baseline rule in your domain
>
> **Prompt:**
>
> > Take three published reports or papers in [my professional domain — e.g., medical research, public health, market research, machine-learning benchmarks]. Find every bar chart. Audit each for zero-baseline compliance. Where the baseline is truncated, identify the proportional ink violation and specify what perceptual distortion it produces. Categorize the violations by whether the truncation appears intentional (rhetorical) or accidental (default tool output). Consider how Cairo's ethical frame applies to each: is this a stylistic choice, or does the chart impede the reader's understanding in a way the author should have caught?
>
> **What to do with the output:** Save the audit. The auditing pattern reappears in Chapter 14, where the Evergreen/Emery checklist scales it up to the full design audit.

---

## Concept 3 — Multiset and stacked: when one variable becomes two

A simple bar chart compares one quantitative attribute across categories. With two quantitative attributes per category — sales by region for both 2023 and 2024, say — you have two main options.

### Multiset (grouped) bars

Two bars per category, side by side, distinguished by color hue. The reader sees the within-category comparison clearly (which year was higher) and can compare across categories with some effort.

Use multiset when:

- The within-category comparison is the primary question.
- You have at most 2–4 sub-categories. Beyond that, the within-category bars become so narrow that the eye loses precision.
- The comparison is between values of the same kind on the same scale (revenue in 2023 vs. revenue in 2024 — both dollars, comparable directly).

### Stacked bars

One bar per category, segmented into colored sub-regions. The total bar height represents the sum across sub-categories.

Use stacked when:

- The total is the primary attribute and the composition is secondary.
- You have 2–6 sub-categories. Beyond 6, the stacking produces a rainbow that is difficult to read.
- The comparison across categories is mainly about the total. Comparing individual segments across stacked bars is *hard* because the segment baselines are not aligned (the second segment in column A starts at a different y-position than the second segment in column B).

### The trade-off, in channel-theory terms

Multiset wins on within-category comparison: each sub-category bar has its own baseline (the x-axis), so the reader is comparing position-along-a-common-scale — the highest-accuracy channel.

Stacked wins on across-category total comparison: the total bar height is position-from-zero, the same highest-accuracy channel. But the individual non-baseline segments lose their baseline; the second segment up has a baseline that varies by category, dropping the channel ranking from "position along common scale" to "position along non-aligned scales" or worse, "length without baseline." The eye cannot compare the second segments across columns accurately.

Neither form wins on cross-category sub-category comparison. For that you want **small multiples** — each sub-category gets its own panel with a shared y-axis. Each panel's bars use position-along-a-common-scale. Comparison across panels uses position-along-aligned-scales, the second-best channel. Small multiples are what you reach for when neither multiset nor stacked is right.

### Worked decision example

The Humanitarians AI dataset (which we will revisit in Chapter 9) tracks humanitarian funding across 4 sectors (food, shelter, water, health) for each of 5 countries in a given year. Three different communication questions, three different chart choices:

- "Which countries received the most total funding?" → **stacked bars**. Total is the answer.
- "In which sectors did each country receive the most?" → **multiset bars**. Within-country comparison is the answer.
- "Which sector was funded most across all countries?" → **small multiples** (one panel per sector, all panels with aligned y-axes).

The chart type is the answer to the question. Different questions, same data, different charts.

> ### ↳ Dig Deeper — Small multiples as the alternative
>
> **Prompt:**
>
> > Walk me through the small-multiples technique (popularized by Edward Tufte in *Envisioning Information* and re-emphasized in contemporary practice by Cole Knaflic and others). When does small multiples beat both multiset and stacked bars? Specify the design rules — shared y-axis scale, consistent panel size, the ordering of panels, the legend treatment. Show me how a four-sector / five-country humanitarian funding dataset would look as small multiples vs. multiset vs. stacked bars. Cite the perceptual basis (channel theory) for each form's strengths.
>
> **What to do with the output:** Save the comparison. Chapter 14 will use this in its design-audit checklist; multiple chart families have small-multiples as the redesign answer.

---

## Concept 4 — Radial bars: when the cycle earns the curve, and when it doesn't

A **radial bar chart** wraps the bars around a central point. Bar length becomes radius — the further from center, the larger the value. The bars fan out like spokes on a wheel.

Radial bars are visually striking. They are also perceptually worse than linear bars for almost every comparison task. Cleveland & McGill's ranking is direct on this: position along a common scale (linear bars) outranks length without a shared baseline, and far outranks length-along-a-curve. The eye cannot judge length along a curve as accurately as length along a straight line.

The radial form also introduces a second distortion: outer arcs cover more visual angle than inner arcs, so two bars of identical "radial length" sweep out different visual areas. Stevens' power law on area perception means the eye misreads this difference in ways that cannot be recovered by attention.

### When radial bars actually work

Two cases earn the radial complexity:

**Cyclic data.** Months of the year, hours of the day, days of the week. The radial layout reinforces the cycle. A radial bar chart of monthly aid delivery looks like a clock face; the eye reads the cycle rather than fighting it. The cyclic encoding *is* the rhetorical move; the perceptual cost is paid in service of communicating cyclicality.

**Decorative or marketing contexts.** When the chart's primary role is to draw attention rather than communicate precise values — magazine infographics, marketing dashboards. The radial form's visual interest is the point, and the audience's job is not precision.

### When radial bars don't work

For ordinary comparison of categories without an inherent cycle, radial bars are noise. The pantry's `radial-bar-chart.html` and `radial-column-chart.html` show working implementations; both are designed to make the form's strengths and weaknesses visible. Compare them to the linear `bar-chart.html`. The linear version is unambiguously easier to read. That is the empirical finding, every time.

The five-bar limit applies more strictly to radial than to linear. Beyond 5 categories, the curved layout compounds the perceptual difficulty. If you have 8 cognitive domains to compare (the Chapter 1 example), do not use a radial bar chart. The reader's eye will fail.

This is not minimalism. It is channel theory: position along a curve is a worse channel than position along a straight line. The Tufte vs. Holmes vs. Few debate is not the issue here. The issue is that the radial form trades the highest-accuracy channel for a worse one in service of visual interest, and most use cases do not justify the trade.

### Common misconceptions

**"Radial charts are more modern."** They are more decorative. Modern visualization design (FT, NYT, Pudding, Reuters) uses linear bars predominantly. The radial form is reserved for cyclic data or specifically decorative contexts.

**"Radial charts work in dashboards."** They consume more pixels per data point and produce less precise readings. A dashboard tile with a radial bar chart can almost always be replaced with a linear bullet graph (Chapter 13) at higher information density and better perceptual accuracy.

---

## Concept 5 — The 15+ category problem: when bar charts stop working

Bar charts scale from 2 categories to roughly 15 before the form starts breaking down. Beyond 15, the chart becomes hard to read for several converging reasons:

- **Label crowding** — even with rotation, 20+ labels overlap or compress into illegibility.
- **Loss of ranking precision** — when 25 bars are nearly the same height, the eye cannot rank-order them at a glance, which is supposed to be the bar chart's strongest move.
- **The "wall of bars" effect** — a chart with 30+ bars stops feeling like a comparison and starts feeling like a list. The reader treats it as text rather than as a visual.

The redesign options:

- **Top N + summary.** Show the top 15 categories explicitly. Aggregate the rest into "All other (84 categories, total = X)." Add a callout if any of the aggregated categories are notable.
- **Hierarchical grouping.** If the 30 categories belong to 5 super-categories (sectors, regions, time periods), show the super-category bar chart with drill-down to the sub-categories.
- **Treemap.** For the entire 30+ category set, a treemap (Chapter 10) often outperforms a bar chart on comprehension and pixel efficiency. Bars have one channel (length); treemaps have one channel (area). Stevens' power law makes treemaps less precise than bars for ranking, but more practical for very large category counts.
- **Lollipop chart.** A point at the value with a thin line connecting to the baseline. Visually less heavy than a full bar, can scale to 30+ categories without the wall-of-bars effect. Same channel (length), thinner ink. Few-resolved: a sensible refinement, not chartjunk.

You will revisit this trade-off in Chapter 10, where the treemap-vs-bar-chart choice for many-category comparison is the load-bearing decision.

---

## Mid-chapter checkpoint

Pick a bar chart you have produced or seen recently. Apply the three structural decisions: bar/column orientation (label length and category count), zero-baseline compliance, multiset/stacked/small-multiples appropriateness. If the chart compares two attributes per category, identify whether the structure matches the communication question (within-category vs. across-category vs. cross-sub-category).

If the chart fails any of these tests, sketch the correction. You should be able to do this in 60 seconds.

---

## Extended worked example — the full Claude Code workflow on the AI adoption bar chart

The pantry's `bar-chart.html` is the example. Walk through the full workflow: specification → prompt → output → audit → iterate.

### Step 1 — The channel specification

Before opening Claude Code, write the channel specification (using Chapter 1's framework):

- **Chart type:** Vertical bar (column) chart.
- **Marks:** Rectangle (bar) per cognitive domain, 8 total.
- **Channels:**
  - x-position: domain identity — *categorical*, 8 values, sorted by score descending for ranking readability.
  - bar height (y-position from zero baseline): score — *quantitative*, range 0–100.
  - color luminance: score — *quantitative*, redundant encoding, sequential pale-to-dark sequential.
- **Layout:** Zero baseline on y. y-ticks at 0, 25, 50, 75, 100. x-axis labels rotated -30° (domain names are 12–17 characters; rotation accommodates them in the column layout).
- **Annotations:** Score value above each bar (precision matters at executive-briefing density). Subtitle: "AI capability scores across cognitive domains — color encodes score magnitude."
- **Color scale:** `d3.scaleSequential` with `d3.interpolateRgb` from "#9B957F" (low) to "#8B0000" (high). Color domain: 30 to 100.
- **Responsive:** Re-render on window resize. Implementation: a `draw()` function called both initially and on `resize` events.
- **Dark mode:** prefers-color-scheme media query support.

### Step 2 — The four-move prompt

```
**Show what I have:**
Dataset: 8 rows. Each row has `domain` (string, 12-17 characters) and
`score` (number, 0-100). Sample data:
  Pattern Recognition, 94
  Language, 87
  Memory Retrieval, 96
  Causal Reasoning, 62
  Moral Judgment, 48
  Creativity, 71
  Embodied Teaching, 35
  Empathy, 41

**Say what I want:**
A vertical bar (column) chart in D3 v7. Single HTML file with inline
CSS and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: rectangles, one per domain.
- x-position: domain (categorical, sorted by score descending).
- y-position from zero baseline: score (quantitative, range 0-100).
  Zero baseline is non-negotiable.
- Color luminance as redundant encoding of score (sequential, pale-to-
  dark). Use d3.scaleSequential with d3.interpolateRgb from "#9B957F"
  (low) to "#8B0000" (high). Color domain: 30 to 100.
- y-axis ticks at 0, 25, 50, 75, 100.
- x-axis labels rotated -30 degrees with text-anchor "end".
- Score value text above each bar, font-size 11px.
- Subtitle: "AI capability scores across cognitive domains — color
  encodes score magnitude". Centered, font-size 12px, fill "#9B957F".
- Light grid lines at each y-tick, opacity 0.07 (light) / 0.06 (dark).
- Dark-mode support via prefers-color-scheme media query: foreground
  "#FFFFFF" in dark mode, "#0D0D0D" in light. Background follows the
  same logic.
- Margins: top 60, right 40, bottom 80, left 60.
- Bar padding: 0.28 of band width. Bar corner radius: 3px.

**Verify:**
Before writing the code, restate the channel decomposition to confirm
you understand. Then write the D3 v7 code with comments showing which
line implements which channel. After the code, list any decisions you
made that are not specified above (font choice, exact axis tick
formatting) so I can confirm or override them.
```

### Step 3 — Read Claude Code's output

Claude Code returns:

1. A specification restatement (verifies the channels).
2. A complete HTML file with inline D3.
3. A list of decisions not specified.

Open the HTML in a browser. Compare to the pantry's `bar-chart.html`. The two should look essentially identical, give or take font choices and exact margins.

### Step 4 — The audit (Evergreen/Emery checklist applied)

Run the comparison-chart subset of the Evergreen/Emery checklist:

| Item | Pass/Fail | Notes |
|---|---|---|
| Title is clear and informative | ✓ | Subtitle makes the chart's claim explicit |
| Axes are labeled and units are clear | ✓ | y-axis ticks + score range visible |
| Data is shown without distortion | ✓ | Zero baseline, no truncation |
| Color is used purposefully | ✓ | Luminance redundantly encodes score; categorical hue not misused |
| Sort order is meaningful | ✓ | Descending by value gives a ranking |
| Labels are readable | ✓ | Rotation accommodates length |
| Sufficient white space; not crowded | ✓ | Bar padding 0.28 of band width |
| No 3D / decorative effects | ✓ | Flat rectangles only |
| Annotations support understanding | ✓ | Score values above bars |
| Color-blind safe | ✓ (likely) | Sequential luminance carries the ranking; verify with simulator |

Every item passes. The chart is publishable as drawn.

### Step 5 — When iteration is needed

Most common iterations on this kind of chart:

- **Font sizes for the deployment context.** Smaller for dashboard tiles, larger for executive slides. One paragraph follow-up.
- **Color scale endpoints.** The muted neutral at the low end is unconventional but reads well in mixed light/dark contexts. Some readers may prefer a more standard sequential palette (Viridis, ColorBrewer); easy follow-up.
- **Hover interaction.** A tooltip on bar hover showing exact value and any drill-down detail. Two-paragraph follow-up.

Each iteration is a one-paragraph follow-up prompt. The base chart is right; you are now refining.

### What this teaches

The full workflow — specification, prompt, audit, iterate — is the model for every chart you build in the rest of the book. Chapters 6 through 13 introduce different chart types, but the workflow does not change. What changes is the specification: which marks, which channels, which design rules apply. The Claude Code interaction is the same.

This is the load-bearing claim of the book. Once you have the specification vocabulary, you do not need to memorize D3. Claude Code writes the D3. You write the specification.

---

## Chapter summary

You can now do five things you could not do before this chapter.

You can apply the bar/column dichotomy structurally (label length and category count, with Gestalt proximity and continuity as the perceptual mechanism), not stylistically.

You can defend the zero-baseline rule from its mechanism — Stevens' power law on area perception, codified by Tufte as proportional ink, evidenced by Pandey et al. (2015) and Weissgerber et al. (2015) — and recognize that the rule is non-negotiable for bar charts because the violation distorts the magnitude channel itself.

You can choose between multiset, stacked, and small multiples by mapping the communication question to the channel ranking — within-category comparison wants multiset (each sub-bar on its own baseline), across-category total wants stacked (the total uses position-from-zero), cross-sub-category comparison wants small multiples (aligned positions across panels).

You can recognize when a radial bar chart earns its curve (cyclic data, decorative contexts) and when it is decorative noise — and you can defend the position from channel theory rather than from minimalism preference.

You can specify a comparison chart precisely enough that Claude Code produces a usable, perceptually honest output on the first attempt — and audit the output against the Evergreen/Emery checklist if it does not.

The thing to watch for, going forward, is the temptation to use a comparison chart for a task that is not a comparison. Drawing a bar chart of "trend over time" wants a line chart (Chapter 6). Bars representing "parts of a whole" want a stacked-bar variant — or, better, a redesign as a treemap or grouped form (Chapters 9 and 10). The bar chart is the workhorse of *comparisons*. Comparisons are not every question.

---

## Key terms

- **Bar chart.** Horizontal bars; categorical axis on the left.
- **Column chart.** Vertical bars; categorical axis on the bottom. (Casual usage often calls both "bar charts"; this book distinguishes them.)
- **Multiset (grouped) bars.** Multiple bars per category, distinguished by hue. Best for within-category comparison of 2–4 sub-categories.
- **Stacked bars.** Single bar per category, segmented into colored sub-regions. Best when the total is the primary question.
- **Small multiples.** A grid of identical chart types, one per sub-category, with shared axis scales. Best for cross-sub-category comparison.
- **Zero baseline.** y-axis (or x on horizontal) starts at zero. Non-negotiable for bar charts because the channel is length-from-axis.
- **Proportional ink.** Tufte's principle: the visual area of a chart element must be proportional to the data value it represents. Truncated y-axes violate this; Stevens' power law on area perception is the underlying mechanism.
- **Radial bar chart.** Bars wrapped around a central point. Earns its complexity for cyclic data; otherwise decorative.
- **Label-length heuristic.** If the longest label exceeds 10–12 characters, default to horizontal bars.
- **Evergreen/Emery checklist.** A 22-point design audit instrument that synthesizes Tufte, Few, and Cairo into a workable list. Used in this chapter for the comparison-chart subset; full checklist in Chapter 14.
- **Few's clarity-over-minimization position.** The Tufte data-ink ratio is a heuristic; the criterion for any visual element is "does this support the message?" not "is this strictly data ink?"

---

## Discussion questions

1. The zero-baseline rule applies to bar charts but not to line charts. Why? Frame the answer in marks-and-channels terms (Chapter 1) — what channel does each form use, and why does the zero requirement attach to one and not the other?
2. Multiset bars and small multiples both compare values across categories and sub-categories. When would you choose one over the other? Use channel theory to ground the answer.
3. The Weissgerber et al. (2015) finding shows that >88% of biology research articles violate good bar-chart practice. Why might professional researchers, publishing in peer-reviewed journals, persist in producing flawed bar charts? What does this suggest about the role of formal training in visualization, and how does Cairo's ethical frame apply?
4. Take a published radial bar chart from a recent newspaper or magazine. Analyze whether the radial form earns its complexity. Specify what would be lost (rhetorical force, visual interest) and gained (perceptual accuracy) by converting to a linear bar chart.
5. *Cross-chapter synthesis.* Chapter 13 will introduce bullet graphs as a dashboard-density alternative to radial dial charts. Frame the bullet graph in marks-and-channels terms — what makes Few argue it is more efficient than the radial form?

---

## Exercises

### Warm-up

**Exercise 5.1** — *Orientation choice.* For each of the following, decide between bar (horizontal) and column (vertical), and justify the choice using label length and category count:
- 5 product categories: Electronics, Apparel, Home Goods, Sports, Beauty. Quantity: revenue.
- 22 country codes (ISO 3-letter). Quantity: GDP per capita.
- 4 regions: North America, EMEA, APAC, LATAM. Quantity: customer count.
- 8 cognitive domains as in the Chapter 1 example. Quantity: AI capability score.

**Exercise 5.2** — *Zero-baseline audit.* You see a bar chart of marketing campaign performance with the y-axis from 6.0 to 7.5 (engagement rate). The bars range from 6.2 to 7.3. Identify the proportional ink violation. Use Stevens' power law to estimate the perceptual distortion (how much larger does the difference appear than it is). Specify three legitimate alternatives to the truncated y-axis.

**Exercise 5.3** — *Multiset vs. stacked.* You have quarterly revenue for 4 product lines across 3 fiscal years. Decide whether multiset, stacked, or small multiples is right for each question, and justify with channel theory:
- "Which product line had the highest Q4 2023 revenue?"
- "How has total revenue grown from 2022 to 2024?"
- "How has Product A's revenue changed across years compared to Product B's?"

### Application

**Exercise 5.4** — *Build a bar chart with Claude Code.* Take a real dataset (5–10 categories, one quantitative attribute). Write a four-move Claude Code prompt following the worked-example pattern. Submit it. Audit the output using the comparison-chart subset of the Evergreen/Emery checklist. If any item fails, write the follow-up prompt that fixes it.

**Exercise 5.5** — *Multiset vs. small multiples comparison.* Take a dataset with 5 categories and 3 sub-categories per category (15 values). Build a multiset bar chart. Build the same data as small multiples. Compare the two for the question "which sub-category was largest in each category." Identify which form better answers the question and why, in channel-theory terms.

**Exercise 5.6** — *Stacked-to-grouped redesign.* Find a stacked-bar chart you find unsatisfying (corporate report, news graphic). Redesign as either multiset or small multiples. Specify the redesign with a Claude Code prompt. Build it. Compare to the original on the question "what sub-category comparison was the original chart trying to support?"

### Synthesis

**Exercise 5.7** — *Truncated-axis audit in the wild.* Find three bar charts in published reports (corporate, governmental, or news media) with truncated y-axes. For each, identify the proportional ink violation, estimate the perceptual distortion using Stevens' power law, and propose the redesign. Submit as a one-page audit. Apply Cairo's ethical frame: which of the three is a stylistic choice, and which crosses into a moral failure?

**Exercise 5.8** — *Cyclic data: radial vs. linear.* Take a dataset with a clear cyclic structure (monthly sales, hourly traffic, day-of-week activity). Build both a radial bar chart and a linear bar chart with Claude Code. Determine which form better serves the cyclic question. Justify with reference to the Cleveland & McGill ranking and the cyclic-emphasis argument. Where does the trade-off land for your specific dataset?

### Challenge

**Exercise 5.9** — *Production redesign.* Find a bar chart in a recent annual report or earnings deck. Audit it against the comparison-chart Evergreen/Emery subset (orientation, zero baseline, multiset/stacked appropriateness, label legibility, color encoding). Redesign with Claude Code. Submit a side-by-side with one paragraph per fix and the perceptual mechanism it serves.

**Exercise 5.10** — *The five-bar pie alternative.* You have a dataset with 5 categories that sums to 100% (a part-to-whole, anticipating Chapter 9). Build a stacked bar (single bar of total, segmented) and compare to a pie chart of the same data. Apply channel theory: which form makes the among-the-parts comparison easier, and why? Build both with Claude Code; write a one-paragraph justification citing Cleveland & McGill's angle-vs-length finding.

---

## LLM Exercise — Chapter 5: Comparison Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A complete, audited comparison chart for a real dataset, plus the channel-mapping audit document and the Claude Code prompt that produced it. The first taxonomy-chapter deliverable; the same pattern repeats in Chapters 6–13.

**Tool:** Claude Code (for the build) + Claude chat (for the audit and iteration)

---

**The Prompt (audit + build):**

```
I have a dataset of [DESCRIBE: your data — rows, columns, types]. The
communication goal is [DESCRIBE: what the reader needs to know in 5
seconds].

Walk me through the comparison-chart design for this dataset using the
Bertin/Cleveland/Munzner framework from Chapter 1 and the design
considerations from Chapter 5:

1. Confirm the chart family is comparison (vs. time-series, distribution,
   relationship, etc.). If it isn't, recommend the right family and
   stop.

2. Decide bar vs. column orientation based on label length and category
   count. Cite Gestalt proximity and continuity in the justification.

3. If there are sub-categories, decide multiset vs. stacked vs. small
   multiples based on the communication goal. Cite the channel ranking
   in the justification — within-category wants multiset (each bar on
   its own baseline), across-category total wants stacked, cross-sub-
   category wants small multiples.

4. Specify the channels using the Chapter 1 framework:
   - x-position (or y-position): which attribute
   - bar height (or length): which attribute, with zero baseline
     (cite proportional ink and Stevens' power law)
   - color: which attribute, sequential / categorical / redundant
   - any other channels in use

5. Specify the layout: axis ticks, label rotation, annotations, sort
   order, margins, color scale endpoints, dark-mode behavior.

6. Write a single Claude Code prompt that follows the four-move
   structure (show, say, constrain, verify) and is precise enough that
   Claude Code produces a usable D3 v7 chart on the first attempt.

After Claude Code returns the chart, audit using the comparison-chart
subset of the Evergreen/Emery checklist:
- Title clear?
- Axes labeled, units clear?
- Zero baseline?
- Sort order meaningful?
- Color used purposefully (not magnitude on hue, not arbitrary
  decoration)?
- Labels readable?
- Color-blind safe?

Flag any audit failure and write the follow-up prompt that corrects it.
```

---

**What this produces:** A markdown audit document and an HTML file containing the working D3 chart. Save as `chapter-05-comparison-audit.md` and `chapter-05-comparison.html`.

**How to adapt this prompt:**
- *For your own domain:* Replace the dataset description.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the Chapter 1 channel framework and the Evergreen/Emery checklist as the system prompt; the per-chapter audit prompt becomes the user message.
- *For Cowork:* Use Cowork to execute the Claude Code prompt and save the resulting HTML file directly to your project directory.

**Connection to previous chapters:** Builds on Chapter 1 (channel ranking, expressiveness/effectiveness, Stevens' power law), Chapter 2 (chart selection — confirming you are in the comparison family), Chapter 3 (data type identification), Chapter 4 (Claude Code workflow, MBTA-style iteration). The Evergreen/Emery checklist that anchors the audit step will be walked in full in Chapter 14.

**Preview of next chapter:** Chapter 6 takes the comparison vocabulary and extends it to data with a continuous time dimension. The static comparison becomes an evolving trajectory. The zero-baseline rule shifts: bar charts require it because length is the channel; line charts do not because point position is the channel. The chapter shows where each rule applies and why.

---

## Visual suggestions

This chapter is about comparison-chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for comparison charts: [Bar Chart](20-bar-chart.md), [Multiset Bar](46-multiset-bar.md), [Stacked Bar](67-stacked-bar.md), [Radial Bar](58-radial-bar.md), [Radial Bar Chart](59-radial-bar-chart.md), [Radial Column](60-radial-column.md), [Radial Column Chart](61-radial-column-chart.md), [Span Chart](64-span-chart.md), [Bullet Graph](26-bullet-graph.md), [Tally Chart](71-tally-chart.md), [Pictogram Chart](52-pictogram-chart.md), [Dot Matrix](35-dot-matrix.md), [Treemap](75-treemap.md). Each Part II chapter has its own prompt.

### Figure 5.1 — The HAI AI adoption bar chart with zero-baseline toggle

The chapter's central worked example. A horizontal bar chart of AI adoption rates by sector, with a toggle that switches the baseline from zero (correct) to the data minimum (the truncation failure mode). The reader sees Few's zero-baseline rule become a perceptual demonstration.

See [Bar Chart](20-bar-chart.md) in Part II for the canonical reference.

```
Generate a horizontal bar chart in D3 v7 with a zero-baseline toggle. Two files:

1. `chapter-05-fig-01.html` — full HTML with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). A bar chart with a toggle button that switches the x-axis between [0, max] and [min, max]. Page subtitle: "Zero baseline vs. truncated baseline — the same data, two readings."

2. `chapter-05-fig-01/data.json` — the dataset.

Data shape:
- 10–12 sectors with AI adoption percentage.
  - `sector`: string — industry sector
  - `adoption_pct`: number — percentage 0–100

{DATA NEEDED} — A representative AI adoption survey by sector. McKinsey State of AI, Stanford AI Index, or similar published source provides this. 10–12 sectors with adoption rates spanning a wide range.

Encoding:
- Horizontal bars sorted descending by `adoption_pct`.
- Bar length encodes percentage on a position-along-common-scale channel.
- Toggle: x-axis range. Default = [0, 100] (zero baseline, correct). Alt = [min(adoption_pct), max(adoption_pct)] (truncated, the demonstration of the failure mode).
- Direct value labels on each bar.
- Caption beneath the toggle reads "Watch the gap between sectors change as the baseline shifts."

Style: warm monochrome — black, dark walnut, blood-red accents. Serif body, JetBrains Mono for labels and the toggle.

Provide both files as separate code blocks.
```

---

## Further reading

- **Cleveland, William S., and Robert McGill. (1984).** "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association* 79(387). The foundational empirical ranking that grounds "bars are most accurate."
- **Heer, Jeffrey, and Michael Bostock. (2010).** "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design." *CHI '10.* The replication confirming the ranking for the contemporary D3 era.
- **Tufte, Edward R. (1983, 2nd ed. 2001).** *The Visual Display of Quantitative Information.* Chapters 4–5 establish proportional ink and the data-ink ratio. Read the principles; apply them as Few-resolved heuristics, not commandments.
- **Few, Stephen. (2011).** "The Chartjunk Debate: A Close Examination of Recent Findings." *Visual Business Intelligence Newsletter*, April–June 2011. The transcript is in the book's pantry. Read this for the "clarity over minimization" position the book adopts.
- **Weissgerber, Tracey L., Natasa M. Milic, Stacey J. Winham, and Vesna D. Garovic. (2015).** "Beyond Bar and Line Graphs: Time for a New Data Presentation Paradigm." *PLOS Biology* 13(4). The empirical analysis of bar-chart misuse in biology research.
- **Pandey, Anshul Vikram, Anjali Manivannan, Oded Nov, Margaret Satterthwaite, and Enrico Bertini. (2014).** "The Persuasive Power of Data Visualization." *IEEE Transactions on Visualization and Computer Graphics.* And: Pandey et al. (2015), "How Deceptive Are Deceptive Visualizations?" *CHI '15.* Controlled experiments on truncated y-axes and other distortions.
- **Knaflic, Cole Nussbaumer. (2015).** *Storytelling with Data.* Chapter 4 is a particularly clear treatment of when to use which chart for comparison tasks. Worked-example density makes it a good professional reference.
- **Evergreen, Stephanie, and Ann K. Emery.** Data Visualization Checklist. The audit instrument used throughout this chapter and in full in Chapter 14. Available at stephanieevergreen.com.

---

## Tags

comparison-charts, bar-chart, column-chart, multiset, grouped-bars, stacked-bars, radial-bar, zero-baseline, proportional-ink, Tufte, Few, Cairo, Weissgerber, Pandey, label-length, small-multiples, Cleveland-McGill, Stevens-power-law, Gestalt-proximity, Gestalt-continuity, Evergreen-Emery, D3, Claude-Code, channel-specification
