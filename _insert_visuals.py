#!/usr/bin/env python3
"""
Insert Visual suggestions sections into Part I chapters of Brutalist d3 x Claude.

Conceptual chapters (Ch 2, 3, 4, 14, 15) get a full set of focal-figure prompts.
Family chapters (Ch 5–13) get a lighter pass — 1–2 focal prompts plus Part II references.
Each section is inserted immediately before the "## Further reading" heading.
"""

from pathlib import Path

ROOT = Path(__file__).parent
CH = ROOT / "chapters"

# Each entry: (filename, section_text)
sections = {}

# ============================================================
# CHAPTER 2 — Chart Selection as Design Decision (CONCEPTUAL)
# ============================================================
sections["04-chart-selection-as-design-decision.md"] = r"""## Visual suggestions

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

"""

# ============================================================
# CHAPTER 3 — Reading a Dataset (CONCEPTUAL)
# ============================================================
sections["05-reading-a-dataset.md"] = r"""## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter is mostly about pre-charting work, so the focal figures are fewer than in adjacent chapters; what matters is the *audit* the figures support, not the chart count.

For chart-type references the chapter mentions in passing, see Part II directly: [Choropleth](29-choropleth.md), [Histogram](40-histogram.md), [Bar Chart](20-bar-chart.md), [Line Graph](43-line-graph.md). Each Part II chapter has its own prompt.

### Figure 3.1 — Two refugee-flow charts from the same dataset

The opening-case figure. The reader is given the prompt "visualize refugee flows" and the same source dataset is rendered two ways: first, the chart that gets produced when no audit happens (a generic choropleth that fails Cairo's "compared with what?" check); second, the chart that gets produced when the audit happens (a flow map with origin-destination pairs and ratio normalization). The figure is the chapter's argument made visible.

See [Choropleth](29-choropleth.md) and [Flow Map](37-flow-map.md) in Part II for the canonical references.

```
Generate a single HTML page in D3 v7 with two side-by-side panels. Two files:

1. `chapter-03-fig-01.html` — full HTML with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). Two map panels in a flex layout, responsive on resize. Page subtitle: "Same dataset, different audit — what the chart shows when no one read the data first."

2. `chapter-03-fig-01/data.json` — the dataset.

Data shape:
- `flows`: array of records, each with `origin_country` (ISO3), `destination_country` (ISO3), `count` (number of displaced persons), `year` (number).
- `country_population`: lookup of ISO3 → population (for ratio normalization in the right panel).

{DATA NEEDED} — UNHCR Refugee Statistics, country-of-origin and country-of-asylum totals, most recent year. Available at https://www.unhcr.org/refugee-statistics/. Match to World Bank population for the ratio panel.

Left panel — choropleth (no audit):
- Base map of all countries.
- Color luminance encodes total refugee count by country (origin + destination summed). Sequential walnut palette.
- This panel is the chart "visualize refugee flows" produces when the dataset is taken at face value. It hides the directional structure (who goes where) and is dominated by absolute counts (which over-reads from population).

Right panel — flow map (audit applied):
- Same base map.
- Arcs from origin to destination for the top-N pairs by count, with arc width encoding count.
- Optional toggle: normalize by destination-country population so the reader sees per-capita absorption, not absolute count.

Caption boxes name the audit failures the left panel exhibits (no direction, no normalization) and the questions the right panel answers ("from where to where?" "relative to host capacity?").

Style: warm monochrome — black, dark walnut, blood-red accents. Quiet base map (light gray country outlines). Serif body, JetBrains Mono for labels.

Provide both files as separate code blocks.
```

### Figure 3.2 — Data type audit: the same column, three encodings

A small three-panel figure showing the same dataset column rendered three different ways depending on whether the data is read as categorical, ordered, or quantitative. The figure makes the data-type-identification step concrete.

```
Generate a 3-panel comparison in D3 v7. Two files:

1. `chapter-03-fig-02.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering the same source column with a different data-type interpretation. Page subtitle: "One column, three readings — categorical, ordered, quantitative."

2. `chapter-03-fig-02/data.json` — one dataset, three encodings derived from it.

Data shape:
- A single column with values that *could* be read three ways. Example: agency-response-time bins ("under 24h", "24-48h", "48-72h", "3-7d", "over 7d") — these are nominally categorical but have ordinal structure and could be quantitative if midpoints are used.

{DATA NEEDED} — A column from any humanitarian operations dataset that has this ambiguity. UN OCHA situation reports often have response-time bins; agency performance data does too.

Panel 1 — categorical reading: bar chart with bars in arbitrary order, distinct colors per bar.
Panel 2 — ordered reading: same bars but sorted by the implied ordinal axis (under 24h → over 7d), single hue with sequential luminance.
Panel 3 — quantitative reading: histogram using the bin midpoints (12h, 36h, 60h, 5d, 14d) on a continuous x-axis.

Caption beneath each panel names the data-type assumption and what the chart now reveals or hides.

Style: warm monochrome. Each panel labeled with its data-type assumption.

Provide both files as separate code blocks.
```

### Figure 3.3 — "Compared with what?" — the four reference baselines

A four-panel figure showing the same single value (a country's refugee count, an agency's response time, etc.) rendered against four different reference baselines: zero, prior period, peer group, target. The figure makes Cairo's "compared with what?" check literal.

```
Generate a 4-panel comparison in D3 v7. Two files:

1. `chapter-03-fig-03.html` — full HTML with inline CSS and inline D3 v7. Four small panels in a row, each rendering one focal value against a different reference baseline. Page subtitle: "One value, four references — zero, prior period, peer, target."

2. `chapter-03-fig-03/data.json` — the focal value plus four reference sets.

Data shape:
- `focal`: one value to be compared.
- `references`: object with four entries: `zero` (single bar at value), `prior_period` (a 12-period time series ending in the focal value), `peers` (10 peer values for cross-comparison), `target` (focal value plus the target it is being measured against).

{DATA NEEDED} — Any operational metric with these four reference views available. Examples: a country's refugee count vs. zero / prior year / peer-country counts / UNHCR target; an agency's response time vs. zero / last quarter / peer agencies / pledge.

Panel 1 — vs. zero: single bar showing the value rising from zero baseline.
Panel 2 — vs. prior period: line chart of the 12 periods with the focal point highlighted.
Panel 3 — vs. peers: dot plot or sorted horizontal bar with the focal entity highlighted.
Panel 4 — vs. target: bullet graph (focal value as bar, target as marker line).

Caption beneath each panel names what the baseline lets the reader conclude.

Style: warm monochrome. The same focal value reads four different ways across the four panels — that is the teaching point.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 4 — Working with Claude Code (CONCEPTUAL)
# ============================================================
sections["06-working-with-claude-code.md"] = r"""## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter is about the prompt → chart pipeline, so the focal figures show that pipeline in action — vague vs. precise prompts producing different charts, MBTA-style iteration, the full pipeline output.

