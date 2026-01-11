# Lecture 40 (EasyOCR)

**Source:** `L40 - Dynamic Programming.pdf`

---

## Page 1

Minimum Sum Path Minimum Sum Path Given a (m x n) grid containing non-negative integers, design a recursive algorithm to compute the sum of numbers along the minimum sum path to reach the (m-1, n-1)th cell from the (0,0)th cell such that at each step you can either move in down or right direction. Example 3 3 Input 1 grid 2 1 Output 4 3 2 - 1 Explanation The path 1 _ 3 _ 1_1 3 minimizes the Sum minlx,)) tIrdo faw mi Sum pm @n fin uhSum Pam twm_ 2 } tend + (M-1,~i)? (0,,) X (m-',^-17 (0,') Ix (Ya+ grid Sn MtSum W LV,o) m xn d"end JCic ) Hj #nd me mI Svm Mtn ton (,j)m cy + m (-1  (@u '+ba nxn m^ + 7J:j L40- Dynatie Programming tm Pum m-1 (M-1,^v)? ,4-1) Riat' Pi',3 Puge

## Page 2

;ait ~9 foo E Kx,j + dndaj' i+63 ^-1 M fx-,^-' fnd/j Mxo Recursive Case Let f (, j) be a function which computes the sum of numbers along the minimum sum path to go from the (i, j)th cell to the (m-1, n-IJth cell then, f (i, j) = grid[IJI] + min [ f (i, j+1) , f'+1,0) ] Base Case What is the reason behind exponential time complexity ? fo 0 m +0 f1, 0 h9 & fo,2 wng = 2 ~ 2 fo, 3 f1,2 f2, f3, fo, n-2 fm-2, fo,n-1 fm-1,0 425 Yo-), 2 P ko-1,' L40- Dynatie Programming 20 7rd _ ~, Ria*' 2 2 M+n ~+C Puge

## Page 3

Mija| m-i Top-Down Dynamic Programming fo, 0 44: 4 M-i fo, f1, 5 4j 201 fo, 2 f1, f2, M= fo,3 f1,2 f2, f3, 0 fo, n-2 fm-2, fo,n-1 fm-1,0 {cit : 2; dptar , mxn ~ where_ f(i, j) is a function which computes the sum of numbers along the minimum sum path to go from the (i, j)th to the (m-1, n-I)th cell. Bottom-Up Dynamic Programming ~8 = &j JRc Jc 7 m xn L40- Dynatie Programming ~2 "- 10-) Puge

## Page 4

where, fli, j) is a function which computes the sum of numbers along the minimum sum path to go from the (i, j)th to the (m-1, n-I)th cell: From recurrence, grid[i]li] + f (i, j+1) m-1 and j!=n-1 grid[ij0] + f (i+1,j) m-1 and j n-1 f (, j) grid[i]Ii] min [ f (i, j+1), f (i+1,j) ] m-1 and Isn-1 grid[i]C m-1 and Therefore, grrapjf} apWFEA m-1 and n- grid[ijuj dp[i+1]D] I=m-1 and n- grid[i]C min dp[i]li- 0,up[i+1JL] ) Fm-1 and j != n-1 dp[i]D] grid[iju] : m-1 and j + ~j+1 i+1 M-i m- m X n [RJ[HW] Building the Min-Sum Path from dp[II] 3 6 3 5 8 7 2 2 7 3 grid[II] dp[IQ] L40- Dynatie Programming n-1 sv9 Puge

## Page 5

Space Optimized Bottom-Up Dynamic Programming I+1 sPalt: an WT J^ ~o(n ) nxp Lvt ^XE HF U _ mxn dr] m-1 L40- Dynatie Programming $8;+J J0;,j" Puge

## Page 6

