# Chapter 12 — Hierarchy Charts
*Containment as the Encoding.*

---

Here is a problem that looks like it has an obvious solution.

You have a government budget. It breaks down into departments. Each department breaks down into programs. Each program breaks down into line items. You want to show, in a single chart, how the money is distributed at every level — how much goes to Health versus Education, how much of Health goes to hospitals versus prevention, how much of hospitals goes to staff versus equipment. You want the reader to see both the big picture and the detail, simultaneously.

You make a treemap. Nested rectangles, area proportional to budget. The top-level rectangles are the departments. Inside each, smaller rectangles are the programs. Inside each program, even smaller rectangles are the line items. The chart works. The reader can see that Health is the largest department at a glance. They can see which program within Health is largest. They can drill down to any line item.

Then someone asks: can you also show the organizational hierarchy — not the budget proportions, but the *reporting structure*? Which programs report to which assistant secretary? How many levels of management separate the line item from the secretary?

You cannot do this with a treemap. The treemap shows area (budget). It does not show hierarchy depth as a distinct visual signal. If you add a fourth level of nesting, the innermost rectangles become unreadable slivers. If you want to show depth as the primary structure, you need a different form.

This is the organizing question of hierarchy chart design: what is the hierarchy *for*? The form follows the answer.

<!-- → [FIGURE: Two side-by-side panels, same government-budget dataset (4 departments → 3–4 programs each → 2–3 line items each). Left: treemap — the reader can immediately see that Health is the largest department; the proportional structure is clear. Right: tree diagram — the reporting structure is clear; Health has an Assistant Secretary, three division directors, and six branch chiefs; but the budget proportions are invisible (all nodes are the same size). Caption: "Same hierarchy, two questions. Left: how are the proportions distributed? Right: who reports to whom? The chart cannot answer both simultaneously. Choose the question first."] -->

---

## What a Hierarchy Actually Contains

Before choosing a form, name what the hierarchy contains. Hierarchies have three distinguishable properties that different forms encode differently.

**Proportions.** At each level, the children of a node divide the parent's value. A department's total budget equals the sum of its programs' budgets. Showing proportions means making the area of each node visually proportional to its value.

**Depth.** The hierarchy has levels, and the number of levels matters. An organization with five layers of management between the CEO and a frontline worker is structured differently from one with two layers — and the chart should make this visible.

**Exact structure.** Who reports to whom. Which nodes are siblings. How many children each parent has. Structure is not the same as proportion or depth — it is the topology of the graph.

These three properties are not equally accessible to every form. The form choice is a question of which property the reader needs to see most.

---

## The Four Forms and What Each Encodes

**Treemap.** Nested rectangles where each rectangle's area encodes its value. The squarified algorithm (Bruls, Huizing, van Wijk, 2000) keeps aspect ratios near square, which maximizes the accuracy with which the reader can compare areas. Treemaps answer the question "how are the proportions distributed?" with the highest accuracy available for area encoding. They do this well for two or three levels of nesting. Past three levels, the innermost rectangles compress into thin slivers where area is impossible to read and labels cannot fit.

**Sunburst.** Concentric rings where the center is the root, each ring is one level of depth, and each segment's angle is proportional to its value within its parent. The sunburst answers the question "how many levels deep does this hierarchy go, and how are the proportions distributed at each level?" It makes depth structurally visible — the ring position encodes level without ambiguity. The failure mode is the inverse of the treemap's: the sunburst can show more levels, but past five or so, the outer ring compresses into illegible slivers because each ring's radial width is a fixed fraction of the radius.

**Circle packing.** Nested circles where each circle's area encodes its value and children are packed inside their parent circle. Circle packing handles irregular hierarchy depth gracefully — a branch with five levels nests five circles deep without forcing other branches to match. It answers the question "what is the proportional structure of this hierarchy, including its irregular branching?" The cost: circles cannot tile space as efficiently as rectangles (typical packing efficiency is 70–90%), and area comparisons between circles are less accurate than between rectangles because circles lack the aligned edges that help the eye anchor.

**Tree diagram.** Nodes connected by edges, usually arranged top-to-bottom or left-to-right. No area encoding — each node is the same visual size regardless of its value. The tree diagram answers "what is the exact structural relationship between nodes?" It shows reporting lines, taxonomy membership, decision paths. It fails when the dataset is large (50+ nodes produces a sprawling chart that requires scrolling) or when the quantitative magnitude at each node is the question.

