# Chapter 8 — Relationship and Correlation Charts
*Two Variables and the Question They Refuse to Settle.*

## Three suggested titles

- Relationship and Correlation Charts: The Annotation That Belongs On All of Them
- Stevens' Power Law and the Bubble Chart's Radius-Not-Area Failure
- Scatterplots, Heatmaps, and the Ethics of Showing Correlation

---

## Chapter overview

By the end of this chapter you will be able to build the family of relationship charts — scatterplots, bubble charts, connected scatterplots, parallel coordinates, heatmaps — and you will know when each is right. You will know why bubble charts must encode the third variable as area and not radius (the Stevens' power law mechanism), why every chart that shows correlation needs a "correlation is not causation" annotation in Cairo's frame, and how to mitigate overplotting (the most common scatterplot failure) without distorting the data.

---

## Learning objectives

1. **(Apply)** Build a scatterplot with OLS trend line and annotate it with the appropriate correlation-is-not-causation caveat — applying Cairo's ethical frame that omitting this caveat is a moral failure, not just a style choice.
2. **(Analyze)** Identify overplotting in a scatterplot and specify at least two mitigation strategies (jittering, alpha transparency, 2D binning) with their trade-offs.
3. **(Evaluate)** Assess whether a bubble chart's third variable encoding (area vs. radius) is perceptually honest and correct it if not, citing Stevens' power law.

---

## Opening case — the HAI scatterplot of education and life expectancy

Open `pantry/visualization/scatterplot.html` in a browser. A single scatterplot. Each point is a country. The x-axis shows the country's education index (0 to 1). The y-axis shows life expectancy (years). An OLS regression line runs through the cloud, sloped upward and to the right. Pearson's r is annotated near the line: r = 0.79.

The chart shows a strong positive correlation between education and life expectancy. The scatterplot mark is a point per country; both quantitative attributes use position (the highest-accuracy channel from Chapter 1); the OLS line summarizes the relationship.

The chart is well-built. It is also incomplete. A reader looking at the chart could conclude that better education *causes* longer life expectancy. The correlation is real. The causal claim is not what the chart shows. The chart shows a statistical association; causation is a separate empirical question.

This is where Cairo's ethical frame applies most pointedly. A scatterplot showing strong correlation, without an explicit annotation distinguishing correlation from causation, invites the reader to make the causal inference. The chart's visual force exceeds its empirical claim. In Cairo's reading, this is not a stylistic oversight — it is a *moral failure*. The designer's professional responsibility includes preventing the over-reading that the chart's visual force would otherwise produce.

The annotation that fixes the chart is short. Add a callout near the trend line: "Correlation is not causation. Education and life expectancy are associated; the causal relationship is not established by this chart." That single line of text does not weaken the chart. It strengthens it. The reader now knows what the chart is and is not claiming.

This chapter is about the family of relationship charts and the design responsibilities they impose. The scatterplot is the canonical form; bubble charts, connected scatterplots, parallel coordinates, and heatmaps are extensions for specific analytical needs. Each form has its own design rules, its own perceptual mechanisms, and its own ethical responsibilities around inference.

---

## Theoretical grounding — Cairo's correlation-is-not-causation, Stevens on area perception, Munzner on parallel coordinates

This chapter draws on three sources, each at the moment its specific contribution is needed.

**Cairo on correlation-is-not-causation.** Cairo's *How Charts Lie* (2019), Chapter 2, includes the El País Catalan independence poll case: 45.3% No vs. 44.5% Yes, margin of error ±2.95. The story said Catalonia "swings toward No." The correct statement: the difference is within sampling error. A chart that shows the 0.8 percentage-point difference without showing the margin of error visually invites a conclusion the data does not support. Cairo's frame: omitting the uncertainty visualization or the appropriate caveat is a moral failure, not a style choice. The same frame applies to scatterplots: a strong correlation without explicit causal-claim disambiguation invites readers to over-read.

**Stevens' psychophysical power law on area perception.** Chapter 1 introduced the law: perception of physical magnitude follows a power function. For *area*, the exponent is approximately 0.7 — perception is sublinear. Doubled area is perceived as roughly 1.5–1.7× larger, not 2×. This matters acutely for bubble charts, where the third variable is encoded as the bubble's size. If the size is encoded as the *radius*, doubling the value produces a bubble with 4× the area (because area scales as radius squared). The eye, applying Stevens' power law to that 4× area, perceives it as roughly 2.5×. The chart now shows three numbers — the data (2×), the area (4×), the perceived area (2.5×) — and none matches the others. The fix is to encode the third variable as *area* directly: doubled value, doubled area, perceived as roughly 1.5–1.7× — closer to the data.

**Munzner on parallel coordinates and axis order.** Tamara Munzner's *Visualization Analysis and Design* (2014) treats parallel coordinates as a high-dimensional visualization technique that works because each axis is position-along-a-common-scale (Chapter 1's highest-accuracy channel). The form's distinctive failure mode — that the visual pattern depends on axis order — is a Bertin-class channel limitation: the lines connecting axes use position to encode pairwise relationships, and changing the order changes the visible pattern without changing the data. Munzner's framework: parallel coordinates are excellent when the analyst can interactively reorder axes (brush and explore); they are weaker when published as static charts (one axis order is canonical, hiding patterns visible in others).

