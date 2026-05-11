# Chapter 4 — Working with Claude Code
*You Decide, the Machine Renders, You Review.*

## Three suggested titles

- Working with Claude Code: From Specification to Working D3
- The MBTA Process Model Applied to Chart Generation
- Iterate on Working Code, Not on Mockups

---

## Chapter overview

By the end of this chapter you will know how to take the outputs of Chapters 1–3 (channel decomposition, chart-type selection, data audit) and turn them into a working D3 chart through Claude Code, with disciplined iteration that reaches a publishable output without burning hours. You will know the prompt anatomy that makes Claude Code reliable, the evaluation criteria (Few/Evergreen/Emery) that determine whether the output is acceptable, and the iteration workflow modeled on the MBTA project's "nothing beat iterating on working code" lesson. You will see the full pipeline walked end to end on a humanitarian dataset.

---

## Learning objectives

1. **(Apply)** Write a Claude Code prompt that specifies chart type, data structure, channel-to-attribute mappings (from Chapter 1), and design constraints precisely enough to produce a usable D3 v7 output on the first attempt.
2. **(Analyze)** Evaluate a Claude Code–generated D3 visualization against the design specifications in the prompt, identifying gaps using the marks-and-channels vocabulary.
3. **(Create)** Iterate on a Claude Code output through at least two revision cycles, each targeting a specific design failure identified by applying Chapters 1–3 frameworks. Apply the MBTA project lesson: nothing beats iterating on working code.

---

## Opening case — two prompts for the same chart

You have a dataset: humanitarian funding allocation by sector for one country in fiscal year 2024. Five sectors, one quantitative value per sector. Communication goal: which sectors received the most funding?

You write a prompt for Claude Code:

> "Make a bar chart of humanitarian funding by sector."

Claude Code returns a working chart in 12 seconds. It is a column chart with five sectors on the x-axis and funding on the y-axis. The bars are roughly the right heights. The y-axis is auto-fit to the data range (starts around $40M, ends around $400M). The bars are the same color (default D3 steelblue). The x-axis labels are unrotated and crowded because three of the sector names are 12+ characters. There are no annotations.

The chart is technically correct. It is also unfit for the purpose. The truncated y-axis violates the proportional ink principle (Chapter 5). The unrotated long labels overlap. The single color does nothing — there's no redundant encoding of magnitude. The reader has to count tick marks to read approximate values.

You write a different prompt:

> "**Show what I have:**
> 5 rows. Each row has `sector` (string, 8–17 characters) and `funding_usd_millions` (number). Sample: Food Security, 380.2 / Shelter, 142.7 / Water and Sanitation, 98.4 / Health, 87.3 / Protection, 64.1.
>
> **Say what I want:**
> Horizontal bar chart in D3 v7. Single HTML file with inline CSS and inline D3 (loaded via CDN). Responsive to window resize.
>
> **Constrain it:**
> - Marks: rectangles, one per sector.
> - y-position: sector (categorical, sorted by `funding_usd_millions` descending for ranking readability).
> - x-position from zero baseline: `funding_usd_millions` (quantitative, range from 0 to ~$400M). Zero baseline non-negotiable.
> - Color luminance redundantly encoding `funding_usd_millions` (sequential pale-to-dark). Use d3.scaleSequential with d3.interpolateRgb from "#9B957F" to "#8B0000".
> - x-axis ticks at $0, $100M, $200M, $300M, $400M. Format as currency with M suffix.
> - Funding values labeled at the right end of each bar.
> - Subtitle: "FY2024 Humanitarian Funding by Sector (USD millions)".
> - Margins: top 60, right 80, bottom 40, left 160 (left margin accommodates sector labels).
> - Dark mode support via prefers-color-scheme media query.
>
> **Verify:**
> Restate the channel decomposition in your own words first. Then write D3 v7 code with comments showing which line implements which channel. List any decisions you made not specified above (font choice, exact tick label format)."

Claude Code returns a chart that matches the specification. Five horizontal bars, sorted by funding descending, on a zero baseline, with redundant color luminance, with currency labels, with rotated nothing because horizontal bars don't need rotation. The reader can rank the sectors at a glance and read approximate values without counting ticks.

The difference between the two prompts is not effort. The second is roughly 250 words; the first is 9. The difference is that the second prompt encodes the outputs of Chapters 1, 2, and 3:

- **Chapter 3 output (data audit):** column types and sample values are stated in "Show what I have."
- **Chapter 2 output (chart selection):** chart type and orientation are stated in "Say what I want," with the implicit Cairo justification (the message demands ranking; bar charts win for ranking).
- **Chapter 1 output (channel decomposition):** every channel-to-attribute mapping is named in "Constrain it."
- **Chapter 00 output (verification request):** the four-move structure ends with the "Verify" step.

