# Lecture 9

**Source:** `L9 - Functions.pdf`

---

Functions in C++ - Part 1

What is a function ?
In C++, a function is a group of statements which upon invocation or calling
performs a task. In general, you can compare them with mathematical functions

f(x) = x2
g(x, y) = x2 + y2

➢ A function to print a greeting message

L9 - Functions Page 1

How to call / invoke a function ?

➢ A function to check if a given integer is even

L9 - Functions Page 2

➢ A function to multiply two integers

L9 - Functions Page 3

➢ A function to increment an integers

Reference Variables ( lvalue Reference )
A reference variable ( lvalue reference ) is an alias for an existing variable (lvalue).

➢ A function to swap two integers

L9 - Functions Page 4

• A reference variables must be initialized.
• A reference variables cannot be reseated.
• A reference variables cannot be assigned the NULL value.

• A reference can be also be const

L9 - Functions Page 5

Functions in C++ - Part 2

➢ A function to check if an integer is prime

➢ A function to print all the prime numbers in the range 2 to M

Function Call Stack
A stack is a pile of objects - a stack of CDs, books, plates etc.

Passing Arrays to Functions

L9 - Functions Page 6

In C++, arrays are by default passed by reference.

➢ Return by Value vs Return by Reference

L9 - Functions Page 7

[R][HW]
➢ An expression is a combination of variables, literals, operators and function
calls that produces a value. Every expression has a type and value category.

The assignment operation requires the left operand of the assignment to be a
modifiable Lvalue expression & the right operand to be an Rvalue expression.

L9 - Functions Page 8

➢ We say an expression is a Lvalue expression if it evaluates to an entity that has
an identity and persists beyond the end of the expression __ for e.g. a variable
➢ We say an expression is a Rvalue expression if it evaluates to literals* or values
returned by functions/operators that are discarded at the end of the expression.

• Lvalue expressions implicitly convert to rvalue expressions in contexts where an
rvalue is expected but an lvalue is provided.

Function Declaration vs Function Definition
In C++, you cannot call a function before you either declare it or define it.

Function Overloading
In C++, we cannot create multiple functions with the same signature (function
name + parameters list) however, we can overload functions.

L9 - Functions Page 9

Function overloading means being able to create multiple functions with the same
name as long as the parameter list differ either in terms of parameter types or the
no. of parameters.

In C++, functions cannot overloaded based on the return type.

Namespaces
A namespace is a mechanism used by C++ to disambiguate conflicting identifiers.
Formally, it is a region that allows you to declare names inside of it for the purpose of
disambiguation.

All the names within a namespace must be unique to avoid naming collisions.

L9 - Functions Page 10

[R][HW] Function Templates

Default Arguments in Functions
In C++, we can provide default arguments i.e. values to function parameters,
such parameters are known as default parameters. During a call to a function if we
don't pass the value for a default parameter then its default value is used.

• In C++, default parameters must provided from right to left.

• In C++, we cannot overload functions on default parameters.

L9 - Functions Page 11

