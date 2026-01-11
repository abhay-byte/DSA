# Lecture 18

**Source:** `L18 - 2D Arrays.pdf`

---

Introduction to 2D Array

Introduction to 2D Arrays
A 2D-array is an array of 1D arrays, referred by a single name, which is used to
store a sequence of values of the same type and can be visualized as a matrix.

10 15 20 25
30 35 40 45
50 55 60 65
3x4

How to declare a 2D-array in C++ ?

A 2D-array is allocated a contiguous block of memory to store its elements.
0

1

2

3

10 15 20 25
30 35 40 45
50 55 60 65

0
1
2

This allocation of contiguous memory is done either in the row-wise manner a.k.a
row-major order or in a column-wise manner a.k.a column-major order.

• Row-Major Order
0
0

1

1
2

3

0

10 15 20 25

1

2
2

3

0

30 35 40 45

1

2

3

50 55 60 65
0

0
1

• Column-Major Order
0
0

1

2
1

2

10 30 50

0

1

2
2

15 35 55

L18 - 2D Arrays Page 1

0

1

3
2

20 40 60

0

1

2

25 45 65

1

2

3

10 15 20 25
30 35 40 45
50 55 60 65

Accessing an element in a 2D array
0
0
1
2

1

2

3

10 15 20 25
30 35 40 45
50 55 60 65

0
0

1

1
2

3

10 15 20 25

0

1

2
2

3

0

30 35 40 45

1

2

3

50 55 60 65

Since 2D-arrays are allocated memory in a contiguous manner, accessing an element in
a 2D-array is a constant time i.e. O (1) operation.

2D-Array Initialization
By default, when we declare a 2D-array in the local-scope, it contains garbage value.

0

arr

0
1

2

1

2

During the initialization of a 2D-array, specifying the no. of rows is optional.

While initializing a row in a 2D-array, the size of the initializer list must not
exceed the no. of columns in the 2D-array.

What if the size of the row initializer list is less than the no. of columns ?

L18 - 2D Arrays Page 2

3

10 15 20 25
30 35 40 45
50 55 60 65

0
0

1
2

L18 - 2D Arrays Page 3

1

2

3

10 15 20 25
30 35 40 45
50 55 60 65

Wave Print

Wave Print
Given an integer matrix of dimensions m x n, write a program that
prints the matrix in the wave form.
Example
Input
0
0
1
2

1

2

10 20 30
40 50 60
70 80 90

Output
10 40 70 80 50 20 30 60 90

L18 - 2D Arrays Page 4

Transpose a Matrix

Transpose a Square Matrix
Given an square matrix of integers of dimensions n x n, write a program to transpose it.

0
1
2
3

0

1

2

3

11
15
19
23

12
16
20
24

13
17
21
25

14
18
22
26

Input

L18 - 2D Arrays Page 5

0
1
2
3

0

1

2

3

11
12
13
14

15
16
17
18

19
20
21
22

23
24
25
26

Output

[HW] Rotate Image

https://leetcode.com/problems/rotate-image/

L18 - 2D Arrays Page 6

2D Arrays and Pointer

Pointers and 1D-arrays
In C++, we can think of name of an array as a pointer to the element at the 0th index.

arr

index

0

value

10 20 30 40 50

1

2

3

4

address 100 104 108 112 116

Pointers and 2D-arrays

0

arr

0

1

1
2

3

0

1

3

0

1

2

3

10 15 20 25

30 35 40 45

50 55 60 65

100 104 108 112

116 120 124 128

132 136 140 144

arr[0]

arr[1]

arr[2]

0

arr

2
2

0

1

1
2

3

0

1

2
2

3

0

1

2

3

10 15 20 25

30 35 40 45

50 55 60 65

100 104 108 112

116 120 124 128

132 136 140 144

arr[0]

arr[1]

arr[2]

L18 - 2D Arrays Page 7

L18 - 2D Arrays Page 8

