# Chapter 3 — Marks and Channels
*The Channels Your Eye Trusts and the Ones It Doesn't.*

---

Here is a puzzle I want you to sit with before we get into anything formal.

I give you two charts. Both encode exactly the same data: fifty countries, two numbers per country — GDP per capita and life expectancy. I ask you one question about each chart: *which countries have the highest life expectancy?*

In the first chart, GDP sits on the x-axis and life expectancy sits on the y-axis. Each country is a dot. The high-life-expectancy countries pile up in the upper right. You answer my question in less than a second.

In the second chart, GDP still sits on the x-axis. But life expectancy is now encoded by color — pale dots for low values, dark dots for high. All the dots sit on a single horizontal line. You scan across looking for the darker ones. Ten seconds pass. You are still not sure.

The data is *identical*. The question is *identical*. The charts are not.

<!-- → [FIGURE: Two side-by-side scatterplots, identical 50-country dataset. Left: x = GDP per capita (log scale), y = life expectancy — reader answers the question in under a second. Right: x = GDP per capita, all points on a single horizontal line, luminance encodes life expectancy — reader cannot answer the question. Caption should name the channels and note the Cleveland & McGill rank of each: position (rank 1) vs. luminance (rank 6).] -->

That gap — that enormous difference in what you can do with the same numbers — is the subject of this chapter. It comes down to two concepts: **marks** (the geometric shapes used to show data) and **channels** (the visual properties that carry the actual values). Understanding them is the difference between a chart that communicates and one that merely depicts.

---

## The Grammar Beneath the Chart

Every chart you have ever seen is built from the same small set of pieces. There are only a handful of geometric primitives — the *marks* — and only a handful of visual properties through which those marks can vary — the *channels*. That is the whole vocabulary. Every scatterplot, bar chart, choropleth, and bubble chart is a specific combination of marks assigned specific channels, each channel carrying a specific attribute from the data.

This grammar was first named systematically by Jacques Bertin in *Sémiologie Graphique* in 1967. Bertin was a French cartographer who noticed that every map and every graph, no matter how complicated it looked, was doing exactly one thing: assigning data attributes to visual variables. He listed the variables. He showed, through worked examples ranging from Napoleon's retreat from Moscow to John Snow's cholera map, that some assignments worked and some did not — and that the difference was not aesthetic but perceptual. The eye could decode some visual variables accurately and others poorly, and this was not a matter of taste. It was a fact about human perception.

William Cleveland and Robert McGill ran the experiments in 1984 that gave Bertin's intuition a number. They showed subjects charts that differed only in how the same data was encoded. Different channels, same values. They asked subjects to estimate the ratios between pairs of values. The results produced a ranking — from most accurate channel to least — that has been replicated and extended ever since. Jeffrey Heer and Michael Bostock ran a version of the same experiment in 2010 using Mechanical Turk and got the same hierarchy. Tamara Munzner synthesized the whole tradition into a framework in her 2014 textbook *Visualization Analysis and Design* that is the standard reference for the field today.

I am going to give you that framework. But I want you to understand *why* it takes the shape it does, not just what the rules are. The rules without the mechanism are just a list to memorize. The mechanism makes the list obvious.

---

## Marks: The Geometric Primitives

A **mark** is a geometric element used to represent data. There are four types:

**Point marks** — single symbols, dots, circles. Each point typically represents one observation. Scatterplots are built from point marks.

**Line marks** — connected sequences of points. Line charts, slope graphs, trend lines. The line implies that the values *between* the plotted points exist and are interpolated. This matters: a line mark makes a claim about continuity. If that continuity is not in your data — if your categories are unrelated, if your x-axis is nominal rather than ordered — the line is lying.

**Area marks** — filled regions. Bar charts (the filled rectangle), area charts (the filled region under a line), treemaps (nested rectangles), choropleth maps (filled polygons). The region's *size* can encode magnitude (bar height encodes a value) or can merely contain another encoding (a country's polygon is filled by a color luminance encoding unemployment rate).

**Glyph marks** — composite symbols. A candlestick chart's body-with-wicks. A bullet graph's bar-with-bands. A wind-rose's directional arrow. Glyphs let a single mark encode multiple attributes simultaneously, at the cost of requiring the reader to learn the symbol.