This is the workflow this chapter teaches. Claude Code becomes reliable when it receives the outputs of the prior chapters. Without those outputs, Claude Code is guessing. With them, Claude Code is executing.

---

## Theoretical grounding — the MBTA project, Few's criteria, the Evergreen/Emery checklist

Three sources ground this chapter, each at the moment its specific contribution is needed.

**The MBTA project's iteration model (Barry & Card, 2014).** Mike Barry and Brian Card built a complete D3-based visualization of Boston's MBTA system as a master's thesis project. Their published reflection includes a sentence that has become canonical for the AI-assisted-coding era: *"Mockups and prototypes helped us formulate ideas, but nothing beat iterating on working code."* The lesson generalizes. When the implementation barrier is low (which it is now, thanks to Claude Code), the right workflow is to produce a working chart fast and then iterate on it, rather than to spend time on mockups that may or may not survive contact with the data. This chapter adopts the model: prompt → working chart → audit → follow-up prompt → improved chart → repeat. The first chart should land in 90 seconds. The iterations move you from working to publishable.

**Stephen Few's clarity-over-minimization criterion.** The book's stance on chartjunk (named in the Preface and developed in Chapter 5) governs the audit step. The criterion for any visual element in a Claude Code output is "does this support the message?" — not "is this strictly data ink?" Functional color encoding stays. Light gridlines that aid value reading stay. Redundant labels that aid scanning stay. Decoration that does not serve the message goes. Few's frame is what Chapter 5 uses to defend the bar chart's color luminance redundancy; it is what Chapter 14 develops as the full design audit; it is what this chapter applies pragmatically to Claude Code output evaluation.

**The Evergreen/Emery 22-point design checklist.** Stephanie Evergreen and Ann Emery's checklist (`pantry/EvergreenDataVizChecklist.txt`) operationalizes Few/Tufte/Cairo into 22 yes-or-no items grouped into five categories: text, arrangement, color, lines, overall. The checklist is the audit instrument. Chapter 14 walks the full version; this chapter introduces the chart-family-applicable subset for use during Claude Code iteration. The five-category structure is the muscle memory the rest of the book builds.

---

## Concept 1 — The Claude Code + D3 pipeline

Before any prompt: the environment.

### Where D3 runs

D3 runs in any environment that can render an HTML/SVG canvas. The four common targets:

**Standalone HTML file.** A single self-contained HTML file with inline CSS and inline D3 loaded via CDN. The simplest target. Open in any browser. Useful for one-off charts, course exercises, embeds. The pantry's chart examples are all this format.

**Observable notebook.** Observable (observablehq.com) is a JavaScript notebook environment optimized for D3 work. Cells re-run on data change; the chart redraws automatically. Useful for exploratory work and for charts that need to be edited collaboratively. Many of the canonical D3 examples are Observable notebooks.

**ES module in a bundler.** D3 imported as `import * as d3 from "d3"` in a Webpack/Vite/Rollup project. Useful when the chart is part of a larger application. The chart code is JavaScript; the rendering happens at runtime.

**React (or Vue, Svelte) component.** D3 inside a component framework. Useful for charts that are part of a React app. The pattern: D3 builds the SVG; React manages the component lifecycle. Several conventions exist for the boundary; the most common is "React renders the SVG, D3 computes the layout."

For most LLM Exercises in this book, the standalone HTML file is the right target. It runs anywhere. It can be opened in a browser without setup. It can be saved as a deliverable. Specify it in the "Say what I want" move of every prompt.

### What Claude Code can see

Claude Code can read files in your project directory. The relevant files for D3 work:

- **The data file.** CSV, JSON, or inlined data. If the data is in a file, name it in the prompt: "data is in `data.csv`."
- **Reference charts in the pantry.** The pantry's HAI chart examples. Naming a pantry file in the prompt ("see `pantry/visualization/bar-chart.html` for the design pattern") gives Claude Code a concrete reference.
- **Your `CLAUDE.md`.** The coding constitution from Chapter 00. Reference it at the start of every session: "follow the conventions in `CLAUDE.md`."
- **Your `DESIGN.md`.** The visual constitution from Chapter 00. Reference it only when the session involves visual decisions — palette choice, dark-mode behavior, typography, responsive breakpoints, component rules. Loading it on routine code-only sessions wastes instructions on rules that don't apply.
- **Prior chart files from your project.** If you've built related charts, naming them maintains visual consistency.

Claude Code cannot see what is not in the project directory. If the data lives in a remote API, you need to specify the API call (or paste the data). If the design pattern lives in your head, you need to specify it explicitly.

### What Claude Code does well in this pipeline

