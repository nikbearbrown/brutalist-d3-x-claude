# Chapter 3 — Reading a Dataset
*Read the Data Before You Reach for the Code.*

## Three suggested titles

- Reading a Dataset Before Touching D3
- The Work Before the Work
- The Reader's Question vs. the Analyst's Question

---

## Chapter overview

By the end of this chapter you will know how to read a dataset before you build a chart from it. You will be able to identify the data types present (categorical, ordinal, quantitative, temporal, geographic), distinguish the analyst's question from the reader's question (and know which one the chart must answer), apply Cairo's "compared with what?" criterion before any chart-type decision, and recognize when your dataset does not actually answer the question the chart is supposed to address. This is the pre-chart-type work that determines whether Chapter 2's framework has anything to operate on.

---

## Learning objectives

1. **(Apply)** Given a raw dataset, identify the data types present (categorical, ordinal, quantitative, temporal, geographic) and the relationships available to visualize.
2. **(Analyze)** Formulate the communication question a visualization should answer — distinguishing the analyst's question (what is interesting in the data) from the reader's question (what they need to know).
3. **(Evaluate)** Assess whether a proposed chart type answers the communication question or answers a different question the author found interesting (the FiveThirtyEight Nigeria failure mode).

---

## Opening case — "visualize refugee flows"

A research team asks you to "visualize refugee flows." The phrase sounds like a chart request. It is not.

The phrase contains a referent ("refugee flows") and a verb ("visualize"). It contains no communication question. *Refugee flows* could mean: the count of refugees by origin country in a single year, the change in refugee counts by destination country across five years, the proportion of refugees relative to host-country population, the path of individual refugees from origin to first reception to final settlement, the rate of new arrivals per month, or any of a dozen other things. Each of these is a different chart, a different dataset, a different communication question.

If you accept "visualize refugee flows" as a brief and walk to Claude Code, you will produce a chart. The chart will be technically correct. It will probably not answer any specific question, because no specific question was asked. It will be the chart the dataset most naturally invited, which may or may not be the chart the team needed.

This is the work before the work. Before you reach for marks and channels (Chapter 1), before you locate the dataset in the FT Visual Vocabulary (Chapter 2), before you write a Claude Code prompt (Chapter 4), you read the dataset and you formulate the communication question. Cairo's "compared with what?" check is the central move of this reading.

The MBTA visualization team (Mike Barry and Brian Card, 2014) named this work explicitly: *"Understanding what information would be interesting to people and then narrowing down our focus based on the data that we could gather."* The first part — what is interesting to people — is the reader's question. The second part — what the data could gather — is the analyst's data audit. The two together produce the chart specification.

---

## Theoretical grounding — Cairo's reader/analyst distinction, FT Visual Vocabulary's data types, the MBTA process

This chapter draws on three sources, each at the moment its specific contribution is needed.

**Cairo's distinction between the analyst's question and the reader's question.** The analyst (you, the data owner, the researcher) has a question that emerged from the data — patterns you noticed, anomalies you want to highlight, comparisons you found compelling. The reader (the audience for the chart) has a different question — what they need to know to make a decision, evaluate a claim, or understand a phenomenon. These questions overlap sometimes; they often do not. A chart that answers the analyst's question and not the reader's is a chart that interests the analyst more than it serves the audience. Cairo names this as the most common diagnostic failure in data journalism and consequential in research communication.

**The FT Visual Vocabulary data type taxonomy.** The vocabulary's pre-chart-type decision tree begins with: *what kind of data do you have?* The answer determines what functional categories are even available. Five primary types: categorical (discrete labels with no inherent order), ordinal (discrete labels with order — small/medium/large; freshman/sophomore/junior/senior), quantitative (numerical values, continuous or discrete), temporal (dates, times, durations), geographic (locations, regions). A dataset usually contains several types; the chart depends on which type is the *primary* one for the communication question.

