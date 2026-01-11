# Lecture 46

**Source:** `L46 -  Graphs.pdf`

---

Graphs - Disjoint Set
[HW] https://codeforces.com/edu/course/2/lesson/7/1/practice
[HW] https://cses.fi/problemset/task/1676

Disjoint Set
A disjoint set is a data structure which maintains a collections of dynamic
sets { S0, S1, S2 . . . } that are pairwise disjoint i.e. for any two sets Si and Sj
in the given collection where i≠j, Si ∩ Sj = Ø
The disjoint set data structure supports three main operations, these include
• createSet ( x )
to create a new set with a single member x ( leader/representative of set )
• unionSet ( x, y )
to create a set S as a union of sets, Sx & Sy that contains x & y respectively.

• findSet ( x )
returns the leader or representative of the set that contains the element x.

1

3

2

4

createSet ( 1 )
createSet ( 2 )
createSet ( 3 )
createSet ( 4 )

unionSet ( 2, 3 )

1

4

2, 3

findSet ( 3 )

unionSet ( 1, 4 )

1, 4

2, 3

findSet ( 4 )

unionSet ( 3, 4 )

1, 2, 3, 4

findSet ( 2 )

Disjoint Set Representation
There are two main strategies used to represent the disjoint set data structure

L46 - Graphs Page 1

• Linked List Representation
• Disjoint Forest Representation ( faster )

In the Disjoint Forest representation, we represent each set in the given set
collection using a Rooted Tree data structure i.e. a tree in which each node
points to its parent and each tree node corresponds to a member of the set.
Moreover, the root node of the tree corresponding to a given set points to
itself and is the leader or the representative of the set.

S1

1

2

3

4

5

S6

6

1

7

9

S10 10

6

2

3

10

7

4

8

5

Operations with Forest Representation
• createSet ( x )
• findSet ( x )
S1

1

2

3

4

5

1
2

3
4

5

unionSet ( x, y )
S1

1

2

3

4

5

S6

3
4

L46 - Graphs Page 2

7

9

6

1
2

6

7
5

8

2

3
4

8

7
5

Disjoint Set Implementation with Forest Representation
To implement the disjoint set data structure with the forest representation, we
will use a hash table to store a mapping b/w nodes and their parents.

S1

1

2

3

4

5

S6

6

7

9

vertex parent
1
1
2
1

2

3

4

5

8

7

4

1
3
3
6
6
6

3

6

1

6

5

7
8

Improving the efficiency of Disjoint Set operations
To reduce the depth of a tree we deploy two heuristics

• Union by rank ( or size )
The idea behind union by rank is, during the union operation, make the
root of the tree with lower rank point to root of the tree with higher rank.

6

1
2

3
4

7
5

1
2

6

or
6

3
4

8

5

7

1

8

2

7

8

3
4

5

• Path Compression
The idea behind path compression is, during the find operation, make every
L46 - Graphs Page 3

•

The idea behind path compression is, during the find operation, make every
node visited along the path to the root node, point to the root.
1

1
2

2

3

4

5

4

3

5

7

6

7

6

When we combine union by rank and path compression, on average the
time complexity of the find operation and the union operation is constant.

Applications of Disjoint Set
• It can be used to detect a cycle in an undirected graph.

2
1

3
4

V = { 1, 2, 3, 4 }
E = { { 1, 2 },
{ 2, 3 },
{ 3, 4 },
{ 4, 1 } }

• It can be used to count components in an undirected graph.
2
1

6
3

5

4

V = { 1, 2, 3, 4, 5, 6, 7 }
E = { { 1, 2 },
{ 1, 4 },
{ 2, 3 },
{ 3, 4 },
{ 5, 6 },
{ 6, 7}}

L46 - Graphs Page 4

7

Graphs - Minimum Spanning Tree

[HW] https://codeforces.com/problemset/problem/1559/D1

Minimum Spanning Tree ( MST )
Given a connected, undirected, weighted graph, design an algorithm to
its find the minimum spanning tree.
4

0

0

2

1
1

1

3

2

1

2
4

4

0

2

3

1

2

0

3

3

2
3

0

3

1
3

3

2

1

2

1

4

2

1

3

Kruskal's Algorithm
The idea behind the Kruskal's algorithm to find the MST for the given
connected, undirected, weighted graph that contains V vertices is to
choose V-1 edges in the increasing order of their weights such that at
no point of time inclusion of an edge in the sub-graph leads to a cycle.

1

4

2

3

6

2

7

5

9

4
1

5
3

7

6
8

Implementation of Kruskal's Algorithm

1

4

2
7

6

2

3
9

4
5

L46 - Graphs Page 5

5

1

6

7

9

4
1

5
3

6
8

7

[R][HW] Prim's Algorithm
1

4

2

5

3

6

2

7

9

4
1

5
3

6
8

7

Implementation of Prims Algorithm

1

4

2

3

6

2

7

5

9

4
1

5
3

7

6
8

Optimized Implementation of Prims Algorithm

L46 - Graphs Page 6

1

4

2

9

4
1

5
3

L46 - Graphs Page 7

3

6

2

7

5

7

6
8

[HW] Minimize Malware Spread

Minimize Malware Spread

0
1
2
3
4
5
6
7
8

0

1

2

3

4

5

6

7

8

1
0
1
0
0
0
0
0
0

0
1
0
1
0
0
0
0
0

1
0
1
0
1
0
0
0
0

0
1
0
1
0
1
0
0
0

0
0
1
0
1
0
0
0
0

0
0
0
1
0
1
1
0
0

0
0
0
0
0
1
1
0
0

0
0
0
0
0
0
0
1
1

0
0
0
0
0
0
0
1
1

L46 - Graphs Page 8

0

1

7

2

3

8

4

5
6

0
1
2
3
4
5

0
1
2
3
4
5

0

1

2

3

4

5

1
0
1
0
0
0

0
1
0
1
0
0

1
0
1
0
1
0

0
1
0
1
0
1

0
0
1
0
1
0

0
0
0
1
0
1

0

1

2

3

4

5

1
0
1
0
0
0

0
1
0
1
0
0

1
0
1
0
1
0

0
1
0
1
0
1

0
0
1
0
1
0

0
0
0
1
0
1

L46 - Graphs Page 9

0

1

2

3

4

5

0

1

2

3

4

5

0
1
2
3
4
5
6
7
8

0
2

1
3

0

1

2

3

4

5

6

7

8

1
0
1
0
0
0
0
0
0

0
1
0
1
0
0
0
0
0

1
0
1
0
1
0
0
0
0

0
1
0
1
0
1
0
0
0

0
0
1
0
1
0
0
0
0

0
0
0
1
0
1
1
0
0

0
0
0
0
0
1
1
0
0

0
0
0
0
0
0
0
1
1

0
0
0
0
0
0
0
1
1

2
2

3
4
5
6
3
2
3
3
parentMap

L46 - Graphs Page 10

7
8

8
8

0

0

1

7

2

3

8

4

5
6

1

2
3

3
4

4

5

rankMap

6

7

8
2

