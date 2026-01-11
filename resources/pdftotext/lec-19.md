# Lecture 19

**Source:** `L19 - DMA and Algo Analysis.pdf`

---

Intro to DMA

Introduction to Dynamic Memory Allocation
• We can visualize the system memory ( RAM ) as a sequence of memory cells
such that each memory cell is of 1B ( 8 bits ) and is addressable.

0 1
n-1

n-2
.....

• When we run a C++ program, a portion of system memory is allocated for
program execution which is known as application memory.

0 1
n-1

n-2
...

...

• The application memory is divided into four segments
○ Code or Text : to store program instructions
○ Global/Static : to store global and static variables
○ Stack : to store local variables
○ Heap or Dynamic

Stack Segment
○ The memory allocated for stack segment of application memory is fixed.
○ The size of the stack frame for a function must be known at compile time.
○ The process of allocation and deallocation of memory is handled by OS*.

Stack

Heap or Dynamic Memory
○ The memory allocated for the heap segment is dynamic in nature.
○ The programmer handles the process memory allocation and deallocation.

L19 - DMA and Algo Analysis Page 1

Heap or Dynamic Memory
○ The memory allocated for the heap segment is dynamic in nature.
○ The programmer handles the process memory allocation and deallocation.

Stack

Heap

Stack

Heap

Memory Leak

Stack

Heap

1D arrays on the Stack or Static Memory
An array is a linear data structure, referred by a single name, which is used to store a
sequence of values of the same type.

In C++, we can think of name of an array as a pointer to the element at the 0th index.

L19 - DMA and Algo Analysis Page 2

arr

index

0

value

10 20 30 40 50

1

2

3

4

address 100 104 108 112 116

1D arrays on the Heap or Dynamic Memory

Stack

Heap

By default, when we declare an array on the heap memory, it contains garbage value.

During the initialization of an array created on the heap memory, specifying the size of the
array is optional. Also, the size of the initializer list should not exceed the array size.

To access elements of a 1D array created on heap or dynamic memory, we can use the
same syntax that is used to access elements of a 1D array created on the stack memory.

Dynamic Array
It an array created on the heap memory that can grow at runtime.
L19 - DMA and Algo Analysis Page 3

Dynamic Array
It an array created on the heap memory that can grow at runtime.

L19 - DMA and Algo Analysis Page 4

2D arrays on the Stack or Static Memory
A 2D-array is an array of 1D arrays, referred by a single name, which is used to
store a sequence of values of the same type and can be visualized as a matrix.

0

0

arr

1

1
2

0

arr

0

1

2

3

10 15 20 25
30 35 40 45
50 55 60 65

1
2

3

0

1

2
2

3

0

1

2

3

10 15 20 25

30 35 40 45

50 55 60 65

100 104 108 112

116 120 124 128

132 136 140 144

arr[0]

arr[1]

arr[2]

L19 - DMA and Algo Analysis Page 5

2D arrays on the Heap or Dynamic Memory
A 2D-array is an array of 1D arrays.

.

.

.

L19 - DMA and Algo Analysis Page 6

Algorithm Analysis

Algorithm Analysis
The analysis of an algorithm is done in terms of the time it takes ( time complexity )
and the space it consumes (space complexity) to perform its operation.

The analysis of an algorithm is always done in terms of the input size. Moreover, we
mostly interest in the worst-case analysis and use the Big-O notation to report the
worst-case time and space complexity of an algorithm.

To analyze the time complexity of an algorithm, we've to first identify algorithm type

L19 - DMA and Algo Analysis Page 7

○ Iterative ( contains only loops )
○ recursive ( contains recursive calls )
○ neither iterative nor recursive - mostly take constant time i.e. O(1)
To analyze the space complexity of an algorithm, you've to analyze how much extra
space or auxiliary space the algorithm consumes with respect to the size of the input.

L19 - DMA and Algo Analysis Page 8

Time Complexity Analysis of Iterative Algorithms

Time Complexity Analysis of Iterative Algorithms

L19 - DMA and Algo Analysis Page 9

L19 - DMA and Algo Analysis Page 10

L19 - DMA and Algo Analysis Page 11

L19 - DMA and Algo Analysis Page 12

L19 - DMA and Algo Analysis Page 13

Space Complexity Analysis of Iterative Algorithms

Space Complexity Analysis of Iterative Algorithms

L19 - DMA and Algo Analysis Page 14

L19 - DMA and Algo Analysis Page 15

