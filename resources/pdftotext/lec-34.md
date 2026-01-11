# Lecture 34

**Source:** `L34 - Heaps.pdf`

---

Perfect Binary Tree

Perfect Binary Trees
A binary tree is said to be a perfect binary tree if all its levels are completely filled
i.e. every internal node in the binary tree has exactly two child nodes.

level 0

level 1
level 2

The height of a perfect binary tree is logarithmic.

level 0

level 1
level 2

level k

This is a finite GP where,

20 + 21 + 22 + 23 + … + 2k = n
a = 20 =1
r=2
# = k+1

The sum of finite GP given as follows
= a * [ (r#-1) / ( r-1) ]
L34 - Heaps Page 1

Substituting the values of a, r, and #, we get
= 1 * [ (2k+1-1) / ( 2-1) ]
= 2k+1-1
~ 2k
Therefore,
2k = n
k = log2n

The number of nodes in a perfect binary tree that has n nodes at a height h is
n / 2h+1

2

1

0

height
0
1
2

1

0

0

L34 - Heaps Page 2

0

#
4
2
1

Complete Binary Tree

Complete Binary Trees
A binary tree is said to be a complete binary tree if all its levels are completely filled
except for the last level which may or may not be filled. And, in case the
last level is partially filled then it is filled in the left to right direction.

The height of a complete binary tree is logarithmic.

The max. no. of nodes in a complete binary tree that has n nodes at a height h is n / 2h+1

Linear Representation of Complete Binary Trees
A

C

B
D
0

F

E
1

2

L34 - Heaps Page 3

3

G
4

5

6

Heap - Introduction

Heap
It is a kind of complete binary tree in which every node satisfies the heap property.

Types of Heap
▪ Min-Heap - optimized for operations on minimum element

▪ Max-Heap - optimized for operations on maximum element

Min-Heap
It is a kind of complete binary tree in which every node satisfies the min-heap property.
The min-heap property states that value of each node in the heap must be less than the
value of all the nodes in its left subtree and its right subtree.

1

2

3
7
9

L34 - Heaps Page 4

5
8

4

6

Max-Heap
It is a kind of complete binary tree in which every node satisfies the max-heap property.
The max-heap property states that value of each node in the heap must be greater than
the value of all the nodes in its left subtree and its right subtree.

9

8

7
5
2

L34 - Heaps Page 5

4
1

6

3

Heap - Implementation

Implementation of Heaps

Linear Representation of Heaps

0

1

2

1

2

3
5

4

3

7

5

0

1

2

3

4

5

6

7

1

3

2

7

5

4

6

8

6

4

6

7

8

Heap Operations
1. Push : to insert an element onto the heap.
2. Pop : to delete and return the smallest/largest element from the heap.
3. Top : to access the smallest/largest element without popping from the heap.

4. Size : return the size of the heap
5. Empty : return True is heap is empty, False otherwise.

L34 - Heaps Page 6

Heap - Operations

Heap Push Operation

1

2

3

7

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

1

3

2

7

5

4

6

8

0
0

1
1

2
2

3
3

4
5

5
4

6
6

7
8

0
7

1
1

2
2

3
3

4
5

5
4

6
6

7
8

8

6

8

Heap Pop Operation

0

2

1

3
8

4

5

6

7

7

2

1

3

5

4

8

L34 - Heaps Page 7

6

8
7

Merge Ropes

Merge Ropes
Given the lengths of N ropes, design an algorithm to compute the minimum cost to
connect these N ropes into one rope such that any point of time you can only merge
two ropes and cost to connect two ropes is equal to the sum of their lengths.
Example
Input : [4, 3, 2, 6]
Output : 29

L34 - Heaps Page 8

Build Heap from Array

Building Heap from an Array

arr

1

2

10

20 50

3

4

30 40

50

50

40

20

0

50

40

30

30

10

10

20

arr

30

40

20

0

1

10

20 50

50

2

10

3

10

4

30 40

0

10

arr

0

1

2

10

20 50

3

4

30 40

1

3

30

2

20
4

40

0
L34 - Heaps Page 9

30

50

40

20

0

50

arr

0

1

2

50

40 30

3

4

20 10

1

2

40

3

30

4

20

10

0

10

arr

0

1

2

10

20 50

3

4

30 40

1

2

20

3

30

50

4

40

The heapify operation, in worst case, takes time proportional to the height of the
node on which it invoked.
The maximum number of nodes in a complete binary tree at a height h ~ n / 2h+1

The total amount of work done at nodes which are at height h,
( n / 2h+1) * O ( h )

Therefore, the total amount of work done at all the non-leaf nodes,
log2n

∑ ( n / 2h+1) * O ( h )

h=1
L34 - Heaps Page 10

log2n

∑ ( n / 2h+1) * O ( h )

h=1

log2n

∑ ( n / 2h+1) * O ( h )

h=1

log2n

<

∑ ( n / 2h+1) * O ( h )

h=0
∞

<

∑ ( n / 2h+1) * O ( h )

h=0
∞

=

∑ ( n / (2.2h) ) * h.c

h=0

∞

= nc/2 ∑ ( 1 / 2h ) * h
h=0

∞

= nc/2 ∑ ( h / 2h )
h=0

=

L34 - Heaps Page 11

n.c ~ O ( n )

[R][HW] Heap Sort

Heap Sort Algorithm
Given an array of n integers, sort them using the heap-sort algorithm.
Example :
Input :
0

1

2

3

4

20

10 50

40 30

0

1

3

10

20 30

Output :
2

4

40 50

0

20
0

1

2

20

10 50

3

4

40 30

1

3

40

2

10

50

4

30

0

50
0

1

50

40 20

L34 - Heaps Page 12

2

3

4

10 30

1

40

2

20

0

1

2

50

40 20

3

4

10 30

1

3

10

L34 - Heaps Page 13

2

40
4

30

20

