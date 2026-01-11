# Lecture 45 (EasyOCR)

**Source:** `L45 - Graphs.pdf`

---

## Page 1

01 Matrix Quelidea^ Di'stunt e (; , %) (n;, 3 ) ~C Mjnhohuq Distual' 01 Matrix (85-775)++l4i-30)" Given a m x n binary matrix mat; for each cell find the distance to the nearest cell with the value 0 such that distance blw adjacent cells is 1. x522 Io -2 I+ 10-21 3 4 Ix;-xj | + Id; - &; | 3 3 4 5 2 9 3 5 3 2 Q9 3 4 3 2 3 i/R %/8 0 2 0 2 2 2 2 2 ; 2 2 2 0 2 1 0 YR 'p #oe tr &n/e 1Fs D (vt2e) w 2 #ndes #edhes ~ Olm ) Mxn -CJs e we'AX (m-)n + m(0-1) lo Coll $ mn-A + mnzm? mo' mo }otol Hme = ~Lmo 7 Mn olmta") L4S Graphs 1 0 (a1| mo mn wots+ mn Puge

## Page 2

4 >  )v Multi-Ste BCs TI1Y queue L4S Graphs Pugc

## Page 3

[HW] Rotten Oranges Rotten Oranges You are given an where each cell can have one of three values: representing an empty cell; representing a fresh orange, or representing a rotten orange_ Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten: Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 Example 1: Minute 0 Minute Minute 2 Minule Minute Input: grid [[2,1,1], [1,1,0] , [0,1,1]] Output: 2 2 2 3 4 2 2 1 2 1 1 ; 3 4 2 | 1 | 1 | 2 L4S Graphs grid 1 | Page

## Page 4

2 | 1 | 1 | 1 | 2 2 2 L4S Graphs 4 | Page

## Page 5

