# Chapter 12 — Spatial and Geographic Charts
*Position on the Earth Is the Story.*

## Three suggested titles

- Spatial and Geographic Charts: The Area-Size Distortion Problem
- Choropleth, Dot Map, Bubble Map, Connection Map
- Why Snow's Map Worked and Why Yours Might Not

---

## Chapter overview

By the end of this chapter you will be able to build the family of geographic charts — choropleth, dot density map, bubble map (proportional symbol), connection/flow map — and you will know the area-size distortion problem that haunts all of them. You will know why choropleths must show *rates* not absolute counts (the Cairo "compared with what?" check applied geographically), why dot density maps work when choropleths don't, and how Friendly's history of Dupin's 1826 choropleth and Snow's 1854 dot map illuminates when each form is the right choice.

---

## Learning objectives

1. **(Apply)** Build a choropleth map and a bubble map for the same geographic dataset; identify the perceptual difference between encoding ratios (choropleth) vs. absolute values (bubble map).
2. **(Analyze)** Diagnose the area-size distortion in a choropleth, explaining why large-area units dominate perceptually regardless of their data value — the specific mechanism Friendly's history traces to Dupin's 1826 choropleth invention.
3. **(Evaluate)** Select between choropleth and dot density map for a given spatial dataset, applying Cairo's "compared with what?" criterion to population-based vs. absolute geographic data.

---

## Opening case — the HAI choropleth of GDP per capita

Open `pantry/visualization/bubble-map.html` (and any choropleth example in the pantry) in a browser. The choropleth shades countries by GDP per capita. Color luminance encodes the value: pale for low GDP, dark for high. The viewer's eye moves first to the largest visible regions: the United States, Russia, Canada, China, Brazil, Australia. These are the countries that dominate the visual.

The data, however, does not match the visual dominance. The United States is high GDP. Russia is middle-to-low. Canada is high. China is middle-low. Brazil is middle. Australia is high. The colors should distinguish them — and they do, in principle — but the visual prominence is driven by *land area*, not by GDP per capita.

This is the **area-size distortion**. Choropleth maps encode the data through color luminance applied to geographic regions. The reader's eye, however, processes the *area* of each region first. Large countries, regardless of their data value, attract attention. Small countries — even with extreme data values — recede. The country at the data extreme can be invisible if it's geographically tiny.

Friendly's history (`pantry/Handbook of Data Visualization 2008 Friendly.txt`) traces the choropleth to Baron Charles Dupin, 1826. Dupin used the form to map French illiteracy: each French department shaded according to its illiteracy rate. The form worked because French departments are roughly comparable in area (the visual area didn't dominate); it also worked because Dupin used a *rate* (illiteracy per population), not an absolute count (number of illiterate people). The two design decisions — comparable-area regions and rates not counts — are what make a choropleth honest.

The contemporary choropleth often violates both decisions. A US-state choropleth shades all 50 states the same color luminance scale, despite vast differences in area. A choropleth of "absolute number of cancer cases by state" makes California and Texas look like cancer hotspots, when the reality is that they have many more people. The "compared with what?" check (Chapter 3) catches this: cancer *rate* per capita is what should be encoded; absolute cases are misleading.

This chapter is about the distinct failure modes of geographic visualization, the four major forms (choropleth, dot density, bubble, connection map), and the design rules that prevent each form's specific failures.

---

## Theoretical grounding — Friendly on Dupin (1826), Tufte on Snow (1854), Cairo on ratio-vs-absolute

**Dupin's 1826 choropleth.** Charles Dupin, a French mathematician and statistician, published in 1826 the first known choropleth map: a map of France with each department shaded by literacy rate (lighter shading meant lower literacy). The map was published in *Forces productives et commerciales de la France*. The form was new; the underlying rationale (geographic visualization of statistical data) was new; the success was immediate. Dupin's specific choices — French departments (relatively uniform in area) and rates (literacy *per* population) — were the right choices for the data and for the perceptual mechanism. Subsequent choropleths often violated these choices and produced area-size distortion failures.

