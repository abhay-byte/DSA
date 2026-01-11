# Lecture 38

**Source:** `L38 - Tries.pdf`

---

Tries - Introduction I

Introduction to Tries
Given a sequence of N words and a sequence of Q queries, design an algorithm to
check if each of the Q queries are present in the given sequence of N words.
Example
Input :

words = ["code", "coder", "coding", "block", "blocks", "news"]
queries = ["code", "coding", "blocked", "block", "news", "new"]

Output :

True, True, False, True, True, False

1. using Linear Search

2. using HashSet (unordered_set)

3. using Tries

L38 - Tries Page 1

Tries - Introduction II

What are Tries ?
It is a data structure, specifically a kind of generic tree that supports efficient
lookups and insert operations that on average take time proportional to the key
length. A generic tree is a tree data-structure in which each node has 0 or
more child nodes.

L38 - Tries Page 2

Tries - String Insert

String Insertion in Tries
Example :
Input : "code"

L38 - Tries Page 3

Tries - String Lookup

String Lookup in Tries

C
O

D
E
R

L38 - Tries Page 4

N
E

W

S

Tries - Unique Prefix Array

Shortest Unique Prefix Array
Given an array of strings, design an algorithm to find the shortest unique prefix
for each string in the given array. If there is no unique prefix, return empty string.
Example

Input "code" "coder" "coding" "new" "neon"
Output
""
"coder" "codi" "new" "neo"

"code" "coder" "coding" "new" "neon"
C

N

E

O

E
R

O

W

D

N

I

N
G

L38 - Tries Page 5

Tries - Longest Common Prefix

Longest Common Prefix
Given an array of strings, design an algorithm to find the longest common prefix
string amongst the given strings. If there is no common prefix, return empty string.
Example

Input
"flow" "floor" "flys"
Output : "fl"

F,3

L,3

Y,1

O,2

W,1

O,1

S,1

R,1

L38 - Tries Page 6

Tries - Integer Insert

Integer Insertion in Tries
Example :

2
4
5
8
10

3rd

2nd

1st

0th

0
0
0
1
1

0
1
1
0
0

1
0
0
0
1

0
0
1
0
0

L38 - Tries Page 7

Tries - Lookup Integer

Integer Lookup in Tries
Example :

2
4
5
8
10

3rd

2nd

1st

0th

0
0
0
1
1

0
1
1
0
0

1
0
0
0
1

0
0
1
0
0

L38 - Tries Page 8

[R][HW] Tries - Maximum XOR Pair

Maximum XOR Pair
Given an array of N non-negative integers, design an algorithm to compute
the maximum XOR possible between a pair of integers in the given array.
Example :

Input :
0

1

2

3

4

2
4
5
8 10
Output : 15
Explanation : 5^10 = 15

Input
0

1

2

3

4

2

4

5

8

10

3rd

2nd

1st

0th

0
0
0
1
1

0
1
1
0
0

1
0
0
0
1

0
0
1
0
0

2
4
5
8
10

L38 - Tries Page 9

a
0
0
1
1

b
0
1
0
1

a^b
0
1
1
0

x=2
yideal
yactual
(x^y)ideal
(x^y)actual

x=5
yideal
yactual
(x^y)ideal
(x^y)actual

3rd

2nd

1st

0th

0

0

1

0

1

1

1

1

3rd

2nd

1st

0th

0

1

0

1

1

1

1

1

L38 - Tries Page 10

[R][HW] Tries - Maximum Subarray XOR

Maximum Subarray XOR
Given an array of N integers, design an algorithm to find the maximum subarray XOR.
Example
Input
0

1

2

3

4

5

25 10

2

8

5

3

Output : 31

arr

cxor

0

0

0

L38 - Tries Page 11

1

2

3

4

5

25 10

2

8

5

3

1

3

4

5

6

2

arr

...

i-1
j

i

arr
cxor

L38 - Tries Page 12

...

.....

0

1

2

3

4

5

25 10

2

8

5

3

0

1

3

4

5

6

0

25 19 17 25 28 31

2

