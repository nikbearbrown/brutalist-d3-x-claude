# Chapter 00 — Claude Basics for D3 Visualization

## Three suggested titles

- Claude Basics for D3 Visualization: The Tool, the Pitfalls, the Discipline
- Working With Claude Code on Charts: Four Moves That Make It Work
- The Specification Skill That Makes Claude Code Useful

## Chapter overview

By the end of this chapter you will know how to work with Claude (specifically Claude Code) on D3 visualization tasks productively. You will know the four-move prompt structure that turns vague requests into working charts, the failure modes specific to D3 generation that you should expect and verify against, the multi-LLM comparison strategy that catches what one model misses, and the verification habit that prevents you from publishing charts whose plausibility outran their accuracy. You will also know why every Claude Code D3 session begins with two files — not one — and what each file is for. The methods here apply to every chapter of this book and to every chart you build outside of it.

## Learning objectives

1. **(Apply)** Choose between Claude Code, Claude chat, a Claude Project, and Cowork for a given D3 task, justifying the choice based on whether the task requires file manipulation, persistent context, or quick iteration.
2. **(Apply)** Write a four-move prompt (show, say, constrain, verify) for a D3 chart that is precise enough to produce a usable output on the first attempt.
3. **(Analyze)** Diagnose three failure modes specific to D3 generation: API hallucination (Claude Code uses syntax that is not actually in D3 v7), chart-type mismatch (Claude Code chooses a chart that does not answer the communication question), and channel mismatch (Claude Code encodes a quantitative attribute on an identity channel).
4. **(Evaluate)** Apply the three-layer verification stack (sanity-check the format, check specific facts, test the work) to any Claude-Code-generated D3 chart before using it.
5. **(Create)** Produce two session-context files — `CLAUDE.md` (coding constitution) and `DESIGN.md` (visual constitution) — and explain why they must remain separate.

## Opening case — why specificity is the skill

It is 2:14 PM. You have a dataset on your screen — eight cognitive domains, each with an AI capability score from 0 to 100. Your colleague needs a chart by 3:30 for a research summary. You open Claude Code. You type:

> "Make a chart showing AI capability across cognitive domains."

Claude Code returns a working D3 visualization. It is a scatterplot. Each cognitive domain is a colored circle floating in a square frame. The x-axis and y-axis are unused. Score is encoded by circle size, domain by color hue. The chart is technically a chart. You cannot read it. The scores are nearly impossible to rank by eye; the colors require staring at a legend; the spatial layout communicates nothing about the data.

You did not get the chart you wanted. You got the chart Claude Code understood you to mean. The gap is the chapter.

You write a different prompt:

> "Vertical bar chart of AI capability scores across 8 cognitive domains. x-position encodes domain (categorical, sorted by score descending). y-position from a zero baseline encodes score (quantitative, range 0–100). Color luminance encodes score as a redundant sequential encoding. x-axis labels rotated -30°. Score values shown above each bar. D3 v7, single HTML file, responsive."

Claude Code returns a working bar chart, sorted, with annotations, on a zero baseline, with redundant color luminance, in 60 lines of D3. You read the ranking in a quarter-second. You send it to your colleague at 2:18.

The difference between the two prompts is not politeness. It is not length. It is **specificity**. The first prompt was vague: make a chart. The second was specific: vertical bar chart, x-position for domain (categorical, sorted), y-position from zero for score (quantitative), color luminance redundantly encoding score.

Specificity is the skill. The book teaches the vocabulary that makes the specificity possible. This chapter teaches how to use Claude Code with that vocabulary.

## Concept 1 — Where Claude lives, and which version to use

Claude is available in several products that all run the same underlying model but differ in what they can see and do. For D3 work specifically:

**Claude Code** (recommended primary tool for this book). A command-line interface (and IDE integrations) where Claude can read files in your project, write new files, run shell commands, and iterate on code. This is the right tool for D3 work because D3 produces files (HTML, JS, CSS) and Claude Code can read the working examples in your project's pantry, write new chart files, and iterate. Most LLM Exercises in this book assume Claude Code as the primary tool.

**Claude.ai chat** (web, desktop, mobile). Universal browser-based access. Good for quick questions, prompt iteration, exploratory dialogue. The weakness for D3 work: you have to paste data, paste reference code, paste each iteration. Anything more than a one-off chart benefits from Claude Code's file access.

**Claude Projects** (claude.ai feature). A persistent context for a long-running project. You can attach reference files (the channel framework from Chapter 1, the Evergreen/Emery checklist, your `CLAUDE.md`) once, and they stay in context for every conversation in the Project. Useful for Part II's chart-by-chart march if you are using web chat instead of Claude Code.

**Cowork** (Claude desktop feature). Claude with access to your file system in a constrained, supervised way. Useful for tasks that span multiple files (reading data from a CSV, generating a chart HTML, saving the result). Cowork's strength is multi-step file workflows; for single-file D3 chart generation, Claude Code is generally faster.

