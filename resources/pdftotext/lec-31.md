# Lecture 31

**Source:** `L31 - Binary Trees.pdf`

---

Introduction to Trees

L31 - Binary Trees Page 1

L31 - Binary Trees Page 2

Tree Terminology

L31 - Binary Trees Page 3

Tree Traversal

L31 - Binary Trees Page 4

L31 - Binary Trees Page 5

Depth First Traversal - 1

10 20 40 -1 -1 50 70 -1 -1 -1 30 -1 60 -1 -1

-1 40 -1 20 -1 70 -1 50 -1 10 -1 30 -1 60 -1

-1 -1 40 -1 -1 70 -1 50 20 -1 -1 -1 60 30 10

L31 - Binary Trees Page 6

Fast Depth First Traversal

L31 - Binary Trees Page 7

L31 - Binary Trees Page 8

Build Tree from Preorder Traversal

L31 - Binary Trees Page 9

L31 - Binary Trees Page 10

[HW] Build Tree from Post-order Traversal

L31 - Binary Trees Page 11

Sum of Nodes

L31 - Binary Trees Page 12

[R][HW] Construct String from Binary Tree

Construct String from Binary Tree

1

1
2
4

2

3
4

5

1(2(4)(5))(3)

L31 - Binary Trees Page 13

1

2
5

1(2(4)(5))

3

4

1()(2(3)(4))

root

LST

L31 - Binary Trees Page 14

RST

Mirror / Invert a Binary Tree

L31 - Binary Trees Page 15

Height of a Tree

L31 - Binary Trees Page 16

[R][HW] Flip Equivalent Binary Tree

Flip Equivalent Binary Tree
Given the roots of two binary trees, root1 and root2, check if the two trees are
flip-equivalent or not. A binary tree X is flip-equivalent to a binary tree Y if and
if we can make X equal to Y after some number of flip operations __ for a binary
tree, we can define a flip operation as follows : choose any tree node, and swap
its left subtree with its right subtree.

L31 - Binary Trees Page 17

[R][HW] Tree Traversal using Iterative DFS

PreOrder Traversal

0
1

3
6

2
5

4
7

InOrder Traversal

L31 - Binary Trees Page 18

8

0
1

3
6

2
5

4
8

7

PostOrder Traversal

0
1
3
6

2
5

4
7

L31 - Binary Trees Page 19

8

[R][HW] Morris Tree Traversal

Morris Tree Traversal

0
1
3
6

PreOrder Traversal

L31 - Binary Trees Page 20

2
5

4
7

8

0
1

3
6

2

5

4
8

7

InOrder Traversal

0
1
3
6

2
5

4
7

L31 - Binary Trees Page 21

8

PostOrder Traversal

0

1
3
6

2
5

4
7

L31 - Binary Trees Page 22

8