For chart-type references the chapter mentions in passing, see Part II directly: [Bar Chart](20-bar-chart.md), [Sankey Diagram](62-sankey-diagram.md), [Line Graph](43-line-graph.md), [Treemap](75-treemap.md), [Scatterplot](36-scatterplot.md). Each Part II chapter has its own prompt.

### Figure 4.1 — Two prompts for the same chart

The opening-case figure. Same source dataset, two prompts: a vague one ("make a bar chart of these numbers") and a precise four-move one. Two resulting charts side by side. The reader sees what each prompt produces and can read off the difference.

See [Bar Chart](20-bar-chart.md) in Part II for the canonical reference.

```
Generate a single HTML page in D3 v7 with two side-by-side bar charts. Two files:

1. `chapter-04-fig-01.html` — full HTML with inline CSS and inline D3 v7. Two SVG panels in a flex layout. Page subtitle: "Same data, two prompts — vague vs. four-move."

2. `chapter-04-fig-01/data.json` — the dataset.

Data shape:
- 8–12 categories with one quantitative attribute.
  - `category`: string — sector or program name
  - `value`: number — funding amount, count, or percentage

{DATA NEEDED} — A humanitarian-program funding-by-sector dataset. UNHCR or OCHA published reports work. 8–12 categories with values of varying magnitude.

Left panel — vague-prompt output:
- Default chart that Claude Code produces from a one-line "make a bar chart" prompt.
- Bars in source order (not sorted), default rainbow palette, no axis labels, no zero baseline highlighted, ambient grid lines.
- This panel is intentionally compromised; do not improve it.

Right panel — four-move-prompt output:
- Bars sorted descending by value.
- Single-hue walnut palette.
- Zero baseline explicit; y-axis ticks at meaningful round numbers.
- Direct value labels on each bar.
- One-line subtitle naming the chart's claim.

Caption box between or beneath both panels showing the two prompts side by side. The reader should be able to read both prompts and see how each one produced its chart.

Style: warm monochrome. The four-move chart looks editorial; the vague chart looks like default software output.

Provide both files as separate code blocks.
```

### Figure 4.2 — MBTA iteration sequence

A 4-panel sequence showing one chart through four iterations of the MBTA review process. The first panel is the initial Claude Code output; each subsequent panel applies one Evergreen/Emery audit correction. The figure is the iteration loop made visible.

```
Generate a 4-panel iteration sequence in D3 v7. Two files:

1. `chapter-04-fig-02.html` — full HTML with inline CSS and inline D3 v7. Four small panels in a row, each rendering the chart at a different iteration stage. Page subtitle: "One chart, four reviews — the MBTA iteration model."

2. `chapter-04-fig-02/data.json` — the dataset (one source, rendered four ways with progressive corrections).

Data shape:
- A 5-source-node, 5-destination-node Sankey diagram representing humanitarian aid flow from donors to programs.
  - `nodes`: array of `{id, label}`.
  - `links`: array of `{source, target, value}`.

{DATA NEEDED} — A humanitarian aid funding flow: top 5 donor countries → top 5 program sectors. OCHA FTS data or UNHCR donor reports.

Panel 1 — initial output: rainbow palette, no labels on small links, ambient grid, default link curves.
Panel 2 — color audit corrected: single-hue walnut palette.
Panel 3 — labeling corrected: direct labels on each link with value.
Panel 4 — final: subtitle, source/destination separation tightened, all corrections applied.

Caption beneath each panel names the audit point applied at that step. Above the sequence, a brief description of the MBTA review process.

Style: warm monochrome. The sequence reads as a progression from default output to publication-ready chart.

Provide both files as separate code blocks.
```

### Figure 4.3 — The full pipeline: end-to-end on one dataset

A wider figure showing the complete pipeline: data input (table view) → audit document (channel decomposition box) → prompt (code block) → chart output (final D3 visualization). The figure is the chapter's pipeline made visible end-to-end.

