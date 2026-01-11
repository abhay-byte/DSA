# Lecture 21

**Source:** `L21 - Object Oriented Programming.pdf`

---

OOP

Object Oriented Programming
It is a style of programming that allows you to very conveniently model real-world entities.

name

...

age

...

gender

...

credits

...

c1
name
age
gender
credits

c2
name
age
gender
credits

c3
name
age
gender
credits

c4
name
age
gender
credits

c5
name
age
gender
credits

...

• A class is a blueprint of the entity you are trying to model e.g. customer.

• A class in itself does not consume any memory.
• An object is an instance of the class and consumes memory.

name

age

L21 - Object Oriented Programming Page 1

gender

credits

name

gender

age

credits

Constructor
It is a special member function of a class used to initialize a class object.
• it has the same name as the class name
• it does not have a return type
• it is invoked automatically upon declaration of an object to construct it.

A parameterized constructor is a class constructor to which we pass arguments
corresponding to initial values of data-members of the object being constructed.

name

Ramanujan
32

M

1729

age

gender

credits

Once you provide an implementation of a parameterized constructor, the compiler no
longer provides an implicit default constructor.

Destructor
It is a special member function of a class used to destruct a class object.
• it has the same name as the class name ( preceded by ~ )
• it does not have a return type
• it does not accept any arguments
• it is invoked automatically once an object goes out of scope to destruct it.
Unlike a constructor, a destructor cannot be overloaded.

L21 - Object Oriented Programming Page 2

Data Members on Heap Memory

Ramanujan
namePtr

credits

1729
32

M

age

gender

C

Operator Overloading

Operators are overloaded by means of operator functions, which are regular
functions with special names ___ their name begins by the operator keyword
followed by the operator sign that is overloaded.

L21 - Object Oriented Programming Page 3

name

Ramanujan
C1
32

M

1729

age

gender

credits

name

Aryabhata
C2
74

M

0

age

gender

credits

Pointers and Objects

name

Ramanujan

L21 - Object Oriented Programming Page 4

32

M

1729

age

gender

credits

Passing Objects to
Functions

Creating Objects on Heap Memory

name

age

gender

credits

name

Ramanujan

32

M

1729

age

gender

credits

This Pointer
this is a const pointer to an object on which a member function is invoked.

The this pointer can be used to disambiguate a parameter with the same name as
a data member withing a member function.

L21 - Object Oriented Programming Page 5

L21 - Object Oriented Programming Page 6

