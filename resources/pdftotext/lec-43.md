# Lecture 43

**Source:** `L43 - Graphs.pdf`

---

Graphs - DFS

Reachability in Graphs
Given a connected graph and a source vertex, design an algorithm to find all the
vertices reachable from the source vertex. A vertex "v" in the graph is said to be
reachable from vertex "u" if there exists a path from vertex "u" to vertex "v".
0
1
3

0
2

1

4
6

5

2
4

3

7

6

8

5
7

8

Depth First Search ( DFS )
The key idea behind the DFS algorithm is that for any vertex "u" in the graph, when
you visit one of its unvisited neighbors, say "v", then first you visit all the unvisited
vertices reachable from "v" before you visit the other unvisited neighbors of "u".
0
1
3

2
4

6

7
8

013642578

L43 - Graphs Page 1

5

0
1
3

2
4

6

5
7

8

L43 - Graphs Page 2

Graphs - BFS

Breadth First Search
The key idea behind the BFS algorithm is that, for any vertex "u" in the graph, you've to
first visit all of its unvisited neighbors before you visit the neighbors of its neighbors.

0
1

2

4

3

6

5

7
8

BFS Implementation
To implement the BFS algorithm, we will maintain

• a Queue to keep track of nodes that have been visited but not yet explored.
• a Set / Map to keep track of nodes that have been visited.

queue

0
1
3

2
4

6

5
7

8

L43 - Graphs Page 3

0

Graphs - Traversal

Graph Traversal

0
2

1
3

5

4
6

L43 - Graphs Page 4

14

13

9
10

12

8

7

11

15

Graphs - Cycle

Cycle Detection
Given an undirected graph design an algorithm to check if contains a cycle.

1

1
0

2

0

2

3
False
False

True

L43 - Graphs Page 5

0

1

[R][HW] Graphs - Bipartite Graph

Bipartite Graph
Given an undirected graph design an algorithm to check if it is a Bipartite graph.
A graph is said to be a Bipartite graph if the graph nodes can be partitioned into two
independent sets A and B such that each edge in the graph connects a node in set
A and a node in set B.

0

1
3

0

2
4

1
5

True
False

0

2
3

True

L43 - Graphs Page 6

1

2

3

4

[HW] Clone Graph

Clone Graph
Given reference of a node in a connected undirected graph, return a deep copy (clone) of the
graph. Note that, each graph node contains a value ( int ) and a list ( List [ Node ] ) of its
neighbors.

...

L43 - Graphs Page 7

Graphs - Back Edge

Back Edge Detection
Given an directed graph design an algorithm to check if contains a back-edge.
v is said to be a back-edge if there exists a directed path
A directed edge u
from vertex v to vertex u.

1

1

0

2

L43 - Graphs Page 8

0

2

L43 - Graphs Page 9

