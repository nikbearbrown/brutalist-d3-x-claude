# Chapter 14 — Spatial and Geographic Charts
*Position on the Earth Is the Story.*

---

Here is a map of the United States. Each state is shaded by the number of uninsured people. Texas is very dark — it has the highest absolute count. California is nearly as dark. New York and Florida are in the middle. Wyoming, Vermont, and Rhode Island are pale.

Now here is the same map shaded by the *uninsured rate* — the percentage of residents without health insurance. Texas is still dark. But California is now much lighter. Wyoming, which looked pale before, is now darker than California. Rhode Island, invisible in the first map, turns out to have a lower rate than the national average. The entire visual story has changed.

Same states. Same underlying health data. Different question.

The first map answers: where do the most uninsured people live? The answer is where the most people live — California, Texas, New York, Florida. The map is mostly showing you population density wearing the costume of a health-care visualization. The second map answers: in which states are residents most likely to be uninsured? The answer is genuinely geographic — a pattern tied to state-level policy, not just to where people live.

This is the core problem of geographic charts. Every spatial form carries a distortion risk that does not exist in bar charts or scatterplots: the size of the geographic unit competes with the data encoded in it. A large region draws the eye regardless of what color it is. Absolute counts in a choropleth mostly track population, which mostly tracks area. The map shows what you drew, but the reader sees what's big.

Fixing this is not a stylistic choice. It is a claim about what the chart is actually answering.

<!-- → [FIGURE: Two US state choropleth maps side by side, same underlying health dataset. Left: "Total uninsured people by state" — Texas and California are very dark; Wyoming, Vermont, Rhode Island are pale. The visual story is population density. Right: "Uninsured rate (%) by state" — Texas remains dark; California is now notably lighter; Wyoming is darker than California; Rhode Island is near the national average. Caption: "Same states. Same underlying data. Different question. Left: where do uninsured people live? Right: in which states are residents most likely to be uninsured? The map shows what you drew; the reader sees what's big." Annotate 2–3 specific states that flip dramatically between the two maps.] -->

---

## What Geographic Visualization Is For

Before choosing a form, name what is actually spatial about the data. Not all data that has a place-name dimension is genuinely spatial. Employees by office location is a ranked comparison that happens to have city names. A bar chart answers that question better than a map, because comparison is the relationship — not spatial proximity, not geographic clustering, not the question "where?"

Geographic visualization earns its complexity when the *location itself* is the answer. When the pattern is legible only in the geographic context — when knowing that these cases cluster in the northeast corner of the city, or that these flows move consistently from east to west, is what the reader needs — then a map is the right tool. When the question is just "which of these is largest?", a bar chart is right and the map is an expensive decoration.

The diagnostic question: would the reader need to know the geographic positions of the values to answer their question, or would a ranked list suffice? If the geographic pattern matters, map it. If not, use the form from Chapter 8.

---

## The Four Spatial Forms

**Choropleth.** Geographic regions shaded by a value. The mark is the region polygon; the channel is color luminance. The choropleth is the default spatial form in data journalism, public health, and policy work. It works when the data is a rate (a ratio per population or per unit), the regions are roughly comparable in area, and the reader's question is geographic pattern rather than precise value.

**Dot density map.** Dots placed within regions, one dot per N units. No area encoding — the mark is a point, the channel is point count per region. The form works for absolute counts where the spatial distribution within a region matters, not just the regional total. John Snow's 1854 cholera map was a dot-per-case map of Soho. The cluster around the Broad Street pump was visible immediately. No choropleth could have shown this: the geographic units (parishes, wards) were too coarse to reveal the cluster.

**Bubble map (proportional symbol).** Circles at region centroids, sized by value. The mark is a circle; the channels are x-position, y-position (geographic), and area (magnitude). The bubble map handles absolute values honestly because the bubble's size encodes the count directly — it doesn't depend on the region's area. Stevens' power law applies: the bubble's *area* must be proportional to the value, not the radius. The same `d3.scaleSqrt` rule from Chapter 10.

**Connection map / flow map.** Lines drawn between geographic locations, encoding the existence or magnitude of a connection. The mark is a line; the channels are the start and end positions (both geographic) and, for flow maps, line width (magnitude). Origin-destination data — migrations, trade routes, flight networks — is the right home for this form. The failure mode is the spaghetti problem: too many routes produces an unreadable tangle. The mitigation is to show only the top N flows, or to aggregate at a coarser geographic level.