<!-- → [FIGURE: Four-panel reference diagram — one panel per mark type. Point: scatterplot excerpt, each dot labeled "one observation." Line: line chart excerpt with annotation "implies interpolation between plotted values." Area: bar chart excerpt with annotation "height encodes magnitude." Glyph: single candlestick with wicks, each component labeled (open, close, high, low). Clean, minimal, no data — the marks themselves are the subject.] -->

The mark choice is not neutral. It is already making a claim about the data. Minard's 1869 flow map of Napoleon's Russian campaign — the one Tufte called "perhaps the best statistical graphic ever drawn" — uses a single continuous *area mark*: a band whose width varies as the army marches and retreats, the width encoding the number of soldiers still alive. The mark is the argument. The army is not a set of sample points at sample times; it is a continuous, depleting mass. A point mark at each waypoint would show locations. The area band shows the *depletion*. Same data, different mark, different claim.

---

## Channels: The Visual Variables

A **channel** is a property of a mark that can vary to encode data. The major channels are:

- **Position** — where on the x-axis, where on the y-axis
- **Length** — how long, how tall
- **Area** — how large the enclosing region is
- **Color hue** — what color (red vs. blue vs. green)
- **Color luminance** — how light or dark
- **Shape** — circle vs. square vs. triangle
- **Orientation** — the angle of a line or symbol

Every chart assigns data attributes to channels. A bar chart assigns a categorical variable to position-along-x and a quantitative variable to the height (length) of the bar. A bubble chart assigns two quantitative variables to x-position and y-position, and a third quantitative variable to the area of the circle. A choropleth map assigns a quantitative variable to color luminance.

The question is: which channel should carry which attribute? And the answer is not arbitrary. The Cleveland & McGill ranking tells you:

1. **Position along a common scale** — the most accurate channel for quantitative data.
2. **Position along non-aligned scales** — slightly less accurate because the reader cannot anchor against a shared reference.
3. **Length** — good, but without a shared baseline the eye loses some precision.
4. **Angle** — moderate. Good for angles between 30° and 150°; progressively worse outside that range.
5. **Area** — consistently underestimated. More on why in a moment.
6. **Color luminance** — the eye can distinguish maybe seven to ten levels reliably.
7. **Color hue** — cannot be ranked at all for quantitative data. The reader cannot decide whether red is greater than blue.
8. **Shape** — categorical only. Useless for quantity.

