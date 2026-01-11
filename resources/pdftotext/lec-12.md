# Lecture 12

**Source:** `L12 - 1D Arrays.pdf`

---

[R][HW] Generate Subsequences

Generate Subsequences
Given a sequence of integers, design an algorithm to generate all of its subsequences.
Note : We define a subsequence of a given sequence as a sequence which can be
obtained by deleting zero or more elements from the given sequence such that the
relative order between the sequence elements doesn't change.
Example
Input
0

1

2

10 20 30

L12 - 1D Arrays Page 1

Generate Pairs

Generate Pairs
Given an array of N integers, design an algorithm to generate all of its pairs.
Example
Input
0

1

2

3

4

10 20 30 40 50
Output

( 10, 20 ), ( 10, 30 ), ( 10, 40 ), ( 10, 50 ),
( 20, 30 ), ( 20, 40 ), ( 20, 50 ),
( 30, 40 ), ( 30, 50 ),
( 40, 50 )

L12 - 1D Arrays Page 2

Target Sum Pairs

Target Sum Pairs
Given a sorted array containing N distinct integers, and a target integer T,
design an algorithm to count the number of pairs of integers in the given
array whose sum is equal to T.

Example
Input
N = 6, T = 60
0

1

2

3

4

5

10 20 30 40 50 60
Output : 2

0
N-1

1

2

3

.....

L12 - 1D Arrays Page 3

0

1

2

3

4

5

10 20 30 40 50 60

L12 - 1D Arrays Page 4

Sereja and Dima

Sereja and Dima

.

L12 - 1D Arrays Page 5

L12 - 1D Arrays Page 6

Container with Most Water

Container with Most Water
Given an array of N integers representing heights of N vertical lines. Find two lines
that together with the x-axis form a container, such that the container contains the
most water. Return the maximum amount of water a container can store.
Example
Input
N=9
0

1

2

3

4

5

6

7

8

1

8

6

2

5

4

8

3

7

Output : 49

8

8

7
6
5
4
3
2
1

0
8

1

2

3

4

5

8

6

7

8
7
6
5

4
3

2
1

0
8

1

L12 - 1D Arrays Page 7

2

3

4

5

6

7

L12 - 1D Arrays Page 8

Merge Two Sorted Arrays

Merge Sorted Arrays
Given two sorted array consisting of N and M integers respectively, design an
algorithm to merge the two sorted array such that the merged array is sorted.
Example
Input
0

1

2

3

0

10 30 50 70

1

2

20 40 60

Output
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

0

3

0

1

2

3

L12 - 1D Arrays Page 9

1

2

20 40 60

10 30 50 70

4

5

6

L12 - 1D Arrays Page 10

[HW] Counting Smaller Elements

Counting Smaller Elements
Given two sorted arrays consisting of N & M integers respectively, find out for
each element in the first array the no. of elements smaller than that element in
the second array.
Example
Input
0

1

2

4

6

8

0

1

2

3

4

5

1

2

3

5

7

9

Output
3

4

5

L12 - 1D Arrays Page 11

[HW] Merge Two Sorted Arrays in O(1) Space

Merge Sorted Arrays in O(1) Space
Given a sorted array "A" of size N+M consisting of N integers & another sorted
array "B" consisting of M integers, design an algorithm to merge the two sorted
array such that the merged array is also sorted without using any extra space.
Example

Input
0

1

2

3

4

5

6

10 30 50 70

1

2

3

1

2

20 40 60

Output
0

0

4

5

6

10 20 30 40 50 60 70

L12 - 1D Arrays Page 12