```
Generate a 4-panel end-to-end pipeline figure in D3 v7. Two files:

1. `chapter-04-fig-03.html` — full HTML with inline CSS and inline D3 v7. Four panels arranged in sequence (left-to-right or top-to-bottom), each showing one stage of the pipeline. Page subtitle: "End to end — data, audit, prompt, chart."

2. `chapter-04-fig-03/data.json` — the dataset and metadata.

Data shape:
- `data_table`: the source data as rows and columns.
- `audit`: a structured object with channel decomposition (mark, channels, attribute mappings).
- `prompt`: the Claude Code prompt as a string.
- `chart_data`: the data shape needed to render the final chart.

{DATA NEEDED} — A humanitarian-funding-by-region dataset, 8–10 regions, two attributes (current-year value, prior-year value).

Panel 1 — data table: render the source data as an HTML table with light borders. 8–10 rows, 3–4 columns.
Panel 2 — audit: a structured callout box with the channel decomposition rendered as a small structured list (Mark: bar; Channels: x-position = region, y-position = value, hue = year).
Panel 3 — prompt: a code block showing the full four-move prompt.
Panel 4 — chart: the final rendered chart (a multiset bar chart comparing current and prior year values).

Caption between panels names what each stage accomplishes.

Style: warm monochrome. Each panel labeled with its pipeline-stage name.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 5 — Comparison Charts (FAMILY, light)
# ============================================================
sections["07-comparison-charts.md"] = r"""## Visual suggestions

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

"""

# ============================================================
# CHAPTER 6 — Time Series and Temporal Charts (FAMILY, light)
# ============================================================
sections["08-time-series-and-temporal-charts.md"] = r"""## Visual suggestions

This chapter is about time-series chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for time-series charts: [Line Graph](43-line-graph.md), [Area Graph](19-area-graph.md), [Stacked Area](66-stacked-area.md), [Stream Graph](69-stream-graph.md), [Spiral Plot](65-spiral-plot.md), [Gantt Chart](38-gantt-chart.md), [Timeline](72-timeline.md), [Timetable](73-timetable.md). Each Part II chapter has its own prompt.

### Figure 6.1 — The HAI AI capability gap line chart

The chapter's central worked example. A multi-series line chart showing AI capability index across high-, middle-, and low-income country groups from 2016 to 2024. The gap widens visibly. The chart demonstrates the line-chart-vs-area-chart decision (line for trajectory comparison, area for cumulative magnitude) and the differential application of the zero-baseline rule (lines do not require zero; areas do).

See [Line Graph](43-line-graph.md) in Part II for the canonical reference.

```
Generate a multi-series line chart in D3 v7 with a line/area toggle. Two files:

1. `chapter-06-fig-01.html` — full HTML with inline CSS and inline D3 v7. Three time-series lines on one chart, with a toggle to switch between line rendering (no zero-baseline requirement) and area rendering (zero baseline required). Page subtitle: "Trajectory vs. magnitude — when zero baseline matters."

2. `chapter-06-fig-01/data.json` — the dataset.

Data shape:
- Three series of monthly or annual values from 2016 to 2024.
  - `series`: object with three keys (`high_income`, `middle_income`, `low_income`), each a time-indexed array of `{date, value}`.

{DATA NEEDED} — An index measuring AI capability across country income groups. UNESCO, ITU, or Stanford AI Index by country group; the World Bank's digital adoption index also works. Annual values 2016–2024.

Encoding:
- x-position: date (linear time scale).
- y-position: capability index value.
- One line per income group; distinct hues (walnut, dark gray, blood-red).
- Toggle: line mode vs. area mode. In line mode, y-axis fits to data range; in area mode, y-axis starts at zero.
- Direct labels at line endpoints rather than a legend.

Caption explains: "Line mode emphasizes trajectory and gap; area mode emphasizes cumulative magnitude. The zero baseline is required for areas because the area itself encodes magnitude; for lines, what matters is the slope, and a tight y-axis range often reads better."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 7 — Distribution Charts (FAMILY, light)
# ============================================================
sections["09-distribution-charts.md"] = r"""## Visual suggestions

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

"""

# ============================================================
# CHAPTER 8 — Relationship and Correlation Charts (FAMILY, light)
# ============================================================
sections["10-relationship-and-correlation-charts.md"] = r"""## Visual suggestions

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

"""