**The MBTA project's "interesting to people" framing.** Barry and Card's MBTA visualization project began with three guiding questions about the Boston transit system: "When and where are the trains crowded or delayed? How do snowstorms affect the system? How congested is my route?" Each question is reader-focused (what would someone using the system want to know) and specific (a chart can be evaluated against whether it answers it). The project's design lesson, applied throughout this chapter: start with the question, not the data.

---

## Concept 1 — Data type identification

The first move when a dataset arrives is to identify the data types present. The types are not always obvious, and misidentification produces predictable downstream failures.

### The five primary types

**Categorical.** Discrete labels with no inherent order. Country names, sector classifications, gender categories (in classifications that treat gender as categorical), color preferences. The encoding decision: identity channels (hue, shape) work; magnitude channels (position-implying-order) introduce false order. If you sort the categories by some other variable (e.g., by funding amount), you create a *derived* order — but the category itself remains unordered.

**Ordinal.** Discrete labels with order, but without uniform spacing between values. Education levels (high school / bachelor's / master's / PhD). Likert-scale responses (strongly disagree / disagree / neutral / agree / strongly agree). T-shirt sizes (S/M/L/XL). The order matters; the *distance* between adjacent values is not necessarily meaningful or uniform. Encoding: position works for order; quantitative-magnitude operations (averaging, summing) require justification.

**Quantitative.** Numerical values with meaningful magnitudes and uniform distances. Height, weight, dollars, counts, percentages, rates. Subdivisions: discrete (counts of integer events) vs. continuous (real-valued measurements like temperature or length); ratio (with a true zero — height, mass) vs. interval (no true zero — Celsius temperature, calendar year). All quantitative variables can be averaged, summed, and encoded on magnitude channels (position, length, area, luminance).

**Temporal.** Dates, times, durations. Technically a special case of quantitative (with the appropriate scale), but visualization treats temporal data distinctly because of conventions: time always runs left-to-right (Western reading order), the temporal axis often shows discrete tick marks at meaningful intervals (years, months, days), and time has cyclical structure (months of the year, hours of the day) that linear quantitative variables don't.

**Geographic.** Locations or regions. Sub-types: point geographies (specific locations — cities, addresses, GPS coordinates), polygon geographies (administrative units — countries, states, ZIP codes), connection geographies (origin-destination pairs — flight paths, migration corridors). The encoding decision: position on a map is the natural choice, with specific design constraints around projection (Chapter 12).

### Mixed datasets

Most real datasets contain multiple types. The MBTA dataset has temporal (timestamp), geographic (station location), categorical (line color: red/orange/blue/green), quantitative (passenger count), and ordinal (peak/off-peak/late-night) variables all in one table. The chart you build uses a subset, determined by the communication question.

Identifying types is therefore a *filtering* step: of all the variables available, which subset answers the question? The answer narrows what charts are even relevant.

### Common type-identification failures

**Treating ordinal as categorical.** Education level is ordinal (high school < bachelor's < master's < PhD). A chart that treats it as categorical (sorted alphabetically rather than by educational attainment) loses the order. The reader cannot see the progression.

**Treating ordinal as quantitative.** Likert-scale responses are ordinal, not quantitative. The distance between "agree" and "strongly agree" is not the same as the distance between "neutral" and "agree." Computing means and standard deviations on Likert data is technically wrong (though common); visualizing them as if they were quantitative compounds the wrongness.

**Treating discrete quantitative as continuous.** A count of children per family (0, 1, 2, 3, 4+) is discrete. Drawing a smooth density curve over it implies values like 2.5 children, which don't exist. The right form is a histogram or a stem-and-leaf plot, not a kernel density estimate.

**Missing the geographic structure.** A dataset that has geographic information embedded in text (city names, state abbreviations, ZIP codes) but not in a structured location field. The geographic potential is invisible unless someone notices.