- **Writes valid D3 v7 syntax** with high reliability.
- **Computes layouts** for non-trivial chart types (Sankey, treemap, force-directed) via D3's layout primitives.
- **Generates accessibility metadata** (ARIA labels, focus states, screen-reader-friendly summaries).
- **Handles responsive resize** via window event listeners and re-rendering.
- **Implements design constraints** when they are named (zero baseline, sort order, label rotation).
- **Generates color scales** (sequential, categorical, diverging) using D3's built-in interpolators.

### What Claude Code does badly

- **Chart selection** when the prompt is vague. (Chapter 2 is the fix.)
- **Channel decomposition** when the prompt doesn't specify it. (Chapter 1 is the fix.)
- **Domain-specific defaults** (e.g., financial chart conventions, scientific publication norms) without explicit instruction.
- **Chart aesthetics** that match a specific brand or publication style without reference examples.
- **Performance optimization** beyond the basics. For very large datasets, hand-tuning is sometimes required.

The labor separation: Claude Code handles syntax and computation; you handle decisions and aesthetic judgment.

---

## Concept 2 — Prompt anatomy applied to D3

The four-move prompt structure (Chapter 00) applies directly. For D3 work specifically, each move has a chart-specific shape.

### Move 1: Show what you have

For D3, "what you have" includes:

**The dataset.** Number of rows, column names, column types, a sample of 3–5 rows. If the data is large, an aggregated or filtered version. If the data is in a file Claude Code can read, name the file path.

**The reference design (optional but powerful).** "See `pantry/visualization/bar-chart.html` for the visual pattern" gives Claude Code a concrete reference. The output will follow the reference's design conventions (typography, color palette, margins) where the prompt doesn't override.

**The `CLAUDE.md` (always for code work) and `DESIGN.md` (when visual decisions are in scope).** "Follow the conventions in `CLAUDE.md`" delegates coding standards to the persistent file. "Apply `DESIGN.md` for palette, typography, and dark-mode behavior" delegates the visual specifications. The split matters because of the instruction budget Chapter 00 names — loading `DESIGN.md` on routine code-only sessions wastes ~50 instruction slots on rules that don't apply to the task at hand.

### Move 2: Say what you want

For D3, "what you want" includes:

**Chart type.** Named explicitly — "horizontal bar chart," "line chart with multiple series," "Sankey diagram." Don't say "comparison chart"; the genre is too broad. The output of Chapter 2's selection framework belongs here.

**Output format.** "Single HTML file with inline CSS and inline D3 (loaded via CDN)" for standalone work. Or "Observable notebook cell," "ES module," "React functional component," depending on target.

**D3 version.** "D3 v7" by default. Specify if working in a project pinned to an older version.

**Responsive behavior.** "Responsive to window resize" or "fixed dimensions: 800×500" depending on deployment context.

### Move 3: Constrain it

This is the longest move. The constraints come from Chapter 1 (channels), Chapter 2 (chart-family-specific design rules), Chapter 3 (data structure decisions), the active `CLAUDE.md` (project-wide coding standards), and — when visual decisions are in scope — the active `DESIGN.md` (project-wide visual standards).

A typical "Constrain it" block for a single chart includes:

- **Marks.** "Rectangles, one per category." "Path with circular markers at data points."
- **Channel-to-attribute mappings.** "y-position encodes [attribute] (data type, with constraint)." Repeat for each channel in use.
- **Sort order.** "Categories sorted by [attribute] descending." If the order matters and is non-default, name it.
- **Axis configuration.** Tick locations, label format, label rotation.
- **Color decision.** Sequential / categorical / diverging; palette endpoints; the function used (`d3.scaleSequential`, `d3.scaleOrdinal`, etc.).
- **Annotations.** Subtitle, value labels, callouts.
- **Layout.** Margins, padding, corner radius, line widths.
- **Accessibility.** ARIA labels, focus states, keyboard interaction (where applicable).
- **Dark-mode behavior.** prefers-color-scheme handling, color inversions.

The "Constrain it" move is where the work is. A two-line "Constrain it" produces a chart that runs on Claude Code's defaults; a 20-line "Constrain it" produces the chart you specified.

### Move 4: Ask for verification

For D3, the verification request has a standard form:

> "Before writing the code, restate the channel decomposition in your own words to confirm. Then write the D3 v7 code with comments showing which line implements which channel. After the code, list any decisions you made that are not specified above so I can confirm or override them."

The restatement catches misinterpretation early (before code is written). The line-by-line comments make the channel decomposition auditable in the code itself. The unspecified-decisions list flags where Claude Code chose for you — useful for catching defaults that don't match your intent.

