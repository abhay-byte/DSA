# Lecture 25 (EasyOCR)

**Source:** `L25 - Recursion.pdf`

---

## Page 1

Generate Permutations Generate Permutations Given a string, design a recursive algorithm to generate all of its permutations_ permutation of a given string is a rearrangement of its characters. Example Input "abc" Output "abc" "acb" , "bac" , "bca' "cab" , "cba" > 2 .: | = = 6 3 | 6 6 < %p 0 c 6 i/p 184 6 0 ( A= 3 6 0 C 4 6 L 6 M 1711 F 1-37 Ie 4 C 6 1 6ca d @ Is |c ~0 8c iR.) 3 6ac ca in8,) 2 iPG; 1e-'Io / (Dut 24 i~P; i-1 ." 1+ va Lrpcj swcCinf;, inP;) ~ }G+) 7 i+ 's   0 fr t1 + +kes sw'p(aR: , inPin) 37 }6+) Swvp(nl ,, inP; ) 4 Hlr ) + 0- Je&'Sions foc $w'p ( p:, iR;+) 5}6+) 4 Solve +is jus +  4eude ~fot) to Swxp CiP; , inka-) +nP itn {Jx Receion Desmutorhis 6 Swxplinps, SwplPs,= Swep(^R,in0.) #G-n) fc) Nx | 14ni Fae

## Page 2

Solve +is jus+  Aeude fo) to Swxp CinP; , 'nRa-) tne itn {Jx foc {20 i+1 6+2 n-- Cn-= C41 Li '3 6 allb aTTFI sla |cf ble4^7 4i-} ~@Tc Receion iit tit) IT4  6FFT Fae

## Page 3

[RJIHW] Generate Unique Permutations Generate_Unique Permutations Given a string, design a recursive algorithm to generate all of its unique permutations: permutation of a given string is a rearrangement of its characters. note generate the permutations without using any extra space_ Example Input "aabc" Output "aabc" , "aacb" 'baac" "baca" "bcaa" "caab" "caba" , "cbaa" G 4 6 ( a 0 &b G 6 @C Tzc 0 6 € & inPs, inPo Gka $ info ,iP) 0 Cz Gc 6a i~Po,nPz 7 Jvpltotes 'ak,inls L2S Recursion inp Page

## Page 4

L2S Recursion Page

## Page 5

[HW] Letter Combination of a Phone Number Letter Combination of a Phone_Number Given a phone keypad, and a string representing a n-digit number write a program to generate all the words possible upon pressing the n-digits on the phone keypad: 23" " 2365'_ "ad" 2 3 32F Ac Der 'ae" 'af' 4 5 6 bd" Oh J Mad 60 be Ad bf 8 Ae 05 Fos Tuv Wz BF 'cd" Af 'ce" "cf" L25 Recursion Page 5 3

## Page 6

[HW] Construct Smallest Number From DI String Construct Smallest Number From DI String Given a 0-indexed string pattern of length n consisting of characters '' meaning increasing and 'D' meaning decreasing: A 0-indexed string num of length n+1 is created using the following conditions 2 | num consists of the digits to '9' where each digit is used at most once if pattern [i] =='', then num [i] < num [i+1] if pattern [i] == D', then num num 1= 4 Design an algorithm to return The Texicographically smallest possible string num: Example 2 ~3 | 4 | 5 | 6 7 8 pattern TDTTTDTDTD num 2 | 3 | 5 | 4 | 9 | 8 | 7 | 6 0vm I2 l/y/3 (5 T T T ho? @ t ha 3 - trve 1 | 2 ~3 74 3 pattern D 1 |  D num S _1 PoIse 6 _ Pxtse 1 _ % {osse 5 Polse pattern num L25 Recursion patternl) Axe Polsr Kve oxse 3 Page

## Page 7

Permutation Sum Permutation Sum Given an array of distinct integers candidates and a target integer target; design a algorithm to find all the permutations of candidates that sum Up to the target: You may print the permutations in any order. The same number may be chosen from candidates an unlimited number of times Example -+ 82,,,,4} Input target = candidates Output +34 ts 2 [21 3 172 215 5-2 L3 +-2 LALU w t3 @rtx tz0 C 0 C = {Co, C1,C2, Cn-1 } Co C1 C2 Cn-1 t-Co t-C1 t-C2 t-Cn-1 t-4 545 3 , 2 4s t3 1B + -2_ 93 2,1 ,3 3] t-0 + -0 2, 3,2 t- | L3 LzS _ Recursion Page

## Page 8