Graphs Dijkstra [HW] https IIcodeforces comlproblemsetlproblem/20/C [HW] https Ilcses filalonltaskli 195 [HW] https Illeetcode com/problemsInumber-of-ways-to-arrive-at-destinationl SSSP using Dijkstra's Algorithm Given a weighted graph and source vertex design an algorithm to find the length of the shortest path from the source vertex to all the other vertices_ Lm vertex distance 10 9 8kM 3 km skm Tensed Edge and Edge Relaxation du :' 8tv) > du +Wuv "5 b0o ? 2900 7 src Kve ~2 me dtv) dusww 2884 btw V 4'v ) 15 Dijkstra's Algorithm To solve the SSSP problem for weighted graphs using the Dijkstra's algorithm, iterate over all the vertices in the graph for which the shortest distance from the source has been computed, and relax all the tensed edges incident on them. vertex distance 10 Mcmby Dijkstra's Implementation 7 #trsre (',47 09 To implement the Dijkstra's algorithm, we will maintain two data structures L2,37 he-p To keep track of graph vertices that have been explored: (? We use a Set for this purpose_ A vertex is marked as explored if its shortest distance from source has been L6,7 computed and all the tensed edges incident on it have been relaxed: 67 L`1 Tr FY To keep track of graph vertices that have not been explored: Ia 9 hep d 1 Graphs PlEc > Ko1 =(Odkm Iis Horjjnq wnjn me^ 100 + T J( Drin ; 6ooKm (in Wuv s"J m Mumba; 2o00 Km K4 Knse & kntohve ) 4107 Mpo minnra So08 (ror" b0.U 22,37 will neab 2~_ 2'1 4 ? 26,17

## Page 6

A vertex is marked as explored if its shortest distance from source has been "/0' computed and all the tensed edges incident on it have been relaxed: 67 L`1 m" pi' To keep track of graph vertices that have not been explored. ln 9 heap 9 1 We will use a Min-Heap for this purpose_ 0 , Each item inside the Min-Heap will be a pair heaf tentative shortest distance of vertex from source 0 label of vertex 3 i5 6,s+0 3 (p' On I6r dlement i0 4,= do+ we ( 70 + =0 +10 (81d2+ Wilsz  Distmop de + Cdist,nole 2? 007 vertex distance explored unexplored (5 2) 10 edc (5 3 Set , min-Heap Woz ? Map Imp L8, 4 0w7d_+Wv,d,/do+ lunezp) d 8isr 86 +Woz (o 0 ) 4-dtw% 0 +5-< $ iSv nofe vertex distance explored unexplored 2 , 51, Set min-Heap (T Map drs Path Construction Q Pamn Tree Snoitesr ( Sr 1) Graphs PlEc 6 nlm 4 ) 17_ L'i L6,97 Qcisc ) (uitc) ~i0 bydltwys 5+32/ 656 Ls sh-  6750132 ored ) aod @ 0 + $ ?v 0 75+23/ (9,3) Aede d1 * drr ~S+127 lcrs C925 neoe 440

## Page 7

Correctness of Dijkstra's Algorithm m { #+ap du < dl Desume i j> mp nic Pefv 4,42 J& m;s Qajy 4 %4 So3 {S 8 65 25 Iong hvs 0 $ J48 _ waks ` Dijkstra's algorithm doesntt work for graphs with a negative weight edge: Is Dijkstra' algorithm exhaustive ? Lreedy For a weighted graph, the SSSP problem isn't defined if the graph contains a negative weight cycle: Src dsr 0 [RJIHW] Implementation of Dijkstra's algorithm using priority_queues> vertex distance explored unexplored 10 Set min-Heap Map Graphs PlEc t4kF wheo (45' out di+ t0 96 d4 fino 1j2e wjiks 0 ,jKsT9 trwph 9 WT Avn-nathya

## Page 8

Graphs PlEc *

## Page 9

[RJIHW] Graphs Bellman Ford [HW] https IIleetcode com/problemslcheapest-flights-within-k-stopsl SSSP using Bellman-Ford Algorithm The Bellman-Ford algorithm can solve the SSSP in case the graph contains negative weight edges. Also it can be used to detect a negative weight cycle in a graph: 2 2 3 3 2 For a weighted graph, containing V vertices, the minimum no. of edges along the shortest path from the source to a destination vertex is 0 & the maximum number of edges along the shortest path is equal to V - 1. If however, the number of edges along the shortest path between the source vertex and destination vertex exceeds V _ 1 then we can say the shortest path between the source and destination vertex contains a negative weight cycle. Bellman-Ford Algorithm The idea behind the Bellman-Ford algorithm for solving the SSSP problem for weighted graph that contains V vertices is to relax all the its edges V - 1 times. 3 41 | 2 | 3 | 4 2 0 2 5 3 0o 0 L45 Graphs Page

## Page 10

How to detect a negative weight cycle using Bellman-Ford ? To detect a negative weight cycle, we relax all the edges of the graph once more. If the distances of 7=1 vertex from the source vertex improve, then we can conclude that the graph contains a negative weight cycle 2 1 | 2 | 3 0 0 2 0 Can we use Bellman-Ford algorithm for undirected graph ? Is Bellman-Ford algorithm exhaustive ? 1 | 2 | 3 2 0 0 2 0 5 3 0 2 4 0 L45 Graphs Page

## Page 11

[RJIHW] Graphs Floyd Warshall's Algorithm [HW] https IIcodeforces com/problemsetlproblem/295/B AIl Pairs Shortest Path using Floyd Warshall's Algorithm Given a weighted graph, find the shortest between all pairs of vertices. 8 2 2 3 4 0 | 6 |^ 4 5 2 2 6 | 0 T 5 T 2 3 1 L5 | 0 3 4 4 | 2 | 3 0 3 3 L4S Graphs Page 11 path

## Page 12

L4S Graphs Page 12

## Page 13

The Floyd-Warshalls algorithm can detect a negative weight cycle in a graph. 8 2 55 2 3 4 3 L4S Graphs Page 13