> ### ↳ Dig Deeper — Build your prompt template
>
> **Prompt:**
>
> > Help me draft a reusable prompt template for D3 chart generation, following the four-move structure adapted to my workflow. Include placeholders for the variable parts (dataset description, chart type, channel mappings) and concrete examples for the parts I want to standardize (output format, D3 version, dark-mode handling, accessibility defaults). The template should fit on one page and be the prompt I copy and adapt for every chart in this book.
>
> **What to do with the output:** Save as `claude-code-prompt-template.md`. Use it for every LLM Exercise. Refine it as you discover what your work consistently needs.

---

## Concept 3 — The MBTA iteration model

"Mockups and prototypes helped us formulate ideas, but nothing beat iterating on working code." — Mike Barry and Brian Card, MBTA Visualization, 2014.

The MBTA team's process model has four practical implications for Claude Code work.

### Get a working chart fast

The first prompt should produce a chart that runs. Not a perfect chart. A chart that opens in a browser and shows the data. The 250-word prompt from this chapter's opening case is the model: enough detail to land near the target on the first attempt, not enough to perfectly nail it.

The first chart almost always has issues. That's expected. The next step is iteration on working code, not on the prompt-in-isolation.

### Iterate on the artifact, not the spec

Once the chart exists, the iteration target is the chart, not the prompt. You read the chart against the audit checklist (Concept 4), identify what's wrong, and write a follow-up prompt that names the specific failure.

A good follow-up prompt is small:

> "The y-axis is starting at $40M instead of $0. Reset to a zero baseline. The Cleveland-McGill argument and proportional ink principle apply: bar charts use length-from-axis as the magnitude channel, and a non-zero baseline distorts the channel. Regenerate."

A bad follow-up prompt re-specifies everything:

> "Change the chart so it has a zero baseline, sorted bars descending, color luminance, currency labels..."

The bad version is restating the original prompt rather than fixing the specific failure. Claude Code's response will be a wholesale regeneration that may introduce new failures. The good version is targeted; the response should be a small change.

### One concern per iteration

When multiple things are wrong, fix them one at a time. Two simultaneous changes in a follow-up prompt introduce ambiguity about which fix produced which effect. The iteration becomes harder to debug.

The order of iterations matters. Fix structural issues (zero baseline, chart type, channel mapping) before stylistic issues (color palette, font size, label positioning). A chart with the wrong channel mapping cannot be fixed by changing colors.

### Working code is the truth

The most important MBTA lesson: a working chart shows you things that mockups don't. The data clusters in unexpected ways. The labels overlap at small browser sizes. The color you chose looks fine in light mode and bad in dark mode. None of these are visible in a sketch or a written specification. They are visible in the rendered chart.

This is why Chapter 00's verification stack is non-negotiable: open the chart in a browser, resize it, switch to dark mode, run a color-blind simulator. The artifact is the truth. The prompt was the hypothesis.

---

## Concept 4 — Evaluating Claude Code output (the Evergreen/Emery subset)

Stephanie Evergreen and Ann Emery's data visualization checklist has 22 items grouped into five categories. The full checklist is Chapter 14's territory; the per-chart subset for Claude Code iteration covers the items that are most likely to fail and are easy to fix.

### The five-category structure

**Text.** Title clear and informative. Axis labels and units. Annotations support understanding. Body text legible at deployment size.

**Arrangement.** Sort order meaningful. Layout uses space efficiently. Related elements grouped (Gestalt proximity). Visual flow matches reading order.

**Color.** Used purposefully (no decoration). Sequential / categorical / diverging matched to data type. Color-blind safe (test with simulator). Sufficient contrast with background.

**Lines.** Gridlines support reading without distracting. Axis lines visible but unobtrusive. Stroke widths consistent. No 3D effects or perspective.

**Overall.** No chartjunk that doesn't support the message. Proportional ink (zero baselines where required). Data shown without distortion. Accessibility metadata present.

### Per-chart audit during iteration

For every Claude Code output, walk the five categories. For each, ask: did the output get this right? If not, what's the specific failure and what's the follow-up prompt?

The audit takes 90 seconds for a static chart. It is the discipline that distinguishes "I got Claude Code to produce a chart" from "I produced a publishable chart with Claude Code's help."

### Common failures and follow-up prompts

A few patterns recur:

**Failure: Y-axis auto-fit instead of zero baseline.**
- Follow-up: "Reset y-axis to start at 0. The proportional ink rule (Tufte, grounded in Stevens' power law on area perception) requires this for bar charts. Regenerate the y-scale and the gridline positions."

**Failure: Wrong channel for the data type.**
- Follow-up: "The chart uses color hue to encode score (a quantitative variable). Hue is an identity channel, not a magnitude channel. Replace with sequential color luminance (pale-to-dark) using d3.scaleSequential. Position-y already encodes score; this is a redundant encoding."

**Failure: Sort order missing or wrong.**
- Follow-up: "Sort the categories by score descending so the highest-scoring category appears at the top of the chart. The categorical x-axis has no inherent order; the sort gives the reader a ranking the data does not impose."

