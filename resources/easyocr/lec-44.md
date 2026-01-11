# Lecture 44 (EasyOCR)

**Source:** `L44 - Graphs.pdf`

---

## Page 1

Max Area of Island Max Area of Island Given two-dimensional grid that contains 0's and where represents water and represents We define an island as group of 1's (representing land) connected four-directionally horizontal & vertical Design an algorithm t0 find the area of the largest island area of an island is the number of 1's contains Example Input Output : 8 5' +n2 Jinding 11m4 s;2€ me fn;n9 mjz$ sfor 2 8 me (arr"t 'pt: X &, Mxn A X = (+0 7: Jx? { 0,0 dx = {0,0 J- = {1 3 k4 3 S 8 + dx[kl; +,) V 5 ) Jps(ox,F 99 =)to +0 = i +1 9)+1 DIpb FAE | otpa MjX Wmpinpnt 6,8S 0y =Vt-13)1 99- { !, Ai-V nx = |+ -( ^J=T 0 Rak<ysbtt) foc( Ax=l+ / -i+) 7 ^X = +93 [RJ; oy = 0j ,)

## Page 2

[HW] Making a Largest Island [editorial] htts Illeetcode com/problemsImaking-a-large-islandleditoriall Making a Largest Island Given a two-dimensional grid that contains 0's and 1's where 0 represents water and represents land. We define an island as a group of 1's (representing land) connected four-directionally horizontal & vertical ): Design an algorithm to find the area of the largest island area of an island is the number of 1's it contains such that you can change at-most one of the 0's into a 1 Example Input Output 11 0 0 | 1 0 1 L 0 | 0 | 0 1 | 0 | 1 1 0 | 1 | 1 / 0 | 1 | 1 | 0 L44 Graphs Page 2

## Page 3

Graphs Topological Sorting Topological Sorting ofa DAG Topological Sorting of a directed acyclic graph or DAG is a linear ordering of its vertices such that for each directed edge from vertex to vertex v in the graph, comes before v in the linear ordering_ 4 _ UF -Je c 0 - 0 4 [ 3, 4 ) 17 %1 0- L ) 2-) % 2 - %P 59 [5,6,*" 3 ? BCo  Y+61 4  0 8 | ? 4 6 + 5 [2] S7 0 7 {+ 0 1 + [ $] +7 0 BFS Implementation Kahn's Algorithm To perform topological sorting of a DAG using the BFS algorithm, we will maintain Queue to track nodes whose dependencies have been resolved i.e. in-degree is 0 HashMap to store mapping blw vertices and their in-degrees_ vericr ~degree Pprsz 0 1 3 4 6 & 5 2 Na-tvral Aeh M a + [HW] DFS Implementation 5 Ao Ljng 0 X 2 Mais Ry Xon Pc M Cycle Detection using Topological Sorting Llm Qvili Lpt ~ 4 [ o ] tinnrF'4: > 4,3) "2,42 xJ2 [ (J (+7 + Kc Lanf 4oj

## Page 4

Io ms m L & L Llm tinnr F'4: = ntude UctuP T

## Page 5

[HW] Graphs Course Schedule II Course_Schedule IL There are a total of numCourses courses you have to labeled from to numCourses You are given an array 'prerequisites where prerequisites[ 1] [ai, bi] indicates that you must take course b    first if you want to take course 0;7ai For example; the [0 , 1] indicates that to take course have to first take course Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array: Example 0 , ', 2 , 3 numCourses prerequisties 2 0 3 1 3 2 3 numCourses 5 S,31 prerequisties 0 2 | 0 3 | 1 3 2 L44 Graphs Page take, pair you

## Page 6

[HW] Alien Dictionary Alien Dictionary 0 6 € 4 e $... 2 There is a new alien language that uses the English alphabet: However; the order among the letters is unknown t0 you: You are given a list of strings words from the alien language's dictionary; where the strings in words are sorted lexicographically by the rules of this new language. Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language"$ rules: If there is no solution, return If there are multiple solutions, return any of them aen 69 Example 1: 0o9 " < DwAY Input: woros ["wrt" Wri "ej ett" cftt"] 0 Output: wertf" wr $ w} 5 & < $ 0} 3 5 Wc € 032 wr} et 3 (  t : 9 L ex ett 7}tt 6I evkk L44 (iraphs Tvied ~ftt wrt detendenyy ms 73 Ix _t e-AY =) @< T Pagc

## Page 7

Graphs SSSP Single Source Shortest Path (SSSP) Given a connected graph and source vertex design an algorithm to find the length of the shortest path from the source vertex to all the other vertices vertex distance 2 3 2 4 2 J 6 2 8 3 8 Svc = 0 Js+ : SSSP using BFS Algorithm 0 D vertex distance 2 2 8 3 1 3 4 5 6 8 7 4 6 W PuHdzy 1 BFS Implementation for SSSP Stc vertex distance 2 3 3 6 9 8 4 St queue Fihd L44 Graphs Src 9193+6+8 Src Iuap| 1 l 713 8 Page

## Page 8

[RJ[HW] Snake and Ladder Snakes and Ladders Game Given a Snakes & Ladders board of size N that contains multiple snakes and ladders. You are also given their starting and ending positions. Design an algorithm to find the minimum no. of throws of a six-sided die required to reach the Nth cell of the board from its 1st cell such that as per game rules If you are bitten by a snake by reaching at a cell having a snake head you will go down to the cell at which the tail of the snake ends_ If you reach a cell at which a ladder starts, you will climb the ladder. Example Input N = 36 ladderPos = [(2,15), (5,7), (9,.27), (18,29), (25,35) ] snakePos [(17,4), (20, 6) , (24, 16) , (32, 30) , (34, 12) ] Output 35 34 33 31 32 d= 3 25 127 29 30 0 ~6 29 26 28 24 21 20 d-' ( 231 22 13 10 Stc dz2 M= |5 36 35 34 33 31 36 35 34 33 32 31 32 25 27 [29 30 28 25 26 27 28 29 30 26 24 21 20 19 24 23 22 21 20 19 23 22 13 16 13 5 18 18] 10 12 10 M=iS Uz1s+3 =/1 7 del,,67 L44 Giraphs Page ~)vel+747 ask Sre v"M+l

## Page 9

L44 Giraphs Fapc

## Page 10

[RJIHW] AII Nodes Distance K in Binary Tree All Nodes Distance Kin Binary Tree Given the root of a binary tree, a target node and an integer K, return an array of values of all the nodes at distance K from the target node. toot 3 target = 5 3 32 K=2 2 5 5 'e [ # 4,'] 38 8 4 31 5 queue 8 L44 Graphs Jve Eore 2 Page

