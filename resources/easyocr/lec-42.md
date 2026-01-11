# Lecture 42 (EasyOCR)

**Source:** `L42 - Graphs.pdf`

---

## Page 1

Graphs Introduction Graphs It is a non-linear data-structure that can be thought of as a collections of nodes 9 (or vertices) and edges_ 1 lmpm"t Ivl-I-57 Ce + 0-'7 Iela- node V= { 0, 1, 2, 3,4 } E={ M Ivl . + 2- lmponeat M: lel + V={0, 1,2, 3,4, 5, 6 } E={{0, 2} 0 {5, 6} } BF Wmc" Wmp Topl Formally, a graph is a pair of sets V and E where V is a non-empty set of Iv| vertices and is a set of edges such that each edge is a pair of vertices_ 1c1 2 V={ 0,1,2,3,4 } {0, 1}, { { {3 , 1 } In a directed graph, each edge is an ordered pair of vertices. V={0, 1,2, 3,4 } ={(0, 2), (1, 0), 51, 3), L42 Graphs Imr m-6 dreph 2- Pupe

## Page 2

E={(0,2), 0 (4,3) } In a weighted graph, each edge is assigned a weight Ws + Di Qein 15 V={0,1,2,3,4 } 10 47 Va d;t E={(,2, 0, 7), : 3,20,; 6 20 2,99 (4, 3, 5) } Applications of Graphs Manktoo) 1. Social Networking Sites Arshst +0vj?8 Users can be thought as nodes in a graph Relationships can be thought as edges between graph nodes Keja 9 2_ Maps of a city Checkpoints can be thought as nodes in a graph Roads can be thought as edges between graph nodes_ Wiksha Szsm; Varonsi 3k Cadaom Dein; 2k Ltr 4R Joi Luckaow) Auedhy Anmedbad Amtilset mis } 2 ~1s 8 L42 Grapls U^ Wat Mjcta;" Dongbse 15), 3 ~1> Pupe

## Page 3

