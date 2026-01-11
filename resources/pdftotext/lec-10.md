# Lecture 10

**Source:** `L10 - 1D Arrays.pdf`

---

Bubble Sort

Bubble Sort
Given an array of N integers, sort the array using the bubble sort algorithm.

Example
Input
0

1

2

3

4

50 40 30 20 10
Output
0

1

2

3

4

10 20 30 40 50

The bubble sort algorithm works in passes such that in its each pass, we place
the largest element in the un-sorted part of the array to its correct position.

0

1

2

3

4

50 40 30 20 10

0

1

2

3

4

40 30 20 10 50

0

1

2

3

4

30 20 10 40 50

0

1

2

3

4

20 10 30 40 50

L10 - 1D Arrays Page 1

0

1

2

3

4

20 10 30 40 50

L10 - 1D Arrays Page 2

L10 - 1D Arrays Page 3

Selection Sort

Selection Sort
Given an array of N integers, sort the array using the selection sort algorithm.
Example
Input
0

1

2

3

4

50 40 10 30 20

Output
0

1

2

3

4

10 20 30 40 50

The selection sort algorithm works in passes such that in its each pass, we place
the smallest element in the un-sorted part of the array to its correct position.

0

1

2

3

4

50 40 10 30 20

0

1

2

3

4

10 40 50 30 20

0

1

2

3

4

10 20 50 30 40

0

1

2

3

4

10 20 30 50 40

L10 - 1D Arrays Page 4

L10 - 1D Arrays Page 5

Insertion Sort

Insertion Sort
Given an array of N integers, sort the array using the insertion sort algorithm.
Example

Input
0

1

2

3

4

50 40 10 30 20
Output
0

1

2

3

4

10 20 30 40 50

The insertion sort algorithm works in passes such that in its each pass, we place
the first element in the un-sorted part of the array to its correct position in the
sorted part of the array.

0

1

2

3

4

50 40 10 30 20

0

1

2

3

4

40 50 10 30 20

0

1

2

3

4

10 40 50 30 20

L10 - 1D Arrays Page 6

0

1

2

3

4

10 30 40 50 20

L10 - 1D Arrays Page 7

L10 - 1D Arrays Page 8

Binary Search

Binary Search
Given a sorted array of N distinct integers & an integer T, implement
the binary search algorithm to find the index of T in the given array.
note : output -1 if T is not present in the given array.
Example
Input
N = 7 ; T = 20
0

1

2

3

4

5

6

10 20 30 40 50 60 70
Output : 1

L10 - 1D Arrays Page 9

L10 - 1D Arrays Page 10

First Occurrence in Sorted Array

First Occurrence in Sorted Array
Given a sorted array of N integers, & an integer T, design an
algorithm to find the index of the 1st occurrence of T in the
given array. You've to output -1 if T isn't present in the array.
Example
Input : N = 8 ; T = 30
0

1

2

3

4

5

6

7

10 20 30 30 30 30 40 50
Output : 2

L10 - 1D Arrays Page 11

[R][HW] Last Occurrence in Sorted Array

Last Occurrence in Sorted Array
Given a sorted array of N integers, & an integer T, design an
algorithm to find the index of the last occurrence of T in the
given array. You've to output -1 if T isn't present in the array.
Example
Input : N = 8 ; T = 30
0

1

2

3

4

5

6

7

10 20 30 30 30 30 40 50
Output : 5

L10 - 1D Arrays Page 12

[R][HW] Count Occurrences in Sorted Array

Count Occurrences in Sorted Array
Given a sorted array of N integers, & an integer T, design an algorithm
to count the total no. of the occurrences of T in the given array. You've
to output -1 if T isn't present in the array.
Example
Input : N = 8 ; T = 30
0

1

2

3

4

5

6

7

10 20 30 30 30 30 40 50
Output : 4

L10 - 1D Arrays Page 13