**Failure: Labels rotated when they don't need to be.**
- Follow-up: "The y-axis labels are rotated -30°. With horizontal bars, labels go on the left and don't need rotation. Set rotation to 0 and right-align."

**Failure: Color palette doesn't match brand or reference.**
- Follow-up: "Use the HAI palette from `pantry/visualization/bar-chart.html`: foreground `#0D0D0D` (light mode) / `#FFFFFF` (dark mode); muted `#9B957F`; accent `#8B0000`. Replace the current palette."

**Failure: No accessibility metadata.**
- Follow-up: "Add ARIA labels: the SVG should have `role='img'` and `aria-label` describing the chart. Each bar should have a `<title>` element with the category name and value for screen-reader access."

The follow-ups are short, specific, and grounded in the chapter's vocabulary. The pattern repeats for every chart in Part II.

> ### ↳ Dig Deeper — Build your iteration log
>
> **Prompt:**
>
> > For the next three charts I build with Claude Code, help me set up an iteration log: a markdown file per chart that captures the initial prompt, the first output (or a description of it), each iteration's follow-up prompt with the failure it targeted, and the final accepted output. The log makes the workflow auditable and surfaces patterns in what fails consistently.
>
> **What to do with the output:** Save the iteration log template. Use it for every LLM Exercise from this point forward. After ten charts, you will know what your typical failures are and which prompt patterns prevent them.

---

## Concept 5 — When Claude Code is not the right tool

Claude Code is the right tool for most chart work in this book. Three contexts where it isn't:

**Highly performant data-driven charts at scale.** Tens of thousands of points, real-time updates, server-side rendering for Twitter-card OG images. Claude Code can produce the chart, but the performance optimization (canvas instead of SVG, virtual scrolling, deck.gl for 3D scenes) often needs hand-tuning. The chart specification still uses the framework from this book; the implementation may need a developer.

**Charts that depend on a custom interaction language.** A research dashboard with a specific brushing-and-linking pattern, a custom hover tooltip, a tightly-coupled visualization-and-data-table combination. Claude Code can produce the components; integrating them into the custom interaction usually needs code review.

**Domain-specific scientific visualizations.** Phylogenetic trees with specific layout algorithms, molecular structure visualization, neuroimaging overlays. The standard D3 layouts don't cover these; specialized libraries or hand-coded algorithms do. Claude Code can produce a starting point; domain expertise is needed to finish.

For these cases, the chapter's framework still applies — channel decomposition, chart selection, audit, iteration. The iteration may include hand-coded sections that Claude Code didn't produce. The Brutalist labor separation is unchanged: the human owns the design judgment; the tooling (whatever it is) executes.

---

## Mid-chapter checkpoint

Pick a chart specification from your work — even a hypothetical one. Walk it through the four-move structure. Write the prompt. Estimate how long the first output will take and how many iterations you expect.

If you cannot write the prompt without going back to Chapters 1, 2, or 3, the prompt is missing prerequisites. Identify which.

---

## Extended worked example — the full pipeline on the humanitarian funding dataset

Walk the complete pipeline end to end. Same dataset as the opening case: humanitarian funding by sector for one country in fiscal year 2024.

### Step 1 — Apply Chapter 3 (read the dataset)

Five rows. Sector (categorical, 5 values, no inherent order). Funding (quantitative, ratio scale, USD millions). One observation per category.

Analyst's question: "How are funds distributed across sectors?"

Reader's question (audience: a humanitarian-program officer): "Which sectors are receiving the most funding and which the least?"

The two questions overlap; the reader's version is more specific (it's about the ranking, not just the distribution). The chart must answer the reader's version.

"Compared with what?" The categories are compared with each other. The within-period comparison is the point.

Relationship type: comparison.

### Step 2 — Apply Chapter 2 (select the chart)

Cairo's four steps:

1. Key message: "Food security received 56% of total funding, more than the next four sectors combined."
2. Data structure: 5 categorical + 1 quantitative.
3. Functional category: comparison.
4. Specific form: bar chart, with sort by funding descending. Long sector labels suggest horizontal orientation.

### Step 3 — Apply Chapter 1 (decompose the channels)

- Marks: rectangles, one per sector.
- y-position (categorical axis): sector. Sorted by funding descending.
- x-position from zero baseline (quantitative axis): funding. Range 0 to ~$400M.
- Color luminance: funding (redundant encoding, sequential pale-to-dark).
- Annotations: funding value at the right end of each bar; subtitle naming the period and units.

### Step 4 — Write the four-move prompt (this chapter)

