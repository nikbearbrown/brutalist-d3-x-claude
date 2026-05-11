# Chapter 7 — Distribution Charts
*Shape, Spread, and Skew — Beyond the Mean.*

## Three suggested titles

- Distribution Charts: What Violin Plots Reveal That Box Plots Hide
- The Bin-Width Problem and the Graphicacy Cost of Each Form
- From Histograms to KDE: Showing the Spread

---

## Chapter overview

By the end of this chapter you will be able to build the family of distribution charts — histograms, box plots, violin plots, density (KDE) plots, stem-and-leaf — and know when each is right. You will know what a violin plot reveals that a box plot hides, why histogram bin width can hide bimodality or invent peaks that aren't there, and how Cairo's *graphicacy* concept becomes a practical design constraint when the audience does not have the statistical background to read the more information-dense forms.

---

## Learning objectives

1. **(Understand)** Explain what information a violin plot reveals that a box plot hides (multimodality, distribution shape) and vice versa (precise quartile values, outlier identification), using kernel density estimation as the mechanism.
2. **(Apply)** Build a box plot and violin plot for the same distribution dataset; identify which features of each distribution are visible in each form.
3. **(Analyze)** Diagnose a histogram where bin width obscures bimodality; specify the corrected bin width with reasoning.
4. **(Evaluate)** Select the most appropriate distribution chart for a specified audience graphicacy level and analytical goal, applying Cairo's concept that more complex forms require more graphicacy to decode.

---

## Opening case — the HAI box plot and the suburban subpopulation

