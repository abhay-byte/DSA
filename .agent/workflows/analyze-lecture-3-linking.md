---
description: Phase 3/3 - Problem Linking & Verification
---

# Phase 3: Problem Linking

**Input:** `resources/claude_analysis/lec-{NUM}.md` (with Text & Visuals)
**Goal:** Connect theoretical concepts to real-world coding problems (LeetCode/GFG).

---

## Step 1: Identify Topics

**Instruction:**
Read the headers (`## Topic X`) in `lec-{NUM}.md`.
Identify the core algorithmic problem (e.g., "Cycle Detection", "Bipartite Graph", "Connected Components").

---

## Step 2: Search & Verify

**Action:**
For each topic, perform a Web Search.
**Queries:**
- "LeetCode {Topic Name}"
- "GeeksForGeeks {Topic Name}"

**Verification:**
- Ensure the problem statement matches the lecture concept.
- Prefer **LeetCode** for standard problems.
- Use **GeeksForGeeks** for theoretical tutorials or if no direct LC exists.

---

## Step 3: Inject Links

**Action:** Edit `resources/claude_analysis/lec-{NUM}.md`.
- Under each `## Topic {Name}` header, insert:

```markdown
**Problem Link:** [{Source}: {Problem Title}]({URL})
```

**Example:**
`**Problem Link:** [LeetCode 207: Course Schedule](https://leetcode.com/problems/course-schedule/)`

**Final Step:**
- Update `resources/PROGRESS.md` status to `✅ Complete`.