[RJIHW] Combination Sum Combination Sum Given an array of distinct integers candidates & a target integer target, design an algorithm to find all the unique combinations of candidates that sum up to the target: You may print the combinations in any order: The same number may be chosen from candidates an unlimited number of times. Two combinations are said to be unique if the frequency of at least one of the chosen numbers is different. Input target = ( 2 3 2 , 2, 3 1 candidates 2 | 3 | 5 7 2 , 3 , & X Output 2 2 | 3 2 | 5 3 , X LA 2 , 5 ` 5,} 5, 2 X C = { Co,C1,C2, Co C1 C2 Cn-1 t-Co t-C1 t-Cn-1 C = { Ci, Ci+1, ' ' ' , Cn-1 } Ci Ci+1 Cn-1 L2S Recursion Page & t-C2 Ci+2

## Page 9

Ci Ci+1 Ci+2 t-Ci t-Ci+1 t-C2 t-Cn-1 [i, n-1] [i+1,n-1] [i+2,n-1] [n-1, n-1] L2S Recursion Page Cn-1

## Page 10

[HW] Combination Sum II https ]Ileetcode com/problems/combination-sum-ii/descriptionL L25 Recursion Page 10

## Page 11

[HW] Ladders Problem Ladder's Problem Consider a ladder with n a person is standing at the bottom of the ladder and wants to reach to its top. Design a recursive algorithm to count the number of ways the person the reach the step i.e. ladder's top from its bottom such that at each step the person can take a jump of size ranging blw one to k Example Input n =4,k =3 Output : 7 Explanation : [1, 1, 1, 1] [1, 1, [1,,2, 3 3 [2, 1, 2 [2, [1, 3 [3, n-1 2 L25 Recursion steps, nth steps. Page

## Page 12

i+k i+2 i+1 Recursive Case Let f (i) be a fn: which computes the no. of ways a person can go from the ith step to the nth step of the ladder then, k f () = f (i+j) 5 i+j <= n jF1 Base Case L25 Recursion 12 Page

## Page 13

Rat in a Maze Rat in a Maze | Given a M x N maze with some blocked cells marked with X and a rat that wants to go from the (0, O)th cell (source) to the (M-1, N-I)th cell (destination) design a recursive algorithm to check if there exists a path to from the source to destination cell such at any point of time the rat can move one step either in the right direction or the down direction: Example Input 0 0 0 0 X 0 Output True Lhelk $ rat (Gn j' 6 frend + checr 'f (0,0 ) (M-1,0-') ? 'k4 (Dn J' tom (9,) 2 X (602) +0 (m-',n-') = n-2 n-1 962 Jwr {d m-2 + chek iF m-1 T't mxn Ron ( 1,0) + (m-1,-) ? (6oe ) 4 tieve i1 6> tm 1+,j 'm (e + ? kit 6i+13 m L2S Recursion Page 13 C9 X o ) JonY (Gr &' 852 (htuk pat (M-I,^-m(eli

## Page 14

m-  mxn tituj 6T 4; ` #ij" Jn i F M-/ A; whCa {~ -~-i ~hco 8; = 'cb shen i~=m-) 6 L2S Recursion Page 14 iact J -0 Hi,j T(L _ ( 7* J *-1-1 Pix, 0 # a-| Jnd R;,i" V - -a-i Bose (asc

## Page 15

Rat in a Maze II Rat in a Maze Given a M x N maze with some blocked cells marked with X ), and a rat that wants to go from the (0, OJth cell (source) to the (M-1, N-1)th cell (destination) design a recursive algorithm to count the number of paths that exists to reach destination cell from the source cell such at any of time the rat can move one step either in the right direction or the down direction. Example Input Output 3 Kn4 #pms tnm 0,0 + M-1,- ? X+) 0,1 to M-1,-1 ? fin #prs tm n-2 n-1 (hiend X (in+ ) Js2 Kniend # h~ #phs m-2 tr Cv') m-1 m Xn Lm ] (iat) {nd A twm (, + (m-1,a-i) 7 ',jtl P'j = fiti T Kt,1 L7 He 5 m xn (l)=zn) Te 0 '(w32e LIS Kecurslon point Yor 6,c+) f ms #(i--m 6 =='x' ) { ~t 0 ) Puee

## Page 16

i~= m- | J=  ( ~et 1 / 5 LIS Kecurslon 10-i ) ?rd Puee

## Page 17

Rat in a Maze III Rat in a Maze III Given a M x N maze with some blocked cells marked with X ), and a rat that wants to go from the (0, O)th cell (source) to the (M-1, N-1)th cell (destination) , design a recursive algorithm to  generate all the paths that exists to go from source cell to the destination cell such that at point of time the rat can move one step either in the right direction or the down direction: Example Input 0 0 0 0 ? X 0 0 0 X X | 0 | 0 0 0 0 mxn mxn m J2e ( J[7 Pomt1c? (' #~i 3 '5 ru S FC,1t'> 22'x' ) #f (mzz;;- ~e ) M-| Jcd ( i~= $ 1911 L2S Recursion 0 -=^) Path;j = `1' fti+i j) Pom 'j = '0' J=zn- poiy) Omat Fage

## Page 18

0 2 702 0 Fs 0 0 mjze Patn L2S Recursion 2 Fage

## Page 19

Rat Chases Its Cheese Rat Chases Its Cheese Given a Mx N maze with some blocked cells marked with X and a rat that wants to go from the (0 , O)th cell (source) to the (M-1, N-1)th cell (destination) , design a algorithm to find the unique that the rat has to take to go from source cell to the destination cell such that at a point of time the rat can move one step in the left; right; up, or the down direction: Example Input 0 1 0 0 0 X 1 m 8 X 0 ~0 0 m-1 m-1 mxn m xn L25 Recursion Page 19 path

## Page 20

[HW] Unique Paths III https ]/leetcode com/problems/unique-paths-iiiL L25 Recursion 20 Page

## Page 21

[HW] Word Search Word Search Given an mx n grid of characters board and a string word, return true if word exists in the The word can be constructed from letters of sequentially adjacent cells , where adjacent cells are horizontally or vertically neighbouring: The same letter cell may not be used more than once. Example word = ABCCED word = SEE A B C E A B C E S F C S S | F | € S A D E E A D E E L25 Recursion Page 2 1 grid.