Graphs Terminology Ioo( e,lle2 07 EO Graph Terminology 8= $ In an undirected graph, if there exists an edge between two vertices then they } < ~66(2) = 986() = {9,2 } are said to be adjacent to each other: d2 d:3^06(2) = { 9 3,4} 1l i2) ~96lo)-/1,0 d-2 30 hv S1,3} 4-2 d=2 433 oahi sabo / d-3 ~06(1 ) ={ } ~466)-4{52} {',1,} ~86(37-8,3 iza In an undirected graph, we define degree of a vertex as the number of vertices Wgke fov adjacent to it: 0" "vh6 In a directed graph; if there exists an directed edge u then we say that vertex uiS predecessor of vertex or vertex is successor of vertex u: d;a P7(1y { 9,3} Pr(o) =5'} Sv(L) = $4} su(6) = { 23 0;0+4 S2} Kor=| din = 0 8et-l SuC4 27$2} 04 () {0,348 : su (3) = _ 9 54 For directed graphs_ we define in-degree #atvertex as the no. of predecessors it has and out-degree of a vertex as the no. of its successors In an undirected graph; two or more edges are said to be parallel edges if - are incident on the same two vertices_ Ilez In a directed graph_ two or more edges are said to be parallel edges if have the e,'XX ez' same tail vertex and the same head vertex loep e |l e In graph theory; we define a loop as an that connects a vertex to itself. A graph that doesn't have parallel edges loops is also known as asimple graph: omt misc nvlt-Jvaph Minimum and Maximum Number of Edges in Graph The minimum no of edges in a graph is zero, such graph is known as empty graph_ Ielmz For maximum no. of edges in a graph; each vertex of the graph must be connected with every other graph vertex: Iv-| Ivl (n-t (o-') Graph Representation There are two key strategies that can be used to represent the graph data structure Adjacency List Adjacency Matrix At a high-level; in each of these strategies we internally implement the graphs using arrays which is indexed by the graph vertices. Girch Fje $ n06(y) = ^j6c 6) Smele 0ut= Jio? Pr(w ) P(3) Fo):_ they they edge and Ivt- MCz " ^lv

## Page 4

Graphs Adjacency List Adjacency List To represent a graph that contains | V | vertices and edges using adjacency list; you've to create an array of size V | such that at each index of the array you store a list of neighbors that correspond to the vertex which has been mapped to that index: Ivl:5 Iei-6 Viun Ledi cl In* (ml u;un LeBM Iylzl 2 3 J/ 44; vector ( Vecto 6,4+77 1s 40 Meke Xute LsetCin+)) J4 0 vruov alwojs Space Complexity Assume you are given an undirected graph that contains V vertices and E edges_ 0 hondehcfi~ lmmu total Spac lvi-I 2E 2 Jea? Iv | Iz| 1- S  pace Por 011 2 1+ 2m ~0 Tv/+ %// Assume you are given an directed graph that contains V vertices and E edges_ Iv)-+ lul+le) (m = 'Za Jovt & =(| (20 L41_ Uraphs Farc + 21 ~a6l"+ wja+ 48 2 Sorted 962' SFJ J*9;

## Page 5

Graphs Adjacency List II Graph Operations Assume you are given an graph that contains vertices and E | edges List all the neighbors of a vertex"u' 6 (deafu) ) Km e Add an edge between vertex "and ver Lse+) Lvr7 Is ent ( 0 ) ') lc8t 6( lor ( 43(42) Check if an edge exists between vertex 'u' and vertex 4 0n4 hme 0 (in(dgt"} 46) 9 9 + natus+ 1 vedw Cveco7 A%tv))) Seeru fo, U ot 6CW (~n(at"} $ cectn jot 4 =) hne X ~jbusr % lse7 (0 smjips Bekt opwon Delete an edge between vertex 'u' and @^ 6 < 6(mz ( &sa(u ) +6 deg ( + ) +cc 0 (Aea(u)' 4 Vrc(4/l7: ba  (dy (v)) 8e: V hmc 6 ( lea (4ed(w) u (s87 : 1 0 ac hco 9e h ngbuSt 28 de2. U Gitach: File v t adj(4): Pb ( 0 'dCu): dv + anQ veuor s24t1h NS bws+ cwm' Le 0 de3(2) 04 V & r960 sF &5 +

## Page 6

Graphs Adjacency List III Adjacency List To represent a graph that contains | V | vertices and E edges using adjacency list;, you've to create an array of size IV such that at each index f the array you store a list of neighbors that correspond to the vertex which has been mapped to that index 0 2 3 2 2 3 2 3 3 2 3 Drawbacks Our current implementation fails when labels assigned to vertices are integer values that exceed V  -1 non-integer values A veuovclhor 7 8 se & cort (raeie? Ia 5 [ B,c] chor 6 3 CA,o ] 0- E267 C 6,0,61 6 5 [t,> 7 L42 Graphs (nbde ) map < Page

## Page 7

Weighted Graphs A A B C DI node B, 2 5 2 Va lue (chcy ) (vectov LQiv ddr,ic+2 A _[ (6,a), (C,')- J 6 -[ (a,+), (0,2) .. L42 Graphs n8esh Kcy Page

## Page 8

Graphs Adjacency Matrix Adjacency Matrix To represent a undirected graph that contains V vertices and E edges using adjacency matrix, you've to create a 2D-Array of size | V | X IV | such that you assign the value one to the cells at the (i, j)th index and (j, i)th index of the matrix if there exists an edge between the vertices of the graph labelled as and j resp: lu) =S 2 0 2 3 3 Graph Operations Assume you are given an graph that contains V vertices and E | edges: Add an edge between vertex u' and 'v" lngt ma+[u)[v ) ~ | Check if an edge exists between vertex 'u' and vertex 'v' boxt MjtC4)lvJ ~=)? Delete an edge between vertex 'u' and 'v' 0 w~+ Ma+m)lv] = List all the neighbors of a verex 6 ( v ) Adjacency List vs Adjacency Matrix Ia1 ~ Iv) Ie| ~Iv) L42 Graphs Page &

## Page 9

Adjacency List vs Adjacency Matrix Ic1 ~ Iv) Ie) ~Iv) Spa tse decs ( If the graph is sparse i.e: it has less number of edges then one should represent it using adjacency list: In contrast; if the graph is dense i.e. it has high number of edges then one snould represent it using adjacency matrix. We know that; for a graph that contains V number of vertices and E| edges the space required to represent it using adjacency list is 0( | V | + |E | ) and the space required to represent it using adjacency matrix is 0 ( | V |2 ): Spatse Ieh~Iv/ cd Vst J 0d)" u +x} Vt 2 V ~ 0 (v ) Jent e [4~IZ J1) ~F U+2z V+ ZvY L42 Graphs Page mj+ " 0jj"st V &

## Page 10

Graphs Terminology II Graph Terminology Walk A walk in a graph is a sequence of vertices such that any two vertices adjacent in the vertex sequence are also adjacent in the graph: 4f Dec _,e Net 2 Wjik Wiiic 4 ( DBA Lujik Cosedv Moreover; we say that a walk is closed is it starts and ends at the same graph vertex: Path in a graph is a walk in which we visit each vertex of the graph at most once_ Acde W alK A Cdbac Qsm Lvik Pamn x Cycle A cycle in a graph is a closed walk in which we traverse each graph edge at most once A cedcepc Loarv Uvs'd Cydex A graph without any cycle is also known as an acyclic graph. Connected-Graph A graph is connected if there exists a between each pair of graph vertices. A graph is which is not connected is also known as a disconnected graph: Graphs Page AeD path AC06e WoIK Uused Uque path Wnn+Lpd

## Page 11

Kosataja Alge. S6c Strongly-Connected Graph A directed graph is strongly-connected if there exists a directed between each pair of vertices in the graph: Nor C-C W € A directed graph is weakly-connected if there exists a undirected path between each pair of vertices in the graph: G" 4 & Sub-Graph A v"4V sub-graph of a graph G = {V, E} is a graph G' = {V', E'} such that V' and E' are 6 6"4 & subsets of V and E respectively: V-Se,,see} C v= {9,4,0} Ab, 6' { ALco} = € 825 Cz L' 4 6 CD _ D & 5 G0 proper sub-graph of a graph is a sub-graph which is the graph itself. Component component of a graph is a sub-graph which is maximally connected: 4 A graph that has multiple components is a disconnected graph = (~ 2 - Wonedsx DAG: Jieded luh ^6de 6?s aydre 3: 2 3 - 6 ( 20~  nhh Rxcrt &r Dio (p7 = Graphs Page path S'€ Sv Ac , 214 Icee aCylsc {repl Qarea + era4]

## Page 12

^6de h?5 ayw€ ] 5 6 ( Qarea + 20~ + nhich Rxct Br '5 Llo (v= Spanning Tree spanning tree of a connected graph is a sub-graph which is a tree and contains all the vertices of the graph: SS Tse TG/ )ulv Zoo 20 (Y S0 3 3*4 Ch eudr 4 St '9 0 Graphs Page f $< lah {rsrl eya4J 2n4 254 F