# ============================================================
# CHAPTER 9 — Part-to-Whole Charts (FAMILY, light)
# ============================================================
sections["11-part-to-whole-charts.md"] = r"""## Visual suggestions

This chapter is about part-to-whole chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example, plus a Nightingale rose figure that earns its keep through the chapter's rhetorical-vs-analytical discussion.

Part II references for part-to-whole charts: [Pie Chart](53-pie-chart.md), [Donut Chart](33-donut-chart.md), [Stacked Bar](67-stacked-bar.md), [Marimekko Chart](44-marimekko-chart.md), [Nightingale](48-nightingale.md), [Proportional Area](56-proportional-area.md), [Radial Bar](58-radial-bar.md). Each Part II chapter has its own prompt.

### Figure 9.1 — Five-slice pie vs. fourteen-slice pie

The chapter's central worked example. Two pie charts side by side: one with 5 slices (within Cleveland & McGill's angle-comparison limit, readable), one with 14 slices (well beyond it, fails). The figure makes the five-slice rule a perceptual demonstration.

See [Pie Chart](53-pie-chart.md) in Part II for the canonical reference.

```
Generate two side-by-side pie charts in D3 v7. Two files:

1. `chapter-09-fig-01.html` — full HTML with inline CSS and inline D3 v7. Two SVG panels in a flex layout. Page subtitle: "The five-slice rule — Cleveland & McGill's angle-comparison limit, illustrated."

2. `chapter-09-fig-01/data.json` — the dataset.

Data shape:
- Two slices arrays: `five_slice` (5 categories summing to 100) and `fourteen_slice` (14 categories summing to 100).

{DATA NEEDED} — Any humanitarian-data part-to-whole breakdown that supports both views. The 5-slice version is a high-level rollup (e.g., 5 macro-sector aggregates); the 14-slice version is the detailed breakdown.

Left panel — five-slice pie:
- Five slices, single-hue family with sequential luminance for ordering.
- Direct percentage labels on each slice.
- Readable at a glance.

Right panel — fourteen-slice pie:
- Fourteen slices, default rainbow palette.
- Detached legend with 14 entries.
- Intentionally hard to read; do not "fix" the encoding.

Caption beneath both: "The eye can compare angles between roughly 30° and 150°. Below 30° (slices under ~8% of the circle), comparison fails. Above five slices, multiple slices fall below this threshold."

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 9.2 — Nightingale rose with the rhetorical-vs-analytical toggle

A coxcomb chart of monthly humanitarian deliveries by category, with a toggle exposing the rhetorical-vs-analytical distinction the chapter draws. The rhetorical mode keeps Nightingale's original radius encoding (visually dramatic, perceptually distorted); the analytical mode applies the area correction (less dramatic, perceptually honest). Both modes labeled.

See [Nightingale](48-nightingale.md) in Part II for the canonical reference.

```
Generate a Nightingale-style rose chart in D3 v7 with a rhetorical/analytical toggle. Two files:

1. `chapter-09-fig-02.html` — full HTML with inline CSS and inline D3 v7. A polar area diagram with a toggle. Page subtitle: "Rhetorical vs. analytical — Nightingale's chart with the area correction made visible."

2. `chapter-09-fig-02/data.json` — the dataset.

Data shape:
- 12 months × 2–4 categories per month.
  - `months`: array of `{month, categories: {sector1: value, sector2: value, ...}}`.

{DATA NEEDED} — Monthly humanitarian deliveries broken down by 2–4 sectors (food, shelter, WASH, protection). UNHCR or WFP monthly delivery reports.

Encoding:
- Angular position: month (12 evenly spaced bands), January at 12 o'clock.
- Per category: a wedge from inner radius to outer radius.
- Toggle:
  - "Rhetorical (Nightingale's original)": outer radius scales linearly with value. Visually dramatic; the eye reads area, which scales as r². A doubled value produces a roughly 4× area on the page.
  - "Analytical (area-corrected)": outer radius = sqrt(value), so area scales linearly with value. Smaller, less dramatic, perceptually honest.
- Hue per category.

Caption beneath the toggle reads: "Both modes are valid in different contexts. The rhetorical mode is appropriate for advocacy where the seasonal pattern is the message. The analytical mode is required for technical comparison where exact values matter."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 10 — Hierarchy Charts (FAMILY, light)
# ============================================================
sections["12-hierarchy-charts.md"] = r"""## Visual suggestions

This chapter is about hierarchy chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for hierarchy charts: [Treemap](75-treemap.md), [Sunburst](70-sunburst.md), [Circle Packing](30-circle-packing.md), [Tree Diagram](74-tree-diagram.md), [Brainstorm](23-brainstorm.md). Each Part II chapter has its own prompt.

### Figure 10.1 — Treemap with squarification toggle

The chapter's central worked example. A treemap of nested humanitarian-AI applications by domain, with a toggle that switches between squarified (Bruls–Huizing–van Wijk 2000, the modern default) and slice-and-dice (the older algorithm) layouts. The figure makes the squarification trade-off concrete: aspect ratio matters because area-perception under elongated rectangles is worse than under near-square ones.

See [Treemap](75-treemap.md) and [Sunburst](70-sunburst.md) in Part II for the canonical references.

```
Generate a treemap in D3 v7 with a squarification toggle. Two files:

1. `chapter-10-fig-01.html` — full HTML with inline CSS and inline D3 v7. A treemap with a toggle that switches layout algorithms. Page subtitle: "Squarification trade-off — aspect ratio and area perception."

2. `chapter-10-fig-01/data.json` — the dataset.

Data shape:
- A nested hierarchy 2–3 levels deep, leaves with quantitative values.
  - Root → 4–5 categories → 3–6 sub-items each.

{DATA NEEDED} — A humanitarian AI capability or program portfolio: top-level domains (Data Collection, Analysis & Prediction, Decision Support, Delivery & Accountability) → specific applications under each.

Encoding:
- Top-level rectangles tile the chart, sub-items tile their parent rectangle.
- Area encodes leaf value.
- Toggle: `d3.treemapSquarify` (modern default) vs. `d3.treemapSlice` or `d3.treemapDice` (alternates that produce extreme aspect ratios for teaching).
- Hue encodes top-level category (identity); luminance optional for sub-item ordering within a parent.
- Direct labels on rectangles large enough to hold them; smaller rectangles hover-only.

Caption beneath the toggle reads: "Squarification keeps aspect ratios near 1:1 so areas are comparable by eye. Slice-and-dice produces narrow rectangles whose area is harder to estimate."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 11 — Flow and Network Charts (FAMILY, light)
# ============================================================
sections["13-flow-and-network-charts.md"] = r"""## Visual suggestions

This chapter is about flow and network chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for flow and network charts: [Sankey Diagram](62-sankey-diagram.md), [Chord Diagram](28-chord-diagram.md), [Arc Diagram](18-arc-diagram.md), [Network Diagram](47-network-diagram.md), [Flow Map](37-flow-map.md), [Parallel Sets](51-parallel-sets.md). Each Part II chapter has its own prompt.

### Figure 11.1 — Sankey with width-as-channel demonstration

The chapter's central worked example. A Sankey diagram of humanitarian aid flow from donors through programs to recipients, with link width encoding flow magnitude. The figure makes width-as-area-channel literal — the reader sees that link width is the data and there is no decorative ink anywhere in the chart.

See [Sankey Diagram](62-sankey-diagram.md) and [Chord Diagram](28-chord-diagram.md) in Part II for the canonical references.

```
Generate a Sankey diagram in D3 v7 with a hairball-mitigation toggle. Two files:

