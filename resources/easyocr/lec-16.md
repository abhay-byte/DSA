# Lecture 16 (EasyOCR)

**Source:** `L16 - Pointers and Character Arrays.pdf`

---

## Page 1

Function Pointers Function Pointers 40 Lod 10 iat X = L0 Cin+) 'a+ # xP+r = 86 Loo 11 L0 Xpty Lout 2< xPtr ) Cint #) ascpty Jptr void greet () int addlint int b) bool ascending(int 0 , int b) cout 7< 'namaste" return b; return D; er"t / Areet add Jada aslendin) 4 scrnd  ^9 boR (+as-t ) ( ij)= Xastending ; oid (#aptr)( )= 8 9teet ; (+aph )(t) = Bada ; (tascpr )(3,2) ; inr 67 Gscendin5ls,1) ) (#ap+r ) ( ) 1 0h (5,+); ) Callback Functions Functions used as arguments to another function are called as Callback Functions _ int 0w() Hat QA[) = { s9,20,9 39,} void bubbleSort(int arr int n) { {at ^ = $; for(int i 1; i n; i+) { for(int j 0; j n i; j+) { 6" ) if(arr[j] arr[j+i]) { swap(arr[j], arr[j+1]; Xcw ( 7 awy; 7 Atj*1 Lo 10 36 46 S7 L16 Pointers and C haracter 87 ) (+aph ) (5,+) 444 dvee+( bobbie Sor t Anay{ Pace

## Page 2

Jcw ( / aw; 7 4)+ Lo 10 30 46 87 40 30 20 I0 aw $ awsti S 0w  bool ascending(int 0, int b) bool descending(int a, int b) { return b; IeEucn b; 47j50w5*1 4w " aw"*i void bubbleSorttint arI int n) { void bubbleSort(int OII, int n) { Tortint 1-1; i n; 1t for(int 11; 1n; 17+) foi(int j-0; j n i; ji ) { fortint j 0; j n i; j+) { (ascending(arr[jl, arr[j+1])) { if(descending(arr[jl, arr[j-1])) { swap(arr[j], arr[j 1]; swap(arr[j], arr[j bubbleSott 47', goscendcg ) / bo66leSecF (iw 0, 8aesdosny) ; bool ascending(int intb) retuin bool descending(int 0, int b) retuin b ; void bubbleSort(int 4ff int n, bool (*f) (int, int) ) forlint 1 1; 1 n; for(int j 0 jn i; j ) ifftarr[j], arr[j+1])) { /1 (*f) (arr[j], arr[j+l]) swap(arr[j], arr[j1]; bobble So+ (ew, ^ , 0$ 6u66ip Soi + ^, drcfndi 9" L16 Pointers and C haracter T1J; cead; Ct~) Anay{ Pace

## Page 3

Algorithm Sunday, 22 June 2025 11.07 AM 'at At [ ] = { 5 , 2o , ", 20,46} `o+ 0 = 205 3 D 20 30 49 Ow ( 7 70 Co, ") ^AS 61+2 ) Sorb ( L Zicst lost ) Aever % (~am) aw +n) [ 0, ^) Ll6 Pointers and Character Arrays Page 3 s )

## Page 4

Introduction to Character Arrays 20 u+L{ Gty 1/1 iat Gw [) = {19, 20, 30,*9,5 J; Introduction to Character Arrays A character array is a linear data structure used to store sequence of characters_ 58 id 26 Isolwln str 2o6 por(i+ i+; %~ 0 Ust LC arvr; , Lhav sh 51 < {9,0,4 "1 abcde Jb3e Lovt 2 L S , `4' ' ~'}; Uhar {'/, " ' Zou+ Ll I1 abcde A character array must always be terminated with the null character i.e. 'I0'_ Reading Input into a Character Array wn $ h ) ts W^ D0 9 <idd bosed @Te w' + aen avdak 0S 10 ) s ty S/2 € ~hen +i aui Chot Ita rs (' >7 sh) 17 ` o' '5 SmlJ aded I0o antomi (J1) Ll Sh Lour LI6 Pointers and C haracter Arrays string sk( ] sh ) 'staiob ch ous i^) Jad ['01] ) (hay cdll) Puje

## Page 5

Length of a String Given string represented as a character array, design an algorithm to compute its length we define the length of a string as the number of characters it contains excluding the null character. Input 'coding' Output 6 he () 0 lhz/ Reverse a String Given a string represented as a character array, design an algorithm to reverse it 4 D 2d Input : "hello" X Output "olleh" 3 + 7 4-s L 14 ) indexen staney ~ ) (Sm') ) F heversr (st , Compare Strings Given a two strings s1 and s2 represented as a character arrays, design an algorithm to compare them such that output 0 if s1 is equal to s2 7 a^_'a 10 LI6 . Pointers and C haracter Arrays 1 j 3 Q sN (2 Jl"itnn St +0 abc "1 Puje

## Page 6

UWUI LYI A}LI 'Jj O4 upyvuUu 4U IIL LI ! 4y" design an algorithm to compare them such that output 0 if s1 is equal to s2 abc " 1o if s1 is greater than s2 61 = 09491 if s1 is less than s2 Se - '1~ 22 0 S1 > $1 S, 7 S2 11 5, S, > 6 c d &f" Sz = S1 S, 70" s1, $ /-1 2 S1 [HW] Copy Strings Given a two strings s1 and s2 represented as a character arrays, design an algorithm to copy the contents of s2 into s1_ note assume length of s2 <= length of s1_ stvcp) 3' [HW] Concatenate Strings Given a two strings S1 and s2 represented as a character arrays, design an algorithm to concatenate append s2 to s1. note assume S1 has enough capacity to accommodate characters of both S1 & s2_ 5 0ba",, S1 > "J5; Kmfe $ S2 + $/ 71 (Oc() sh(at (S, S2) ; LI6 Pointers and C haracter Arrays "abc" 6cd v 5 1 4 JJs} Puje

## Page 7

tovp Li $1 , 11 abcd'{ String Tokenization Given string represented as a character array, design an algorithm to tokenize it based on a delimiting string also represented as a character array. Tokenization of a string is a process of splitting a string into tokens substrings such that consecutive tokens are separated by one or more delimiting characters. Example Input "abc def.ghi" and Output "abc" , "def" , "ghi" Qt (1 4b c. dej ah6 Iinl - (o Lela/delt F1 pt strtR sh Jlm ) U1at jhi lur LL Pw abc Rh shrtok (nul, dl,) Cu - LL prt ; shbk ( nu"l, Jl;m) Pt lut L( Rw ; "ah;" LI6 Pointers and C haracter Arrays (dn +) sh ( ) def"' Puje

