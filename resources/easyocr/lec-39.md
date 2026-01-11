# Lecture 39 (EasyOCR)

**Source:** `L39 - Dynamic Programming.pdf`

---

## Page 1

Intro to DP Dynamic Programming (D.P ) It is a problem-solving technique that is used to perform Recursion without Repetition by storing the results of unique sub-problems in a table and referring to it as and when required: Fibonacci Numbers Given a non-negative pumber Tndesign a recursive algorithm to compute the nth Fibonacci number. 5 8 (n) 2 3 5 8 13 21 34 n71 fn = #o-' fr-1 Recursive Case fi = Let f(n) be a function which computes the nth Fibonacci number then f (n) = f (n-1) + f (n-2) Base Case Lo Li Lz L 3 n- La -  Assuming all the levels are filled, total no. of sub-problems is equal to 20 + 21 + 22 + 23 + 2n-1 This is a finite GP where, a = r =2 #=n The sum of finite GP given as follows [(r#-1) /(r-1)] ,) @nri Progtatuning #-~~ Pg

## Page 2

#=n 7 The sum of finite GP given as follows [(r#-1) /(r-1) ] Substituting the values of a,r, and #, we get [(2n-1) /(2-1) ] 2n_1 2n How much time do we spepd on each sub-problem ? lnst O(n) Vor Space : Therefore, the time complexity is equal to (2") Fm What is the reason behind exponential time complexity ? (mn1 Sty 1 fiad Jut J + {n 0+1 unii Swcw biem (0l) we Cin &rPak 42 (bok ~R 2  anaJ (as amp) 98 8r1 (JRCaJb-') { 1ti + Stbre rswits 3 ' Tet'0 Jpta?; 011 me 3ni460' 9wbfrobiors Top-Down Dynamic Programming Membiz a1'on ba6 (0 $ R 1i 0_~') & F (oz~o 11 netundp@] in , ~5 ~sfo Ju7ry rewrs i € Case lorkups {a;+ ; 1 + fo-2? tetvm JPto)= fo-) 8 Ro= $ JP; = f JRa = fo dp{] where, 0+ f(i) is a function which computes the ith Fibonacci number hme; (q+ ) . wnst ~ dla) dup kz5 ~2   3 1  dve m R 0' 2 f & f # # Hr knop Stk 0 1 1 2 3 5 Rs Lnsk s hace: o(n) (ann ) tns Xp Ola ) @nri Progtnuning Fage ? Od. 8Mprobiems o 9" Ptlon?i J,= f + n (3" 5 Jpt? Aox 6h Aac , ) 6"

## Page 3

