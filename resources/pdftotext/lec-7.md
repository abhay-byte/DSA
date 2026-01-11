# Lecture 7

**Source:** `L7 - Intro to C^M^M.pdf`

---

Pattern - 8

Given a positive number N, design an algorithm to print the pattern as
shown in the example below.
Example
N=5

A
A
A
A
A

B
B
B
B

C
C
C

D
D

E

L7 - Intro to C^M^M Page 1

Pattern - 9

Given a positive number N, design an algorithm to print the pattern as
shown in the example below.
Example
N=5

A
A
A
A
A

B
B
B
B
A

C
C
C
B

D
D
C
A

E
D
B

E
C
A

D
B

C
A

B

A

C
C
C
B

D
D
C
A

E
D
B

E
C
A

D
B

C
A

B

A

N=5

A
A
A
A
A

B
B
B
B
A

L7 - Intro to C^M^M Page 2

[HW] Pattern - 10

Given a positive odd number N, design an algorithm to print the
pattern as shown in the example below.

Example
N=9

*
*
*
*
*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*

*
*
*

*

N=9

L7 - Intro to C^M^M Page 3

*
*
*
*
*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*

*
*
*

*

L7 - Intro to C^M^M Page 4

Pattern - 11

Given a positive odd number N, design an algorithm to print the
pattern as shown in the example below.
Example

N=9

*

*
*
*

*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*

*
*
*

*

*
*
*
*
*
*
*

*
*
*
*
*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*

*
*
*

*

N=9

*

*
*
*

*
*
*
*
*

N=9

*
L7 - Intro to C^M^M Page 5

N=9

*

*
*
*

*
*
*
*
*

*
*
*
*
*
*
*

*
*
*
*
*
*
*
*
*

L7 - Intro to C^M^M Page 6

*
*
*
*
*
*
*

*
*
*
*
*

*
*
*

*

[HW] Pattern - 12

Given a positive odd number N, design an algorithm to print the pattern as
shown in the example below.
Example
N=9

*
*
*
*
*

*
*
*
*

*

*

*

*

*

*

*

*

*
*
*

*
*
*

*
*

*
*

*

*

*
*

*
*

*
*
*

*
*
*
*

*
*
*
*
*

*

*

*
*
*

*

*

*

*

*

*

*
*
*

*
*
*
*

*
*
*
*
*

N=9

*
*
*
*
*

*
*
*
*

*
*
*

*
*

*

_

_

_

_

_

_

_

_

_

_

_

_

_

_

_

*

*

_

_

_

_

_

*

_

L7 - Intro to C^M^M Page 7

*
*

*

*

*

_

_

_

_

_

*

*

*

*

_

_

_

*

*

_

*

*

*
*

*

*

*
*

*
*
*

*

*

*
*
*

*

*

*

L7 - Intro to C^M^M Page 8

Bitwise Operators in C++ - Part I

Bitwise Operators in C++
C++ offers six different Bitwise operators.
Bitwise Comparator
&
|
^
~
<<
>>

Example
a&b
a|b
a^b
~a
a << b
a >> b

Meaning
Bitwise AND
Bitwise OR
Bitwise XOR
Bitwise NOT
Bitwise Left Shift
Bitwise Right Shift

Bitwise AND ( & ) Operator

1
1
0
0

1
0
1
0

&
1
0
0
0

L7 - Intro to C^M^M Page 9

4th 3rd 2nd 1st 0th

a = 25

1

1

0

0

1

b = 19
a&b

1

0

0

1

1

Bitwise OR ( | ) Operator

1
1
0
0

1
0
1
0

|
1
1
1
0

Bitwise XOR ( ^ ) Operator

L7 - Intro to C^M^M Page 10

4th 3rd 2nd 1st 0th

a = 25

1

1

0

0

1

b = 19
a | b

1

0

0

1

1

Bitwise XOR ( ^ ) Operator

1
1
0
0

1
0
1
0

^
0
1
1
0

4th 3rd 2nd 1st 0th

a = 25 1

1

0

0

1

b = 19
a^b

0

0

1

1

1

Bitwise NOT( ~ ) Operator

1
0

~
0
1

L7 - Intro to C^M^M Page 11

4th 3rd 2nd 1st 0th

a = 25 1
~a
0

1
0

0
1

0
1

1
0

Unique Number

Unique Number
Given a sequence of N non-negative numbers where every number is present
twice except for one number which is present only once. Design an algorithm to
find the unique number without using any extra space.
Example
Input : N = 7

3

1

4

1

2

3

Output : 2

L7 - Intro to C^M^M Page 12

4

Bitwise Operators in C++ - Part II

Bitwise Operators in C++
C++ offers six different Bitwise operators.
Bitwise Comparator
&
|
^
~
<<
>>

Example
a&b
a|b
a^b
~a
a << b
a >> b

Meaning
Bitwise AND
Bitwise OR
Bitwise XOR
Bitwise NOT
Bitwise Left Shift
Bitwise Right Shift

Bitwise Left Shift Operator ( << )
The bitwise left shift operator moves the bits of its first operand to the left by
the number of places specified by its second operand. It also inserts zero bits
to fill the gaps that arise on the right side of the new bit pattern.

3rd 2nd 1st 0th

0

L7 - Intro to C^M^M Page 13

0

0

1 a=1