**Snow's 1854 dot map of cholera.** John Snow's map of the 1854 London cholera outbreak — a dot per case, plotted on a street map of Soho — is the canonical case for dot density mapping. The map made the cluster around the Broad Street pump immediately visible. No choropleth could have shown this; the geographic units (parishes, wards) were too coarse. Tufte (1983) treats Snow's map as the foundational example of how visualization can reveal causal patterns. Friendly (2008) and Cairo (2016) trace its lineage and influence.

**Cairo's ratio-vs-absolute rule.** Choropleths should show rates (rates per population, ratios, percentages), not absolute counts. The reason is the area-size distortion: absolute counts on a choropleth mostly track population, which mostly tracks geographic area. The chart's color signal becomes redundant with the area signal. Rates control for population; the color signal becomes informative. Cairo's "compared with what?" check (Chapter 3) operationalizes this: every geographic claim must specify the comparison it makes, and absolute counts on a choropleth almost always make the wrong comparison.

---

## Concept 1 — Choropleths: when the area-size distortion is acceptable

A choropleth map shades geographic regions according to a value. The mark is a region (the geographic polygon); the channel is color luminance.

### When choropleths work

- **Geographic units are roughly comparable in area.** Census tracts, ZIP codes, and similar fine-grained units (within a country) often work. Countries (varying by orders of magnitude in area) often don't.
- **The data is a rate, not an absolute count.** Per-capita measures, percentages, ratios.
- **The reader's question is "where in this map are the high values?" or "what's the geographic pattern?"** The chart's strength is showing patterns at the level of the regional unit.

### When choropleths fail

- **Vastly different region sizes.** A US-state choropleth has Wyoming (area 254,000 km², population 580k) and Rhode Island (4,000 km², population 1.1M) at the same color luminance scale. Wyoming dominates the visual; Rhode Island is invisible. Population, not state-level data, drives perception.
- **Absolute counts.** A choropleth of "absolute COVID cases by state" mostly shows where the population is.
- **Sub-national units that are geographically tiny.** A choropleth of European countries makes Luxembourg invisible regardless of its data value.

### Design decisions

**Color scale type.** Sequential (single hue, varying luminance) for unipolar quantitative data. Diverging (two-hue, midpoint at zero or at a meaningful baseline) for data with positive and negative values. Categorical hue is wrong — choropleths are quantitative encoding.

**Bin count.** Most choropleths use 5–7 luminance levels (the human eye distinguishes 7–10 levels reliably). The choice of bin boundaries (quantile bins, equal-interval bins, manually-set bins) substantially changes which patterns are visible.

**Projection.** The Mercator projection distorts area at high latitudes (Greenland looks much larger than Africa, when actually Africa is 14× larger). For choropleths, projections that preserve area (Mollweide, Equal Earth) are better. D3's `d3-geo` library provides many projection options; specify in the prompt.

For Claude Code work: specify the projection explicitly. "Use d3.geoEqualEarth() for the projection" prevents Mercator's area distortion from compounding the choropleth's own distortion.

> ### ↳ Dig Deeper — Choropleth design choices
>
> **Prompt:**
>
> > Walk me through the design decisions for a choropleth: bin count (5-7 levels), bin boundaries (quantile vs. equal-interval), color scale (sequential vs. diverging vs. classified), and projection. For each, name the trade-off. Cite Cairo's "compared with what?" check and the Stevens-power-law mechanism behind luminance perception.
>
> **What to do with the output:** Save the analysis. Reuse for every choropleth project.

---

## Concept 2 — Dot density maps: where Snow's form works

A dot density map places dots (one per N units of the variable) at locations distributed across each geographic region. The pattern of dot density encodes the spatial distribution.

### When dot density maps work

- The data is a count or absolute value where dot-per-unit makes sense (cases of a disease, instances of a behavior).
- Spatial pattern matters more than precise value reading.
- The geographic unit is large enough that dots don't all overlap (sub-state, city-level, etc.).

### Why they're more honest for density data

Dot density maps don't have the area-size distortion problem. The dot count is the data; the regional area is just the canvas. A region with many dots has many cases; a region with few dots has few. The visual prominence tracks the count, not the area.

