# Lecture 14 (EasyOCR)

**Source:** `L14 - 1D Arrays.pdf`

---

## Page 1

Prefix Sum Revision Saturday, 14 June 2025 10.29 AM 5 aw[37 = 2 3 Lo 3 0 40 50 40 30 Pxumt;) store s 2   3 4 tbe sum 4 Psumt? 12| z0| 60 |D0 150 Prefix cnd s 0 + me 5 im 'x [i-'7 + Gw[,] 1=0 7 PSvmo 1-$ 3 20 3 0 40 Sp 3 3 0 10 ^+i Sum J (ryix Sum 2 Swm d (xyix h (rs mat tnxt ends ar JF '> 2 pef; k Ot i7 0 idx np end} Sum' [6) stses te 9 Prefir te l-t) h i47 0 J+ + aw [i-'] ~9| [,) Iesum$+'2 Ipsumti 7 Sij= Svm (6 + $) Sum (ot i-1) LI4 ID Arrays Psvm[17+ Psw[3] tnt p sum PSum[i] {71 awo (sumt ) ends Sum Psumti-,3 Rsum Fage

## Page 2

Sum ( / t )) LI4 ID Arrays Fage

## Page 3

Difference Arrays le' Io - |o 1 2 les le$ Difference Arrays 8; : 65* cr;,t;] You are given an array of N integers, and Q queries each of the form { 1i, ri,xi } where 0<-li<-ri<-N-1. Your task is to apply each of the Q queries to the given array & print the resulting array applying a query to the array means adding xi to all the elements of the array with indexes from Li Lo ri inclusive_ Example 2 3 4 N =5,Q =3 Xs 2 3 5 576 WZ> Qo Q1 8 9 ( "2 / K Q2 S3 |9 6 42 Ii 10 %8' X = 0 ^. 1-1 tne Wors+ _ ()8 k 'Ppl ) '0 w2U @inter hme 148'9 itevbhe kom 9 +r Jssumia) J"4 t0 'Pp'y J 1484) Ib Is total nme :wn ) Jo " '.4 TLe F^e5 Jifftrj +3 Xi L lnst 2 5 | 2 Ji}PCt#) -*; _ T Qo 2 13 Q1 2 | 3 | 2 1 Q2 3 | 4 7 exka sbt + mkf impl' P6ser Jfc avo;9 4+ (36 $ Jip}" [ 5 Vaev ^=5_| Jiffcrj +#X 0 ^ lns+ Jift 6r+12 -= * Qo 2 Io LI4 -ID v & Spend 5 . 1d" 2| Uya (v Ny Dec

## Page 4

T-0 2 ^ * 4x| 212 dffle ) ls + Ji}t 6r+07 -=* Qo 9 6 12 |i Io 1 3 Fnt=6 1 ' Wast + q'tnst :. 0(t4) wast J4z5 H4 2 --2 -+ ^ 2 3 += Jiff ti-] 5 0 9 -1 0 J#}5s LI4- g Ji}}[;] Ny Dec

## Page 5

Little Girl and Maximum Sum Little_Girl and Maximum Sum The little girl loves the problems on array queries very much One she came across a rather well-known problem: you've got an array of n elements (the elements of the array are indexed starting from 1J; also, there are q queries, each one is defined by a of integers /,, ri (1 <l <r < n): You need to find for each query the sum of elements of the array with indexes from / t0 r , inclusive: The Iittle girl found the problem rather boring: She decided to reorder the array elements before replying to the queries in a way that makes the sum of query replies maximum possible. Your task is to find the value of this maximum sum: Input The first line contains two space-separated integers n (1 < n < 2 . 10') and q (1 < q < 2 . 10' the number of elements in the array and the number of queries, correspondingly: next line contains n space-separated integers @; (1 < @ 107) the array elements. Each of the following q lines contains two space-separated integers /, and ri (1 <l, <ri < n) _ the i-th query: Output In a single print; a single integer the maximum sum of query replies after the array elements are reordered  4cj [0 } ? ] Wjat J" mximir 23+ 3 5+ 2.2 X Examples 5+3= 8 7 0i - tniS 6 + IS + 9 input 9 = 3 9 } 3+2 = 5 8 123 42+6) 28 = 001 J* 5+3+2=/0 Cl [ 3, 5, 2] 65 3 4 a[1 2] 1 2 2 43 20, + 243 49t output CoF C2$, 25 input 0:$ 423 Copy 02 1 3 A[) 2 6% 19 output 41+02+43+44+45 Copy 02+93 33 Jft 02+ 631 $ 1a + 342+ 1awtles €mjxinf r Ttt; tnil 2 0 -2 1+2 + 3.$ + 3.4 + 04 + 1.3 Ala: 2 2 + I5 + 12 + (+3 4 42 43 4y 4 3 $ [R,r] Jipttr? ++, Jirp(v+1) - - ) LI4 ID Arrays day pair <2 . The line }zv 3 ] 05 Ta Page

## Page 6

3 3 1 3 3 1 1 3 3 1 ! 3 4 $ 4 € ? 5 2 Y | 3 Hi+ 12+1-3+3745 3 > ^-| 0 Sott (V' beainc ) V-erdl ) Cfast Ips LI4 ID Arrays {reqv;' J Page

## Page 7

[HW] Karen and Coffee Karen and Coffee Karen, a coffee aficionado, wants to know the optimal temperature for brewing the perfect cup of coffee: Indeed, she has spent some time reading several recipe books, including the universally acclaimed The Art of the Covfefe' She knows n coffee recipes. The i-th recipe suggests that coffee should be brewed between l; and ri degrees, inclusive, to achieve the optimal taste_ Karen thinks that a temperature is admissible if at least k recipes recommend it. Karen has a rather fickle mind, and so she asks q questions. In each question, given that she only wants to prepare coffee with a temperature between a and b, inclusive; can you tell her how many admissible integer temperatures fall within the range? Input The first line of input contains three integers, n, k (1 <k<n<200000), and q (1 <q < 200000), the number of recipes, the minimum number of recipes a certain temperature must be recommended by to be admissible, and the number of questions Karen respectively: The next n lines describe the recipes. Specifically; the i-th line among these contains two integers /; and ri (1 <l<ri<200000), describing that the i-th recipe suggests that the coffee be brewed between /; and r; degrees, inclusive. The next q lines describe the questions. Each of these lines contains a and b, (1<a<b<200000), describing that she wants to know the number of admissible integer temperatures between a and b degrees, inclusive. Output For each question, output a single integer on a line by itself, the number of admissible integer temperatures between a and b degrees, inclusive_ LI4 ID Arrays Page has,

## Page 8

Examples input Copy 3 91 94 92 97 97 99 92 94 93 97 95 96 90 100 output Copy 3 input Copy 200000 200000 90 100 output Copy LI4 ID Arrays Page &