Bitwise Right Shift Operator ( >> )
The bitwise right shift operator moves the bits of its first operand to the right
by the number of places specified by its second operand. Moreover, it inserts
zero bits to fill the gaps that arise on the left side of the new bit pattern.

3rd 2nd 1st 0th

1

L7 - Intro to C^M^M Page 14

0

0

0 a=8

Check Odd Even

Check Odd Even
Given a non-negative integers N, use bitwise operators to check if it is odd or even.
Example
Input : N = 10
Output : True
Input : N = 7
Output : False

L7 - Intro to C^M^M Page 15

Set Kth Bit

Set Kth Bit
Given a non-negative integer N, design an algorithm set its Kth bit.
Example

Input : N = 42, K = 4
Output : 58

N=42, K=4
5th

4th

3rd

2nd

1st

0th

i/p

1

0

1

0

1

0

o/p

1

1

1

0

1

0

L7 - Intro to C^M^M Page 16

Clear Kth Bit

Clear Kth Bit
Given a non-negative integer N, design an algorithm clear its Kth bit.
Example
Input : N = 42, K = 3
Output : 34

N=42, K=3
5th

4th

3rd

2nd

1st

0th

i/p

1

0

1

0

1

0

o/p

1

0

0

0

1

0

L7 - Intro to C^M^M Page 17

Check Kth Bit

Check Kth Bit
Given a non-negative integer N, design an algorithm check if its Kth bit is set or not.
Example
Input : N = 42, K = 3
Output : true
Input : N = 42, K = 4
Output : false
5th

4th

3rd

2nd

1st

0th

1

0

1

0

1

0

N=42, K=4

N=42, K=3
5th

4th

3rd

2nd

1st

0th

5th

4th

3rd

2nd

1st

0th

0
1 << K 0
N
1
&
0

0
0
0
0

0
1
1
1

0
0
0
0

0
0
1
0

1
0
0
0

0
1 << K 0
N
1
&
0

0
1
0
0

0
0
1
0

0
0
0
0

0
0
1
0

1
0
0
0

5th

4th

3rd

2nd

1st

0th

1

0

1

0

1

0

N=42, K=4

N=42, K=3

N

5th

4th

3rd

2nd

1st

0th

1

0

1

0

1

0

L7 - Intro to C^M^M Page 18

N

N=42, K=4

N=42, K=3
5th

4th

3rd

2nd

1st

0th

1
N >> K 0
0
&
0

0
0
0
0

1
0
0
0

0
1
0
0

1
0
0
0

0
1
1
1

N

L7 - Intro to C^M^M Page 19

N

5th

4th

3rd

2nd

1st

0th

1

0
0
0
0

1
0
0
0

0
0
0
0

1
1
0
0

0
0
1
0

N >> K 0
&

0
0

Flip Kth Bit

Flip Kth Bit
Given a non-negative integer N, design an algorithm flip its Kth bit.
Example
Input : N = 42, K = 3
Output : 34
Input : N = 42, K = 4
Output : 58
5th

4th

3rd

2nd

1st

0th

1

0

1

0

1

0

5th

4th

3rd

2nd

1st

0th

i/p

1

0

1

0

1

0

o/p

1

0

0

0

1

0

5th

4th

3rd

2nd

1st

0th

i/p

1

0

1

0

1

0

o/p

1

1

1

0

1

0

N=42, K=3

N=42, K=4

L7 - Intro to C^M^M Page 20

o/p

1

1

1

0

1

L7 - Intro to C^M^M Page 21

0

Count Set Bits

Count Set Bits
Given a 32-bit non-negative integer N, design an algorithm to count the no. of its set bits.
Example
Input : N = 42
Output : 3
5th

4th

3rd

2nd

1st

0th

1

0

1

0

1

0

L7 - Intro to C^M^M Page 22

[HW] Longest Run of 1s

Longest Run of 1s in Binary
Given a integer N, find the length of the longest consecutive run of 1s in its binary representation.

Example
Input : N = 247
Output : 4

N

7th

6th

5th

4th

3rd

2nd

1st

0th

1

1

1

1

0

1

1

1

L7 - Intro to C^M^M Page 23

[HW] Hamming Distance

Hamming Distance
Given two 32-bit integers N and M, design an algorithm to find the Hamming Distance
between them. The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Example
Input : N = 42 M = 36
Output : 3
5th

4th

3rd

2nd

1st

0th

N

1

0

1

0

1

0

M

1

0

0

1

0

0

L7 - Intro to C^M^M Page 24

[HW] Power of 2

Power of 2
Given a non-negative integer N, design an algorithm to check if it is a power of 2.

Example
Input : N = 8
Output : True

Input : N = 10
Output : False

L7 - Intro to C^M^M Page 25

[HW] Power of 4

Power of 4
Given a 32-bit non-negative integer N, design an algorithm to check if it is a power of 4.
Example

Input : N = 16
Output : True
Input : N = 8
Output : False

L7 - Intro to C^M^M Page 26

Compound Assignment Operators

Compound Assignment Operators in C++
Operator
+=
-=
*=
/=
%=
&=
|=
^=
<<=
>>=

Example
a += b
a -= b
a *= b
a /= b
a %= b
a &= b
a |= b
a ^= b
a <<= b
a >>= b

L7 - Intro to C^M^M Page 27

Equivalent to
a=a+b
a=a-b
a=a*b
a=a/b
a=a%b
a=a&b
a=a|b
a=a^b
a = a << b
a = a >> b