LD' `0' (011$ (ann) " Ok^ ) % Pa- Bottom-Up Dynamic Programming Tabuliz?ton 7 f; 4 #86 & Jep J;= f; Jo-fr JQ;-,+Jp; > Base (st where, 0+i f(i) is a function which computes the ith Fibonacci number Xxan From recurrence, f () = f (-1) + f (i-2) i>=2 JP = po =  Therefore, dpli] = dpji-1] dpli-2] 17 2 J9,-h/ Space Optimized Bottom-Up Dynamic Programming i-2 C=atl Jp; = 1R;-' + 'R;- @nri Progtatuning Page } Aac , 87"s Bc% Xcc

## Page 4

Min. Steps to One Minimum Steps to One Given a positive number n, design a recursive algorithm to compute the minimum no of steps required to reduce the given no. to one such that at each step yOu can 1o 40 1 reduce n to n-1 reduce n to n/2 if n is divisible by 2 or L0 reduce n to n/3 if n is divisible by 3 or 7 X Example 8 2s, Input n = 10 Output Explanation 10 7>9+5>3-31 : mi 0 sk Qs" ^48410 L Fta) = 7 k 1 12 Tt mi ^ n-1 F. Recursive Case Let f (n) be a function which computes the minimum number of steps required to reduce n to one then (n) = 1 +min f (n-1) f ("/2) ("I3) Base Case 29s 6MC ) J+ J2 (t: $ Ld #o', Jm 5- %' v%68 Li 3' Lz l Assuming all the levels are filled, total no. of sub-problems is equal to 30 + 31 + 32 + 33 + 3n-1 Dynamic Programming Page 4 190," 1 find re jul' Ar2

## Page 5

This is a finite GP where, a = r =3 #=n The sum of finite GP given as follows =a *[(r#-1) /(r-1) ] Substituting the values of a, and #, we get [(3n-1) / ( 3-1) ] 3n_1) /2 How much time do we spend on eack sub-problem Wast Therefore , the time complexity is equal to [3") What is the reason behind exponential time complexity Js Top-Down Dynamic Programming b fo Inl2 (fni3 Anit subcrorcs iaft: 8k,= # 8k2 }; Ja-tn dpc7 where, f(i) is a function which computes the minimum number of steps required to reduce the to one 41   2   3 4 5 dp Dynamic Programming Page 5

## Page 6

; Bottom-Up Dynamic Programming = 0 -#=0 T dp #p; i' % Bzt where, Oti Jpa= $ f(i) is a function which computes the minimum number of steps L%inal ons ) required to reduce to one From recurrence, f (j) = 1 + min (77 ), 1(12); Therefore, dpli] = 1 + min dpl1]; dpf], dplh] Dynamic Programming Parc

## Page 7

[HW] Coin Change Problem Coin Change Problem You are given an integer array coins representing coins of K different denominations and an integer N representing total amount of money: Design a recursive algorithm to compute the fewest number of coins required to make up that amount i.e. reduce the given amount N to 0. may assume that you have an infinite supply of each kind of coin: Example Input coins = [1, 2, 5],n = 11 Output 3 Explanation = 11 = 5 + 5 + 1 coins = { Co, C1,C2, Co C1 C2 Ck-1 N-Co N-C1 N-C2 N-Ck-1 Recursive Case Let f (n) be a function which computes the minimum no of coins required to reduce the given amount N to 0 then k-1 f (n) = 1 + min ( f (n-Cj) ) n-Cj >= 0 j=0 L39 Dynamic Programming Page You

## Page 8

Base Case What is the reason behind exponential time complexity ? N =4 coins = { 1, 2 } f4 f3 f2 "2 22 2 fo 2 fo fo fo fo Top-Down Dynamic Programming N=4 coins = { 1, 2 } f3 2 "2 22 f2 f1 fo f1 fo fo fo fo n-" L39 Dynamic Programming Page

## Page 9

where , f (i) is a function which computes the minimum number of coins required to reduce the amount to 0. N =4 1   2   3 4 coins = { 1,2 } dp 3 f2 "2 12 f1 fo 22 f1 fo fo fo fo Bottom-Up Dynamic Programming n dp where, f(i) is a function which computes the minimum number of coins required to reduce amount to 0_ From recurrence, k-1 f () = 1 + min ( f (n-Cj) ) i-Cj >= 0 Therefore, k-1 dp [i] = 1 + min dp[i-cj] ) L39 Dynamic Programming Page jF0 j-0

## Page 10

Ladders Problem Ladder's Problem Consider a ladder with steps person is standing at the bottom of the ladder and wants t0 reach to its top. Design a recursive algorithm to count the number of k} ways the person the reach the nth step i.e: ladder's from its bottom such that 01, 5 at each step the person can take ajump of size ranging blw one t0 k steps_ Example cand: [', 3] Input :PaTK3 Output homc ce Explanation nT1,1] 3 1, 2] D 2 33 [3, 1j X+y+2 fx waj + riech ) L tn 0 + trm botem k-? hone fn #wj d' 2 n-2 & woys + d' trm 6 +  0 4 Pa=) '+ '>a fn # w'js +6 oeoch tt frds trm tweys + Teoun ^ {1 K Mm bin Bo-t ~fn p_ 2 #-; 5 n-> 4-j J-1 ^ -} 14j &k n-X Recursive Case R-} Let f(n) be a function which computes the no: of ways a person can reach the nth step i.e_ the top of the ladder from its bottom then; (n) = 2fn-j) 69330 Base Case {l) = ? - 1 What is the reason behind exponential time complexity Top-Down Dynamic Programming Ja ~ $ +| DYI Prezhaenil Pug: top Xt)tt 3 1,2,}

## Page 11

Ja _> + +| ia#: a8 , J;e8, Jn=} Jpcs where , 0+ f (i) is a function which computes the total number of ways person can reach the ith step of the ladder from its bottom_ fo = Ztc-j 0770 Bottom-Up Dynamic Programming J= # ak p:-4; 0jz 0 f; = 2e ap I$ 2tabl where Ot+ (i) is a function which computes the total number of ways 0 os6 person can reach ith step of the ladder from its bottom Lasc From recurrence_ 6 J,ek=/ i-j >= 0,i > 0 Therefore, dpd-EdpT : > k Time Optimized Bottom-Up Dynamic Programming_ 2a8,- PG-K-' dp 24i 4k 7Jr = / 748,: J, do; = 2 6-j70 2 200, JR,+J0. j-1 Of;- J8 ; JV;-+ #-t 7 4 S+ 313 0z+2,+J2 2d82 Jiz Jp; stat transi*en DYI Prezhaenil Pug: J8= # ~1 45J6; fn Jp; ) {(=E{(y) ap;; 4;+' Jz € Jl;-> 2jQ ;-(

## Page 12

[RJIHW] House Robber | House Robber / You are a professional robber planning to rob houses along a street: Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night: Given an integer array nums representing the amount of money of each house, return the maximum amount of money can rob tonight without alerting the police. Example Input N =5 2 3 4 100 50 400 200 100 i-1 i+1 i+2 n-1 Recursive Case L39 Dynamic Programming Page 12 you

## Page 13

Let f (i) be a function which computes the maximum amount of money that can be robbed in a night from a given sequence of houses starting at the ith index without alerting the police then , f (i) = max { nums[i] + f (i+2) , f (i+1) } Base Case What is the reason behind exponential time complexity ? fo f2 f1 f4 f3 f3 f2 f6 f5 f4 f3 fn Top-Down Dynamic Programming n n+1 L39 Dynamic Programming Page 13

## Page 14

where, f (i) is a function which computes the maximum amount of money which can be robbed in a night from a given sequence of houses starting at the ith index without alerting the police. Bottom-Up Dynamic Programming n n+1 dp From recurrence, f (i) = max { nums[i] + f (i+2) , f (i+1) } Therefore , dp[i] = max nums[i] + dp [i+2] dp [i+1] } L39 Dynamic Programming Page 14

## Page 15

[HW] House Robber II House Robber IL You are a professional robber planning to rob houses along a street: Each house has a certain amount of money stashed. All houses at this place are arranged in a circle That means the first house is the neighbor of the last one: Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night: Given an integer array nums representing the amount of money of each house, return the maximum amount of money You can rob tonight without alerting the police. Example Input : N = 8 2 | 3 | 4 5 | 6 7 | 4 | 1 | 9 | 3 | 8 | 6 | 5 2 | 3 4 | 5 | 6 7 7 | 4 | 1 | 9 | 3 | 8 | 6 | 5 7 Maximum value obtainable from Start house 9 7 | 4 | 1 | 9 3 8 6 OR Last 5 3 house 8 4 |9 3 | 8 | 6 5 L39 Dynamic Programming Page 15

## Page 16

[RJ[HW] House Robber III House Robber Given the root of a binary tree; in which each node corresponds to a house and the value of the node represents the amount of money in each house: Design an algorithm, to find the maximum amount of money a thief can rob without alerting the police such that he is initially standing at the root node & police will be informed if two directly-linked houses are robbed together. 3 3 2 3 5 3 3 root root L39 Dynamic Programming Page 16

## Page 17

6 5 6 5 3 2 4 3 2 4 8 9 8 9 L39 Dynamic Programming Page 17