[HW] Dungeon Game Dungeon Game The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon The dungeon  consists of rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess The knight has an initial health represented by a positive integer: If at any his health point drops to or below; he dies immediately: -2 -3 3 Some of the rooms are guarded by demons (represented by negative integers) , so the knight loses health upon entering these rooms; other rooms are either empty -5 -10 (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers). To reach the princess as quickly as possible; the knight decides to move only rightward 10 30 -5 or downward in each step. Return the knight's minimum initial health so that he can rescue the princess. Note that any room can contain threats or power-UpS, even the first room the knight enters and the bottom-right room where the princess is imprisoned_ n-~ dungeon F m-1 mxn Recursive Case L4O Dynamic Programming point point Page '

## Page 7

Let f (i, j) be a function which computes the minimum initial health the knight needs starting from the (i, j)th cell to rescue the princess from the (m-1, n-T)th cell then, min(x, y) grid[i]Li] 0 min(x; y) - grid[i]Ii] grid[i]I] < 0 f (i, j) = min(x, y) ' grid[i]D] grid[i]D] > 0 && grid[i]I] < min(x; y) grid[i]Ii] > 0 && grid[i]l] >= min(x, y) Base Case What is the reason behind exponential time complexity ? fo, 0 f1,0 fo; f2,0 f1, f1, fo, 2 f3, f2, f1,2 fo, 3 m-1, 0 fo,n-1 fm; 0 fo, n Top-Down Dynamic Programming fo, 0 L4O Dynamic Programming Page

## Page 8

f1,0 fo,1 f2, f1, f1, fo, f3, f2, f1,2 fo, 3 fm-1,0 fo,n-1 fm; 0 fo, (m+1) x (n+1) where, fli, j) is a function which computes the minimum initial health the knight requires starting from the (i, j)th cell to rescue the princess Bottom-Up Dynamic Programming L4O Dynamic Programming Page

## Page 9

(m+1) x (n+1) where , f(i, j) is a function which computes the minimum initial health the knight requires starting from the (, j)th cell to rescue the princess From recurrence, min(x, y) grid[i]D] == 0 min(x,; Y) - grid[i]D] grid[i]I] < 0 f (i, j) = min(x, Y) - grid[i]D] grid[iJ] > 0 && grid[i]I] < min(x; y) grid[i]Ii] > 0 && grid[i]I] >= min(x; y) j-1 j (m+1) x (n+1) L4O Dynamic Programming Page

## Page 10

(m+1) x (n+1) L4O Dynamic Programming 10 Page

## Page 11

