# Circle Packing

*Crisis Response and Healthcare dominate the AI humanitarian footprint*

![Circle Packing](../images/30-circle-packing.jpg)

Also known as: Bubble Hierarchy · Packed Circles · Circular Treemap

## What this chart type is

Circle packing encodes hierarchy through *containment* and quantitative value through *area* . Each parent circle contains its children; each leaf circle's area is proportional to its data value. The perceptual mechanism is two-channel: spatial containment communicates structure (which things belong together), while area communicates magnitude (which things are larger).

It is a circular variant of the Treemap. The structural encoding — containment — is actually stronger in circle packing than in a Treemap, because nested circles make parent-child relationships spatially unambiguous. The trade-off is **space efficiency** : circles pack poorly, leaving significant void between them. Treemaps fill their bounding rectangle completely.

Circle packing is best used when *hierarchy revelation matters as much as magnitude comparison* — when the viewer needs to immediately understand which items belong together before they compare their sizes.

## How to read this chart

Each **large outer circle** represents a humanitarian domain. Its size reflects the total relative weight of AI applications within that domain. The **smaller nested circles** inside each domain represent individual application areas; their size encodes relative investment or activity level within the domain.

**Colour encodes domain membership** — walnut for Crisis Response, blood-red for Healthcare, grey for Education, mist for Food Security, and sienna for Climate Resilience. Colour is applied at the domain level and inherited by all children, so any circle's domain is identifiable without reading a label.

**Click any outer circle** to zoom in and see its subcategories at full legibility. Click the background or the breadcrumb path to zoom back out. Click a legend item to zoom directly to that domain. **Hover any circle** for the exact value in the tooltip.

## Why circle packing — not treemap

A Treemap would show the same hierarchy with better space efficiency and more accurate area comparison (rectangles are easier to compare than circles). The trade-off: hierarchical structure is harder to read. When branches interlock in a Treemap, the parent boundary can be ambiguous — especially at three or more levels of depth.

Circle packing makes nesting **structurally unambiguous** : a circle is either inside another circle or it is not. There is no visual ambiguity about which parent a child belongs to. This matters here because the domain assignment (Crisis Response vs Healthcare vs Education) is the primary story — the size comparison is secondary.

## Honest limitations

Circle packing is among the **least space-efficient chart types** . The gaps between circles are wasted display area — in a 600×600 canvas, roughly 21% of the space is void even with optimal packing. This limits how many nodes can be shown at a legible size.

**Area comparison is a weak perceptual channel** for circles. Humans are poor at judging the ratio between two circles of similar size — a circle with twice the area does not look twice as large. The chart compensates with interaction (click to zoom, hover for exact values) and with redundant colour encoding by category.

If precise magnitude comparison across all items is the primary goal, a **bar chart or dot plot will outperform circle packing** every time. This chart earns its place specifically when hierarchy revelation is as important as magnitude comparison.

## About this example — AI application landscape in humanitarian work

This chart maps the relative scale of AI-assisted activities across five major humanitarian domains as framed by the **Humanitarians AI** initiative. Each outer circle is a domain; its size encodes the total relative weight of AI application activity within that domain. The nested circles inside each domain represent specific application areas — for example, within Healthcare, the nested circles might include diagnostics support, supply chain optimisation, and disease surveillance.

**Crisis Response** (walnut) and **Healthcare** (blood-red) carry the two largest circles, reflecting the current concentration of AI humanitarian investment in emergency triage, displacement tracking, and diagnostic support. **Education** (grey) and **Food Security** (mist) show mid-tier activity levels. **Climate Resilience** (sienna) is the smallest domain — reflecting that AI climate-humanitarian applications are newer and less deployed than the crisis and health verticals, despite being a growing area.

The zoom interaction resolves the chart's central limitation: at the full view, the five domain sizes are the story. After clicking into any domain, the individual application areas become individually legible, revealing which sub-areas are driving the domain's overall footprint. To substitute real data, replace the `circle-packing/data.json` file with a hierarchical JSON object following the same `name / children / value` schema.

## Prompt

Paste this into Claude Code to generate a working version of this chart, plus its data file. The result will not be a perfect replica — the goal is that the reader can run the prompt, get a chart of this type, and read its source.

```
Generate a complete, self-contained circle packing in D3 v7. Two files:

1. `circle-packing.html` — a full HTML page with inline CSS and inline D3 v7 (loaded from `https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js`). The chart should fill the viewport, be responsive on resize, support keyboard focus on interactive elements, and include a tooltip on hover. The page title is "Circle Packing" and the slide subtitle is "Crisis Response and Healthcare dominate the AI humanitarian footprint".

2. `circle-packing/data.json` — the data file the chart loads via `d3.json("./circle-packing/data.json")`, with a fallback inline literal in the HTML if the fetch fails.

Data shape:
- Hierarchical dataset for circle packing. Each leaf node has a numeric value determining circle area. Parent nodes group leaves into categories. Maximum recommended depth is 3 (root → category → leaf).
  - `name`: string — label displayed inside or beside the circle
  - `value`: number (leaf nodes only) — determines circle area. Omit on parent nodes.
  - `children`: array (parent nodes only) — nested child nodes. Omit on leaf nodes.

Encoding: use the perceptually honest channel for this chart type (circle packing). Do not invent decorative encodings. Annotate the chart with a one-line in-chart subtitle that names what the chart shows. Include an accessibility `<title>` and `<desc>` inside the SVG.

Style: warm monochrome — black, dark walnut, blood-red accents only. Serif font for body text, JetBrains Mono for labels and controls. No drop shadows, no rounded corners, no gradients. Clean editorial register suitable for a print-ready textbook page.

Provide both files as separate code blocks. Do not explain — just produce the files.
```

The original code and data — copy-paste-ready — live at [bearbrown.co](https://www.bearbrown.co/).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Johannes Kepler** conjectured in 1611 that no arrangement of equal-size spheres in three dimensions could pack more densely than the face-centered cubic — the stacked-cannonball arrangement. The conjecture was finally proven by Thomas Hales in 1998. Every modern circle-packing layout, from sunburst files to bubble enclosures, is wrestling with the descendant of Kepler's question: how tightly can you pack circles into a container before they overlap?

![Johannes Kepler, circa 1610. AI-generated portrait based on a public domain engraving.](../images/johannes-kepler.jpg)
*Johannes Kepler, circa 1610. AI-generated portrait based on a public domain engraving (Wikimedia Commons).*

**Run this:**

```
Who was Johannes Kepler, and how does his sphere-packing conjecture connect to the circle-packing layout we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Johannes Kepler conjecture sphere packing"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through what the Kepler conjecture says about *equal-size* spheres versus what a circle-packing chart faces with *variable-size* circles encoding data.
- Ask it to compare the 1611 Kepler conjecture with the 1998 Hales proof — what changed about how mathematicians validate geometric claims.

What changes? What gets better? What gets worse?
