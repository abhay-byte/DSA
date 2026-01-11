---
description: Analyze lecture PDF (Master Workflow - 3 Phases)
---

# Lecture Analysis Workflow (Master)

This process is divided into **3 INDEPENDENT Phases**. 
Execute them sequentially for the best result.

**Target:** `resources/claude_analysis/lec-{NUM}.md`

---

## Phase 1: Text & Structure
**Goal:** Convert PDF and create valid Markdown skeleton with concepts.
**Workflow:** `analyze-lecture-1-text.md`
**Command:**
`/analyze-lecture-1-text`

---

## Phase 2: Visuals & Traces
**Goal:** Reconstruct exact ASCII/Mermaid diagrams and "Debugger" traces from images.
**Workflow:** `analyze-lecture-2-visuals.md`
**Command:**
`/analyze-lecture-2-visuals`

---

## Phase 3: Linking & Finalize
**Goal:** Search and link LeetCode/GFG problems. Update Progress.
**Workflow:** `analyze-lecture-3-linking.md`
**Command:**
`/analyze-lecture-3-linking`

## Phase 4: Instructor Code
**Goal:** Link C++ implementations from the instructor's GitHub.
**Workflow:** `analyze-lecture-4-code.md`
**Command:**
`/analyze-lecture-4-code`

---

## Usage Guide
1. Start with **Phase 1**.
2. Review the output.
3. Run **Phase 2** to add visuals.
4. Run **Phase 3** to link problems.
5. Run **Phase 4** to link code.
