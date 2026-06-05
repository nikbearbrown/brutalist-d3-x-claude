# Chapter 10 — Relationship and Correlation Charts
*Two Variables and the Question They Refuse to Settle.*

---

Here is a chart. Each point is a country. The x-axis shows the education index — a composite score between 0 and 1 measuring school enrollment and years of schooling. The y-axis shows life expectancy in years. There are about 170 points. An OLS regression line runs through the cloud, sloped upward and to the right. Pearson's r is annotated near the line: r = 0.79.

The chart shows a strong positive correlation. Countries with higher education indices tend to have longer life expectancy. r = 0.79 is a substantial association. A reader looking at this chart, without anything else to go on, will naturally form the thought: better education leads to longer life.

That thought is not what the chart shows.

The chart shows a statistical association. Whether education *causes* longer life, whether longer-life-expectancy countries invest more in education, whether both are caused by a third variable — institutional quality, wealth, political stability, nutrition — the chart cannot say. The OLS line fits the cloud. It does not identify a causal mechanism. Every statistics textbook says this. Every scatterplot that omits the caveat invites the reader to forget it.

Alberto Cairo's frame is specific: a scatterplot showing strong correlation, without an explicit annotation distinguishing correlation from causation, invites the reader to make the causal inference. The chart's visual force exceeds its empirical claim. This is not a stylistic oversight. It is a moral failure. The designer's professional responsibility includes preventing the over-reading that the chart's visual authority would otherwise produce.

The fix is short. Add a text block near the trend line: "Correlation does not imply causation. These variables are associated; the causal mechanism is not established by this chart." The caveat does not weaken the chart. It completes it. The reader now knows what is and is not being claimed.

<!-- → [FIGURE: Two identical scatterplots side by side. Same 170-country education-index vs. life-expectancy dataset, same OLS trend line, same r = 0.79 annotation. Left: no causation caveat — the chart invites the causal inference. Right: a visible callout box near the trend line reads "Correlation does not imply causation. These variables are associated; the causal mechanism is not established by this chart." Caption: "Same chart. Left invites an inference the data cannot support. Right completes the claim. The caveat is not decoration — it is the difference between a chart that misleads and one that informs."] -->

This chapter is about the family of relationship charts and the design responsibilities that come with them. The scatterplot is the canonical form. Bubble charts, connected scatterplots, heatmaps, and parallel coordinates are extensions for specific analytical situations. Each form has its own channel rules, its own failure modes, and its own version of the ethical obligation Cairo names.

---

## What a Scatterplot Actually Is

A scatterplot has two quantitative axes and a point mark for each observation at the (x, y) coordinate corresponding to its values. The channels are x-position and y-position — the two highest-accuracy channels from the Cleveland and McGill ranking. The marks are points. The form shows how two variables co-vary.

The convention: the independent variable — the one the designer suspects is the predictor or cause — goes on the x-axis. The dependent variable — the one being predicted or caused — goes on the y. The convention matters because readers default to reading x as input and y as output. If the designer places variables arbitrarily, the reader imports a causal story the designer did not intend.

The OLS regression line is the standard addition. It summarizes the linear relationship: for each unit increase in x, the line predicts a given increase in y. Pearson's r measures the strength of the linear association: 0 is no association, 1 is perfect positive correlation, −1 is perfect negative. Both statistics are honest summaries of the data. Neither is a causal claim. The chart that reports them without annotation leaves the reader to make the inference.

The scatterplot's strength is the cloud shape. Not just the trend line — the whole shape of the scatter. A linear cloud and a curved cloud have the same r if the curve is symmetric; they have different implications for the relationship. A cloud with a consistent band width is homoscedastic; a fan-shaped cloud where variance increases with x is heteroscedastic. An outlier ten standard deviations from the trend line may be a data error or the most important observation. None of these is visible in a summary statistic. The scatterplot shows them all.

<!-- → [FIGURE: Four small scatterplot panels, each with the same r ≈ 0.7 annotated. Panel 1: linear cloud — what the trend line correctly summarizes. Panel 2: curved (quadratic) cloud — r = 0.7 is technically correct but the relationship is non-linear; the linear trend line misrepresents it. Panel 3: fan-shaped cloud (heteroscedastic) — r = 0.7 but variance increases with x; the model is unstable at high x. Panel 4: linear cloud with one extreme outlier — r = 0.7 is dominated by the outlier; removing it gives r ≈ 0.3. Caption: "The same r = 0.7 can describe any of these clouds. The number summarizes; the chart shows. Always look at the cloud, not just the statistic."] -->

