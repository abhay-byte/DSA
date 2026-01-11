# Lecture 4

**Source:** `L4 - Intro to C^M^M.pdf`

---

Introduction to C++

Introduction to C++
➢ The extension of C++ file is .cpp

010101
010101
010101

compiler

.cpp

machine code

source code

preprocessor

.cpp

.i

compiler

010101
010101
010101
machine code

source code

What is a function ?
In C++, a function is a group of statements which upon invocation or calling
performs a task. In general, you can compare them with mathematical functions

f(x) = x2

g(x, y) = x2 + y2

L4 - Intro to C^M^M Page 1

Comments in C++
A comment is a line of text which is used to document a program and is ignored
by the compiler.

Reading Input in C++

L4 - Intro to C^M^M Page 2

Naming Rules for Variables
➢ It must only contain uppercase or lowercase alphabets, digits and underscore.
➢ It must not start with a digit.

➢ It should not a keyword. e.g. return, main, int, true, false etc.
➢ In C++, variable names are case-sensitive.

Common Issues using Variables

L4 - Intro to C^M^M Page 3

In C++,
○ You cannot use a variable before you declare it.

○ You can create multiple variables with the same names.
○ You cannot re-declare a variable.

○ By default a variable contains a garbage value.

L4 - Intro to C^M^M Page 4

Arithmetic Operators in C++

Arithmetic Operators in C++
C++ supports five basic arithmetic operations, these include
• Addition ( + ) : to add two numbers

• Subtraction ( - ) : to subtract two numbers or to denote a negative number
• Multiplication ( * ) : to multiply two numbers
• Division ( / ) : to divide two numbers
• Modulus ( % ) : returns remainder of dividing the 1st operand by the 2nd

Operator Precedence and Associativity
The precedence of an operator dictates the order of operations in an expression.
Example

L4 - Intro to C^M^M Page 5

The precedence of an operator dictates the order of operations in an expression.
Example
3 + 5 * 4 = 23
8 __ 4 / 2 = 6
In C++, we can use parentheses ( ) to enforce precedence.
(3 + 5) * 4 = 32
(8 __ 4) / 2 = 2

The associativity of an operator is used to determine the order of operations when
operators in an expression have the same precedence.
100 / 10 * 10 = 100
5 __ 2 + 3 = 6

Simple Interest
Given the values of principal, rate and time, write a program to find simple interest.

L4 - Intro to C^M^M Page 6

Relational Operators in C++

Relational or Boolean Operators in C++
C++ offers six different Relational or Boolean operators
Boolean Comparator
>
<
>=
<=
==
!=

Example
a>b
a<b
a >= b
a <= b
a == b
a != b

Meaning
a greater than b
a less than b
a greater than or equal to b
a less than or equal to b
a equal to b
a not equal to b

A Relational or Boolean operator always evaluates to True or False .

L4 - Intro to C^M^M Page 7

Logical Operators in C++

Logical Operators in C++
C++ offers three different logical operators
P
True
True
False
False

Q
True
False
True
False

P and Q
True
False
False
False

P or Q
True
True
True
False

P
True
False

not P
False
True

• precedence(not) > precedence(and) > precedence(or)
• All the logical operators are left to right associative.

Short-Circuiting of Logical and & or Operators
Consider two Boolean expressions "P" & "Q"
• During evaluation of expression P and Q, if "P" evaluates to False, since the
overall expression evaluates to False, expression "Q" will not be evaluated.
• During evaluation of expression P or Q, if "P" evaluates to True, since the overall
expression evaluates to True, expression "Q" will not be evaluated.

Truthy vs Falsy Values
L4 - Intro to C^M^M Page 8

In C++, individual values can evaluate to True or False. The values which evaluate
to True are considered Truthy & values that evaluate to False are considered Falsy.
Truthy values include non-zero numbers, and the constant true. In contrast, Falsy
values include the numeric zero-value and the constants false & NULL.

L4 - Intro to C^M^M Page 9

Conditionals in C++

Conditional Logic in C++
➢ if Statement

➢ else Statement

L4 - Intro to C^M^M Page 10

➢ else if Statement

L4 - Intro to C^M^M Page 11

Largest of three numbers
Given three numbers, design an algorithm to find the largest number.
Example
Input : 2, 6, 4
Output : 6

L4 - Intro to C^M^M Page 12

Loops in C++

Loops in C++
A loop is programming construct that allows you to do the same task repeatedly
while a condition is true. In general, a loop has four components
○ Initialization
○ Condition Checking
○ Body of the loop
○ Update Rule

➢ The while Loop

L4 - Intro to C^M^M Page 13

Homework

L4 - Intro to C^M^M Page 14

