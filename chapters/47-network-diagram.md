# Network Diagram

*Data Integration and Crisis Mappingare the central hubs of the AI ecosystem*

![Network diagram showing AI humanitarian ecosystem with Data Integration and Crisis Mapping as central hub nodes](../images/47-network-diagram.png)
*Figure 47.1 — Data Integration and Crisis Mapping are the central hubs*

## What this chart is

A network diagram (or node-link diagram) encodes relationships between entities as nodes connected by link lines. The perceptual mechanism is spatial proximity — the force-directed layout clusters well-connected nodes together, making dense sub-graphs (communities) visible without explicit labelling. The viewer's eye traces paths between nodes to understand chains of relationship.

Force-directed layouts use a physics simulation: links act as springs pulling nodes together, while a global repulsion force pushes all nodes apart. The resulting position is an energy minimum, not a meaningful coordinate system. Node *position* carries no information — only *topology* (who is connected to whom) and *degree* (how many connections a node has) are encoded.

## Why it was chosen here

The data structure is a tripartite network: three node groups (organisations, technologies, domains) connected by directed and undirected edges of three semantic types. The message is structural — which entities are most connected, which technologies bridge the most domains, and which organisations cluster around the same capabilities.

No matrix, bar chart, or hierarchy encodes this. A chord diagram could show pairwise flows but would lose the tripartite structure. A tree would impose a hierarchy that doesn't exist in the data. The network diagram is the only chart type that lets the clustering emerge from the data structure itself.

## The hairball problem

Network diagrams degrade rapidly with scale. At ~60–80 nodes and high link density, the layout becomes a "hairball" — visually dense, analytically useless. This dataset sits at 21 nodes and 49 links (average degree ~4.7), which is within the legible range.

If your network grows beyond this, the correct alternatives are: an **adjacency matrix** (scales well, loses spatial intuition), a **chord diagram** (shows flow magnitudes between groups), or an **arc diagram** (preserves ordering, reveals clusters through arc density). The network diagram should be the *last* resort, not the first, for large networks.

## Three encoding decisions

**Node size by degree.** Nodes with more connections are larger, making hubs immediately legible without requiring the viewer to count edges. Data Integration and Crisis Mapping visually dominate because they have the highest degree.

**Link color by type.** Three semantic edge types (uses, enables, operates in) are color-coded and styled — directed edges carry arrowheads; "operates in" edges are dashed. Color encodes the relationship type redundantly with style, supporting color-blind users.

**Group color on nodes.** Node fill color encodes group membership (organisation, technology, domain) — the most important categorical distinction in this network.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained network diagram in D3 v7. Two files:

1. `network-diagram.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Network Diagram" and the slide subtitle is "Data Integration and Crisis Mappingare the central hubs of the AI ecosystem".

2. `network-diagram/data.json` — the data file the chart loads via `d3.json("./network-diagram/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Node-link data for a force-directed network diagram. Three node groups form a layered ecosystem: humanitarian organisations, AI/technology capabilities, and operational domains. Links encode which orgs use which technologies and which technologies support which domains.
  - `nodes[].id`: string — unique identifier referenced by links
  - `nodes[].label`: string — full name shown in tooltip
  - `nodes[].short`: string — abbreviated label rendered on the node
  - `nodes[].group`: org | tech | domain — determines node color and base size
  - `nodes[].description`: string — shown in tooltip
  - `links[].source`: string — source node id
  - `links[].target`: string — target node id
  - `links[].type`: uses | enables | operates — semantic relationship type
  - `links[].weight`: number 1–3 — controls link stroke width
  - `links[].directed`: boolean — true renders an arrowhead at the target node

Encoding: use the perceptually honest channel for this chart type (network diagram). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

> Reference implementation: `d3/47-network-diagram.html`

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Jacob L. Moreno** drew the first sociogram in 1934 — a network diagram of which children at a girls' reform school liked or disliked which other children. He coined "sociometry" and laid the foundation for modern social network analysis.

![Jacob L. Moreno, circa 1934. AI-generated portrait based on a public domain photograph.](../images/jacob-l-moreno.jpg)
*Jacob L. Moreno, circa 1934. AI-generated portrait based on a public domain photograph (Wikimedia Commons).*

**Run this:**

```
Who was Jacob L. Moreno, and how does his sociogram work connect to the network diagram we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Jacob L. Moreno"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to describe one of Moreno's 1934 sociograms — what nodes, what edges, what conclusions he drew.
- Ask it about the bridge from Moreno's sociometry to modern computational social network analysis.

What changes? What gets better? What gets worse?
