# Lecture 8 (EasyOCR)

**Source:** `L8 - 1D Arrays.pdf`

---

## Page 1

Introduction to Arrays lout LL OM[67 vnvetied / avo'd tcs Introduction to Arrays am^ [:] 0 <| 40-1 An array is a linear data structure, referred by a single name, which is used to store a sequence of values of the same type. Mzs iJx ero,4] arr 30 c' >7 ar [4J, idd 31 iJx e [9,0-') [out 24 4ns [ 3 4ms [2]++; Lout Ll A^a [ 1 ] ; 6A^ [ 0] = ido; How to declare an array in Ct+ ? 1 / syntax for array declaration lmtiguas type name[size] ; 6 a 206 When euer   Jov 2   3   4 a c(esJ 'nt 0 , i^ tne fldalm k" 46 46 46 46 46 qn ocig sts idx tco A=s tnot % * AAs C;] 's lact Tst tme Since arrays are allocated memory in a contiguous fashion, we can randomly access an element in an array using its index in constant time i.e. 0 (1) time. Array Initialization ID Arrays 1 ) ar) an^ [ 5] / Page

## Page 2

Array Initialization By default; when we declare an array in local-scope, it contains garbage value. inijifzet Iist int A[5] {10 , 20 , 30 _ 40 , 50} ; A[o] 209 2 ~3 AC J Ac? 10 20 30 40 50 4P 40 4d 46 40 Ac;7 02 | emi During the initialization of an array, specifying the size f the array is optional. During initialization, the size of the initializer list must not exceed the array size. int A[5] {10, 20 30 40, 50 _ 60} ; ewor What if the size of initializer list is less then array size ? slots int A[S] {10 , 20 , 30}; Renjiaing wi u 6 0 Hid zero 6 v) lues {oto aroy 1 = / tonshraints Snt amlio)) 11 67sp0 5 Uvask Rc+ Cia 0 3 4 $ EFKaI Lin)7 am (v )= ^-s cic>7 0w( ) (int (0; {4n;i++){ Gw(1j ' fov ~7 Gw(; 1' ID Arrays Page 2 wim Qadir] ^'/ 770 /

## Page 3

Ci^> 0w ( ) = Cin+ (0; {4n;i++)? Gio > Gwli) _ Jov ci)) GwG;), Ga >) aw(s)' (o>) aw (M1 ID Arrays Page

## Page 4

First Occurrence First Occurrence Given an array of N integers, and an integer T, design an algorithm to find the index of the first occurrence of T in the given array: note 2 output -1 if T is not present in the given array: Example Input : N = 5 ; T=20 T= I 0 2 3 4 10 20 30 10 20 %/p : -) Output : 1 L8 ID Arrays Page 4

## Page 5

[HW] Last Occurrence Last Occurrence Given an array of N integers, and an integer T, design an algorithm to find the index of the last occurrence of T in the given array: note 2 output -1 if T is not present in the given array: Example Input : N = 5 ; T=10 1 | 2 3 4 10 20 30 10 20 Output : 3 L8 ID Arrays Page 5

## Page 6

AIl Occurrences AIl Occurrences Given an array of N integers, and an integer T, design an algorithm to find the indices of all occurrence of T in the given array: note 2 output -1 if T is not present in the given array: Example Input : N = 5 ; T= 20 2 3 4 10 20 30 10 20 Output : 1,4 L8 ID Arrays Page 6

## Page 7

Reverse Array Reverse Array Given an array of N integers, design an algorithm to reverse it. Example Input 2 3 4 5 6 10 20 30 40 50 60 70 Output 2 5 6 70 60 50 40 30 20 10 i0 X3io/ {A} 20 40 50 60 70 Swp ( * ,1 ) 1126 Lout 2LY; 10 60 S0 40 30 20 10 'p 70 60 50 3 " 1 id 2 2 3 X w  20 4 PY 20 40 4d 30 ~ 2 ^ 5 (ar(,*1 , swip L 2 j i+4 10 20 Jat X 1 / 2 2 int 4 = 5 ; 5 o ia+ {at 6 = l0 , J = 20 ; 4 :4tb) b = Ra+ kemp , tmr 4 -6 ; ID Arrays Page J;20, 2 J; W |u luul 1= + Appr  Lot Gwij)) % (a+x 

## Page 8

LDJ Iae_ atbL | D - CU Ra+ kemp , tmr 97. 6-6; kmp=x, Q = a - 6 , 0 - 4 - & X = 9} V+6 Je kmi) X = Xl XaJ ^) 9 = X^ ) X ~ 52 Reverse in Range Given an array of N integers,  and two non-negative integers and where 0 <= i<j <= N-1 design an algorithm to reverse the subarray that starts at the ith index and ends at the jth index: Example Input = 2, j =5 2 3 | 4 5 6 10 20 30 40 50 60 70 Output 2 5 6 10 20 60 50 40 30 70 2 3 | 4 5 6 10 20 30 40 50 60 70 ID Arrays Page @+x)

## Page 9

Rotate Array Rotate Given an array of N integers, design an algorithm to rotate the array once in the clockwise direction. 10 Example Input 33 s 5 6 60 2 10 20 30/40 50 60 70 30 5o Gupe 20/+01_ (ar aws) Swip 6 , 70 10 20 30 40 50 60 (cw$ , On4 ) Sws| (uty GTy 5) Sw20 Swap (cw5, Gw2) 2 ~3 | 4 | 5 6 10 20 30 40 50 60 70 ow,) Swvz( SwoQ (ar , Gr0) (ow ; am ;- ) Swdp iiF 9 ; =^-1 + | K-Rotate Array Given an array of N integers, and a positive integer K design an algorithm to K-rotate the array in the clockwise direction: Example Input N=7;K=3 2 3 | 4 5 10 20 30 40 50 60 70 ID Arrays Array 3 J42 (6t1 , Page

## Page 10

Output 2 3 4 5 50 60 70 10 20 30 40 { + {+ #R*# N=7;k=3 . :.(o ) 2 4y 5 6 Tevetse 10 20 30 40 50 60 70 to 60 4o 30 20 /o rev dw [o.ki Tev awlk-L"v) n-k 50 (0 46 id 20 30 *0 N=7;k=3 2 3 4 5 6 io Z0 3 0 0 Tut0tons 10 20 30 40 50 60 70 R-l . 30 i0 20 bz|rot 10 p= Zrot 2o 30 20 k? 3 rot lo kz Urot 70 30 La Svt 30 i0 Lo L8 ID Arrays ^-) 30 Page

## Page 11

[RH[HW]Three Largest Elements Three Largest Elements Given an array of N integers, design an algorithm to find the three largest elements present inside the given array Example Solve tnrs "0 Otn) Input tae' 2 3 4 5 20 5 0 25 15 10 Output 15 20 25 L8 ID Arrays Page 11

## Page 12

[HW] Maximum Product of a Triplet Maximum Product of a Triplet Given an array of N integers, design an algorithm to find the maximum product of a triplet present inside the given array: Example Input 2 U 34 4 15 X Loxls 20 5 25 15 10 Output ' 7500 Input 20 3l 4 -10 "20 1 | 2 | 3 Output [ 600 L8 ID Arrays Page 12

