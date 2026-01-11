# Lecture 43 (EasyOCR)

**Source:** `L43 - Graphs.pdf`

---

## Page 1

Graphs DFS dfs bfs Reachability in Graphs Given a connected graph and a source vertex, design an algorithm to find all the vertices reachable from the source vertex A vertex "v" in the graph is said to be reachable from vertex "u" if there exists a path from vertex "u" to vertex "v"_ Sre Srt 1P {0,1,2,,4,} {9,1,2 24} 2 2 5,6,4,8 3 5 3 5 rort 8 8 Depth First Search DFS ) The key idea behind the DFS algorithm is that for any vertex "u" in the graph, when you visit one of its unvisited neighbors, say V then first you visit all the unvisited vertices reachable from before you visit the other unvisited neighbors of "u" D i 2 3 4 S6 +8 FRrARR t €rt & V +* 0 13 6 4 2 5 7 8 0 - [Q2 ) 17 [0, 3,4) 2 -  [ 9,4,52 3 - [ ', 6] 4 - [ 1,2, 6,97 5 5 1z) 7) 6 - [ 3, 4, 8 ) 1 5 [7,5,37 } - [ 6, 97 L43 Graphs Page

## Page 2

d}s - Lages 3" srni2 248p has 0 bckedje mp * 4 4 bor iL neans hs 4 mnra me tyee bujlx &j JPslYs *  %p 9 dfs 's Oot uniqve o0 Kou t Jyendy he Jeu L43 Graphs ~tre€ Gack ernt- (eph nt / Sonnind .dde 7qbu8t procees Pagc

## Page 3

Graphs BFS Breadth First Search The idea behind the BFS algorithm is that; for any vertex "u" in the graph, you've to first visit all of its   unvisited neighbors before you visit the neighbors of its neighbors _ BFS Implementation To implement the BFS algorithm, we will maintain Queue to keep track of nodes that have been visited but not yet explored: Set Map to keep track of nodes that have been visited: Stc queue TZTTTDI LlkL_ LX vs TxHHAFIH b}s-tree 2 & 4 $ ( 1 8 Bbocked&ea L43 Graphs key Puge

## Page 4

Graphs Traversal 1 "? 4 5 6 94 9 3 '4 IS " Graph Traversal 82 8 3<ttt t t 1t Y % t 12 2 3 13 14 5 10 15 LA3 Graphs % % t t Page 

## Page 5

Graphs Cycle Cycle Detection Given an undirected graph design an algorithm to check if contains a cycle. 0 0 2 17 2 False True Falso 3 L43 Graphs Page

## Page 6

[RJHHW] Graphs Bipartite Graph 2 - Qreblem Bipartite Graph Given an undirected graph design an algorithm to check if it is a Bipartite graph: A graph is said to be a Bipartite graph if the graph nodes can be partitioned into two independent sets A and B such that each edge in the graph connects a node in set A and a node in set B. 2 2 2 3 4 5 3 3 True True False 0(5 A 6 1 7 X L43 - Graphs Page 6 @loicj

## Page 7

[HW] Clone Graph Clone Graph Given reference of a node in a connected undirected graph, return a deep copy (clone) of the graph: Note that; each graph node contains a value int and a list List [ Node ] ) of its neighbors: class Node public int val; lic List<Node> neighbors; L43 Graphs Page pub

## Page 8

Graphs Back Edge Back Edge Detection Given an directed graph design an algorithm to check if contains a back-edge. A directed edge u is said to be a back-edge if there exists a directed path from vertex to vertex U_ c exp- '/ : tve 'p %J ' flse '&' Joise Lmh B/e: Nve Us6) Jk6) 5v,',, d%sl ) dxsko> Jtsof 9s61) L43 Graphs W Page

## Page 9

Y # DJslo ) L43 Graphs dkki Page