```
**Show what I have:**
5 rows. Each row has `sector` (string, 8-17 characters) and
`funding_usd_millions` (number). Sample:
  Food Security, 380.2
  Shelter, 142.7
  Water and Sanitation, 98.4
  Health, 87.3
  Protection, 64.1

See pantry/visualization/bar-chart.html for the visual pattern (HAI
palette, dark-mode support, responsive resize). Follow CLAUDE.md
for coding conventions; apply DESIGN.md for palette, typography,
and dark-mode behavior. Follow these for any decision not specified
below.

**Say what I want:**
Horizontal bar chart in D3 v7. Single self-contained HTML file with
inline CSS and inline D3 (loaded via CDN). Responsive to window
resize.

**Constrain it:**
- Marks: rectangles, one per sector.
- y-position: sector (categorical, sorted by `funding_usd_millions`
  descending).
- x-position from zero baseline: `funding_usd_millions` (quantitative,
  range 0 to ~$400M). Zero baseline non-negotiable.
- Color luminance redundantly encoding `funding_usd_millions`
  (sequential pale-to-dark). Use d3.scaleSequential with
  d3.interpolateRgb from "#9B957F" to "#8B0000". Color domain: 0 to 400.
- x-axis ticks at $0, $100M, $200M, $300M, $400M. Format as currency.
- Funding values labeled at the right end of each bar.
- Subtitle: "FY2024 Humanitarian Funding by Sector (USD millions)".
- Margins: top 60, right 80, bottom 40, left 160 (left margin
  accommodates sector labels).
- Dark mode support via prefers-color-scheme media query.
- ARIA: SVG role="img", aria-label describing the chart; each bar has
  a <title> element for screen readers.

**Verify:**
Restate the channel decomposition in your own words first. Then write
D3 v7 code with comments showing which line implements which channel.
After the code, list any decisions you made that are not specified
above so I can confirm or override them.
```

### Step 5 — Read Claude Code's first output

Claude Code returns:

1. A specification restatement (good — confirms understanding).
2. An HTML file with inline D3 (the chart).
3. A list of decisions: "I chose Inter as the font (consistent with the pantry reference). I used 12px for axis labels and 14px for the subtitle. I rounded bar corner radius to 3px to match the pantry."

Open the HTML in a browser.

### Step 6 — Audit (Evergreen/Emery subset)

| Item | Pass/Fail | Notes |
|---|---|---|
| Title clear and informative | ✓ | Subtitle names period and units |
| Axes labeled, units clear | ✓ | x-axis has $ M format |
| Sort order meaningful | ✓ | Descending by funding |
| Data shown without distortion | ✓ | Zero baseline; bar lengths match values |
| Color used purposefully | ✓ | Luminance redundantly encodes funding |
| Color-blind safe | ✓ (sequential luminance) | Verified with Sim Daltonism |
| No chartjunk | ✓ | No decoration; no 3D |
| Accessibility metadata | ✓ | ARIA labels and titles present |
| Responsive | ✓ | Resize works in browser |
| Dark mode | ✓ | Tested |

All items pass. The chart is publishable as-is.

### Step 7 — When iteration is needed

Suppose one item failed. Suppose the color domain Claude Code used was `d3.extent(data)` (auto-fit to data), so the lightest bar at $64M is mapped to the palest color and the darkest at $380M to the darkest — but the relative-magnitude differences feel compressed.

Follow-up prompt:

> "The color luminance scale is auto-fit to the data range, which compresses the magnitude differences visually. Reset the color domain to [0, 400] (the full range from zero to the maximum). The luminance redundantly encodes the absolute magnitude, not the within-data range. Regenerate the d3.scaleSequential with this domain."

Claude Code returns the corrected version. Audit. Pass.

### What this teaches

The full pipeline — Chapter 3 (data audit) → Chapter 2 (selection) → Chapter 1 (channels) → Chapter 4 (prompt + iterate) → ready output — is the model for every chart in Part II. Each chapter's contribution is a section of the audit/specification that funnels into the prompt. Without any one of them, the prompt is incomplete and the iteration is longer.

This is the load-bearing claim of Part I: do the work upstream, and the chart almost mechanically follows. Skip the work upstream, and you spend the time downstream in iteration.

---

## Chapter summary

You can now do five things you could not do before this chapter.

You can write a Claude Code prompt for a D3 chart that integrates the outputs of Chapters 1, 2, and 3 — channel decomposition, chart-type selection, data audit — into a single specification that lands near the target on the first attempt.

You can apply the MBTA iteration model: get a working chart fast, iterate on the artifact (not the spec), one concern per iteration, and trust the rendered chart over the imagined one. The first chart in 90 seconds; the iterations move you to publishable.

You can audit any Claude Code output using the Evergreen/Emery five-category subset (text, arrangement, color, lines, overall) and write follow-up prompts that target specific failures with the chapter's vocabulary.

