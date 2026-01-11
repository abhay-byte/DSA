# Lecture 22

**Source:** `L22 - Recursion.pdf`

---

Recursion - Intro

➢ Reduction

fX {

...
gY

...
}

➢ Recursion
It is a kind of Reduction.
Suppose you are given a problem X for which you want to design a
recursive algorithm then recursion says
□ If you can solve X directly then solve it directly. [Base Case]
□ Otherwise, reduce X into one or more smaller instances of
the same problem (sub-problem). [Recursive Case]

L22 - Recursion Page 1

fX {
...
fx1 . . . fxn

...
}

L22 - Recursion Page 2

L22 - Recursion Page 3

Factorial

Factorial of a Number
Given a non-negative number n, design a recursive algorithm to compute n!.

L22 - Recursion Page 4

L22 - Recursion Page 5

Fibonacci Numbers

Fibonacci Numbers
Given a non-negative number n, design a recursive algorithm to compute the
nth Fibonacci number.

n
f (n)

0

1

2

3

4

5

6

7

9

…

0

1

1

2

3

5

8

13 21 34

…

L22 - Recursion Page 6

8

L22 - Recursion Page 7

L22 - Recursion Page 8

Multiply Numbers

Multiply Numbers
Given two non-negative integers x and y, design a recursive algorithm to compute their
product.

L22 - Recursion Page 9

L22 - Recursion Page 10

Print Increasing

Print Increasing
Given a positive integer N, design a recursive algorithm to print numbers from 1 to N in
the increasing order.

L22 - Recursion Page 11

Print Decreasing

Print Decreasing
Given a positive integer N, design a recursive algorithm to print numbers from N to 1 in
the decreasing order.

L22 - Recursion Page 12

[HW] 3n + 1 Sequence

https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/Q

L22 - Recursion Page 13

Power

Power
Given two non-negative integers x and y, design a recursive algorithm to compute xy.

Example
Input : x = 2 y = 3
Output : 8

L22 - Recursion Page 14

L22 - Recursion Page 15

[HW] Count Good Numbers

https://leetcode.com/problems/count-good-numbers/

L22 - Recursion Page 16

[R][HW] Generate Binary

Generate Binary
Given a position integer N, design a recursive algorithm to generate its binary
Example
Input : N = 20
Output : 10100

L22 - Recursion Page 17

[R][HW] String to Integer

String to Integer
Given a string str, design a recursive algorithm to convert it to an integer.

Example
Input : str = "123"
Output : 123

L22 - Recursion Page 18

[HW] Spell Number

Spell Number
Given a positive integer N, design a recursive algorithm to spell it.
Example
Input : N = 123
Output : one two three

L22 - Recursion Page 19

[HW] Move X

Move X
Given a string "str", design a recursive algorithm to move all the 'x' characters to
the end of the given string such that relative position
of non-x characters doesn't change.
Example
Input : str = "xaxbxc"
Output : "abcxxx"
Input : str = "axbxcx"
Output : "abcxxx"

L22 - Recursion Page 20

Tower of Hanoi

Tower of Hanoi
Given a three towers and N disks of varying sizes that can slide onto any
of the towers. Initially, all the N disks are placed in the decreasing order of
their sizes on the 1st tower (source) i.e. the smallest disk at its top and the
largest disk at its bottom. Design a recursive algorithm for generating the
steps required to move the N disks from the source tower to the 3rd tower
(destination) using the 2nd tower (helper) such that at any point of time
○ you can move a one disk from top of one tower to the top of another.
○ you cannot place a larger disk on top of smaller disk
Example

Input : N = 3

move disk from A to C
move disk from A to B
move disk from C to B
move disk from A to C
move disk from B to A
move disk from B to C
move disk from A to C

L22 - Recursion Page 21