The trade-off: dot density maps are imprecise about exact values. The reader can estimate "many" or "few" but can't read off counts. Add hover tooltips or callouts for precise values.

### Design decisions

**Dot-per-N.** Each dot represents N units. The choice of N is like the bin width in histograms — too few dots loses pattern; too many dots merges into a uniform mass. Adjust based on the dataset's range.

**Dot placement within regions.** D3 doesn't have a built-in dot-density layout; positions are typically generated as random distributions within each region's polygon. The randomness should be deterministic (seeded) so the chart is reproducible.

**Categorical encoding.** Different dot colors can encode different categories (each dot color = a different cause of death; the spatial mixing pattern shows where each cause concentrates).

The pantry's bubble-map.html is a closely related form (proportional symbol map); the dot density variant adapts the same code with multiple dots per region rather than one symbol.

---

## Concept 3 — Bubble maps: proportional symbols at locations

A bubble map (proportional symbol map) places a circle (or other shape) at the centroid of each region. The size of the circle encodes the value.

### When bubble maps work

- Absolute values (where dot density would be too dense).
- A small number of regions (countries, US states, counties).
- The reader's question is about magnitude, not pattern.

### Stevens' power law applied geographically

The same area-perception issue from bubble charts (Chapter 8) applies here. Encode the bubble's *area* proportional to the value, not the radius. Use `d3.scaleSqrt()` for the radius scale.

### Design decisions

**Area encoding.** As above — `d3.scaleSqrt()` for radius scaling.

**Centroid placement.** The bubble's center should be at the region's geographic centroid (computed via `d3.geoCentroid()` for each polygon).

**Color hue.** Categorical encoding (one hue per category) layered on top of the size encoding. The reader sees both magnitude (size) and category (color).

**Overlap.** When bubbles overlap (dense regions of small countries), use alpha transparency. Dense overlap may indicate switching to a small-multiples regional view.

The pantry's bubble-map.html shows this form for US food-assistance data.

---

## Concept 4 — Connection maps and flow maps

Connection maps draw lines between geographic locations to indicate connections, paths, or flows.

### When connection maps work