You can recognize when Claude Code is not the right tool — high-performance scenarios, custom interaction languages, domain-specific scientific visualizations — and adjust the workflow without abandoning the chapter's framework.

You can sequence the upstream chapters' contributions into a reproducible pipeline: every chart you build for the rest of the book follows the same arc, with chart-family-specific design rules supplied by Chapters 5–13.

The thing to watch for, going forward, is the temptation to skip the upstream work and produce the chart from a vague prompt. The opening case of this chapter is the lesson in miniature: 9 words of prompt produce 12 seconds of work and a chart that is wrong in five ways; 250 words of prompt produce 12 seconds of work and a chart that is right. The work scales with specificity. Specificity scales with upstream discipline.

---

## Key terms

- **The MBTA iteration model.** Get a working chart fast; iterate on the artifact, not the spec; one concern per iteration; trust the rendered chart over the imagined one.
- **Evergreen/Emery 22-point checklist.** The audit instrument used during iteration. Five categories: text, arrangement, color, lines, overall. The full checklist is Chapter 14's territory; the per-chart subset is this chapter's tool.
- **Few's clarity-over-minimization.** The criterion for any visual element: does this support the message? — not "is this strictly data ink?"
- **Working chart vs. publishable chart.** A working chart runs. A publishable chart has been audited and iterated to remove the failures the audit caught.
- **Targeted follow-up prompt.** A short prompt that names a specific failure and the perceptual or design rule it violates. Distinguished from re-specifying the original prompt.

---

## Discussion questions

1. The MBTA project's "nothing beat iterating on working code" lesson predates Claude Code by a decade. Why does it apply more strongly now than it did then?
2. The four-move prompt structure is roughly 250 words for a single chart. Is this overhead worth paying for every chart? What types of charts justify shorter prompts; what types justify longer?
3. Claude Code's failure modes (Chapter 00 named three: API hallucination, chart-type mismatch, channel mismatch) are often diagnosable from the output without running it. Which can be caught by reading the prompt and the response together; which require running the chart?
4. The Evergreen/Emery five-category subset is the per-chart audit. What item is most often missing from charts you produce? What does the consistent gap suggest about your prompt patterns?
5. *Cross-chapter synthesis.* Chapter 14 walks the full Evergreen/Emery checklist and the Tufte/Few/Cairo synthesis. Frame the relationship between this chapter's per-chart audit and Chapter 14's project-wide audit: where does each operate, and when does the per-chart audit defer to the project-wide one?

---

## Exercises

### Warm-up

**Exercise 4.1** — *Write a four-move prompt for a familiar chart.* Take a chart you have produced before (a bar chart, a line chart, a scatterplot from your professional work). Write the four-move prompt that would produce it from scratch with Claude Code. Submit the prompt without running it. Estimate how close to your original chart Claude Code's output would be.

**Exercise 4.2** — *Targeted follow-up.* Claude Code produces a chart with three failures: (1) y-axis auto-fits to data range instead of zero, (2) color hue encodes a quantitative variable, (3) sort order is alphabetical instead of by value. Write three separate follow-up prompts, one per failure. Order them in the right sequence (structural before stylistic).

**Exercise 4.3** — *Audit subset.* Apply the Evergreen/Emery five-category subset (text, arrangement, color, lines, overall) to a chart in the pantry. Report which categories pass, which fail, and what follow-up would fix the failures.

### Application

**Exercise 4.4** — *End-to-end pipeline.* Take a real dataset you have. Walk the full pipeline: Chapter 3 audit, Chapter 2 selection, Chapter 1 decomposition, Chapter 4 prompt. Run the prompt through Claude Code. Audit the output. Iterate to publishable. Submit: the audit document, the prompt, the first output, the iteration log, the final chart.

**Exercise 4.5** — *MBTA-model practice.* Build the same chart twice: once with a vague prompt and as much iteration as needed to land on a publishable output, once with a four-move prompt. Compare the time, the number of iterations, and the final chart. The exercise teaches you what specificity buys in concrete terms.

**Exercise 4.6** — *CLAUDE.md update from experience.* After building 5 charts in your domain, review your prompt history. What constraints did you specify in every prompt? Promote them to your `CLAUDE.md`. What constraints did you specify but were ignored or misinterpreted? Note them as potential clarifications for the next round.

### Synthesis

**Exercise 4.7** — *Iteration log analysis.* Build 10 charts using the four-move structure and keep an iteration log per chart. After 10 charts, analyze: which failures recur? Which categories of the Evergreen/Emery checklist fail most often? What patterns can be moved upstream into the initial prompt or the `CLAUDE.md`?

**Exercise 4.8** — *Multi-LLM iteration comparison.* Take the same flawed Claude Code output. Submit a follow-up prompt to Claude Code, ChatGPT, and Gemini. Compare how each handles the iteration. Where do they converge? Where does each LLM produce a different correction?

