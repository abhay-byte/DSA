# Lecture 42

**Source:** `L42 - Graphs.pdf`

---

Graphs - Introduction

Graphs
It is a non-linear data-structure that can be thought of as a collections of nodes
(or vertices) and edges.

0

2

V = { 0, 1, 2, 3, 4 }
4

1

3

0
1

E = { {0, 1},
{0, 2},
{1, 3},
{2, 3},
{2, 4},
{3, 4} }

V = { 0, 1, 2, 3, 4, 5, 6 }

4
6

2

5

3

E = { {0, 1},
{0, 2},
{1, 3},
{2, 3},
{4, 5},
{4, 6},
{5, 6} }

Formally, a graph is a pair of sets V and E where V is a non-empty set of
vertices and E is a set of edges such that each edge is a pair of vertices.

0

2

V = { 0, 1, 2, 3, 4 }
4

1

3

E = { {0, 1},
{0, 2},
{1, 3},
{2, 3},
{2, 4},
{3, 4} }

In a directed graph, each edge is an ordered pair of vertices.

0

2

V = { 0, 1, 2, 3, 4 }
4

L42 - Graphs Page 1

E = { (0, 2),
(1, 0),
(1, 3),
(2, 4),

4
1

3

E = { (0, 2),
(1, 0),
(1, 3),
(2, 4),
(3, 2),
(4, 3) }

In a weighted graph, each edge is assigned a weight.

0

15

2
9

7

4
5

1

20

V = { 0, 1, 2, 3, 4 }

10

3

E = { (0, 2, 15),
(1, 0, 7),
(1, 3, 20),
(2, 4, 10),
(3, 2, 9),
(4, 3, 5) }

Applications of Graphs
1. Social Networking Sites
▪ Users : can be thought as nodes in a graph
▪ Relationships : can be thought as edges between graph nodes.
2. Maps ( of a city )
▪ Checkpoints : can be thought as nodes in a graph
▪ Roads : can be thought as edges between graph nodes.

L42 - Graphs Page 2

Graphs - Terminology I

Graph Terminology
• In an undirected graph, if there exists an edge between two vertices then they
are said to be adjacent to each other.

0

2

4
1

3

• In an undirected graph, we define degree of a vertex as the number of vertices
adjacent to it.

v then we say that vertex
• In a directed graph, if there exists an directed edge u
u is predecessor of vertex v or vertex v is successor of vertex u.

0

2
4

1

3

• For directed graphs, we define in-degree of a vertex as the no. of predecessors it
has and out-degree of a vertex as the no. of its successors.

• In an undirected graph, two or more edges are said to be parallel edges if they are
incident on the same two vertices.

• In a directed graph, two or more edges are said to be parallel edges if they have the
same tail vertex and the same head vertex.

• In graph theory, we define a loop as an edge that connects a vertex to itself. A graph
that doesn't have parallel edges and loops is also known as a simple graph.

Minimum and Maximum Number of Edges in Graph
• The minimum no. of edges in a graph is zero, such a graph is known as empty graph.
• For maximum no. of edges in a graph, each vertex of the graph must be connected
with every other graph vertex.

0

2

0

2

1

3

1

3

Graph Representation
There are two key strategies that can be used to represent the graph data structure
□ Adjacency List
□ Adjacency Matrix
At a high-level, in each of these strategies, we internally implement the graphs using
arrays which is indexed by the graph vertices.

L42 - Graphs Page 3

Graphs - Adjacency List I

Adjacency List
To represent a graph that contains | V | vertices and | E | edges using adjacency list,
you've to create an array of size | V | such that at each index of the array you store a
list of neighbors that correspond to the vertex which has been mapped to that index.

0

0

1

2

3

4

1

0

0

1

2

2

3

3

2

3

4

4

2

4
1

3

Space Complexity
Assume you are given an undirected graph that contains | V | vertices and | E | edges.

0

4
1

0

1

2

3

4

1

0

0

1

2

2

3

3

2

3

4

4

2

3

Assume you are given an directed graph that contains | V | vertices and | E | edges.

0

4

1

0

1

2

3

4

2

0

4

2

3

2

3

L42 - Graphs Page 4

3

Graphs - Adjacency List II

Graph Operations
Assume you are given an graph that contains | V | vertices and | E | edges.

• List all the neighbors of a vertex 'u'

• Add an edge between vertex 'u' and 'v'

• Check if an edge exists between vertex 'u' and vertex 'v'

• Delete an edge between vertex 'u' and 'v'

L42 - Graphs Page 5

Graphs - Adjacency List III

Adjacency List
To represent a graph that contains | V | vertices and | E | edges using adjacency list,
you've to create an array of size | V | such that at each index of the array you store a
list of neighbors that correspond to the vertex which has been mapped to that index.

0

1

2

3

4

1

0

0

1

2

2

3

3

2

3

4

4

2
4

1

0

3

Drawbacks
Our current implementation fails when labels assigned to vertices are
○ integer values that exceed | V | -1
○ non-integer values

A

C
E

B

L42 - Graphs Page 6

D

Weighted Graphs

A

1

C

6

9

7

E
5

B

2

D

L42 - Graphs Page 7

A

B

C

D

E

B, 7

A, 7

A, 1

B, 2

C, 6

C, 1 D, 2

D, 9

C, 9

D, 5

E, 6

E, 5

Graphs - Adjacency Matrix

Adjacency Matrix
To represent a undirected graph that contains | V | vertices and | E | edges using
adjacency matrix, you've to create a 2D-Array of size | V | x | V | such that you
assign the value one to the cells at the (i, j)th index and (j, i)th index of the matrix
if there exists an edge between the vertices of the graph labelled as i and j resp.

0

2
4

1

3

0
0 0
1 1
2 1

1
1

2
1

3
0

0

0

1

4
0
0

0

0

1

1

3 0

1
0

1

0

1

1

1

0

4

0

Graph Operations
Assume you are given an graph that contains | V | vertices and | E | edges.
• Add an edge between vertex 'u' and 'v'

• Check if an edge exists between vertex 'u' and vertex 'v'
• Delete an edge between vertex 'u' and 'v'
• List all the neighbors of a vertex 'u'

Adjacency List vs Adjacency Matrix

L42 - Graphs Page 8

Adjacency List vs Adjacency Matrix

If the graph is sparse i.e. it has less number of edges then one should represent it
using adjacency list. In contrast, if the graph is dense i.e. it has high number of
edges then one should represent it using adjacency matrix.
We know that, for a graph that contains | V | number of vertices and | E | edges the
space required to represent it using adjacency list is O( | V | + | E | ) and the space
required to represent it using adjacency matrix is O ( | V |2 ).

L42 - Graphs Page 9

Graphs - Terminology II

Graph Terminology
• Walk
A walk in a graph is a sequence of vertices such that any two vertices adjacent in
the vertex sequence are also adjacent in the graph.
A

C
E

B

D

Moreover, we say that a walk is closed is it starts and ends at the same graph vertex.

• Path

A path in a graph is a walk in which we visit each vertex of the graph at most once.

A

C
E

B

D

• Cycle
A cycle in a graph is a closed walk in which we traverse each graph edge at most once.

A

C
E

B

D

A graph without any cycle is also known as an acyclic graph.

• Connected-Graph
A graph is connected if there exists a path between each pair of graph vertices.

A

C
E

B

D

A graph is which is not connected is also known as a disconnected graph.

L42 - Graphs Page 10

• Strongly-Connected Graph
A directed graph is strongly-connected if there exists a directed path between
each pair of vertices in the graph.
0

2

0

2

1

3

1

3

A directed graph is weakly-connected if there exists a undirected path between
each pair of vertices in the graph.

• Sub-Graph
A sub-graph of a graph G = {V, E} is a graph G' = {V', E'} such that V' and E' are
subsets of V and E respectively.

A

C
E

B

D

A proper sub-graph of a graph is a sub-graph which is the graph itself.

• Component

A component of a graph is a sub-graph which is maximally connected.

0
1

4
6

2
3

5

A graph that has multiple components is a disconnected graph.

L42 - Graphs Page 11

• Spanning Tree
A spanning tree of a connected graph is a sub-graph which is a tree and contains all
the vertices of the graph.

A

B

A

C

A

C

B

D

B

D

A

C

A

C

B

D

B

D

C

D

L42 - Graphs Page 12