1. `chapter-11-fig-01.html` — full HTML with inline CSS and inline D3 v7 (loaded via CDN; also load the d3-sankey plugin from `https://cdnjs.cloudflare.com/ajax/libs/d3-sankey/0.12.3/d3-sankey.min.js`). A Sankey diagram with a toggle to filter low-volume links. Page subtitle: "Width-as-channel — flow visible without decorative ink."

2. `chapter-11-fig-01/data.json` — the dataset.

Data shape:
- A 3-layer flow: donors (5–8) → programs (4–6) → recipient regions (5–7).
  - `nodes`: array of `{id, label, layer}` (layer: 0, 1, or 2).
  - `links`: array of `{source, target, value}`.

{DATA NEEDED} — Humanitarian aid flow, donor → program → recipient region. OCHA Financial Tracking Service publishes this; UNHCR and WFP also have donor-program-recipient flow data.

Encoding:
- Three vertical columns, one per layer.
- Node height: total flow through that node.
- Link width: flow value between source and target.
- Hue: by source layer (walnut for donors, blood-red for high-volume programs, gray for everything else) OR by program for cross-layer continuity.
- Toggle: filter out links below a chosen volume threshold (slider). Demonstrates hairball mitigation — the chart becomes more readable as the threshold rises, at the cost of showing fewer relationships.

Caption: "Every pixel of link width encodes a flow value. The chart's data-ink ratio is near 1.0; what looks like decoration is structure."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 12 — Spatial and Geographic Charts (FAMILY, light)
# ============================================================
sections["14-spatial-and-geographic-charts.md"] = r"""## Visual suggestions

This chapter is about spatial chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example.

Part II references for spatial charts: [Choropleth](29-choropleth.md), [Dot Map](34-dot-map.md), [Bubble Map](25-bubble-map.md), [Connection Map](31-connection-map.md), [Flow Map](37-flow-map.md). Each Part II chapter has its own prompt.

### Figure 12.1 — Choropleth with ratio-vs-absolute toggle

The chapter's central worked example. A world choropleth of a humanitarian metric, with a toggle that switches between absolute counts (the common error — large countries dominate the visual encoding regardless of per-capita reality) and ratios (per-capita normalization, which reveals the actual distribution). The figure is the chapter's ratio-vs-absolute argument made visible.

See [Choropleth](29-choropleth.md) in Part II for the canonical reference.

```
Generate a world choropleth in D3 v7 with a ratio/absolute toggle. Two files:

1. `chapter-12-fig-01.html` — full HTML with inline CSS and inline D3 v7. A world map with a sequential-luminance choropleth and a toggle. Page subtitle: "Ratio vs. absolute — the choropleth's most common failure made visible."

2. `chapter-12-fig-01/data.json` — the dataset and population lookup.

Data shape:
- `metric`: per-country absolute value of a humanitarian metric (e.g., refugee count, aid received, COVID cases).
- `population`: per-country population.

{DATA NEEDED} — Refugee count by host country (UNHCR), aid received by country (OCHA), or any per-country humanitarian indicator. World Bank population for the ratio normalization.

Encoding:
- Base map: world countries in equal-area projection (`d3.geoEqualEarth()` or `d3.geoMollweide()`).
- Color luminance: absolute or per-capita value, sequential walnut palette.
- Toggle: "Absolute (raw count)" vs. "Per capita (count / population)".
- Quintile or quantile classification (5 bins) so the legend is readable.

Caption beneath the toggle reads: "Absolute counts make large countries dominate the encoding. Per-capita ratios reveal the per-person experience. Neither is wrong; each answers a different question. Make the choice explicit; do not let the default obscure it."

Style: warm monochrome. Equal-area projection, not Mercator (Mercator distorts country areas, compounding the choropleth's existing area-perception issues).

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 13 — Specialized and Financial Charts (FAMILY, light)
# ============================================================
sections["15-specialized-and-financial-charts.md"] = r"""## Visual suggestions

This chapter is about specialized and financial chart selection. Each chart family it discusses has a Part II reference; the focal figure here is the chapter's central worked example — Few's argument that bullet graphs replace gauge charts.

Part II references for specialized charts: [Bullet Graph](26-bullet-graph.md), [Candlestick Chart](27-candlestick-chart.md), [OHLC Chart](49-ohlc-chart.md), [Kagi Chart](30-kagi-chart.md), [Point and Figure](54-point-figure.md), [Radar Chart](57-radar-chart.md), [Span Chart](64-span-chart.md), [Illustration Diagram](41-illustration-diagram.md), [Venn Diagram](76-venn-diagram.md), [Word Cloud](78-word-cloud.md). Each Part II chapter has its own prompt.

### Figure 13.1 — Bullet graph vs. gauge chart for the same KPI

The chapter's central argument made visible. The same dashboard KPI rendered two ways: a gauge chart (the dashboard cliché — round dial with a needle) and a bullet graph (Few's replacement — a bar with target marker and qualitative bands). The reader sees what each chart lets them read.

See [Bullet Graph](26-bullet-graph.md) in Part II for the canonical reference.

