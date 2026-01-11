# Lecture 30

**Source:** `L30 - Stack and Queues.pdf`

---

Nearest Greater Element to the Right

Nearest Greater Element to the Right
Given an array of N integers, design an algorithm to find, for each element, the
nearest greater element to its right.

Note : for an element without a greater element to its right, output -1.
Example :
Input
Output

5
6

3
6

6
7

7
-1

L30 - Stack and Queues Page 1

2
4

1
4

4
-1

5

3

6

7

-1 4 4 -1 7 6 6

L30 - Stack and Queues Page 2

2

1

4

L30 - Stack and Queues Page 3

Nearest Greater Element to the Left

Nearest Greater Element to the Left
Given an array of N integers, design an algorithm to find, for each element, the nearest
greater element to its left.
Note : for an element without a greater element to its left, output -1.
Example :
Input
Output

5
-1

2
5

0
2

4
5

-1 5 2 5 4 4 -1

L30 - Stack and Queues Page 4

1
4

3
4

6
-1

Stock Span Problem

Stock Span Problem
Given prices of a stock for N consecutive days, design an algorithm to find, for each
day, span of stock price on that day.
We define span of stock price today as the maximum number of consecutive days
( staring from today and going backwards ) for which the stock price was less than or
equal to today's price.
Example :

0
1
2
3
4
5
6
Input 100 80 60 70 60 75 85
Output 1
1
1
2
1
4
6

0
1
2
3
4
5
6
7
Input 100 80 60 70 60 75 85 200
Output 1
1
1
2
1
4
6
8

0
1
2
3
4
5
6
7
Input 100 80 60 70 60 75 85 200
Output 1
1
1
2
1
4
6
8

0
1
2
3
4
5
6
7
Input 100 80 60 70 60 75 85 200

L30 - Stack and Queues Page 5

L30 - Stack and Queues Page 6

[HW] 132-Pattern

132-Pattern
Given an array of N integers nums, design an algorithm to check if there exists a
132-Pattern in nums. We define a 132-Pattern as a subsequence of 3-integers
nums[i], nums[j] and nums[k] such that
• i < j < k and
• nums[i] < nums[k] < nums[j].
Example :
N=6

Input

0
3

1
4

2
6

3
2

Output : true

L30 - Stack and Queues Page 7

4
1

5
5

[R][HW] Nearest Smaller Element to the Right

Nearest Smaller Element to the Right
Given an array of N integers, design an algorithm to find, for each element, the index
of nearest smaller element to its right.
Note : for an element without a smaller element to its right, output N
Example :

Input
Output

0
2
2

1
5
2

2
1
6

3
3
6

L30 - Stack and Queues Page 8

4
6
5

5
4
6

6
0
7

[R][HW] Nearest Smaller Element to the Left

Nearest Smaller Element to the Left
Given an array of N integers, design an algorithm to find, for each element, the index
of nearest smaller element to its left.
Note : for an element without a smaller element to its left, output -1
Example :

Input
Output

0
0
-1

1
3
0

2
5
1

3
4
1

L30 - Stack and Queues Page 9

4
1
0

5
6
4

6
2
4

[HW] Number of Valid Subarrays

Number of Valid Subarrays
Given an integer array nums, design an algorithm to find the number of non-empty
sub-arrays with the leftmost element of the subarray not larger than other elements in
the subarray.
Example :

Input

0
1

1
4

2
2

3
5

Output : 15

L30 - Stack and Queues Page 10

4
3

5
9

[R][HW] Largest Rectangle in Histogram

Largest Rectangle in Histogram
Given an array of N integers representing heights of bars in a histogram where width
of each bar is a 1 unit, design an algorithm to find the area of the largest rectangle
in the histogram.
Example :
0
2

1
1

6
2
5

3
6

4
2

5
3

5
3
2

2
1

6
5
3

2

2
1

0
-1

0
0

L30 - Stack and Queues Page 11

1

2

3

4

5

6

6

5
3
2

2
1

0
-1

0
0

L30 - Stack and Queues Page 12

1

2

3

4

5

6

[HW] Maximal Rectangle

https://leetcode.com/problems/maximal-rectangle/

L30 - Stack and Queues Page 13

Nearest Greater Element to the Right

Nearest Greater Element to the Right
Given an array of N integers, design an algorithm to find, for each element, the nearest
greater element to its right.

Note : for an element without a greater element to its right, output -1.
Example :
Input
Output

5
6

3
6

6
7

7
-1

L30 - Stack and Queues Page 14

2
4

1
4

4
-1

Input

ans

L30 - Stack and Queues Page 15

0
5

1
3

2
6

3
7

4
2

5
1

6
4

0

1

2

3

4

5

6

[HW] Next Greater Element IV

https://leetcode.com/problems/next-greater-element-iv/

L30 - Stack and Queues Page 16

[HW] Next Greater Node in Linked List

http://leetcode.com/problems/next-greater-node-in-linked-list/

L30 - Stack and Queues Page 17

Queue Data Structure

L30 - Stack and Queues Page 18

L30 - Stack and Queues Page 19

L30 - Stack and Queues Page 20

First Non-Repeating Character in a Stream

First Non-Repeating Character in a Stream
Given a stream of characters, design an algorithm to find, for each character, first
non-repeating character in the stream.
Note : output -1 if upon reading a character there are no non-repeating characters
in the stream.
Example :

Input
Output

0
a
a

1
a
-1

2
b
b

3
c
b

4
d
b

5
b
c

0
a

1
a

2
b

3
c

4
d

5
b

6
c

Input

L30 - Stack and Queues Page 21

6
c
d

[HW] Implement a Stack using Two Queues

Implement a Stack Class using Two Queues

L30 - Stack and Queues Page 22

