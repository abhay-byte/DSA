# Lecture 25

**Source:** `L25 - Recursion.pdf`

---

Generate Permutations

Generate Permutations
Given a string, design a recursive algorithm to generate all of its permutations.

A permutation of a given string is a rearrangement of its characters.
Example
Input : "abc"
Output : "abc", "acb", "bac", "bca", "cab", "cba"

.

L25 - Recursion Page 1

L25 - Recursion Page 2

[R][HW] Generate Unique Permutations

Generate Unique Permutations
Given a string, design a recursive algorithm to generate all of its unique permutations.
A permutation of a given string is a rearrangement of its characters.
note : generate the permutations without using any extra space.

Example
Input : "aabc"
Output : "aabc", "aacb", "baac", "baca", "bcaa", "caab", "caba", "cbaa"

i
inp

.
L25 - Recursion Page 3

.

L25 - Recursion Page 4

[HW] Letter Combination of a Phone Number

Letter Combination of a Phone Number
Given a phone keypad, and a string representing a n-digit number write a program to
generate all the words possible upon pressing the n-digits on the phone keypad.
"23"
"ad"
"ae"
"af"
"bd"
"be"
"bf"
"cd"
"ce"
"cf"

L25 - Recursion Page 5

[HW] Construct Smallest Number From DI String

Construct Smallest Number From DI String
Given a 0-indexed string pattern of length n consisting of characters 'I' meaning increasing
and 'D' meaning decreasing. A 0-indexed string num of length n+1 is
created using the following conditions • num consists of the digits '1' to '9' where each digit is used at most once
• if pattern [i] == 'I', then num [i] < num [i+1]
• if pattern [i] == 'D', then num [i] > num [i+1]

Design an algorithm to return the lexicographically smallest possible string num.
Example
0

1

2

3

4

5

6

7

pattern

I

I

I

D

I

D

D

D

num

1

2

3

5

4

9

8

7

pattern

8

6

0

1

2

3

D

I

I

D

num

i
pattern

num

L25 - Recursion Page 6

4

Permutation Sum

Permutation Sum
Given an array of distinct integers candidates and a target integer target, design a
algorithm to find all the permutations of candidates that sum up to the target. You
may print the permutations in any order.
The same number may be chosen from candidates an unlimited number of times.
Example
Input
target = 7
candidates

0

1

2

3

2

3

5

7

Output
2

2

3

2

3

2

2

5

3

t

2

5

2

7

c = { c0, c1,c2, . . . , cn-1 }

c0

c1

t-c0

t-c1

L25 - Recursion Page 7

2

c2

. . . cn-1
t-c2

...

t-cn-1

[R][HW] Combination Sum

Combination Sum
Given an array of distinct integers candidates & a target integer target, design
an algorithm to find all the unique combinations of candidates that sum up to
the target. You may print the combinations in any order.
The same number may be chosen from candidates an unlimited number of
times. Two combinations are said to be unique if the frequency of at least one of
the chosen numbers is different.
Input
target = 7
candidates

0

1

2

3

2

3

5

7

Output
2

2

3

2

5

7

t
cn-1 }
c0

c1

t-c0

t-c1

c = { c0, c1,c2, . . . ,
. . . cn-1

c2

t-c2

t'
ci
t-ci

...

t-cn-1

c = { ci, ci+1, . . . , cn-1 }

ci+1

t-ci+1

L25 - Recursion Page 8

. . . cn-1

ci+2
t-c2

...

t-cn-1

ci
t-ci

ci+1

t-ci+1

[i, n-1] [i+1, n-1]

L25 - Recursion Page 9

. . . cn-1

ci+2
t-c2

[i+2, n-1]

...

t-cn-1

[n-1, n-1]

[HW] Combination Sum II

https://leetcode.com/problems/combination-sum-ii/description/

L25 - Recursion Page 10

[HW] Ladders Problem

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

k
2
1
0

L25 - Recursion Page 11

n

i+k
i+2
i+1
i

1
0

Recursive Case
Let f (i) be a fn. which computes the no. of ways a person
can go from the ith step to the nth step of the ladder then,
k

f (i) = ∑ f (i+j) ; i+j <= n
j=1

Base Case

L25 - Recursion Page 12

Rat in a Maze I

Rat in a Maze I
Given a M x N maze with some blocked cells ( marked with X ), and a rat that
wants to go from the (0, 0)th cell (source) to the (M-1, N-1)th cell (destination)
design a recursive algorithm to check if there exists a path to from the source to
destination cell such at any point of time the rat can move one step either in the
right direction or the down direction.
Example
Input :
0
0
0
0
0
0
0 X

0
X
0
0

0
0
X
0

Output : True

0

1

n-2

n-1

.....

0
1

.
.

.
.

m-2

.....

m-1

mxn

j

i

m-1

L25 - Recursion Page 13

.

n-1

m-1

mxn

L25 - Recursion Page 14

Rat in a Maze II

Rat in a Maze II
Given a M x N maze with some blocked cells ( marked with X ), and a rat that
wants to go from the (0, 0)th cell (source) to the (M-1, N-1)th cell (destination)
design a recursive algorithm to count the number of paths that exists to reach
destination cell from the source cell such at any point of time the rat can move
one step either in the right direction or the down direction.
Example
Input :
0
0
0
0
0
0
0 X

0
X
0
0

0
0
X
0

Output : 3

0

1

n-2

n-1

.....

0
1

.
.

.
.

m-2

.....

m-1

mxn

j

0

n-1

0

i

.

m-1

mxn

L25 - Recursion Page 15

L25 - Recursion Page 16

Rat in a Maze III

Rat in a Maze III
Given a M x N maze with some blocked cells ( marked with X ), and a rat that
wants to go from the (0, 0)th cell (source) to the (M-1, N-1)th cell (destination),
design a recursive algorithm to generate all the paths that exists to go from
source cell to the destination cell such that at a point of time the rat can move
one step either in the right direction or the down direction.
Example

Input :
0
0
0
0

0
0
0
X

0
X
0
0

0
0
X
0

1
1
1
0

0
0
1
0

0
0
1
1

0
0
0
1

1
1
0
0

0
1
1
0

0
0
1
1

0
0
0
1

1
0
0
0

1
1
1
0

j

i

j

.

0
0
0
1

n-1

i

mxn

mxn

0
L25 - Recursion Page 17

0
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

L25 - Recursion Page 18

0
0
0
X

0
X
0
0

0
0
X
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
0
0

0
0
0
0

Rat Chases Its Cheese

Rat Chases Its Cheese
Given a M x N maze with some blocked cells ( marked with X ), and a rat that
wants to go from the (0, 0)th cell (source) to the (M-1, N-1)th cell (destination),
design a algorithm to find the unique path that the rat has to take to go from
source cell to the destination cell such that at a point of time the rat can move
one step in the left, right, up, or the down direction.
Example
Input :
0
0
X
X
X

X
0
0
0
X

0
0
X
0
0

0
X
0
X
0

1
1
0
0
0

0
1
1
1
0

j

0

0
0
0
1
1

0
0
0
0
1

n-1

0

0

i

j

0

n-1

.

i

.

m-1

m-1

mxn

L25 - Recursion Page 19

mxn

[HW] Unique Paths III

https://leetcode.com/problems/unique-paths-iii/

L25 - Recursion Page 20

[HW] Word Search

Word Search
Given an m x n grid of characters board and a string word, return true if word exists
in the grid. The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighbouring. The same letter cell
may not be used more than once.
Example

word = ABCCED

word = SEE

L25 - Recursion Page 21