---

## The Overplotting Problem

When sample size is large and points cluster, the standard scatterplot fails. The dense region becomes a black blob. The cloud shape disappears under the ink. The outliers become invisible relative to the mass. A scatterplot of 50,000 transactions or 10 years of daily measurements hits this problem immediately.

Three strategies mitigate it:

**Alpha transparency.** Set point fill opacity low — 0.1 to 0.3. Each individual point is faint; dense regions accumulate alpha and appear darker; sparse regions remain visible as individual points. The cloud shape returns. This is the simplest strategy and almost always the right first move. It preserves the point-level structure while revealing the density structure simultaneously.

**Jittering.** Add small random offsets to point positions. Useful when many points have identical or near-identical values — which happens with discrete variables (ratings from 1 to 5, integer measurements) or with rounded data. Without jittering, a scatterplot of discrete data shows only a small grid of dot clusters; with jittering, the count at each (x, y) position becomes visible as a local cloud.

**2D binning.** Aggregate points into a 2D grid (rectangular or hexagonal) and show count per cell as color luminance — a hexbin chart. This converts the point cloud into a density display. Hexagonal binning is preferred over rectangular because hexagons tile without directional bias. The trade-off: individual outliers disappear into their bins; the cloud shape is revealed at the cost of exact positions.

The right strategy depends on what the reader needs to see. If individual points matter (each is a named country, a specific patient, a unique transaction that might be wrong), alpha transparency preserves point-level information. If the distribution shape is the question (where do most of the 100,000 points live?), 2D binning answers it more clearly. If the data has discrete clustering, jittering reveals structure that alpha cannot.

These strategies belong in the "Constrain it" block of the Claude Code prompt. The default scatterplot will overplot on dense data. Specify: "use alpha transparency 0.2" or "use hexagonal 2D binning with d3.hexbin" or "jitter x-positions by up to 0.5 units." Without explicit instruction, Claude Code renders the default, and the default for large n is a black mass.

<!-- → [FIGURE: Four-panel comparison using the same 10,000-point dataset. Panel 1: full opacity — dense region is a solid black mass, cloud shape invisible. Panel 2: alpha transparency 0.15 — cloud shape visible, individual outliers preserved, density gradient clear. Panel 3: jittered — useful only if the data had discrete clustering (this panel works best with a discrete-variable dataset). Panel 4: hexagonal 2D binning — density shown as luminance gradient, individual points lost, useful when the distribution shape is the question. Caption below each panel names the strategy, what it reveals, and what it hides.] -->

---

## Bubble Charts and the Radius Trap

A bubble chart is a scatterplot with a third variable encoded as point size. The two position channels carry the first two variables; the size channel carries the third.

Size, as a channel, is area perception. And area perception follows Stevens' power law with an exponent of approximately 0.7: a doubled area looks 1.5 to 1.7 times larger, not twice as large. This is the sublinear perception that Chapter 3 established. The bubble chart lives inside this perceptual cost. The question is how to minimize it.

The question of whether to encode size as *radius* or *area* is not a question of taste. It is a question of what the eye receives.

If you scale the bubble's **radius** linearly with the value, a value that doubles produces a bubble whose radius doubles — and whose **area** quadruples. The eye, applying Stevens' law to the quadrupled area with exponent 0.7, perceives something roughly 2.6 times as large. The data said 2×. The chart delivered 4×. The eye reads 2.6×. Three different numbers, none of which matches.

If you scale the bubble's **area** linearly with the value, a value that doubles produces a bubble whose area doubles. The eye perceives it as roughly 1.5× to 1.7× as large. The data said 2×. The chart delivered 2×. The eye reads 1.6×. Two of the three numbers match; only Stevens' compression remains.

There is no way to eliminate Stevens' compression entirely — it is a fact of human perception, not a chart design choice. But the radius encoding compounds it with an avoidable squared distortion. Area encoding removes that compounding and leaves only the perceptual distortion that cannot be designed away.

