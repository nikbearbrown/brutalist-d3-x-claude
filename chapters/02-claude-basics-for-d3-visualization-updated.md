# Chapter 02 — Claude Basics for D3 Visualization

*The gap between "make a chart" and "make the chart" is the whole problem.*

---

It is 2:14 PM. You have eight numbers — cognitive domain scores, 0 to 100. Your colleague needs a chart by 3:30. You open Claude Code and type:

> "Make a chart showing AI capability across cognitive domains."

Claude Code returns a working D3 visualization in about four seconds. It is a scatterplot. Each cognitive domain is a colored circle floating in a square frame. The scores are encoded by circle size. The domains are distinguished by hue. The chart is technically a chart. You cannot read it.

You try to rank the domains by eye. You can't. Size is a terrible channel for ranking — the human visual system handles position well and area badly. The colors require staring at a legend. The spatial layout communicates nothing at all. You have a chart. You do not have information.

You write a different prompt:

> "Vertical bar chart of AI capability scores across 8 cognitive domains. x-position encodes domain (categorical, sorted by score descending). y-position from a zero baseline encodes score (quantitative, range 0–100). Color luminance encodes score as a redundant sequential encoding. x-axis labels rotated -30°. Score values shown above each bar. D3 v7, single HTML file, responsive."

Claude Code returns a working bar chart, sorted, annotated, on a zero baseline, with redundant luminance, in 60 lines of D3. You read the ranking in a quarter-second. You send it to your colleague at 2:18.

<!-- → [INFOGRAPHIC: side-by-side comparison of the two prompts — left column is the vague prompt with annotations flagging each decision Claude Code had to make on its own (chart type, marks, channels, sort order, baseline); right column is the specific prompt with the same decision points labeled as author-controlled. Caption: "Every decision the vague prompt omits is a decision the model makes for you."] -->

![Figure 2.1 — Every decision the vague prompt omits is a decision the model makes for you](../images/02-claude-basics-for-d3-visualization-fig-01.jpg)

| | **Property** | **Value** |
|---|---|---|
| **Row 1** | _fill in_ | _fill in_ |
| **Row 2** | _fill in_ | _fill in_ |

: {.infographic-table}


The difference between those two prompts is not length, and it is not politeness. It is **specificity**. The first prompt told Claude Code to make a chart. The second told Claude Code *which* chart, *which* marks, *which* channels, *which* constraints. The model did not decide these things. You did.

That gap — between letting the model decide and deciding yourself — is the entire subject of this chapter. The rest of the book gives you the vocabulary to close it for every chart type, every dataset, every communication goal. This chapter teaches you the machinery that makes the vocabulary useful.

---

## Where Claude lives

Claude runs in several products. They all use the same underlying model, but they differ in what they can see and what they can do. For D3 work, the distinctions matter.

**Claude Code** is a command-line interface where Claude can read files in your project directory, write new ones, execute shell commands, and iterate. This is the right tool for building charts. D3 produces files — HTML, JS, CSS — and Claude Code can read your project's reference examples, write new chart files, and revise them without you copying and pasting anything. Most exercises in this book assume Claude Code.

**Claude.ai chat** (web or desktop) is the universal interface. It has no file-system access. Everything you want Claude to see, you paste. For a one-off question — "does a Sankey diagram make sense for this dataset?" — that is fine. For a workflow that produces a dozen charts across multiple sessions, it becomes friction fast.

**Claude Projects** is a feature inside Claude.ai that gives you a persistent context — reference files you attach once stay in scope for every conversation in that project. Useful if you are working in chat and want your channel framework, your design constitution, or your worked examples available without pasting them every time.

**Cowork** is a Claude desktop feature with supervised access to your file system. It handles multi-step file workflows well: read data from a CSV, generate a chart HTML, save the result. For single-file D3 chart generation, Claude Code is faster.

The general rule is simple: if the task produces a file, use Claude Code. If the task produces a conversation, use Claude chat. If the task spans files across many sessions, use a Project.

| Product | File-system access | Persistent context | Best for | Typical D3 use case |
|---|---|---|---|---|
| Claude Code | Yes | Yes (in project memory) | Building, iterating, and shipping chart code | Generating `chart.html` from a CSV, watching it render, asking for the next revision |
| Claude.ai (web) | No | No (per conversation) | Sketching prompts and explaining concepts | Drafting a four-move prompt before pasting it into Claude Code |
| Claude in Chrome | Page DOM only | No | Inspecting an existing chart on the web | Asking "what's wrong with this chart?" while looking at it |
| Claude API | Whatever you wire up | Whatever you persist | Programmatic pipelines — batch chart generation, build scripts | Generating 50 small multiples from a script |
*Figure 2.2*

| | **Property** | **Value** |
|---|---|---|
| **Row 1** | _fill in_ | _fill in_ |
| **Row 2** | _fill in_ | _fill in_ |

: {.infographic-table}


---

## The instruction budget, and why two files beat one

Here is something most people don't know when they first start working with Claude Code: every session begins with a hidden cost you don't control.

Claude Code loads its own system prompt at the start of every session — Anthropic's instructions about how to behave as a coding agent. That system prompt consumes approximately 50 of the roughly 150–200 behavioral rules the model can reliably track at once. Think of it as a budget. You don't see the first 50 line items. You only get to spend the rest.

This has a direct consequence for how you design your session context.

A `CLAUDE.md` that runs to 400 lines — D3 version rules, naming conventions, a 20-color palette with hex values, spacing scale, dark-mode behavior, voice and tone guidance, typography stack, responsive breakpoints, component rules for cards and shadows — is a file that exceeds the remaining budget. The later rules don't vanish. But they degrade. Claude Code holds the first hundred instructions clearly; the ones that appear later are tracked with decreasing reliability. The degradation is silent. You won't get an error. You'll get a chart that almost follows the rules.

The solution is not to write a shorter `CLAUDE.md`. It is to recognize that not everything belongs in `CLAUDE.md` in the first place.

**`CLAUDE.md` is your coding constitution.** It contains everything that governs how code gets written: D3 version policy, naming conventions for SVG IDs and CSS classes, what Claude Code must not do without explicit instruction, the prompt structure you use for every chart, accessibility standards, transition vocabulary. These rules apply to every session. Load them every session.

**`DESIGN.md` is your visual constitution.** It contains everything the designer needs and the coder doesn't: the color palette with hex values and semantic roles, the typography stack, the spacing scale, dark-mode palette behavior, responsive breakpoints, component rules. For most chart-building sessions — the ones about scales, data joins, axis ticks, transitions — these rules are irrelevant. Loading them wastes 40–60 instruction slots on constraints that don't apply to the work at hand.

`DESIGN.md` loads on demand. When a session involves visual design decisions — picking a palette for a new series, specifying dark-mode behavior for a dashboard, reviewing whether a chart's type treatment matches the site's typography — you load it explicitly. When a session is about whether `.join()` is the right pattern for this data update, you don't.

```
CLAUDE.md     → loads every session
DESIGN.md     → loads when visual decisions are in scope

Together:  ~100–150 instructions, within budget.
Merged:    ~200+ instructions, budget exceeded, later rules degraded.
```

