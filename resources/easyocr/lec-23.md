# Lecture 23 (EasyOCR)

**Source:** `L23 - Recursion.pdf`

---

## Page 1

Sum of Array Sum of Array Given an array of N integer, design a recursive algorithm to compute the sum of array elements Example #ne 0(n) {at $ = 0 Input (io; i2c, {++) { 0 (1 ) foc spar Gm[;1) 20 30 Output 150 Loot L[< tnc Sum Xlo _^-i] Jin Xi X [ ] { } Kz Xa-| Xo + S Sum (t (#riend ` 9 S}tix S - Xo + 4 ( N* I( P+ i   Q fn tnt finds C) +ne Aum XCi- 9-+7)E 7ht) Xiti Xa- X[ij + flit) '+ i 4 fo (xCi+: {70 Sum #ncs tne svm 4 K[mtl 0-,J fl) 3 10 2 0 3 0] 40 flo ) xton + #lo) L xrj+f() L) xt2o+#() ~-0 J - -n- | t invol; d }"A }l) t (fn) Sts tnF 4+ ^ a fa ~a Ro Ine fiads [n:- ti+ fs Svm d U1 tn} Svm ) {xn-'} Re-urslon F fc [ 71) Xo-| 70, 4-) 5 tn + 0 F stotts Yi+l, +w + Xc;] X[ 0-iJ ; i+ i$ n-/7 XCn-1

## Page 2

tne DV"' 3 {xn'} 1 *6 (ase Xn-1 (n-i) int flint X[] , int int Base (>6 base case (1_ 0 Il t(n-1) find the sun return XIn 1] ; 50 wnst recursive case Fa-z #me 0(o ) 11 f(i) find the Sum of Xli 9 1 90 Ja-' Ii 1. ask your friend t0 find fviend I20 Int A = f(x, 1); 7 pa 6 00 " return Xli] F =0 14 0( n ) (Sv { } exists :==^-| XCn-,] + fta) vild i~= 0 X (n) Jlnti ~ ) Reils f() Pko ) +no F Uil ' "a {n tne 4 {ds XC a 0-'7 {} 3 int flint X[I , int int 1) Lo L0 3 0 4D 0 (0 ) #ne; (a1) wast N base case if (i E n) 2 0 (n ) 1 f(n) find the sum Wnst ~ return A = (ati) . 2 So I1 recursive case p A = 1i f(i) find the sum of 11 ask your friend to 0-$ + 2 9 int A T(x, 1); 2 i2d return Xli] 9 f A'0 (50 Rezurslou Fuce - 0-'7 XCn-/ 0 =5 9 R. s (ace : Prbkm Wn + 9 ac & 0-'] Xla . JSSume ftn-,) {vi; = 0 Sum Snace: X

## Page 3

10 10 3 0 4 0 tni$ + +1J usin 9 Xe $ fil Dc $ Rezurslou Fuce _ Aw Solue 9 ves prep' x

## Page 4

[HW] First Occurrence First Occurrence Given an array of N integers and a target integer T, design a recursive algorithm to find the index of its first occurrence in the given array: note return -1 if T is not present in the given array: Example Input T =20 2 3 10 20 30 20 30 Output 1 L23 Recursion Page

## Page 5

[HW] Last Occurrence Last Occurrence Given an array of N integers and a target integer T, design a recursive algorithm to find the index of its last occurrence in the given array: note return -1 if T is not present in the given array: Example Input T =20 2 3 4 10 20 30 20 30 Output 0 3 L23 Recursion Page

## Page 6

[HW] AII Occurrences AIl Occurrences Given an array of N integers and a target integer T, design a recursive algorithm to find the indices of all of its occurrences in the given note print -1 if T is not present in the given array: Example Input T =20 2 3 10 20 30 20 30 Output : 1,3 L23 Recursion Page 6 array:

## Page 7