Four forms, each right for a specific combination of data type and question. The choice is not decoration.

<!-- → [INFOGRAPHIC: Four-panel reference grid, one panel per geographic form. Each panel: form name (uppercase, JetBrains Mono), a thumbnail of the form's visual structure, the primary channel, and the "use when" condition. Panels: Choropleth (shaded polygons, "color luminance encodes rate," "rate data, comparable regions"), Dot density (dots within regions, "point count encodes magnitude," "absolute count, spatial pattern at sub-regional resolution"), Bubble map (circles at centroids, "circle area encodes absolute value," "absolute magnitude, severs area-size distortion"), Connection/flow map (lines between locations, "line width encodes flow magnitude," "origin-destination data"). This is the navigation reference.] -->

---

## The Area-Size Distortion

The choropleth is the most common spatial form and the most commonly misused. Its failure mode is structural, not just a matter of poor implementation.

The problem: the reader's eye processes the *area* of each region before it processes the color. Large regions attract attention. Small regions recede. This happens regardless of what color is encoded. A choropleth of "quality of life" shading Luxembourg alongside France will always make France visually dominant, even if Luxembourg has the highest quality of life by a factor of two. Luxembourg is, roughly, 1/500th the area of France.

This is not a design error you can fix by choosing a better color scale. It is a perceptual fact about how the eye processes images. Area is a preattentive feature — processed before conscious attention is applied. The choropleth asks color luminance to override that preattentive impression. When the regions differ vastly in size, color does not win.

Charles Dupin understood this when he invented the choropleth in 1826. His map of French illiteracy used French departments — roughly comparable in area (most are between 5,000 and 9,000 km²). He also used a rate (illiteracy per population), not an absolute count. Both choices were deliberate. The roughly-equal areas reduced the area-size distortion. The rate removed the confound between population density and the phenomenon he was measuring.

Modern choropleths routinely violate both of Dupin's choices. US state choropleths have Wyoming (254,000 km²) alongside Rhode Island (4,000 km²) — a 63:1 area ratio. Country-level choropleths have Russia (17 million km²) alongside Luxembourg (2,600 km²) — a 6,500:1 ratio. The color luminance encoding is technically present, but the area-size distortion overwhelms it. The reader sees a picture mostly shaped by land mass.

<!-- → [FIGURE: A world choropleth on Equal Earth projection where all countries have the same value encoded — a mid-range luminance. Every country is the same color. The only variable is geographic area. Caption: "Every country has the same value. The reader's eye still moves to Russia, Canada, and Australia — not because their values are different, but because their areas are. This is the area-size distortion: preattentive area processing precedes color reading regardless of what the color encodes." Annotate Greenland (appears large on Mercator) and Luxembourg (invisible on both projections).] -->

---

## Rates, Not Counts

The ratio-vs-absolute rule is Cairo's "compared with what?" check applied geographically.

A choropleth of absolute counts answers a different question than the designer usually intends. "Number of COVID cases by state" mostly shows "where do people live?" — because the number of COVID cases in a large state is mostly a function of its population, not of anything specific about how the state managed the pandemic. The chart's signal is dominated by the confound.

The fix is simple: divide by population. Cases per 100,000 residents removes the population confound. The chart now shows the per-capita disease burden — how likely a resident of each state was to contract COVID — which is the question the designer usually intended to answer.

The rule generalizes. Any time an absolute geographic count is dominated by population (and it almost always is), the honest encoding is a rate. Number of hospitals → hospitals per 100,000 residents. Total aid received → aid per displaced person. Absolute exports → exports as a percentage of GDP.

Exceptions exist. Total refugee count is sometimes legitimately the question: "which countries are hosting the largest absolute number of displaced people?" is not the same as "which countries are hosting the most displaced people relative to their own population?" Both questions are valid. The designer's job is to name which one the chart answers and make that choice visible — in the title, in the legend, in the axis labels.

---

## Snow's Dot Map and Why It Worked

John Snow's 1854 cholera map of the Soho neighborhood in London is the canonical example of geographic visualization enabling causal reasoning. It is also the best argument for the dot density form over the choropleth.

Snow's question was: where in Soho are the cholera deaths concentrated? He had a list of addresses — every household that reported a death during the 1854 outbreak. He placed a dot at each address on a detailed street map. The dots were distributed across the neighborhood at low density most places, but clustered visibly around the corner of Broad Street and Cambridge Street. The Broad Street water pump stood at that corner.

A choropleth of the same data — shading each parish by total deaths — would have been useless. The parishes are large; the cluster was sub-block. The geographic resolution that made the pattern visible was street-level, not parish-level. The dot map was the right form because the spatial pattern was the answer and the resolution required was finer than any administrative boundary.

The dot map's strength is that it doesn't impose a geographic aggregation unit. Every case plots at its actual location. The pattern emerges from the data, not from the boundary definitions that a choropleth must use. When the relevant pattern is finer-grained than the available administrative units, dot maps are the only form that can show it.

The cost: dot density maps require point-level data, which is often unavailable due to privacy restrictions, aggregation in the source, or simply because the data was collected at the regional level. When the data is already aggregated (cases per county), the dot placement within the county is artificial. The dots encode "this region has many cases" in a way that looks like geographic precision but is actually a distribution algorithm applied to a regional count.

For Claude Code work: dot density maps with truly random dot placement are reproducible if you seed the random number generator. Specify this in the prompt: "use a deterministic seeded random placement within each polygon so the chart is reproducible."

<!-- → [FIGURE: Two panels of the same Soho neighborhood, same cholera dataset. Left: choropleth — each parish shaded by total deaths; the cluster is hidden within the parish boundaries; Saint James parish appears moderately affected. Right: Snow-style dot map — one dot per death at its street address; the cluster around the Broad Street pump is immediately visible as a dense concentration in a single block. Caption: "Same data, two resolutions. The choropleth aggregates to parishes — too coarse to reveal the cluster. The dot map plots every case at its address — the pump stands at the cluster's center. The form that can answer the question is determined by the resolution the question requires."] -->

---

## Projections and Why They Matter

Every geographic visualization involves a projection — a mathematical transformation from the sphere of the Earth to a flat surface. All projections distort something: area, shape, distance, or angle. There is no perfect projection.

The choice of projection matters for geographic charts because different distortions interact differently with different encodings.

**Mercator projection.** Preserves angle (conformal). Used for navigation, which is why it persists. Distorts area dramatically at high latitudes: Greenland appears roughly the size of Africa, but Africa is actually fourteen times larger. For choropleths and bubble maps, Mercator compounds the area-size distortion. Greenland's shading looks visually important whether or not Greenland is important in the data.

**Equal-area projections (Mollweide, Equal Earth, Albers).** Preserve area; every region's map area is proportional to its real land area. For choropleths, this is the right choice. The area-size distortion already exists as a perceptual problem; equal-area projections at least ensure the map areas are honest representations of real land area, not additional distortions layered on top.

**Albers USA.** A specific equal-area conic projection designed for the contiguous United States. Inset panels move Alaska and Hawaii to visible positions. Standard for US state choropleths and bubble maps. Specify `d3.geoAlbersUsa()` in every US geographic chart prompt.

For Claude Code work: Claude Code defaults to Mercator because Mercator is familiar. Specify the projection explicitly. "Use `d3.geoEqualEarth()` for a world-level map" or "use `d3.geoAlbersUsa()` for a US-state map." The follow-up when Mercator appears:

> "The projection is Mercator. Replace with `d3.geoEqualEarth()`. Mercator distorts country areas at high latitudes, which compounds the choropleth's area-size distortion. Regenerate."

<!-- → [FIGURE: Two world maps showing the same choropleth data side by side. Left: Mercator — Greenland appears roughly the same size as Africa (annotated with actual ratio: "Africa is 14× larger"). Russia visually dominates the northern hemisphere. Right: Equal Earth — Africa's actual dominance is visible; Greenland is a small island; Russia is large but proportional to its actual area. Caption: "Mercator compounds the area-size distortion by adding another layer of area inaccuracy. Equal Earth preserves actual land areas so the choropleth's perceptual distortion is at least bounded by geographic reality."] -->

---

## When Bubble Maps Outperform Choropleths

The bubble map beats the choropleth when the data is an absolute value and the visual priority is magnitude rather than geographic pattern.

A choropleth of absolute refugee counts shades large countries darkly because they contain more people — Syria, Afghanistan, and South Sudan generate large refugee flows. But the visual result favors the areas (Russia, Canada, Australia) that have few refugees but large land masses. The map does not show what the data says.

A bubble map places a circle at each country's centroid sized by the absolute refugee count. Syria, Afghanistan, and South Sudan produce large bubbles. Russia, Canada, and Australia produce small or invisible ones. The map shows what the data says. The area-size distortion is severed because the bubble's area is independent of the country's area.

The trade-off: bubble maps work less well when the bubbles need to overlap to show the data. Dense regions of small countries — the Sahel, the Balkans, Central America — produce bubbles that pile on top of each other. Mitigations include alpha transparency, offset positioning, or aggregating to a coarser level.

Stevens' power law applies to bubble maps identically to bubble charts. Encode the bubble area proportional to the value, not the radius. Specify `d3.scaleSqrt` for the radius scale. The follow-up when radius encoding appears:

> "The bubble radius is scaled linearly. This makes visual area scale as value squared, compounding Stevens' area perception distortion. Replace with `d3.scaleSqrt` for the radius scale. Regenerate."

<!-- → [FIGURE: Two world maps side by side, same absolute refugee-count dataset. Left: choropleth (Equal Earth) — large countries like Turkey, Pakistan, and Uganda (which host many refugees) are moderately dark, but Russia, Canada, and Australia (few refugees, large areas) are visually prominent. The chart misleads because large land masses dominate. Right: bubble map (Equal Earth, d3.scaleSqrt radius encoding) — Turkey, Pakistan, and Uganda have large visible bubbles; Russia, Canada, and Australia have small or absent bubbles. The visual story matches the data. Caption: "Same data, two forms. Choropleth: large areas dominate regardless of refugee count. Bubble map: the bubble area is independent of the country's area. The form that severs the distortion is the honest one for absolute counts."] -->

---

## How This Changes the Prompt

Geographic charts have form-specific specifications that belong in every prompt.

**For choropleths:** the projection (`d3.geoEqualEarth()` or `d3.geoAlbersUsa()`); the encoding explicitly stated as rate or ratio ("encoding is uninsured *rate*, not absolute uninsured count"); the color scale type (sequential for unipolar data; diverging for data with a meaningful zero); the bin count (5–7) and bin method (quantile or equal-interval); the legend.

**For bubble maps:** the projection; `d3.scaleSqrt` for the radius scale; `d3.geoCentroid()` for centroid computation; alpha transparency for overlapping bubbles.

**For dot density maps:** the dots-per-N specification; the seeded random placement for reproducibility; the categorical color encoding if multiple categories need distinguishing.

**For connection/flow maps:** great-circle paths for long-distance routes (`d3.geoGraticule` + `d3.geoPath`); line width proportional to flow magnitude (with `d3.scaleSqrt` for the same reason as bubbles); the top-N filter if the dataset risks spaghetti.

The most common Claude Code failure for geographic charts is the projection default. Specify the projection by name in every geographic prompt. The second most common failure is absolute-count encoding for a choropleth that should show rates. State the encoding choice explicitly and include it in the "Verify" move: "Confirm that the encoding is [rate], not [absolute count]."

---

## The Feynman Test

The test for this chapter: given any geographic dataset, answer three questions before touching Claude Code.

First: is geography the right family, or is a ranked comparison chart the honest answer? If the question is "which state has the highest uninsured rate?", a bar chart answers it faster and more accurately than a choropleth. If the question is "what is the geographic pattern of uninsured rates?", the choropleth answers it. The word "pattern" is the signal.

Second: is the encoding a rate or an absolute count? Absolute counts in choropleths mostly show where people live. Rates show the phenomenon per person. Apply Cairo's "compared with what?" check: what is the denominator, and is it the right one?

Third: do the regions vary widely in area? If yes, either use a bubble map (the bubbles' area is independent of the region's area) or accept the area-size distortion explicitly and disclose it. Equal-area projections mitigate the problem without solving it.

If you can answer all three questions in sixty seconds, you know the chapter. The forms, their distortion mechanisms, and the corrections are compact enough to hold in working memory. The geographic dimension adds one problem that bar charts and scatterplots don't have — the competition between area and data. Everything else is the same channel-theory framework you have been using since Chapter 3.

---

## Exercises

### Warm-up

**Exercise 14.1 — Form selection.** For each of the following, name the right geographic form (choropleth, dot density, bubble map, or connection/flow map) and justify the choice in one sentence:

- Per-capita income by US county (rate, roughly comparable-area units).
- Total cancer cases by US state (absolute count, large region area variation).
- Locations of every reported opioid overdose in a single city over one year.
- Volume of container shipping between the top 20 port pairs globally.
- Refugee population hosted by each country (you want to show absolute numbers, not per-capita rate).

**Exercise 14.2 — Rate conversion.** You are given a choropleth showing "total COVID deaths by country." (a) Name the population confound: what does this map mostly show instead of the pandemic's severity? (b) Specify the rate that would remove the confound. (c) Name one scenario where the absolute count is legitimately the right encoding and explain why.

**Exercise 14.3 — Projection audit.** Find a published world choropleth that uses Mercator projection. (a) Identify two countries where the area-size distortion is most severe (name them and give approximate real-area vs. Mercator-area ratios). (b) Specify the redesign projection and explain in one sentence why it is better for a choropleth.

### Application

**Exercise 14.4 — Build a US choropleth with Albers projection.** Take a state-level rate dataset (uninsured rate, unemployment rate, any per-capita measure). Write the four-move prompt specifying `d3.geoAlbersUsa()`, a sequential color scale, quantile binning with 7 levels, and a legend. Verify in the code that the projection is not Mercator and the encoding is a rate. Iterate to publishable.

**Exercise 14.5 — Choropleth vs. bubble map comparison.** Take the same dataset with both a rate version and an absolute-count version. Build the rate version as a choropleth (`d3.geoAlbersUsa()`, sequential color) and the absolute version as a bubble map (`d3.scaleSqrt`). Compare what each reveals. Name one question each form answers better than the other.

**Exercise 14.6 — Ratio-vs-absolute toggle.** Build a world choropleth with a toggle that switches between absolute count encoding and per-capita rate encoding for the same dataset. This is the opening hook of the chapter made interactive. Document in the iteration log how the visual story changes when you switch modes.

### Synthesis

**Exercise 14.7 — Snow-style dot density map.** Take a dataset of geographic events at the point level (crime incidents, disease cases, service requests, restaurant inspections). Build a dot density map. Then build a choropleth of the same data aggregated to administrative units (ZIP codes, census tracts). Compare: what does the dot map reveal that the choropleth cannot? Where does the choropleth's coarser resolution hide a pattern?

**Exercise 14.8 — Flow map with spaghetti mitigation.** Take an origin-destination dataset (migration flows, flight routes, trade volumes). Build a connection map showing all routes. Identify when the chart becomes unreadable (how many routes before spaghetti?). Then apply the top-N filter — show only the routes above a magnitude threshold. Compare the two charts and specify the threshold that preserves the key story while eliminating the noise.

### Challenge

**Exercise 14.9 — Multi-projection comparison.** Build a world choropleth three times using Mercator, Equal Earth, and Mollweide projections. For each, measure the visual area of Greenland and Africa on the rendered chart and compute the ratio. Compare to the actual area ratio (Africa ≈ 14× Greenland). Which projection introduces the least distortion for a humanitarian-data choropleth?

**Exercise 14.10 — Spatial-temporal animation.** Build a choropleth that animates across time — annual changes in a state-level rate variable over five or more years. Use D3 transitions. Audit the animation: does the color scale remain consistent across frames (it must, or the reader cannot compare years), and are the transitions smooth enough to read the directional change without losing individual state positions?

---

## Key Terms

**Choropleth.** Region-shaded map; color luminance encodes value. Invented by Dupin (1826) for French illiteracy by department. Requires rate encoding and comparable-area regions.

**Area-size distortion.** Choropleths are perceptually dominated by the size of geographic regions regardless of the data value encoded. Structural to the form; mitigated by equal-area projections and comparable-area regions; eliminated by switching to bubble maps or dot density maps.

**Dot density map.** Dots placed within regions at one dot per N units. No area encoding; count encodes data. Canonical example: Snow (1854), cholera deaths in Soho.

**Bubble map (proportional symbol).** Circles at region centroids sized by value. Area encoding required (`d3.scaleSqrt`). Severs the area-size distortion.

**Connection map / flow map.** Lines between locations encoding connection (existence) or flow magnitude (line width). Great-circle paths for long distances. Spaghetti mitigation: top-N filter.

**Ratio-vs-absolute rule.** Choropleths should encode rates, not absolute counts. Cairo's "compared with what?" applied geographically.

**Equal-area projection.** Projection preserving area relationships between regions. Essential for choropleths. `d3.geoEqualEarth()` for world maps; `d3.geoAlbersUsa()` for US state maps.

**Dupin (1826).** First known choropleth. French illiteracy by department. Used comparable-area regions and a rate.

**Snow (1854).** Canonical dot map. Cholera deaths by address in Soho. Pattern visible at sub-parish resolution unavailable to choropleths.

---

## LLM Exercise — Chapter 14: Spatial Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A geographic chart with explicit form selection and an audit document confirming the ratio-vs-absolute encoding, the projection choice, and the area-size distortion mitigation.

**Tool:** Claude Code (for the build) + Claude chat (for the audit and iteration).

---

**The Prompt (audit + build):**

```
I have geographic data of [DESCRIBE: regions, locations, or origin-
destination pairs; values and what each represents]. The communication
goal is [DESCRIBE: what the reader needs to know in 5 seconds].

Walk me through the spatial-chart design:

1. Confirm the geographic family is appropriate. If the question is
   a comparison (which region is largest?) rather than a spatial
   pattern (where does this concentrate?), flag the mismatch and
   recommend a comparison chart instead.

2. Apply the ratio-vs-absolute check (Cairo's "compared with what?").
   If the data is an absolute count, recommend converting to a rate.
   Name the denominator.

3. Apply the area-size distortion check. If regions vary widely in
   area (e.g., country-level or US-state-level), recommend bubble
   map over choropleth for absolute values, or equal-area projection
   for rates.

4. Choose form: choropleth (rate, comparable areas), dot density
   (absolute count, fine spatial pattern), bubble map (absolute
   magnitude, independent of region area), or connection/flow
   (origin-destination).

5. Specify projection. For world maps: d3.geoEqualEarth(). For US
   state maps: d3.geoAlbersUsa(). Do not use Mercator.

6. Specify channels. For choropleths: sequential or diverging color
   scale matched to data bipolarity; 5–7 bins; quantile or equal-
   interval bin method. For bubble maps: d3.scaleSqrt for radius.

7. Write a four-move Claude Code prompt that produces the chart.

After Claude Code returns, audit using the Evergreen/Emery subset plus
spatial-specific checks: projection is equal-area (confirm in code),
encoding is rate not absolute count (confirm in data join), color
scale type matches data bipolarity, legend interpretable, bubble size
uses d3.scaleSqrt if applicable.
```

---

**What this produces:** Audit document plus working geographic chart. Save as `chapter-14-spatial-audit.md` and `chapter-14-spatial.html`.

**How to adapt this prompt:**
- *For your own dataset:* Replace the description and communication goal.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the spatial-chart framework as system context.
- *For Cowork:* Use Cowork to read the GeoJSON and data files directly.

**Connection to previous chapters:** Builds on Chapter 3 (Stevens' power law on area and luminance — both apply here), Chapter 4 (Cairo's "compared with what?" — the ratio-vs-absolute rule is this check applied geographically), Chapter 10 (bubble charts — the `d3.scaleSqrt` rule for area encoding applies identically to bubble maps). The area-size distortion is a new problem specific to geographic forms; everything else is the channel-theory framework from Part I.

**Preview of next chapter:** Chapter 15 covers the design audit — walking the full Evergreen/Emery 22-point checklist on a completed project, plus the Tufte/Few/Cairo synthesis as the governing framework. Where previous chapters applied the per-chart audit, Chapter 15 applies the project-level audit: do all the charts in this project form a coherent visual language?

---

## Further Reading

- **Friendly, Michael. (2008).** "A Brief History of Data Visualization." In *Handbook of Data Visualization*, edited by C. Chen, W. Härdle, and A. Unwin. Springer. Includes Dupin's 1826 choropleth and its lineage. In the book's pantry.
- **Tufte, Edward R. (1983, 2nd ed. 2001).** *The Visual Display of Quantitative Information.* The Snow analysis is Tufte's canonical case for how visualization reveals causal structure.
- **Cairo, Alberto. (2019).** *How Charts Lie: Getting Smarter About Visual Information.* Chapter 5 on map distortions and the ratio-vs-absolute rule.
- **The book's pantry** — `bubble-map.html` for the proportional symbol map; the Visualizing Origin to Destination Flows reference for connection/flow maps.
