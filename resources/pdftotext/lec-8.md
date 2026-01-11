# Lecture 8

**Source:** `L8 - 1D Arrays.pdf`

---

Introduction to Arrays

Introduction to Arrays
An array is a linear data structure, referred by a single name, which is used
to store a sequence of values of the same type.

arr

10 20 30 40 50

How to declare an array in C++ ?

Since arrays are allocated memory in a contiguous fashion, we can randomly
access an element in an array using its index in constant time i.e. O (1) time.

Array Initialization
L8 - 1D Arrays Page 1

Array Initialization
By default, when we declare an array in local-scope, it contains garbage value.

0

1

2

3

4

10 20 30 40 50

During the initialization of an array, specifying the size of the array is optional.

During initialization, the size of the initializer list must not exceed the array size.

What if the size of initializer list is less then array size ?

L8 - 1D Arrays Page 2

L8 - 1D Arrays Page 3

First Occurrence

First Occurrence
Given an array of N integers, and an integer T, design an algorithm
to find the index of the first occurrence of T in the given array.
note : output -1 if T is not present in the given array.
Example
Input : N = 5 ; T = 20
0

1

2

3

4

10 20 30 10 20
Output : 1

L8 - 1D Arrays Page 4

[HW] Last Occurrence

Last Occurrence
Given an array of N integers, and an integer T, design an algorithm
to find the index of the last occurrence of T in the given array.
note : output -1 if T is not present in the given array.
Example
Input : N = 5 ; T = 10
0

1

2

3

4

10 20 30 10 20
Output : 3

L8 - 1D Arrays Page 5

All Occurrences

All Occurrences
Given an array of N integers, and an integer T, design an algorithm
to find the indices of all occurrence of T in the given array.
note : output -1 if T is not present in the given array.
Example
Input : N = 5 ; T = 20
0

1

2

3

4

10 20 30 10 20
Output : 1, 4

L8 - 1D Arrays Page 6

Reverse Array

Reverse Array
Given an array of N integers, design an algorithm to reverse it.
Example
Input
0

1

2

3

4

5

6

10 20 30 40 50 60 70

Output
0

1

2

3

4

5

6

70 60 50 40 30 20 10

0

1

2

3

4

5

6

10 20 30 40 50 60 70

0

1

2

3

4

5

6

10 20 30 40 50 60 70

L8 - 1D Arrays Page 7

Reverse in Range
Given an array of N integers, and two non-negative integers i and j
where 0 <= i<j <= N-1 design an algorithm to reverse the subarray that
starts at the ith index and ends at the jth index.
Example

Input
i = 2, j = 5
0

1

2

3

4

5

6

10 20 30 40 50 60 70
Output
0

1

2

3

4

5

6

10 20 60 50 40 30 70

0

1

2

3

4

5

6

10 20 30 40 50 60 70

L8 - 1D Arrays Page 8

Rotate Array

Rotate Array
Given an array of N integers, design an algorithm to rotate the
array once in the clockwise direction.
Example
Input
0

1

2

3

4

5

6

10 20 30 40 50 60 70
Output
0

1

2

3

4

5

6

70 10 20 30 40 50 60

0

1

2

3

4

5

6

10 20 30 40 50 60 70

K-Rotate Array
Given an array of N integers, and a positive integer K design an
algorithm to K-rotate the array in the clockwise direction.
Example
Input
N=7;K=3
0

1

2

3

4

5

6

10 20 30 40 50 60 70

L8 - 1D Arrays Page 9

Output
0

1

2

3

4

5

6

50 60 70 10 20 30 40

N=7;K=3
0

1

2

3

4

5

6

10 20 30 40 50 60 70

N=7;K=3
0

1

2

3

4

5

6

10 20 30 40 50 60 70

L8 - 1D Arrays Page 10

[R][HW]Three Largest Elements

Three Largest Elements
Given an array of N integers, design an algorithm to find the
three largest elements present inside the given array

Example
Input
0

1

2

3

4

5

20

5

0

25 15 10

Output
15 20 25

L8 - 1D Arrays Page 11

[HW] Maximum Product of a Triplet

Maximum Product of a Triplet
Given an array of N integers, design an algorithm to find the
maximum product of a triplet present inside the given array.
Example
Input
0

1

2

3

4

20 5 25 15 10
Output : 7500
Input
0

1

2

3

4

-10 -20 1
Output : 600

2

3

L8 - 1D Arrays Page 12