Wine Problem Wines Problem Given N bottles of wine along with their prices {Po; P1= PN-1 } Design a recursive algorithm to compute the maximum profit one can make by selling all the bottles of wine such that each year one can sell a single bottle of wine which is chosen from the extreme ends. Moreover, in the yth year the price of the ith bottle of wine increases from pi to y*pi: Example Tz+ 27 + I-5 Input N=5 2+ 5 1.2 - 2 prices 5 Jaar 1. 3 = 6 L 5 5J Output : 50 214 Jea T 3. 4 = L2 45 3*4 Jro7 4'1 = 4 4h Jr6r 5.$ 7 25 51 Jray 9 #r 1j * pra*+ kom m #ijy $ + wX ] i^ me jm Jeey "ait 7= 0 1 J - =^ X 3e J = 1 Je~ae for Jm Yre7 Swu 0te boltle when j=2) bo#1 < seR @ sid' € Itf+ 7&; + Mjx 98: P* ^ Recursive Case Let f (i,j,y) be a function which computes, the maximum profit one can make by selling (j-i+1) bottles of wines[i _j] starting from the yth year then, f (i, j,y) = max Pi*y + f (i+1,j, y+1), pj *y + f (i, j-1, y+1) Base Case *n DT tto 5 What is the reason behind exponential time complexity ? fo,N-1,1 f1,N-1,2 fo,N-2,2 f2,N-1,3 f1,N-2,3 T1,N-2,3 fo, N-3,3 f3,N-1,4 f2,N-2,4 f1,N-3,4 fo,N-4,4 fn-1,N-I,N fo, 0,N Dynunur [TVLI_rning MsC only 2 + cte "5] ~inps ( /.. Xol" J = 1- 7'' boik wim {;;')" kip"' 85) 9*  8 J-zn

## Page 12

Top-Down Dynamic Programming #0-/ 30 041 fo,N-1,1 '0 4 ) ~o-1 ~ f1,N-1,2 fo,N-2,2 (44&0 f2,N-1,3 f1, N-2,3 f1,N-2,3 fo,N-3,3 f3,N-1,4 f2,N-2,4 f1,N-3,4 fo,N-4,4 N-I,N fo, 0,N Jy?#jy NxNx (N+1) where, f (i,j,y) is a fn. which finds the max profit one can make by selling (j-i+1) bottles of wines[i  _j] starting from the yth year: State or Parameter Optimization (ytea+ JeGt d* # bottles lejt # botts Sold 0 - (j-;+') @ss ed t / 9- Cj-it) Lvrren+ Ytx 6<1 =n- / 30 3o 0 2 J =o-/ 1x0 Jw-&j Dynunur [TVLI_rning MsC fN-1, J -; +1 jecrs Ytr (4) = 1-) +i A-J + i

## Page 13

Jy-Yij NxN where, f (i,j) is a fn. which finds the max: profit one can make by selling (j - i+1) bottles of wines[i  . j] starting from the yth year such that y=n-j+i Bottom Up Dynamic Programming Js-}1 NxN where, f (i, j) is a fn. which finds the max: profit one can make by selling (j - i +1) bottles of wines[i.. j] starting from the yth year such that y =n-j+i From recurrence, max pi *y + f (i+1,j), Pity + f (i,j-1) } ;i < j f (, pi *y Therefore, max pi *y + dp[i+1Jlil; Pi*y + dp[i]li-1] } ;i < j dp[i]D] pi *y {ol 3$ Oase (as6 n.P; or o+R; nz NxN Dynunur [TVLI_rning MsC JRcwc? d=n-jti Jk24 Xz > 17)

## Page 14

[RJ[HW] 0/1 Knapsack Problem 0l1 Knapsack Problem Given a set of N items along with their prices po, p1, pN-1 } and weights Wo; WN-1 } & a knapsack that has a maximum weight capacity of W. Design an algorithm to find the maximum profit you can make by selecting a subset of items & placing them in the knapsack such that the sum of weights of the selected items does not exceed the knapsack's capacity. Example Input N =5,W =4 1 | 2 | 3 4 prices 8 4 | 1 | 5 3 weights 2 | 3 | 2 2 Output 13 i-1 i+1 L4O Dynamic Programming Page 14 W1,

## Page 15

Recursive Case Let fli, w) be a function that finds the maximum profit you can make by selecting a subset of items [ i N-1 ] and placing them in the knapsack such that the current knapsack capacity is w then, f (i, w) = cmax { pi + f (i+1, W-Wi), f (i+1, w) } Wi <= W f (i+1, w) otherwise Base Case What is the reason behind exponential time complexity ? fo, w f1,W-1 f1,w f2,W-2 f2,W-1 f2,W-1 f2,w f3,W-3 f3, W-2 f3,W-1 f3,W Top-Down Dynamic Programming fo, w f1,W-1 f1,W L4O Dynamic Programming Page 15

## Page 16

f2,W-2 f2,W-1 f2,W-1 f2,W f3,W-3 f3, W-2 f3,W-1 f3, W W (N+1) x (W+1) where , fli, w) is a function that finds the maximum profit you can make by selecting a subset of items [ i N-1 ] and placing them in the knapsack such that the current knapsack capacity is w Bottom-Up Dynamic Programming W (N+1) x (W+1) where, L4O Dynamic Programming Page 16

## Page 17

f(i, w) is a function that finds the maximum profit you can make by selecting a subset of items [ i N-1 ] and placing them in the knapsack such that the current knapsack capacity is w From recurrence, f (i,w) = max { pi + f (i+1, W-Wi), f (i+1,w) } Wi <= W f (i+1, w) ; Wi>W ;isn or w =0 Therefore, dp[i][w] = max { p; + dp[i+1]Iw-Wi], dp[i+1, w] } ; Wi <= W dp[i+1][w] Wi > W ;i=n or w = 0 W W i+1 N-1 N (N+1) x (W+1) Bottom-Up Dynamic Programming Space Optimized W L40 Dynamic Programming Page 17

