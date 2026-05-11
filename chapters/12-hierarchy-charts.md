# Chapter 10 — Hierarchy Charts
*Containment as the Encoding.*

## Three suggested titles

- Hierarchy Charts: Treemap, Sunburst, Circle Packing — When Each Wins
- Showing Proportion vs. Depth vs. Exact Structure
- The Squarification Algorithm and What It Optimizes

---

## Chapter overview

By the end of this chapter you will be able to build the family of hierarchy charts — treemap, sunburst, circle packing, tree diagram — and you will know which form best reveals which feature of a hierarchical dataset (proportion vs. depth vs. exact structure). You will know why treemaps fail past three levels of depth, why circle packing handles irregular branching better than treemaps, and how to specify a hierarchy chart for Claude Code with the right layout algorithm and depth limit.

---

## Learning objectives

1. **(Apply)** Build a treemap and sunburst from the same hierarchical dataset; identify what each form reveals that the other hides (proportion vs. depth).
2. **(Analyze)** Diagnose a sunburst with more than five hierarchy levels, explain why outer rings compress into illegible slivers, and specify the redesign.
3. **(Evaluate)** Justify the choice between treemap and circle packing for a dataset with irregular hierarchy depth, citing the specific perceptual mechanism each exploits.

---

## Opening case — the HAI circle packing chart

Open `pantry/visualization/treemap.html` and `pantry/visualization/illustration-diagram.html` (or whichever pantry files show the HAI circle packing example). Both visualize humanitarian-AI-application categories with sub-categories. The treemap shows nested rectangles. The circle packing shows nested circles.

The treemap looks orderly: each top-level category is a rectangle, subdivided into smaller rectangles for its sub-categories. The squarification algorithm (Bruls, Huizing, van Wijk 1999) arranges them to keep aspect ratios close to square, maximizing area-comparison accuracy. Where the hierarchy has uniform depth (every branch goes 3 levels deep), the treemap reads cleanly.

The circle packing chart looks organic: each top-level category is a circle, with sub-categories as nested circles inside. Where one branch has more sub-categories than another, the circles arrange themselves around the available space. Where the hierarchy has irregular depth (some branches go 3 levels, others 2), circle packing handles it gracefully — the circles simply nest deeper where they need to.

