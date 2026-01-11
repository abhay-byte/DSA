# Lecture 13

**Source:** `L13 - 1D Arrays.pdf`

---

Rain-Water Trapping

Rain-Water Trapping
Given an array of N integers representing height of N buildings, find the total
amount of rainwater that can be trapped between the building such width of
each building is 1 unit.
Example :
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

10

11

0

1

0

2

1

0

1

3

2

1

2

1

i-1

i

i+1

h

0
n-1
.....

L13 - 1D Arrays Page 1

.....

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

9

10

11

h

0

1

0

2

1

0

1

3

2

1

2

1

l
r

L13 - 1D Arrays Page 2

L13 - 1D Arrays Page 3

[HW] Product of Array Except Self

Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Example :
Input
0

1

2

3

4

1

2

3

4

5

2

3

4

Output
0

1

120 60 40 30 24

L13 - 1D Arrays Page 4

[R][HW] 3Sum

[HW] https://leetcode.com/problems/3sum-closest/
[HW] https://leetcode.com/problems/4sum/

3Sum
Given an integer array nums, return all the triplets { numsi, numsj, numsk }
such that i != j, i != k and j != k and numsi + numsj + numsk == 0.
Notice that the solution set must not contain duplicate triplets.

Example
Input
0

1

2

3

4

5

-1

0

1

2

-1

-4

L13 - 1D Arrays Page 5

[HW] 3Sum Closest

[HW] https://leetcode.com/problems/3sum-closest/

L13 - 1D Arrays Page 6

[HW] 4Sum

[HW] https://leetcode.com/problems/4sum/

L13 - 1D Arrays Page 7

DNF Sort

DNF (Dutch National Flag) Sort
Given an array containing 0s, 1s & 2s design an algorithm to sort the array.
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

0

1

2

0

1

2

0

1

Output
0

1

2

3

4

5

6

7

8

0

0

0

1

1

1

1

2

2

The idea behind the DNF algorithm is to partition the given array into
four parts using three pointers - low, mid & high and then to iteratively
shrink the unknown part to zero elements so that the array is sorted.

zeros

arr

arr

arr

ones

unknown

twos

0

1

2

3

4

5

6

7

8

0

1

1

1

0

1

2

0

2

0

1

2

3

4

5

6

7

8

0

0

1

1

1

1

2

0

2

0

1

2

3

4

5

6

7

8

0

0

1

1

1

1

2

0

2

L13 - 1D Arrays Page 8

arr

arr

0

1

2

3

4

5

6

7

8

0

0

1

1

1

1

2

0

2

0

1

2

3

4

5

6

7

8

0

0

1

1

1

1

0

2

2

L13 - 1D Arrays Page 9

Counting Sort

Counting Sort
Given an array of N non-negative integers, design an algorithm to
sort the array such that each array element is <= a given integer K.
Example
Input
N = 9, K = 3
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

0

3

2

3

1

2

0

2

Output
0

1

2

3

4

5

6

7

8

0

0

1

1

2

2

2

3

3

L13 - 1D Arrays Page 10

[R][HW] Generalized Counting Sort

Generalized Counting Sort
Given an array of n integers, design an algorithm to sort the array such
that each array element is in the range [ l, r ] , assume l <= r
Example
Input
n = 10, l = 2, r = 4
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

4

3

2

2

4

3

5

4

5

2

Output
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

2

2

2

3

3

4

4

4

5

5

L13 - 1D Arrays Page 11