<!-- → [FIGURE: Two bubble pairs side by side, each showing a small bubble (value 100) and a large bubble (value 200). Left pair: radius-linear encoding. Small bubble radius = 10px; large bubble radius = 20px. Area ratio = 4:1. Stevens' perceived ratio ≈ 2.6:1. Three annotated numbers: "Data: 2×. Area: 4×. Perceived: 2.6×. None match." Right pair: area-linear encoding (d3.scaleSqrt). Small bubble area = 100 units; large bubble area = 200 units. Radius ratio ≈ 1.41:1. Stevens' perceived ratio ≈ 1.6:1. Three annotated numbers: "Data: 2×. Area: 2×. Perceived: 1.6×. Two match." Caption: "Radius encoding makes a bad situation worse. Area encoding makes it as good as human perception allows."] -->

The D3 implementation is specific: `d3.scaleSqrt` maps the value to the radius such that the area is proportional to the value. The function applies the square root to the input (because radius = sqrt(area/π), up to a constant), producing a radius that gives the right area. `d3.scaleLinear` for bubble radius is the common error; it produces radius-linear encoding, area-quadratic distortion, and a chart that visually amplifies large values far beyond what the data supports.

For the Claude Code prompt, the specification is explicit and non-negotiable: "Use `d3.scaleSqrt` for the bubble radius scale. The bubble's visual area must be proportional to the value. Do not use `d3.scaleLinear` for the radius." The follow-up when it comes back wrong:

> "The bubble radius is scaled linearly. This makes visual area scale as value squared — a Stevens' power law violation. Replace `d3.scaleLinear` with `d3.scaleSqrt` for the radius scale and regenerate."

