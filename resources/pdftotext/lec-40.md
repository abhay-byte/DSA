# Lecture 40

**Source:** `L40 - Dynamic Programming.pdf`

---

Minimum Sum Path

Minimum Sum Path
Given a (m x n) grid containing non-negative integers, design a recursive algorithm to
compute the sum of numbers along the minimum sum path to reach the (m-1, n-1)th cell
from the (0,0)th cell such that at each step you can either move in down or right direction.
Example :
Input :
grid =

1
1
4

3
5
2

1
1
1

Output : 7
Explanation : The path 1 → 3 → 1 → 1 → 1 minimizes the sum.

0

1

n-1

.....

0
1

grid =

.
.
.

.
.
.

m-1

.....
mxn

L40 - Dynamic Programming Page 1

Recursive Case
Let f (i, j) be a function which computes the sum of numbers along the
minimum sum path to go from the (i, j)th cell to the (m-1, n-1)th cell then,
f (i, j) = grid[i][j] + min [ f (i, j+1) , f (i+1, j) ]

Base Case

What is the reason behind exponential time complexity ?

f0, 0

f0, 1
f0, 2
f0, 3

f0, n-2
f0, n-1

L40 - Dynamic Programming Page 2

f1, 0

f1, 1
f1, 2

f1, 1

f2, 0
f2, 1

f3, 0

fm-2, 0
fm-1, 0

Top-Down Dynamic Programming
f0, 0
f1, 0

f0, 1
f0, 2
f0, 3

f1, 1

f1, 1
f1, 2

f2, 0
f2, 1

f3, 0

f0, n-2

fm-2, 0

fm-1, 0

f0, n-1

j

i

mxn

where,

f(i, j) is a function which computes the sum of numbers along the
minimum sum path to go from the (i, j)th to the (m-1, n-1)th cell.

Bottom-Up Dynamic Programming
0

j

n-1

0

i

m-1
mxn

L40 - Dynamic Programming Page 3

where,

f(i, j) is a function which computes the sum of numbers along the
minimum sum path to go from the (i, j)th to the (m-1, n-1)th cell.

From recurrence,

f (i, j) =

