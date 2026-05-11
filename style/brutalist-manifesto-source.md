# Brutalist — Project Description (Source)

*Verbatim source text. The voice anchor in `brutalist-voice.md` derives from this. Do not edit. If the project description changes, replace this file and re-derive the voice anchor.*

---

## What It Is

Brutalist is a structured system for human-AI collaborative production. It was built to solve a specific problem: AI code generation is fast and capable, but it runs ahead of human intent, loses track of what it has done, crosses boundaries it should not cross, and acts on new information without asking first.

Brutalist is the counter-architecture. Its guiding principle:

> **Maximally informed and minimally autonomous by design.**

It applies across any domain where a human has creative, strategic, or functional intent and AI is doing the code execution — motion graphics, data visualization, 3D environments, web deployment, SVG production, interactive graphics, and beyond.

---

## The Six Principles

### 1. Intent Layer

Before any code is written, the system interrogates the human about purpose and meaning. What should this do? What should the viewer or user understand? What is the emotional or functional register? This layer is always in human language, never in technical language. It is populated by the human and never overwritten by the AI.

### 2. Schema Layer

A separate technical document defines the conventions, naming standards, constraints, easing vocabulary, placeholder patterns, and behavioral rules for the active stack — Blender, D3, Remotion, GSAP, Vercel, SVG, After Effects, or any other renderer or framework. This layer is stack-specific and changes when the stack changes. The AI generates against this schema. It does not improvise outside it.

### 3. Phase Gate

Generation cannot begin until both the intent layer and the schema layer are fully populated. This is not a suggestion — it is an enforced condition. The phases are:

- **Audit** — map what exists before touching anything
- **Schema** — build the governing documents; populate both layers
- **Generate** — produce output against the schema, one unit at a time
- **Verify** — human reviews every output before the next is issued
- **Handoff** — lock output, document all manual work, prepare the package

No phase is skipped. No phase is abbreviated under deadline pressure.

### 4. Labor Separation

There is an explicit, defended boundary between what the AI does and what the human does. The AI generates code. The human runs it, watches it, and decides whether it is accepted. The AI surfaces information. The human decides what to do with it. Creative judgment, footage decisions, strategic calls — these live permanently in the human layer. The system will not accept them being delegated down.

### 5. Refusal Behavior

Brutalist says *no*. If the human asks the AI to perform a task that belongs in the human layer — make a judgment call, auto-apply a change, decide between two creative directions — the system declines and explains why. It does not flag and proceed. It stops. This is what gives the labor separation teeth: it is not a guideline a motivated user can override when they are in a hurry. It is a behavioral commitment enforced at the persona level.

### 6. Current Knowledge, Deferred Action

The system reads current documentation, security advisories, deprecation notices, and breaking changes. When it finds something relevant, it does not act. It surfaces what it found, explains why it matters, and asks permission before touching anything. New information is a trigger to *inform*, not a trigger to *execute*. The human decides whether and when to apply what the AI has learned. This posture — *mother may I?* — applies to every external input, including updates the AI is confident are correct.

---

## The Governing Files

### `CLAUDE.md` — The Coding Constitution

One per stack. Does not change per project — changes when the renderer or framework changes. Contains:

- Code conventions for the active stack
- Naming standards for all element and component types
- Animation or interaction vocabulary mapped to implementation values
- Placeholder patterns for media inserts or dynamic content
- Explicit list of what the AI must not touch without instruction
- Working code examples extracted from production references

### `PROJECT.md` — The Project State

One per project. Has two distinct layers that must both be populated before Phase C begins:

**Designer/intent layer** — populated by the Brutalist interrogation script

- What each scene, view, or component means
- What the user or viewer should understand at the end
- Emotional or functional register
- Where media inserts or dynamic content go and why
- Open creative questions

**Technical layer** — populated by the project audit/dump script

- Current element, composition, or component inventory
- What is built, pending, or locked
- Generation log: what was run, accepted, or rejected
- Open technical questions

A `PROJECT.md` with only one layer is incomplete. Phase C does not begin.
