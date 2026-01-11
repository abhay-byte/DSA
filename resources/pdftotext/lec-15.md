# Lecture 15

**Source:** `L15 - Pointers.pdf`

---

Intro to Pointers

Introduction to Pointers in C++
• We can visualize the system memory ( RAM ) as a sequence of memory cells
such that each memory cell is of 1B ( 8 bits ) and is addressable.

0 1
n-1

n-2
.....

• These addresses depending on the system ( and the compiler ) are either of 32bits i.e. 4B or 64-bits i.e. 8B. Moreover, computer use the hexa-decimal i.e. the
base-16 number system to represent addresses.

• When we run a C++ program, a portion of system memory is allocated for
program execution which is known as application memory.

0 1
n-1

n-2
...

...

• To know the address of a byte in C++, we use the address of ( & ) operator.

• When we print address of a character using the cout <<, C++ prints the
contents of the memory stored at that address until it encounters the null
character ( '\0' ).

Pointers in C++
A pointer is a variable which is used to store address of another variable.

Since a pointer stores an address which are of 8B, in C++, we can use a pointer of
one type to store the address of a variable of another type via explicit type-casting.

L15 - Pointers Page 1

Dereferencing a Pointer in C++
To dereference a pointer, i.e. to access the value of the variable whose address
is stored by the pointer variable, we use the dereference operator ( * ).

31
0

9

....

1

8

0

7

0

6

0

5

0

4

0

3

0

2

1

1

0

0

Pointer Arithmetic
A pointer variable only supports arithmetic addition and subtraction operations.
Moreover, in C++, we can also subtract two pointer variables.

L15 - Pointers Page 2

A pointer variable only supports arithmetic addition and subtraction operations.
Moreover, in C++, we can also subtract two pointer variables.

const Pointer vs Pointer to const vs const Pointer to const

L15 - Pointers Page 3

Pointers and Functions

L15 - Pointers Page 4

Void or Generic Pointers
A generic or void pointer (void*) can be used to address of a variable of any type.

L15 - Pointers Page 5

In C++, void pointers cannot be dereferenced.

Null Pointers
A null pointer is a pointer variable that contains the null pointer value and therefore
it points to nowhere.

In C++, null pointers cannot be dereferenced.

Pointer to Pointer
In C++, we can create a pointer to point to another pointer.

Pointers and Arrays
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

L15 - Pointers Page 6

Since the name of an array in C++ works exactly how a pointer works, we can
assign an array name to a pointer.

The difference between a pointer and array name is that while a pointer can be
assigned a different address, the array name cannot be assigned anything.

L15 - Pointers Page 7

