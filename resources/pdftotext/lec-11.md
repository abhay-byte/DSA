# Lecture 11

**Source:** `L11 - 1D Arrays.pdf`

---

Generate Sub-Arrays

Generate Sub-Arrays
Given an array of N integers, design an algorithm to generate all of its sub-arrays.
Note : We define a sub-array of an array as a contiguous part of the given array.
Example
Input
0

1

2

3

4

10 20 30 40 50

L11 - 1D Arrays Page 1

Maximum Subarray Sum

Maximum Subarray Sum
Given an array of N integers, design an algorithm to find the maximum subarray sum.
Example

Input
0

1

2

3

4

5

6

7

8

-2

1

-3

4

-1

2

1

-5

4

Output : 6

0 -2 -1 -4 0 -1 1 2 -3 1

arr
csum

0

0

1

2

3

4

5

6

7

8

-2

1

-3

4

-1

2

1

-5

4

1

2

3

4

5

6

7

8

9

0

arr

...

i-1
j

i

arr
csum

...

.....

0

1

2

3

4

5

6

7

8

-2

1

-3

4

-1

2

1

-5

4

0

1

2

3

4

5

6

7

8

9

0

-2

-1

-4

0

-1

1

2

-3

1

L11 - 1D Arrays Page 2

Maximum Subarray Sum using Kadane's Algorithm

Maximum Subarray Sum using Kadane's Algorithm
Given an array of N integers, design an algorithm to find the maximum subarray sum.

Example
Input
0

1

2

3

4

-3

2

-1

4

-5

Output : 5

arr

0
N-1

1

2

3

.....

arr

0

1

2

3

4

-3

2

-1

4

-5

i-1

i

X

arr

0
N-1

1

2

.....

L11 - 1D Arrays Page 3

.....

arr

X

L11 - 1D Arrays Page 4

0

1

2

3

4

-3

2

-1

4

-5

L11 - 1D Arrays Page 5

[HW] Maximum Circular Subarray Sum

Maximum Circular Subarray Sum
Given an array of N integers, design an algorithm to find the maximum circular
subarray sum.
Example
Input
0

1

2

3

4

5

-1 -2 -3
Output : 6

1

2

3

2

3

4

5

1
2 -3
Output : 14

-4

5

6

Input
0

1

L11 - 1D Arrays Page 6

[HW] Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/description/

L11 - 1D Arrays Page 7

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

L11 - 1D Arrays Page 8

Vectors
Saturday, 17 May 2025

10:46 AM

L11 - 1D Arrays Page 9

L11 - 1D Arrays Page 10

