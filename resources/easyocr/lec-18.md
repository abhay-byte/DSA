# Lecture 18 (EasyOCR)

**Source:** `L18 - 2D Arrays.pdf`

---

## Page 1

Introduction to 2D Array Introduction to 2D Arrays A 2D-array is an array of 1D arrays, referred by a single name, which is used to store a sequence of values of the same type and can be visualized as a matrix 3 iat 0w [J[4) 10 15 20 25 @ODzzk Bobolekd (2INTEK 7 3 0+7 3 30 35 40 45 50 55 60 65 m = 3 (o +2 ) 3*4 9= 4 (o + > ) 12.4B = 480 (wontjuos) How to declare a 2D-array in C++ ? 'nt am [}J[4); 1/ syntax for 2D-array declaration type namelrows] [cols]; 2D-array is allocated a contiguous block of memory to store its elements_ 2 10 15 20 25 12 iot X 46 30 35 40 45 50 55 60 65 480 3x4 This allocation of contiguous memory is done either in row-wise manner a.ka row-major order or in a column-wise manner a.ka column-major order 480 Row-Major Order 2 3 10 15 20 25 30 35 40 45 50 55 60 65 16 | 16b i66 T0 75 20 25 486 30 35 40 45 Column-Major Order 50 55 60 65 3x4 '2 1 | 2 10 30 50 15 35 55 20 40 60 25 45 65 LI8 ZD Amays Page the

## Page 2

26 126 126 126 Accessing an element in a 2D array ann 10 15 20 25 2 | 3 1 | 2 MB 30 35 40 (45 10 20 25 30 35 40 45 50 55 60 65 50 55 66 3*4 45 4nk (2)[2) Gw [o JC'J AAA[ ) [s] 7 ^ aw6) {t J0 Atay 0 J^ Aw0 ) 'at 'ar 0,,,2,3 M=3 (#tois) L 041 4M-1 1 = 4 ^m [;J[j] {o 0 , 2 Since 2D-arrays are allocated memory in a contiguous manner; accessing an element in 2D-array is a constant time i.e. 0 (1) operation: 2D-Array Initialization By default; when we declare a 2D-array in the local-scope, it contains garbage value 2 int arr[3] [4] {{10, 15, 20 , 25} 10 15 20 25 {30 , 35 _ 40, 45} , arr 30 35 40 45 {50 , 55 _ 60 65} } ; 50 55 60 65 3 *4 During the initialization of a 2D-array, specifying the no. of rows is optional While initializing a row in a 2D-array, the size of the initializer list must not exceed the no. of columns in the 2D-array. et' int arr[] [2] {{10 , 20, 30} , {40 , 50}} ; What if the size of the row initializer list is less than the no. of columns ? int arr[] [3] {{10 , 20  30} , W'tn {40 , 50}} ; 6 < Zew $' LIS Page (#cins '0i^ vaioit;alized Aird Oiu Arny

## Page 3

aw [1J[4] 'at {,}; memsu (4w, size%lr)) / L > ; 4ASTo )[o ) 2 41s [67 [(] Tow 25 QAA [+) [+) 72d, ' , 2 Gm 137 ^*3 QASTIJCe ) TdW (i-o ; zm., '+1) 5 41s [12 [(] Jor  4m [1)[2) AAA[ OJ[o ) Gm 0 4J137 41^ [1J ['] AAR[ZJ[ ) 20d row Qa^ [1J( ) 045 [22 ['7 Gm ICJ137 4x [27 (2) am [47 [37 Values '0 2 $ - Arra ] rals n 2 i0 1 < i0 wnstuias on Rat an Cw J[1)/ m ~ 3 1 = 1 {4+ m,9', 3 4 = L #liso, m,i++8 5 j++2{ 4 +lj-,j-~ Gw6 )67_ Iv Xiv LIS Page 5 } | T07 Rendin]) (rsto 'bosed m77) (in>) Cic>7 Arny

## Page 4

Wave Print Wave Print Given an integer matrix of dimensions m x n, write a program that prints the matrix in the wave form: 3 Example Lo 1$ lo es Input 3 0 5s 0 2 0 10 20 30 Ss 4s 40 50 60 2 70 80 90 Output 3x3 10 40 70 80 50 20 30 60 90 LI8 2D Page 4 Arrays

## Page 5

Transpose a Matrix Transpose a Square Matrix Given an square matrix of integers of dimensions n X n, write a program to transpose it. 2 3 2 3 12 13 15 19 23 6 Zu 2 2 3 3 Input Qutput 2 1 2 3 4 $ _ + ^- | 0 2 + 0-i 2 1 3 Y~i { 5+ ^-i ( +o-i 04 | < 0 nxo I+1 $ ^-) LI8 2D Arrays Page 5 8,8 0

## Page 6

[HW] Rotate Image https:]Ileetcode com/problemsIrotate-imagel LI8 2D Arrays Page

## Page 7

2D Arrays and Pointer 8t at(] ={10,20, 30,40, w } Pointers and 1D-arrays In C++ we can think of name of an array as a pointer to the element at the Oth index 20d index arr value 710 20 30 40 50 addre s 108 112 116 Sar[o ) Ks + | 6 A (owm)-arG 2 Gas+| Sarr C,7 (om12 ) = Arrl? Uiakmo"J Aak+2 2 darr (2 ? Io0 + 1. Sizeyli+) = =(0 4 Iv0 8arrti ] AAa + t Ga+ ) 0ny + % * sizey Pointers and 2D-arrays 0 ! 2 3 0 40 1S Lo 297 2 | 3 2 | 3 1 | 2 1 30 35 40 457 arr 15 20 25 30 35 40 45 50 55 60 65 104 108 112 120 124 128 136 140 144 sS7 6' 4f Sxy arr[0] arr[1] arr[2] Ctr (0J (0) awr [1 ) [0] Sar (1 216 ) Gtr + 2 awtI 106 + ?' (4.4) J 2 QTy 2 132 (00 l (44 2" 6 arr 10 715 20 25 35 40 45 55 60 65 Ar [o) + 2 704 '108 112 7672071244128 532 136 140 144 atrty 0 ^ e arr[0] arr[1] arr[2] Ilo + 2Y a ^ ior Xar [o JC ] fnkrmll- arC;) + J * $iz3lw) J c Gtru) n+ %nkroail) AaX + , Sizcy (row) LIS _ ZD Array; PlEc an67 Kat = Ow (i ) (ow +2) + 1.4 2 5 0t + | awtl C2J+3 +1.((4+4 132 + 3.4 = towS Gtu y (0 8 0AK [i)

## Page 8

int %nk roai/)_ i, sizcd Gw) am + Cui" RAS Y+) J ^ Gtvo $ tows the 'm foln at[;Jcj ? 1`3' + at +8 2m Tol tbe 2 40 (ar +?) aw T; ) U) to tnp 3 arT; ) + ) Jh j8 * aw LIS _ ZD Array; Plrc * sizeed #wins Size 8os  de vh Win tne 'a8 i0t Gn 1;] +) ) C;) Cj )

## Page 9

Matrix Search Matrix Search Given an integer matrix of dimensions m X n, and a target integer T, write a program to search for the target in the given matrix Example Input : T = 10 t -F 0 0 0 2 50 80 20 'e' fvlse 90 10 70 2 60 30 40 Output ' True LI8 2D Arrays Page

## Page 10

Sorted Matrix Search Sorted Matrix Search Given an integer matrix of dimensions m x n, which is sorted row-wise and a target integer T, write a program to search for the target in the given matrix: Example Input T =50 Slvo k Over Tows ) m Ipj 40 50 60 6 ^079 10 20 30 'r'j Spartn 70 80 90 R((h Tdw + 60 Output True #ox t aw ( 1 { I0, Lu 30 4 0, S0 5 n+ ^ + 5 2  3 awv 2 6 30 | 40 50 (0o To 4 T0 8 02 ub 120 anr+0 2ud [o,) s0rc ( at ) Mat(102 v 8 4@ nxn Motl; ) ntlitiz ecd 8ttt = matli J ~arr ,J+0 LIS 6 Yatth Cmr +0,+) binoryJ - 8hatr ATys Puge

## Page 11

Sttt = ma+ti ] m? +X;+ 7 01 end 3 ^ot usp4 2 3 0 3 2 @Ec@lc 3xy 1 %-li_iv-1 H6-L An[a7 atlv) Ioxio LIS ma+th)+0 4+67+ ( L-L ATys Puge

## Page 12

Sorted Matrix Search Sorted Matrix Search Given an integer matrix of dimensions mxn which is sorted row-wise and column-wise and a target integer T, write a program to search for the target in the given matrix: Example Input T = 50 5' 60 40 80 20 3 0 40 $ 0 10 20 30 10 40 50 60 70 80 90 F mXn Output True Ibs (mn) t- 55 +0 30 30 25 > 6 0 I0 2 0 10 20 25 sosk 4 Stairese Sesrb) 0-| (30 J? nxi; =-t? 2 No Yes tve tznof;_ ret nxn = &)m"ij L*+ 12 m  > =0 Soxkd 50 1^4 Vhi | 0 ^n"

## Page 13

[HW] Count Negative Numbers in Sorted Matrix https [Ileetcode_com/problemsIcount-negative-numbers-in-a-sorted-matrixL LI8 2D Arrays Page 13

## Page 14

[RJIHW] Spiral Print a Matrix Spiral Print a Matrix Given an integer matrix of dimensions m x n, design an algorithm to the matrix spirally in a clock-wise direction: Example Input 2 3 11 12 13 14 22| 2372 2 24 26 25 3 Output 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 2 3 11 12 13 14 22 23 24 15 2 21 26 25 16 3 20 19 18 17 LI8 2D Arrays print Page

## Page 15

[RJ[HW] Diagonal Traversal Diagonal Traversal Given an integer matrix of dimensions m x n, design an algorithm to traverse the matrix diagonally_ Example Input 12 13 15 _ 16 _ 19 22 Output 19 15 20 11 | 16 21 12 17 22 13 18 14 11 12 13 14 22 23 24 15 21 26 25 16 20 19 18 17 LIS JD Arrays J41 F r

## Page 16

[RJIHW] Diagonal Sort a Matrix Diaqonal Sort a Matrix Given an integer matrix of dimensions m X n, write a program to sort it diagonally: Input 2 0 5Q 80 w/ 30| 2 60 30 Output 2 0 10 20 30 40 2 6Q 9_ 50 LI8 2D 16 Arrays Page

## Page 17

[RJ[HW] 2D Prefix Sum [HW] https [Icses fi/problemsetltask/1652 2D Prefix Sum You are given a 2d-array of MxN integers, and Q queries, each of the form (1i, ri) and (lj,rj) where 0<-li,ri<-lj,rj<-N-1. Your task is to find for each of the Q queries sum of all elements within the submatrix defined by the top-left corner (1i, ri) and the bottom-right corner (1lj , *j) Example N =5 Q =3 2 3 4 2 3 | 0 | 5 Qo 0 | 0 | 1 4 9 3 2 Q1 1 | 2 | 3 4 2 6| 8 1 0 4 Q2 2 | 0 | 4 | 1 3 L5 | 4 | 2 3 4 | 0 T 6 | 8 T 6 | 1 LI8 2D 17 9 | Arrays Page

## Page 18

MxN 2 3 4 1 | 2 | 3 4 2 3 0 | 1 | 5 4 3 2 2 6 8 9 0 4 2 3 | 9 | 5 | 4 | 2  3 3 4 | 0 | 6 | 8 | 6 | 1 4 LI8 2D 18 Arrays Page

## Page 19

MxN 2 3 4 2 3 4 2 3 0 1 | 5 2 5 | 5 | 6 11 4 9 3 2 6 16 25 29 36 2 6 | 8 0 4 2 12 30 40 44 55 3 9 | 5 | 4 | 2 3 3 21 44 58 64 78 4 | 0 | 6 | 8 | 6 | 1 4 21 50 72 84 99 LI8 2D 19 Arrays Page

