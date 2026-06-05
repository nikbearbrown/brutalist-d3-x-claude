# Worked Exercises: Introduction

*Chapter 00 of Brutalist d3 x Claude*

*Bridge chapter — Parts D, E, and F omitted.*

> These exercises follow a research-backed sequence: full worked example →
> matched practice → completion problem → error-recognition → transfer →
> interleaved review. Each section builds on the previous. Do not skip ahead.

---

## Prerequisites

What you need from this chapter before these exercises make sense:

- transfer — understand that the book is about carrying concepts into usable visualization judgment.
- judgment — distinguish knowing chart vocabulary from using it well.
- structure — know how the chapters form a path from concepts to D3 production.

---

## Part A — Full Worked Example

**What this demonstrates:** This example makes visible how the book's transfer-and-judgment frame connects data structure, reader task, marks, channels, and implementation constraints.

**The problem:**

A learner knows the names of several D3 chart types but cannot yet choose or critique one for a real data problem.

**The solution:**

**Step 1 — Name the reader task**
State what the viewer must do first: compare, rank, trace change, see distribution, inspect relationship, follow flow, read geography, or audit a generated chart.
*Why:* The chapter treats chart choice as a design decision. A chart is right only relative to the task it helps the reader perform.
*Check:* The task can be written as a verb phrase, not just as a chart name.

**Step 2 — Identify the data structure**
List the relevant fields and classify them as categorical, quantitative, temporal, geographic, hierarchical, relational, or textual.
*Why:* Marks and channels must express the attribute types actually present in the data.
*Check:* Each field has a type, and no chart claim requires a field that the dataset does not contain.

**Step 3 — Assign marks and channels deliberately**
Use the chapter vocabulary mark, marks, and channel to specify which visual marks carry which data attributes.
*Why:* A D3 prompt that names marks and channels is a specification; a prompt that only names a chart type invites defaults.
*Check:* Quantitative values use magnitude channels where precision matters, and categorical identity is not encoded as if it were quantity.

**Step 4 — State what the chosen form prevents**
Name one misleading alternative and explain what story it would fabricate or obscure.
*Why:* The chapter's practical judgment comes from knowing not only what to use, but what not to use.
*Check:* The rejected chart fails for a specific reason: wrong data structure, wrong reader task, weak perceptual channel, or misleading convention.

**Step 5 — Translate the decision into a Claude/D3 instruction**
Write one implementation sentence that names the data file, the primary encoding, and one quality requirement such as responsiveness, accessibility, tooltip behavior, or scale choice.
*Why:* The book links visualization judgment to executable D3 work; the prompt should carry the design decision into code.
*Check:* A developer or Claude Code could implement the sentence without guessing the main encoding.

**Final answer:** The correct solution is to treat the introduction as a transfer problem: move from knowing chart vocabulary to using reader task, data structure, marks, channels, and D3 constraints as a decision process.

**What made this work:** The solution worked because it did not stop at naming a chart type. It connected the reader task to the data structure, mapped attributes onto visual channels, rejected a misleading alternative, and translated the result into implementation language. A naive approach would memorize chart names and hope recognition alone produced good visualization judgment.

**Self-explanation prompt:** Before moving on, close this page and write one sentence answering: *What principle did Step 3 rely on, and when would that principle not apply?*

---

## Part B — Matched Practice Problem

**Same structure, different surface.** This problem uses the same underlying concept as Part A but different details. Do not copy the Part A solution. Work it from scratch.

**The problem:**

A learner can name several chart types but cannot decide which one fits a dataset or reader task. Build a response that turns recognition into usable judgment.

Your answer should name the reader task, classify the data fields, choose marks and channels, reject one misleading alternative, and write one Claude/D3 instruction.

**Stuck?** Return to Part A and identify which step maps to your current obstacle. Do not read ahead to Part C until you have attempted this problem.

*Instructor note: A worked solution for Part B is not provided here. The point is production, not verification. If you need a solution key, generate one from the Part A template using the same step-label structure.*

---

## Part C — Completion Problem

**What's missing:** Steps 3 and 4 have been removed. You must supply them.

**The problem:**

A student has a polished chart description but no route for deciding whether it is the right chart. Complete the reasoning sequence.

**Partial solution:**

**Step 1 — Name the reader task**
The reader must perform the task that Introduction is built to support, not merely recognize the chart form.
*Why:* Task first; chart name second.

**Step 2 — Identify the data structure**
The dataset must be checked for the field types required by the chart: categories, measures, time, geography, hierarchy, relation, or text as appropriate.
*Why:* The chart cannot honestly encode data attributes that are absent or misclassified.

**Step 3 — [BLANK]**
*Your work here:*

_____________________

*Why (your explanation):*

_____________________

**Step 4 — [BLANK]**
*Your work here:*

_____________________

*Why (your explanation):*

_____________________

**Step 5 — Translate the decision into a Claude/D3 instruction**
The final prompt must specify the data shape, marks, channels, and at least one quality requirement such as responsive layout or SVG accessibility.
*Why:* Implementation quality depends on carrying the design decision into the prompt.

**Final answer:** The completed reasoning should justify Introduction through the connection between reader task, data structure, encoding choice, and implementation constraints.

**Self-explanation prompt:** Compare your Step 3 and Step 4 to the Part A solution. Where did your reasoning match? Where did it differ? Which difference matters?