Four forms. Four primary questions. The choice is not aesthetic.

<!-- → [INFOGRAPHIC: Four-panel reference grid, one panel per hierarchy form. Each panel: form name (uppercase, JetBrains Mono), a thumbnail sketch of the form's visual structure, the primary channel labeled, and the one-line "use when" condition. Panels: Treemap (nested rectangles, "area encodes value," "proportions are the question"), Sunburst (concentric rings, "ring position encodes depth, angle encodes proportion," "depth is the question"), Circle packing (nested circles, "area encodes value, nesting reflects topology," "irregular depth"), Tree diagram (nodes + edges, "structure only, no area encoding," "exact parent-child relationships"). This is the navigation reference the reader returns to whenever they have hierarchical data.] -->

---

## Why Rectangles Win on Area Comparison

Both treemaps and circle packing encode area. The treemap wins on area comparison accuracy, and the reason is the same mechanism that makes bar charts outperform pie charts.

Rectangles have aligned edges. When two rectangles share a common baseline or a common axis, the reader can compare their heights or widths with near-position-accuracy — the eye anchors on the shared reference. This is the same mechanism that makes bar charts so readable: position along a common scale is the highest-accuracy channel Cleveland and McGill identified.

Circles have no such alignment. Comparing the area of two circles requires the eye to estimate both radii, square them (or estimate the area directly), and compare. Stevens' power law applies: area perception has an exponent of about 0.7, so a doubled area is perceived as roughly 1.5 to 1.7 times larger. For both forms, the area compression applies. But rectangles provide an additional anchor — the shared edges — that circles do not.

The practical consequence: for datasets where precise area comparison matters, use a treemap. For datasets where the hierarchy's irregular structure is the point — some branches deep, some shallow, the topology itself the argument — use circle packing. The perceptual trade-off is real but bounded; the structural-match trade-off is not.

<!-- → [FIGURE: Two pairs of shapes side by side showing the alignment advantage. Left pair: two rectangles (100 and 200 square units) sharing a common left edge — the reader can anchor the right edges against each other and estimate the 2:1 ratio with high accuracy. Right pair: two circles (100 and 200 square units) — no alignment, no anchor; the reader estimates area by radius, which introduces more error. Caption: "Rectangles provide an alignment anchor; circles do not. The same Stevens exponent applies to both, but rectangles' shared edges reduce the estimation error." Annotate approximate perceived ratio under Stevens for each pair.] -->

---

## The Depth Limit and Why It Exists

Treemaps fail past three levels. Sunbursts fail past five. These are not arbitrary rules — they follow from the geometry of the encoding.

For a treemap at level n, the area allocated to a node is the area of its parent rectangle multiplied by the node's proportion of its parent's value. Each level of nesting multiplies by a fraction less than 1. At three levels, a node with 10% share at each level has an area equal to 0.1 × 0.1 × 0.1 = 0.001 of the total chart area. If the chart is 800×600 pixels, that node occupies 0.48 square pixels — smaller than a single pixel. It is not just hard to label; it does not exist visually.

For a sunburst, the radial width allocated to each ring is the total radius divided by the number of levels. A chart with a radius of 400 pixels and six levels gives each ring a width of about 67 pixels. The outermost ring at 400 pixels radius has a circumference of 2π × 400 ≈ 2,513 pixels, divided among all the segments at that level. If there are 50 leaf nodes, each segment is about 50 pixels wide. If there are 200 leaf nodes, each is about 12 pixels wide — too small to label and almost too small to distinguish visually.

The depth limits are where the geometry of the encoding runs out of space. Knowing the mechanism means knowing when to stop and either truncate (show only the top N levels) or switch forms (zoomable treemap for deep hierarchies, circle packing for irregular ones).

<!-- → [FIGURE: Two panels showing depth-limit failure. Left: a treemap with 5 levels. The innermost rectangles at level 5 are shown with a zoom box: they measure approximately 2×3 pixels. Annotation: "At 10% share per level, a level-5 node occupies 0.001% of chart area = 0.48 sq px on an 800×600 chart. Not visible." Right: a sunburst with 7 levels. The outermost ring is shown with a zoom box: at 200 leaf nodes, each segment is ~12 pixels wide. Annotation: "200 leaf nodes at radius 400px → 12px per segment. Too small to label; barely distinguishable from gaps." Caption: "Both depth limits follow from the geometry of the encoding, not from taste."] -->

---

## Squarification and Why the Algorithm Matters

The squarified treemap algorithm deserves its own explanation because it is not obviously better than alternatives, and understanding why it is reveals something about the area-comparison mechanism.

The first treemap algorithms (slice-and-dice, attributed to Shneiderman 1991) divided each rectangle by alternating horizontal and vertical cuts. A large parent rectangle gets sliced into vertical columns; each column gets diced into horizontal rows. This produces a visually clean structure but tends to generate extremely elongated rectangles — a node with 2% of its parent's value, in a parent that is 600 pixels wide, gets a column that is 12 pixels wide and perhaps 400 pixels tall. A 12×400 rectangle and a 400×12 rectangle have the same area; they look nothing alike, and neither looks like it encodes the same value as a 69×69 rectangle (which is the squarish version of the same area).

Stevens' power law applies here too: the perception of area in elongated rectangles is more distorted than in near-square ones, because the eye tends to read the longer dimension as dominant. A very tall thin rectangle "looks bigger" than its actual area implies.

The squarified algorithm minimizes the worst aspect ratio in the layout. It groups items into the most square arrangement possible at each step. The result looks less regular than slice-and-dice, but area comparison is more accurate because the rectangles are closer to square.

For Claude Code work: specify `d3.treemapSquarify` explicitly. The other D3 treemap algorithms (`treemapSlice`, `treemapDice`, `treemapBinary`) have specific uses (slice-and-dice for time-ordered data where one dimension should be preserved, binary for balanced splits) but the default for general area comparison is squarify.

<!-- → [FIGURE: Two treemaps side by side, same dataset (12 nodes with varying values). Left: slice-and-dice layout — several rectangles are extremely elongated (aspect ratios of 10:1 or higher). Three of the elongated rectangles are highlighted with their actual area and an annotation: "Eye reads this as larger than it is." Right: squarified layout — all rectangles are near-square. The same three nodes are highlighted: "Aspect ratios within 2:1. Eye reads area more accurately." Caption with the Stevens calculation: "A 12×400 rectangle and a 69×69 rectangle have identical areas. Stevens' dominant-dimension bias makes the tall thin one look larger."] -->

---

## Sunbursts and the Gestalt Figure-Ground Mechanism

The sunburst diagram works because of a Gestalt perceptual mechanism that the treemap does not use: figure-ground.

In a sunburst, the center is the figure. The outer rings recede into background. The reader's eye naturally treats the center as the root — the organizing structure from which everything else radiates. Moving outward means moving deeper into the hierarchy. This spatial metaphor is so natural that readers unfamiliar with sunburst charts tend to understand the center-to-outer structure without instruction.

The Gestalt mechanism also produces the failure mode. When the sunburst has six or seven levels, the outer rings compress into slivers. The outermost ring is the least prominent, most recessed part of the figure — visually, it becomes part of the background rather than the content. The hierarchy's deepest elements, which are often the most granular and specific, become the least visible. The chart is punishing its most detailed elements for being detailed.

The fix for deep hierarchies is interactive zooming: clicking on a segment expands it to fill the entire chart as a new root, with its children as the new ring structure. The reader navigates depth by zooming, not by trying to read all levels simultaneously. This is how the sunburst earns its keep for deeper hierarchies — not by showing all levels at once, but by letting the reader explore one branch at a time.

For Claude Code work: specify click-to-zoom interaction for sunbursts with more than three or four levels. Without interaction, a deep sunburst is typically worse than a treemap.

---

## Irregular Depth and Circle Packing's Structural Advantage

The case for circle packing is most legible on an example.

Imagine a dataset describing humanitarian aid organizations: some are large multinationals with programs, sub-programs, and project activities (three levels); some are regional NGOs with programs only (two levels); some are local grassroots organizations with no formal sub-structure (one level). A treemap would need to decide how to handle the single-level organizations — either leaving them as flat rectangles that look formally equivalent to the top level of the multi-level organizations, or artificially adding empty hierarchy levels to equalize depth.

Circle packing makes no such demand. Each organization is a circle. If it has programs, smaller circles nest inside. If those programs have sub-programs, smaller circles nest inside those. Organizations without sub-structure are just circles with no children — visually simple, reflecting their structural simplicity. The chart's topology matches the data's topology.

The circle packing advantage is structural honesty for irregular hierarchies. The cost — lower area-comparison accuracy, poorer space efficiency — is real but often acceptable when the topology is what the reader needs to see.

<!-- → [FIGURE: Two panels, same dataset of humanitarian aid organizations with irregular depth. Left: treemap — single-level organizations are shown as flat rectangles visually equivalent to the top level of multi-level organizations; the chart looks like all organizations have the same depth, which is false. A 1-level local NGO and a 3-level multinational look formally similar. Right: circle packing — the 1-level local NGO is a single circle with no children; the 3-level multinational has three layers of nested circles. The structural difference is immediately visible. Caption: "Treemap forces a uniform grid onto unequal structure. Circle packing reflects the data's actual topology."] -->

---

## The Tree Diagram: When Topology Is Everything

Sometimes neither proportions nor depth is the question. The question is: who reports to whom?

A tree diagram is the right form when the structure itself is the answer. An organizational chart showing reporting relationships. A phylogenetic tree showing species divergence. A decision tree showing conditional branches. In all these cases, the quantitative value at each node matters less than the edges between nodes — the explicit parent-child relationships that define the hierarchy.

Tree diagrams fail gracefully at small-to-medium sizes (up to 50 or so nodes) and fail hard at large sizes. A 500-node org chart cannot be read as a static tree diagram; it becomes a wall of boxes and lines. The solutions are either filtering (show only the top three levels; let the reader drill into sub-trees) or switching to a different form (a treemap or sunburst that uses area to make the large organization legible at a glance).

For Claude Code work: D3's `d3.tree()` and `d3.cluster()` layouts handle the geometry. Specify the orientation (top-to-bottom vs. left-to-right), the node spacing, and whether to use smooth bezier curves or right-angle connectors. Left-to-right layouts work better for deep hierarchies (more horizontal space); top-to-bottom layouts work better for wide hierarchies (more vertical space).

---

## How This Changes the Prompt

The channel decomposition for hierarchy charts differs from the charts in previous chapters because the primary channel — nested area — emerges from the layout algorithm, not from explicit x/y position assignments.

For a treemap, the critical constraints are: the layout algorithm (`d3.treemapSquarify`), the depth limit (state it explicitly so Claude Code does not render all levels), the color encoding (top-level hue cascading to children, or a second quantitative variable as luminance), and the label rule (labels only on rectangles above a minimum size threshold, tooltip fallback for smaller ones).

For a sunburst, the critical constraints are: the depth limit (5 maximum for static; more with click-to-zoom specified), the click-to-zoom interaction (required for depth > 3), and the color cascade (same top-level hue convention as treemaps).

For circle packing, the critical constraint is that there is no depth limit — but the color encoding needs to identify levels, because the visual nesting alone may not be sufficient for the reader to count levels. Specify color or stroke-width to distinguish depth levels.

For tree diagrams, the critical constraints are: orientation, node spacing, connector style (orthogonal right-angle connectors for org charts; diagonal beziers for phylogenies), and whether nodes should encode a quantitative variable via size or color.

A follow-up prompt for the most common hierarchy failure — Claude Code rendering all six levels of a treemap when you specified three:

> "The treemap is rendering all six levels. Limit to 3 levels by setting `root.depth <= 2` as the leaf condition in the layout. Rectangles at depth 3 should be leaf nodes regardless of whether the data has children below them. Regenerate."

---

## The Feynman Test

The test for this chapter: given any hierarchical dataset, answer three questions before touching Claude Code.

First: what is the primary question — proportion, depth, or structure? Proportion points to treemap. Depth points to sunburst. Structure points to tree diagram. Irregular topology points to circle packing.

Second: how deep is the hierarchy, and is the depth regular or irregular? More than three levels in a treemap means the innermost nodes will be illegible. More than five levels in a sunburst means the outermost ring will be unreadable. Irregular depth in a treemap means artificial padding or misleading flat rectangles.

Third: does the form require interaction to work? A treemap with four levels needs click-to-zoom. A sunburst with six levels needs click-to-zoom. A static chart at those depths fails. Knowing this before building saves the iteration that discovers it after.

If you can answer all three questions in sixty seconds, you know the chapter. The forms, their encoding mechanisms, and their depth limits are compact enough to hold in working memory. What changes chart to chart is the data's structure — but the questions that reveal which form the structure requires are always the same three.

---

## Exercises

### Warm-up

**Exercise 12.1 — Form selection.** For each of the following, name the right hierarchy form (treemap, sunburst, circle packing, or tree diagram) and justify in one sentence using the chapter's three-property framework (proportions, depth, structure):

- A government budget broken down by department, sub-department, and line item (3 uniform levels, proportions are the question).
- A taxonomic classification with 6 levels of depth, from kingdom to species.
- A portfolio of humanitarian aid organizations, some with 3 levels of structure and some with 1.
- An organizational chart for a 30-person team where reporting lines are the question.
- A file system visualization where disk space usage at every level is the question.

**Exercise 12.2 — Depth-limit calculation.** A treemap is 900×700 pixels (630,000 total square pixels). A node at the third level of nesting has a 15% share at each level. (a) Calculate its area in square pixels. (b) Would a label fit? (c) Specify the redesign — what two options does the chapter name?

**Exercise 12.3 — Squarification audit.** Find a published treemap (in a report, dashboard, or data journalism piece). Estimate the aspect ratios of five rectangles. Are they close to 1:1 (squarified) or highly elongated (slice-and-dice)? If elongated, explain using Stevens' power law why the chart under-represents the size differences between nodes.

### Application

**Exercise 12.4 — Build a treemap with depth limit.** Take a hierarchical dataset with at least 3 levels. Write the four-move prompt specifying `d3.treemapSquarify`, a depth limit of 3, top-level hue cascading, and a label threshold (labels only on nodes above 3% of total). Run, audit, iterate. Document what Claude Code got wrong on the first attempt.

**Exercise 12.5 — Build a sunburst with click-to-zoom.** Take a hierarchical dataset with 4–5 levels. Write the four-move prompt specifying a depth limit of 5, click-to-zoom interaction, and the color cascade. Verify that the interaction works by clicking three levels deep.

**Exercise 12.6 — Circle packing for irregular depth.** Take a dataset with irregular hierarchy depth (some branches 3 levels, some 1). Build it as both a treemap and circle packing with Claude Code. Compare how each handles the branches with fewer levels. Identify which form is structurally honest.

### Synthesis

**Exercise 12.7 — Hierarchy form portfolio.** Take one hierarchical dataset and build it as all four forms: treemap, sunburst, circle packing, and tree diagram. For each, name one question it answers clearly and one question it cannot answer. The exercise makes the form-choice framework concrete rather than abstract.

**Exercise 12.8 — Deep hierarchy strategy.** Take a hierarchical dataset with 6 levels. The chapter names three strategies for handling it: depth-limited static display (show top 3), zoomable interaction, or form switch. Implement all three with Claude Code. Which gives the reader the most useful access to the data? Justify using the three-question Feynman test.

### Challenge

**Exercise 12.9 — Squarification algorithm comparison.** Build the same treemap using `d3.treemapSquarify`, `d3.treemapSlice`, and `d3.treemapBinary`. For each, measure the aspect ratio of the five largest rectangles. Calculate the Stevens-predicted area perception error for the most elongated rectangle in each version. Confirm that squarify produces the smallest perception error.

**Exercise 12.10 — Hybrid hierarchy form.** Design and build a two-panel chart: a sunburst showing the top 3 levels on the left, and a treemap expanding the selected branch on the right. When the user clicks a segment in the sunburst, the treemap on the right updates to show that branch's sub-hierarchy in detail. This combines depth-as-primary-channel (sunburst) with proportion-as-primary-channel (treemap) in a coordinated view.

---

## Key Terms

**Treemap.** Nested rectangles where area encodes value. Best for proportion comparison. Squarified algorithm minimizes aspect-ratio variance. Depth limit: 3 levels for static display.

**Squarified algorithm.** Bruls, Huizing, van Wijk (2000). Groups nodes to minimize worst aspect ratio. More accurate for area comparison than slice-and-dice. Implemented as `d3.treemapSquarify`.

**Sunburst.** Concentric rings; radial position encodes depth, angle encodes proportion within parent. Makes depth structurally visible. Depth limit: 5 levels for static; more with click-to-zoom.

**Circle packing.** Nested circles; area encodes value. Handles irregular hierarchy depth without the forced-depth problem of treemaps. Lower area-comparison accuracy than treemaps due to absent aligned edges.

**Tree diagram.** Node-link representation showing exact parent-child structure. No area encoding. Best for topology questions.

**Depth limit.** The level beyond which the form becomes illegible. Treemap: 3. Sunburst: 5. Circle packing: no hard limit. Tree diagram: ~50 nodes.

**Gestalt figure-ground (sunburst).** The center reads as the figure; outer rings recede. Makes hierarchy depth intuitively readable but punishes deep outer rings with visual compression.

**Click-to-zoom.** Interaction pattern for deep hierarchy charts. Clicking a node expands it as a new root, showing its children as a new layout.

---

## LLM Exercise — Chapter 12: Hierarchy Charts

**Project:** [TBD — selected after Chapter 00]

**What you're building this chapter:** A hierarchy chart with explicit form selection and an audit document confirming depth limits, algorithm choice, color cascade, and label placement.

**Tool:** Claude Code (for the build) + Claude chat (for the audit and iteration).

---

**The Prompt (audit + build):**

```
I have a hierarchical dataset of [DESCRIBE: levels, branching pattern,
values at leaves or nodes, whether depth is regular or irregular]. The
communication goal is [DESCRIBE: what the reader needs to know in 5
seconds].

Walk me through the hierarchy-chart design:

1. Identify the depth (how many levels?) and whether it is regular
   (all branches the same depth) or irregular (branches vary in depth).

2. Identify the primary question:
   - Proportions matter most → treemap.
   - Depth matters most → sunburst.
   - Irregular topology → circle packing.
   - Exact structure → tree diagram.

3. Apply the depth limit. For treemaps: 3 levels maximum for static
   display; specify click-to-zoom if deeper. For sunbursts: 5 levels
   maximum; specify click-to-zoom if deeper.

4. For treemaps: specify d3.treemapSquarify (the squarified algorithm,
   not slice-and-dice). Justify why squarification improves area
   comparison accuracy.

5. Specify the color encoding: top-level hue cascading to children
   with luminance variation, or a second quantitative variable as
   luminance.

6. Specify the label rule: visible labels only on nodes above a
   minimum size threshold; hover tooltip for smaller nodes.

7. Write a four-move Claude Code prompt that produces the chart.

After Claude Code returns, audit using the Evergreen/Emery subset plus
hierarchy-specific checks: depth limit observed, squarified algorithm
confirmed in code, color cascade correct, labels appear only where
readable, click-to-zoom implemented if the depth requires it.
```

---

**What this produces:** Audit document plus working hierarchy chart. Save as `chapter-12-hierarchy-audit.md` and `chapter-12-hierarchy.html`.

**How to adapt this prompt:**
- *For your own dataset:* Replace the description and communication goal.
- *For ChatGPT / Gemini:* Works as-is.
- *For a Claude Project:* Save the hierarchy-chart framework as system context.
- *For Cowork:* Use Cowork to read the data file directly.

**Connection to previous chapters:** Builds on Chapter 3 (Stevens' power law on area — treemap area encoding), Chapter 4 (chart selection — confirming the hierarchy family from the FT Visual Vocabulary), Chapter 5 (the Claude Code four-move prompt applied to hierarchical specifics). The area-encoding principle from Chapter 3 governs both bubble charts (Chapter 10) and hierarchy charts; this chapter applies it to the specific geometry of nested rectangles and circles.

**Preview of next chapter:** Chapter 13 covers flow and network charts — Sankey, alluvial, chord, arc, force-directed. Where this chapter used containment as the encoding, Chapter 13 uses connection — the existence or magnitude of a link between entities.

---

## Further Reading

- **Shneiderman, Ben. (1992).** "Tree visualization with tree-maps: 2-d space-filling approach." *ACM Transactions on Graphics* 11(1). The original treemap.
- **Bruls, Mark, Kees Huizing, and Jarke J. van Wijk. (2000).** "Squarified treemaps." In *Proceedings of the Joint Eurographics and IEEE TCVG Symposium on Visualization.* The squarified layout algorithm; available online.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* CRC Press. Chapter on hierarchical visualization, including the depth-limit analysis and the treemap-vs-sunburst trade-off.
- **Friendly, Michael. (2008).** "A Brief History of Data Visualization." In *Handbook of Data Visualization.* Springer. The origin story of Shneiderman's treemap and its development.
- **The book's pantry** — `treemap.html`, `circle-packing.html`, `tree-diagram.html` for working examples of each form.
