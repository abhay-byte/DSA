# Lecture 45

**Source:** `L45 - Graphs.pdf`

---

01 Matrix

01 Matrix
Given a m x n binary matrix mat, for each cell find the distance to the
nearest cell with the value 0 such that distance b/w adjacent cells is 1.

0
1
2
3
4

0
1
2
3
4

0
1
2
3
4

0

1

2

3

4

1
1
1
1
1

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

1
1
1
1
1

0

1

2

3

4

0
1
1
1
0

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

0
1
1
1
0

0

1

2

3

4

1
1
1
1
1

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

1
1
1
1
1

0

1

2

3

4

0
1
1
1
0

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

0
1
1
1
0

0
1
2
3
4

0
1
2
3
4

0

1

2

3

4

4
3
2
3
4

3
2
1
2
3

2
1
0
1
2

3
2
1
2
3

4
3
2
3
4

0

1

2

3

4

0
1
2
1
0

1
2
1
2
1

2
1
0
1
2

1
2
1
2
1

0
1
2
1
0

0
.

0
0
1
2
3
4

0

0

L45 - Graphs Page 1

0

0

0

0
1
2
3
4

0

1

2

3

4

0
1
1
1
0

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

0
1
1
1
0

0

0

queue

L45 - Graphs Page 2

0

0

[HW] Rotten Oranges

Rotten Oranges

2
0
1
2
3
4

0

1

2

3

4

2
1
1
1
2

1
1
1
1
1

1
1
0
1
1

1
1
1
1
1

2
1
1
1
2

0

2
L45 - Graphs Page 3

2

2

4

2

1

1

1

2
2

L45 - Graphs Page 4

2

Graphs - Dijkstra

[HW] https://codeforces.com/problemset/problem/20/C
[HW] https://cses.fi/alon/task/1195
[HW] https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

SSSP using Dijkstra's Algorithm
Given a weighted graph and source vertex design an algorithm to find the
length of the shortest path from the source vertex to all the other vertices.

1

3

1

9

8
4

3

0

5

2

2

vertex distance
0
0
8
1
5
2
9
3
7
4

10

Tensed Edge and Edge Relaxation

u

src

wuv

v

Dijkstra's Algorithm
To solve the SSSP problem for weighted graphs using the Dijkstra's algorithm,
iterate over all the vertices in the graph for which the shortest distance from the
source has been computed, and relax all the tensed edges incident on them.

3
8
4

1

1

9

2

vertex distance
0
0
1
∞

10
3

2

0
5

2
3
4

∞
∞
∞

Dijkstra's Implementation
To implement the Dijkstra's algorithm, we will maintain two data structures

• To keep track of graph vertices that have been explored.
▪ We will use a Set for this purpose.
▪ A vertex is marked as explored if its shortest distance from source has been
computed and all the tensed edges incident on it have been relaxed.
• To keep track of graph vertices that have not been explored.
▪ We will use a Min-Heap for this purpose.
L45 - Graphs Page 5

▪ We will use a Set for this purpose.
▪ A vertex is marked as explored if its shortest distance from source has been
computed and all the tensed edges incident on it have been relaxed.
• To keep track of graph vertices that have not been explored.
▪ We will use a Min-Heap for this purpose.
▪ Each item inside the Min-Heap will be a pair ◊ tentative shortest distance of vertex from source
◊ label of vertex

3

1
9

8
4

3
8

4

1

2

1

3
2

0

2

∞
∞
∞

3

5

.
.
.
.
Set

4

Map

1

9

2

explored
.

vertex distance
0
0
1
∞

10

vertex distance
0
0
1
∞

10
3

0

2

2

.
.
.
.
Set

∞
∞
∞

3

5

explored
.

4

Map

Path Construction

3
8

4

Correctness of Dijkstra's Algorithm
L45 - Graphs Page 6

1

1

9

2

10
3

2

0
5

unexplored
( 0, 0 )
( ∞, 1 )
( ∞, 2 )
( ∞, 3 )
( ∞, 4 )

min-Heap

unexplored
( 0, 0 )

min-Heap

Correctness of Dijkstra's Algorithm

Dijkstra's algorithm doesn't work for graphs with a negative weight edge.

1

2

1
0

3
-3

4

2

Is Dijkstra' algorithm exhaustive ?

For a weighted graph, the SSSP problem isn't defined if the graph contains a negative weight cycle.

0

1

1

2

2

3

3

-3

[R][HW] Implementation of Dijkstra's algorithm using priority_queue<>

3
8
4

1

1

9

2

10
3

2

vertex distance
0
0
1
∞

0
5

L45 - Graphs Page 7

2

∞
∞
∞

3
4

Map

explored
.

unexplored
.

.
.
.
.
Set

.
.
.
.
min-Heap

L45 - Graphs Page 8

[R][HW] Graphs - Bellman Ford
[HW] https://leetcode.com/problems/cheapest-flights-within-k-stops/

SSSP using Bellman-Ford Algorithm
The Bellman-Ford algorithm can solve the SSSP in case the graph contains
negative weight edges. Also it can be used to detect a negative weight
cycle in a graph.

1

2

2

1

-3

4

2

0

2

-3

0

3

1

1

For a weighted graph, containing V vertices, the minimum no. of edges along
the shortest path from the source to a destination vertex is 0 & the maximum
number of edges along the shortest path is equal to V - 1.
If however, the number of edges along the shortest path between the source
vertex and destination vertex exceeds V - 1 then we can say the shortest path
between the source and destination vertex contains a negative weight cycle.

Bellman-Ford Algorithm
The idea behind the Bellman-Ford algorithm for solving the SSSP problem for
weighted graph that contains V vertices is to relax all the its edges V - 1 times.

3

6

1

1

4

1

2
0

1

4

0
1

2

L45 - Graphs Page 9

5

2
3
4

0
0

∞
∞
∞
∞

1

2

3

4

How to detect a negative weight cycle using Bellman-Ford ?

To detect a negative weight cycle, we relax all the edges of the graph once
more. If the distances of >=1 vertex from the source vertex improve, then we
can conclude that the graph contains a negative weight cycle.

2
0

2

-3

0
1

2

1

1

0
0

1

2

3

∞
∞

Can we use Bellman-Ford algorithm for undirected graph ?

Is Bellman-Ford algorithm exhaustive ?

3

6

1

1

4

1

2
0

1

4
2

L45 - Graphs Page 10

0
1

5

2

3
4

0
0

∞
∞
∞
∞

1

2

3

4

[R][HW] Graphs - Floyd Warshall's Algorithm

[HW] https://codeforces.com/problemset/problem/295/B

All Pairs Shortest Path using Floyd Warshall's Algorithm
Given a weighted graph, find the shortest path between all pairs of vertices.

8

1

2

5

1
3

3

2

4

i

L45 - Graphs Page 11

1
2
3
4

1

2

3

4

0
6
1
4

6
0
5
2

1
5
0
3

4
2
3
0

j

i

L45 - Graphs Page 12

k

j

The Floyd-Warshall's algorithm can detect a negative weight cycle in a graph.

1

1
3

L45 - Graphs Page 13

8

2

-5

3

2
4

