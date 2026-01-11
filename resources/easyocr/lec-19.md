# Lecture 19 (EasyOCR)

**Source:** `L19 - DMA and Algo Analysis.pdf`

---

## Page 1

Intro to DMA Peinters YMA Obj: Ur: Introduction to Dynamic Memory Allocation Reautsisn We can visualize the system memory RAM as a sequence of memory cells Linked List such that each memory cell is of 1B 8 bits and is addressable_ Jad 0 ueves Tets n2 Fwie Greph When we run a Ct+ program, a portion of system memory is allocated for program execution which is known as application memory: mjial ) { M(Mdij ;at x= %o; n-2 48 The application memory is divided into four segments Lode sB Code or Text to store program instructions GlobalStatic to store global and static variables loba | 2 5 B Loo @ Stack to store local variables Heap or Dynamic fxd Stack S0 9 200 tear / Dynom;e able Stack Segment The memory allocated for stack segment Of appiication memory is fixed. The size of the stack frame for a function must be known at compile time_ The process of allocation and deallocation of memory is handled by OS* intk f() int 10; return 6X; int main() intk xptr f(; cout Kar xptr 735 endl; L0o aia return (iat+) Stack Heap or Dynamic Memory Pr aew 7T7 The memory allocated for the heap segment is dynamic in nature_ 5 The programmer handles the process memory allocation and deallocation. LI9 DMA and Algo Analysis Rs S#k ?Pe)"_ Pacd Hypk Pupe

## Page 2

The memory allocated for the segment is dynamic in nature_ The programmer handles the process memory allocation and deallocation. maial ) { iat * ptr aew {t; idd 2 #Pt i0r 40 +L m) nain Ptr Cicnt # Stack Heap Memory Leak mjinl ) { 48 in} Pt 2 alw iar) r PttT = 5) 1co 40 Lout X1 * Ph ; 1/5u 50 Main elete ph ph pt 3 in+ ) Gat*) Stack Heap int f() { int xptr new int; xptr 10; Xptt Cim #) 1o return xptr; ido 40 int main() { int xptr fu; liat# ) xpwv ; Stack 66 1D arrays on the Stack or Static Memory knwn ot em Hce An array is a linear data structure, referred by a single name, which is uskd to store a sequence of values of the same type_ aw[s1; 11 syntax for array declaration type name[size] ; In C++, we can think of name of an array as a pointer to the element at the Oth index LI9 DMA and Algo Analysis heap 5 1 Lvvl 200 alw Xph Zout 42 Heap shovld Pupe

## Page 3

206 index arr value 10)720 30 40 50 addreks 10 10/ 408 112 116 48 46 46 40 #0 rett = C6 ] At 7 4ry [6) X (4rr+1) = Cw6,) latr+1) = derr6 2 (Grr4 1) 7 arr[17 1 (at+ &) 7 J aw (1? 7 e[;1 Aw C,) * (Sr + ; ) 9 Oty + 0 . 5110 3 (i+ ` 1D arrays on the Heap or Dynamic Memory 6R-Kme Tua-hie 1/ syntax for array declaration on the heap memory type ptr nel type[size] ; 'a* PN = alw int [51) % |o OT #Pir =i6) Zup +pl +i) = 20 , & MOj-rai (ia+ # ) 30) % 30/ Stack Heap Art+} ) o (T [3 ) = LD) ( Rr+Y) So * 50, It A* [4) = 52; By default; when we declare an array on the heap memory, it contains garbage value_ intk arr new int [5]{10 , 20, 30 , 40 _ 50} ; During the initialization of an array created on the heap memory, specifying the size of the array is optional: Also, the size of the initializer list should not exceed the array size_ To access elements of a 1D array created on heap or dynamic memory, we can use the same syntax that is used to access elements of a 1D array created on the stack memory Dynamic C: (a0.4 vet LI9 DMA and Algo Analysis Gt $ ; ) = Prto J:i Pw [+7 : (prr+2 ) = Array Pupe

## Page 4

Dynamic Array C: c?p.] It an array created on the heap memory that can grow at runtime_ size % vect . C-0 6<0 upY {8 ~6 01 C-2 622 br) 40 C=4 l7? I2. 2| #0 S6 Ick Ise/ F2X 'Spx, C 8at ( = | ) 30 {n+ A 7 ^e w in+[c2) Jak (tve ) 5 'a+ *) Lic>X , 6reak ) # { H/~ e $t ze Ar;j = * 8 L0 lo lw |ze(xo| 1 |1 LI9 DMA and Algo Analysis vet {-Z8+ ;~ = wAile  (x<0) $ ( < ==:) ++ ) Pupe

## Page 5

lo 1e Isa/y/ 1I C=4 resile Io 20 40 10 0 C = 624 J  X?50 2D arrays on the Stack or Static Memory 2D-array is an array of 1D arrays, referred by a single name, which is used to store a sequence of values of the same type and can be visualized as a matrix: 11 syntax for 20-array declaration type name [rows] [cols] ; 2 10 15 20 25 arr 30 35 40 45 50 55 60 65 1 | 2 arr 10 15 20 25 30 35 40 45 50 55 60 65 100 104 108 112 116 120 124 128 132 136 140 144 arr[0] arr[1] arr[2] LI9 DMA and Algo Analysis [0w2() Pupe

## Page 6

2D arrays on the Heap or Dynamic Memory 2D-array is an array of 1D arrays_ LI9 DMA and Algo Analysis (nwpr) Pupe

## Page 7

Algorithm Analysis Algorithm Analysis The analysis of an algorithm is done in terms of the time it takes time complexity and the space it consumes (space complexity) to perform its operation. 77 0s,5s,15 OCa' ) Set( - ) 0 (  nlja) sot 0,') 2 67a) Jap_ The analysis of an algorithm is always done in terms of the input size. Moreover; we mostly interest in the worst-case analysis and use the Big-0 notation to report the worst-case time and space complexity of an algorithm: 1L L 0 b est Gv) Wusr C?Se LasC (,sc To analyze the time complexity of an algorithm, we've to first identify algorithm type Ll9 DMA and Algo Analysis Page

## Page 8

Iterative contains only loops ) recursive contains recursive calls neither iterative nor recursive mostly take constant time i.e 0(1, To analyze the Space complexity of an algorithm, ve to analyze how much extra space or auxiliary space the algorithm consumes with respect to the size of the input: Ll9 DMA and Algo Analysis you[ Page

## Page 9

Time Complexity Analysis of Iterative Algorithms Time Complexity Analysis of Iterative Algorithms Kme #nkohos = 0 void flint n) { forlint 1 1; 1 n; i++) { cout 30 73 bns+ ^6mh 6( ) void flint n) { forlint 11; 1n; i++) { forlint j 1; j  n; j++) { 116 ~ Oln1) MC cout C S void flint n) { 20 _0 int 1 1; 4 int 1; 3 whilels n) { 1; 3 6 4 5 Ja. bas} br J ) 20 _K k W fshe 42 40 k-/ Kat$ k2 = 0 i45 k < J^ LI9 DMA and Algo Analysis 1 @nst KlKt) ) ~k? Page

## Page 10

void flint n) { forlint 11; 1 1 K= n; it+) { cout Joswrst : 0(J ) slars void flint n) { forlint 1 1; 1 n; i++) { Ix ) for(int j 1; ji; j++) { cout 1t2 2 ; + 3 1 2 - ^ (^ +,)~q :@CJt D(n+ ) t 7 #stars void flint n) { 12 for(int 11; 1 n; i++) { : 4 + 42 for(int j 1; j-iti; j++) { 2 2 cout ^lo+1) (2n+,) C 3 ` 3 1 h }' 9 3. Onst 0 (0s ) 2 k 02 '2+1 void flint n) { 2 i 2^ ? forlint 1 1; 1 n; ik2) { cout 21 = 2 2n 9 2" = 4 20 ? 8 2K. 0 logf: bnsy :~o( lon:' K= Jos ? 16 tue Kti 2n % 2 k plse Ll9 DMA and Algo Analysis 1 + 2' 9 Censi 2  = 2 Y = Page

## Page 11

20 ? 57 |~ 4 #lse Ln SF 2 { ~'e5": s+6 void flint n) { 1< Ximt $ fortint 1 0/2; 1 n; itt) { for(int j 1; j n/2; j++) { (qt1np2 ) for(int k1; k n; kx2) {7 cout Ioj R void flint n) { for(int 1 n/2; 1 n; it+) { forlint j 1; j n; j -2) { for(int k 1; k n; kx2) { Ioj  cout 1o52 CnS+ 1"6^ 1%3^ 6( =n 22/-0 6 void flint n) { 717v-0 while(n 1) { n /= 2; Uori 2 n?^/2; 3 7 1 ? Unst 0( 195^ ) Slsc 2k= n K Kmcs Kz1q3 Ll9 DMA and Algo Analysis 26 " a ^0"s~) ) 2. 3 3 Is~ Page

## Page 12

void f(int n) { forlint 11; 1 n; i++) { forlint j-1; ]  n; j+-i) { 1 + 0 3 cout 4 + 0 ~12 +< 8 .4+475 " 3 1 + 0 2433+" 3 4 +0 1-4 6 ( n: Ivy? 1+2 int flint arr[], int n, int t) { int 0; int n 1; whilels 43 e) { int 5 (e 5)/2; if(arr[m] t) { return m; } else if(arr[m] t) { m 1; } else { 3 m+l; return-1; void f(int arr[], int n) forlint 1 1; 1 n; 1+) { for(int j-0; j n i; j++) { if(arr[j] arr[j+1]) { swap(arr[j], arr[j+1]) ; Ll9 DMA and Algo Analysis 2 ~ 3 Page

## Page 13

void flint n) { cout C4 n 10; hme? 6( 1 ) Ll9 DMA and Algo Analysis Page

## Page 14

Space Complexity Analysis of Iterative Algorithms Space Complexity Analysis of Iterative Algorithms ^-1 #nes ~1 2 + void flint n) int int if(n 0 ||en = 1) { #ime : Oln ) Teturn n; 0 . @ns+ forlint 1-2; 1 n; i++) { dli ) int a+b; b; Way C; return b; Lt 35 void flint n) { = " Gt +x DEL forlint 1 (; 1n; i++) { int arr new int [n]; kATICD sQace: '2 O(n+) 623 ~ ^ LI9 DMA and Algo Analysis Page 14 shre e :

## Page 15

void flint n) { (int 1 0; 1 n; i++) { 5 pa 41 ! int arr new int [n]; delete [] arr; LI9 DMA and Algo Analysis Page 15 u(^ ) for

