# Lecture 39

**Source:** `L39 - Dynamic Programming.pdf`

---

Intro to DP

Dynamic Programming (D.P.)
It is a problem-solving technique that is used to perform Recursion
without Repetition by storing the results of unique sub-problems
in a table and referring to it as and when required.

Fibonacci Numbers
Given a non-negative number n, design a recursive algorithm to compute the
nth Fibonacci number.
n 0
f (n) 0

1
1

2
1

3
2

4
3

5
5

6 7 8 9 …
8 13 21 34 …

Recursive Case
Let f(n) be a function which computes the nth Fibonacci number then
f (n) = f (n-1) + f (n-2)

Base Case
f (0) = 0
f (1) = 1

fn
fn-2

fn-1
fn-3

fn-2
fn-3

fn-4

f2

f1

f0

Assuming all the levels are filled, total no. of sub-problems is equal to
20 + 21 + 22 + 23 + … + 2n-1
This is a finite GP where,
a=1
r=2
#=n
The sum of finite GP given as follows
= a * [ (r#-1) / ( r-1) ]
L39 - Dynamic Programming Page 1

#=n
The sum of finite GP given as follows
= a * [ (r#-1) / ( r-1) ]

Substituting the values of a, r, and #, we get
= 1 * [ (2n-1) / ( 2-1) ]
= 2n-1
~ 2n
How much time do we spend on each sub-problem ?
Therefore, the time complexity is equal to O (2n)
What is the reason behind exponential time complexity ?

fn
fn-2

fn-1
fn-3

fn-2
fn-4

fn-3

f2
f0

f1

Top-Down Dynamic Programming
fn

fn-2

fn-1
fn-3

fn-2
fn-3

fn-4

f2
f0

f1

0

1

i

n-1

.....

.....

where,
f(i) is a function which computes the ith Fibonacci number

f5

0
dp

f3

f4
f2

f3
f2

f1

L39 - Dynamic Programming Page 2

1

2

3

4

5

n

f1

f2
f0

f1

Bottom-Up Dynamic Programming
0

1

i

n-1

.....

dp

n

.....

where,
f(i) is a function which computes the ith Fibonacci number
From recurrence,

f (i) = f (i-1) + f (i-2) ; i >= 2

Therefore,
dp[i] = dp[i-1] + dp[i-2]

Space Optimized Bottom-Up Dynamic Programming

0

dp

1

i-2 i-1

.....

L39 - Dynamic Programming Page 3

n-1

i

.....

n

Min. Steps to One

Minimum Steps to One
Given a positive number n, design a recursive algorithm to compute the minimum no.
of steps required to reduce the given no. to one such that at each step you can
□ reduce n to n-1
□ reduce n to n/2 if n is divisible by 2 or
□ reduce n to n/3 if n is divisible by 3 or

Example
Input : n = 10
Output : 3
Explanation : 10 -----> 9 -----> 3 -----> 1

n

-1

/3

/2

n-1

n/
3

n/
2

Recursive Case
Let f (n) be a function which computes the minimum number of steps required to
reduce n to one then
f (n) = 1 + min ( f (n-1) ,
f ( n /2 ) ,
f (n/3) )

Base Case

fn
fn-1

fn/2

fn/3

fn-2
fn-3

f1

Assuming all the levels are filled, total no. of sub-problems is equal to
30 + 31 + 32 + 33 + … + 3n-1
This is a finite GP where,
L39 - Dynamic Programming Page 4

This is a finite GP where,

a=1
r=3
#=n

The sum of finite GP given as follows
= a * [ (r#-1) / ( r-1) ]

Substituting the values of a, r, and #, we get
= 1 * [ (3n-1) / ( 3-1) ]
= (3n-1) / 2
~ 3n
How much time do we spend on each sub-problem ?
Therefore, the time complexity is equal to O (3n)
What is the reason behind exponential time complexity ?

f5
-1

f4
/2

-1

f3
-1

f2
-1

/2

f1

f1

f2
/3

-1

/2

f1

f1

f1

Top-Down Dynamic Programming
fn
fn/2

fn-1

fn/3

fn-2
fn-3
f1

0

1

.....

i

n-1

.....

n

where,
f(i) is a function which computes the minimum number of steps
required to reduce the i to one.

f5

0
dp

-1

f4
-1

f3

/2

f2

L39 - Dynamic Programming Page 5

1

2

3

4

5

dp

f4
/2

-1

f3
-1

f2
-1

/2

f1

f1

f2
/3

-1

/2

f1

f1

f1

Bottom-Up Dynamic Programming
0

1

dp

.....

i

.....

n-1

where,
f(i) is a function which computes the minimum number of steps
required to reduce i to one.
From recurrence,
f (i) = 1 + min ( f (i-1), f (i/2), f (i/3) )
Therefore,
dp[i] = 1 + min ( dp[i-1], dp[i/2], dp[i/3] )

L39 - Dynamic Programming Page 6

n

[HW] Coin Change Problem

Coin Change Problem
You are given an integer array coins representing coins of K different
denominations and an integer N representing total amount of money.
Design a recursive algorithm to compute the fewest number of coins
required to make up that amount i.e. reduce the given amount N to 0.
You may assume that you have an infinite supply of each kind of coin.
Example
Input : coins = [1, 2, 5], n = 11
Output : 3
Explanation : 11 = 5 + 5 + 1

N
ck-1 }

coins = { c0, c1,c2, . . . ,

c0

c1

N-c0

N-c1

c2

. . . ck-1
N-c2

...

N-ck-1

Recursive Case
Let f (n) be a function which computes the minimum no.
of coins required to reduce the given amount N to 0 then
k-1

f (n) = 1 + min ( f (n-cj) )
j=0

Base Case
L39 - Dynamic Programming Page 7

; n-cj >= 0

Base Case

What is the reason behind exponential time complexity ?

N=4
coins = { 1, 2 }

f4
-2

-1

f3

f2

-1

f2

-2

-1

-2

f1

f1

f0

-1

-2

-1

-1

f1

f0

f0

f0

-1

f0

Top-Down Dynamic Programming
f4

N=4
coins = { 1, 2 }

-2

-1

f3
-1

f2

f2
-2

-1

-2

f1

f1

f0

-1

-2

-1

-1

f1

f0

f0

f0

-1

f0

0
n

1

i
.....

L39 - Dynamic Programming Page 8

n-1
.....

where,
f (i) is a function which computes the minimum number
of coins required to reduce the amount i to 0.

f4

N=4
coins = { 1, 2 }

0
-2

-1

f2

2

dp

f3
-1

1

f2
-2

-1

-2

f1

f1

f0

-1

-2

-1

-1

f1

f0

f0

f0

-1

f0

Bottom-Up Dynamic Programming

dp

0
n

1

i

n-1

.....

.....

where,
f(i) is a function which computes the minimum number of coins
required to reduce amount i to 0.
From recurrence,
k-1

f (i) = 1 + min ( f (n-cj) )
j=0

; i-cj >= 0

Therefore,
k-1

dp [i] = 1 + min ( dp[i-cj] )
j=0

L39 - Dynamic Programming Page 9

3

4

Ladders Problem

Ladder's Problem
Consider a ladder with n steps, a person is standing at the bottom of the ladder
and wants to reach to its top. Design a recursive algorithm to count the number of
ways the person the reach the nth step i.e. ladder's top from its bottom such that
at each step the person can take a jump of size ranging b/w one to k steps.
Example
Input : n = 4, k = 3
Output : 7
Explanation : [1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[1, 3]
[3, 1]

4
3
2
1
0

n
n-1

n-2
n-3
n-k
2

1
0

Recursive Case
Let f(n) be a function which computes the no. of ways a person can
reach the nth step i.e. the top of the ladder from its bottom then,
k

f (n) = ∑ f (n-j) ; n-j >= 0
j=1

Base Case

What is the reason behind exponential time complexity ?

fn
-1

-2

-1

-k

fn-2

....

-1

-k

fn-3

....

-k

fn-2

fn-1

. . . . fn-k

-1

-k

fn-3 . . . . fn-2-k

fn-1-k

fn-2-k

-k

fn-3-k
f0

....

Top-Down Dynamic Programming
fn
-1

-2

fn-1
-1

L39 - Dynamic Programming Page 10

-k

-k

fn-2
-1

. . . . fn-k
-k

fn
-1

-2

-1

-k

fn-2

....

-1

-k

fn-3

....

-k

fn-2

fn-1

. . . . fn-k

-1

-k

fn-3 . . . . fn-2-k

fn-1-k

fn-2-k

-k

fn-3-k

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
f (i) is a function which computes the total number of ways
a person can reach the ith step of the ladder from its bottom.

Bottom-Up Dynamic Programming
0

1

i

n-1

.....

dp

n

.....

where,

f (i) is a function which computes the total number of ways
a person can reach ith step of the ladder from its bottom
From recurrence,
k

f (i) = ∑ f (i-j)

; i-j >= 0, i > 0

j=1

Therefore,
k

dp [i] = ∑ dp[i-j]
j=1

Time Optimized Bottom-Up Dynamic Programming

0

dp

i-k-1 i-k

...

L39 - Dynamic Programming Page 11

i-2

...

i-1

n-1

i

.....

n

[R][HW] House Robber I

House Robber I

Example
Input : N = 5
0

1

2

3

4

100 50 400 200 100

0

i-1

.....

Recursive Case
L39 - Dynamic Programming Page 12

i

n-1

i+1 i+2

.....

Let f (i) be a function which computes the maximum amount of money that
can be robbed in a night from a given sequence of houses starting at the ith
index without alerting the police then,
f (i) = max { nums[i] + f (i+2) ,
f (i+1) }

Base Case

What is the reason behind exponential time complexity ?
f0
f1

f2
f4
f6

f3

f3
f5

f2
f4

f3

fn

Top-Down Dynamic Programming

0

n n+1

i
.....

L39 - Dynamic Programming Page 13

.....

where,
f (i) is a function which computes the maximum amount of money which
can be robbed in a night from a given sequence of houses starting at the ith
index without alerting the police.

Bottom-Up Dynamic Programming
0

i
.....

dp

n n+1
.....

From recurrence,
f (i) = max { nums[i] + f (i+2) ,
f (i+1) }
Therefore,
dp[i] = max { nums[i] + dp [i+2] ,
dp [i+1] }

L39 - Dynamic Programming Page 14

[HW] House Robber II

House Robber II

Example
Input : N = 8
0

1

2

3

4

5

6

7

7

4

1

9

3

8

6

5

0

1

2

3

4

5

6

7

7

4

1

9

3

8

6

5

L39 - Dynamic Programming Page 15

[R][HW] House Robber III

House Robber III
Given the root of a binary tree, in which each node corresponds to a house
and the value of the node represents the amount of money in each house.
Design an algorithm, to find the maximum amount of money a thief can rob
without alerting the police such that he is initially standing at the root node &
police will be informed if two directly-linked houses are robbed together.

root

L39 - Dynamic Programming Page 16

root

7

7

6

5

1

3

8

2
9

L39 - Dynamic Programming Page 17

6
4

5

1

3
8

2
9

4