## Page 18

i+1 N-1 (N+1) x (W+1) L4O Dynamic Programming Page 18

## Page 19

[RJIHW] Unbounded Knapsack Problem https IIwww youtube comlatch?v-DKSZ9ttunEQ&t-4739s Unbounded Knapsack Problem Given a set of N objects along with their prices po; p1, pN-1 and weights Wo; WN-1 } and a knapsack that has a maximum weight capacity of W: Design a recursive algorithm to compute the maximum profit one can make by choosing a subset of objects and putting them in the knapsack such that the sum of weights of the objects in the knapsack doesn't exceed knapsack capacity and you can choose an item multiple times. Example Input N=3,W =10 2 prices 6 3 8 weights 3 1 4 i-1 i  i+1 Recursive Case L4O Dynamic Programming Page 19 W1, put

## Page 20

Let f (i, w) be a function which computes the maximum profit one can make by choosing a subset of objects to be in the knapsack from the given set of objects that starts at the ith index such that the knapsack capacity is w then, f (i, w) = rmax { pi + f (i, W-Wi), f (i+1, w) } ; Wi <= W f (i+1, w) otherwise Base Case What is the reason behind exponential time complexity ? fo,w fo,W-1 f1,w fo, W-2 f1,W-1 f1,W-1 fo, w-3 f1,W-2 f2,W-1 f3,w Top-Down Dynamic Programming fo, w fo, w-1 L4O Dynamic Programming Page 20 put fz,w f1,W

## Page 21

fo, W-2 f1,W-1 f1,W-1 f2,W fo,W-3 f1,W-2 f2,w-1 f3, w W (N+1) x (W+1) where, f (i, w) is a function which computes the maximum profit one can make by choosing a subset of objects to be put in the knapsack from the given set of objects staring at the ith index such that the knapsack capacity is W: Bottom-Up Dynamic Programming W (N+1) x (W+1) L4O Dynamic Programming Page 21

## Page 22

where, f (i,w) is a function which computes the maximum profit one can make by choosing a subset of objects to be put in the knapsack from the given set of objects staring at the ith index such that the knapsack capacity is W . From recurrence, f (i, w) = max { pi + f (i, W-Wi), f (i+1, W) } ; Wi <= W f (i+1, w) Wi > W isn or W = Therefore, dp[i]Iw] = max { pi dp[i][w-wi], dp[i+1, w] } ; Wi <= W dp[i+1][w] ; Wi > W isn or W = W i+1 N-1 N (N+1) x (W+1) Bottom-Up Dynamic Programming Space Optimized L4O Dynamic Programming Page 22

## Page 23

W i+1 N-1 N (N+1) x (W+1) L4O Dynamic Programming Page 23

## Page 24

