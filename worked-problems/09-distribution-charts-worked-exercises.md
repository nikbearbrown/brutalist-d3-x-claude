# Worked Exercises: Distribution Charts

*Chapter 09 of Brutalist d3 x Claude*

> These exercises follow a research-backed sequence: full worked example →
> matched practice → completion problem → error-recognition → transfer →
> interleaved review. Each section builds on the previous. Do not skip ahead.

---

## Prerequisites

What you need from this chapter before these exercises make sense:

- Distribution Charts — know the chapter's central visualization task.
- channel — understand how this term functions in the chapter, not just its definition.
- What the mean hides — be able to explain why this section shapes the design decision.

---

## Part A — Full Worked Example

**What this demonstrates:** This example makes visible how the design logic of Distribution Charts connects data structure, reader task, marks, channels, and implementation constraints.

**The problem:**

Evaluate this chapter-grounded visualization case: This is the central tension of the whole chapter. Every distribution chart is a compression. Some compressions preserve the shape. Others preserve the quartiles. Others preserve the raw values. No single form preserves everything, and the right choice depends on what the reader needs to see and what they are able to read.

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
Use the chapter vocabulary channel, channels, and encoding to specify which visual marks carry which data attributes.
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

**Final answer:** The correct solution is to treat Distribution Charts as a design response to a specific reader task and data structure, then express that decision through explicit marks, channels, and D3 implementation constraints.

**What made this work:** The solution worked because it did not stop at naming a chart type. It connected the reader task to the data structure, mapped attributes onto visual channels, rejected a misleading alternative, and translated the result into implementation language. A naive approach would ask Claude to "make a Distribution Charts" and hope the defaults matched the chapter's design logic.

**Self-explanation prompt:** Before moving on, close this page and write one sentence answering: *What principle did Step 3 rely on, and when would that principle not apply?*

---

## Part B — Matched Practice Problem

**Same structure, different surface.** This problem uses the same underlying concept as Part A but different details. Do not copy the Part A solution. Work it from scratch.

**The problem:**

A new dataset has the same underlying visualization problem as Distribution Charts, but the labels and values are different. Decide which marks, channels, and reader task should govern the design.

Your answer should name the reader task, classify the data fields, choose marks and channels, reject one misleading alternative, and write one Claude/D3 instruction.

**Stuck?** Return to Part A and identify which step maps to your current obstacle. Do not read ahead to Part C until you have attempted this problem.

*Instructor note: A worked solution for Part B is not provided here. The point is production, not verification. If you need a solution key, generate one from the Part A template using the same step-label structure.*

---

## Part C — Completion Problem

**What's missing:** Steps 3 and 4 have been removed. You must supply them.

**The problem:**

A Claude Code prompt for a Distribution Charts is missing the encoding rationale and the quality check. Complete the missing reasoning steps before code generation.

**Partial solution:**

**Step 1 — Name the reader task**
The reader must perform the task that Distribution Charts is built to support, not merely recognize the chart form.
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

**Final answer:** The completed reasoning should justify Distribution Charts through the connection between reader task, data structure, encoding choice, and implementation constraints.

**Self-explanation prompt:** Compare your Step 3 and Step 4 to the Part A solution. Where did your reasoning match? Where did it differ? Which difference matters?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**
> For complete novices working through this chapter for the first time,
> skip to Part E and return here after completing the full chapter.

**What's wrong:** The solution below contains one error. It is marked with ⚠.
Your job is to find it, explain why it is wrong, and correct it.

**The problem:**

A student proposes a Distribution Charts for data that superficially resembles the chapter example. The solution sounds plausible, but one design move violates the chapter's encoding logic.

**The flawed solution:**

**Step 1 — Name the chart type**
The student identifies Distribution Charts as the intended form.

**Step 2 — Describe the visible design**
The student mentions labels, colors, and the general layout.

**Step 3 — Let visual appeal substitute for encoding fit** ⚠
The student keeps the chart because it looks clear, without checking whether the marks and channels match the data structure and reader task.

**Step 4 — Send the prompt to Claude Code**
The student asks for a polished D3 implementation, so the result may look professional while preserving the original design mistake.

**Your tasks:**

1. Identify which step contains the error (do not just say "Step 3" — explain
   what is wrong with it and why the correct approach is different).
2. Write the corrected Step 3.
3. Explain what principle the original Step 3 violated.
4. Describe a test you could run to catch this class of error in your own work.

**Why this error is common:** Students often learn chart forms as visual templates before they learn to test whether the encoding fits the data and the reader task.

---

## Part E — Transfer Problem

**Same principle, new context.** This problem uses the same underlying concept
from the chapter but in a scenario not discussed in the chapter. No worked
example is provided.

**The problem:**

Use the principle from Distribution Charts in a different domain: civic data, classroom analytics, public health, finance, or operations. The surface topic changes; the reader task and encoding logic stay central.

**Hint (use only if stuck after 10 minutes):** Do not start with the chart name. Start with the reader task and the field types, then select the encoding.

**Reflection prompt:** After completing this problem, write two sentences:
(1) What concept from the chapter did you apply, and how did you recognize
it applied here? (2) What was different about applying it in this new context?

---

## Part F — Interleaved Review

**Mixed problem set.** These problems draw on concepts from this chapter and
from previous chapters. You must decide which concept or method applies to
each problem before solving it. That selection step is the point.

**Problem F1:**
A dataset appears suitable for Distribution Charts. Decide what marks and channels would make the reader task explicit, and name one implementation requirement for the D3 version.
*Chapter this draws from: Chapter 09 — Distribution Charts*

**Problem F2:**
A second dataset looks more like Time Series and Temporal Charts. Decide whether the previous chapter's method or the present chapter's method better matches the reader task.
*Chapter this draws from: Chapter 08 — Time Series and Temporal Charts*

**Problem F3:**
A polished chart appears to use the right visual family, but the decisive issue is whether the encoded data structure matches Distribution Charts or a different chart logic from an earlier chapter. Choose the governing concept and justify it before solving.
*Note to instructor: This problem is intentionally ambiguous on first reading. The student should commit to an approach before solving, then reflect on whether the approach was correct.*

**After completing F1–F3, answer:** For each problem, state which concept
you reached for first and whether that was the right call. If you chose
wrong, what cued you to switch?

---

## Instructor Notes

**Common errors to watch for in student work:**

- Naming a chart type without naming the reader task it supports.
- Encoding quantitative data with a weak or inappropriate channel when a stronger one is available.
- Sending Claude Code an underspecified prompt that leaves marks, channels, scales, or accessibility behavior to defaults.

**Signs a student needs to return to the chapter before these exercises:**

- The student cannot explain how What the mean hides connects to the chart choice.
- The student describes visual style but cannot classify the underlying data fields.

**Scaffolding adjustments:**

- *For students who struggle with Part A:* Give them a four-column worksheet: reader task, data fields, marks/channels, rejected alternative.
- *For students who finish Part F quickly:* Ask them to write a stricter Claude Code prompt that includes data shape, responsive behavior, SVG title/desc, and tooltip requirements.

**Domain adaptation note:** These exercises were generated from the chapter
as written. An instructor teaching a different population (e.g., engineering
students vs. humanities students) can substitute domain-appropriate surface
content in Parts B, E, and F while preserving the structural sequence.
