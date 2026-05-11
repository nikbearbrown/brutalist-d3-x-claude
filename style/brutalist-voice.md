# Brutalist Voice — Per-Book Style Anchor

*This file overrides root `style/` for chapters in `brutalist-d3-x-claude`. Read before drafting.*

---

## The Posture

The book teaches D3 visualization through Claude Code, but the deeper subject is **Brutalist**: a system for human–AI collaborative production built around one commitment —

> **Maximally informed and minimally autonomous by design.**

The tone of every chapter must carry that commitment in its bones. Not as a slogan. As a working stance.

---

## What "Brutalist Tone" Means in Prose

**Load-bearing, not decorative.** Every paragraph holds weight or it gets cut. No softening hedges. No throat-clearing. No "in this chapter we will explore" preambles. The structure is exposed, like the concrete of the buildings the name borrows from. Sentences are framed, not finished.

**Refuses to perform expertise.** The voice does not flatter the reader or the tool. Claude Code is not magical; it is a code-generator under human direction. D3 is not elegant; it is an API the student must direct with judgment. The chapter does not pretend the reader is closer to mastery than they are.

**Names the boundary.** Every chapter makes the labor separation visible: this is the work Claude does, this is the work you do. Where a reader might want to delegate a creative or strategic decision, the chapter names it as the human's job and does not blur the line.

**Says no.** When a chart, a default, or a pattern is wrong for the task, the chapter says so. Plainly. "A pie chart with seven slices is unreadable. Do not build it." Brutalism does not negotiate with bad defaults to spare anyone's feelings.

**Surfaces, then defers.** When the chapter introduces new D3 syntax, a security note, a deprecation, or a breaking change, it names what is happening and hands the decision to the reader. *Here is what the documentation now says. Here is what would change if you applied it. You decide.*

**Phase discipline as prose discipline.** The chapter respects the same phases the system enforces: audit before schema, schema before generate, generate before verify, verify before handoff. The prose does not jump phases. It does not show a finished chart before specifying what the chart is supposed to do.

---

## Vocabulary Markers

Use:

- "The human decides."
- "Claude generates. You verify."
- "Refuse the default."
- "The chart is doing work, or the chart is performing effort."
- "Surface, do not act."
- "Intent first. Schema second. Generation third. No phase skipped."
- "Here is what the AI does. Here is what does not transfer."
- "Read before writing."

Cut on sight:

- "Effortlessly."
- "Just" (as in "just ask Claude to...").
- "Magic," "magical," "wizardry."
- "Seamless," "seamlessly."
- "Empowers you to..."
- "Unleash the power of..."
- "Let AI handle the heavy lifting."
- "AI-powered" as a modifier.
- Any sentence that reads as if it could appear on a SaaS landing page.

---

## The Six Principles, Mapped to the Chapter Form

Every chapter in this book carries at least one of these as an undertone. Not every one in every chapter — but the book, taken whole, exemplifies all six.

1. **Intent Layer.** The opening of each chapter specifies the visualization's purpose in plain English before any code appears. *What should the reader of this chart understand?* The question precedes the syntax.

2. **Schema Layer.** When code appears, the chapter names the conventions — naming, scales, color, easing, defaults — and treats them as governed, not improvised. Claude generates against the schema, not against vibes.

3. **Phase Gate.** Chapters move in order: read the data, choose the chart, justify the choice, generate the code, verify the result, lock the output. Mid-chapter exercises mirror the same gate.

4. **Labor Separation.** Each chapter names what Claude Code can do (write the join, tween the path, set the scale domain) and what it cannot (decide whether a violin plot is the right form for *this* dataset and *this* reader). The boundary is made explicit, not assumed.

5. **Refusal Behavior.** When a reader is likely to ask Claude Code to make a judgment call — pick a chart, choose a palette, decide whether to log-scale — the chapter shows the refusal: *That is not Claude's call. Here is how to make it yours.*

6. **Current Knowledge, Deferred Action.** When a chapter touches anything that drifts — D3 version, browser API, accessibility standard, a paper's findings — it names the date of the reading and frames updates as something the reader applies, not something the chapter assumes is current forever.

---

## How the Tone Reads on the Page

A chapter on the pie chart does not open with "the pie chart is a classic visualization for part-to-whole comparisons." It opens with the failure: a screenshot of seven slices that no human can rank. It names the human task (estimate the proportion) and the perceptual channel (angle, area, arc length) and shows that the channel fails above three or four categories. It tells the reader: if you have more than four slices, refuse the pie. Then, and only then, does it show Claude Code generating a small, defensible three-slice pie — and a stacked bar that handles the seven-category case better. The chapter does not apologize for being opinionated. The opinion is the teaching.

A chapter on a Sankey diagram does not call it "powerful" or "elegant." It says: a Sankey shows flow when the quantities at every node sum cleanly and the reader needs to follow paths. It does not show direction-of-change well. It does not show small flows well. It is a chart that performs effort when the data does not earn it. Here is the case where it earns it. Here is the case where it does not. The reader is given the rule and the exception, not a celebration.

A chapter on Claude Code's role does not call it a "co-pilot." Claude is the syntax-generator the reader directs. The reader writes the intent in human language. Claude renders it into D3. The reader verifies. If Claude proposes a creative direction unprompted, the reader rejects it. The chapter teaches that posture as a habit, not as a special-case caution.

---

## Forbidden Postures

- **Tool-cheerleading.** The book does not sell Claude Code. It uses Claude Code. The difference shows.
- **Reader-flattery.** "You've got this!" and similar warmings have no place. The reader is a working professional. The voice treats them as one.
- **Frictionless framing.** The book never pretends the work is easy. The work is structured, gated, and verified. That is the point.
- **Authority-by-citation alone.** When a paper or a designer is invoked, the chapter shows the work being done, not just the name being dropped.
- **Trend-tone.** No "in the age of AI," no "as we increasingly...". The book is dated to its moment but does not narrate the moment.

---

## The Closing Sentence Test

Every chapter ends with a short, declarative line that could survive being printed on a wall. If the closing reads as a hedge, rewrite it. If the closing reads as a recap, rewrite it. The closing is the load-bearing wall: it holds up everything before it.

---

*Source: Brutalist project description (Nik Bear Brown). Voice ground truth for `brutalist-d3-x-claude`. Overrides root `style/` on conflict.*