{

grid[i][j] + f (i, j+1)
grid[i][j] + f (i+1, j)
grid[i][j] + min [ f (i, j+1), f (i+1, j) ]
grid[i][j]

; i .= m-1 and j != n-1
; i != m-1 and .j .= n-1
; i != m-1 and .j != n-1
;!i = m-1 and .j .= n-1

Therefore,

dp[i][j] =

{

grid[i][j] + dp[i][j+1]
grid[i][j] + dp[i+1][j]
grid[i][j] + min ( dp[i][j+1], dp[i+1][j] )
grid[i][j]

0

.....

j

j+1

.....

; i .= m-1 and j != n-1
; i != m-1 and .j .= n-1
; i != m-1 and .j != n-1
;!i = m-1 and .j .= n-1

n-1

0

i
i+1

m-1
mxn

[R][HW] Building the Min-Sum Path from dp[][]

0
1

2

0

1

2

1
1
4

3
5
2

1
1
1

grid[][]

L40 - Dynamic Programming Page 4

0
1
2

0

1

2

7
8
7

6
7
3

3
2
1

dp[][]

Space Optimized Bottom-Up Dynamic Programming
0

j

j+1

n-1

0

i
i+1

m-1
mxn

i
i+1

L40 - Dynamic Programming Page 5

[HW] Dungeon Game

Dungeon Game

0

1

n-1

.....

0
1

dungeon =

.
.
.

.
.
.

m-1

.....
mxn

Recursive Case
Let f (i, j) be a function which computes the minimum initial health the knight
L40 - Dynamic Programming Page 6

Let f (i, j) be a function which computes the minimum initial health the knight
needs starting from the (i, j)th cell to rescue the princess from the (m-1, n-1)th
cell then,

f (i, j) =

{

min(x, y)
; grid[i][j] == 0
min(x, y) - grid[i][j] ; grid[i][j] < 0
min(x, y) - grid[i][j] ; grid[i][j] > 0 && grid[i][j] < min(x, y)
1
; grid[i][j] > 0 && grid[i][j] >= min(x, y)

Base Case

What is the reason behind exponential time complexity ?
f0, 0
f0,1

f1, 0
f2, 0
f3, 0

f1, 1

f1, 1

f2, 1

fm-1, 0

f1, 2

f0, 3

f0, n-1
f0, n

fm, 0

Top-Down Dynamic Programming
f0, 0

L40 - Dynamic Programming Page 7

f0, 2

f0,1

f1, 0
f2, 0

f3, 0

f1, 1

f1, 1
f2, 1

f0, 2
f1, 2

f0, 3

fm-1, 0

f0, n-1

f0, n

fm, 0

j

i

(m+1) x (n+1)

where,
f(i, j) is a function which computes the minimum initial health the
knight requires starting from the (i, j)th cell to rescue the princess

Bottom-Up Dynamic Programming
0
0

L40 - Dynamic Programming Page 8

j

n

i

m
(m+1) x (n+1)

where,
f(i, j) is a function which computes the minimum initial health the
knight requires starting from the (i, j)th cell to rescue the princess

From recurrence,

f (i, j) =

{

min(x, y)
; grid[i][j] == 0
min(x, y) - grid[i][j] ; grid[i][j] < 0
min(x, y) - grid[i][j] ; grid[i][j] > 0 && grid[i][j] < min(x, y)
1
; grid[i][j] > 0 && grid[i][j] >= min(x, y)

0
0

.....

j-1

j

.....

n

i-1
i

m
(m+1) x (n+1)
L40 - Dynamic Programming Page 9

m
(m+1) x (n+1)

L40 - Dynamic Programming Page 10

Wine Problem

Wines Problem
Given N bottles of wine along with their prices { p0, p1, . . . , pN-1 }. Design a recursive
algorithm to compute the maximum profit one can make by selling all the bottles of
wine such that each year one can sell only a single bottle of wine which is chosen from
the extreme ends. Moreover, in the yth year the price of the ith bottle of wine increases
from pi to y*pi.
Example
Input : N = 5

prices

0

1

2

3

4

2

3

5

1

4

Output : 50

i
j

.

.....

.

Recursive Case
Let f (i, j, y) be a function which computes, the maximum profit one can make
by selling (j-i+1) bottles of wines[i…j] starting from the yth year then,
f (i, j, y) =

max { pi *y + f (i+1, j, y+1),
pj *y + f (i, j-1, y+1) }

Base Case

What is the reason behind exponential time complexity ?
f0, N-1,1
f1, N-1,2
f2, N-1,3
f3, N-1,4

fN-1, N-1,N

L40 - Dynamic Programming Page 11

f0, N-2,2

f1, N-2,3

f2, N-2,4

f1, N-2,3

f0, N-3,3
f1, N-3,4

f0, N-4,4

f0, 0,N

Top-Down Dynamic Programming
f0, N-1,1

f0, N-2,2

f1, N-1,2
f2, N-1,3
f3, N-1,4

f1, N-2,3

f1, N-2,3

f2, N-2,4

f0, N-3,3
f1, N-3,4

f0, N-4,4

fN-1, N-1,N

f0, 0,N

i
j

y

N x N x (N+1)

where,

f (i, j, y) is a fn. which finds the max. profit one can make by
selling (j-i+1) bottles of wines[i…j] starting from the yth year.

State or Parameter Optimization

j

i

.

NxN
L40 - Dynamic Programming Page 12

.

i

NxN

where,

f (i, j) is a fn. which finds the max. profit one can make by selling
(j - i +1) bottles of wines[i…j] starting from the yth year such that
y=n-j+i

Bottom Up Dynamic Programming
j

0

N-1

0

.

i

N-1
NxN

where,
f (i, j) is a fn. which finds the max. profit one can make by
selling (j - i +1) bottles of wines[i…j] starting from the yth year
such that y = n - j + i

From recurrence,

f (i, j) =
== j

{

max { pi *y + f (i+1, j), pj*y + f (i, j-1) }
pi *y

;i < j
;i

{

max { pi *y + dp[i+1][j], pj*y + dp[i][j-1] }
pi *y

;i < j
;i

Therefore,
dp[i][j] =
== j

0

j

j-1

N-1

0

i

.

i+1

N-1
NxN

L40 - Dynamic Programming Page 13

[R][HW] 0/1 Knapsack Problem

0/1 Knapsack Problem
Given a set of N items along with their prices { p0, p1, . . . , pN-1 } and weights
{ w0, w1, . . . , wN-1 } & a knapsack that has a maximum weight capacity of W.
Design an algorithm to find the maximum profit you can make by selecting a
subset of items & placing them in the knapsack such that the sum of weights
of the selected items does not exceed the knapsack’s capacity.
Example
Input : N = 5, W = 4

0

1

2

3

4

prices

8

4

1

5

3

weights

1

2

3

2

2

Output : 13

0
n-1

i-1

.....

Recursive Case
L40 - Dynamic Programming Page 14

i

i+1

.....

Recursive Case
Let f(i, w) be a function that finds the maximum profit you can make by selecting a
subset of items [ i . . . N-1 ] and placing them in the knapsack such that the current
knapsack capacity is w then,
f (i, w) =

{

max { pi + f (i+1, w-wi), f (i+1, w) } ; wi <= w
f (i+1, w)
; otherwise

Base Case

What is the reason behind exponential time complexity ?
f0, W
f1, W

f1, W-1
f2, W-2

f3, W-3

f2, W-1

f2, W-1

f3, W-2

f3, W-1

Top-Down Dynamic Programming
f0, W
f1, W-1

L40 - Dynamic Programming Page 15

f2, W

f1, W

f3, W

f2, W-2
f3, W-3

f2, W-1

f2, W-1

f3, W-2

f2, W
f3, W-1

f3, W

w

.

i

(N+1) x (W+1)

where,
f(i, w) is a function that finds the maximum profit you can make by selecting a subset of
items [ i . . . N-1 ] and placing them in the knapsack such that the current knapsack
capacity is w

Bottom-Up Dynamic Programming
0

w

W

0

i

.

N

(N+1) x (W+1)

where,
f(i, w) is a function that finds the maximum profit you can make by selecting a
L40 - Dynamic Programming Page 16

f(i, w) is a function that finds the maximum profit you can make by selecting a
subset of items [ i . . . N-1 ] and placing them in the knapsack such that the
current knapsack capacity is w

From recurrence,
f (i, w) =
w=0

{

max { pi + f (i+1, w-wi), f (i+1, w) }
f (i+1, w)
0

Therefore,
dp[i][w] =

w=0

; wi <= w
; wi > w
; i = n or

{

max { pi + dp[i+1][w-wi], dp[i+1, w] } ; wi <= w
dp[i+1][w]
; wi > w
0
; i = n or

1

0

w

W

0

i

i+1

N-1
N

(N+1) x (W+1)

Bottom-Up Dynamic Programming Space Optimized
0

1

0

L40 - Dynamic Programming Page 17

w

W

0

1

w

W

0

i
i+1

N-1
N
(N+1) x (W+1)

L40 - Dynamic Programming Page 18

[R][HW] Unbounded Knapsack Problem

https://www.youtube.com/watch?v=DK5Z9ttunEQ&t=4739s

Unbounded Knapsack Problem
Given a set of N objects along with their prices { p0, p1, . . . , pN-1 } and weights
{ w0, w1, . . . , wN-1 } and a knapsack that has a maximum weight capacity of W.
Design a recursive algorithm to compute the maximum profit one can make by
choosing a subset of objects and putting them in the knapsack such that the sum of
weights of the objects put in the knapsack doesn't exceed knapsack capacity and
you can choose an item multiple times.
Example
Input : N = 3, W = 10
0

1

2

prices

6

3

8

weights

3

1

4

0
n-1

i-1

.....

i

i+1

.....

Recursive Case
Let f (i, w) be a function which computes the maximum profit one can make
L40 - Dynamic Programming Page 19

Let f (i, w) be a function which computes the maximum profit one can make
by choosing a subset of objects to be put in the knapsack from the given set of
objects that starts at the ith index such that the knapsack capacity is w then,
f (i, w) =

Base Case

{

max { pi + f (i, w-wi), f (i+1, w) } ; wi <= w
f (i+1, w)
; otherwise

What is the reason behind exponential time complexity ?
f0, W
f1, W

f0, W-1
f0, W-2

f1, W-1

f1, W-1

f1, W-2

f0, W-3

f2,W
f2, W-1

Top-Down Dynamic Programming
f0, W
f0, W-1
f0, W-2
L40 - Dynamic Programming Page 20

f1, W
f1, W-1

f1, W-1

f2, W

f3, W

f1, W

f0, W-1
f0, W-2

f0, W-3

f1, W-1

f1, W-1
f1, W-2

f2, W

f2, W-1

f3, W

w

.

i

(N+1) x (W+1)

where,

f (i, w) is a function which computes the maximum profit one can make by
choosing a subset of objects to be put in the knapsack from the given set of
objects staring at the ith index such that the knapsack capacity is w.

Bottom-Up Dynamic Programming
0

w

W

0

i

.

N
(N+1) x (W+1)

where,
L40 - Dynamic Programming Page 21

(N+1) x (W+1)

where,
f (i, w) is a function which computes the maximum profit one can make
by choosing a subset of objects to be put in the knapsack from the given
set of objects staring at the ith index such that the knapsack capacity is w.

From recurrence,
f (i, w) =
0

{

max { pi + f (i, w-wi), f (i+1, w) }
f (i+1, w)
0

Therefore,
dp[i][w] =
0

; wi <= w
; wi > w
; i = n or w =

{

max { pi + dp[i][w-wi], dp[i+1, w] } ; wi <= w
dp[i+1][w]
; wi > w
0
; i = n or w =

1

0

W

w

0

i
i+1

N-1
N
(N+1) x (W+1)

Bottom-Up Dynamic Programming Space Optimized
0

1

L40 - Dynamic Programming Page 22

w

W

Bottom-Up Dynamic Programming Space Optimized
0

1

w

W

0

i
i+1

N-1
N
(N+1) x (W+1)

L40 - Dynamic Programming Page 23

[R][HW] Colorful Knapsack Problem
https://www.youtube.com/watch?v=DK5Z9ttunEQ&t=6370s

Colorful Knapsack Problem
You are given a sequence of N objects that are coloured using M colours
labelled from 1 to M, along with their weights, and a knapsack that has a
weight capacity of X . You are required to fill the knapsack with the given
set of objects in such a way that its unused capacity is minimised. Design
an algorithm to find the minimum unused capacity of the knapsack such
that the knapsack contains exactly one object of each colour and the sum of
the weights of objects put in the knapsack doesn't exceed its capacity.
note : return -1 if there is no way to fill the knapsack
Example
Input : N = 8, M = 3, X = 13

0

1

2

3

4

5

6

7

weights

2

3

4

2

4

5

2

3

colors

1

1

1

2

2

2

3

3

i-1

i

i+1

1
M

.....

.....

Recursive Case
Let f (i, x) be a function which computes the minimum unused capacity of
the knapsack when we choose a sequence of objects to be put in the
L40 - Dynamic Programming Page 24

the knapsack when we choose a sequence of objects to be put in the
knapsack, one object from each of the remaining colors, starting with the ith
color such that the current capacity of the knapsack is x then,

f (i, x) =

min { f (i+1, x-xij) } ; xij <= x

Base Case

What is the reason behind exponential time complexity ?
fi=1, x=13
fi=2, x=11
fi=3, x=9
fi=4, x=7

fi=2, x=10

fi=3, x=7

fi=4, x=6

fi=4, x=5

fi=2, x=9

weights

2

3

4

2

4

5

2

3

colors

1

1

1

2

2

2

3

3

fi=3, x=6
fi=4, x=4 fi=4, x=4

fi=4, x=3
fi=4, x=6

Top-Down Dynamic Programming

L40 - Dynamic Programming Page 25

fi=3, x=8

fi=3, x=6

fi=4, x=5

fi=4, x=4

fi=3, x=5
fi=4, x=3 fi=4, x=3

fi=4, x=2

LCS

Longest Common Subsequence (LCS)
Given two strings S1 and S2 of lengths M and N respectively. Design a recursive
algorithm to find the length of the longest common subsequence between them.
Example :
Input : S1 = "ATGC", M = 4
S2 = "AGCT", N = 4
Output : 3
Explanation : The LCS between S1 and S2 is "AGC"

S1

S2

0
1
M-1

.....

0
1
N-1

.....

Recursive Case
Let f (i, j) be a function which computes the length of the longest
common subsequence between S1[i … M-1] and S2[j … N-1] then,
f (i, j) =

{

max { f (i+1, j), f (i, j+1) } ; S1[i] .!= S2[j]
1 + f (i+1, j+1)
; S1[i] == S2[j]

Base Case

What is the reason behind exponential time complexity ?
f0, 0

f1, 0
f2, 0
f3, 0

f0, 1
f1, 1

f1, 1

f2, 1

fM, 0

Top-Down Dynamic Programming

L40 - Dynamic Programming Page 26

f0, 2
f1, 2

f0, 3

f0, N

f0, 0
f1, 0
f2, 0
f3, 0

f0, 1
f1, 1

f1, 1
f2, 1

f0, 2

f0, 3

f1, 2

fM, 0

f0, N

j

.

i

(M+1) X (N+1)

where,

f (i, j) is a function which computes the length of the longest
common subsequence between S1[i … M-1] and S2[j … N-1]

Bottom Up Dynamic Programming
0

j

N

0

.

i

M
(M+1) X (N+1)

where,

f (i, j) is a function which computes the length of the longest
common subsequence between S1[i … M-1] and S2[j … N-1]

From recurrence,
f (i, j) =

{

dp[i][j] =

{

max { f (i+1, j), f (i, j+1) }
1 + f (i+1, j+1)

; S1[i] .!= S2[j]
; S1[i] == S2[j]

max { dp[i+1][j], dp[i][j+1] }
1 + dp[i+1][j+1]

; S1[i] .!= S2[j]
; S1[i] == S2[j]

Therefore,

0

0

L40 - Dynamic Programming Page 27

j

j+1

N

j

0

j+1

N

0

.

i
i+1

M
(M+1) X (N+1)

[R][HW] Building the LCS from dp[][]

A
T
G
C

A
0
3
2
2
1
0

0
1
2
3
4

G
1
2
2
2
1
0

C
2
1
1
1
1
0

T
3
1
1
0
0
0

4
0
0
0
0
0

dp[][]

[R][HW] Space Optimized Bottom-Up Dynamic Programming

j

0

j+1

N

0

i
i+1

M
(M+1) X (N+1)

i
i+1

0
0

L40 - Dynamic Programming Page 28

j

j+1

N

0

j

j+1

N

0

i
i+1

M
(M+1) X (N+1)

L40 - Dynamic Programming Page 29

[R][HW] Edit Distance

Edit Distance
Given two strings S1 and S2 of lengths M and N respectively. Design a recursive
algorithm to find the minimum number of edits required to transform S1 into S2 such
that each edit operation performed on S1 can be a letter insertion or letter deletion
or a letter substitution.
Example :
Input : S1 = "food" ; S2 = "money"
Output : 4

0

S1

0

1

2

3

f

o

o

d

i

...

0
4

m

L40 - Dynamic Programming Page 30

2

3

o

n

e

0

M-1

...

1

S2

y

j

...

N-1

...

Recursive Case
Let f (i, j) be a function which computes the minimum no. of edits
required to transform S1[i … M-1] into S2[j … N-1] then,

f (i, j) = min

{

1 + f (i, j+1),
1 + f (i+1, j),
S1[i] .!= S2[j] + f(i+1, j+1)

Base Case

f(i=M, j) is a function which computes the minimum number of
edits required to transform S1[M … M-1] into S2[j … N-1]

0

M-1

L40 - Dynamic Programming Page 31

M

0

N-1

......

S1

S2

...

i

...

j

f(i, j=N) is a function which computes the minimum number of
edits required to transform S1[i … M-1] into S2[N … N-1]

0

S1

M-1

...

...

0

N-1

......

S2

j

i

What is the reason behind exponential time complexity ?

f0, 0
f1, 0

f0, 1
f1, 1

N

f2, 0

L40 - Dynamic Programming Page 32

f1, 1
f2, 1

f1, 2

f2, 1

f2, 2

f1, 1

f2, 0

f2, 1

f1, 2

f2, 1
f2, 2

f3, 1

f3, 0

f2, 1

f2, 2

f3, 1

f3, 2

f1, 2

f2, 1

Top-Down Dynamic Programming

f0, 0

f1, 0

f0, 1
f1, 1
f2, 1

f2, 0
f3, 0

f1, 1
f2, 1
f2, 2

f3, 1

j

0

f2, 2
f3, 2

f3, 1

N

0

i

.

M
(M+1) x (N+1)

L40 - Dynamic Programming Page 33

where,

f (i, j) is a function which computes the minimum number
of edits required to transform S1[i … M-1] into S2[j … N-1]

Bottom Up Dynamic Programming
0

j

N

0

.

i

M
(M+1) x (N+1)

where,

f (i, j) is a function which computes the minimum number
of edits required to transform S1[i … M-1] into S2[j … N-1]

From recurrence,

f (i, j) = min

{

1 + f (i, j+1),
1 + f (i+1, j),
S1[i] .!= S2[j] + f (i+1, j+1)

Therefore,

dp[i][j] = min

{

1 + dp[i][j+1],
1 + dp[i+1][j],
S1[i] .!= S2[j] + dp[i+1][j+1]

L40 - Dynamic Programming Page 34

dp[i][j] = min

{

1 + dp[i][j+1],
1 + dp[i+1][j],
S1[i] .!= S2[j] + dp[i+1][j+1]

0

j

j+1

N

0

.

i
i+1

M
(M+1) x (N+1)

Space Optimized Bottom-Up Dynamic Programming

0

j

j+1

N

0

i
i+1

M
(M+1) X (N+1)
L40 - Dynamic Programming Page 35

M
(M+1) X (N+1)

i
i+1

0

j

j+1

N

0

i
i+1

M
(M+1) X (N+1)

L40 - Dynamic Programming Page 36

[R][HW] Wildcard Matching

Wildcard Matching
Given an input string S and a pattern P that contains 0 or more wildcard characters
( '?' and '*' ), design an algorithm to determine if P completely matches S such that
the wildcard '?' can match any single character and '*' matches 0 or more characters.
Example
S

a

b

c

a

b

c

a

P

a

?

c

*

?

a

*

S

a

b

c

a

b

c

P

a

?

b

*

S

0
M-1

a

i

...

...

L40 - Dynamic Programming Page 37

P

0
N-1

j

...

...

Recursive Case
Let f (i, j) be a function which checks if P[j … N-1] matches S[i … M-1] then,

f (i, j) =

{

f (i+1, j+1)
f(i, j+1) or f(i+1, j)
false

; P[j] == S[i] or P[j] == '?'
; P[j] == '*'
; P[j] != S[i]

Base Case

What is the reason behind exponential time complexity ?

L40 - Dynamic Programming Page 38

Top-Down Dynamic Programming
j

0

N

0

.

i

M
(M+1) x (N+1)

where,
f (i, j) is a function which checks if P[j … N-1] matches S[i … M-1]

Bottom Up Dynamic Programming
0

j

N

0

i

.

M
(M+1) x (N+1)

where,
f (i, j) be a function which checks if P[j … N-1] matches S[i … M-1]

From recurrence,
L40 - Dynamic Programming Page 39

From recurrence,

f (i, j) =
Therefore,

dp[i][j] =

{
{

f (i+1, j+1)
f(i, j+1) or f(i+1, j)
false

; P[j] == S[i] or P[j] == '?'
; P[j] == '*'
; P[j] != S[i]

dp[i+1][j+1]
dp[i][j+1] or d[i+1][ j]
false

; P[j] == S[i] or P[j] == '?'
; P[j] == '*'
; P[j] != S[i]

j

0

j+1

N

0

i

.

i+1

M
(M+1) x (N+1)

L40 - Dynamic Programming Page 40