The choice between forms is not stylistic. It is a channel-and-structure decision. Treemaps are better at proportion comparison (rectangular area is more accurately judged than circular area). Circle packing is better at irregular hierarchies (it doesn't try to fit unequal branches into a fixed grid). Sunbursts are better at depth (concentric rings make level structure visible).

This chapter is about that choice — and about the specific design failures (depth limits, label crowding, area encoding errors) that hierarchy charts produce when their forms are mismatched to the data.

---

## Theoretical grounding — Bertin on area, Gestalt figure-ground, Friendly on Shneiderman's treemap

Three sources ground this chapter.

**Bertin on area encoding.** Hierarchy charts use *area* as the primary magnitude channel: the area of each region (rectangle in a treemap, circle in circle packing, ring segment in a sunburst) encodes the value at that node. Stevens' power law (Chapter 1) on area perception applies — perception is sublinear, exponent ≈ 0.7. The eye underestimates area. Ratios between large and small regions are read with some compression, but the relative ordering is preserved.

**Gestalt figure-ground.** Sunburst diagrams in particular create strong figure-ground relationships: the center is the figure, the outer rings are background structure. The Gestalt mechanism makes hierarchy depth visible — the inner rings (closer to the center) read as parents, the outer rings (further out) read as children. The same mechanism produces the failure mode: when too many rings are stacked, the outer rings compress into unreadable slivers because each ring shares the available radial space with all the levels below it.

**Friendly on Ben Shneiderman's treemap (1991).** Shneiderman invented the treemap to visualize disk usage with nested directories. The original problem: the file system has a hierarchy (files in folders in folders), and Shneiderman wanted a visualization that fit on a single screen. The treemap was the answer: nested rectangles where area encodes file size. Knowing the original problem clarifies when treemaps work — they work for hierarchies where the *area* is the primary question and the depth is bounded. They work less well for hierarchies where exact structure matters (a phylogenetic tree) or where depth varies widely.

---

## Concept 1 — Treemaps: the squarified hierarchy

A treemap divides a rectangular space into smaller rectangles, each representing a node in the hierarchy. The area of each rectangle encodes the node's value. Children of a node are nested inside their parent's rectangle.

### When treemaps work

- Hierarchies with relatively uniform depth (most branches go 2–3 levels).
- The reader needs to compare *proportions* (area of one node vs. another).
- The dataset is large enough that a treemap is more space-efficient than a tree diagram.

### Design decisions

**Layout algorithm.** D3's `d3-hierarchy` library offers several treemap layout algorithms:

- `treemapBinary` — splits each rectangle in half repeatedly. Produces long thin rectangles for skewed data.
- `treemapDice` / `treemapSlice` — always splits horizontally (slice) or vertically (dice).
- `treemapSquarify` — minimizes aspect ratio variance. Most readable for area comparison. Default in most contexts.

For Claude Code work: specify `treemapSquarify` explicitly. The other algorithms have specific use cases (slice for time-ordered hierarchies, etc.) but squarify is the right default.

**Depth limit.** Three levels is the practical limit. Past three, inner rectangles become too small to read or label. For deeper hierarchies, consider zoomable interaction (where the reader clicks a rectangle to drill into its children) or switch to a different form (sunburst, circle packing).

**Labels.** Top-level rectangles get visible labels. Second-level rectangles get labels if they're large enough. Third-level rectangles often need hover tooltips rather than visible labels. Layout-aware labeling (only label rectangles above a minimum size threshold) is the right default.

**Color.** Two common encoding choices:

- **Top-level category as color hue.** Each top-level rectangle and its descendants share a color. The reader sees the hierarchy structure immediately.
- **Quantitative variable as color luminance.** A second variable (beyond size) encodes via color. The reader sees both the size structure and the second variable.

Don't try to encode three variables (size + hue + luminance). The cognitive load exceeds what most readers can decode at a glance.

> ### ↳ Dig Deeper — Treemap depth strategies
>
> **Prompt:**
>
> > Walk me through the three strategies for handling deep hierarchies in treemaps: depth-limited (show top 3 levels only, aggregate the rest), zoomable (interactive drill-down), and switching forms (sunburst or circle packing). For each, name the use case where it's best and the trade-offs. Cite Shneiderman's original treemap paper and modern extensions.
>
> **What to do with the output:** Save the analysis. The depth-limit decision recurs in every treemap project.

---

## Concept 2 — Sunburst diagrams: depth as the primary channel

A sunburst diagram is a hierarchy chart with concentric rings. The center represents the root; each subsequent ring represents one level of depth. Each segment's *angle* encodes its value (proportional to the parent), and the *radial extent* encodes its level.

### When sunbursts work

- Hierarchies where *depth* is the primary question (organizational structure with many levels; taxonomic classification; file-system browsing).
- Up to ~5 levels of depth. Past 5, outer rings compress into slivers.
- The reader needs to see hierarchy structure clearly.

### When sunbursts fail

- Hierarchies with too many leaves at deep levels. The outer ring becomes a wall of tiny segments.
- Datasets where exact value comparison matters. Angle is rank 4 in Cleveland & McGill (Chapter 1); position-based forms (treemap, bar) are more accurate.
- Audiences without graphicacy for radial-encoded forms.

### Design decisions

**Depth limit.** Five levels maximum. Past 5, the outer ring slivers are illegible. The pantry's sunburst examples observe this limit.

**Angle encoding.** The default is for angle to be proportional to value (each segment's angle = parent's angle × child's share). This gives a consistent encoding: zooming in or out, the relative angles preserve proportions.

**Color.** Top-level categorical hue cascading through descendants is the standard. Each "branch" of the sunburst has its own hue family. Within a branch, sub-categories share the parent's hue with luminance variation.

**Interaction.** Sunbursts work better with interaction. A click on a segment can rotate or zoom to focus on that branch. Static sunbursts past 4 levels are rarely readable.

The pantry's sunburst implementation shows the standard form. The depth limit is observed; the colors cascade by top-level category.

---

## Concept 3 — Circle packing: the irregular-hierarchy form

Circle packing represents each hierarchy node as a circle. Children of a node are circles nested inside their parent's circle. The packing algorithm (Wang's algorithm or `d3-hierarchy`'s implementation) places the children to minimize wasted space.

### When circle packing works

- Hierarchies with *irregular depth* (some branches go 3 levels, others 5, others 1).
- Datasets where the part-to-whole structure matters and depth comparison is secondary.
- Audiences who appreciate the organic, less-structured aesthetic.

### Why irregular depth matters

Treemaps assume each branch will be subdivided. When one branch has only one level and another has three, the treemap forces the single-level branch into a single rectangle while the three-level branch is subdivided heavily. The chart reads as if the deeper branches "matter more" because they have more visual elements.

Circle packing handles this gracefully. Each branch's hierarchy is shown to whatever depth it has; less-detailed branches simply have fewer nested circles. The visual hierarchy reflects the data's actual structure.

### Limitations

- **Space efficiency.** Circles don't tile rectangular space; circle packing uses 70–90% of the available area, vs. treemaps' near-100%. For dense dashboards, this matters.
- **Area perception.** Circle area is harder to compare than rectangle area (rectangles have aligned edges; circles don't). Stevens' power law applies similarly, but rectangles' alignment makes ranking easier.
- **Labeling.** Circles inside circles can have labeling challenges; the leaf circles are smaller than the parent circles, and labels often overlap.

The pantry's circle packing example shows the form. Compare to the treemap: same hierarchical data, different visual structure.

> ### ↳ Dig Deeper — Treemap vs. circle packing for your data
>
> **Prompt:**
>
> > Take a hierarchical dataset I have (organizational structure, file system, taxonomic classification, expense breakdown). Walk through whether the depth is regular or irregular. If regular, recommend treemap with depth limit. If irregular, recommend circle packing. Build both with Claude Code. Compare what each reveals.
>
> **What to do with the output:** Save the comparison. The form choice for hierarchical data recurs across many domains.

---

## Concept 4 — Tree diagrams and dendrograms

A tree diagram represents the hierarchy as a node-link structure. Each node is a circle (or rectangle) with text; each parent-child relationship is a line. The chart shows exact structure rather than proportions.

### When tree diagrams work

- The reader needs to see *exact structure* (which node is the parent of which child) rather than proportions.
- Phylogenetic relationships, organizational charts where reporting structure matters more than headcount, decision trees.
- Audiences familiar with org-chart-style visualization.

### When they fail

- Large hierarchies (50+ nodes). The chart sprawls and requires scrolling or zooming.
- Datasets where the *quantitative magnitude* at each node is the primary question (treemap or sunburst is better).
- Wide trees (many siblings per node). The horizontal layout becomes unwieldy.

### Dendrograms

A dendrogram is a tree diagram with the nodes arranged along an axis (typically vertical). Used commonly for hierarchical clustering output: the leaves are observations, the branches are merges, and the height of each merge encodes the dissimilarity at which it occurred.

For Claude Code work: D3's `d3-hierarchy` provides `cluster` and `tree` layouts for these forms. Specify the layout in the prompt.

---

## Concept 5 — Choosing among hierarchy forms

The four major forms map to four primary questions:

- **Proportions matter most → treemap.** Rectangular area is the most accurate hierarchical encoding.
- **Depth matters most → sunburst.** Concentric rings make level structure visible.
- **Irregular depth → circle packing.** Handles unequal branching gracefully.
- **Exact structure matters most → tree diagram.** Node-link makes parent-child relationships explicit.

The choice depends on what the reader needs to see. Most published hierarchical charts reach for the treemap by default; the alternatives win in specific contexts where the default fails.

For Claude Code work, the specification belongs in the prompt:

> "Treemap with depth limit 3, squarified algorithm (`d3.treemapSquarify`), top-level hue cascading through descendants."

vs.

> "Sunburst with depth limit 5, click-to-zoom interaction, top-level hue cascading through descendants."

vs.

> "Circle packing with no depth limit (irregular), bubble color encoded by top-level category."

The form follows the question, the audience, and the data structure.

---

## Mid-chapter checkpoint

Pick a hierarchical dataset from your work. Identify the depth (regular or irregular?). Identify the primary question (proportion, depth, or structure?). Match to a form. Walk through the channel decomposition you'd specify.

You should be able to do this in 90 seconds.

---

## Extended worked example — building the HAI treemap

Build the HAI humanitarian R&D treemap. The data: 4 sectors, each with 3–5 sub-categories, each sub-category with a funding value.

### Channel decomposition

- Marks: nested rectangles.
- Position-area (top-level): position by squarified algorithm; area by funding sum of children.
- Position-area (sub-category): position within parent by squarified algorithm; area by funding value.
- Color hue: sector identity (top-level), cascading to sub-categories with luminance variation.
- Labels: sector names on top-level rectangles; sub-category names on rectangles above 5% of total.

### The four-move prompt

```
**Show what I have:**
Hierarchical funding data, 4 sectors with sub-categories. Sample (one
sector):

  Food Security
    - Direct Aid: 280
    - Cash Transfers: 60
    - Voucher Programs: 40

Total values per sector range $50M to $300M.

**Say what I want:**
Treemap in D3 v7. Single self-contained HTML file with inline CSS and
inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Hierarchy: 2 levels (sector → sub-category).
- Marks: nested rectangles.
- Layout: d3.treemap() with d3.treemapSquarify (default).
- Top-level rectangle area: sum of children (sector total).
- Sub-category rectangle area: that sub-category's funding.
- Color hue: sector identity. Use d3.scaleOrdinal with HAI palette
  (Food Security #8B0000, Shelter #6B6B5E, Water #5C3317,
  Health #4A4A4A).
- Sub-category color: parent hue with luminance variation
  (lighter for larger values within the parent).
- Labels: sector name on top-level (always visible). Sub-category name
  on rectangles >5% of total (otherwise hover tooltip).
- Subtitle: "Humanitarian R&D Funding by Sector and Sub-category".
- Margins: top 60, right 40, bottom 40, left 40.
- Dark mode support.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements which channel. Note any decisions not
specified.
```

### Audit

Standard Evergreen/Emery plus:

- Squarified algorithm used (not slice or dice).
- Depth limit observed (2 levels in this case; 3 maximum).
- Color hierarchy cascades correctly.
- Labels appear on rectangles large enough to read.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build a treemap, sunburst, circle packing, or tree diagram — choosing the form based on whether the question is about proportions, depth, irregular branching, or exact structure.

You can apply the depth limits each form requires (3 for treemaps; 5 for sunbursts; circle packing handles irregular without limit; tree diagrams scale to 50+ nodes before sprawl).

You can specify the layout algorithm for treemaps (`d3.treemapSquarify` for area-comparison readability) and the interaction model for sunbursts (click-to-zoom for deep hierarchies).

You can recognize when a hierarchical chart is the wrong family — when the data is part-to-whole without depth (use Chapter 9's forms), or when exact node-by-node structure matters more than aggregate proportions (use a node-link tree).

---

## Key terms

- **Treemap.** Nested rectangles, area encodes value. Best for proportion comparison.
- **Squarified algorithm.** Treemap layout that minimizes aspect-ratio variance. The default in modern treemap practice.
- **Sunburst.** Concentric rings; angle encodes value, radial position encodes depth.
- **Circle packing.** Nested circles; handles irregular hierarchy depth.
- **Tree diagram.** Node-link representation; shows exact parent-child structure.
- **Depth limit.** Treemaps max 3, sunbursts max 5; past these, the chart fails on legibility.

---

## Discussion questions

1. Treemaps and circle packing both encode area. Why do treemaps win on accuracy when both forms work?
2. Sunbursts make depth visible at the cost of angle perception. When is the trade-off worth it?
3. Tree diagrams scale poorly to large hierarchies. What does this say about visualizing organizational structures with 1,000+ employees?
4. The depth limits in this chapter (treemap: 3; sunburst: 5) are practical heuristics. What conditions could justify exceeding them?
5. *Cross-chapter synthesis.* Chapter 9 (part-to-whole) and Chapter 10 (hierarchy) both deal with proportion encoding. Frame the boundary between them.

---

## Exercises

### Warm-up

**Exercise 10.1** — *Form selection.* For each, choose treemap / sunburst / circle packing / tree diagram and justify:
- Government budget broken down by department, sub-department, line item (3 levels).
- A taxonomic tree of species with 6 levels of depth.
- An organizational structure where some divisions have 4 layers and others have 1.
- A phylogenetic relationships diagram for 30 organisms.

**Exercise 10.2** — *Treemap depth diagnosis.* You see a treemap with 5 levels of depth. Rectangles at the deepest level are too small to label. Specify the redesign.

**Exercise 10.3** — *Circle packing vs. treemap.* Take a hierarchical dataset where some branches are deeper than others. Build both forms with Claude Code. Compare.

### Application

**Exercise 10.4** — *Build a sunburst with depth limit.* Take a 5-level hierarchical dataset. Build a sunburst with click-to-zoom interaction.

**Exercise 10.5** — *Audit a published treemap.* Find one in a recent publication. Audit using Evergreen/Emery + hierarchy-specific (depth limit, labeling, color cascade).

**Exercise 10.6** — *Tree diagram for org structure.* Take an organization chart. Build a tree diagram. Identify when the chart starts to fail (size? width?).

### Synthesis

**Exercise 10.7** — *Hierarchy form portfolio.* Take one hierarchical dataset and build it as treemap, sunburst, circle packing, and tree diagram. Compare what each reveals.

**Exercise 10.8** — *Interaction design.* Add zoomable interaction to a treemap with Claude Code. Test it on a 4-level dataset.

### Challenge

**Exercise 10.9** — *Squarified vs. slice algorithms.* Build the same treemap using `d3.treemapSquarify` and `d3.treemapSlice`. Compare what each reveals about the data.

**Exercise 10.10** — *Hybrid form.* Build a hybrid that combines a sunburst (showing top 3 levels) with a treemap (showing the deepest level when zoomed). Use Claude Code.

---

## LLM Exercise — Chapter 10: Hierarchy Charts

```
I have a hierarchical dataset of [DESCRIBE: levels, branching pattern,
values at leaves]. The communication goal is [DESCRIBE].

Walk me through:
1. Identify hierarchy depth (regular vs. irregular).
2. Identify the primary question (proportion, depth, structure).
3. Choose form: treemap (proportion + regular depth), sunburst
   (depth + 5-level limit), circle packing (irregular depth), or tree
   diagram (exact structure).
4. For treemaps: choose squarified algorithm; specify depth limit.
   For sunbursts: specify depth limit; specify zoom interaction.
   For circle packing: specify color encoding.
5. Specify channels.
6. Write four-move Claude Code prompt.

Audit using Evergreen/Emery + hierarchy-specific (depth limits,
algorithm choice, label placement, color cascade).
```

**Connection to previous chapters:** Chapter 1 (Stevens' power law on area), Chapter 9 (part-to-whole connection), Chapter 4 (workflow).

**Preview of next chapter:** Chapter 11 covers flow and network charts — Sankey, alluvial, chord, arc, force-directed. Where Chapter 10 used hierarchy depth as the structural channel, Chapter 11 uses connection (existence or magnitude) between entities.

---

## Visual suggestions

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

## Further reading

- **Shneiderman, Ben. (1992).** "Tree visualization with tree-maps: 2-d space-filling approach." *ACM Transactions on Graphics.* The original treemap.
- **Bruls, Mark, Kees Huizing, and Jarke J. van Wijk. (2000).** "Squarified treemaps." The squarified layout algorithm.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* Section on hierarchical visualization.
- **The book's pantry** — `treemap.html`, `tree-diagram.html`.

---

## Tags

hierarchy-charts, treemap, sunburst, circle-packing, tree-diagram, dendrogram, Shneiderman, squarified-algorithm, depth-limit, Bertin-area, Stevens-power-law, Gestalt-figure-ground, D3, Claude-Code