### Challenge

**Exercise 4.9** — *Edge case: a high-performance chart.* Take a dataset with 50,000+ points. Walk the four-move pipeline. When you hit a performance issue (Claude Code's straightforward implementation chokes), write the follow-up prompt that asks for the optimization (canvas instead of SVG, virtual scrolling, deck.gl). Document what Claude Code did well and where the human (you) had to intervene.

**Exercise 4.10** — *Build your team's CLAUDE.md.* If you work with a team, draft a shared `CLAUDE.md` for the team's D3 work. Include: the team's color palette with hex values, the team's typography conventions, the team's accessibility requirements, the team's preferred D3 version, the team's responsive design conventions. Test it on three real charts and refine.

---

## LLM Exercise — Chapter 4: The Full Pipeline

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A complete D3 chart from raw dataset to publishable output, walked through the full pipeline (Chapters 1–4) with iteration logs documenting the failures and follow-ups. The deliverable demonstrates the workflow that Chapters 5–13 will apply to specific chart families.

**Tool:** Claude Code (primary) + Claude chat or a Claude Project (for the audit step if working in a Project).

---

**The Prompt (full pipeline):**

```
I am working through Chapter 4 of Brutalist d3 x Claude. I want
to build a complete chart from a dataset I have, demonstrating the full
pipeline. Help me through the steps:

1. Read the dataset I'm providing: [DESCRIBE: rows, columns, types,
   source]. The communication goal is [DESCRIBE: what the reader needs
   to know in 5 seconds; the audience].

2. Apply Chapter 3's audit: data types, analyst's vs. reader's question,
   "compared with what?", relationship the data supports.

3. Apply Chapter 2's selection: Cairo's four-step framework. Recommend
   a chart type with justification.

4. Apply Chapter 1's channel decomposition: marks, channel-to-attribute
   mappings, design constraints.

5. Write the four-move Claude Code prompt that integrates all the above.
   Submit the prompt to Claude Code. Read the first output.

6. Apply the Evergreen/Emery five-category subset (text, arrangement,
   color, lines, overall). Identify any failures.

7. For each failure, write a targeted follow-up prompt naming the
   specific failure and the perceptual or design rule it violates.

8. Iterate to a publishable output (typically 1-3 iterations after the
   first). Document each iteration in an iteration log.

Save the audit, the channel decomposition, the prompt, the iteration
log, and the final chart as a `chapter-04-full-pipeline/` directory
with the appropriate files. The directory becomes a model for every
chart you build in Chapters 5-13.
```

---

**What this produces:** A directory containing the full audit-to-output trail for one chart. Files: `01-data-audit.md`, `02-selection-audit.md`, `03-channel-decomposition.md`, `04-prompt.txt`, `05-iteration-log.md`, `06-final-chart.html`. The directory is your reference template.

**How to adapt this prompt:**
- *For your own dataset:* Replace the dataset description and communication goal.
- *For ChatGPT / Gemini:* Works as-is. Both will produce the audit; the chart still gets built in Claude Code.
- *For a Claude Project:* Save the audit framework as system context; the per-chart pipeline becomes the user message.

**Connection to previous chapters:** This is the chapter that integrates everything from Part I. Chapters 1, 2, 3 produce the inputs; Chapter 4 produces the output. Future chapters' LLM Exercises will follow the same pattern with chart-family-specific design rules added.

**Preview of next chapter:** Chapter 5 begins Part II — the chart taxonomy. Each Part II chapter adds chart-family-specific design rules to the framework you have just built. Chapter 5 (comparison charts) is the first; the same pipeline applies, with comparison-specific design rules layered on.

---

## Visual suggestions

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

## Further reading

- **Barry, Mike, and Brian Card. (2014).** "Visualizing MBTA Data." Available online. The full project report; read the section on iteration philosophy.
- **Evergreen, Stephanie. (2019).** *Effective Data Visualization: The Right Chart for the Right Data.* SAGE Publications. Includes the Evergreen/Emery checklist with extensive examples.
- **Few, Stephen.** *Now You See It: Simple Visualization Techniques for Quantitative Analysis.* Few's most accessible book; the chapters on iteration and audit are directly relevant.
- **The book's pantry** — particularly `pantry/EvergreenDataVizChecklist.txt` for the full checklist and `pantry/00-claude-prompting-tips.md` for the prompt-writing discipline that this chapter applies to D3 specifically.

---

## Tags

Claude-Code, D3, four-move-prompt, MBTA-iteration-model, Evergreen-Emery-checklist, Few-clarity-criterion, working-chart, publishable-chart, targeted-follow-up, audit-checklist, full-pipeline, channel-decomposition
