# Lecture 3

**Source:** `L3 - Number System.pdf`

---

Binary To Decimal

Number System
Humans use the decimal or base-10 number system. In contrast, since computers only
understand the language of 0's and 1's, they use the binary or base-2 number system.
➢ Converting a number from base-2 to base-10
5th 4th 3rd 2nd 1st 0th

( 1

0

1

0

1

0 )2

25

26

( ? ) 10

Power of 2's
20

21

22

23

24

1

2

4

8

16 32 64 128 256 512 1024 …

27

28

29

210

…

5th 4th 3rd 2nd 1st 0th

( 1 0
32 16

1
8

0
4

1
2

0 )2
1
( ? ) 10

5th 4th 3rd 2nd 1st 0th

( 1

0

1

0

1

0 )2
( ? ) 10

2nd 1st 0th

( 1

2

3 ) 10

L3 - Number System Page 1

( ? ) 10

.

L3 - Number System Page 2

Decimal to Binary

➢ Converting a number from base-10 to base-2

( 4

2 ) 10

( ? )2

Power of 2's
20

21

22

23

24

1

2

4

8

16 32 64 128 256 512 1024 …

25

26

27

28

29

210

…

5th 4th 3rd 2nd 1st 0th

( 4

2 ) 10

L3 - Number System Page 3

( 1

0

1

0

1

0 )2

Decimal range for n-bit binary number

Decimal Range of n-bit binary number
➢ How many n-bit binary numbers are possible ?
(n-1)th (n-2)th

2nd

.....
.....
1st
0
0
1
1

0th
0
1
0
1

2nd
0
0
0
0
1
1
1
1

1st
0
0
1
1
0
0
1
1

1st

0th

0th
0
1
0
1
0
1
0
1

➢ What is the smallest n-bit binary number ?

pos. (n-1)th (n-2)th
bit
wgt. 2n-1
2n-2

...
...
...

ith

2i

...
...
...

2nd

1st

0th

22

21

20

...
...
...

2nd

1st

0th

22

21

20

➢ What is the largest n-bit binary number ?

pos. (n-1)th (n-2)th
bit
wgt. 2n-1
2n-2

...
...
...

L3 - Number System Page 4

ith

2i

With n-bits, we can form 2n binary numbers in the decimal range [0, 2n-1]

.

L3 - Number System Page 5

Minimum Bits to represent Decimal Number

➢ What is the least number of bits required to represent a decimal number ?

3rd 2nd 1st 0th

( 1

2 ) 10

( 1

( 1

8 ) 10

( 1

1

0

0 )2

4th 3rd 2nd 1st 0th

0

0

1

0 )2

We know that, with n-bits, we can form 2n binary numbers in the decimal range [0, 2n-1]

.

L3 - Number System Page 6

L3 - Number System Page 7

Complementary Number System

Complementary Number System
It is used to perform subtraction using addition.

4th 3rd 2nd 1st 0th

( 1

2 ) 10

( 0

1

1

0

0 )2

4th 3rd 2nd 1st 0th

( 9 ) 10

( 0

1

0

0

1 )2

.

L3 - Number System Page 8

L3 - Number System Page 9

L3 - Number System Page 10

.

L3 - Number System Page 11

Binary Representation for Signed Integers

Binary Representation for Signed Integer

(n-1)th (n-2)th

.....
.....

2nd

1st

0th

4th 3rd 2nd 1st 0th

( 1

0

1

0

0 )2

3rd 2nd 1st 0th

( 0

1

1

0 )2

➢ Converting a signed integer from base-2 to base-10

4th 3rd 2nd 1st 0th

( 1

0

1

0

0 )2

3rd 2nd 1st 0th

( 0

1

1

0 )2

L3 - Number System Page 12

.

L3 - Number System Page 13

Decimal range for n-bit signed binary number

Decimal Range of n-bit Signed binary number
➢ How many n-bit signed binary numbers are possible ?
(n-1)th (n-2)th

2nd

.....
.....

1st

0th

➢ What is the smallest n-bit signed binary number given that sign bit is zero?

pos. (n-1)th (n-2)th
bit
0
wgt. -2n-1
2n-2

...
...
...

...
...
...

ith
2i

2nd

1st

0th

22

21

20

➢ What is the largest n-bit signed binary number given that sign bit is zero?

pos. (n-1)th (n-2)th
bit
0
wgt. -2n-1
2n-2

...
...
...

ith

...
...
...

2i

2nd

1st

0th

22

21

20

Assuming the sign bit is zero, with n-bits, we can form 2n-1 signed binary numbers
in the decimal range [ 0, 2n-1-1 ].

➢ What is the smallest n-bit signed binary number given that sign bit is one?

pos. (n-1)th (n-2)th
bit
1
wgt. -2n-1
2n-2

...
...
...

ith
2i

...
...
...

2nd

1st

0th

22

21

20

➢ What is the largest n-bit signed binary number given that sign bit is one?

pos. (n-1)th (n-2)th
bit
1
wgt. -2n-1
2n-2

...
...
...

ith
2i

...
...
...

2nd

1st

0th

22

21

20

Assuming the sign bit is one, with n-bits, we can form 2n-1 signed binary numbers
in the decimal range [ -2n-1, -1 ].

L3 - Number System Page 14

.

L3 - Number System Page 15

.

L3 - Number System Page 16

L3 - Number System Page 17

Hexa-Decimal Number System

Hexa-Decimal (Base-16) Number System
In hexa-decimal number system, we form numbers using 16 digits ranging from 0 to 9 & A to F.

➢ Converting a number from base-16 to base-2
5th 4th 3rd 2nd 1st 0th

( F

A

7

B

9

2 ) 16

➢ Converting a number from base-2 to base-16
5th 4th 3rd 2nd 1st 0th

( 1

1

1

0

1

1 )2

The hexa-decimal representation for a n bit binary number contains n / 4 digits.

L3 - Number System Page 18

L3 - Number System Page 19