---

## Concept 1 — Scatterplots: the workhorse of relationship

A scatterplot is a chart with two quantitative axes (x and y), and a point mark for each observation at the (x, y) coordinate corresponding to its values. Scatterplots show how two variables co-vary.

### When scatterplots work

- Two quantitative variables. The relationship between them is the question.
- Sample size large enough to see a pattern (n > 30 typical; more is better).
- The reader wants to see the *cloud shape* — direction of correlation, strength, outliers, possible non-linearity.

### Design decisions

**Axes.** Both quantitative; both use position (the highest-accuracy channel). Convention: independent variable (cause, predictor) on x; dependent variable (effect, outcome) on y. The convention matters because readers default to "x predicts y."

**Trend line.** OLS regression line is the standard. Other options: LOESS (locally weighted, captures non-linearity), median trend, Theil-Sen (robust to outliers). Choose based on whether the relationship is plausibly linear.

**Confidence band.** Optional shaded region around the trend line showing uncertainty in the trend. Useful when sample size is moderate (the band shows whether the trend is well-estimated).

**Annotations.** Pearson's r (or appropriate correlation coefficient) near the trend line. The correlation-is-not-causation annotation. Any specific points worth highlighting (outliers, named cases).

### The overplotting problem

When sample size is large and points cluster, a standard scatterplot becomes a black blob in the dense region. The cloud shape becomes invisible. Three mitigation strategies:

**Alpha transparency.** Set point fill opacity to 0.1–0.4. Dense regions accumulate alpha and appear darker; sparse regions remain visible as individual points. The cloud shape returns. This is the simplest and usually the right first move.

**Jittering.** Add small random offsets to point positions. Useful when many points have identical or near-identical values (typical with discrete variables on a scatterplot). Jittering reveals the count at each value.

**2D binning.** Aggregate points into a 2D grid; show count per cell as color luminance (a hexbin chart). This converts the scatterplot into a heatmap-style display. Good for very large datasets (n > 10,000); loses individual outliers.

For Claude Code work: specify the mitigation strategy in the prompt. The default scatterplot will overplot if the data is dense; the prompt should say "use alpha transparency 0.3" or "use 2D hexagonal binning" for the appropriate strategy.

> ### ↳ Dig Deeper — Overplotting strategies in your domain
>
> **Prompt:**
>
> > Take a scatterplot context typical of my work where overplotting is likely (10,000+ point comparison; clustered discrete data; etc.). Walk through alpha transparency, jittering, and 2D binning as mitigations. For each, name the perceptual trade-off (what gets revealed; what gets hidden). Recommend the right strategy for my context.
>
> **What to do with the output:** Save the analysis. Use it next time you build a scatterplot of dense data.

---

## Concept 2 — Bubble charts and the radius-not-area failure

A bubble chart is a scatterplot where each point's *size* encodes a third variable. The mark is a point (typically a circle); the channels are x-position, y-position, and size.

### When bubble charts work

- Three quantitative variables with one designated as "size" (cumulative magnitude, weight, importance).
- The reader needs to compare three values per observation.
- The size variable has meaningful magnitude differences across observations (otherwise all bubbles look the same).

### The radius-vs-area trap

The defining design decision is how the size encodes the value. Two options:

**Encode by radius.** Bubble radius scales linearly with the value. A value of 100 produces a bubble of radius 10; a value of 200 produces radius 20. The *areas* are 100π and 400π. The visual area is 4× for a 2× value — distorted before perception even enters.

**Encode by area.** Bubble area scales linearly with the value. A value of 100 produces area 100; a value of 200 produces area 200. The *radii* are √100 ≈ 10 and √200 ≈ 14. The visual area matches the value.