Is Array Sorted ? Is Sorted ? Given an array of N integer, design a recursive algorithm to check if it is sorted in 0( ^ ) the increasing order. hae Stri 4) 0( ) (220-2; 1++) { Example 40 60 Input { lan €; ) / $ 10 20 30 40 50 folse , < 0w/ [1+17 Output True Gw ( ; ) 3 i0 < 2 0 2 0 < }0 04 , < 1-2 36 < 4 0 40 ( 57 kec $ Xl...0-,7 re + mve / Xo X| X[] = Xo 2 X | fslse X7u & X[] {5 +0 Sof ask nedc i xCi  0 'J "5 tno+ (heds 4 {+ is 4 #a K 's Sot X[;_0-] Xn-'} X;2 X i+1 %8 fl+ Ro?+ i~0 fto) Xn-1 Xo Jon) Pih tue Pto-' > { X-'} Xca-i__0-') t trak 4 7> Sos kd n-s 0 Rerunsiun Array #-(i=; stece : Gwct)) _ tetvra sotkQ Yo-' Y1 / Qor +ed dnbn$ Jbr S64d F;) Xir > p(o-) - {avolid 7g

## Page 8

n-s 3 bool flint X[], int n, int 1) { 1d 20 6 0 #or: @n) M base case if (1 = n _ 1) { 40 2 5 a f(u) te Space! On) 11 f(n-1) check if XIn-1...n-1] return crue; L 30 < Y0 {us)' twe recursive case fnena wwe 20 € 30 Jn4 #lt) f(i) check if Xli;:.n-1]is sorted return Xli] Xli 1] and f(X, n, 1); 10< 20 Jnd 36J= Nve Rerunsiun 40 i.e. Jnd f 7g

## Page 9

[HW] Binary Search Binary Search Given a sorted array consisting of N distinct integers and a target integer T, design a recursive algorithm to find the index of its occurrence in the array: note return -1 if T is not present in the given array: Example Input T =20 2 3 4 10 20 30 40 50 Output 1 L23 Recursion Page 9

## Page 10

[RJIHW] Ternary Search Ternary Search Ternary Search is an algorithm that is used to find the maximumlminimum value in an unimodal function. f() I(X) f(x) S m1   m2 S m1 L23 Recursion Page 10 ~m2

## Page 11

Analysis of Ternary Search L23 Recursion Page 11

## Page 12

[RJIHW] Peak Index in Mountain Peak Index _in Mountain Array Given an unimodal sequence of integers, design an algorithm to find the maximum element present in it: 10 Example 10 1 | 2 | 3 | 4 | 5 6 1 | 3 | 10 | 3 | 1 0 S m1 m2 L23 Recursion 12 Array Page

## Page 13

Merge Sort time : 0 (nlog^ ) Merge Sort spale: o(n) Given an array of N integers, sort it using the merge sort algorithm. Example 3 50 40 30 20 10 10 20 30 40 50 The merge sort algorithm operates as per the divide and conquer strategy and involves three steps to sort an array divide the array into two subarray around the mid-points recursively sort the two sub-arrays merge the two sorted subarrays Ttead ,fiead Sorte netq Sefte4 M= (S +e ) 7 5 < 0 e = ^-) 1 m - Stle-s ) 7 #(s,2) 5 n-i ) [S...m] M ~ S + (e-$ ) / Awv [Mti . e 1 2 3 Ki,mv) (asc TF2 ret e ) L23 Recursion Page 13 +l,5 Qak # (s-- e) Kewtsivc nerje ( $,m,

## Page 14

I~5 Sor+e4 L nt L=m 5 ott4 124 Jemt| tempt? Kz $ wij 0=6 2 3 4 5 60 S 40 J0 Lo (0 S-0 e =5 M-2 e ~2 M= | fs-3 e=s M =4 Es-3 &-4 m-3 #s-5 &-5 #s-o= e-1 M-0 e=2 Es-o ez0 ez1 e~2 e=Y L23 Recursion 0+ ( ) V<= e Xss' Ks {s-s Ks` Ps-' Paee

## Page 15

0 2 3 mZ 40 J6 Lo 3 Teo &-8 Me | { C+s ny 50 30 20 10 48 #seoe-i- #s-z &z Es-s 6-4 03] #s ea 6 0 20 |0 Mi0 40 s0 323 Y 2 {izo = Cz6 {s:' e2/ {-h &-y Yo S6 66 5"2 46 (0 20 30 5' 20 30 46 (? 6 Lo # L) fq #o LL 2 L3 Lk TQ ( . be has tni$ K+i leves = 2k = 0 (Lo + Lk) 2 K= Jog 2 log ^ + ) te e ha += log 2 Ied ^ L23 Recursion {ses &-> : 6 R 8 % Pjge

## Page 16

8tk + nerae Wnst @ome Iegn S Qacp Stk Jor s0 Rvomes s+k krome S + 0 ~ Oln ) Jan: & L23 Recursion Fage 16 pace

## Page 17

[HW] Reverse Pairs https l lleetcode comlproblemslreverse-pairsh L23 Recursion 17 Page

## Page 18

Quick Sort worf 0SC tae! 0 (4+) (nlogn ) Dn avq wrsh (JJC Quick Sort OCn) 6- 0n 0 9  Given an array of N integers, sort it the quick sort algorithm_ BClean ) Example 60 50 20 10 40 30 10 20 30 40 50 60 The quick sort algorithm operates as per the divide and conquer strategy and involves two steps to sort an array las+ 0 . partition the array into two subarray around the such uch inx tKrn all the elements in the left partition are the pivot all the element in the right partition are > the pivot as recursively sort the two sub-arrays piot S-0 Cea- { Rid> Portton (&r , (eP+ plo,^-) Pix~ ) P; $t Pijet e( e) Piet pitor Lf"e {eat Ifuondat j 3 { ret ) su j 60 50 20 10 40 30 nid 1 Pivot _ aw[2? T low md 2$ low low 75 1 6 ~ Su Le ) S tp (mrd Pivo+ ) $ 28 10> 40 80 7 drv(low); 10 'f 5 Wa p (owr Cmid Sai, JNJf J4 low ++ wd m Mr4+t ! else { 20 10 S0 40 Mra+F) IekF rien low Swp' p( Awte  aw(low)) 3 4 S 40 6o 2o Lo 3 56 Rcc ufsIcn /ele ~pace using pivoke + ( < s,8 ) / Pivt Tignt Plpnrti, {'ad Setha If ookom| 46 >e)_ 'p (s==e) wk 1e Gw Cmid 7 wd ivr=Onte 7 m'4 M' 20

## Page 19

40 2o Lo 3 56 na"t teph ~3 60 50 20 10 40 30 2 3   4 5 + 26 10 30 50 40 60 S.0 ee5 Pihx -2 62" 2 # low Sz0 e= | 8-3 e=5 Pse +s-1 ez | e- -1 Gase Cosc (mnb " #;' e-0 Ps-z e-1 Rcc ufsIcn /ele Pivot Pidxeo 0; Jx : | atoj )

## Page 20

[HW] Quick Select Quick Select Given an array of N integers, design an algorithm to find the Kth smallest element in it: Example K=3 0 | 1 | 2 | 3 | 4 5 arr [] 2 | 7 | 5 | 3 | 8 4 pi L23 Recursion Page

## Page 21

L23 Recursion Page