Matrix Search

Matrix Search
Given an integer matrix of dimensions m x n, and a target integer T, write a
program to search for the target in the given matrix.

Example
Input : T = 10
0
0
1
2

1

2

50 80 20
90 10 70
60 30 40

Output : True

L18 - 2D Arrays Page 9

Sorted Matrix Search I

Sorted Matrix Search I
Given an integer matrix of dimensions m x n, which is sorted row-wise and a
target integer T, write a program to search for the target in the given matrix.
Example

Input : T = 50
0
0

1
2

1

2

40 50 60
10 20 30
70 80 90

Output : True

L18 - 2D Arrays Page 10

L18 - 2D Arrays Page 11

Sorted Matrix Search II

Sorted Matrix Search II
Given an integer matrix of dimensions m x n, which is sorted row-wise and
column-wise and a target integer T, write a program to search for the target in
the given matrix.
Example
Input : T = 50
0

0
1

2

1

2

10 20 30
40 50 60
70 80 90

Output : True

0
0
1
2

1

2

10 20 30
25 50 60
70 80 90

L18 - 2D Arrays Page 12

[HW] Count Negative Numbers in Sorted Matrix

https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

L18 - 2D Arrays Page 13

[R][HW] Spiral Print a Matrix

Spiral Print a Matrix
Given an integer matrix of dimensions m x n, design an algorithm to print the
matrix spirally in a clock-wise direction.
Example

Input
0
1
2
3

0

1

2

3

11
22
21
20

12
23
26
19

13
24
25
18

14
15
16
17

Output
11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

0
1
2
3

0

1

2

3

11
22
21
20

12
23
26
19

13
24
25
18

14
15
16
17

L18 - 2D Arrays Page 14

[R][HW] Diagonal Traversal

Diagonal Traversal
Given an integer matrix of dimensions m x n, design an algorithm to traverse the
matrix diagonally.
Example
Input
0
0

1
2

1

2

3

11 12 13 14
15 16 17 18
19 20 21 22

Output
19 15 20 11 16 21 12 17 22 13 18 14

0
1
2
3

0

1

2

3

11
22
21
20

12
23
26
19

13
24
25
18

14
15
16
17

L18 - 2D Arrays Page 15

[R][HW] Diagonal Sort a Matrix

Diagonal Sort a Matrix
Given an integer matrix of dimensions m x n, write a program to sort it diagonally.
Input
0
0
1
2

1

2

50 80 20
90 10 70
60 30 40

Output
0
0
1
2

1

2

10 70 20
30 40 80
60 90 50

L18 - 2D Arrays Page 16

[R][HW] 2D Prefix Sum

[HW] https://cses.fi/problemset/task/1652

2D Prefix Sum
You are given a 2d-array of MxN integers, and Q queries, each of the form (li,ri)
and (lj,rj) where 0<=li,ri<=lj,rj<=N-1. Your task is to find for each of the
Q queries sum of all elements within the submatrix defined by the top-left corner
(li,ri)and the bottom-right corner (lj,rj).
Example
N=5

0
1

2
3

4

Q=3
0

1

2

3

4

2
4
6
9
0

3
7
8
5
6

0
9
1
4
8

1
3
0
2
6

5
2
4
3
1

Q0

0

0

1

1

Q1

1

2

3

4

Q2

2

0

4

1

j

L18 - 2D Arrays Page 17

.

i

MxN

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
4
6
9
0

3
7
8
5
6

0
9
1
4
8

1
3
0
2
6

5
2
4
3
1

0

0
1

2
3

4

j

L18 - 2D Arrays Page 18

1

2

3

4

.

i

MxN

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
4
6
9
0

3
7
8
5
6

0
9
1
4
8

1
3
0
2
6

5
2
4
3
1

L18 - 2D Arrays Page 19

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
6
12
21
21

5
16
30
44
50

5
25
40
58
72

6
29
44
64
84

11
36
55
78
99

