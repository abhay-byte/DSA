# Lecture 41

**Source:** `L41 - Dynamic Programming.pdf`

---

Rod Cutting Problem

Rod Cutting Problem
Given a rod of length n and the prices of its pieces of different lengths from 1 to n.
Design a recursive algorithm to find the maximum profit you can make by cutting the
rod and a selling its pieces.
Example
Input : n = 8

length
prices

1
1

2
5

3
8

4
9

5
6
7
8
10 17 17 20

Output : 22
Explanation : 5(2) + 17(6) = 22

n
Pn-1 }
+P0 ; -1

n-1

+P1 ; -2

prices = { P0, P1, P2, . . . ,

. . . +Pn-1 ; -n

+P2 ; -3

n-2

n-3

.....

n-n

Recursive Case
Let f (n) be a function which computes the maximum profit one
can make by cutting a rod of length n and selling its pieces then
n

f (n) = max p[j-1] + f (n-j)
j=1

Base Case

What is the reason behind exponential time complexity ?

fn
-1

fn-1

L41 - Dynamic Programming Page 1

-2

-n

fn-2

....

f0

fn
-1

-n

-2

fn-1
-1

-n-1

fn-2

....

-1

-n-2

fn-3

....

fn-2

....

-1

-n-3

f0

fn-3 . . . . f0

f0

f0

-n-3

f0
f0

....

Top-Down Dynamic Programming
fn
-1

-1

-n-1

fn-2

....

-1

-n-2

fn-3

....

-n

-2

fn-1
f0

fn-2

....

-1

-n-3

f0

fn-3 . . . . f0

f0

-n-3

f0

f0

0

....

1

i

n-1

.....

n

.....

where,
f (i) is a function which computes the maximum profit one
can make by cutting a rod of length i and selling its pieces.

Bottom-Up Dynamic Programming
0

1

i
.....

dp

n-1
.....

where,
f (i) is a function which computes the maximum profit one
can make by cutting a rod of length i and selling its pieces.
From recurrence,
i

f (i) = max p[j-1] + f (i-j)
L41 - Dynamic Programming Page 2

; i>0

n

can make by cutting a rod of length i and selling its pieces.
From recurrence,
i

f (i) = max p[j-1] + f (i-j)

; i>0

j=1

Therefore,
i

dp [i] = max p[j-1] + dp[i-j]
j=1

L41 - Dynamic Programming Page 3

Partition Array for Maximum Sum

Partition Array for Maximum Sum
Given an integer array, partition the array into (contiguous) subarrays of length at
most K such that after the partitioning each subarray has their value changed to
the maximum value of the subarray. Design an algorithm to find the largest sum
of the given array after partitioning.
Input : K = 3
0

1

2

3

4

5

6

1

15

7

9

2

5

10

0

1

2

3

4

n-1

.....

0

i-1

.....

i

i+1

n-1

.....

Recursive Case
Let f (i) be a function which finds the largest sum of the given array that starts
at the ith index after partitioning then,
j < i+k and < n

f (i) = max { max (arr [i…j]) * (j-i+1) + f (j+1) }
j=i

Base Case

L41 - Dynamic Programming Page 4

What is the reason behind exponential time complexity ?

0

1

2

3

4

n-1

.....

Top-Down Dynamic Programming

0

i

n

.....

.....

where,
f (i) is a function which finds the largest sum of the given array that
starts at the ith index after partitioning

Bottom-Up Dynamic Programming
0

i
.....

dp

n
.....

From recurrence,
j < i+k and < n

f (i) = max { max (arr [i…j]) * (j-i+1) + f (j+1) }
j=i

Therefore,
j < i+k and < n

dp[i] = max { max (arr [i…j]) * (j-i+1) + dp[j+1] }
j=i

L41 - Dynamic Programming Page 5

[R][HW] Tenzing and Balls

Tenzing and Balls

0

1

2

3

4

n-1

.....

0

i-1

i

i+1

n-1

.....

.....

Recursive Case
Let f (i) be a function that find the maximum no. of balls Tenzing can remove from a[i...n-1] then,
<n

f (i) = max { f(i+1), max ( (j-i+1) + f (j+1) ) } such that a[i] is equal to a[j]
j = i+1

Base Case

What is the reason behind exponential time complexity ?

L41 - Dynamic Programming Page 6

0
n-1

1

2

3

4

.....

Top-Down Dynamic Programming

0
n

i

.....

.....

where,
f (i) be a function that find the maximum no. of balls Tenzing can remove
from a[i...n-1] then,

Bottom-Up Dynamic Programming
dp

0
n

i

.....

.....

From recurrence,
j<n

f (i) = max { f(i+1), max ( (j-i+1) + f (j+1) ) } such that a[i] is equal to a[j]
j = i+1

Therefore,
j<n

dp[i] = max { dp[i+1], max ( (j-i+1) + dp[j+1] ) } such that a[i] is equal to a[j]
j = i+1

Time Optimization Bottom-Up Dynamic Programming

L41 - Dynamic Programming Page 7

.

L41 - Dynamic Programming Page 8

[YT][HW] Best Time to Buy and Sell Stock IV

https://www.youtube.com/watch?v=bXg1-S3hWNY&t=2953s

Best Time to Buy and Sell Stock IV
You are given an integer array prices where prices [i] is the price of a given stock
on the ith day, and an integer K. Design an algorithm to find the maximum profit
you can achieve by completing at most K transactions.

Note : You may note engage in multiple transactions simultaneously i.e. you must
sell the stock before you buy again.
Input : K= 2
0

1

2

2

4

1

0

1

2

3

4

5

prices

3

2

6

5

0

3

0

1

prices

Input : K= 2

2

3

4

n-1

.....

L41 - Dynamic Programming Page 9

0

i-1

i

i+1

n-1

.....

.....

Recursive Case
Let f (i, k) be a function which computes the maximum profit one can make by
completing at most k transactions starting from the ith then,
n-1

f (i, k) = max { f (i+1, k), max {prices[j]-prices[i] + f (j+1, k-1)} }
j = i+1

Base Case

L41 - Dynamic Programming Page 10

What is the reason behind exponential time complexity ?

0

1

2

3

4

n-1

.....

Top-Down Dynamic Programming

L41 - Dynamic Programming Page 11

k

.

i

(N+1) x (K+1)

where,

f (i, k) is a function which computes the maximum profit one can
make by completing at most k transactions starting from the ith day

Bottom-Up Dynamic Programming
0

k

K

0

i

.

N

where,

(N+1) x (K+1)

f (i, k) is a function which computes the maximum profit one can
make by completing at most k transactions starting from the ith day

L41 - Dynamic Programming Page 12

From recurrence,
n-1

f (i, k) = max { f (i+1, k), max{ prices[j]-prices[i] + f (j+1, k-1)} }
j = i+1

Therefore,
n-1

dp[i][k] = max { dp[i+1][k], max{prices[j] - prices[i] + dp[j+1][k-1]} }
j = i+1

0

1

k

K

0
i
i+1

j+1

N
(N+1) x (K+1)

L41 - Dynamic Programming Page 13

[YT][HW] Count Palindromic Partitioning

https://www.youtube.com/watch?v=VPlphqIYz1A&t=110s

Count Palindromic Partitioning
Given a string of length N, design a recursive algorithm to count the number of its
palindromic partitioning.

Example
Input : N = 5
0

1

2

3

4

a

b

a

a

a

0
n-1

i

.....

L41 - Dynamic Programming Page 14

i+1 i+2 i+3

.....

i
n-1

i+1 i+2

.....

Recursive Case
Let f(i) be a function which counts the number of palindromic partitioning of
str[i . . . n-1] then,
n-1

f (i) = ∑ f (j+1) such that str[i . . . j] is a palindrome
j=i

Base Case

L41 - Dynamic Programming Page 15

What is the reason behind exponential time complexity ?
f0
f2

f1
f2

f3

fn

...

fn

...

...

fn

...

f3

...

fn

fn

...

fn

Top-Down Dynamic Programming
f0

f2

f1

f2

...

fn

fn

...

f3
...

f3

...

fn

L41 - Dynamic Programming Page 16

...

fn

fn

...

fn

0
n

i

.....

.....

where,
f(i) is a function which counts the number of palindromic partitioning of
str[i . . . n-1].

Bottom-Up Dynamic Programming
dp

0
n

i
.....

.....

where,
f(i) is a function which counts the number of palindromic
partitioning of str[i . . . n-1]

From recurrence,
n-1

f (i) = ∑ f (j+1)
j=i

such that str[i . . . j] is a palindrome

Therefore,
n-1

dp[i] = ∑ dp[j+1] such that str[i . . . j] is a palindrome
j=i

L41 - Dynamic Programming Page 17

i
j

i+1

j-1

.....

0
n-1

1

2

3

4

.....

0

0
L41 - Dynamic Programming Page 18

j-1

j

N-1

0

j

j-1

N-1

0

.

i

i+1

N-1

NxN

L41 - Dynamic Programming Page 19

[YT][HW] Split Array Largest Sum
Try to also solve this problem using binary search
[DP solution] https://www.youtube.com/watch?v=S6Kp7juvkFA&t=133s

Split Array Largest Sum
Given an integer array nums, and an integer K, split the array into K non-empty
subarrays such that the largest sum of the any subarray is minimized. Design an
algorithm to find the minimized largest sum of the split.
Input : K = 2
0

1

2

3

4

7

2

5

10

8

0
n-1

1

2

3

4

.....

L41 - Dynamic Programming Page 20

0
n-1

i-1

i

.....

.....

i
n-1

.....

L41 - Dynamic Programming Page 21

i+1

Recursive Case
Let f (i, k) be a function which finds the minimized largest sum upon
partitioning / splitting arr[i . . . n-1] into k non-empty subarrays then,
<n

f (i, k) = min { max [ Sarr[i. . .j], f (j+1, k-1) ] }
j=i

Base Case

What is the reason behind exponential time complexity ?
L41 - Dynamic Programming Page 22

What is the reason behind exponential time complexity ?

0
n-1

1

2

3

4

.....

Top-Down Dynamic Programming
k

i

.

(N+1) x (K+1)

where,

f(i,k) is a function which finds the minimized largest sum upon
partitioning / splitting arr[i . . . n-1] into k non-empty subarrays

L41 - Dynamic Programming Page 23

Bottom-Up Dynamic Programming
0

k

K

0

dp

.

i

N
(N+1) x (K+1)

where,

f(i,k) is a function which finds the minimized largest sum upon
partitioning / splitting arr[i . . . n-1] into k non-empty subarrays

From recurrence,
<= n-k

f (i, k) = min { max [ Sarr[i. . .j], f (j+1, k-1) ] }
j=i

Therefore,
<= n-k

dp[i][k] = min { max ( Sarr[i. . .j], dp[j+1][k-1] ) }
j=i

L41 - Dynamic Programming Page 24

[HW] Matrix Chain Multiplication
[HW] Burst Balloons on Leetcode

Matrix Chain Multiplication ( MCM )
Given a sequence of N matrices {A1 , A2 , . . . , AN}, design an algorithm to find the
minimum no. of operations (i.e. scalar multiplications) required to multiply them,
assume the dimensions of the matrices are compatible for multiplication.
Example

Input : N = 3
0

1

2

3

2

1

2

4

Output : 16

a11 a12
a21 a22
a31 a32

b11 b12 b13
b21 b22 b23

c11 c12 c13
c21 c22 c23
c31 c32 c33

2x3
3x2

3x3

Input : N = 3
0

1

2

3

2

1

2

4

Input : N = 4

L41 - Dynamic Programming Page 25

0

1

2

3

4

1

2

1

4

1

.

i
j

Ai

i
j

Ai

Aj

k

Ak

Aj

Recursive Case

.

Let f (i, j) be a function which computes the minimum no. of operations
required to multiply a chain of matrices { Ai , Ai+1 , . . . , Aj } then,
f (i, j) =

j-1

min { f (i, k) + f (k+1, j) + d [i-1] * d [k] * d[j] }
k=i

Base Case
L41 - Dynamic Programming Page 26

Base Case

What is the reason behind exponential time complexity ?

Top-Down Dynamic Programming
j

i

.

NxN

where,
f (i, j) is a function which computes the minimum no. of operations
required to multiply a chain of matrices {Ai , Ai+1 , . . . , Aj}

Bottom Up Dynamic Programming
j

1

N

1

i

.

N

where,
f (i, j) is a function which computes the minimum no. of operations
required to multiply a chain of matrices {Ai , Ai+1 , . . . , Aj}

L41 - Dynamic Programming Page 27

NxN

From recurrence,

f (i, j) =

{

j-1

min { f (i, k) + f (k+1, j) + d [i-1] * d [k] * d[j] } ; i < j

k=i

0

; i == j

Therefore,

dp[i][j] =

{

j-1

min { dp[i][k] + dp[k+1][j] + d [i-1]*d [k]*d[j] } ; i < j

k=i

0

; i == j

1

j

j-1

N

1

i

.

i+1

N
NxN

L41 - Dynamic Programming Page 28

[YT][HW] LIS-K Problem
https://www.youtube.com/watch?v=gI322KuDul8&t=75s

Longest Increasing Subsequence (LIS-K) Problem
Given an array of N integers and a non-negative integer K (< N), design a recursive
algorithm to compute the length of the longest increasing subsequence that starts at
the Kth index of the given integer array.

Example
Input : N = 7, K = 1
0

1

2

3

4

5

6

1
2
5
3
0
4
6
Output : 4
Explanation : The LIS starting at 1st index is {2, 3, 4, 6}

0
n-1

i

.....

L41 - Dynamic Programming Page 29

i+1 i+2 i+3

.....

0
n-1

i

i+1 i+2 i+3

.....

.....

Recursive Case
Let f(i) be a function which computes the length of the longest increasing
subsequence that starts at the ith index of the given array of integers then,
n-1

f (i) = 1 + max f (j)
j = i+1

; A[j] >= A[i]

Base Case

What is the reason behind exponential time complexity ?
L41 - Dynamic Programming Page 30

fk

fk+2 . . . fn-1

fk+1
fk+2

fk+3 . . . fn-1

fn-1

...

...

fk+3

...

fn-1

fn-1

...

fn-1

Top-Down Dynamic Programming
fk
fk+1
fk+2

...

fk+2 . . . fn-1
fk+3 . . . fn-1

fn-1

...

fk+3

...

...

fn-1

fn-1

fn-1

0
n-1

i
.....

L41 - Dynamic Programming Page 31

.....

where,
f(i) is a function which computes the length of the longest increasing
subsequence that starts at the ith index of the given array of integers.

Bottom-Up Dynamic Programming
dp

0
n-1

i
.....

.....

where,

f(i) is a function which computes the length of the longest
increasing subsequence that starts at the ith index of the given
array of integers.
From recurrence,
n-1

f (i) = 1 + max f (j) ; A[j] >= A[i], i < n-1
j=i+1

Therefore,
n-1

dp [i] = 1 + max dp[j]
j=i+1

L41 - Dynamic Programming Page 32

[YT][HW] LIS Problem
Try to solve in O(nlogn)
[DP solution] https://www.youtube.com/watch?v=gI322KuDul8&t=75s

Longest Increasing Subsequence Problem
Given an array of N integers design a recursive algorithm to compute the length of
the longest increasing subsequence in the given integer array.
Example
Input : N = 7
0

1

2

3

4

5

6

1
2
5
3
0
4
6
Output : 5
Explanation : The LIS starting at 1st index is {1, 2, 4, 4, 6}

L41 - Dynamic Programming Page 33