Stevens' power law adds another layer. Even with area encoding, perception of area is sublinear (exponent ≈ 0.7). A doubled-area bubble is perceived as roughly 1.5–1.7× larger. With area encoding, the data-to-perception map is data → area (linear) → perception (sublinear). With radius encoding, it's data → area (squared) → perception (sublinear) — the squaring compounds the perceptual distortion.

The HAI bubble chart in `pantry/visualization/bubble-chart.html` includes a toggle: "encode by radius" vs. "encode by area." Open it. Switch the toggle. The visual difference is dramatic. The same dataset under radius encoding looks like extreme values dominate; under area encoding, the values are visually proportional (within the limits Stevens' law allows).

For Claude Code work: specify "area encoding" explicitly. Specify the scale function: `d3.scaleSqrt` (which scales by the square root of the input, producing area-proportional radii) is the canonical D3 method. The prompt: "use d3.scaleSqrt for the bubble radius scale, so that bubble area is proportional to the value."

### When to skip the bubble chart

- The size variable doesn't add much beyond x and y. Dropping it produces a clean scatterplot.
- The dataset is large (overplotting compounds with bubble size; bubbles cover each other).
- The audience's graphicacy doesn't include "bubble chart with three variables." Two-variable scatterplot + small multiples often communicates better.

The bubble chart is a higher-graphicacy form than the standard scatterplot. Use it when the third variable matters; skip it otherwise.

---

## Concept 3 — Heatmaps and parallel coordinates

Two specialized relationship forms for specific situations.

### Heatmaps

A heatmap is a 2D grid where each cell's color encodes a value. Common uses:

- **Two categorical variables + intensity.** A heatmap of "AI adoption by sector × by region" with color luminance encoding adoption rate. The form is part-comparison, part-relationship.
- **Joint distribution of two quantitative variables.** A heatmap of a 2D KDE (or histogram), showing where in (x, y) space observations cluster. This is the 2D-binning extension of the scatterplot for very dense data.
- **Correlation matrix.** A heatmap showing pairwise correlations across a set of variables. Each cell shows the correlation between two variables, usually with a sequential or diverging color scale.

Heatmap design rules:

- **Color scale matched to data.** Sequential (single hue, varying luminance) for unipolar data. Diverging (two-hue, midpoint at zero) for data with meaningful zero. Categorical color is usually wrong for heatmap intensity (luminance is the magnitude channel).
- **Cell labels for precise reading.** When exact values matter, add the value as text inside each cell. The chart now uses two channels (color luminance + text) — redundant but more readable.
- **Sort order.** Rows and columns ordered to reveal structure. Hierarchical clustering, manual ordering by relevance, or numerical sort all work.

The pantry's `heatmap.html` shows a standard form.

### Parallel coordinates

Parallel coordinates show high-dimensional data by drawing parallel vertical axes (one per variable) and connecting each observation as a polyline that crosses all axes at the appropriate values.

When parallel coordinates work:

- 3+ quantitative variables. The form generalizes scatterplots beyond two dimensions.
- The reader can interactively explore (brushing, axis reordering, filtering). Static parallel coordinates are weaker.
- Pattern detection across multiple dimensions matters more than precise comparison of any single pair.

Parallel coordinates' fundamental limitation: the visual pattern depends on axis order. Reordering axes can reveal patterns invisible in other orders. For static charts, you choose one axis order; the chart shows what that order makes visible. For interactive charts, the user can explore.

For Claude Code work: parallel coordinates are typically built with brushing interaction. Specify the interaction in the prompt: "include axis brushing — clicking and dragging on an axis filters the lines to show only observations within the brushed range."

---

## Concept 4 — Connected scatterplots and other extensions

A connected scatterplot connects scatterplot points in chronological order with a line. The form shows two quantitative variables co-varying over time.

### When connected scatterplots work

- Two quantitative variables, both varying over time.
- The *path* between (x, y) values matters, not just the cloud of points.
- Examples: GDP vs. CO₂ emissions over time for one country; revenue vs. customer count for one company.

### Design rules

- **Temporal direction.** Use color luminance (pale-to-dark) along the path to show time direction. Or arrowheads at intervals. Or annotated points at key dates.
- **Axes.** Both quantitative; standard scatterplot conventions.
- **Path smoothing.** Usually `d3.curveLinear` (straight segments between points) is right. Smoothing can introduce visual artifacts.

The form is uncommon but useful. A scatterplot of two variables hides their temporal evolution. A line chart of each variable separately hides the relationship. The connected scatterplot shows both.

### Other extensions

- **Slope graphs.** Connect two points (before/after) per category. Useful for showing change between two time points across categories.
- **Marginal histograms.** Add small histograms along the x and y axes of a scatterplot to show univariate distributions in addition to the joint distribution.
- **Hexbin overlay.** Show the cloud shape as a hexbin grid (color luminance for density) with selected outlier points highlighted on top.

Each extension is a specific solution to a specific limitation of the standard scatterplot. Reach for them when the question demands.

---

## Mid-chapter checkpoint

Pick a relationship-chart context from your work. Walk through the form selection: scatterplot (two variables, cloud-shape question), bubble chart (three variables, with size as the third), connected scatterplot (two variables over time, path matters), parallel coordinates (3+ variables, multivariate exploration), heatmap (2D categorical or joint distribution).

Then identify the failure mode each form is most prone to: overplotting (scatterplot), radius-not-area (bubble chart), axis-order dependence (parallel coordinates), wrong color scale (heatmap). Specify the design that prevents the failure.

You should be able to do this in 90 seconds.

---

## Extended worked example — building a scatterplot with annotations

Take a dataset: 50 countries with GDP per capita (x), life expectancy (y), and population (third variable). Communication question: what is the relationship between GDP and life expectancy, and which countries deviate from the trend?

### Channel decomposition

- Marks: points (one per country). Size: bubble area encoding population.
- x-position: GDP per capita (quantitative).
- y-position: life expectancy (quantitative).
- Bubble area: population (quantitative). Use `d3.scaleSqrt` for area-proportional sizing.
- Color hue: continent (categorical, identity channel).
- OLS trend line (with optional confidence band).
- Annotations: Pearson r; correlation-is-not-causation caveat; named outliers.

### The four-move prompt

```
**Show what I have:**
50 countries. Each row: country (string), gdp_per_capita (number, USD),
life_expectancy (number, years), population (number, millions),
continent (string, 6 values).

Sample:
  USA, 65000, 78.9, 331, North America
  Norway, 75000, 82.4, 5.4, Europe
  Bangladesh, 1700, 72.6, 165, Asia
  ...

**Say what I want:**
Bubble scatterplot in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: circles, one per country.
- x-position: gdp_per_capita (quantitative, range 0 to 80000, log scale
  recommended given the wide GDP range).
- y-position: life_expectancy (quantitative, range 50 to 90).
- Bubble area: population (quantitative). USE d3.scaleSqrt for radius
  (NOT linear scaling). The bubble's visual AREA must be proportional
  to population, not the radius. Stevens' power law applies.
- Color hue: continent (categorical, identity channel). Use 6 distinct
  hues.
- Alpha transparency: 0.7 (some overlap is acceptable; full opacity
  obscures clusters).
- OLS trend line: through (gdp, life_expectancy). Display the slope
  and Pearson r near the line.
- Annotations:
  - Top-right corner: "Correlation is not causation. Education and
    life expectancy are associated; the causal relationship is not
    established by this chart."
  - Outliers (3+ standard deviations from trend): label by country name.
- x-axis: log scale, ticks at 1000, 5000, 10000, 50000.
- y-axis: linear, ticks at 60, 70, 80, 90.
- Legend: continent colors, top-right.
- Margins: top 80, right 240 (legend), bottom 60, left 80.
- Dark mode support.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements which channel. Confirm that the bubble
size uses d3.scaleSqrt (NOT linear). List any decisions not specified.
```

### Audit

The standard Evergreen/Emery checks plus:

- Bubble size uses `d3.scaleSqrt` (verify in the code).
- Correlation-is-not-causation annotation is present and visible.
- Trend line is OLS (or specified alternative).
- Pearson r is annotated.
- Overplotting is mitigated (alpha transparency in the constraints).

The most common Claude Code failure on this prompt: linear scaling of bubble radius despite the explicit instruction. The follow-up prompt: "The bubble radius is scaled linearly with population. This produces visual area scaling as population squared, which is a Stevens' power law violation (Chapter 1). Replace `d3.scaleLinear` with `d3.scaleSqrt` for the radius scale. The bubble's visual area should be proportional to population, not its radius."

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build a scatterplot with appropriate design decisions — OLS trend line, Pearson r annotation, correlation-is-not-causation caveat, overplotting mitigation strategy.

You can build a bubble chart that encodes the third variable as area (using `d3.scaleSqrt` for the radius scale), avoiding the Stevens' power law radius-not-area trap.

You can build a heatmap with appropriate color scale (sequential for unipolar; diverging for bipolar), and a parallel coordinates chart with awareness of the axis-order dependence problem.

You can apply Cairo's frame to relationship charts: the correlation-is-not-causation annotation is not optional aesthetic — it is a professional responsibility. Omitting it when the chart's visual force invites the causal inference is a moral failure in Cairo's reading.

The thing to watch for, going forward, is the temptation to skip the annotation. A "clean" scatterplot without the caveat looks tidier; it also lies by omission. The caveat is the small text that prevents the over-reading the chart would otherwise produce.

---

## Key terms

- **Scatterplot.** Two-quantitative-variable chart with point marks at (x, y) coordinates.
- **Bubble chart.** Scatterplot extended with a third variable encoded as point size.
- **Connected scatterplot.** Scatterplot with points connected in time order.
- **Heatmap.** 2D grid with color luminance encoding intensity per cell.
- **Parallel coordinates.** Multi-axis chart for 3+ quantitative variables; observations as polylines.
- **Stevens' power law (area perception).** Perceived area scales as area^0.7. Applies to bubble chart sizing.
- **`d3.scaleSqrt`.** D3 scale function that produces area-proportional bubble radii.
- **Overplotting.** When point density obscures cloud shape. Mitigated by alpha, jittering, or 2D binning.
- **OLS trend line.** Ordinary Least Squares regression line through scatterplot points.
- **Correlation-is-not-causation annotation.** Cairo-class ethical requirement on charts showing strong correlation without explicit causal disambiguation.

---

## Discussion questions

1. The correlation-is-not-causation annotation is widely repeated as an exhortation. Cairo's frame makes it stronger: omitting it is a moral failure. Where does the moral language land for you, and where does it overreach?
2. Bubble charts encode three variables. The compounding perceptual loads (Stevens' power law on area; cognitive load of three channels) make them harder than scatterplots. When do they earn their cost?
3. Parallel coordinates are powerful when interactive and weaker when static. What does this say about how to choose static vs. interactive forms in your professional context?
4. Heatmaps use color luminance for magnitude — sixth on Cleveland & McGill's accuracy ranking. What do they offer that compensates for the channel-accuracy cost?
5. *Cross-chapter synthesis.* Chapter 9 (part-to-whole) and Chapter 12 (spatial) both encounter area-as-channel. Frame the unified principle that connects them across chapters.

---

## Exercises

### Warm-up

**Exercise 8.1** — *Form selection.* For each, name the right relationship form:
- Two variables across 200 observations, focus on cloud shape.
- Two variables across 50,000 observations.
- Three variables, the third varying continuously across observations.
- Five quantitative variables across 100 observations.
- Two categorical variables with intensity values.

**Exercise 8.2** — *Bubble-chart audit.* Find a published bubble chart. Does the bubble area or radius encode the third variable? If radius, specify the redesign.

**Exercise 8.3** — *Causation diagnosis.* Find a published scatterplot showing strong correlation. Does it include the correlation-is-not-causation caveat? If not, write the caveat that should be added.

### Application

**Exercise 8.4** — *Build a scatterplot with Claude Code.* Take a real two-variable dataset. Build with OLS, Pearson r, alpha transparency, causation caveat. Audit.

**Exercise 8.5** — *Overplotting experiment.* Take a dense scatterplot dataset. Build it three ways: alpha transparency, jittering, 2D hexbin. Compare. Choose the right strategy for your context.

**Exercise 8.6** — *Heatmap from a correlation matrix.* Take a multi-variable dataset. Compute the correlation matrix. Build a heatmap of it with diverging color scale (zero at midpoint).

### Synthesis

**Exercise 8.7** — *Connected scatterplot.* Take a two-variable dataset that varies over time (a country's GDP and CO₂ emissions over decades; a company's revenue and employee count over years). Build a connected scatterplot. Compare to two separate line charts.

**Exercise 8.8** — *Parallel coordinates with brushing.* Take a multi-variable dataset (5+ variables). Build parallel coordinates with axis brushing. Test whether reordering axes reveals different patterns.

### Challenge

**Exercise 8.9** — *Cairo audit on a published chart.* Find a published correlation chart that you suspect makes a stronger causal claim than the data supports. Write the redesign that respects the data while preserving the chart's information.

**Exercise 8.10** — *Marginal histograms.* Build a scatterplot with marginal histograms along the x and y axes. Use Claude Code. Compare to the bare scatterplot.

---

## LLM Exercise — Chapter 8: Relationship Charts

**Project:** [TBD — selected after Chapter 00]

**The Prompt (audit + build):**

```
I have a relationship dataset of [DESCRIBE: variables, types, sample
size, what each variable represents]. The communication goal is
[DESCRIBE].

Walk me through:
1. Confirm the family is relationship/correlation.
2. Choose the form (scatterplot / bubble / connected scatter / parallel
   coordinates / heatmap).
3. For bubble charts, confirm area-not-radius encoding (Stevens' power
   law). For heatmaps, choose appropriate color scale type.
4. Specify channels per Chapter 1.
5. Specify the correlation-is-not-causation annotation explicitly
   (Cairo's ethical frame).
6. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + relationship-specific (overplotting
mitigation, area-not-radius, causation caveat).
```

**Connection to previous chapters:** Chapter 1 (Stevens' power law for bubble sizing), Chapter 2 (selection — relationship category), Chapter 3 (audit), Chapter 4 (workflow). Chapter 14 will revisit the design audit including ethical annotation requirements.

**Preview of next chapter:** Chapter 9 covers part-to-whole — pies, donuts, waffles, Marimekko, Nightingale rose. Where Chapter 8 used position for two variables, Chapter 9 will use angle (pies) or area (treemaps) for proportions, with the corresponding perceptual costs.

---

## Visual suggestions

This chapter is about relationship and correlation charts. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for relationship charts: [Scatterplot](36-scatterplot.md), [Bubble Chart](24-bubble-chart.md), [Parallel Coordinates](50-parallel-coordinates.md), [Heatmap](39-heatmap.md), [Parallel Sets](51-parallel-sets.md), [Connection Map](31-connection-map.md). Each Part II chapter has its own prompt.

### Figure 8.1 — The HAI scatterplot with correlation-not-causation annotation

The chapter's central worked example. A scatterplot of GDP per capita vs. AI capability index, with an OLS regression line and an explicit annotation naming the correlation-is-not-causation moral requirement. The chart makes Cairo's ethical frame literal: a scatterplot with no caveat is a chart that fails its reader.

See [Scatterplot](36-scatterplot.md) and [Bubble Chart](24-bubble-chart.md) in Part II for the canonical references.

```
Generate a scatterplot in D3 v7 with a correlation-coefficient readout and a moral-disclaimer annotation. Two files:

1. `chapter-08-fig-01.html` — full HTML with inline CSS and inline D3 v7. A scatterplot with OLS trend line, Pearson r live readout, and a prominent annotation. Page subtitle: "Correlation, with the moral disclaimer Cairo requires."

2. `chapter-08-fig-01/data.json` — the dataset.

Data shape:
- 50 countries with two attributes.
  - `country`: string
  - `gdp`: number — GDP per capita
  - `capability`: number — AI capability index

{DATA NEEDED} — World Bank GDP per capita + an AI capability index by country (Stanford AI Index, ITU AI Readiness, or similar). 50 countries spanning the income range.

Encoding:
- x-position: GDP per capita (log scale).
- y-position: AI capability index (linear).
- OLS regression line with shaded 95% confidence band.
- Pearson r computed and displayed in a small readout box.
- Annotation in a prominent box: "This chart shows that GDP and AI capability are correlated. It does not show that GDP causes AI capability or vice versa. Likely confounders: educational infrastructure, internet penetration, research investment, government policy. A causal claim requires evidence this chart cannot provide."

Style: warm monochrome — black, dark walnut, blood-red accents. The disclaimer box is in walnut, not buried.

Provide both files as separate code blocks.
```

---

## Further reading

- **Cairo, Alberto. (2019).** *How Charts Lie.* Chapter 2 develops the correlation-is-not-causation framing.
- **Stevens, S. S. (1957).** "On the Psychophysical Law." *Psychological Review.* The power-law mechanism behind area perception.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* Section on parallel coordinates.
- **The book's pantry** — `scatterplot.html`, `bubble-chart.html`, `heatmap.html`.

---

## Tags

relationship-charts, scatterplot, bubble-chart, connected-scatter, parallel-coordinates, heatmap, OLS, Pearson-r, Stevens-power-law, area-not-radius, correlation-is-not-causation, Cairo, Munzner, overplotting, alpha-transparency, hexbin, D3, Claude-Code