```
Generate two side-by-side dashboard KPI panels in D3 v7. Two files:

1. `chapter-13-fig-01.html` — full HTML with inline CSS and inline D3 v7. Two SVG panels in a flex layout, each rendering the same KPI value. Page subtitle: "Bullet graph vs. gauge chart — Few's argument made visible."

2. `chapter-13-fig-01/data.json` — the dataset.

Data shape:
- Three KPIs, each with `actual`, `target`, and `bands` (poor / acceptable / good thresholds).
  - For example: response time (target = 24h, bands at 12 / 24 / 48 hours), program completion (target = 95%, bands at 70 / 90 / 95 / 100), donor satisfaction (target = 4.5, bands at 3.0 / 4.0 / 4.5 / 5.0).

{DATA NEEDED} — Three humanitarian-program KPIs with actual, target, and three qualitative bands per KPI. UNHCR or program-evaluation reports.

Left panel — gauge chart:
- A semicircular dial with a needle pointing at the current value.
- Bands (poor/acceptable/good) drawn as colored arcs.
- This is the dashboard cliché. Render it competently; do not improve the encoding beyond what is conventional.

Right panel — bullet graph:
- Horizontal bar showing the actual value.
- A small marker line showing the target.
- Background bands (poor/acceptable/good) drawn behind the bar in light gray gradations.
- Direct value label.

Caption beneath: "The bullet graph uses position-along-a-common-scale (Cleveland & McGill rank 1) for the actual value; the gauge uses angular position (rank 4). The bullet graph fits in less space and reads faster. Few's argument: replace gauges with bullets, in every dashboard, every time."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 14 — Design Principles in Practice (CONCEPTUAL)
# ============================================================
sections["16-design-principles-in-practice.md"] = r"""## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter is about audit and redesign, so the focal figures are before/after pairs — flawed published charts and their corrections, with the audit point named.

For chart-type references the chapter mentions in passing, see Part II directly: [Bar Chart](20-bar-chart.md), [Bubble Chart](24-bubble-chart.md), [Area Graph](19-area-graph.md), [Scatterplot](36-scatterplot.md), [Line Graph](43-line-graph.md), [Heatmap](39-heatmap.md). Each Part II chapter has its own prompt.

### Figure 14.1 — Before/after audit of a flawed bar chart

The chapter's central worked example. A bar chart with multiple Evergreen/Emery audit failures (truncated y-axis, rainbow palette, ambient grid lines, no zero baseline highlighted, decorative gradients) followed by the same data redrawn with each failure corrected. Each correction is labeled.

```
Generate a 6-panel audit/redesign sequence in D3 v7. Two files:

1. `chapter-14-fig-01.html` — full HTML with inline CSS and inline D3 v7. A 2×3 grid: top row is the flawed original chart with 5 audit-failure annotations; bottom row is the same data through 5 sequential corrections to a final clean chart. Page subtitle: "From flawed to clean — five Evergreen/Emery checklist items applied."

2. `chapter-14-fig-01/data.json` — the dataset.

Data shape:
- 8–10 categories with one quantitative value, plus a target value for context.
  - `category`: string
  - `value`: number
  - `target`: number (optional reference)

{DATA NEEDED} — Any humanitarian-program metric by category where multiple-axis problems can be illustrated. Sectoral funding-vs-need ratios, agency response-time-vs-target by region, etc.

Top row, 3 panels — flawed and annotated:
- Panel 1: the original flawed chart (truncated y-axis starting at the data minimum, rainbow palette, ambient grid, 3D bars, no zero indicator).
- Panel 2: same chart with arrows pointing at each failure, labeled (truncation, palette, grid, 3D, etc.).
- Panel 3: the audit checklist with checkboxes — 5 items, each marked failed.

Bottom row, 3 panels — sequential corrections:
- Panel 4: zero baseline established, y-axis range fixed.
- Panel 5: palette reduced to single hue with sequential luminance for ordering; grid simplified.
- Panel 6: final cleaned chart with direct labels, no ambient elements, subtitle naming the chart's claim.

Caption beneath: each panel labeled with the specific Evergreen/Emery checklist item it addresses.

Style: warm monochrome — except the "before" charts which intentionally show the failures (do not fix them).

Provide both files as separate code blocks.
```

### Figure 14.2 — Color scale family: categorical, sequential, diverging

A reference figure showing the three color scale types side by side, each applied to a small dataset of the appropriate type. The reader sees the expressiveness principle (categorical scale for categorical data, sequential for ordered, diverging for centered) made visible.

```
Generate a 3-panel color-scale demonstration in D3 v7. Two files:

1. `chapter-14-fig-02.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering a small chart with one of the three color scale types applied. Page subtitle: "Three scale types, three data types — categorical, sequential, diverging."

2. `chapter-14-fig-02/data.json` — three small datasets.

Data shape:
- `categorical`: 5 categories (programs, regions) for a categorical-bar example.
- `sequential`: 8 ordered values (low to high) for a sequential heatmap.
- `diverging`: 10 values centered on zero (positive and negative deviations) for a diverging-bar example.

{DATA NEEDED} — Any three small datasets of the appropriate types. The chapter's worked-example dataset works for the categorical and sequential cases; the diverging case wants a deviation-from-target dataset.

Panel 1 — categorical:
- 5-category bar chart.
- Hue encodes category identity; 5 distinct hues with similar luminance (so no category reads as more important).

Panel 2 — sequential:
- 8-cell heatmap row.
- Single-hue palette with sequential luminance from light to dark.

Panel 3 — diverging:
- 10-bar deviation chart with positive bars right of zero, negative bars left.
- Two-hue diverging palette (e.g., walnut for negative, blood-red for positive) with white at zero.

Caption beneath each panel names the scale type and the data type it serves.

Style: warm monochrome — except where the scale demonstration requires the named hues (e.g., the diverging panel must show two hues).

Provide both files as separate code blocks.
```