> ### ↳ Dig Deeper — Type-identify a dataset you work with
>
> **Prompt:**
>
> > Take a dataset I work with regularly. Walk through every column. For each column, identify the data type (categorical, ordinal, quantitative, temporal, geographic) and any sub-type details (continuous vs. discrete, point vs. polygon geography, etc.). Identify any column whose type might be misclassified — for example, a numerical-looking column that is actually categorical (postal codes), or an ordinal column being treated as categorical. Then specify what charts each type opens up and what charts each type rules out.
>
> **What to do with the output:** Save the column-by-column type audit. The audit is the prerequisite for every chart you build from that dataset.

---

## Concept 2 — The analyst's question vs. the reader's question

The single most consequential pre-chart distinction is whose question the chart answers.

### The analyst's question

The analyst — the person who works with the data day to day, the researcher who collected it, the data owner — has questions that emerged from the data:

- "Notice that this metric spiked in October."
- "There's an unusual cluster in the northwest region."
- "These two variables are weakly correlated but not what I expected."
- "The distribution has a long right tail that the mean hides."

The analyst's questions are interesting to the analyst because the analyst already understands the surrounding context. The questions arise from contact with the data over time. They are often *exploratory* — questions the analyst is still working through.

### The reader's question

The reader — the audience for the chart — has questions that arise from a different context. They want to:

