# Lecture 35

**Source:** `L35 - Heaps and HashMaps.pdf`

---

K Largest Elements

K Largest Elements
Given an array nums of N integers and a positive number K ( < N ),
design an algorithm to print the K largest elements in the given array.
Note : You can print the K largest element in any order.

Example
Input : nums = [60, 50, 10, 20, 30, 40], K = 3
Output : { 40, 50, 60 }

L35 - Heaps and HashMaps Page 1

K Largest Elements in a Stream

K Largest Elements in a Stream
Given a running stream of integers and a positive integer K, design an algorithm to
print the K largest elements in the stream every time you read a -1 from the stream.
Note : You can print the K largest element in any order.
Example
Input : [60, 50, 10, -1, 20, 30, -1, 40, -1, . . .], K = 3
Output : { 10, 50, 60 }
{ 30, 50, 60 }
{ 40, 50, 60 }
...

L35 - Heaps and HashMaps Page 2

Merge K-Sorted Linked Lists

Merge K-Sorted Linked List
Given the K sorted linked list, design an algorithm to merge them such that the
merged linked list is also sorted.

L35 - Heaps and HashMaps Page 3

L35 - Heaps and HashMaps Page 4

[R][HW] Merge K-Sorted Arrays

Merge K-Sorted Arrays
Given the K sorted arrays, design an algorithm to merge them such that the
merged array is also sorted.
Example
Input
0

1

2

3

1
2
0

3
4
6

7
5
8

10
11
9

Output
0
1

2

3

4

0
1
2

5

L35 - Heaps and HashMaps Page 5

6

7

8

9

10 11

[R][HW] Reorganize String

Reorganize String
Given a string, design an algorithm to check if the characters of the
given string can be reorganized in a way that no two characters
with the same value are adjacent to each other.

Example
Input

: "aab"

Input

: "aabca"

Input

: "aaab"

L35 - Heaps and HashMaps Page 6

[R][HW] Median of a Running Stream

Median of a Running Stream
Given a running stream of integers, design an algorithm to print the median of
the numbers in the stream each time a new integer is added to the stream.

Example
Input
Stream
Median

4
4

6
5

2
4

5
4.5

L35 - Heaps and HashMaps Page 7

3
4

1
3.5

7
4

9
4.5

8
5

...
...

Introduction

HashTable / HashMap
It is a data structure which is used to store a collection of key-value pairs.

Why use a HashTable ?
HashTable, as a data-structure supports very efficient lookup operation.

Reason behind Efficiency ?
Data is stored in a HashTable in an unordered-way.

L35 - Heaps and HashMaps Page 8

HashTable Implementation

HashTable Implementation
Example
Key
0
1
2
3
4

Value
0
1
4
9
16

0
-1

1
-1

2
-1

3
-1

4
-1

Limitations

• Keys are integer values that exceed the valid range of indices.
• Keys are non-integer values, e.g. strings

To solve this problem, we use a hash function - a mathematic function that transforms
the keys into a valid index inside the hash table a.k.a hash index.
Example

Key
0
7
9
6
8

Value
0
49
81
36
64

0
-1

1
-1

2
-1

3
-1

4
-1

Limitations
• Multiple (key, value) pairs can be mapped to the same index - collision
Example
Key
0
7
9
6

Value
0
49
81
36

0
0

1
2
36 49

3
-1

4
81

Handling Collision
• Closed Hashing or Open Addressing

○ Linear Probing
○ Quadratic Probing
○ Double Hashing
• Open Hashing or Chaining
The idea behind chaining is to maintain a linked list at each index ( or bucket ) of
the hash table to store all the (key, value) pairs that have been mapped to that index.

Key
0
7
8
6
2

Value
0
49
64
36
4

0

1

2

3

0,0

6,36

7,49

8,64

4

2,4

Rehashing
The idea behind rehashing is to double the capacity of hash table once the load
factor M/N exceeds a certain threshold.
How ?
By creating a new hash table with twice the capacity of the current hash table and
rehashing (key, value) pairs from current hash table to the new hash table. This way
we can lower the load factor & improve the efficiency of operations on hash table.

We will internally represent the hash table using a dynamic array of singly linked lists
such each node of the linked list present at the ith ( 0<=i<=N-1) index of the hash
table contains a (key, value) pair that was hashed/mapped to the ith index of the hash
table.

L35 - Heaps and HashMaps Page 9

L35 - Heaps and HashMaps Page 10

0

1

2

3

4

...

L35 - Heaps and HashMaps Page 11

L35 - Heaps and HashMaps Page 12

