# Lecture 26

**Source:** `L26 - Recursion.pdf`

---

N Queens
N-Queens Optimization Recording
https://drive.google.com/file/d/1Ppn1s_KM9TlMdXLjI9S6NonDIECzLkM6/view?usp=sharing

N Queens
Given a N x N chessboard, and N queens, design a recursive algorithm to
place the queens on the chessboard such that no two queens attack each
other _ we say that two queens will attack each other when they are placed
along the same row, column or diagonal.
Example

N=4
0
0
1
2
3

1
Q0

2

3

0
0
1
2
3

Q1
Q2
Q3

1

2
Q0

3

Q1
Q2
Q3

0

j

N-1

0

r-1
r

.

r+1

N-1
NxN

L26 - Recursion Page 1

j

0
.
.
.

r-4

r-3
r-2
r-1

.

r

j

0
.
.
.

r-4
r-3

r-2
r-1
r

.

j

0
.
.
.

r-4
r-3

r-2
r-1
r

L26 - Recursion Page 2

.

[R][HW] Solve Sudoku

Solve Sudoku
Given a partially filled 9x9 Sudoku Grid, design a recursive algorithm to
assign a digit in the range 1 to 9 to all the empty cells such that each row,
column & √9 x √9 sub-grid contain exactly one instance of a digit.
Example
3
5
.

.
2
8

6
.
7

5
.
.

.
.
.

8
.
.

4
.
.

.
.
3

.
.
1

.
9
.

.
.
5

3
.
.

.
8
.

1
6
9

.
3
.

.
.
6

8
.
.

.
5
.

1
.
.

3
.
.

.
.
5

.
.
2

.
.
.

.
.
6

2
.
3

5
7
.

.
4
.

0

j

0

i

.
L26 - Recursion Page 3

N-1

i

.

N-1
NxN

3
5
.

.
2
8

6
.
7

5
.
.

.
.
.

8
.
.

4
.
.

.
.
3

.
.
1

.
9
.

.
.
5

3
.
.

.
8
.

1
6
9

.
3
.

.
.
6

8
.
.

.
5
.

1
.
.

3
.
.

.
.
5

.
.
2

.
.
.

.
.
6

2
.
3

5
7
.

.
4
.

L26 - Recursion Page 4

Time & Space Complexity Analysis of Recursive Algorithms

Time & Space Complexity Analysis of Recursive Algorithms

L26 - Recursion Page 5

L26 - Recursion Page 6

L26 - Recursion Page 7

L26 - Recursion Page 8

L26 - Recursion Page 9

L26 - Recursion Page 10