- Origin-destination data (flights, migration, trade routes).
- Spatial patterns of connection matter (where do flights go from O'Hare?).
- Audiences who can read networks at geographic scale.

### Two variants

**Existence connection maps** show that A connects to B without encoding magnitude. Useful for "every flight route in our network."

**Flow maps** add line width as the magnitude channel. Wider lines = more flow. Useful for "traffic volume along major routes."

The pantry's `pantry/Visualizing Origin to Destination Flows.txt` discusses several variants in detail.

### Design decisions

**Great-circle paths vs. straight lines.** Long-distance routes are typically drawn as great-circle paths (the shortest path on the globe), which look curved on a Mercator projection. Short routes can be straight lines.

**Line width encoding (for flow maps).** Stevens' power law applies to line width as a magnitude channel; ensure proportionality.

**Spaghetti.** Dense connection maps become spaghetti. Mitigation: filter to top routes, aggregate at higher level, or switch to a non-spatial flow chart (Chapter 11).

---

## Concept 5 — When spatial isn't the right family

Sometimes data has geographic structure but the geographic dimension isn't the question.

A dataset of "employees by office location" can be visualized geographically (a bubble map of office locations sized by employee count) or non-geographically (a horizontal bar chart of offices sorted by employee count). If the question is "which offices have the most employees?", the bar chart wins — comparison is the relationship, not spatial pattern. If the question is "where in the country are our employees concentrated?", the bubble map wins.

The diagnostic: when the answer benefits from geographic context, use a spatial chart. When the answer is just a ranking that happens to have place names, use a comparison chart.

---

## Mid-chapter checkpoint

Pick a geographic dataset from your work. Apply the form selection: choropleth (rate data, comparable regions), dot density (absolute counts, spatial pattern), bubble map (small number of locations, magnitude), connection map (origin-destination data).

Apply the area-size distortion check: are your regions comparable in area, or will large regions dominate? Apply the ratio-vs-absolute check: is your encoding a rate, or an absolute count?

You should be able to do this in 90 seconds.

---

## Extended worked example — building a choropleth with Claude Code

Build a choropleth of US state-level health-insurance uninsured rate for 2024. Data: 50 states + DC, with a percentage value per state.

### Channel decomposition

- Marks: state polygons.
- Channel: color luminance (sequential, pale-to-dark, where dark = higher uninsured rate).
- Projection: equal-area (Albers USA) — preserves area for fair comparison.
- Annotations: legend showing the color scale; quantitative tooltip on hover.

### The four-move prompt

```
**Show what I have:**
US state uninsured rates for 2024. 51 records (50 states + DC), each
with state abbreviation and percentage. Sample:
  TX, 18.4
  FL, 13.2
  NY, 5.7
  MA, 2.5
  ...

US states GeoJSON file: data/us-states.geojson

**Say what I want:**
Choropleth in D3 v7. Single self-contained HTML file with inline CSS
and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Marks: state polygons.
- Projection: d3.geoAlbersUsa() (equal-area; standard for US choropleths).
- Color encoding: d3.scaleSequential with d3.interpolateReds. Color
  domain: 0 to 25 (typical range for uninsured rates).
- 7 luminance bins (the human eye distinguishes 7-10 levels reliably).
- Bin boundaries: quantile-based (use d3.scaleQuantize or
  d3.scaleQuantile based on data distribution).
- Legend: horizontal color bar at bottom-right with bin boundary labels.
- Subtitle: "Uninsured Rate by US State, 2024 (%)".
- Tooltip on hover: state name + exact percentage.
- Margins: top 60, right 40, bottom 80, left 40.
- Dark mode support.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements which channel. Confirm projection is
equal-area (preserves visual fairness for area). Confirm encoding is
percentage (not absolute count of uninsured persons).
```

### Audit

Standard Evergreen/Emery plus:

- Projection is equal-area (d3.geoAlbersUsa, not Mercator).
- Encoding is rate (percentage), not absolute count.
- 5–7 luminance bins.
- Color scale is sequential (one hue, varying luminance), not categorical or diverging.
- Legend interpretable.

The most common failure: Claude Code uses Mercator projection by default (which distorts US states' relative areas). Specify `d3.geoAlbersUsa()` explicitly.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build choropleth maps, dot density maps, bubble maps, and connection/flow maps — choosing the form based on whether the data is rate (choropleth), absolute count with spatial pattern (dot density), absolute count with magnitude (bubble), or origin-destination flow (connection).

You can apply the area-size distortion diagnostic: if regions vary widely in area, the choropleth's color signal will be dominated by the area signal. Mitigations: switch forms, use comparable regions, or accept the distortion (advocacy contexts) with explicit disclosure.

You can apply Cairo's ratio-vs-absolute rule: choropleths should show rates, not absolute counts. The "compared with what?" check operationalizes this for every geographic claim.

You can specify a geographic chart for Claude Code with the right projection (equal-area for choropleths and bubble maps) and the right encoding (sequential luminance for choropleths; sqrt-scaled radius for bubble maps; line width for flow maps).

---

## Key terms

- **Choropleth.** Region-shaded map; color luminance encodes value.
- **Dot density map.** Dots placed within regions; count-per-region encodes data.
- **Bubble map (proportional symbol).** Circles at region centroids; size encodes value.
- **Connection map / flow map.** Lines between locations; existence or width encodes connection or flow.
- **Area-size distortion.** Choropleths visually weighted by region area regardless of data value.
- **Equal-area projection.** Projection that preserves area (Albers, Equal Earth, Mollweide). Essential for choropleths and bubble maps.
- **Ratio-vs-absolute rule.** Choropleths must show rates, not absolute counts. Cairo's "compared with what?" check.
- **Dupin (1826).** First known choropleth — French illiteracy by department.
- **Snow (1854).** Canonical dot map — cholera deaths in Soho.

---

## Discussion questions

1. The area-size distortion is structural — it can't be designed away within the choropleth form. What does this say about choropleth use in publications about countries with vastly different areas?
2. Snow's dot map is celebrated. Replicating it requires fine-grained data (point-level cases) and willingness to forgo precise statistics. When is this trade-off available in modern contexts?
3. Bubble maps and choropleths can show the same data. When does each win?
4. Connection maps risk spaghetti. What about the data structure or the rendering tells you when to switch to a non-spatial flow chart?
5. *Cross-chapter synthesis.* Chapter 11 (flow charts) and Chapter 12 both encounter the spaghetti problem. Frame the unified principle.

---

## Exercises

### Warm-up

**Exercise 12.1** — *Form selection.* For each, choose the right geographic form:
- Per-capita income by US state.
- Total cancer cases by US state (absolute count).
- Locations of all 7-Eleven stores in a city.
- Migration flows between countries.
- Earthquakes globally with magnitude.

**Exercise 12.2** — *Distortion audit.* Find a choropleth of European countries colored by total population. Identify the area-size distortion. Specify the redesign.

**Exercise 12.3** — *Ratio diagnosis.* Take a choropleth of "absolute" data (any kind). Convert to a rate or ratio that respects Cairo's check. Build with Claude Code.

### Application

**Exercise 12.4** — *Build a US choropleth with Albers projection.* Take state-level rate data. Build using d3.geoAlbersUsa(). Audit.

**Exercise 12.5** — *Bubble map vs. choropleth comparison.* Take the same dataset. Build both forms. Identify what each reveals.

**Exercise 12.6** — *Audit a published map.* Find a map in a recent publication. Audit using Evergreen/Emery + spatial-specific (projection, ratio-vs-absolute, color scale).

### Synthesis

**Exercise 12.7** — *Snow-style dot density map.* Take a dataset of geographic events. Build a dot density map. Compare to the choropleth alternative.

**Exercise 12.8** — *Flow map of origin-destination data.* Take a dataset of flows between locations. Build a flow map with width encoding flow magnitude.

### Challenge

**Exercise 12.9** — *Multi-projection comparison.* Build a world choropleth using Mercator, Equal Earth, and Albers. Compare what each makes visible.

**Exercise 12.10** — *Spatial-temporal animation.* Build a choropleth that animates across time (annual changes in a rate). Use D3 transitions.

---

## LLM Exercise — Chapter 12: Spatial Charts

```
I have geographic data of [DESCRIBE: regions, locations, or origin-
destination pairs; values; what each represents]. The communication
goal is [DESCRIBE].

Walk me through:
1. Identify type of geographic data: regional values, point locations,
   flow/connection data.
2. Apply the ratio-vs-absolute check (Cairo). If absolute, recommend
   conversion to rate.
3. Apply the area-size distortion check. If regions vary widely,
   recommend dot density or bubble map over choropleth.
4. Choose form: choropleth / dot density / bubble / connection-flow.
5. Specify projection (equal-area for choropleths; standard for others).
6. Specify channels.
7. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + spatial-specific (projection, ratio-vs-
absolute, color scale type, legend).
```

**Connection to previous chapters:** Chapter 1 (Stevens' power law on area; luminance accuracy), Chapter 3 (Cairo's "compared with what?"), Chapter 8 (bubble chart's d3.scaleSqrt for area-not-radius), Chapter 11 (flow charts overlap).

**Preview of next chapter:** Chapter 13 covers specialized and financial charts — candlestick, Kagi, Point & Figure, bullet graph, radar. Domain-specific conventions earn their own forms.

---

## Visual suggestions

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

## Further reading

- **Friendly, Michael. (2008).** "A Brief History of Data Visualization." Includes Dupin's 1826 choropleth.
- **Tufte, Edward. (1983).** *The Visual Display of Quantitative Information.* The Snow analysis.
- **Cairo, Alberto. (2019).** *How Charts Lie.* Chapter 5 on map distortions.
- **The book's pantry** — `bubble-map.html`; the Visualizing Origin to Destination Flows reference.

---

## Tags

spatial-charts, geographic-charts, choropleth, dot-density, bubble-map, proportional-symbol, connection-map, flow-map, Dupin, Snow, area-size-distortion, ratio-vs-absolute, Cairo, equal-area-projection, D3-geo, d3.geoAlbersUsa, D3, Claude-Code