**Claude in Chrome.** Useful when you want Claude to read a web page (a published chart, an Observable notebook, a D3 tutorial) and discuss what you are seeing. Less useful for generation; more useful for analysis of existing work.

### When to use which

Most LLM Exercises in this book recommend Claude Code as the primary tool. The exceptions:

- Exploratory questions about a dataset before you build a chart — use Claude chat. Quick, conversational, no file overhead.
- The audit step (channel decomposition, sort order, color decisions) before you write the prompt — use Claude chat or a Claude Project. The audit is dialogue; the build is execution.
- Multi-LLM comparison (described in Concept 4) — use the relevant LLM's primary interface (ChatGPT for OpenAI, Gemini for Google, Claude chat for Anthropic) to compare framings.
- Reading a long reference document (one of the pantry's reference docs) — use Claude.ai with the file attached, or use Claude Code with the file in your project directory.

The general rule: if the task produces a file, use Claude Code. If the task produces a conversation, use Claude chat. If the task spans multiple files and persistent context, use a Claude Project (in chat) or Cowork (with files).

### The instruction budget: why CLAUDE.md must stay lean

Here is something most people don't know about Claude Code: every session starts with a hidden instruction cost you don't control.

Claude Code loads its own system prompt at the start of every session — the instructions baked in by Anthropic about how to behave as a coding agent. That system prompt consumes approximately 50 of the roughly 150–200 instructions Claude can reliably track at once. Think of it as a budget: the model can hold about 150–200 discrete behavioral rules in active attention. Claude Code's own wiring uses the first 50. That leaves you approximately 100–150 instructions for your project context.

This has a direct consequence for how you design your session-context files.

A `CLAUDE.md` that runs to 400 lines — D3 version rules, naming conventions, color palette with 20 hex values, spacing scale, dark-mode behavior, voice and tone guidance, typography stack, responsive breakpoints, component rules for cards and shadows — is a file that exceeds the remaining budget. The later rules don't get ignored entirely, but they get degraded: Claude Code holds the first 100 instructions clearly and handles the rest with decreasing reliability.

The solution is not to write a shorter `CLAUDE.md`. The solution is to recognize that not everything belongs in `CLAUDE.md` in the first place.

### CLAUDE.md versus DESIGN.md: two files, two jobs

`CLAUDE.md` is your **coding constitution**. It loads every session because coding decisions apply to every session. For D3 work: D3 version policy, naming conventions for SVG IDs and CSS classes, what Claude Code must not do without explicit instruction, the four-move prompt template, accessibility standards, transition and easing vocabulary. These rules govern *how code gets written*. A D3 chart-building session always touches them.

`DESIGN.md` (or `.claude/skills/design/SKILL.md`, following the Brutalist skill convention) is your **visual constitution**. It contains everything the designer needs and the coder doesn't: color palette with hex values and semantic roles, typography stack, spacing scale, dark-mode palette behavior, responsive breakpoints, component rules for cards, shadows, borders, and corner radii, voice and tone guidance. For D3 work specifically, most chart-building sessions — the ones about scales, data joins, axis ticks, transitions — never touch the design system at all. Loading the full design specification every session wastes 40–60 instruction slots on rules that don't apply.

`DESIGN.md` is loaded **on demand**, not by default. When a session involves visual design decisions — picking a palette for a new chart series, specifying dark-mode behavior for a dashboard, reviewing whether a chart's type treatment matches the site's typography — you load `DESIGN.md` explicitly. When a session is about whether `.join()` is the right pattern for this data update, you don't.

The split is a consequence of the instruction budget, not a style preference. Two files with clear separation of concerns keep both files within the budget and keep each session fast.

```
CLAUDE.md          → loads every session
DESIGN.md          → loads when visual decisions are in scope

Together: ~100-150 instructions, within budget.
Merged:    ~200+ instructions, budget exceeded, later rules degraded.
```

A note on naming. `DESIGN.md` is the convention used in this book. If your project follows the Brutalist skill directory convention, the same file lives at `.claude/skills/design/SKILL.md` and is referenced by name in your prompts when needed. The naming is less important than the principle: the design context is a separate file that loads separately.

### Common misconceptions

**"Claude Code is just chat in a terminal."** Claude Code can read your project files, edit them, run commands, and iterate without you copying and pasting. For a workflow that produces dozens of D3 files, the file-system access is not a minor convenience — it is the workflow.

**"You should always use the most powerful tool."** No. A one-off question about whether a chart type fits a dataset is a Claude chat task. Spinning up Claude Code, opening a project directory, running a prompt — that is friction for a question that has a one-paragraph answer.

**"One big CLAUDE.md is better than two smaller files."** No. The instruction budget is real. A merged file that exceeds ~150 instructions produces a session where the later rules are degraded silently. Two focused files — coding constitution and visual constitution — keep both within budget and let you load only what the session requires.

**"Claude in different products produces different output."** It produces output adapted to the available context. The underlying reasoning is the same. The difference is what Claude can see and do, not how Claude thinks.

## Concept 2 — The four-move prompt structure

A productive prompt for D3 chart generation has four parts. They do not have to be separate paragraphs, but every good prompt hits all four.

**Move 1: Show what you have.** Paste the data structure. Describe the columns and types. If you have a sample, paste a few rows. If the data is in a file Claude Code can read, name the file. If you have a reference chart in the pantry, name it.

> "Eight rows. Each row has `domain` (string, 12–17 characters) and `score` (number, 0–100). Sample: Pattern Recognition, 94 / Language, 87 / Memory Retrieval, 96."

**Move 2: Say what you want.** Name the chart type and the marks. Specify D3 version. Specify the deliverable format (single HTML file, ES module, React component).

> "Vertical bar chart in D3 v7. Single HTML file with inline CSS and inline D3 (loaded via CDN). Responsive to window resize."

**Move 3: Constrain it.** Name the channel-to-attribute mappings (Chapter 1's framework). Name the design constraints (zero baseline, sort order, label rotation, color scale type, color palette endpoints). Name the layout (margins, padding, corner radius if relevant). Name accessibility decisions (color-blind safety, ARIA labels, focus states).

> - x-position: domain (categorical, sorted by score descending).
> - y-position from zero baseline: score (quantitative, range 0-100). Zero baseline non-negotiable.
> - Color luminance redundantly encoding score, sequential pale-to-dark.
> - y-axis ticks at 0, 25, 50, 75, 100.
> - x-axis labels rotated -30°.
> - Score value text above each bar.
> - Margins: top 60, right 40, bottom 80, left 60.
> - Dark mode support via prefers-color-scheme media query.

**Move 4: Ask for verification.** Request reasoning. Ask Claude Code to restate what it understood before writing code. Ask for the channel decomposition to be commented in the code. Ask for any decisions not specified to be flagged.

> "Before writing the code, restate the channel decomposition in your own words to confirm. Then write the D3 v7 code with comments showing which line implements which channel. After the code, list any decisions you made that are not specified above (font choice, exact axis tick formatting) so I can confirm or override them."

The four-move structure is the single highest-leverage thing this chapter teaches. Every LLM Exercise in this book uses it. Every chart you build for the rest of your career, if you adopt the discipline, can use it. The four moves take perhaps 90 seconds longer to write than a vague prompt, and they reliably produce charts that are right on the first attempt.

### What changes for D3 specifically

The four-move structure works for any AI-assisted code task. For D3 specifically, three additional notes:

**Always specify the D3 version.** D3 v3 (2013), v4 (2016), v5 (2018), v6 (2020), and v7 (2021) have substantial syntactic differences. Claude Code can produce code that mixes versions if the prompt is ambiguous. Default to v7 (the current major version as of this writing). If you are working in a project with a pinned older version, name it explicitly: "D3 v6 syntax, no v7-only methods."

**Specify the rendering target.** A single self-contained HTML file is one option. An ES module that exports a chart-rendering function is another. A React component is a third. An Observable notebook cell is a fourth. The choice affects what Claude Code generates around the D3 itself.

**Name the data-loading method.** Inline data (paste it in), CSV from a URL, JSON from a file, an Observable AttachedFile — each requires different boilerplate. If the data is small (the AI capability example fits in a few lines), inline is simplest. If the data is large or live, specify the loading method explicitly.

> ### ↳ Dig Deeper — A vague prompt vs. a specific prompt, side by side
>
> **Prompt:**
>
> > Take a real dataset I work with (or invent one if I haven't named one). Generate two Claude Code prompts for a chart of that dataset: one vague ("make a chart of this") and one fully specified using the four-move structure. For each prompt, predict what Claude Code will produce. Then explain why the specific prompt's output is more likely to be usable on the first attempt, citing the marks-and-channels framework as the reason specificity works.
>
> **What to do with the output:** Save the comparison. Use the specific version as a template for your own work. The pattern repeats in every later chapter.

## Concept 3 — Three failure modes specific to D3 generation

Generic LLM failure modes (hallucination, smoothing of disagreement, hidden framings) apply to D3 work as they do to any other domain. Three D3-specific failure modes deserve their own attention.

### Failure 1: API hallucination

Claude Code occasionally produces D3 syntax that is not valid in the version you are targeting. Common manifestations:

- Mixing v6 and v7 syntax. v6 had `d3.scaleOrdinal().domain([])`; v7 added some methods that v6 doesn't have. A mixed-version output runs in neither environment cleanly.
- Inventing methods. Claude Code occasionally produces a call like `d3.scaleSequential().interpolator(d3.interpolateMagical)` where `interpolateMagical` is not actually an exported function. The error appears at runtime as `d3.interpolateMagical is not a function`.
- Misusing data joins. D3's enter-update-exit pattern has changed across versions. Code that uses pre-v6 join syntax (`.enter().append().merge(update)`) does not match the v6+ `.join()` shorthand. Claude Code occasionally mixes them.

**The fix.** Specify the D3 version explicitly in the prompt. Read the generated code's `import` or CDN reference to confirm the version. Run the code (don't accept it without running it). When errors appear, paste the error message back to Claude Code with the version reminder.

### Failure 2: Chart-type mismatch

Claude Code chooses a chart that is technically valid for the data but does not answer the communication question. This is less an API failure than a framework failure — the prompt did not specify the question precisely enough.

Common manifestations:

- The communication question implies a comparison; Claude Code returns a scatterplot.
- The data is part-to-whole; Claude Code returns a multiset bar chart that loses the proportion.
- The data is hierarchical with irregular depth; Claude Code returns a treemap (which assumes regular depth) instead of circle packing.

**The fix.** Specify the chart type in Move 2. Do not let Claude Code choose. The book's chart selection framework (Chapter 2) gives you the vocabulary to commit to a chart type before the prompt runs. Once the chart type is named, Claude Code becomes much more reliable.

### Failure 3: Channel mismatch

Claude Code encodes a quantitative attribute on an identity channel (typically hue), or an identity attribute on a magnitude channel (typically position-implying-order). The chart looks fine. It reads wrong.

Common manifestations:

- A scatterplot where hue encodes a third quantitative variable. The reader cannot rank the third variable; only categorical comparison is possible.
- A bar chart where bar color is a sequential gradient applied to category labels (which have no inherent order). The gradient implies an order the data does not have.
- A choropleth where color hue (rather than luminance) encodes a sequential variable. Hue does not have an inherent ordering; the reader cannot rank states by hue alone.

**The fix.** Specify the channel-to-attribute mapping in Move 3. Use the Chapter 1 vocabulary explicitly: "x-position encodes [attribute] (categorical/quantitative)," "color luminance redundantly encodes [attribute] (sequential)," "color hue encodes [attribute] (categorical, identity channel)." When Claude Code produces the chart, audit it: is the mapping the prompt specified actually what you see? If not, the follow-up prompt names the channel-theory violation.

> ### ↳ Dig Deeper — Audit a Claude Code output you have lying around
>
> **Prompt:**
>
> > I have a Claude-Code-generated D3 chart that I'm not sure is right. [Paste the prompt and the resulting code, or describe the chart.] Walk me through the three failure modes from Chapter 00 — API hallucination, chart-type mismatch, channel mismatch. Diagnose any present in this output. For each, specify the fix as a follow-up prompt.
>
> **What to do with the output:** Apply the fixes. Save the audit pattern as your default review process for any future Claude Code chart output.

## Concept 4 — Multi-LLM comparison

A specific use case worth knowing: comparing responses across different LLMs.

The major LLMs you will likely have access to: Claude (Anthropic), ChatGPT (OpenAI), and Gemini (Google). Other systems exist; the three above are the most widely used as of this writing.

The systems are similar enough that, on most chart-generation tasks, their outputs converge — same channels, similar D3, comparable accessibility decisions. They differ in characteristic ways:

- Claude tends toward more cautious framings and more explicit acknowledgment of uncertainty. Asked "what chart should I use here," Claude will often offer two candidates and the criteria for choosing between them.
- ChatGPT tends toward more confident framings, sometimes recommending a chart type without naming the trade-offs.
- Gemini's behavior varies more depending on the version.

These tendencies shift as the systems are updated. The point is not to pick the best LLM (the best one for chart generation is the one that produces the chart you want for your task) but to use the differences strategically.

### Targeted multi-LLM comparison

The productive use of multi-LLM comparison is **targeted**: when an LLM gives you a response that seems suspiciously confident, or that seems to skip considerations you expected, ask another LLM the same question. Where they agree, the answer is more likely supported. Where they disagree, you have identified a question worth investigating.

For D3 generation specifically, two cases where multi-LLM comparison is high-leverage:

**Chart selection (Chapter 2).** Asked "which chart type should I use for this dataset and communication goal," LLMs sometimes anchor on the most familiar form rather than the best. Asking two or three LLMs reveals when one anchored differently. The variation flags genuine choice points the single-LLM answer would have hidden.

**Accessibility decisions (Chapter 14).** Color palette choices, ARIA labeling, focus states, color-blind safety — different LLMs prioritize these differently. Comparing outputs surfaces decisions you might not have considered.

For routine chart-building, single-LLM use is fine. Save the multi-LLM comparison for moments when the choice is contestable.

## Concept 5 — The three-layer verification stack

Every chart Claude Code produces gets three checks before you ship it. The checks layer:

**Layer 1: Sanity-check the format.** Did Claude Code produce what you asked for? You asked for a single HTML file; you got a single HTML file. You asked for D3 v7; the CDN reference says v7. You asked for inline CSS; the CSS is inline. Format check takes 10 seconds and catches the obvious mistakes.

**Layer 2: Check specific facts.** The data values in the chart match the data values you provided. The axis labels are spelled correctly. The color palette uses the colors you specified. The encoding matches what you asked for (sort by score descending; zero baseline; color luminance for score, not hue). For Layer 2, you read the chart against the prompt.

**Layer 3: Test the work.** Open the HTML in a browser. Resize the window. Test in dark mode. Test with a color-blind simulator (Sim Daltonism for macOS, Coblis online). Read the chart at the size it will be deployed (dashboard tile, full-screen presentation, mobile). The Layer 3 check is the one that catches the failures the prompt didn't anticipate.

For routine chart work, do all three layers. Do them in order. The full verification takes maybe two minutes for a static chart. It will save you from publishing the chart that looked fine in your prompt and broke at the size your reader actually saw it.

### What goes wrong without verification

The opening case from this chapter's introduction is the failure mode in miniature. Claude Code produced a scatterplot that looked like a chart of cognitive domain scores. Layer 1 would have noticed — you asked for a chart and got a chart, format pass. Layer 2 would have caught it — the channel mapping (size for score, hue for domain) does not match what the prompt would have specified if the prompt had specified it. Layer 3 would have confirmed — opening the chart in a browser and trying to read the ranking would have made the failure obvious in two seconds.

In the rewritten prompt, the same checks pass: the format is right, the channels match the specification, and reading the chart in a browser confirms it. The verification stack is what closes the gap between "Claude Code generated something" and "I am confident in shipping this chart."

## Worked example — the Chapter 1 LLM Exercise, walked through

Take the Chapter 1 LLM Exercise as a reference workflow. The exercise produces a channel audit document and a Claude Code prompt for a chart.

### Step 1 — Open the right tool

You are about to produce a working chart and write a markdown audit document. The deliverables are files. Use Claude Code, opened in your project directory.

### Step 2 — Submit the audit prompt

```
I have a dataset of 8 cognitive domains and a quantitative AI capability
score per domain (0-100). The communication goal is: which cognitive
domains have the largest AI capability gaps?

Walk me through the marks-and-channels analysis using the
Bertin / Cleveland & McGill / Munzner framework:

1. Identify each data attribute and classify as categorical, ordered,
   or quantitative.
2. Identify the most important attribute given the communication goal.
3. Recommend a chart type by applying Munzner's expressiveness and
   effectiveness principles.
4. Specify the marks and channel-to-attribute mappings precisely enough
   that the chart could be built from the specification alone.
5. Flag any channel used redundantly. Justify the redundancy.

Then write a single Claude Code prompt for the chart following the
four-move structure. Save the audit as
chapter-01-channel-audit.md.
```

### Step 3 — Read the audit

Claude Code returns a markdown audit document. Read it. Confirm the channel decomposition matches what Chapter 1 taught:

- Score is quantitative; it should be on position (highest-ranked magnitude channel).
- Domain is categorical; x-position is appropriate.
- Color luminance can redundantly encode score (acceptable).
- Hue should not encode score (would be a channel mismatch).

If anything in the audit is wrong, push back: "The audit recommends color hue for score. Score is quantitative; hue is an identity channel. Revise."

### Step 4 — Take the four-move prompt and submit it

The audit produces a Claude Code prompt. Submit it. Claude Code returns an HTML file with the chart.

### Step 5 — Run the verification stack

Layer 1 (format): Single HTML file? D3 v7? Inline CSS? ✓

Layer 2 (facts): Data values correct? Axis labels right? Sort order descending by score? Zero baseline? ✓

Layer 3 (test): Open in a browser. Resize. Dark mode. Color-blind simulator. Compare to the bar-chart.html in the pantry — does your chart match the design intent?

If all three layers pass, save the chart. Move on. If anything fails, write the follow-up prompt naming the failure and the channel-theory violation it implements.

### What this teaches

The pattern — audit, prompt, build, verify — is the model for every LLM Exercise in this book. It is also the pattern Brutalist names: Phase A (audit), Phase B (schema, in this case the audit document), Phase C (generate), Phase D (verify). Phase E (handoff) is the publishing step we will revisit in Chapter 15.

The pattern is not optional. It is the discipline that makes Claude Code reliably useful for chart work. Without the audit, Claude Code produces charts on guesses. Without the verification, you publish charts on hope.

## Chapter summary

You can now do six things you could not do before this chapter.

You can choose between Claude Code, Claude chat, Claude Projects, and Cowork for a given D3 task — and you know that for chart-building work, Claude Code's file access is the right default.

You can write a four-move prompt (show, say, constrain, verify) that turns "make a chart of this" into a precise specification Claude Code can execute on the first attempt. The four-move structure is the single highest-leverage skill this chapter teaches.

You can diagnose three failure modes specific to D3 generation: API hallucination (mixed-version syntax), chart-type mismatch (a valid chart that doesn't answer the question), channel mismatch (quantitative attribute on identity channel or vice versa). Each failure has a specific fix; each fix is one follow-up prompt.

You can apply targeted multi-LLM comparison strategically — using disagreement among LLMs as a signal for where to dig deeper, not as a default workflow.

You can run the three-layer verification stack on any Claude-Code-generated D3 chart: sanity-check the format, check specific facts, test the work in a browser. Done in this order, the verification takes two minutes and catches the failures that would otherwise ship.

And — new to this chapter — you understand why every Claude Code D3 session begins with two files rather than one. `CLAUDE.md` is the coding constitution: it loads every session because code decisions apply to every session. `DESIGN.md` is the visual constitution: it loads when visual decisions are in scope, and stays out of the way when they aren't. The split is a consequence of the instruction budget. This chapter produced both artifacts. That distinction carries forward to every subsequent chapter.

The thing to watch for, going forward, is the temptation to skip the verification. Claude Code produces fluent, confident-looking output. The output is sometimes wrong in ways that are not visible until the chart is in front of a reader. The verification is the discipline that prevents the second outcome.

## Key terms

- **Claude Code.** A command-line interface (and IDE integration) where Claude can read project files, write new files, run commands, and iterate on code. Recommended primary tool for D3 work.
- **Claude Project.** A persistent context for a long-running project in claude.ai. Reference files attached once stay in context for every conversation.
- **Cowork.** Claude desktop feature with constrained, supervised access to your file system. Useful for multi-step file workflows.
- **Four-move prompt structure.** Show what you have, say what you want, constrain it, ask for verification. The high-leverage prompt format for D3 generation.
- **Instruction budget.** The approximate limit (~150–200 instructions) of behavioral rules Claude can reliably track in a session. Claude Code's own system prompt consumes ~50, leaving ~100–150 for project context. The budget is the reason `CLAUDE.md` must stay lean and `DESIGN.md` must stay separate.
- **`CLAUDE.md`.** The coding constitution: D3 version policy, naming conventions, what Claude Code must not do, the four-move prompt template, accessibility standards, transition vocabulary. Loads every session.
- **`DESIGN.md`.** The visual constitution: color palette with hex values and semantic roles, typography stack, spacing scale, dark-mode behavior, responsive breakpoints, component rules. Loads on demand, when visual decisions are in scope.
- **API hallucination.** Claude Code produces D3 syntax that does not exist in the targeted version. Failure mode 1.
- **Chart-type mismatch.** Claude Code chooses a chart that is technically valid but does not answer the communication question. Failure mode 2.
- **Channel mismatch.** Claude Code encodes an attribute on a channel inappropriate to its type (quantitative on hue; categorical on position-implying-order). Failure mode 3.
- **Three-layer verification stack.** Sanity-check the format, check specific facts, test the work. Applied in order before any chart ships.
- **Targeted multi-LLM comparison.** Asking two or three LLMs the same question only when the choice is contestable. Not a default workflow; a strategic tool.

## Discussion questions

1. The book's argument is that Claude Code has dissolved the implementation barrier in D3 visualization. What barrier remains, and why is the remaining one harder to dissolve?
2. The four-move prompt structure asks you to write longer prompts than feel natural. When is this overhead justified, and when is a shorter prompt actually more efficient?
3. The three failure modes named in Concept 3 are specific to D3 generation. Which would you expect to encounter most often in your own work, and why?
4. Multi-LLM comparison is named as a targeted tool, not a default workflow. What is the cost of using it as a default, and when does the cost become worth paying?
5. The instruction budget argument says that merging `CLAUDE.md` and `DESIGN.md` into one file degrades the later rules silently. What would you use as evidence that degradation was actually happening — what observable failure mode would it produce?
6. *Cross-chapter synthesis.* The verification stack in this chapter overlaps with the design audit framework in Chapter 14. Frame the relationship: what does the verification stack do that the design audit doesn't, and vice versa?

## Exercises

### Warm-up

**Exercise 0.1** — *Tool choice.* For each of the following D3 tasks, name the right Claude product and justify the choice in one sentence:

- Building a single bar chart from a dataset you have in your head.
- Building 12 charts for a course module across multiple sessions.
- Discussing whether a Sankey diagram is the right form for an unfamiliar dataset.
- Reading a published chart on a website and discussing whether the encoding is honest.

**Exercise 0.2** — *Vague vs. specific prompt.* Take this vague prompt: "Make a bar chart of revenue by region." Rewrite using the four-move structure. Add at least: chart type and orientation, channel-to-attribute mappings, sort order, color decision, axis ticks, label rotation, and a verification request. Aim for 150–200 words.

**Exercise 0.3** — *Failure mode identification.* Claude Code produces a chart that uses color hue (red, green, blue) to encode "Q1 revenue, Q2 revenue, Q3 revenue" with bars sized by total annual revenue. Identify all channel mismatches. Specify the corrected encoding.

### Application

**Exercise 0.4** — *Build with the four-move structure.* Take a real dataset you work with. Write a four-move Claude Code prompt for a chart of it. Submit. Audit using the three-layer verification stack. Hand in the prompt, the output, and the verification log.

**Exercise 0.5** — *Multi-LLM comparison on chart selection.* Pick a dataset where the right chart type is contestable. Submit the chart-selection question to Claude, ChatGPT, and Gemini. Compare the three responses. Where do they agree? Where do they disagree? What does the disagreement tell you about which decisions are genuinely contestable?

**Exercise 0.6** — *Document your default workflow.* Write a one-page document describing your personal default workflow for any new D3 chart. Include: which tool you start with, the four-move structure as your prompt template, the verification stack, and the conditions under which you escalate to multi-LLM comparison or to Claude Code from chat.

### Synthesis

**Exercise 0.7** — *Audit a published chart.* Find a chart in a recent newspaper, dashboard, or publication. Apply the chart-type-mismatch and channel-mismatch failure modes. If the chart was produced by an LLM (some are; the patterns are recognizable), specify what the LLM probably got wrong. If it was produced by a human, specify what the human got wrong. The diagnostic skill is the same.

**Exercise 0.8** — *Iterate to convergence.* Take a Claude Code output for a chart that didn't quite work. Write the follow-up prompt that names the specific failure (API hallucination, chart-type mismatch, or channel mismatch) and corrects it. Iterate until the chart is right. Hand in the prompt sequence and the final chart.

### Challenge

**Exercise 0.9** — *Build your `CLAUDE.md` and `DESIGN.md`.*

Before you draft either file, understand why there are two.

`CLAUDE.md` loads at the start of every Claude Code session. So does Claude Code's own system prompt — approximately 50 instructions you don't control and can't see. The total instruction budget for a session is roughly 150–200 behavioral rules. That means your `CLAUDE.md` has a real limit: approximately 100–150 instructions before reliability degrades. A file that contains both your D3 coding rules and your full design system — palette, typography, spacing, dark-mode behavior, responsive breakpoints, voice and tone — will exceed that limit. The rules that appear late in the file will be held less reliably than the rules that appear early.

The fix is not compression. It is separation. Coding decisions belong in `CLAUDE.md` because they apply to every session. Design decisions belong in `DESIGN.md` because they apply only when visual decisions are in scope — which, for most chart-building sessions (scales, data joins, axis ticks, transitions), is not.

Two files. One for code. One for design. Each within budget. Each loaded when and only when needed.

**Part A — Draft `CLAUDE.md`.** Include:

- D3 version policy (default v7; how to specify a legacy version).
- Naming conventions for SVG IDs and CSS classes (e.g., `chart-{type}-{n}` pattern, or your own preference with justification).
- Easing and transition vocabulary: which D3 curve names map to which visual behaviors.
- Accessibility standards: ARIA labels, focus states, color-blind safety, minimum contrast ratios.
- What Claude Code must NOT do without explicit instruction (no modifying existing charts; no encoding decisions without specification; no chart-type substitutions).
- The four-move prompt template you will use for every chart.

Keep it under 150 lines. If a rule belongs in `DESIGN.md`, move it. If a rule is ambiguous, ask: does this govern how code gets written, or how the result looks? Code → `CLAUDE.md`. Appearance → `DESIGN.md`.

**Part B — Draft `DESIGN.md`.** Include:

- Color palette: 6–10 named colors with hex values, semantic roles (primary, accent, sequential scale endpoints, error, disabled), and notes on color-blind safety.
- Typography stack: display face, body face, mono face, and the size/line-height ramp for each context (chart title, axis label, annotation, caption).
- Spacing scale: the base unit and the 8-step scale derived from it.
- Dark-mode behavior: how the palette inverts, which colors stay near-identical, which shift.
- Responsive breakpoints: which viewport widths trigger layout changes and what changes at each.
- Component rules: cards (background, border, radius, shadow, padding), axis treatment (tick density, gridline style), annotation style (leader lines, callout boxes).

Save both files in your project root as `CLAUDE.md` and `DESIGN.md`. Reference `CLAUDE.md` at the start of every subsequent session. Reference `DESIGN.md` explicitly when a session involves visual decisions.

**Exercise 0.10** — *Run a complete project audit.* Take a project (a small one — three to five charts) that you have produced previously. For each chart, apply the verification stack. For each failure, write the follow-up prompt that would have caught it. Hand in the audit log. The exercise teaches you what your typical failure modes are, which is the prerequisite for catching them in the future.

## LLM Exercise — Chapter 00: Building your prompting practice

**Project:** [TBD — selected after this chapter]

**What you're building this chapter:** Two files — your `CLAUDE.md` (coding constitution) and your `DESIGN.md` (visual constitution) — that travel with you across every chapter of this book and every D3 project beyond it. Plus a worked example showing your default workflow.

**Tool:** Claude Code (recommended) or Claude chat with a Claude Project for the persistent context.

### Why two files, not one

`CLAUDE.md` loads every session. `DESIGN.md` loads when visual decisions are in scope. They are separate because the LLM instruction budget is real: Claude Code's own system prompt consumes roughly 50 of the ~150–200 instructions available per session. A single merged file containing both coding rules and design system specifications will exceed the remaining budget, and the later rules — the ones that appear after the first ~100 lines — will be tracked less reliably. Two focused files keep each within budget. For most chart-building sessions (scales, joins, transitions), the design system is irrelevant; loading it wastes instructions on rules that don't apply.

### Part 1 — The Prompt for `CLAUDE.md`:

```
I am working through the Brutalist d3 x Claude book. Help me draft
my CLAUDE.md — the coding constitution I will reference at the start
of every Claude Code D3 session.

CLAUDE.md governs coding decisions only. Design decisions (palette,
typography, spacing, dark-mode, responsive behavior) belong in a
separate DESIGN.md and should NOT appear here.

Walk me through the sections it should contain:

1. D3 version policy (default; legacy projects).
2. Naming conventions for SVG IDs and CSS classes (chart-{type}-{n}
   pattern, or whatever I prefer, with justification).
3. Easing and transition vocabulary: which D3 curve names map to which
   visual behaviors.
4. Accessibility standards: ARIA labels, focus states, color-blind
   safety, minimum contrast ratios.
5. What Claude Code must NOT do without explicit instruction (no
   modifying existing charts; no encoding decisions without the
   specification; no chart-type substitutions).
6. The four-move prompt template I will use for every chart.

For each section, recommend defaults appropriate to the kind of work
described in the book. Where I should make a personal choice, name
the choice and the trade-offs. Keep the file under 150 lines total —
if a decision belongs in DESIGN.md, flag it rather than include it.

Save the document as CLAUDE.md.
```

### Part 2 — The Prompt for `DESIGN.md`:

```
Now help me draft my DESIGN.md — the visual constitution I will
reference when a Claude Code session involves design decisions:
palette, type, spacing, dark-mode behavior, responsive layout,
component rules.

DESIGN.md is loaded on demand, not every session. It governs how
charts and the surfaces around them look. Coding decisions (D3
version, naming conventions, accessibility implementation, the
four-move template) belong in CLAUDE.md and should NOT appear here.

Walk me through the sections it should contain:

1. Color palette: 6-10 named colors with hex values and semantic
   roles (primary, accent, sequential scale endpoints, error,
   disabled). Note color-blind safety for each.
2. Typography stack: display face, body face, mono face. Size and
   line-height for each context (chart title, axis label, annotation,
   caption).
3. Spacing scale: base unit and the 8-step scale derived from it.
4. Dark-mode behavior: how the palette inverts, which colors stay
   near-identical, which shift.
5. Responsive breakpoints: which viewport widths trigger layout
   changes and what changes at each.
6. Component rules: cards (background, border, radius, shadow,
   padding), axis treatment (tick density, gridline style),
   annotation style (leader lines, callout boxes).

For each section, recommend defaults that are practical for
data visualization work. Where I should make a personal choice,
name the choice and the trade-offs.

Save the document as DESIGN.md.
```

**What this produces:** Two markdown files that serve as your persistent session context for the rest of this book. `CLAUDE.md` loads every session. `DESIGN.md` loads when visual decisions are in scope. Save both; reference both; update both as you discover what works and what breaks.

**How to adapt these prompts:**

- *For your team:* Replace "I" with "we"; the team files become the shared coding and design standards for all D3 work in your organization.
- *For ChatGPT / Gemini:* Works as-is. The output documents are LLM-agnostic.
- *For a Claude Project:* Save `CLAUDE.md` as a reference file attached to the Project. Add `DESIGN.md` to sessions where visual decisions are in scope.

**Connection to previous chapters:** None — this is the first chapter that produces deliverables. Both files will be referenced in every subsequent chapter's LLM Exercise.

**Preview of next chapter:** Chapter 1 introduces marks and channels — the perceptual vocabulary that grounds every encoding decision in the rest of the book. The `CLAUDE.md` you drafted here does not yet have channel-decomposition rules; Chapter 1 supplies the vocabulary to add them. The `DESIGN.md` you drafted here does not yet reference a chart-specific color palette; Chapter 1's discussion of color channels will give you a principled basis for the choices you made.

## Further reading

- **Anthropic.** (2024–present). *Claude Code documentation.* The current canonical reference for the CLI tool. Read the introduction and the prompt-engineering section.
- **Anthropic.** (2024–present). Prompt engineering documentation at docs.claude.com. The "Be clear and direct" guidance is the same advice this chapter gives, generalized across all use cases.
- **The Brutalist system documentation** at [brutalist.art](https://www.brutalist.art/). The architectural framework this book inherits — phase model, labor separation, supervisory capacities, two governing files.
- **The book's pantry** at `pantry/00-claude-prompting-tips.md`. A workplace-focused chapter on Claude prompting that overlaps with this one and develops the four-move structure for non-D3 contexts.

## Tags

Claude-Code, prompting, four-move-structure, verification, multi-LLM-comparison, D3, API-hallucination, channel-mismatch, chart-type-mismatch, CLAUDE.md, DESIGN.md, instruction-budget, Brutalist, specification-skill, course-textbook