Open `pantry/visualization/box-whisker.html` in a browser. Five box plots, side by side, one per residential zone (Urban Core, Inner Suburbs, Outer Suburbs, Exurban, Rural). Each box shows household income distribution for that zone — the Q1, median, Q3, and the whisker extent (1.5× IQR per Tukey's rule). Outlier points appear above or below the whiskers where they exist.

The Inner Suburbs box has an interesting feature: a cluster of outlier points sitting well above the upper whisker. The cluster suggests there's a high-income group within the Inner Suburbs that doesn't fit the rest of the distribution. The box plot reveals their existence. The box plot does *not* reveal whether the cluster is a separate sub-population (a bimodal distribution) or a long right tail of the same distribution.

This is the box plot's most consequential limitation. Box plots summarize distributions using five numbers: minimum, Q1, median, Q3, maximum. The five-number summary captures central tendency and spread efficiently, and lets the reader compare distributions across groups at a glance. But the five-number summary cannot distinguish between distribution *shapes*. A normal distribution and a bimodal distribution can have identical five-number summaries; the box plot will show them identically.

A violin plot answers the follow-up question. A violin plot is a density estimate (kernel density estimation, KDE) drawn symmetrically around a vertical axis. The width of the violin at any point represents the density of observations at that value. A bimodal distribution shows two bulges. A normal distribution shows a single symmetric bulge. A skewed distribution shows an asymmetric bulge.

The trade-off: a violin plot reveals shape but loses the precise five-number summary. The reader cannot read off the exact median or the exact Q1; they read the *envelope* of the density, not specific quartile values. Often this is the right trade. Sometimes it isn't.

This chapter is about that trade. The choice between box plot and violin plot — and between either of those and the histogram, density plot, or stem-and-leaf — depends on what the reader needs to see, and what graphicacy level the reader brings.

---

## Theoretical grounding — Tukey's box plot, Cairo's graphicacy, Heer & Bostock on histograms

This chapter draws on three sources, each at the moment its specific contribution is needed.

**John Tukey's box and whisker plot (1977).** Tukey's *Exploratory Data Analysis* introduced the box plot as a five-number summary: minimum, Q1, median, Q3, maximum. Tukey's specific design choices — the box from Q1 to Q3, the median line inside the box, the whiskers extending to the most extreme value within 1.5×IQR of Q3 (or Q1) — became the standard. The 1.5×IQR fence rule for outliers is empirical; Tukey chose it because it reliably separated genuine outliers from the natural tail of common distributions. Every design decision in the standard box plot traces back to Tukey's paper. Variations (notched box plots showing 95% confidence intervals around the median) appeared later but rest on the same five-number foundation.

**Cairo's concept of graphicacy.** Graphicacy is the audience's capacity to read visual representations of data. Just as literacy varies (some readers handle complex prose, others need simpler text), graphicacy varies (some readers handle violin plots, others need histograms with annotations). A chart that exceeds the audience's graphicacy is a failure of design — the chart is technically informative but practically useless to its readers. This chapter is where graphicacy becomes a *practical design constraint* rather than just a theoretical concept. Distribution charts span a wide graphicacy range: stem-and-leaf is accessible to general audiences; histograms are familiar to most college-educated readers; box plots require statistical training; violin plots require both statistical training and visualization training. The choice of form depends on who the reader is.

**Heer & Bostock (2010) on histogram perception.** The Heer-Bostock crowdsourced replication of Cleveland & McGill (Chapter 1) included tests on histogram and bar chart perception. The finding relevant here: bin choices substantially affect perceived distribution shape, and readers consistently misjudge the underlying distribution when bin width is poorly chosen. This is the empirical evidence that the histogram bin-width problem (Concept 3) is not a theoretical concern; it is a measurable perceptual failure that produces wrong conclusions.

---

## Concept 1 — Histograms: the bin-width problem

A histogram bins continuous data into discrete intervals and shows the count (or density) per bin as a column. The chart is the most common distribution form because it is taught in every introductory statistics class.

### When histograms work

- The dataset is large enough (typically n > 50, ideally n > 200) for the binning to produce stable patterns.
- The reader needs to see the distribution's shape — peaks, tails, gaps.
- The data is continuous or near-continuous (a histogram of integer counts 0–10 looks like a bar chart, which is fine).

### The bin-width problem

The defining design decision is the *bin width* — how wide each interval is. The choice has substantial consequences.

**Too few bins (too-wide bins).** The distribution's structure compresses into a smooth shape. Bimodality (two peaks) merges into a single broad peak. Skewness can be hidden. The chart shows less than the data contains.

**Too many bins (too-narrow bins).** Random noise in the data produces visual peaks that aren't real. The chart shows more than the data supports — apparent multi-modality that's actually sampling variation.

**Right bin width.** The structure of the distribution is visible; the noise is averaged out. The shape the reader sees corresponds to the underlying population.

There is no universal "right" bin width. Several rules of thumb provide starting points:

- **Sturges' rule:** k = ⌈log₂(n) + 1⌉ bins. Works for normal-ish distributions with moderate n.
- **Square-root rule:** k = ⌈√n⌉ bins. A common simple default.
- **Scott's rule:** bin width = 3.5σ / n^(1/3). Optimized for normal distributions.
- **Freedman-Diaconis rule:** bin width = 2 × IQR / n^(1/3). Robust to outliers; often the best default.

For Claude Code work: specify the bin width or the rule explicitly. "Use Freedman-Diaconis binning" or "bin width = 5" leaves no ambiguity. Letting Claude Code choose the default usually produces Sturges' rule or a similar conservative choice that misses fine structure.

### The bimodality test

If you suspect the distribution might be bimodal, test multiple bin widths. A bimodality that survives across several reasonable bin widths is real. A bimodality that appears at narrow bins and vanishes at wider bins is sampling noise. The test is: build the histogram with three bin widths (narrow, medium, wide). If the two peaks remain visible across all three, the bimodality is real.

If the bimodality is real, consider switching to a violin plot or KDE plot. The histogram form is least informative for showing genuine multi-modality; density-based forms are better.

> ### ↳ Dig Deeper — Bin-width sensitivity in your domain
>
> **Prompt:**
>
> > Pick a typical distribution dataset from my work (incomes, response times, scores, etc.). Compute Sturges, Scott's, and Freedman-Diaconis bin widths. Build histograms at each width with Claude Code. Compare what each reveals. Where do they agree on the distribution's shape? Where do they disagree, and which is more likely correct? Cite Heer & Bostock (2010) on histogram perception.
>
> **What to do with the output:** Save the comparison. The bin-width sensitivity analysis is the muscle the rest of this chapter builds.

---

## Concept 2 — Box and whisker plots

Tukey's box plot summarizes a distribution using five numbers and visualizes them with a specific shape.

### The standard form

- **Box:** spans Q1 (lower edge) to Q3 (upper edge). The box's height (or width, in horizontal orientation) is the IQR.
- **Median line:** horizontal line inside the box at Q2.
- **Whiskers:** extend from the box to the most extreme data point within 1.5×IQR of the box's edge. The whisker doesn't necessarily reach the data minimum or maximum.
- **Outliers:** individual points beyond the whiskers.

### What box plots show well

- **Cross-distribution comparison.** Five box plots side by side let the reader compare central tendency (median position), spread (IQR — box height), and outlier presence at a glance. This is what the HAI box plot does for residential zones.
- **Skewness.** When the median sits near one edge of the box, the distribution is skewed in that direction.
- **Outlier identification.** Tukey's 1.5×IQR rule produces a defensible flagging of unusual points.
- **Robustness to outliers.** Because box plots use quartiles (rank-based statistics) rather than means and standard deviations, they are not pulled by extreme values the way mean-based summaries are.

### What box plots hide

- **Distribution shape beyond skewness.** Bimodal, trimodal, and unusually shaped distributions look the same in box plots.
- **Within-quartile structure.** The box doesn't show how data is distributed within each quartile range.
- **Sample size.** Two box plots from samples of n=10 and n=10,000 look identical, but the inferential weight is dramatically different.

### Variations

- **Notched box plot.** Adds a "notch" around the median showing approximately the 95% confidence interval. Two notches that don't overlap suggests medians differ significantly.
- **Variable-width box plot.** Box width encodes sample size; wider boxes are larger samples.
- **Letter-value plot.** Tukey's extension showing more quantile boundaries (Q1, Q3, and finer divisions) for larger datasets.

For Claude Code work: the standard Tukey box plot is the default. Specify variations explicitly when needed. The pantry's `box-whisker.html` shows the standard form.

---

## Concept 3 — Violin plots and KDE

A violin plot draws a kernel density estimate (KDE) symmetrically around a vertical axis. The width at any point encodes the density of observations at that value.

### What KDE is

Kernel density estimation is a method for estimating a continuous probability density from a finite sample. Each data point contributes a small "kernel" function (typically Gaussian, sometimes Epanechnikov or other shapes) centered at the data value. The sum of all kernels produces a smooth density estimate.

The estimate has a parameter: the *bandwidth* (how wide each kernel is). Like the histogram bin width, the bandwidth choice matters:

- **Too narrow:** the estimate is rough and shows sampling noise as wiggles.
- **Too wide:** the estimate is over-smoothed and hides real features.
- **Right bandwidth:** the underlying distribution shape is visible; noise is suppressed.

D3's `d3-array` library and several KDE-specific libraries provide bandwidth-selection rules (Silverman's rule, Scott's rule). For Claude Code work, specify the bandwidth selection method or use a standard default.

### When violin plots win

- **Bimodal or multi-modal distributions.** The bulges in the violin reveal the modes.
- **Skewed distributions.** The asymmetric shape of the violin shows the skew direction.
- **Audiences with statistical literacy.** Readers comfortable with distribution shape concepts can extract more information from the violin than from the box plot.

### When violin plots fail

- **Audiences without statistical literacy.** A violin plot to a general audience is often unreadable. The form requires graphicacy that hasn't been built.
- **Small sample sizes (n < 40).** KDE on small samples produces unreliable shapes; the violin is mostly artifact.
- **Precise quartile reading.** The violin's edge isn't a clean Q1/Q3 boundary; readers can't read exact quartile values.

### The hybrid: box-violin

Many practitioners overlay a thin box plot inside the violin. The box gives the precise quartile values; the violin gives the shape. The hybrid form is denser but more informative — best for audiences with high graphicacy.

The pantry's `violin-plot.html` shows a standard violin form. Compare it to the `box-whisker.html` for the same data; the differences reveal what each form makes visible.

> ### ↳ Dig Deeper — Bandwidth selection
>
> **Prompt:**
>
> > Walk me through Silverman's rule, Scott's rule, and cross-validation for KDE bandwidth selection. Build a violin plot of a real bimodal distribution using each method. Compare the resulting shapes. Where do they agree? Where do they disagree, and which is more faithful to the underlying distribution? Cite the Heer & Bostock evidence on bin-width / bandwidth sensitivity.
>
> **What to do with the output:** Save the comparison. Bandwidth selection is the most under-discussed technical decision in violin plot work.

---

## Concept 4 — Stem-and-leaf and density plots

Two less-commonly-used forms deserve mention because they fill specific niches.

### Stem-and-leaf plots

Tukey introduced the stem-and-leaf plot for small datasets where you want to preserve the original data values while showing the distribution. The "stem" is the leading digit(s) of each value; the "leaf" is the trailing digit. Each value is represented by its leaf, placed next to its stem. The result is a textual chart that doubles as a sorted list of the actual values.

Stem-and-leaf plots win for:

- **Small datasets (n < 50).** Statistical inference is shaky for small samples; preserving raw values lets the reader inspect them directly.
- **Audiences without statistical graphicacy.** The plot is more readable than histograms for readers unfamiliar with binning.
- **Datasets where exact values matter.** A stem-and-leaf preserves all data; a histogram aggregates it.

The pantry's `stem-leaf.html` shows the form. It's an unusual chart to build in D3 (it's almost text-as-chart), but the form has a niche.

### Density plots without the violin shape

A simple density plot shows a KDE as a line on a coordinate plane (x = value, y = density). Multiple distributions can be overlaid as multiple lines. This is the form most often used in scientific publications for comparing distributions.

When to use density plots over violin plots:

- The reader needs to compare distributions directly (overlaid lines).
- Statistical literacy is assumed (the form is academic-publication standard).
- The comparison is between specific distributions, not many groups.

When to use violin plots:

- Multiple groups (5+) where overlay would be unreadable.
- The shape of each distribution is the primary message.

---

## Mid-chapter checkpoint

Pick a distribution dataset you have on hand. Walk through the form selection: histogram (audiences without statistical training), box plot (cross-group comparison, robust statistics), violin plot (bimodality or skew matters), density plot (overlaid comparison), stem-and-leaf (small dataset, preserve values). Justify the choice using the audience's graphicacy level and the question being asked.

Then identify the binning/bandwidth decision the chart requires. What rule will you use, and why?

You should be able to do this in 90 seconds. If you cannot, the dataset is unusual or the audience is unspecified.

---

## Extended worked example — building the HAI box plot with Claude Code

The HAI box plot in `pantry/visualization/box-whisker.html` shows simulated AI capability scores across five cognitive domains. Walk the full pipeline.

### Step 1 — Apply Chapter 3 (read the dataset)

Five domains × 80 simulated observations each. Domain (categorical, 5 values, no inherent order). Score (quantitative, range 10–100, ratio scale).

Communication question: "How does the distribution of AI capability scores compare across cognitive domains?"

Cairo "compared with what?" — the comparison is across the five domains, on multiple distribution features (median, spread, outliers).

### Step 2 — Apply Chapter 2 (select the chart)

Functional category: distribution. Multiple groups → cross-group distribution comparison. The standard form for this is box plot.

Why not violin plot? The audience is a research summary — graphicacy is moderate, the comparison is multi-group (5 panels would crowd at violin width), and the precise quartile values matter for the analysis. Box plot wins.

Why not histogram? Five separate histograms takes too much space and makes cross-group comparison difficult.

### Step 3 — Apply Chapter 1 (channel decomposition)

- Marks: rectangles (boxes), lines (whiskers and median), points (outliers).
- x-position: domain (categorical, 5 values, sorted by median for ranking readability).
- y-position: score (quantitative, range 10–100).
- Box top: Q3.
- Box bottom: Q1.
- Median line: Q2.
- Whisker top: max value within Q3 + 1.5×IQR.
- Whisker bottom: min within Q1 − 1.5×IQR.
- Outlier points: beyond 1.5×IQR fences.
- Color hue: domain identity (redundant with x-position; supports legend).

### Step 4 — Write the four-move prompt

```
**Show what I have:**
Five domains, 80 observations each. Domain (string), score (number,
10-100). Sample data file: data/ai-capability-distribution.csv

See pantry/visualization/box-whisker.html for the visual pattern.

**Say what I want:**
Box and whisker plot in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: rectangle (box), line (median, whiskers), point (outliers).
- x-position: domain (categorical, sorted by median descending).
- y-position: score (quantitative, range 10-100, shared y-axis across
  all boxes for direct comparison).
- Box top edge: Q3 (75th percentile).
- Box bottom edge: Q1 (25th percentile).
- Whisker top: max value within Q3 + 1.5*IQR (Tukey's rule).
- Whisker bottom: min value within Q1 - 1.5*IQR.
- Median: horizontal line at the 50th percentile inside the box.
- Outliers: points beyond 1.5*IQR fences.
- Color hue: domain identity, redundant with x-position. Use a
  five-color palette: #8B0000, #5C3317, #6B6B5E, #4A4A4A, #9B957F.
- y-axis ticks at 0, 25, 50, 75, 100.
- x-axis labels rotated -30 degrees.
- Subtitle: "AI Capability Score Distribution by Cognitive Domain
  (n=80 per domain)".
- Margins: top 60, right 40, bottom 60, left 60.
- Dark mode support.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements each statistical channel (Q1, Q3,
median, whiskers, outliers). List any decisions not specified above.
```

### Step 5 — Audit

Standard Evergreen/Emery subset plus distribution-specific checks:

- Box top is Q3 (not Q4); box bottom is Q1 (not Q0).
- Whiskers follow Tukey's rule (1.5×IQR), not min/max of all data.
- Outliers are flagged as individual points beyond the whiskers.
- Median line is inside the box, not on the box edge.

The most common Claude Code failure: the "box" shows min-to-max range instead of Q1-to-Q3. The chart looks like a box plot but communicates very different information. Catch this in the audit; the follow-up prompt is "the box should span Q1 to Q3 (the IQR), not min to max. Tukey's rule for the whiskers is max within Q3 + 1.5×IQR; outliers are points beyond. Regenerate."

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build a histogram, box plot, violin plot, density plot, or stem-and-leaf plot — choosing the form based on the dataset's size, the audience's graphicacy, and what the communication question demands.

You can apply the bin-width / bandwidth decision rules (Sturges, Scott, Freedman-Diaconis for histograms; Silverman, Scott for KDE) and recognize when the choice substantially changes what the chart reveals.

You can name what a violin plot reveals that a box plot hides (multi-modality, distribution shape) and what a box plot shows that a violin plot doesn't (precise quartile values, robust outlier flagging via Tukey's rule).

You can apply Cairo's graphicacy concept as a practical design constraint: distribution charts span a wide graphicacy range, and the right form depends on what your audience can read.

The thing to watch for, going forward, is the temptation to use whatever distribution chart is most familiar to you regardless of the audience. The right chart for a paper read by statisticians is rarely the right chart for a public-policy briefing. The form follows the audience.

---

## Key terms

- **Histogram.** Continuous data binned into discrete intervals; column per bin shows count or density.
- **Box plot.** Tukey's five-number-summary visualization: box from Q1 to Q3, median line, whiskers to 1.5×IQR, outlier points.
- **Violin plot.** KDE drawn symmetrically around a vertical axis; width encodes density at each value.
- **Kernel density estimation (KDE).** Method for estimating a smooth probability density from a finite sample.
- **Bin width.** Histogram's defining design decision. Rules: Sturges, Scott, Freedman-Diaconis.
- **Bandwidth.** KDE's defining design decision. Rules: Silverman, Scott.
- **Tukey's 1.5×IQR rule.** Whisker extends to most extreme value within 1.5×IQR; points beyond are outliers.
- **Stem-and-leaf.** Small-dataset distribution form that preserves raw values.
- **Graphicacy (Cairo).** The audience's capacity to read visual representations of data; varies across audiences and across chart forms.

---

## Discussion questions

1. The box plot vs. violin plot trade-off is shape-vs-precision. When does each side win? Cite specific audience and communication-question contexts.
2. Histogram bin width substantially changes what the chart reveals. Why is this not a violation of "show the data"? Or is it?
3. Stem-and-leaf plots are unusual in modern publications. What do they offer that newer forms don't?
4. KDE produces a smooth shape from sample data. Smoothing always introduces bias. When is the bias acceptable, and when does it matter for the inferential conclusion?
5. *Cross-chapter synthesis.* Chapter 8 (relationship/correlation) will introduce scatterplots. A scatterplot of two variables shows joint distribution. Frame the relationship between Chapter 7's univariate distribution charts and Chapter 8's bivariate joint-distribution charts.

---

## Exercises

### Warm-up

**Exercise 7.1** — *Form selection by audience.* For each of the following, select the right distribution form:
- Income distribution within a single ZIP code, presented in a community town hall.
- Response time distribution for a clinical trial, in a peer-reviewed paper.
- Test score distribution across five schools, for a school board.
- Distribution of survey responses on a 1–5 Likert scale.

**Exercise 7.2** — *Bin-width diagnosis.* You see a histogram of household incomes with bin width $10,000, showing a single broad peak. Suspect bimodality. How do you test for it? What bin widths should you try?

**Exercise 7.3** — *Tukey's rule application.* Given a dataset with Q1 = 25, Q3 = 75, IQR = 50, what is the whisker extension? At what value do points become outliers?

### Application

**Exercise 7.4** — *Box plot vs. violin plot, same data.* Take a real distribution dataset. Build it as both a box plot and a violin plot with Claude Code. Compare what each reveals. Identify which is right for your professional context and audience.

**Exercise 7.5** — *Bin-width experiment.* Take a dataset that may be bimodal. Build histograms at three bin widths (Sturges, Scott, Freedman-Diaconis). Compare. Apply the bimodality test from Concept 1.

**Exercise 7.6** — *Audit a published distribution chart.* Find a histogram, box plot, or violin plot in a recent publication. Audit using Evergreen/Emery plus distribution-specific checks. Identify any failures.

### Synthesis

**Exercise 7.7** — *Graphicacy audit.* Take a distribution chart you produced. Estimate the audience's graphicacy. Is your form appropriate? If not, what is the fallback that maintains the message?

**Exercise 7.8** — *Multi-form comparison.* Take a single dataset. Build five forms: histogram, box plot, violin plot, KDE line plot, stem-and-leaf. Compare. Which best supports each of three different communication questions you can identify for the data?

### Challenge

**Exercise 7.9** — *Hybrid box-violin.* Build a hybrid plot that overlays a thin box on a violin. Use Claude Code. Compare to either form alone.

**Exercise 7.10** — *Bandwidth selection from data.* Implement cross-validation bandwidth selection for a KDE in D3 + Claude Code. Compare to Silverman's rule on the same data. When does each win?

---

## LLM Exercise — Chapter 7: Distribution Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A distribution chart selected for a specific audience and built with the bin/bandwidth decision documented.

**Tool:** Claude Code (build) + Claude chat (audit).

---

**The Prompt (audit + build):**

```
I have a distribution dataset of [DESCRIBE: rows, single quantitative
variable, sample size, any group structure]. The audience is [DESCRIBE:
graphicacy level, statistical training assumed].

Walk me through:
1. Confirm distribution family.
2. Choose form (histogram / box / violin / density / stem-and-leaf)
   based on audience and communication question.
3. For histograms: name the bin-width rule. For KDE-based forms: name
   the bandwidth selection method.
4. Specify channels per Chapter 1.
5. Apply Tukey's rule (for box plots) explicitly.
6. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + distribution-specific checks (correct box
boundaries, correct whisker rule, correct binning).
```

---

**What this produces:** Audit document plus distribution chart. Save as `chapter-07-distribution-audit.md` and `chapter-07-distribution.html`.

**Connection to previous chapters:** Chapter 1 (channels for distribution), Chapter 2 (selection — distribution category), Chapter 3 (audit — graphicacy assessment), Chapter 4 (workflow).

**Preview of next chapter:** Chapter 8 introduces relationship/correlation charts — scatterplots, bubble charts, parallel coordinates, heatmaps. The questions shift from "what does this variable's spread look like" to "how do these variables relate."

---

## Visual suggestions

This chapter is about distribution-chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for distribution charts: [Histogram](40-histogram.md), [Box Plot](21-box-plot.md), [Box and Whisker Plot](22-box-whisker.md), [Violin Plot](77-violin-plot.md), [Density Plot](32-density-plot.md), [Stem and Leaf Plot](68-stem-leaf.md), [Multimodal Distribution](45-multimodal-distribution.md), [Population Pyramid](55-population-pyramid.md), [Error Bars](36-error-bars.md). Each Part II chapter has its own prompt.

### Figure 7.1 — Same data, three distribution charts

The chapter's central comparison. The same simulated AI-capability score dataset rendered three ways: histogram, box plot, and violin plot. The reader sees what each chart reveals and what each one hides.

See [Histogram](40-histogram.md), [Box Plot](21-box-plot.md), and [Violin Plot](77-violin-plot.md) in Part II for the canonical references.

```
Generate a 3-panel distribution comparison in D3 v7. Two files:

1. `chapter-07-fig-01.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering the same source data with a different distribution chart. Page subtitle: "Same data, three views — what each chart reveals and hides."

2. `chapter-07-fig-01/data.json` — the dataset.

Data shape:
- 80–120 simulated values in a known mixture distribution (so bimodality is genuinely present).
  - `values`: array of numbers.

{DATA NEEDED} — Any dataset where bimodality is plausible (response times, test scores by mixed-ability cohort, agency capacity scores spanning new and mature programs). Or simulate a Gaussian mixture for the demonstration.

Panel 1 — histogram: 15–20 bins, bar height = frequency.
Panel 2 — box plot: five-number summary, Tukey 1.5×IQR whiskers, outlier dots.
Panel 3 — violin plot: KDE with overlaid box plot, Silverman bandwidth.

Caption beneath each panel names what it reveals (histogram: bin frequency, multimodality if visible; box plot: quartiles, outliers, skew; violin: full shape, multimodality always visible).

Style: warm monochrome. Same x-axis range across all three panels so the reader can align them visually.

Provide both files as separate code blocks.
```

---

## Further reading

- **Tukey, John W. (1977).** *Exploratory Data Analysis.* Addison-Wesley. The original box plot.
- **Silverman, B. W. (1986).** *Density Estimation for Statistics and Data Analysis.* Chapman & Hall. KDE bandwidth selection.
- **Wilke, Claus O. (2019).** *Fundamentals of Data Visualization.* O'Reilly. Chapter 7 on distributions is the modern standard.
- **The book's pantry** — `histogram.html`, `box-whisker.html`, `violin-plot.html`, `stem-leaf.html`.

---

## Tags

distribution-charts, histogram, box-plot, violin-plot, KDE, kernel-density-estimation, stem-and-leaf, Tukey, bin-width, bandwidth, graphicacy, Cairo, Heer-Bostock, multimodality, D3, Claude-Code
