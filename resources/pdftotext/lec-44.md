# Lecture 44

**Source:** `L44 - Graphs.pdf`

---

Max Area of Island

Max Area of Island
Given a two-dimensional grid that contains 0's and 1's where 0 represents water
and 1 represents land. We define an island as a group of 1's (representing land)
connected four-directionally ( horizontal & vertical ). Design an algorithm to find the
area of the largest island - area of an island is the number of 1's it contains.
Example
Input :

1
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
0
0
0

0
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
0
0
1
1

0
0
1
1
0

1
0
0
1
1

0
0
1
1
0

Output : 8

1
1
0
1
1

L44 - Graphs Page 1

[HW] Making a Largest Island

[editorial] https://leetcode.com/problems/making-a-large-island/editorial/

Making a Largest Island
Given a two-dimensional grid that contains 0's and 1's where 0 represents water and
1 represents land. We define an island as a group of 1's (representing land)
connected four-directionally ( horizontal & vertical ). Design an algorithm to find the
area of the largest island - area of an island is the number of 1's it contains such
that you can change at-most one of the 0's into a 1.
Example
Input :

1
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
0
0
0

0
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
0
0
1
1

0
0
1
1
0

1
0
0
1
1

0
0
1
1
0

Output : 11

1
1
0
1
1

L44 - Graphs Page 2

Graphs - Topological Sorting

Topological Sorting of a DAG
Topological Sorting of a directed acyclic graph or DAG is a linear ordering of its
vertices such that for each directed edge from vertex u to vertex v in the graph, u
comes before v in the linear ordering.
0

1

2

3

4

5

6

7
0

1

3

4

6

0

7

5

2

5

2

1

2

3

4

5

6

7
0

1

3

4

6

7

BFS Implementation ( Kahn's Algorithm )
To perform topological sorting of a DAG using the BFS algorithm, we will maintain

• a Queue to track nodes whose dependencies have been resolved i.e. in-degree is 0.
• a HashMap to store a mapping b/w vertices and their in-degrees.

0
2

vertex in-degree
0
0
1
1
2
3
3
2
4
2
5
2
6
2
7
2

1
3

5

0

4
6

7

[HW] DFS Implementation

0

2

1
3

5

4
6

7

Cycle Detection using Topological Sorting

L44 - Graphs Page 3

L44 - Graphs Page 4

[HW] Graphs - Course Schedule II

Course Schedule II

Example
numCourses 4
prerequisties

1

0

2

0

3

1

3

2

1

0

2

0

3

1

3

2

numCourses 5
prerequisties

.

L44 - Graphs Page 5

[HW] Alien Dictionary

Alien Dictionary

.

L44 - Graphs Page 6

Graphs - SSSP

Single Source Shortest Path (SSSP)
Given a connected graph and source vertex design an algorithm to find the length
of the shortest path from the source vertex to all the other vertices.

vertex distance
0
0
1
1
2
1
3
2
4
2
5
2
6
3
7
3
8
4

0
1

2

3

4

5

6

7
8

SSSP using BFS Algorithm

0

0

1

2

3

1

4

3

5

6

7

2

4
6

8

5
7

8

vertex distance
0
0
1
2
3
4
5
6
7
8

BFS Implementation for SSSP

0
1

3

2

4
6

7

8

queue

5

0

L44 - Graphs Page 7

vertex distance
0
0
1
2
3
4
5
6
7
8

[R][HW] Snake and Ladder

Snakes and Ladders Game
Given a Snakes & Ladders board of size N that contains multiple snakes and
ladders. You are also given their starting and ending positions. Design an
algorithm to find the minimum no. of throws of a six-sided die required to
reach the Nth cell of the board from its 1st cell such that as per game rules -

➢ If you are bitten by a snake ( by reaching at a cell having a snake head )
you will go down to the cell at which the tail of the snake ends.
➢ If you reach a cell at which a ladder starts, you will climb the ladder.

Example
Input : N = 36
ladderPos = [ (2, 15), (5, 7), (9, 27), (18, 29), (25, 35) ]
snakePos = [ (17, 4), (20, 6), (24, 16), (32, 30), (34, 12) ]
Output : 4

L44 - Graphs Page 8

36

35

34

33

32

31

25

26

27

28

29

30

24

23

22

21

20

19

13

14

15

16

17

18

12

11

10

9

8

7

1

2

3

4

5

6

.

L44 - Graphs Page 9

[R][HW] All Nodes Distance K in Binary Tree

All Nodes Distance K in Binary Tree
Given the root of a binary tree, a target node and an integer K, return
an array of values of all the nodes at distance K from the target node.

target = 5
K=2

queue

.

L44 - Graphs Page 10

