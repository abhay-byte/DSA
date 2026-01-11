# Lecture 23

**Source:** `L23 - Recursion.pdf`

---

Sum of Array

Sum of Array
Given an array of N integer, design a recursive algorithm to compute the sum of
array elements.
Example
Input
0

1

2

3

4

10 20 30 40 50
Output : 150

L23 - Recursion Page 1

L23 - Recursion Page 2

L23 - Recursion Page 3

[HW] First Occurrence

First Occurrence
Given an array of N integers and a target integer T, design a recursive algorithm to
find the index of its first occurrence in the given array.
note : return -1 if T is not present in the given array.
Example
Input
T = 20
0

1

2

3

4

10 20 30 20 30
Output : 1

L23 - Recursion Page 4

[HW] Last Occurrence

Last Occurrence
Given an array of N integers and a target integer T, design a recursive algorithm to
find the index of its last occurrence in the given array.
note : return -1 if T is not present in the given array.
Example
Input
T = 20
0

1

2

3

4

10 20 30 20 30
Output : 3

L23 - Recursion Page 5

[HW] All Occurrences

All Occurrences
Given an array of N integers and a target integer T, design a recursive algorithm
to find the indices of all of its occurrences in the given array.

note : print -1 if T is not present in the given array.
Example
Input
T = 20
0

1

2

3

4

10 20 30 20 30
Output : 1, 3

L23 - Recursion Page 6

Is Array Sorted ?

Is Array Sorted ?
Given an array of N integer, design a recursive algorithm to check if it is sorted in
the increasing order.
Example
Input
0

1

2

3

4

10 20 30 40 50
Output : True

L23 - Recursion Page 7

L23 - Recursion Page 8

[HW] Binary Search

Binary Search
Given a sorted array consisting of N distinct integers and a target integer T, design a
recursive algorithm to find the index of its occurrence in the array.
note : return -1 if T is not present in the given array.
Example
Input

T = 20
0

1

2

3

4

10 20 30 40 50
Output : 1

L23 - Recursion Page 9

[R][HW] Ternary Search

Ternary Search
Ternary Search is an algorithm that is used to find the maximum/minimum
value in an unimodal function.

s

m1

m2

e

L23 - Recursion Page 10

s

m 1 m2

e

Analysis of Ternary Search

L23 - Recursion Page 11

[R][HW] Peak Index in Mountain Array

Peak Index in Mountain Array
Given an unimodal sequence of integers, design an algorithm to find the
maximum element present in it.
Example
0

1

2

3

4

5

6

0

1

3

10

3

1

0

s

m1

L23 - Recursion Page 12

m2

e

Merge Sort

Merge Sort
Given an array of N integers, sort it using the merge sort algorithm.
Example
0
1
2
3
4
50 40 30 20 10
10 20 30 40 50
The merge sort algorithm operates as per the divide and conquer strategy and
involves three steps to sort an array

○ divide the array into two subarray around the mid-points
○ recursively sort the two sub-arrays
○ merge the two sorted subarrays

L23 - Recursion Page 13

L23 - Recursion Page 14

L23 - Recursion Page 15

L23 - Recursion Page 16

[HW] Reverse Pairs

https://leetcode.com/problems/reverse-pairs/

L23 - Recursion Page 17

Quick Sort

Quick Sort
Given an array of N integers, sort it using the quick sort algorithm.
Example
0
1
2
3
4
5
60 50 20 10 40 30
10 20 30 40 50 60
The quick sort algorithm operates as per the divide and conquer strategy and
involves two steps to sort an array
○ partition the array into two subarray around the pivot such that
▪ all the elements in the left partition are < the pivot
▪ all the element in the right partition are > the pivot
○ recursively sort the two sub-arrays

0
1
2
3
4
5
60 50 20 10 40 30

0
1
2
3
4
5
60 50 20 10 40 30

.

.

L23 - Recursion Page 18

.

0
1
2
3
4
5
60 50 20 10 40 30

L23 - Recursion Page 19

[HW] Quick Select

Quick Select
Given an array of N integers, design an algorithm to find the Kth smallest element in it.
Example
K=3

arr []

0

1

2

3

4

5

2

7

5

3

8

4

s
e

pi

.....

L23 - Recursion Page 20

.....

.

L23 - Recursion Page 21

