# Lecture 5

**Source:** `L5 - Intro to C^M^M.pdf`

---

Sum of Digits

Sum of Digits
Given a positive integer N, design an algorithm to find the sum of its digits.
Example
Input : N = 123
Output : 6
Input : N = 456
Output : 15

L5 - Intro to C^M^M Page 1

Reverse a number

Reverse a Number
Given a positive number N, design an algorithm to reverse the number.
Example
Input : N = 123
Output : 321
Input : N = 456
Output : 654

L5 - Intro to C^M^M Page 2

Variable Scope

Variable Scope
In C++, scope of a variable can be thought of as the visibility of the variable.
In general, a variable can either have a block scope or a global scope.
• Block Scope
Any variable declared within a block ( { } ) has a block scope i.e. it visible /
accessible from the point of its declaration till the end of the block. We call
variables with block scope as local variables.
• Global Scope

Any variable declared not within a block ( { } ) has a global scope and we call
such variables as global variables.

Variable Scope Resolution
L5 - Intro to C^M^M Page 3

L5 - Intro to C^M^M Page 4

Scope Resolution Operator [ : : ]
One of the use cases of the scope resolution operator [ :: ] is to be
able to access a global variable when there is a local variable with
the same name.

L5 - Intro to C^M^M Page 5

Static Variables

L5 - Intro to C^M^M Page 6

Fibonacci Numbers

Fibonacci Numbers
Given a non-negative integer n, design a algorithm to find the nth Fibonacci number.

0
n
f (n) 0

1

2

3

4

5

6

1

1

2

3

5

8

L5 - Intro to C^M^M Page 7

...
13 21 34 . . .
7

8

9

L5 - Intro to C^M^M Page 8

Largest of N numbers

Largest of N numbers
Given N integer values, design an algorithm to find the largest of the N numbers.
Example
Input : N = 5
2
4
0

8

6

Output : 8

L5 - Intro to C^M^M Page 9

Controlling Loops in C++

• Break Statement
The break statement is used to pre-maturely terminate a loop.

• Continue Statement
The continue statement is used to skip an iteration of the loop.

L5 - Intro to C^M^M Page 10

Ternary Operator in C++

Ternary Operator in C++
The ternary or conditional operator evaluates a condition &
executes a block of code based of the result of the condition.

L5 - Intro to C^M^M Page 11

In C++, the ternary or conditional operator can be nested i.e. we can use a
ternary operator within a ternary operator.

L5 - Intro to C^M^M Page 12

[HW] Check Fibonacci Number

Check Fibonacci Number
Given a non-negative integer N, check if it is a Fibonacci number.
0
n
f (n) 0

1

2

3

4

5

6

1

1

2

3

5

8

Example :
Input : N = 10
Output : false
Input : N = 8
Output : true

L5 - Intro to C^M^M Page 13

...
13 21 34 . . .
7

8

9

Check Prime

Check Prime
Given a positive number N (>1), design an algorithm to check if the given
number is a prime number.
Example

Input : N = 5
Output : true
Input : N = 4
Output : false
A number n is a prime no. if it is divisible by only 1 & the number itself.

L5 - Intro to C^M^M Page 14

Square Root of a Number

Find Square Root
Given a non-negative integer N, design an algorithm to find its square root.
Example
Input : N = 64
Output : 8
Input : N = 30
Output : 5.47

L5 - Intro to C^M^M Page 15

L5 - Intro to C^M^M Page 16

