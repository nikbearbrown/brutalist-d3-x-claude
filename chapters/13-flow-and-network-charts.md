# Chapter 11 — Flow and Network Charts
*What Flows Where — and How Much.*

## Three suggested titles

- Flow and Network Charts: Sankey, Chord, Arc, Force-Directed
- When Width Carries Meaning, and When It Doesn't
- The Hairball Problem and What to Do About It

---

## Chapter overview

By the end of this chapter you will be able to build the family of flow and network charts — Sankey diagrams, alluvial diagrams, chord diagrams, arc diagrams, force-directed graphs — and you will know when each is right. You will know the channel-theory distinction between *flow magnitude* (Sankey/alluvial/chord-with-ribbons) and *connection existence* (non-ribbon chord, arc, force-directed), and how the distinction determines which form to choose.

---

## Learning objectives

1. **(Apply)** Build a Sankey diagram where flow width is proportional to quantity; verify that the proportionality holds at both the widest and narrowest flows (Tufte's proportional ink principle).
2. **(Analyze)** Diagnose a chord diagram that has become unreadable due to too many entities and propose a structural redesign, distinguishing between cases where ribbon width carries quantitative meaning vs. cases where existence is all that matters.
3. **(Evaluate)** Assess whether a force-directed graph or a Sankey diagram better serves a specified flow communication goal, using the Gestalt law of connection to justify the choice.

---

## Opening case — the HAI Sankey of global energy flow

Open `pantry/visualization/sankey-diagram.html` in a browser. Energy sources on the left (oil, coal, natural gas, nuclear, renewables); intermediate transformations in the middle (electricity, transportation fuel, heating); end uses on the right (industrial, residential, commercial). The flows between them are bands whose *width* is proportional to the energy quantity in exajoules.

You can read the chart in seconds: oil dominates as an energy source. Most oil flows to transportation fuel. Coal and natural gas dominate the electricity-generation flow. Nuclear and renewables contribute smaller bands. The thinnest flows (some renewable contributions to specific end uses) are visibly thin; the largest flow (oil to transportation fuel) is the dominant visual.

The chart is a flow map in Bertin's framework: width-as-channel encodes quantitative magnitude. The mark is a flow band; the channel is band width. The reader's perception applies Stevens' power law on area perception (Chapter 1) — wider bands look proportionally larger, with sublinear compression. Width is the channel that distinguishes Sankey from a non-quantitative network diagram.

What breaks if the flow widths are uniform? The chart becomes a topology diagram (does this connection exist?) rather than a flow diagram (how much flows?). The visual claim is fundamentally different. The data has not changed; the channel decision has, and the chart's meaning has shifted with it.

This is the channel-theory distinction this chapter is built around. **Flow magnitude** charts (Sankey, alluvial, chord-with-ribbons) use width as the magnitude channel; the question is "how much flows from A to B?" **Connection existence** charts (non-ribbon chord, arc, force-directed) use line presence; the question is "does A connect to B at all?" The two questions produce different chart families.

---

## Theoretical grounding — Bertin on width-as-channel, Gestalt connection, Cairo on Sankey origins

**Bertin on width as a channel.** Bertin's framework includes width (or thickness) as a magnitude channel. A line of consistent width carries no quantitative information; a line whose width varies encodes magnitude. Sankey diagrams exploit this directly: the flow band's width at any point is proportional to the quantity flowing there. If the flow narrows, the quantity has decreased; if it widens, increased. Width-as-channel is rank ~3 in Cleveland & McGill's accuracy ranking — usable but worse than position. The form earns its complexity when the flow structure itself is the question.

**Gestalt law of connection.** The principle: connected elements are perceived as belonging to the same group. Force-directed graphs exploit this — nodes and edges form clusters that the eye reads as cohesive groups. The Gestalt mechanism is what makes the visualization work. The same mechanism produces the failure mode (the "hairball"): when connection density is high, every node connects to many others, the visual becomes a tangled mass, and the Gestalt grouping breaks down.

**Cairo on Sankey origins.** Sankey diagrams were invented for energy-flow analysis (Captain Matthew Henry Phineas Riall Sankey, 1898). The original problem: visualize how energy is consumed and lost through industrial processes. Knowing the original problem clarifies when Sankey works — for *flows* (substances or quantities moving from sources to destinations through transformations), not for *correlations* or *similarity relationships*. Alluvial diagrams (a related form) extend Sankey to track *category transitions over time* (which voters shifted from one party to another between elections, for example).

---

## Concept 1 — Sankey diagrams

A Sankey diagram shows flows from a source set to a destination set (often with intermediate processing steps). Each flow is a band whose width encodes quantity.

### When Sankey diagrams work

- Quantitative flow data: things move from A to B with measurable magnitude.
- The structure of the flow (where does the most go?) is the primary question.
- 2–4 levels of source-intermediate-destination structure. Past 4, the chart becomes hard to read.

### Design decisions

**Layout direction.** Most Sankey diagrams flow left to right (matching reading direction). Top-to-bottom is also defensible. Right-to-left and bottom-to-top are unusual and earn explanation costs.

**Node ordering.** Within each column, nodes are typically ordered to minimize crossing flows. D3's `d3-sankey` layout handles this automatically (with some manual adjustment available). Reducing crossings improves readability significantly.

**Color hue.** Each node typically has its own color hue (categorical encoding). Flows can inherit either source's or destination's hue, or use a neutral color. The choice matters for what relationship the reader emphasizes.

**Annotations.** Quantitative labels on the larger flows; tooltip on hover for smaller flows. The largest flows get prominence; the smaller ones remain available to detailed reading.

For Claude Code work: `d3-sankey` is the canonical D3 implementation. Specify it: "use d3.sankey() for layout."

> ### ↳ Dig Deeper — Sankey design choices
>
> **Prompt:**
>
> > Walk me through three Sankey design decisions: node ordering (which algorithm, how to override), flow color (source vs. destination vs. neutral), and quantitative label placement (always vs. above-threshold). For each, name the trade-off. Cite Tufte's proportional ink principle as the constraint that the flow widths must respect.
>
> **What to do with the output:** Save the analysis. The decisions recur in every Sankey project.

---

## Concept 2 — Alluvial diagrams: Sankey across time

An alluvial diagram is a Sankey extended to track category transitions over multiple time points. Voters in election 2020 by party → voters in election 2022 by party → voters in election 2024 by party. The flows show *who shifted to where*.

### When alluvial diagrams work

- Categorical data tracked across multiple time points.
- The transitions (who moved to where) are the primary question.
- 3–6 time points. Past 6, the chart sprawls.

The form generalizes Sankey to longitudinal categorical data. The use cases (voter shifts, student outcome cohorts, customer journey transitions) are specific but consequential.

The pantry's alluvial implementation shows the form. Compare to Sankey: same flow vocabulary, different time structure.

---

## Concept 3 — Chord diagrams

A chord diagram is a circular layout where entities are placed around the circle's perimeter and flows between them are drawn as ribbons (or lines) crossing the interior.

### Two variants

**Ribbon chord** uses width to encode flow magnitude. Like Sankey, the ribbon's width is the magnitude channel. Used for trade flows between countries, message flows between groups, etc.

**Non-ribbon chord** uses lines without width — only the *existence* of a connection matters. Used for relationship networks where the question is "who is connected to whom?" rather than "how much flows."

The distinction matters. The same dataset can produce two different chord diagrams; the choice depends on whether the flow magnitude or the connection existence is the question.

### When chord diagrams work

- Inter-entity relationships within a closed set of entities.
- 5–20 entities. Past 20, the chord lines crisscross unreadably.
- Circular arrangement is acceptable to the reader (some audiences find it harder than left-to-right Sankey).

### Failures

- Too many entities (>20). Chord lines tangle.
- Asymmetric relationships (A→B is a different magnitude than B→A). Chord diagrams handle this with different ribbon ends, but the visual gets complicated.
- Relationships that aren't really cyclical or symmetric (data flows from sources to destinations without back-flows). Sankey is cleaner.

The pantry's chord implementations show both variants. Compare them.

---

## Concept 4 — Arc diagrams: connection-existence in a linear arrangement

An arc diagram places entities along a horizontal line and draws arcs above (or below) the line connecting related entities. The arc height typically has no encoding; only the existence of a connection is visualized.

### When arc diagrams work

- Network data where the structure of connections matters (which nodes are central, which are peripheral).
- Linear arrangement is meaningful (nodes have an order — alphabetical, by category, by connection count).
- Audience prefers a single horizontal layout to a circular one.

### When they fail

- Dense networks. Arcs overlap.
- Networks where connection magnitude matters. Use a Sankey or ribbon chord instead.

The pantry's arc-diagram example shows the form.

---

## Concept 5 — Force-directed graphs: the network as physics

A force-directed graph treats nodes as particles connected by springs (the edges). The layout algorithm runs a physics simulation: connected nodes attract each other; all nodes repel each other; the layout settles into a stable configuration where related nodes cluster.

### When force-directed graphs work

- Networks with non-trivial cluster structure. The clusters become visible as the layout settles.
- Up to ~50 nodes. Larger networks become hairballs.
- Audiences who can read a network diagram (graphicacy required).

### When they fail

- Highly dense networks (every node connects to many others). The hairball failure mode.
- Networks where flow magnitude matters. Force-directed shows existence; not magnitude.
- Reproducibility matters. The simulation has random initial conditions; running the layout twice produces different results. This is fine for exploration; problematic for publication.

### Design decisions

**Edge style.** Curved edges look organic; straight edges are easier to read. Choose based on density.

**Node size.** Can encode a quantitative property (degree centrality, betweenness centrality, node-specific value). Stevens' power law applies.

**Color hue.** Categorical (community membership) or sequential (some node attribute).

**Interaction.** Hover-to-highlight neighbors; click to expand; drag to rearrange. Interactive force-directed graphs work much better than static ones.

For Claude Code work: D3's `d3-force` library handles the simulation. Specify forces: "use forceSimulation() with forceLink, forceManyBody, forceCenter."

The pantry's force-directed example shows the form.

---

## Concept 6 — The hairball problem

The recurring failure mode of network visualization. When a network is too dense or too large, the visual becomes a tangled mass — the "hairball" — where individual nodes and connections cannot be distinguished.

### Why hairballs happen

The Gestalt law of connection produces grouping. When too many connections compete, the grouping breaks down. The chart shows a network exists but reveals no structure.

### Mitigations

**Filter.** Show only the most-connected nodes (top-25 by centrality). Or only nodes within 2 hops of a focal node. Or only edges above a certain weight.

**Cluster.** Use a community-detection algorithm to find groups; visualize the groups as super-nodes; show within-group structure on demand.

**Switch forms.** A matrix view (heatmap of adjacency) is sometimes more readable than a force-directed graph for dense networks. The matrix shows every connection; structure emerges from the row/column ordering.

**Aggregate.** Show the network at a higher level of abstraction. Don't try to show every node; show every cluster.

The hairball is a structural failure, not a design failure. The chart cannot show what it tries to show. The fix is to change what you are trying to show.

---

## Mid-chapter checkpoint

Pick a flow or network context from your work. Identify the primary question: flow magnitude (Sankey/alluvial/chord-with-ribbons) or connection existence (non-ribbon chord, arc, force-directed). Estimate the number of entities and connections. Predict whether the form you would choose risks the hairball.

You should be able to do this in 60 seconds.

---

## Extended worked example — building a Sankey with Claude Code

Take a humanitarian dataset: aid flows from donor countries through implementing organizations to recipient countries. 5 donor countries, 4 implementing organizations, 8 recipient countries. Three columns of nodes; flows between adjacent columns.

### Channel decomposition

- Marks: rectangles (nodes) and bands (flows).
- Position-x: column (donor / implementer / recipient — 3 columns).
- Position-y (within column): node ordering, optimized to minimize crossings.
- Width-of-flow-band: aid magnitude (USD).
- Color hue: donor country (cascading through subsequent flows).

### The four-move prompt

```
**Show what I have:**
Three-column flow data: donor → implementer → recipient. Aid amounts
in USD millions for each donor-implementer pair and each
implementer-recipient pair. Donors: USA, EU, UK, Germany, Japan.
Implementers: UN agencies, ICRC, Red Cross, MSF. Recipients: 8 countries.

**Say what I want:**
Sankey diagram in D3 v7. Single self-contained HTML file with inline
CSS and inline D3 (loaded via CDN). Responsive to window resize.

**Constrain it:**
- Use d3.sankey() for layout.
- Marks: rectangles (nodes), bands (flows).
- Layout direction: left to right.
- Node ordering: d3.sankeyJustify() for default layout.
- Flow width: proportional to aid amount (USD millions).
- Color hue: donor country, cascading through implementer and recipient.
- Annotations: quantitative labels on flows >$50M; tooltip on smaller
  flows.
- Subtitle: "International Humanitarian Aid Flows, FY2024 (USD millions)".
- Margins: top 60, right 200 (legend), bottom 40, left 80.
- Dark mode support.

**Verify:**
Restate the channel decomposition. Then write D3 v7 code with comments
showing which line implements which channel. Verify that flow widths
are proportional (Tufte's proportional ink applies — the band's area
must encode the value; band-width-times-band-height must be proportional
to aid amount).
```

### Audit

Standard Evergreen/Emery plus:

- Flow widths proportional to values (proportional ink).
- Node ordering minimizes crossings.
- Color cascade works (donors visible at all three columns).
- Quantitative labels on the largest flows.

---

## Chapter summary

You can now do four things you could not do before this chapter.

You can build Sankey diagrams, alluvial diagrams, chord diagrams (ribbon and non-ribbon), arc diagrams, and force-directed graphs — choosing the form based on whether flow magnitude or connection existence is the question.

You can apply the Bertin width-as-channel framework to flow charts: when width encodes quantity, the form is a Sankey or ribbon chord; when width is uniform, the form shows topology not flow.

You can recognize the hairball failure mode in dense network charts and apply mitigation strategies (filter, cluster, switch forms to matrix, aggregate).

You can specify a flow chart for Claude Code with the right layout algorithm (`d3.sankey()`, `d3.chord()`, `d3.forceSimulation()`) and the right encoding decisions for the family.

---

## Key terms

- **Sankey diagram.** Flows from sources to destinations; width-as-channel encodes magnitude.
- **Alluvial diagram.** Sankey across multiple time points; tracks category transitions.
- **Chord diagram (ribbon).** Circular layout with magnitude-encoding ribbons.
- **Chord diagram (non-ribbon).** Circular layout with existence-only lines.
- **Arc diagram.** Linear node arrangement with arcs above for connections.
- **Force-directed graph.** Physics simulation; clusters emerge from layout.
- **Hairball problem.** Dense networks visualize as tangled mass; structure invisible.
- **Width-as-channel (Bertin).** Width can encode magnitude; uniform width means existence only.
- **Gestalt law of connection.** Connected elements perceived as same group; mechanism behind force-directed visualization.

---

## Discussion questions

1. The Sankey/chord distinction is layout (linear vs. circular), not channel (both use width for magnitude). What does each layout afford that the other doesn't?
2. Force-directed graphs hide the magnitude question. When is this acceptable; when does it become a Cairo-class moral failure?
3. The hairball problem is structural, not aesthetic. What does this say about whether visualization can solve it?
4. Alluvial diagrams are uncommon. What contexts in your domain would justify them?
5. *Cross-chapter synthesis.* Chapter 12 will introduce flow maps (geographic flow visualization). Frame the relationship between non-spatial flow charts (Chapter 11) and spatial flow maps (Chapter 12).

---

## Exercises

### Warm-up

**Exercise 11.1** — *Form selection.* For each, choose the right flow/network form:
- Aid flows from 5 donors through 3 implementers to 10 recipients.
- Voter shifts between 4 parties across 3 elections.
- Connections between 200 academic researchers (co-authorships).
- Trade between 12 countries (bilateral, asymmetric).
- Co-occurrence of 50 keywords in a corpus.

**Exercise 11.2** — *Sankey vs. chord.* Take a bilateral flow dataset. Build a Sankey and a chord diagram. Compare.

**Exercise 11.3** — *Hairball mitigation.* You have a network of 200 nodes with high connection density. Specify three mitigation strategies.

### Application

**Exercise 11.4** — *Build a Sankey.* Take a real flow dataset. Build with `d3.sankey()`. Audit.

**Exercise 11.5** — *Build a force-directed graph with interaction.* Network data, 20–50 nodes. Add hover-highlight and drag interaction.

**Exercise 11.6** — *Audit a published flow chart.* Find one in a recent publication. Audit using Evergreen/Emery + flow-specific (proportional widths, node ordering).

### Synthesis

**Exercise 11.7** — *Alluvial cohort.* Take longitudinal categorical data (student cohort outcomes, customer state transitions). Build an alluvial diagram.

**Exercise 11.8** — *Network as matrix.* Take a moderately dense network. Build it as both a force-directed graph and a matrix (heatmap of adjacency). Compare.

### Challenge

**Exercise 11.9** — *Sankey with energy data.* Replicate a simplified energy-flow Sankey (sources → transformations → uses) for a real energy dataset.

**Exercise 11.10** — *Multi-level Sankey.* Build a Sankey with 4–5 levels (donor → fund → program → project → outcome). Test how readable it remains at depth.

---

## LLM Exercise — Chapter 11: Flow and Network Charts

```
I have flow or network data of [DESCRIBE: entities, connections,
magnitudes if applicable]. The communication goal is [DESCRIBE].

Walk me through:
1. Confirm flow vs. network family.
2. Identify primary question: flow magnitude or connection existence.
3. Choose form: Sankey / alluvial / chord (ribbon or not) / arc /
   force-directed.
4. If risk of hairball, specify mitigation.
5. Specify channels (width as magnitude channel for Sankey/ribbon;
   uniform width for existence-only).
6. Write four-move Claude Code prompt with appropriate D3 layout
   (d3.sankey, d3.chord, d3.forceSimulation).

Audit using Evergreen/Emery + flow-specific (proportionality, node
ordering, label placement, hairball check).
```

**Connection to previous chapters:** Chapter 1 (width-as-channel from Bertin), Chapter 4 (workflow), Chapter 9 (cross-form proportional encoding).

**Preview of next chapter:** Chapter 12 covers spatial and geographic charts. Where Chapter 11 was about flow between abstract entities, Chapter 12 is flow and pattern across geography.

---

## Visual suggestions

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

## Further reading

- **Sankey, Captain. (1898).** Original paper on energy-flow visualization.
- **Munzner, Tamara. (2014).** *Visualization Analysis and Design.* Section on network visualization.
- **The book's pantry** — `sankey-diagram.html`, `arc-diagram.html`, `chord-diagram.html` (in some implementations).

---

## Tags

flow-charts, network-charts, Sankey, alluvial, chord-diagram, ribbon-chord, arc-diagram, force-directed, hairball, Bertin-width, Gestalt-connection, d3-sankey, d3-force, D3, Claude-Code
