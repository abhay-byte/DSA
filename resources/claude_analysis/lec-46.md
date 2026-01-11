# Lecture 46 - Graphs: Disjoint Set & MST

**Source:** `L46 - Graphs.pdf`

---

## Page 1: Disjoint Set (Union-Find) Introduction

### What is a Disjoint Set?
A **disjoint set** is a data structure that maintains a collection of **dynamic sets** {S₀, S₁, S₂, ...} that are pairwise disjoint (no overlap). For any two sets Sᵢ and Sⱼ: Sᵢ ∩ Sⱼ = ∅

### Three Main Operations:
1. **createSet(x)** - Create a new set with a single member x (leader/representative)
2. **unionSet(x, y)** - Create a set S as union of Sₓ & Sᵧ containing x & y
3. **findSet(x)** - Returns the leader/representative of the set containing x

### Visual Example:
```
Initial:     createSet(1), createSet(2), createSet(3), createSet(4)
             [1]    [2]    [3]    [4]

unionSet(2,3): [1]   [2,3]   [4]

findSet(3) → 2

unionSet(1,4): [1,4]  [2,3]

unionSet(3,4): [1,2,3,4]

findSet(1) → 1
findSet(2) → 1
findSet(3) → 1
findSet(4) → 1
```

---

## Page 2: Disjoint Forest Representation

### Two Representation Methods:
1. Linked List Representation
2. **Disjoint Forest Representation** (faster)

### Forest Structure:
- Each set = Rooted Tree
- Each node points to its **parent**
- **Root node** points to **itself** (the leader)

```
S₁: {1,2,3,4,5}          S₆: {6,7,9}        S₁₀: {10}
       1                       6                  10
      / \                     / \
     2   3                   7   8
    /
   4
   |
   5
```

### Operations with Forest:
- **createSet(x)**: Create single-node tree, parent[x] = x
- **findSet(x)**: Follow parent pointers to root (time ∝ height of tree)

```
findSet(5):
    5 → 4 → 2 → 1 (root)
    Return 1
```

- **unionSet(x, y)**:
  1. Find roots: findSet(x), findSet(y)
  2. Make one root point to the other

---

## Page 3: Implementation with Hash Table

### Data Structure:
Use a **hash table** to store mapping between nodes and their parents.

| vertex | parent |
|--------|--------|
| 1 | -1 (root) |
| 2 | 1 |
| 3 | 1 |
| 4 | 3 |
| 5 | 3 |
| 6 | 6 (root) |
| 7 | 6 |
| 8 | 6 |

### Efficiency Optimization - Two Heuristics:

#### 1. Union by Rank (or Size)
During union operation, make the root of the tree with **lower rank** point to the root of the tree with **higher rank**.

```
Before union(S₁, S₂):     After (attach smaller to larger):
    1       6                    1
   /|\      |                  / | \
  2 3 4    7,8                2  3  6
           |                     |  |
                                4   7,8
```

---

## Page 4: Path Compression

### Idea:
During **find** operation, make every node visited along the path **point directly to the root**.

```
Before findSet(7):          After findSet(7):
       1                          1
      /                       /|\ \ \
     2                       2 3 4 5 7
    /
   3
  /
 4
/
5
|
7
```

### Combined Complexity:
When combining **Union by Rank** + **Path Compression**:
- Time complexity: O(α(n)) ≈ **constant** for practical inputs
- α(n) = inverse Ackermann function (grows extremely slowly)

---

## Page 5: Applications of Disjoint Set

### 1. Detect Cycle in Undirected Graph
```
V = {1, 2, 3, 4}
E = {{1, 2}, {2, 3}, {3, 4}, {4, 1}}  ← Cycle!

Process edges:
- unionSet(1,2): No cycle
- unionSet(2,3): No cycle  
- unionSet(3,4): No cycle
- unionSet(4,1): findSet(4) == findSet(1)? YES → CYCLE DETECTED!
```

### 2. Count Connected Components
```
V = {1,2,3,4,5,6,7}
E = {{1,2}, {1,4}, {2,3}, {3,4}, {5,6}, {6,7}}

After all unions:
- Component 1: {1,2,3,4}
- Component 2: {5,6,7}

numComponents = Number of distinct roots = 2
```

---

## Page 6-7: Minimum Spanning Tree (MST)

### Definition:
Given a **connected, undirected, weighted** graph, find the **minimum spanning tree** - a tree connecting all vertices with minimum total edge weight.

> **Property:** A tree with n nodes has exactly **n-1 edges**

### Kruskal's Algorithm:
1. Sort all edges by weight (ascending)
2. For each edge (in order):
   - If adding edge doesn't create cycle → add to MST
   - Use **Union-Find** to check for cycles

```
Example:
Edges sorted: 5-6:1, 2-4:2, 5-7:3, 1-2:4, 1-3:5, ...

Step by step:
- Add 5-6 (weight 1) ✓
- Add 2-4 (weight 2) ✓
- Add 5-7 (weight 3) ✓
- Add 1-2 (weight 4) ✓
- ...until V-1 edges added
```

### Prim's Algorithm:
- Start from any vertex
- Repeatedly add the **minimum weight edge** connecting visited to unvisited
- Uses **min-heap** for optimization

---

## Page 8-10: Minimize Malware Spread Problem

### Problem Statement:
Given:
- Network of n nodes as **adjacency matrix** (graph[i][j] == 1 means connected)
- Some nodes are **initially infected** with malware
- Malware spreads through direct connections

**Goal:** Remove exactly ONE node from initial infected list to **minimize M(initial)** - final number of infected nodes.

### Example:
```
Adjacency Matrix (9 nodes):        Graph:
  0 1 2 3 4 5 6 7 8               0---1-------7
0[1 0 1 0 0 0 0 0 0]               \   \     /
1[0 1 0 1 0 0 0 0 0]                2---3   8
2[1 0 1 0 1 0 0 0 0]                    |
3[0 1 0 1 0 1 0 0 0]                    4---5
4[0 0 1 0 1 0 1 0 0]                       /
5[0 0 0 1 0 1 1 0 0]                      6
6[0 0 0 0 1 1 1 0 0]
7[0 0 0 0 0 0 0 1 1]
8[0 0 0 0 0 0 0 1 1]
```

### Solution Approach:
Use **Union-Find** to:
1. Build connected components
2. Track which components have infected nodes
3. Find component where removing one infected node saves most nodes

### Data Structures:
- **parentMap[i]**: parent of node i in Union-Find forest
- **rankMap[i]**: rank of node i (for union by rank)

---

## Summary

| Concept | Time Complexity |
|---------|-----------------|
| createSet | O(1) |
| findSet (naive) | O(n) |
| findSet (with path compression) | O(α(n)) ≈ O(1) |
| unionSet (naive) | O(n) |
| unionSet (union by rank + path compression) | O(α(n)) ≈ O(1) |
| Kruskal's MST | O(E log E) |
| Prim's MST | O(E log V) with min-heap |

### Key Takeaways:
1. **Union-Find** is essential for dynamic connectivity problems
2. **Path compression** + **Union by rank** = near-constant time operations
3. **Kruskal's** uses Union-Find to build MST by sorting edges
4. **Prim's** grows MST from a starting vertex using greedy selection