<!-- → [TABLE: Cleveland & McGill channel ranking — two columns: Rank (1–8) and Channel name, with a third column: Best attribute type (Quantitative / Categorical / Both). Add a fourth column: Stevens' exponent where applicable (position/length ≈ 1.0, area ≈ 0.7, luminance ≈ 0.33, hue/shape: N/A). Reader should be able to use this as a quick-reference card alongside the chapter.] -->

This ranking is the answer to the opening puzzle. The first chart used *position* for life expectancy — channel number one. The second chart used *color luminance* — channel number six. The reader in the second chart was trying to read quantity off a channel that human perception handles six times less accurately than position. The chart didn't fail because it was ugly. It failed because the assignment was wrong.

---

## Why Area Gets Underestimated: Stevens' Power Law

The mechanism behind the ranking is a psychophysical finding from Stanley Smith Stevens in 1957. Stevens showed that human perception of physical magnitudes follows a power function:

$$\Psi = k \cdot I^{\,a}$$

where Ψ is perceived intensity, *I* is actual physical intensity, *k* is a scaling constant, and *a* is an exponent that varies by the type of stimulus.

For **length**, *a* ≈ 1.0. Double a line, the eye sees a doubled line. Perception is nearly linear with reality. This is why position and length are at the top of the accuracy ranking — the perceptual system handles them honestly.

For **area**, *a* ≈ 0.7. Double an area, and the eye perceives only about 1.5 to 1.7 times the original — not 2 times. The eye *systematically underestimates* area. Not randomly, not occasionally, but consistently and predictably.

For **brightness (luminance)**, *a* ≈ 0.33. Even more compressed. A luminance that is physically doubled appears only slightly brighter.

This is why bubble charts fail when sized by radius instead of area. If you scale the bubble's *radius* with the data value, the *area* scales with the *square* of that radius. A value that doubles produces a bubble whose area is four times as large. The eye, applying Stevens' law with an exponent of 0.7, perceives that four-times-larger area as about 2.6 times larger. Three different numbers — the data (2×), the area (4×), the perceived area (2.6×) — and none of them matches.

The fix is to scale by area: if the value doubles, the area doubles, and the eye perceives roughly 1.5 times the original. Still not perfect — the sublinear exponent ensures the reader will always underestimate bubble-encoded magnitudes — but it is the least dishonest version of the encoding.

This is not a stylistic complaint about bubble charts. It is a statement about human perception. The chart is asking the reader to compare quantities encoded on a channel whose perceptual exponent is 0.7, when a channel with an exponent of 1.0 is available. The reader will be wrong, and they will be wrong in a systematic direction.

<!-- → [FIGURE: Side-by-side bubble pair showing the radius-vs-area distortion. Left: two bubbles sized by radius — one with value 1, one with value 2. Label shows actual area ratio (4×) vs. data ratio (2×) vs. perceived ratio under Stevens (≈2.6×). Right: same two bubbles sized by area — area ratio (2×) matches data ratio, perceived ratio ≈1.5×. The three-number divergence on the left is the teaching point; make all three numbers visible.] -->

---

## Magnitude Channels and Identity Channels

Munzner's framework adds one more cut that I find clarifying. The channels divide into two families:

**Magnitude channels** are suited for quantitative data — data that has a meaningful order and size. Position, length, area, luminance. These channels convey "more" and "less" in a way the reader can decode.

**Identity channels** are suited for categorical data — data with distinct labels but no inherent ordering. Hue, shape, texture. These channels convey "different from" but not "greater than."

The most common encoding error in visualization — in undergraduate work and in plenty of professional work — is putting a quantitative attribute on an identity channel. A chart where a numerical variable is encoded by color hue (bluer means more, redder means less, but the reader must decode the legend to know this and cannot estimate magnitudes from the hues directly) is asking the reader to do something the channel is not built for. The channel distinguishes categories; the data requires ranking. The mismatch is the failure.

The mirror error — putting a categorical attribute on a magnitude channel — is less common but also misleading. A bar chart of regional sales where the regions happen to be sorted alphabetically implies, through the magnitude channel, that West > South > Northeast > Midwest in some ordered sense. If the regions have no inherent order, the ordering the magnitude channel implies is false. This is why categorical bar charts are typically sorted by value: if the channel will imply an ordering anyway, make the ordering real.

Munzner calls these the **expressiveness principle** (the channel must be capable of expressing the attribute type — don't put quantity on hue) and the **effectiveness principle** (encode the most important attribute on the highest-ranked channel that is appropriate for its type). Two principles. Everything else in chart design is a consequence of them.

<!-- → [INFOGRAPHIC: Two-column taxonomy — Magnitude Channels vs. Identity Channels. Left column: Position, Length, Area, Luminance — each with a small icon and the note "suited to: quantitative / ordered data." Right column: Hue, Shape, Texture — each with a small icon and the note "suited to: categorical data." Below each column, a one-line example of the correct use and the most common misuse. The expressiveness and effectiveness principles appear as captions under the two columns.] -->

---

## Three Worked Examples from Before the Framework Had a Name

The framework is abstract. Three charts make it concrete. All three were made before Bertin named the grammar they were using.

**John Snow's 1854 cholera map of London.** Snow's question was: where in the Soho neighborhood are the cholera deaths concentrated? His most important attribute was location — two-dimensional, geographic, continuous. He used position-on-map to encode it. Each death is a point mark; its (x, y) coordinates are the address. Nothing else needed. The cluster around the Broad Street pump is visible immediately. Snow used the expressiveness principle (location requires a spatial channel) and the effectiveness principle (the most important attribute on the most accurate channel available). The pump handle came off. The outbreak ended.

**Charles Joseph Minard's 1869 Napoleon campaign.** Five channels, all carrying data. Geographic position (x and y) gives the spatial context. Band width encodes army size — area as a magnitude channel for a quantitative attribute. Hue (warm brown for the advance, black for the retreat) is an identity channel for the categorical attribute of direction. A separate temperature axis below is aligned to the geographic x-axis, letting the reader see the cold that killed the return. The chart shows Napoleon losing 400,000 soldiers in one graphic element, with the cause (Russian winter) visible in the subordinate panel. It works because every channel is carrying something real, and every assignment matches the expressiveness principle.

**Florence Nightingale's 1858 polar area chart.** Twelve months around a circle. Wedge area encodes deaths from three causes: preventable disease, wounds, and other. Hue distinguishes the causes. The seasonal swell of preventable deaths is preattentively obvious — the blue wedges dominate the winter months and dwarf the red wound-deaths. The chart helped persuade Parliament to fund sanitary reform in British military hospitals.

But. The polar area form means that the outer portions of each wedge are amplified relative to the inner portions. A wedge twice as long does not have twice the area; it has roughly four times as much. Nightingale was aware of this. She used the form anyway. The political argument she needed to make — *preventable deaths dwarfed inevitable ones* — was served by the amplification. The chart is rhetorically effective precisely because the area-channel distortion makes the disproportion look even more dramatic than it was.

This is the case that matters for how you think about the framework. The rules describe perceptual mechanisms. A designer who understands the mechanism can decide when the payoff justifies the cost. Nightingale knew. Most people who use polar area charts today — a form that has become fashionable in data journalism — do not. They get the drama without understanding that the drama is partially an artifact of a perceptual distortion, not just the data.

<!-- → [FIGURE: Nightingale's 1858 polar area chart rendered twice. Left: radius-linear (original) — wedges amplified, seasonal swell of preventable deaths is visually dominant. Right: area-corrected version — same data, smaller visual spread. Caption: "The distortion is the argument. Left panel is what Nightingale published. Right panel is what the data would show if area were scaled honestly. The difference is the rhetorical choice." Make the two versions visually comparable at the same size.] -->

---

## How This Changes the Prompt You Write

The marks-and-channels framework is not only a lens for reading charts. It is a specification language for building them.

When you ask Claude Code to "make a box plot of these AI capability scores," Claude Code will produce something that looks like a box plot. It may show the full range instead of the interquartile range. It may size the outliers as ticks instead of points. It may scale the y-axis to the data range rather than the meaningful range. It may encode category identity using a luminance gradient (a magnitude channel) instead of hue (an identity channel), because luminance gradients look professional. Any of these is a channel-theory violation, and without the vocabulary to name it, you will not know how to fix it in a follow-up prompt.

With the vocabulary, you can write this instead:

```
x-position: cognitive domain (categorical, 5 values — no inherent order,
  sort by median for readability).
y-position: capability score (quantitative, range 10–100, shared y-axis
  across all boxes for direct comparison).
Box: rectangle mark. Top edge at Q3, bottom edge at Q1. Median as a
  horizontal line at the 50th percentile inside the box.
Whiskers: line marks. Top whisker to the maximum value within
  Q3 + 1.5*IQR (Tukey's rule). Bottom to Q1 - 1.5*IQR.
Outliers: point marks beyond the 1.5*IQR fences.
Color hue: category identity — one distinct hue per domain, redundant
  with x-position for accessibility. This is an identity channel for a
  categorical attribute.
```

That prompt is the channel decomposition. Claude Code now has a specification, not a guess. The chart comes back right on the first attempt because the marks-and-channels assignment is in the prompt, not in whatever defaults the model reaches for.

Every chart in this book has a version of this specification. Every chapter adds constraints — zero baselines for bar charts, label-length heuristics, color scale selection — but the core pattern is always the same: name the marks, specify the channel-to-attribute assignments, justify each assignment using the expressiveness and effectiveness principles.

---

## The Feynman Test

Feynman had a test for understanding: if you can teach something to a freshman, you understand it. The lecture is over when the student can work the problem, not just recognize the answer.

The test for this chapter is simpler. Pick a chart you saw today — a newspaper, a dashboard, a research paper, anything. Give yourself ninety seconds to answer these questions:

1. What are the marks?
2. What channels are those marks using to vary?
3. What data attribute does each channel encode?
4. For each quantitative attribute, is the channel a magnitude channel?
5. For each categorical attribute, is the channel an identity channel?
6. Any mismatches?

If you can do that in ninety seconds, you know the chapter. If you cannot, re-read the channels section and try again on a different chart. The vocabulary is small. The application is fast once the vocabulary is there.

The two scatterplots at the beginning of this chapter are the simplest possible test case. The first chart used position — magnitude channel, quantitative attribute, highest-ranked option, expressiveness satisfied, effectiveness satisfied. The second chart used luminance — magnitude channel, quantitative attribute, expressiveness satisfied, effectiveness violated (luminance is sixth; position was available and is first). One chart works. One chart does not.

The rest of this book is the details.

---

## Exercises

### Warm-up

**Exercise 3.1 — Channel identification.** For each of the following charts, identify (a) the marks, (b) the channels in use, (c) the data attribute each channel encodes, and (d) whether each channel-attribute pairing satisfies the expressiveness principle.

- A bubble chart where x-position is GDP per capita, y-position is life expectancy, bubble area is population, and bubble hue is continent.
- A choropleth map where polygon fill luminance encodes unemployment rate.
- A scatterplot where point shape (circle, square, triangle) encodes year (2020, 2021, 2022).

**Exercise 3.2 — The opening puzzle, reversed.** The chapter opens with two encodings of the same dataset: position for life expectancy (works), luminance for life expectancy (fails). Design a third encoding of the same data that is *worse* than the luminance version. Name the channel, identify the expressiveness or effectiveness violation, and explain using Stevens' power law or the Cleveland & McGill ranking why it fails.

**Exercise 3.3 — Mark claim.** A dataset records daily closing stock prices for one company over one year. Sketch (in words) the same data rendered as (a) a point mark per day and (b) a line mark connecting those points. What claim does the line make that the points do not? Under what circumstances is that claim false?

### Application

**Exercise 3.4 — Channel choice for a three-attribute dataset.** You have 50 countries: country name (categorical), GDP per capita (quantitative), and continent (categorical, 6 values). Design a chart that shows GDP ranked across countries with continent as a secondary identifier. Specify the marks and all channel-attribute assignments. For each channel, name the Munzner principle it satisfies or violates and explain why you made the trade-off you did.

**Exercise 3.5 — Bubble chart repair.** A colleague submits a bubble chart where bubble *radius* scales linearly with population. The largest population is 1.4 billion (China); the smallest is 400,000 (Iceland). Calculate the area ratio the chart produces. Then calculate the area ratio the corrected (area-linear) encoding would produce. Using Stevens' power law (exponent 0.7), estimate the perceived ratio under each encoding. How far is each from the true data ratio?

**Exercise 3.6 — Audit a published chart.** Find a chart published in the past month — news, financial report, research paper, or dashboard. Apply the marks-and-channels framework. List every channel in use and the attribute it encodes. Identify any expressiveness violation (identity channel on a magnitude attribute, or vice versa) and any effectiveness violation (a more important attribute on a lower-ranked channel than a less important one). Specify one concrete redesign with a one-paragraph perceptual justification.

### Synthesis

**Exercise 3.7 — The Nightingale defense.** Nightingale's polar area chart violates the area-perception accuracy rule. The chapter argues she knew and chose to use the distortion for rhetorical effect. Make the case for and against applying the same reasoning to a contemporary humanitarian-data context of your choosing. Where does the rhetorical-vs-analytical distinction land you, and what would a reader need to know to evaluate your chart honestly?

**Exercise 3.8 — Minard decomposition.** Look up Charles Joseph Minard's 1869 flow map of Napoleon's Russian campaign. List every mark and every channel-to-attribute mapping in the chart. Identify the most important attribute, name the channel it uses, and justify the choice using the effectiveness principle. Then write a Claude Code prompt — using the show / say / constrain / verify structure — that would produce a contemporary version of the same channel decomposition applied to a different dataset of your choice.

### Challenge

**Exercise 3.9 — Replicate the ranking on a small scale.** Design a five-question estimation survey: same dataset, same values, five different encodings (bar chart, pie chart, bubble chart, choropleth, radial bar). Ask three people to estimate specific values from each chart. Record their answers. Report how the accuracy varies by channel and compare your results to the Cleveland & McGill ranking. Where does your small-N replication agree with the published ranking? Where does it diverge, and what might explain the divergence?

**Exercise 3.10 — Channel limits in your domain.** Identify a chart type that is conventional in your professional or research domain. Diagnose its channel use against the effectiveness and expressiveness principles. If the domain's conventions override the ranking, identify the domain-specific reason — is it historical habit, print constraints, audience familiarity, or a genuine case where the override is perceptually defensible? Argue the case either way using the Nightingale framework from the chapter.

---

## Key Terms

**Mark.** A geometric primitive (point, line, area, glyph) used to represent data.

**Channel.** A visual variable (position, length, area, hue, luminance, shape, orientation) that encodes a data attribute by varying.

**Magnitude channel.** A channel suited to quantitative or ordered data — position, length, area, luminance. These convey "more" and "less."

**Identity channel.** A channel suited to categorical data — hue, shape, texture. These convey "different from" but not "greater than."

**Expressiveness principle (Munzner).** The channel must be capable of expressing the attribute type. Quantity on magnitude channels; categories on identity channels.

**Effectiveness principle (Munzner).** Encode the most important attribute on the highest-ranked appropriate channel.

**Cleveland & McGill ranking (1984).** Empirical accuracy hierarchy: position > length > angle > area > luminance > hue.

**Stevens' power law (1957).** Perceived magnitude = k · (actual magnitude)^a. Length: a ≈ 1.0 (linear). Area: a ≈ 0.7 (sublinear — consistently underestimated). Luminance: a ≈ 0.33 (strongly sublinear). The mechanism behind why the ranking takes the shape it takes.

**Redundant encoding.** Two channels carrying the same attribute. Useful for accessibility; clutter when applied without purpose.

---

## LLM Exercise — Chapter 3: Marks and Channels

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A channel-mapping audit document for a real dataset, plus the Claude Code prompt that builds the corresponding chart.

**Tool:** Claude Code (for the build) + Claude chat (for the audit)

---

**The Prompt (channel audit):**

```
I have a dataset of [DESCRIBE: rows, columns, types — for example,
"5 cognitive domains and 80 simulated capability scores per domain,
score range 10-100"] and a communication goal: [DESCRIBE: what the
reader needs to know in 5 seconds].

Walk me through the marks-and-channels analysis using the
Bertin / Cleveland & McGill / Munzner framework:

1. Identify each data attribute and classify as categorical, ordered,
   or quantitative.

2. Identify the most important attribute given the communication goal.

3. Recommend a chart type by applying Munzner's expressiveness and
   effectiveness principles. Use the Cleveland & McGill ranking
   (replicated by Heer & Bostock 2010) as the scaffold.

4. Specify the marks (point, line, area, glyph) and the
   channel-to-attribute mappings precisely enough that the chart could
   be built from the specification alone.

5. Flag any channel that is being used redundantly. Justify the
   redundancy in terms of accessibility, emphasis, or legend support.

6. Cite Stevens' power law where it applies (bubble chart area-vs-radius;
   choropleth luminance accuracy; pie chart angle accuracy).

Then write a single Claude Code prompt that would produce the chart.
The prompt should follow the four-move structure (show, say, constrain,
verify) and should be precise enough that Claude Code produces a usable
output on the first attempt.
```

---

**What this produces:** A markdown document with the channel audit (six sections) and a copy-paste-ready Claude Code prompt. Save as `chapter-03-channel-audit.md`.

**How to adapt this prompt:**
- *For your own domain:* Replace the dataset description with your data. The structure works for any dataset.
- *For ChatGPT / Gemini:* Works as-is. Some LLMs default to "use any visually appealing chart" rather than the Cleveland & McGill ranking; the explicit instruction to use the ranking is the constraint that fixes this.
- *For Claude Code:* Submit the channel audit document as context, then ask Claude Code to build the chart. The two-step process (audit, then build) makes the encoding decisions explicit before the code runs.
- *For a Claude Project:* Save the channel framework as the system prompt; the audit prompt becomes the user message. The same Project can serve every chapter's LLM Exercise.

**Connection to previous chapters:** The attribute types introduced in Chapter 2 (categorical, ordered, quantitative) are the inputs to the expressiveness principle here. If a concept feels unfamiliar, the prerequisite is there.

**Preview of next chapter:** Chapter 4 takes the channel framework and applies it to chart selection — given the data attributes and the communication goal, which chart type is the right one? Cairo's ethical frame joins the framework here: a chart that fails its reader is not merely a design failure.

---

## Further Reading

- **Bertin, Jacques. (1967, English ed. 1983).** *Semiology of Graphics.* ESRI Press reissue. Chapters 1 and 6 are the essential sections.
- **Cleveland, William S., and Robert McGill. (1984).** "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association* 79(387). The foundational empirical ranking.
- **Heer, Jeffrey, and Michael Bostock. (2010).** "Crowdsourcing Graphical Perception: Using Mechanical Turk to Assess Visualization Design." *CHI '10.* The replication that extended the ranking to pie charts, treemaps, and circle packing.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* CRC Press. Chapter 5 is the comprehensive channel taxonomy. If you read one academic textbook on visualization, read this one.
- **Stevens, S. S. (1957).** "On the Psychophysical Law." *Psychological Review* 64(3). The power-law mechanism. Read for the formulation; later work has refined the exponents but not overturned the structure.
- **Kelleher, Curran.** Observable notebooks and YouTube tutorials. The marks-and-channels material is the accessible entry point for all of this.
- **Tufte, Edward R. (1983, 2nd ed. 2001).** *The Visual Display of Quantitative Information.* The Minard, Snow, and Nightingale readings in Chapter 1 are the most-cited treatments in the literature.