### Figure 14.3 — Annotation strategy: the same chart at three annotation levels

A 3-panel comparison showing one chart at three annotation levels: under-annotated (no labels, no subtitle, no in-chart context), well-annotated (subtitle, direct labels, one in-chart highlight), and over-annotated (every detail labeled, multiple subtitles, callouts everywhere). The figure is the annotation Goldilocks principle made visible.

```
Generate a 3-panel annotation comparison in D3 v7. Two files:

1. `chapter-14-fig-03.html` — full HTML with inline CSS and inline D3 v7. Three small panels in a row, each rendering the same chart with different annotation density. Page subtitle: "Annotation Goldilocks — too little, just right, too much."

2. `chapter-14-fig-03/data.json` — the dataset.

Data shape:
- A 12-month time series with 3 series, plus a few notable events to annotate.
  - `series`: 3 lines of monthly values.
  - `events`: 3–5 dated events with `month` and `note`.

{DATA NEEDED} — Any time-series with annotatable events: humanitarian funding by month with major appeal launches; refugee arrivals with policy-change events; agency response times with operational-incident dates.

Panel 1 — under-annotated:
- Three lines, default colors.
- No subtitle, no axis labels, no series labels, no event markers.
- Reader cannot tell what they are looking at.

Panel 2 — well-annotated:
- Three lines with direct labels at endpoints.
- Subtitle naming the chart's claim.
- 2–3 dated events highlighted with vertical reference lines and one-line notes.
- Y-axis at meaningful round numbers.

Panel 3 — over-annotated:
- Same chart with every monthly value labeled, every series with multiple labels at different points, every event with multi-line callouts, an excessive subtitle, multiple axis annotations.
- Reader cannot find anything because everything is labeled.

Caption beneath: "Annotation should make the reader's primary question answerable in under three seconds. Under-annotation forces guessing; over-annotation forces filtering."

Style: warm monochrome.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# CHAPTER 15 — Building a Complete Project (CONCEPTUAL)
# ============================================================
sections["17-building-a-complete-project.md"] = r"""## Visual suggestions

The figures this chapter discusses, with Claude Code prompts to generate them. The chapter walks the full Brutalist pipeline end-to-end on the UNHCR humanitarian dataset; the focal figures are the deliverables of each phase.

For chart-type references the chapter mentions in passing, see Part II directly: [Heatmap](39-heatmap.md), [Bar Chart](20-bar-chart.md), [Stacked Bar](67-stacked-bar.md), [Sankey Diagram](62-sankey-diagram.md), [Line Graph](43-line-graph.md), [Choropleth](29-choropleth.md), [Bubble Chart](24-bubble-chart.md), [Flow Map](37-flow-map.md). Each Part II chapter has its own prompt.

### Figure 15.1 — Phase A: data audit visualization

The chapter's Phase A deliverable. A summary visualization of the dataset structure: which attributes are categorical, ordered, quantitative, temporal, spatial; which combinations support which chart types. The figure is the channel-decomposition audit document made visible.

```
Generate a dataset-structure audit visualization in D3 v7. Two files:

1. `chapter-15-fig-01.html` — full HTML with inline CSS and inline D3 v7. A multi-panel layout showing the dataset structure: a small data table preview, a column-type-classification chart, and a chart-type-feasibility matrix. Page subtitle: "Phase A deliverable — what the data has, what it supports."

2. `chapter-15-fig-01/data.json` — the dataset metadata.

Data shape:
- `columns`: array of `{name, type (categorical|ordered|quantitative|temporal|spatial), n_unique, sample_values}`.
- `rows_count`: total row count.
- `chart_feasibility`: matrix of column-pair-to-chart-type viability.

