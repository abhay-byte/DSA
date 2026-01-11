# Lecture 36

**Source:** `L36 - HashMaps.pdf`

---

Contains Duplicate I

Contains Duplicate I
Given a array of N integers values, design an algorithm to check if there
exists a duplicate value in the given array or not.
Example
0

1

2

3

1

2

3

1

0

1

2

3

1

2

3

4

L36 - HashMaps Page 1

[HW] Contains Duplicate II

Contains Duplicate II
Given a array of N integers values and an integer K, design an algorithm to
check if there exists two distinct indices i and j such that values at the ith
and jth indices of the given array are equal and abs( i - j ) <= K.
Example

K=3
0

1

2

3

1

2

3

1

0

1

2

3

4

5

1

2

3

1

2

3

K=2

L36 - HashMaps Page 2

Longest Palindrome

Longest Palindrome
Given a string which consists of lowercase or uppercase letters, design an
algorithm to find the length of the longest palindrome that can be build
with those letters.
Example

Input : "abccccdd"
Output : 7

L36 - HashMaps Page 3

Longest Consecutive Sequence

Longest Consecutive Sequence
Given an unsorted array of integers nums, design an algorithm to
find the length of the longest sequence of consecutive elements.
Example
2

3

4

5

6

100 4 200
Output : 4

0

1

3

2

101 201 102

0

1

1

7

8

2

3

4

5

6

7

8

9

0
3
7
Output : 9

2

5

8

4

6

0

1

L36 - HashMaps Page 4

[R][HW] Count Triangles

Count Triangles
Given N cartesian points in a 2D plane, count the number of right-angled triangles that
can be formed whose base or perpendicular is parallel to the x-axis or the y-axis.
Example :
Input : [ (1, 2), (2, 1), (2, 2), (2, 3), (3, 2) ]

•
•

•

•

•
Output : 4

•

•
•

•

•

L36 - HashMaps Page 5

•

•

•

Input : [ (1, 2), (2, 1), (2, 2), (2, 3), (3, 2) ]

x-coordinate

frequency

xFreqMap

L36 - HashMaps Page 6

y-coordinate

frequency

yFreqMap

[HW] Count Rectangles

Count Rectangles
Given N cartesian points in a 2D plane, design an algorithm to count the number of
axis-parallel rectangles that can be formed from the given set of points.
Example :
Input : [ (1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2) ]

•

•

•

•

•

•

Output : 3

L36 - HashMaps Page 7

•

•

•

•

L36 - HashMaps Page 8

•

•

•

•

Find the Duplicate Number I

Find the Duplicate Number I
Given a array of integers containing N+1 integers where each integer is in
the range [1, N] inclusive. Design an algorithm to find the duplicate
number given that there is only one repeated number.
Example
0

1

2

3

4

1

3

4

2

2

0

1

2

3

4

3

1

3

4

2

L36 - HashMaps Page 9

0

1

2

3

4

1

3

4

2

2

0

1

2

3

4

3

1

3

4

2

0

1

2

3

4

1

3

4

2

2

[HW] Find the Duplicate Numbers II

Find the Duplicate Number II
Given a array of integers containing N integers where each integer is in the
range [0, N-1] inclusive. Find all the duplicate numbers present in the
given array in constant space.

Example
0

1

2

3

4

1

0

1

0

2

0

1

2

3

4

1

2

2

2

3

L36 - HashMaps Page 10

Homework

https://cses.fi/problemset/task/1661
[R] https://leetcode.com/problems/find-duplicate-subtrees/
[R] https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

L36 - HashMaps Page 11