[RJ[HW] Colorful Knapsack Problem https IIwww youtube comlwatch?v-DKSZ9ttunFQ&t-6370s Colorful Knapsack Problem You are given a sequence of N objects that are coloured using M colours labelled from 1 to M, along with their weights, and a knapsack that has a weight capacity of X _ You are required to fill the knapsack with the given set of objects in such a way that its unused capacity is minimised. Design an algorithm to find the minimum unused capacity of the knapsack such that the knapsack contains exactly one object of each colour and the sum of the weights of objects in the knapsack doesn't exceed its capacity. note return -1 if there is no way to fill the knapsack Example Input N =8,M=3,X=13 0 | TTGTATSCG 7 weights 2 T3 | 4 | 2 | 4 | 5 | 2 3 colors 1TTTTT 2T 2T 2T 3 3 +1 i   i+1 Recursive Case Let f (,x) be a function which computes the minimum unused capacity of L4O Dynamic Programming Page 24 put

## Page 25

the knapsack when we choose a sequence of objects to be put in the knapsack; one object from each of the remaining colors, starting with the ith color such that the current capacity of the knapsack is x then, f (i,x) = min { f (i+1, X-Xij) } Xij <= X Base Case What is the reason behind exponential time complexity ? fi-1,*=13 weights 2 3 | 4 | 2 | 4 | 5 | 2 3 colors 1 | 1 | 1 | 2 | 2 | 2 | 3 3 fi-2,*=11 fi-2,*-10 fi-2,*-9 fi-3,*-9 fi-3, fi-3,X-6 fi-4,x-7 X=6 X=5 X-4 X=4 X=3 fi-3,x-8 X=6 fi-3,*-5 X=6 X=5 X=4 X-3 X=3 fi-4,x-2 Top-Down Dynamic Programming L4O Dynamic Programming Page 25 X=7 fi=4, " fi=4, = fie4, " fi-3, = fi-4,= fi-4, fi=4, = fi=4, fi=4, fi=4,- fi-4,-

## Page 26

LCS Longest Common Subsequence (LCS) Ac Given two strings S1 and Sz of lengths M and N respectively. Design a recursive algorithm to find the length of the longest common subsequence between them_ L Example atic S2 AGct Input S1 = "ATGC" , M =4 S;= 6 c d Sz = "AGCT"  N=4 N=l Output M-4 Explanation The LCS between S1 and Sz is "AGC" Auc S1[07 = = s1 Co) false Le 0-'1 )-& Sz (0 - S, [0 _ m-'] 3t Les N-'7 len 9 Lcs (95_."-17, Szli._N-i7) S E 8nend S2 Recursive Case S1 $, { Let f (i, j) be a function which computes the length of the longest common subsequence between Si[i M-1] and Szlj N-1] then, S2 max {F (+1,))= STuT [= Sz0r 9 f (i, j) = 1 +f(i+1,j+1) S, [i] == Sz[i] J Base Case 0 I=0 #G--7,;): WNF What is the reason behind exponential time complexity Jssute S,5;) apj'y fo, 0j tuu +nxoo = N + / f1, +xd8eo = r fo, 2 X f1,2 fo, fm, 0 ` M+a Top-Down Dynamic Programming Dynamic Prograning Page 26 albg S,'..M-J S2 Lz-. 1F] +u,a-en) = 0 2m+2 82 5j ) M+| #edpez4 [ Aobra = {a,"'

## Page 27

fo, n+' f1, 0 fo, 04 | 4 M f2, 0 fo, 0:ja f3, f2, f1,2 fo, + Mti) (011) fm; fo, N #;j (M+1) X (N+1) where, f (i, j) is a function which computes the length of the longest common subsequence between S,[i M-1] Sz[ij N-1] Bottom Up Dynamic Programming 4v= # (M+1) X (N+1) where, f (i, j) is a function which computes the length of the longest common subsequence between S,[i M-1] and Sz[j N-1] From recurrence, (max f (i+1, j), f (i, j*1) } S-[i] != Sz[i] (i, j) = 1 +f (i+1,j+1) Si[i] == SzDi] Therefore, max { dp[i+Wu], dp[iju+1] S-[i] 1= S2[i] dp[i]l] dp[i+1]Ii+1] Si[i] == Sz[i] j=+0 j+1 toe T~|: LID - Dynamic Prograning Page 27 718, and

## Page 28

toe $ M-i {#m 5 7 evos (M+1) X (N+1) [RJ[HW] Building the LCS from dp[II] G dp[JD] [RJIHW] Space Optimized Bottom-Up Dynamic Programming j+1 (M+1) X (N+1) Dynamic Progranming Page ;

## Page 29

j+1 (M+1) X (N+1) Dynamic Prograning Page 29

## Page 30

[RJ[HW] Edit Distance Edit Distance Given two strings S1 and Sz of lengths M and N respectively. Design a recursive algorithm to find the minimum number of edits required to transform S1 into Sz such that each edit operation performed on S1 can be a letter insertion or letter deletion or a letter substitution: Example Input : S1 = "food" Sz = "money" Output 4 f T T o [ d mToTn ~e | y M-1 N-1 S1 S2 L4O Dynamic Programming Page 30 ( 0

## Page 31

Recursive Case Let f (i, j) be a function which computes the minimum no. of edits required to transform Si[i M-1] into Sz[j N-1] then, 1 + f (, j+1), 1 + f (i+1,j); f (i, j) = min Si[i] I= S2[j] + f(i+1,j+1) Base Case f(i-M, j) is a function which computes the minimum number of edits required to transform S1[M M-1] into S2[j N-1] M-1 M N-1 L4O Dynamic Programming Page 31

## Page 32

S1 S2 fl, j-N) is a function which computes the minimum number of edits required to transform S1[i M-1] into Sz[N N-1] M-1 N-1 N S1 Sz 1 What is the reason behind exponential time complexity ? fo, 0 fo, f1,0 f1, f1. f2. 0 f2 1 f1.2 f2 1 f2. 2 L4O Dynamic Programming Page 32

## Page 33

f1, f2, 0 f2, f1,2 f2, f2,2 f2, f3, 0 f3, f2, 2 f3, f3,2 Top-Down Dynamic Programming fo,0 fo,1 f1,0 f1, f1, f2, 0 f2,1 f1,2 f2,1 f2, 2 f2, f3,0 f3, f2,2 f3, 1 f3, 2 N M (M+1) x (N+1) L4O Dynamic Programming Page 33

## Page 34

where , f (, j) is a function which computes the minimum number of edits required to transform Si[i M-1] into Sz[j N-1] Bottom Up Dynamic Programming N M (M+1) x (N+1) where, f (i, j) is a function which computes the minimum number of edits required to transform S-[i M-1] into Sz[j N-1] From recurrence, 1 +f (,j+1), f (, j) F min 1 + f (i+1,j), Si[i] I= S2[j] +f (i+1,j+1) Therefore, + dp[i]Ij+1], 1 + dp[i+1JI], dp[i]D] = min Sili] L= Solil + dpi+1Ii+11 L4O Dynamic Programming Page 34

## Page 35

UPV'V ' 'J, 1 + dp[i+1JI], dp[i]D] = min Si[i] I= S2[i] + dp[i+1]I+1] j   j+1 N i+1 M (M+1) x (N+1) Space Optimized Bottom-Up Dynamic Programming j+1 N i+1 M L4O Dynamic Programming Page 35

## Page 36

M (M+1) X (N+1) i+1   j+1 N i+1 M (M+1) X (N+1) L4O Dynamic Programming Page 36

## Page 37

[RJ[HW] Wildcard Matching Wildcard Matching Given an input string S and a pattern P that contains 0 or more wildcard characters ('?' and '* ), design an algorithm to determine if P completely matches S such that the wildcard '?' can match any single character and *i matches 0 or more characters. Example S a | b | c | a | b | c | a a P a | ? | c | * | ? | a |a | b | c | a | b C P ~a | ? | b / * S P L4O Dynamic Programming Page 37 S ||

## Page 38

Recursive Case Let f (i, j) be a function which checks if PLj N-1] matches S[i M-1] then, f (i+1,j+1) PD] F= S[i] or PI] == '2' I*i f(i, j+1) or f(i+1, j) PD] FF f (i, j) = false ; PI] != S[i] Base Case What is the reason behind exponential time complexity ? L4O Dynamic Programming Page 38

## Page 39

Top-Down Dynamic Programming N M (M+1) x (N+1) where, f (i, j) is a function which checks if PQ N-1] matches S[i M-1] Bottom Up Dynamic Programming N M (M+1) x (N+1) where, f (, j) be a function which checks if PIj N-1] matches S[i M-1] L4O Dynamic Programming Page 39

## Page 40

From recurrence, f (i+1, j+1) PI] F= S[i] or PLi] == '?' I*i f(i, j+1) or f(i+1,j) PD] FF f (i, j) false ; PI] != S[i] Therefore, dp[i+1JIi+1] PI] =F= S[i] or PLi] == '?' dp[i]Ii+1] or d[i+1][ j] PI] == I+i dp[i]l] F false ; PI] != S[i] j+1 N i+1 M (M+1) x (N+1) L4O Dynamic Programming Page 40