{DATA NEEDED} — The UNHCR refugee statistics dataset (https://www.unhcr.org/refugee-statistics/) or any structured humanitarian dataset with multiple column types. The audit visualization is structural; the specific dataset choice can be adjusted.

Panel 1 — column-type bar chart: counts of categorical / ordered / quantitative / temporal / spatial columns.
Panel 2 — chart-type-feasibility matrix: rows = column pairs, columns = chart types, cell color = viable (walnut), marginal (light gray), infeasible (white). The reader sees which charts the dataset can support.
Panel 3 — small preview table: 5 rows × all columns, with type-color borders.

Caption beneath: "The Phase A deliverable is not a pretty chart — it is a documented audit. The reader of this document is the future self designing the chart."

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 15.2 — Phase B: schema document rendered as a chart

The chapter's Phase B deliverable. The `PROJECT.md` schema document for the worked-example chart, rendered as a structured visualization: chart type, data structure, channel decomposition, design constraints, color palette, sort order, accessibility decisions. The figure makes the schema concrete.

```
Generate a schema-document visualization in D3 v7. Two files:

1. `chapter-15-fig-02.html` — full HTML with inline CSS and inline D3 v7. A structured layout rendering the PROJECT.md content as labeled panels. Page subtitle: "Phase B deliverable — the schema as the chart's blueprint."

2. `chapter-15-fig-02/data.json` — the schema content.

Data shape:
- `chart_type`: string.
- `data_structure`: object describing rows/columns.
- `channels`: array of `{channel_name, attribute, type, justification}`.
- `design_constraints`: array of strings.
- `color_palette`: array of hex codes with usage notes.
- `accessibility`: array of strings.

{DATA NEEDED} — The PROJECT.md content for whichever chart is being built in the chapter's worked example. If the chapter uses a heatmap of refugee count by origin × destination, the schema is built for that.

Render each schema element as a labeled panel:
- "Chart type" — large label, brief description.
- "Data structure" — table of columns with their types.
- "Channels" — list of channel-attribute mappings with justifications.
- "Design constraints" — bulleted list.
- "Color palette" — swatches with usage labels.
- "Accessibility" — bulleted list.

The figure should look like a one-page reference document, not a decorative chart.

Style: warm monochrome.

Provide both files as separate code blocks.
```

### Figure 15.3 — Phase C: the final chart deliverable

The chapter's Phase C deliverable — the actual chart the project produces. A heatmap (or whichever chart the worked-example schema specifies) of UNHCR refugee data, rendered to publication standard with all design decisions from Phases A and B applied. The figure is the project's output.

See [Heatmap](39-heatmap.md) in Part II for the canonical reference.

```
Generate the final project chart in D3 v7 — a heatmap of refugee origin-destination counts. Two files:

1. `chapter-15-fig-03.html` — full HTML with inline CSS and inline D3 v7. A heatmap with origin countries on one axis, destination countries on the other, color luminance encoding count. Responsive on resize. Page subtitle: "Phase C deliverable — the chart Phases A and B specified."

2. `chapter-15-fig-03/data.json` — the dataset.

Data shape:
- `origin_destinations`: array of `{origin, destination, count}` for the top-N origin-destination pairs.

{DATA NEEDED} — UNHCR refugee statistics, country-of-origin × country-of-asylum top pairs by count. https://www.unhcr.org/refugee-statistics/.

Encoding:
- Rows: origin countries, sorted by total outflow.
- Columns: destination countries, sorted by total inflow.
- Cell color luminance: count (sequential walnut palette).
- Direct value labels in cells where count exceeds a readability threshold; tooltip otherwise.
- Subtitle: "Top refugee origin–destination pairs, [year]. Color encodes count."

Apply all design decisions from the chapter's worked-example schema: zero baseline (cell color from light-cream-zero to dark-walnut-max), categorical sort by row/column total, accessible color contrast, direct labels where space permits, alt text for screen readers.

Style: warm monochrome — black, dark walnut, blood-red. Editorial register.

Provide both files as separate code blocks.
```

### Figure 15.4 — Phase D: the audit checklist applied

The chapter's Phase D deliverable. The Evergreen/Emery 22-point checklist applied to the project's chart, with each item marked pass/fail/partial. The figure makes the verification phase concrete.

```
Generate a checklist-audit visualization in D3 v7. Two files:

1. `chapter-15-fig-04.html` — full HTML with inline CSS and inline D3 v7. A 22-row checklist with status indicators for each item. Page subtitle: "Phase D deliverable — the 22-point Evergreen/Emery audit applied."

2. `chapter-15-fig-04/data.json` — the audit results.

Data shape:
- `audit`: array of 22 entries, each `{item_number, item_text, status (pass|fail|partial), notes}`.

{DATA NEEDED} — The Evergreen/Emery checklist itself (published in Stephanie Evergreen's *Effective Data Visualization*; many free summaries online). For the per-item status, the audit is performed by the reader against the chart from Figure 15.3.

Render as a structured checklist:
- Each row: item number, item text, status indicator (filled circle for pass, half-filled for partial, empty for fail), brief notes.
- Group items by category (Text, Arrangement, Color, Lines, Overall).
- Summary at top: "X of 22 pass, Y partial, Z fail."

Style: warm monochrome. The status indicators are the only graphical elements; everything else is text.

Provide both files as separate code blocks.
```

### Figure 15.5 — Phase E: the published artifact

The chapter's Phase E deliverable. The chart from Figure 15.3, packaged for publication: with caption, source citation, methodology note, accessibility statement, and link to the underlying data. The figure makes the handoff concrete.

```
Generate the publication-packaged chart in D3 v7. Two files:

1. `chapter-15-fig-05.html` — full HTML with inline CSS and inline D3 v7. The chart from Figure 15.3 wrapped in a publication container with caption, source, methodology, and accessibility statement. Page subtitle: "Phase E deliverable — the chart, packaged for the reader who is not in the room."

2. `chapter-15-fig-05/data.json` — same data as Figure 15.3.

Layout:
- The chart from Figure 15.3, full width.
- Title above: "Top refugee origin–destination pairs, [year]."
- Subtitle below title: a one-sentence claim the chart makes.
- Caption below the chart: 2–3 sentences explaining what the reader should take away.
- Source line: "Data: UNHCR Refugee Statistics, [date]. URL: https://www.unhcr.org/refugee-statistics/"
- Methodology line: "Methodology: Top-N pairs by absolute count. Sort: row and column totals descending. Color: sequential luminance, cream-to-walnut, 5 quantile bins."
- Accessibility statement: "Alt text and SVG `<title>`/`<desc>` provided. Color contrast meets WCAG AA. Tooltip values readable by screen reader."

Style: warm monochrome. Editorial register, suitable for publication on a humanitarian-organization website or in a print report.

Provide both files as separate code blocks.
```

---

"""

# ============================================================
# Insert each section before the "## Further reading" line
# ============================================================
inserted = 0
for filename, section in sections.items():
    path = CH / filename
    if not path.exists():
        print(f"  MISSING: {filename}")
        continue
    text = path.read_text(encoding="utf-8")
    if "## Visual suggestions" in text:
        print(f"  ALREADY HAS Visual suggestions: {filename}")
        continue
    # Insert before "## Further reading"
    marker = "## Further reading"
    if marker not in text:
        print(f"  NO marker found in {filename}")
        continue
    new_text = text.replace(marker, section + marker, 1)
    path.write_text(new_text, encoding="utf-8")
    inserted += 1
    print(f"  inserted into: {filename}")

print(f"\nTotal: inserted into {inserted} chapters")
