# Lecture 46 (EasyOCR)

**Source:** `L46 -  Graphs.pdf`

---

## Page 1

Graphs Disjoint Set Uain-fice [HW] https [[codeforces com/edulcourse/2Ilesson/Z/1/practice_ [HW] https: cses fi/problemsetltask/1676 Disjoint Set A disjoint set is a data structure which maintains a collections of dynamic sets So, S1, S2 - } that are pairwise disjoint i.e. for any two sets Si and Sj in the given collection where i+j, 81718;- 0 The disjoint set data structure supports three main operations, these include createSet x) to create a new set with a single member X leaderlrepresentative of set unionSetkx yH to create a set S as a union of sets, Sx & Sy that contains x & y respectively. findSet (n) returns the leader or representative of the set that contains the element x createSet 1 ) createSet 2 createSet 3 ) E unionSet 2,3 ) 2, 3 findSet ( 3 ) 592 unionSet 1,4 ) 4 2,3 findSet ( 4 ) 3 1 unionSet 3,4 ) #aofe( ) 1,2,3,4 findSet ( 2 ) L) 2 {rd Set /3) badfe-(u > Disjoint Set Representation There are two main strategies used to represent the disjoint set data structure L46 Graphs ~ 73 Page

## Page 2

Linked List Representation Disjoint Forest Representation faster In the Disjoint Forest representation, we represent each set in the given set collection using a Rooted Tree data structure i.e. a tree in which each node points to its parent and each tree node corresponds to a member of the set: Moreover , the root node of the tree corresponding to a given set points to itself and is the leader or the representative of the set. S1 TL2 L: L4 L5 S6 6 , S1o 101 10 2 3 5 1 (S)int Fosrs + Operations with Forest Representation createSet x ) WN' findSet x) S1 2 | 3 | 4 | 5 hme C N% 1e #ad{etks ) 2 3 5 unionSet X,y ) S1 1 | 2 | 3 | 4 | 5 S6 13| 2- | unionse+C,&) 6 3 5 4-3 2 3 8 Rndses (5) _>1 $ ) 3 0~ (2)-6 L46 Graphs Page

## Page 3

473 2 3 8 Raaser (5) -31 8 > 3 5 Ad4e+(8)36 $56 Disjoint Set Implementation with Forest Representation To implement the disjoint set data structure with the forest representation, we will use a hash table to store a mapping blw nodes and their parents. S1 2 | 3 | 4 5 S6 6 9 vertex parent  2 3 _ 4 3 2 8 5 6 + 6 5 6 8 6 Fasecr) unio (s,8 ) Y Improving the efficiency of Disjoint Set operations 4) To reduce the depth of a tree we deploy two heuristics Union by ahx( orsiz3 See 2 7 '3 & The idea behind union by rank is, during the union operation, make the root of the tree with lower rank to root of the tree with higher rank T= 2 r= 2 3 8 2 5 or 2 3 8 5 8 2 3 5 Path Compression L46 Graphs Page 7 ^6 7t 7 ^4 Teoti ar point

## Page 4

The idea behind path compression is, during the find operation, make every node visited along the path to the root node, to the root: 2 3 2 3 5 6 6 didSec(+) When we combine union by rank and compression, on average the time complexity of the find operation and the union operation is constant ls9n %(a) ~ (5 { +  Applications of Disjoint Set iCV. Acke Mja In It can be used to detect a cycle in an undirected graph. 2 3 V = 1,2,3, E={{1,2}7 2,3 3, 4, M Covp =_ It can be used to count components in an undirected graph: 2 3 5 5,6 V={1,2, 3,4,5,6,7 } S$ E={{1,2} 1,4 }, 2,3 } {3,4} {5,6 5, {6, 7}} L46 Graphs point path VVV' 1 6 Vl, 5 Page

## Page 5

Graphs Minimum Spanning Tree In 4 hee wim ^'dos 3 au se 0-1 ape [HW] https IIcodeforces com/problemset/problem/1559[D1 1o0(T Minimum Spanning Tree MST ) bor 5 0 (7 Given a connected, undirected, weighted graph, design an algorithm to its find the minimum spanning tree. 4d(t 0 ) 2 2 Kruskai CJsu) 2 3 3 Rria (ainn /) 3 2 2 } 3 3 Kruskal's Algorithm The idea behind the Kruskal's algorithm to find the MST for the given connected, undirected; weighted graph that contains V vertices is to choose V-1 edges in the increasing order of their weights such that at no point of time inclusion of an edge in the sub-graph leads to a cycle. 5 - 6 : 1 2- 4 : 2 2 S-1 : 3 u _v '-2 : 4 1-3 : 5 2 -< : ? Implementation of Kruskal's Algorithm 2 L46 Graphs Ieve 25 (Y [rj ^>7 Page

## Page 6

5 [RJ[HW] Prim's Algorithm 2 3 5 Implementation of Prims Algorithm 2 5 Optimized Implementation of Prims Algorithm L46 Graphs Page

## Page 7

2 2 5 L46 Graphs Page

## Page 8

[HW] Minimize Malware Spread Minimize Malware Spread You are given a network of nodes represented as an adjacency matrix graph where the ith node is directly connected to the jth node if graph[ 1][ j ] F= 1 Some nodes initial are initially infected by malware. Whenever two nodes are directly connected, and at least one of those two nodes is infected by malware, both nodes will be infected by malware. This spread of malware will continue until no more nodes can be infected in this manner. Suppose M(initial) is the final number of nodes infected with malware in the entire network after the spread of malware stops. We will remove exactly one node from initial Return the node that; if removed, would minimize M(initial) If multiple nodes could be removed to minimize M(initial) return such a node with the smallest index Note that if a node was removed from the initial list of infected nodes, it might still be infected later due to the malware spread: 0 2 3 4 5 6 7 8 0 0 1 0 2 0 2 3 8 ; 6 U ; 1  0 5 7 0 0 5 8 |o | 0 | 0 /  L46 Graphs Page 8

## Page 9

0 2 3 4 5 0 0 ; W 2 3 5 5 0 2 3 4 5 0 0 3 WW 0 2 3 4 5 0 0 4 5 L46 Graphs Page 9

## Page 10

2 3 4 5 6 7 8 0 0 1 2 2 3 8 0 1 VH 8 0 4 ] 8 0 | 0 | 0 2 3 4 | 5 6 7 8 1 | 2 3 4 | 5 6 8 2 | 3 | 2 3 | 2 | 3 3 | 8 8 3 4 2 parentMap rankMap L46 Graphs Page 10