- Make a decision (should we fund this program? should I take this medication?).
- Understand a phenomenon (why are home prices rising? what's causing the outbreak?).
- Evaluate a claim (is this reform actually working? is the trend the headline reports real?).
- Get oriented in unfamiliar territory (what is this dataset about? what should I notice?).

The reader's questions are usually *summative* (give me an answer) rather than exploratory. The reader does not have the analyst's context. The reader is busy. The reader is reading a chart, not analyzing data.

### Why the distinction matters

The chart must answer the reader's question. Not the analyst's question. This is harder than it sounds, because the analyst is the one designing the chart, and the analyst's questions are the ones the analyst notices first.

A chart that answers the analyst's question without first answering the reader's question often looks like:

- A chart with multiple overlapping trends, where the analyst sees the "interesting deviation" but the reader cannot find the main signal.
- A chart that highlights a statistical pattern (the long tail, the weak correlation) the reader needs background to interpret.
- A chart that uses the analyst's vocabulary (technical terms, internal categories) without translation.
- A chart that answers the question "what is interesting about this data?" rather than "what does this data tell me?"

The Cairo frame applies: a chart that answers the analyst's question while a more appropriate chart for the reader was available is, in Cairo's strong reading, a moral failure. The designer prioritized their own intellectual interest over the reader's understanding.

### Reconciling the two

The questions sometimes align. Often they do not. The reconciliation is to start with the reader's question and work back. What does the audience need to know? What decision are they making? What context do they bring? Once the reader's question is named, the analyst's question can be checked: does the data support the reader's question, or does it support a different question the analyst found more interesting?

In the MBTA project, the team's three questions ("when and where are trains crowded," "how do snowstorms affect the system," "how congested is my route") are all reader-focused. The analyst version of these questions might have been "what is the system's load distribution," "how does ridership respond to weather variables," "what is the reliability profile of the network." The two sets are about the same data; the reader's set is what the chart answers.

> ### ↳ Dig Deeper — A chart from your domain, audited for reader vs. analyst
>
> **Prompt:**
>
> > Take a chart I or my team produced recently. Walk it through the analyst-vs-reader distinction. What was the analyst's question (what was interesting to the producer)? What is the reader's question (what does the audience need to know)? Where do they overlap, and where do they diverge? If the chart answered the analyst's question but not the reader's, specify the redesign that flips the priority.
>
> **What to do with the output:** Save the audit. The pattern reapplies to every chart you produce.

---

## Concept 3 — "Compared with what?"

Cairo's question is the mandatory check before any chart is finalized. Every quantitative claim a chart makes must be set against a reference — explicit or implicit — that gives the claim meaning.

A chart of "Q4 revenue by region" makes a quantitative claim about each region's revenue. *Compared with what?* The other regions' Q4 revenue (within-period comparison). The same regions' Q3 revenue (quarter-over-quarter). The same regions' Q4 last year (year-over-year). The annual target (target comparison). Each is a different chart because each answers a different "compared with what."

The check forces the designer to name the comparison the chart actually makes. A chart that fails the check makes a claim without a reference and produces a meaningless reading.

### Common "compared with what?" failures

**Absolute counts where ratios are needed.** A choropleth of "absolute number of cancer diagnoses by U.S. state" looks informative until you realize that California (population 39M) and Wyoming (population 0.6M) cannot be meaningfully compared on absolute counts. The "compared with what?" answer should be *rate per population*: cancer diagnoses per 100,000 residents. The redesign uses rates, not counts. (Chapter 12 walks the choropleth-specific version of this rule.)

**Time series without baseline.** A line chart of "S&P 500 over five years" makes a claim about market change. *Compared with what?* The market has gone up 60%; how does that compare to inflation (also up 20%)? To peer indices (the FTSE, the Nikkei)? To a 5% target return? Each comparison reveals different information. The chart that just shows the absolute price line is making the comparison "compared with the starting price" — which is sometimes the right comparison and often is not.

**Cross-sectional comparison without controls.** A bar chart of "average income by region" compares regions on income — but compared with what? The cost of living (regions vary). The age distribution (regions with more retirees have different income profiles). The industry composition. Without controls, the chart shows differences that may be artifacts of the missing comparison.

**Single-value claims.** A chart that shows "65% support" without comparing to a previous measurement, a different population, or a margin of error is making an unanchored claim. *Compared with what?* If support was 60% last year, the current 65% is a meaningful increase. If support is 95% in a peer country, the 65% is low. The single number means nothing without a reference.

### The check applied

Every chart specification should answer the "compared with what?" question explicitly. The four-step framework from Chapter 2 builds this in: step 1 (key message) requires the comparison to be named in the message. "Funding for food security is highest" fails the check; "funding for food security is highest, more than twice the next-largest category" makes the comparison explicit.

When the comparison is missing from the message, it is missing from the chart. The fix is to revise the message before the chart is built.

---

## Concept 4 — Identifying the relationships your data supports

Step 2 of Chapter 2's framework asked you to name the data structure. This concept goes deeper: given the data types and the question, what *relationships* does the data actually support?

The eight functional categories from Chapter 2 each correspond to a relationship type:

- **Comparison** — independent values or categories on a single dimension.
- **Change over time** — a value or set of values across a continuous temporal dimension.
- **Distribution** — the spread of a single variable.
- **Relationship (correlation)** — how two or more variables co-vary.
- **Part-to-whole** — components summing to a defined total.
- **Hierarchy** — nested or layered structure.
- **Flow** — movement or transition between states.
- **Spatial** — patterns tied to geographic location.

Reading a dataset includes identifying which of these relationships the data can actually support. Sometimes the data supports multiple; sometimes only one; sometimes the relationship the question implies is not actually present in the data.

### Worked example — a humanitarian dataset

Take the example dataset from Chapter 2: monthly humanitarian funding amounts across five sectors for one country across three years (2022–2024).

**Data types present:**
- Sector — categorical, 5 values, no inherent order.
- Month — temporal, 36 values (3 years × 12 months).
- Country — categorical, 1 value (constant).
- Funding amount — quantitative, ratio scale (USD).

**Relationships the data supports:**

- *Comparison:* funding by sector (cumulative or for a specific period) — yes, the categorical sector + quantitative funding gives this directly.
- *Change over time:* funding over the 36-month period — yes, the temporal axis + quantitative funding gives this.
- *Distribution:* the spread of monthly funding amounts within each sector — yes, but n=36 per sector is small; the histogram won't show much.
- *Relationship (correlation):* between two quantitative variables — *no*, the dataset has only one quantitative variable. To support correlation, you'd need a second (e.g., emergency severity index, displaced population count).
- *Part-to-whole:* sectors summing to the total — yes, the sectors are mutually exclusive components of total funding.
- *Hierarchy:* nested structure — *not directly*, unless the sectors have sub-sectors not shown in the dataset.
- *Flow:* transitions between sectors — *not really*, unless the data shows fund reallocation events (which it doesn't in the basic version).
- *Spatial:* geographic patterns — *no*, the country is constant.

So the dataset supports four relationships natively: comparison, change over time, distribution (weakly, for short series), and part-to-whole. The chart you build depends on which of these the communication question targets. Different questions, different charts.

The relationships the data does *not* support are equally important. If the question is "how does sector X compare with sector Y in another country," the dataset cannot answer it — country is constant. The right move is to acknowledge the data gap, not to build a chart that pretends to answer.

### When the data doesn't answer the question

This is the most uncomfortable diagnostic. Sometimes the question is good and the data does not support it. The honest moves:

**Find better data.** Add the missing variable (emergency severity, displaced population). Add the missing geographic dimension. Reframe the question in terms the data does support.

**Reframe the question.** "How does funding compare across sectors?" works with this dataset. "How does funding compare across countries?" does not. Reframe the question to match the data, or acknowledge the gap.

**Acknowledge the gap honestly.** If you must produce a chart with the available data, name what the data does and does not show. A chart of single-country funding does not support claims about cross-country differences; the chart's title and annotations should make this clear.

The failure mode to avoid: producing a chart that *looks like* it answers the original question but actually answers a different one because the data only supported the different one. The FiveThirtyEight Nigeria case from the Introduction is exactly this failure: the question was about kidnappings; the data was about news stories; the chart pretended the two were equivalent.

> ### ↳ Dig Deeper — Audit a question against your data
>
> **Prompt:**
>
> > Take a question I want to answer with a dataset I have. Walk through whether the data actually supports the question. Identify each variable I would need to answer the question; check whether the dataset contains it. If any are missing, propose the alternatives: collect more data, reframe the question, or acknowledge the gap. Apply Cairo's frame: at what point does my dataset no longer ethically support the chart I'm planning to make?
>
> **What to do with the output:** Save the audit. This is the discipline that prevents publishing a chart whose visual claims exceed its empirical support.

---

## Mid-chapter checkpoint

Pick a dataset you have on hand. Identify every column's data type. Name three communication questions the dataset could plausibly answer. For each question, identify which relationship(s) the dataset supports. Apply Cairo's "compared with what?" check to each question. Note any question where the data is insufficient.

You should be able to do this in five minutes. If you cannot, the dataset is unusual or the question is unfocused.

---

## Extended worked example — applying the audit to the HAI choropleth dataset

The Humanitarians AI choropleth example in `pantry/visualization/bubble-map.html` (and `pantry/Visualizing Origin to Destination Flows.txt`) uses geographic data to visualize US food assistance. Walk the audit.

### Step 1 — Identify data types

The dataset:

- State — categorical (US states), with implicit geographic structure (each state has a polygon).
- Total food assistance dollars — quantitative, ratio scale.
- Population — quantitative (for ratio normalization if needed).
- Year — temporal (if the dataset is multi-year; for one year, this column is constant).

### Step 2 — Identify the analyst's vs. the reader's question

**Analyst's question (probably):** "Where is food assistance flowing? Are there clusters? Are there outliers?" — exploratory, pattern-finding.

**Reader's question (depends on audience):**
- *Policymaker:* "Where is the program reaching the most people, and where is it under-reaching given need?"
- *Analyst at a peer NGO:* "How does our program's geographic footprint compare with the federal program?"
- *General public reader:* "Which states get the most help, and is it where the need is highest?"

The three reader questions are different. The chart that answers each is different.

### Step 3 — Apply "compared with what?"

For the policymaker version: "Where is the program reaching the most people compared with where need is highest?" The implicit comparison is *food assistance per capita* vs. *food insecurity rate*. The chart needs both variables; a single-variable choropleth (just dollars per state) doesn't make this comparison.

For the peer-NGO version: "How does our program compare with the federal program on geographic distribution?" The comparison is *between two programs*. A single-program choropleth doesn't make this comparison either.

For the general-public version: "Which states get the most help, and is it where need is highest?" The comparison is *program reach vs. need*. Same data requirement as the policymaker version.

In all three cases, the single-variable choropleth (just food assistance dollars by state) fails the "compared with what?" check. The chart that answers the question needs at least two variables: assistance and need (or assistance and program comparison).

### Step 4 — Identify what the dataset actually supports

If the dataset only contains state + total assistance + population, then:

- It supports a chart of *assistance per capita* (which is a "compared with what?" answer to "is assistance going where the population is").
- It does *not* support a chart of *assistance per food-insecure household* (which would require food-insecurity data).
- It does *not* support a chart comparing this program's reach with another program's reach (which would require the second program's data).

The honest move: build the chart the data supports (assistance per capita choropleth), and explicitly name what the chart does *not* tell you (whether assistance matches food-insecurity rate, whether this program differs from peers).

### Step 5 — The chart specification follows from the audit

Now Chapter 2's framework operates with full information:

- **Key message:** "Food assistance dollars per capita vary by a factor of 10 across U.S. states, with the highest per-capita rates in the rural Southwest."
- **Data structure:** Geographic (state polygons) + quantitative (assistance dollars) + quantitative (population). Derived: assistance per capita.
- **Functional category:** Spatial (geographic patterns).
- **Specific form:** Choropleth, with color luminance encoding assistance per capita (sequential, pale-to-dark). Title and annotations explicitly note that the chart shows program reach, not need or efficacy.

This chart honestly answers the question the data supports. The reader knows what they are seeing. The "compared with what?" answer is explicit (per capita rates across states). The chart's claims do not exceed its data.

This is the chart the audit produces. It is also a different chart than the bubble-map.html implementation actually shows — which uses bubble area (proportional symbols at state centroids) rather than choropleth color. The trade-off between these forms is Chapter 12's territory; the audit is the same.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can identify data types in any dataset (categorical, ordinal, quantitative, temporal, geographic) and recognize the failure modes of misclassification — treating ordinal as categorical, treating Likert as quantitative, treating discrete as continuous, missing geographic structure embedded in text.

You can distinguish the analyst's question (exploratory, pattern-finding, interesting to the producer) from the reader's question (summative, decision-supporting, what the audience needs to know). You know the chart must answer the reader's question, and you have a workflow for surfacing the reader's question when the analyst's question is the more obvious starting point.

You can apply Cairo's "compared with what?" check to any chart specification. You can name the four common failures (absolute counts where ratios are needed, time series without baseline, cross-sectional comparison without controls, single-value claims) and the redesign each requires.

You can identify which of the eight relationships your dataset actually supports — and recognize when the dataset does *not* support the question being asked. You know the three honest moves when data is insufficient: find better data, reframe the question, or acknowledge the gap.

The thing to watch for, going forward, is the temptation to skip this chapter's work. Most charts that fail in production fail because the work of this chapter was skipped: the data types weren't audited, the reader's question wasn't named, the comparison wasn't made explicit, the data didn't actually support the chart. Once these are done, Chapters 1, 2, and 4 produce the chart almost mechanically. Without them, the rest of the book operates on hope.

---

## Key terms

- **Categorical, ordinal, quantitative, temporal, geographic.** The five primary data types. The first move when reading a dataset is to identify which types are present in which columns.
- **Analyst's question vs. reader's question.** The analyst's question emerges from data exploration; the reader's question emerges from audience need. The chart must answer the reader's question.
- **"Compared with what?"** Cairo's mandatory check. Every quantitative claim must be set against an explicit reference.
- **Absolute counts where ratios are needed.** The most common "compared with what?" failure. The fix: rates, percentages, or per-capita normalization.
- **Eight relationships.** The structural patterns in data that map to functional categories (Chapter 2): comparison, change over time, distribution, relationship, part-to-whole, hierarchy, flow, spatial.
- **Data gap.** When the dataset does not support the question being asked. Honest moves: find better data, reframe the question, acknowledge the gap.

---

## Discussion questions

1. The analyst-vs-reader distinction was named in Cairo's *The Truthful Art*. Why is it harder to apply than it sounds? What practical workflow steps would force you to surface the reader's question before the chart is built?
2. Cairo's "compared with what?" check is a methodological move. Frame the check as a habit rather than a one-off audit. What would the habit look like in your professional practice?
3. The four common "compared with what?" failures in Concept 3 are all forms of unanchored claim. Which is most common in published charts you read? Which is most common in charts you produce?
4. Take a dataset you've worked with where the question and the data did not align. What was the gap? What was the move (find better data, reframe, acknowledge)?
5. *Cross-chapter synthesis.* Chapter 4 covers the Claude Code workflow. The audit work of Chapter 3 is *prerequisite* to the prompts of Chapter 4. Frame the relationship: what does Chapter 4 assume about Chapter 3's outputs?

---

## Exercises

### Warm-up

**Exercise 3.1** — *Type identification.* For each of the following columns, identify the data type and any relevant sub-type:
- ZIP code (numeric format).
- Customer satisfaction (Likert: 1–5).
- Number of children per household.
- Latitude in decimal degrees.
- Date of birth.
- Education level (high school, bachelor's, master's, PhD).

**Exercise 3.2** — *Question reframing.* Take this analyst's question: "What's interesting about our customer churn data?" Rewrite as three reader-focused questions targeting different audiences (marketing manager, executive, customer-service team).

**Exercise 3.3** — *"Compared with what?" diagnosis.* For each of the following, identify the missing reference:
- "Our website had 1.4M visitors last quarter."
- "65% of survey respondents support the policy."
- "The state with the most kidnappings is Borno."
- "Our quarterly revenue is up."

### Application

**Exercise 3.4** — *Audit a real dataset.* Take a dataset you work with. Walk through every column for type. Identify the analyst's question(s) it raises. Identify the reader's question(s) for at least two different audiences. Apply "compared with what?" to each. Submit a one-page audit document.

**Exercise 3.5** — *Identify the gap.* Take a chart specification (yours or someone else's) where the question and the data may not align. Walk through the data audit. Identify any gap. Choose one of the three honest moves (find better data, reframe, acknowledge). Document the choice.

**Exercise 3.6** — *The MBTA exercise.* Pick a dataset typical of your domain. Following the MBTA project model, write three reader-focused, specific questions the dataset could answer. For each, identify which functional category and which specific chart type the question implies. Compare to the chart you'd have built without doing the audit.

### Synthesis

**Exercise 3.7** — *The FiveThirtyEight pattern in your domain.* Find a chart in your professional domain that, on inspection, may answer a different question than its title implies (the FiveThirtyEight Nigeria pattern: "kidnappings" vs. "news stories about kidnappings"). Specify the gap. Propose the redesign.

**Exercise 3.8** — *Cairo audit on a dashboard.* Take a public dashboard. Audit five charts using the analyst-vs-reader distinction and the "compared with what?" check. Categorize each chart by which audit it fails (if any). Rate the dashboard's overall reader-orientation discipline.

### Challenge

**Exercise 3.9** — *Build the audit habit.* Following Concept 4's checklist, draft a one-page worksheet you will fill out before any new chart you produce: data types, analyst's question, reader's question, "compared with what?" answer, gap audit. Use the worksheet on the next three charts you build. Refine the worksheet from experience.

**Exercise 3.10** — *Multi-LLM audit.* Submit the same dataset and analyst's question to Claude, ChatGPT, and Gemini. Ask each to identify the reader's question(s) and apply "compared with what?". Compare the three outputs. Where do they agree? Where do they identify different reader questions? What does the variation reveal about which audit decisions are genuinely contestable?

---

## LLM Exercise — Chapter 3: Reading a Dataset

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A pre-chart audit document for a real dataset. Type identification, analyst-vs-reader question framing, "compared with what?" check, gap audit. The audit feeds directly into Chapter 2's selection framework and Chapter 4's Claude Code prompt.

**Tool:** Claude chat or Claude Code (for the audit document).

---

**The Prompt:**

```
I have a dataset of [DESCRIBE: rows, columns, types, source, what it
contains]. I want to build a chart from it. Walk me through the
pre-chart audit:

1. Identify each column's data type (categorical, ordinal, quantitative,
   temporal, geographic) and any sub-type details.

2. Identify the analyst's question(s) the data raises — what is
   interesting about it from a producer's perspective.

3. Identify the reader's question(s) — what would [DESCRIBE: my audience
   — e.g., a policymaker, a peer researcher, a general reader] need to
   know? Where do the analyst's question and the reader's question
   diverge?

4. Apply Cairo's "compared with what?" check. For the reader's primary
   question, name the comparison the chart must make explicit. If the
   comparison is missing, name it.

5. Identify which of the eight relationships from the FT Visual
   Vocabulary (comparison, change over time, distribution, relationship,
   part-to-whole, hierarchy, flow, spatial) the data supports. Flag
   any relationship the question implies but the data does not support.

6. Recommend whether to proceed (data supports the question), reframe
   (data supports a different question worth answering), find better
   data (data is genuinely insufficient), or acknowledge the gap (proceed
   with explicit annotation of what the chart does and does not show).

Save the audit as chapter-03-data-audit.md. The audit becomes the input
to Chapter 2's selection framework and Chapter 4's Claude Code prompt.
```

---

**What this produces:** A markdown audit document with six sections. Save as `chapter-03-data-audit.md`. Reference it for the chart-selection step (Chapter 2) and the Claude Code prompt (Chapter 4).

**How to adapt this prompt:**
- *For your own dataset:* Replace the description.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the audit framework as system context; the per-dataset audit becomes the user message.

**Connection to previous chapters:** Builds on Chapter 1 (channel ranking) at step 5 (relationship identification). Feeds Chapter 2 (chart selection) directly. The "compared with what?" check operationalizes Cairo's frame from Chapter 2.

**Preview of next chapter:** Chapter 4 covers the Claude Code workflow itself: how to turn the audit (Chapter 3) and the chart-type recommendation (Chapter 2) into a working D3 chart, how to evaluate and iterate on Claude Code output, and what the MBTA project's "iterate on working code" lesson means in practice.

---

## Visual suggestions

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

## Further reading

- **Cairo, Alberto. (2016).** *The Truthful Art.* Chapter 2 develops the analyst-vs-reader distinction; Chapter 3 develops "compared with what?".
- **Cairo, Alberto. (2019).** *How Charts Lie.* Chapter 1 walks the FiveThirtyEight Nigeria case in detail. The case is the canonical illustration of this chapter's failure modes.
- **Barry, Mike, and Brian Card. (2014).** "Visualizing MBTA Data." Available online. The project's process model — start with the question, iterate on working code — is the model for Chapter 15.
- **Tukey, John W. (1977).** *Exploratory Data Analysis.* Tukey's approach to reading a dataset before formal analysis is the methodological grandfather of this chapter's audit.
- **Wickham, Hadley. (2014).** "Tidy Data." *Journal of Statistical Software* 59(10). The structural audit Wickham describes (one row per observation, one column per variable) is the data-engineering complement to this chapter's reading audit.

---

## Tags

reading-data, data-types, categorical, ordinal, quantitative, temporal, geographic, analyst-question, reader-question, Cairo, compared-with-what, FT-visual-vocabulary, MBTA-project, FiveThirtyEight-Nigeria, gap-audit, pre-chart-audit, D3, Claude-Code