The bubble chart earns its three-channel complexity only when the third variable genuinely matters for the reader's question. If the size variable does not add much beyond the two position channels — if the reader's question is answered by x and y alone — drop the size and use a clean two-variable scatterplot. The channel cost (Stevens' area compression) is only worth paying when the third dimension justifies it.

---

## Heatmaps: Position Traded for Density

A heatmap is a 2D grid where each cell's color encodes a value. The channels are x-position (categorical or continuous), y-position (categorical or continuous), and color luminance (for the magnitude at each intersection).

The heatmap appears in several analytical contexts:

**Two categorical variables with an intensity value.** A matrix of regions (rows) by sectors (columns), with color luminance encoding adoption rate per cell. Each cell is a single number; the chart shows patterns across all combinations at once.

**Correlation matrix.** A square grid of variables, each cell showing the Pearson r between two variables. Color scale is diverging: one hue for negative correlations, white or gray at zero, a second hue for positive correlations. The reader can scan the matrix for clusters of correlated variables faster than they can read a table.

**Joint distribution of two quantitative variables.** This is the 2D-binning strategy applied to a scatterplot: divide the (x, y) space into a grid, count observations per cell, color by count. The result shows where the cloud is densest without the individual-point clutter.

The critical design decision is the color scale type:

- **Sequential** (single hue, varying luminance from pale to dark): for unipolar data, where zero or near-zero is one end of the meaningful range.
- **Diverging** (two hues, meeting at a neutral midpoint): for bipolar data, where zero is meaningful — correlations (−1 to +1), temperature anomalies (negative to positive), profit/loss.

The most common heatmap error is using a categorical or rainbow color scale for intensity — encoding a magnitude channel with an identity channel. As Chapter 3 established, hue is an identity channel; it distinguishes categories but cannot be ranked. A rainbow-colored heatmap forces the reader to remember which color corresponds to which magnitude, a task that varies by the reader's ability to hold a legend in working memory. Sequential or diverging luminance scales are magnitude channels and communicate intensity directly.

The second design decision is sort order. For categorical axes, the default is often alphabetical or source-file order — usually wrong. Sort rows and columns to reveal structure: by maximum value (which row has the highest intensity overall?), by hierarchical clustering (which rows are most similar to each other?), or by a domain-specific order the reader expects. The heatmap's visual pattern is highly dependent on ordering; the right order makes clusters visible, the wrong order hides them.

<!-- → [FIGURE: Two heatmaps side by side, same dataset (8 regions × 6 sectors, luminance = adoption rate). Left: alphabetical row and column order — no visible pattern, cells appear random. Right: rows sorted by maximum value (highest-adoption region at top), columns sorted by average value across regions (highest-adoption sector at left) — a bright upper-left cluster is immediately visible, showing that certain high-adoption regions concentrate in specific sectors. Caption: "Same data, two orderings. Left hides the pattern. Right reveals it. Sort order is a design decision, not a default."] -->

---

## Parallel Coordinates: When Dimensions Multiply

A scatterplot encodes two variables. A bubble chart encodes three. What about five variables, or ten?

Parallel coordinates solve this by drawing multiple vertical axes side by side, one per variable, and representing each observation as a polyline that connects its values on all axes simultaneously. A dataset with 200 observations and six variables produces 200 polylines, each crossing all six axes. Observations with similar profiles produce similar-looking lines; divergent observations produce crossing lines.

The form's advantage: it generalizes the scatterplot to any number of dimensions using the highest-accuracy channel (position) on each axis. The reader can see, at once, how all variables relate to each other for a given observation.

The form's fundamental limitation, named by Tamara Munzner: the visual pattern depends entirely on axis order. A dataset with six axes has 720 possible orderings (6! = 720). Each ordering makes different pairwise relationships visible and hides others. Two adjacent axes show their relationship clearly (the polylines connect them directly); non-adjacent axes show only the indirect relationship mediated by the axes between them.

This limitation is manageable when the chart is interactive — the reader can drag axes, reorder them, brush to filter subsets, and explore the space of orderings. It is severe when the chart is static — one ordering is chosen, and patterns visible in other orderings are invisible.

For Claude Code work: specify the axis order in the prompt (name the variables in the order that makes the most important pairwise relationships adjacent) and include axis brushing in the interaction requirements. A static parallel coordinates chart without brushing is often outperformed by a matrix of pairwise scatterplots.

<!-- → [FIGURE: Two parallel coordinates charts, same dataset (six quantitative variables, 200 observations). Left: original axis order (alphabetical or source-file order) — the polyline patterns look tangled with no clear structure. Right: reordered axes placing the two most correlated variable pairs adjacent — two clear clusters emerge, visible as distinct bands of parallel lines. Annotation between the panels: "Axis order 1 hides the clusters. Axis order 2 reveals them. Same data. 720 possible orderings. This is Munzner's axis-order-dependence problem." Annotation on the right panel: "These two orderings were selected by placing the highest-r pairs adjacent."] -->

---

## Connected Scatterplots: Time as the Third Dimension

A connected scatterplot is a standard scatterplot with the points connected in temporal order by a line. The form shows two quantitative variables co-varying over time — the path between (x, y) positions is itself the data.

The canonical case: GDP and CO₂ emissions for one country, one point per year from 1970 to 2020. A standard scatterplot shows the cloud of points; a connected scatterplot shows how the country moved through that cloud over time. The path might show a phase where GDP rose with emissions (industrialization), followed by a phase where GDP rose while emissions stabilized (efficiency), followed by a phase where GDP continued rising while emissions declined (decarbonization). None of that trajectory is visible in the cloud without the connecting path.

The design decisions are simple:

- Time direction must be explicit. Color luminance along the path (pale at early dates, dark at late) encodes time. Arrowheads at intervals reinforce direction. Annotations at key dates label pivotal moments.
- Smoothing is usually `d3.curveLinear` — straight segments between annual points. Aggressive smoothing introduces visual artifacts.
- The axes are standard scatterplot conventions: both quantitative, independent variable on x if one exists.

The form is uncommon enough that it requires a brief orientation for unfamiliar readers. A caption note — "Each point is one year; the line shows the path in order" — prevents the reader from interpreting the line as a trend across the scatterplot rather than a time path through it.

---

## Cairo's Frame Applied Precisely

Every chapter has mentioned Cairo's ethical frame. This chapter is where it is most specific.

The correlation-is-not-causation problem is structural to the scatterplot. The visual force of a tight cloud around an upward-sloping trend line, with r = 0.79 annotated, is persuasive. The reader's default inference is directional: x leads to y, or y follows from x. The chart did not claim this. The chart showed association. But the visual grammar of the scatterplot — independent variable on x, dependent on y, upward-sloping line — mimics the grammar of causation.

Cairo's frame: when the chart's visual force exceeds its empirical claim, the designer has a professional responsibility to close the gap. Not by weakening the chart. Not by hiding the correlation. By annotating explicitly what the chart shows and what it does not.

The annotation belongs in the chart as text, not in a caption below it or a footnote at the bottom of the report. The reader who looks at the chart must see the caveat in the same visual field as the chart that invites the inference. A footnote does not discharge the responsibility. A methods section does not discharge it. The annotation does.

For Claude Code prompts, specify this annotation explicitly: "Add a text annotation in a visible callout box: 'Correlation does not imply causation. These variables are associated; the causal mechanism is not established by this chart.' Position the annotation inside the chart area, near the trend line." Without explicit specification, Claude Code will not add it. And without the annotation, the chart invites an inference the data does not support.

---

## How This Changes the Prompt

Every form in this chapter has a specific specification that must appear in the "Constrain it" block.

**Scatterplots:** overplotting strategy named (alpha, jitter, or hexbin); OLS trend line requested; Pearson r annotation requested; correlation-is-not-causation annotation text provided verbatim.

**Bubble charts:** `d3.scaleSqrt` specified explicitly for the radius scale; the word "area" in the size description ("bubble area encodes population"); "NOT d3.scaleLinear" if necessary to prevent the default error.

**Heatmaps:** color scale type named (sequential or diverging); sort order specified (alphabetical, by maximum, by clustering); cell labels requested if exact values matter; color-blind-safe palette specified.

**Parallel coordinates:** axis order named (most important pairwise relationships adjacent); brushing interaction specified; tooltip on hover for individual observation values.

**Connected scatterplots:** time direction encoding named (color luminance along path, or arrowheads); annotation note explaining "each point is one [time unit]"; key dates annotated.

The chapter's content — the perceptual mechanisms, the failure modes, the ethical requirements — becomes the "Constrain it" block. The prompt does not re-derive the mechanism; it specifies the consequence of the mechanism. "Use d3.scaleSqrt" is the consequence of Stevens' power law. "Add the correlation-is-not-causation annotation" is the consequence of Cairo's frame. The Chapter 3 vocabulary produces the specification.

---

## The Feynman Test

The test for this chapter: next time you see a scatterplot with a strong correlation, ask three questions.

First: is there an explicit annotation distinguishing the correlation from a causal claim? If not, the chart has failed its reader by omission, regardless of how well it is otherwise built.

Second: if the chart is a bubble chart, is the size encoding radius-proportional or area-proportional? Scale by the fourth or fifth data point on the size axis. Is the large bubble visually 4× the small one, or 2×? Radius encoding produces 4×; area encoding produces 2×. The difference is visible.

Third: is the overplotting handled? If the chart has more than a few hundred points and the cloud is a solid mass, the cloud shape is hidden. The form is not doing its job.

If you can answer all three in thirty seconds, you know the chapter. The perceptual mechanisms — Stevens' law, the channel hierarchy, the structure of the visual authority a chart carries — are now in your diagnostic vocabulary. The ethical obligation — the annotation that closes the gap between what the chart shows and what it invites the reader to infer — is in your professional vocabulary.

The scatterplot is the most honest form in this book, in the sense that its channels are the most accurate ones available. It is also among the most morally demanding, because the inference it invites is the most tempting one in data analysis. Correlation is not causation. The chart must say so.

---

## Exercises

### Warm-up

**Exercise 10.1 — Form selection.** For each of the following, name the right relationship form (scatterplot, bubble chart, connected scatterplot, heatmap, or parallel coordinates) and justify the choice in one sentence:

- Two quantitative variables across 200 country observations; the question is cloud shape and trend.
- Two quantitative variables across 80,000 individual transactions; the question is where density concentrates.
- Three quantitative variables per country; one is population and is the "weight" of each observation.
- Five quantitative variables across 100 hospitals; the question is multivariate profile comparison.
- Two categorical variables (8 regions × 6 sectors) with a numeric intensity value per cell.

**Exercise 10.2 — Bubble-chart audit.** Find a published bubble chart. (a) Determine whether it encodes the third variable by radius or by area — scale two points whose ratio you can estimate and see whether the visual ratio matches the radius ratio or the area ratio. (b) If it uses radius encoding, calculate the three-number problem: what the data ratio is, what the area ratio is, and what Stevens' law predicts the perceived ratio to be (use exponent 0.7). (c) Specify the redesign.

**Exercise 10.3 — Causation diagnosis.** Find three published scatterplots with trend lines. For each: (a) does it carry an explicit correlation-is-not-causation annotation? (b) Does the axis convention (independent variable on x) match the directional inference the reader would naturally form? (c) If the annotation is absent, write the one-sentence caveat that should be added, placed inside the chart area near the trend line.

### Application

**Exercise 10.4 — Build a scatterplot with Claude Code.** Take a real two-variable dataset. Write the four-move prompt specifying: OLS trend line, Pearson r annotation, overplotting mitigation (alpha, jitter, or hexbin — choose based on sample size and data type), and the correlation-is-not-causation annotation verbatim. Run, audit, iterate to publishable.

**Exercise 10.5 — Overplotting experiment.** Take a scatterplot dataset with at least 5,000 points. Build it three ways with Claude Code: full opacity, alpha transparency at 0.15, and hexagonal 2D binning. Compare what each reveals and hides. Identify a specific observation (an outlier, a cluster, a gap) that is visible in one version and not in another.

**Exercise 10.6 — Heatmap design.** Take a dataset with two categorical variables and an intensity value per combination (e.g., regions × sectors, countries × years). Determine whether the color scale should be sequential or diverging by checking whether zero is a meaningful midpoint. Build the heatmap with Claude Code, specifying sort order (not alphabetical — sort by row maximum or by clustering). Audit the color scale choice.

### Synthesis

**Exercise 10.7 — Connected scatterplot.** Take a two-variable dataset that varies over time (GDP and CO₂ emissions by decade, revenue and employee count by year). Build it as both a connected scatterplot and as two separate line charts. Compare: what does the connected form reveal about the relationship that the two line charts hide? What does the trajectory shape tell you that a static cloud does not?

**Exercise 10.8 — Parallel coordinates with axis order.** Take a dataset with five or more quantitative variables. Build parallel coordinates with Claude Code. Then reorder the axes to place a different variable pair adjacent — rebuild. Compare the two orderings. Name at least one pattern visible in the second ordering that was hidden in the first. This is Munzner's axis-order-dependence problem made concrete.

### Challenge

**Exercise 10.9 — Cairo audit on a published chart.** Find a published correlation chart — in a news article, academic paper, or corporate report — where you suspect the visual force exceeds the empirical claim. Apply Cairo's frame: what causal inference does the chart invite? Is that inference supported by the data the chart shows? Write the redesign, including the annotation text and its position, that closes the gap between what the chart shows and what it claims.

**Exercise 10.10 — Marginal histograms.** Build a scatterplot with marginal histograms along both the x and y axes using Claude Code. The marginal histograms show the univariate distribution of each variable in addition to the bivariate relationship. Compare to the bare scatterplot: what does knowing each variable's individual distribution add to your interpretation of the joint distribution?

---

## Key Terms

**Scatterplot.** Two-quantitative-variable chart with point marks at (x, y). Channels: x-position and y-position (both highest accuracy).

**Bubble chart.** Scatterplot extended with a third variable as point size. The size channel encodes magnitude via area perception.

**`d3.scaleSqrt`.** D3 scale function that maps values to radii producing area-proportional bubbles. The correct encoding for bubble charts.

**Connected scatterplot.** Scatterplot with points connected in time order. Shows trajectory through two-variable space over time.

**Heatmap.** 2D grid with color luminance encoding intensity per cell. Color scale must match data bipolarity: sequential or diverging.

**Parallel coordinates.** Multi-axis chart for 3+ quantitative variables; observations as polylines. Pattern depends on axis order.

**Overplotting.** When point density obscures cloud shape. Mitigated by alpha transparency, jittering, or 2D hexagonal binning.

**OLS trend line.** Ordinary Least Squares regression line through scatterplot points. Summarizes linear association.

**Correlation-is-not-causation annotation.** Cairo-class ethical requirement. Required on any chart showing strong correlation, inside the chart area, visible to any reader who sees the chart.

**Stevens' power law (area perception).** Perceived area scales as area^0.7. Applies to bubble chart sizing. Radius encoding compounds this with a squared distortion; area encoding does not.

---

## A note about AI

Relationship charts test whether a pattern is in the data or in the viewer. The model can produce scatter plots with regression lines on request. The regression line is a hypothesis, not an observation.

Where the model genuinely helps: producing the scatter plot with and without the regression line, with and without the loess curve, with and without the residual plot. The contrast surfaces what each adds.

Where the model does damage: declaring that the relationship is real because the regression p-value is small. The p-value is a statistic; the relationship is a claim.

The rule: charts from the model; the relationship claim from your own argument.

---

## LLM Exercise — Chapter 10: Relationship Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A relationship chart with explicit form selection and an audit document that confirms the correlation-is-not-causation annotation, the overplotting mitigation strategy, and — for bubble charts — the area-not-radius encoding.

**Tool:** Claude Code (for the build) + Claude chat (for the audit and iteration).

---

**The Prompt (audit + build):**

```
I have a relationship dataset of [DESCRIBE: variables, types, sample
size, what each variable represents]. The communication goal is
[DESCRIBE: what the reader needs to know in 5 seconds].

Walk me through the relationship-chart design:

1. Confirm the family is relationship/correlation. If the question is
   distribution (how values spread) or composition (how parts sum to
   a whole), flag the mismatch.

2. Choose the form: scatterplot, bubble chart, connected scatterplot,
   heatmap, or parallel coordinates. Justify the choice using:
   - Number of variables (2 for scatterplot; 3 for bubble; 3+ for
     parallel coordinates or heatmap).
   - Whether time is a structuring variable (connected scatterplot).
   - Whether the data is categorical × categorical (heatmap matrix).
   - Sample size (large n pushes toward alpha, hexbin, or heatmap).

3. For bubble charts, confirm area-not-radius encoding. Name the
   D3 scale function: d3.scaleSqrt, not d3.scaleLinear.

4. For heatmaps, name the color scale type (sequential or diverging)
   and the sort order for rows and columns.

5. Specify channels using Chapter 3's framework.

6. Specify the correlation-is-not-causation annotation explicitly.
   Provide the exact text of the annotation and its position in the
   chart. This is Cairo's ethical requirement — it is not optional.

7. Specify the overplotting mitigation (alpha, jitter, hexbin) if
   sample size is large.

8. Write a four-move Claude Code prompt that produces the chart.

After Claude Code returns, audit using the Evergreen/Emery subset plus
relationship-specific checks: area-not-radius encoding confirmed in
code (look for d3.scaleSqrt), causation annotation present and visible,
overplotting addressed, color scale appropriate for heatmaps.
```

---

**What this produces:** Audit document plus working relationship chart. Save as `chapter-10-relationship-audit.md` and `chapter-10-relationship.html`.

**How to adapt this prompt:**
- *For your own dataset:* Replace the description and communication goal.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the relationship-chart framework as system context.
- *For Cowork:* Use Cowork to read the data file directly.

**Connection to previous chapters:** Builds on Chapter 3 (Stevens' power law for bubble sizing; channel hierarchy for scatterplot axis assignment), Chapter 4 (chart selection — confirming the relationship/correlation family), Chapter 5 (the Claude Code four-move prompt applied to relationship specifics). Cairo's ethical frame is introduced in Chapter 4; this chapter applies it most precisely.

**Preview of next chapter:** Chapter 11 covers part-to-whole charts — pies, donuts, waffles, treemaps, Marimekko. Where this chapter used position for two variables, Chapter 11 uses angle (pies) or area (treemaps) for proportions, with the corresponding perceptual costs and the five-category pie limit.

---

## Further Reading

- **Cairo, Alberto. (2019).** *How Charts Lie: Getting Smarter About Visual Information.* Chapter 2 develops the correlation-is-not-causation framing with the Catalan independence poll case and others.
- **Stevens, S. S. (1957).** "On the Psychophysical Law." *Psychological Review* 64(3). The power-law mechanism behind area perception — the direct grounding for the bubble-chart area-not-radius rule.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* CRC Press. The section on parallel coordinates and the axis-order-dependence problem.
- **Cleveland, William S., and Robert McGill. (1984).** "Graphical Perception." *Journal of the American Statistical Association* 79(387). The accuracy ranking that puts position-along-common-scale at the top — the foundation for why scatterplots use both axes as position channels.
- **The book's pantry** — `scatterplot.html`, `bubble-chart.html`, `heatmap.html` for working examples of each form.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Francis Galton** drew the first scatter plot in 1885 to compare parents' and children's heights — and named the resulting downward-sloping pattern "regression toward the mean." His statistical instincts were brilliant; his applications of them (founding eugenics) were catastrophic.

![Francis Galton, circa 1890. AI-generated portrait based on a public domain photograph.](../images/francis-galton.jpg)
*Francis Galton, circa 1890. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

![Francis Galton](../images/francis-galton-8pc.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who was Francis Galton, and how does his invention of the scatter plot connect to the relationship and correlation charts we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Francis Galton"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Galton's height-and-regression experiment, and explain what "regression to the mean" actually does and doesn't say.
- Ask it to confront the entanglement of Galton's statistical innovations with his founding role in eugenics.

What changes? What gets better? What gets worse?
