---
description: Phase 4/4 - Instructor Code Linking to Topics
---

# Phase 4: Instructor & User Code Linking

**Input:** `resources/claude_analysis/lec-{NUM}.md` (with Text, Visuals & Problem Links)
**Goal:** Link instructor's C++ code and User's practice code to each topic.

---

## Code Repositories

### 1. Instructor Code (Local)
| Field | Value |
|-------|-------|
| **Repository** | [abhishek18124/PPCPPMar2025](https://github.com/abhishek18124/PPCPPMar2025) |
| **Local Clone** | `instructor_code/` (in dsa repo root) |
| **Structure** | `Lecture {NUM}/` folders containing `.cpp` files |

### 2. User Practice Code (Internal Clone)
| Field | Value |
|-------|-------|
| **Repository** | [abhay-byte/DSA_Practice](https://github.com/abhay-byte/DSA_Practice) |
| **Local Clone** | `user_practice_code/` (in dsa repo root) |
| **Path** | `user_practice_code/CB/LEC{NUM}/` |
| **Link Pattern** | `../../user_practice_code/CB/LEC{NUM}` (relative to `claude_analysis/`) |

---

## Step 0: Setup User Code

**Action:**
Ensure the user practice repository is cloned and up to date.

// turbo
```bash
if [ -d "user_practice_code" ]; then
    cd user_practice_code && git pull
else
    git clone https://github.com/abhay-byte/DSA_Practice.git user_practice_code
fi
```

---

## Step 1: Identify Available Code Files

**Action:**
List files in `instructor_code/Lecture {NUM}/`:

// turbo
```bash
ls -la /home/abhay/repos/dsa/instructor_code/Lecture\ {NUM}/
```

**Expected Output:**
```
001TopicA.cpp
002TopicB.cpp
003TopicC.cpp
...
```

---

## Step 2: Map Code Files to Topics

**Instruction:**
For each code file, determine which topic in `lec-{NUM}.md` it corresponds to:

| Code File | Likely Topic Match |
|-----------|-------------------|
| `*Search*.cpp` | DFS/BFS, Reachability |
| `*Traverse*.cpp` | Graph Traversal, Connected Components |
| `*Cycle*.cpp` | Cycle Detection |
| `*BackEdge*.cpp` | Back Edge Detection (Directed) |
| `*Bipartite*.cpp` | Bipartite Graph |
| `*Clone*.cpp` | Clone Graph |
| `*Shortest*.cpp` | Shortest Path (BFS) |

**Verification:**
- Open each `.cpp` file and read the comment header
- Match the implementation to the corresponding topic in the markdown

---

## Step 3: Create Local Relative Links

**Format:**
```
../instructor_code/Lecture%20{NUM}/{FILENAME}
```

**Alternative (Absolute):**
```
/home/abhay/repos/dsa/instructor_code/Lecture {NUM}/{FILENAME}
```

**Example:**
```
../instructor_code/Lecture%2043/001Graphs_Search.cpp
```

---

## Step 4: Inject Code Links into Markdown

**Action:** Edit `resources/claude_analysis/lec-{NUM}.md`.

Under each `## Topic {Name}` section, after the **Problem Links**, add:

```markdown
**Instructor Code:** 
- [filename.cpp](../instructor_code/Lecture%20{NUM}/{FILENAME})

**My Practice Code:** 
- [DSA_Practice/CB/LEC{NUM}](../../user_practice_code/CB/LEC{NUM})
```

**Example:**
```markdown
## Topic 2: Depth First Search (DFS)

**Problem Links:**
- [LeetCode 200: Number of Islands](...)

**Instructor Code:** 
- [001Graphs_Search.cpp](../instructor_code/Lecture%2043/001Graphs_Search.cpp) - DFS Implementation

**My Practice Code:** 
- [DSA_Practice/CB/LEC43](../../user_practice_code/CB/LEC43)
```

---

## Step 5: Embed Code Snippets (Optional)

For key implementations, embed the actual code in a collapsible section:

```markdown
<details>
<summary>View Code: DFS Implementation</summary>

```cpp
void dfs(int cur, const vector<vector<int>>& adj, vector<bool>& vis) {
    vis[cur] = true;
    cout << cur << " ";
    for (int ngb : adj[cur]) {
        if (!vis[ngb]) {
            dfs(ngb, adj, vis);
        }
    }
}
```

</details>
```

**Rules:**
- ✅ Only embed short, key functions (< 30 lines)
- ✅ Always include the local link for full file
- ❌ Do NOT embed entire files

---

## Step 6: Update Progress

**Action:** Update `resources/PROGRESS.md`:

Change status from:
```
| L{NUM} | ✅ | ✅ | ✅ Complete |
```

To:
```
| L{NUM} | ✅ | ✅ | ✅ Complete (4 Phases) |
```

---

## Code File Naming Patterns

Common patterns found in the instructor's repository:

| Pattern | Meaning |
|---------|---------|
| `001`, `002`, ... | Sequence in lecture order |
| `Graphs_*` | Graph-related algorithms |
| `*Impl*.cpp` | Implementation variants |
| `*0`, `*1`, `*2` | Alternative implementations |
| `[EC]` in folder name | Extra Class content |

---

## Quick Reference: Lecture 43 Example

| File | Topic | Local Link |
|------|-------|-------------|
| `001Graphs_Search.cpp` | DFS (Topic 2) | [Link](../instructor_code/Lecture%2043/001Graphs_Search.cpp) |
| `001Graphs_Search2.cpp` | BFS (Topic 3) | [Link](../instructor_code/Lecture%2043/001Graphs_Search2.cpp) |
| `002Graphs_Traverse.cpp` | Connected Components (Topic 4) | [Link](../instructor_code/Lecture%2043/002Graphs_Traverse.cpp) |
| `003Graphs_DetectCycle.cpp` | Cycle Detection (Topic 5) | [Link](../instructor_code/Lecture%2043/003Graphs_DetectCycle.cpp) |
| `004Graphs_BackEdge.cpp` | Back Edge Detection (Topic 8) | [Link](../instructor_code/Lecture%2043/004Graphs_BackEdge.cpp) |
