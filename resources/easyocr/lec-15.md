# Lecture 15 (EasyOCR)

**Source:** `L15 - Pointers.pdf`

---

## Page 1

Intro to Pointers RAm 1kb 10248 32 - 6,+/40< ALeo) 102 L02 4123 64 . Jxe 16 46 26 40 Introduction to Pointers in C++ 1024 We can visualize the system memory RAM as a sequence of memory cells such that each memory cell is of 1B 8 bits and is addressable_ n-2 These addresses depending on the system and the compiler are either of 32- bits i.e. 4B or 64-bits i.e. 8B. Moreover; computer use the hexa-decimal i.e. the base-16 number system to represent addresses When we run a C++ program, portion of system memory is allocated for Ox program execution which is known as application memory: 9 06 main() { pPplenem"y in+ x=40, Iob L00 n-2 Lout 4 40 dovble Y= 3-14; {ou+2l 49;// z0 0 To know the address of a byte in C++ we use the address of ( & ) operator: When we print address of a character using the cout <<, C++ prints the contents of the memory stored at that address until it encounters the null character '0 Pointers in C++ A pointer is a variable which is used to store address of another variable_ 100 X (ict 1/ syntax for pointer deciartion 'at X - 10 ; L0 type name= 4b 27 >PY = &x, 90 /-6 xpt *) Since a pointer stores an address which are of 8B, in C++ we can use a pointer of one type to store the address of a variable of another type via explicit type-casting: Ado 48 200 iB int main() Id 64) 4 7 ch int 10; ptri (char: Loo Lod LIS Pointers 2 16 X "3 17100 8*; L00 Cint (tc) char 16; Fazc

## Page 2

ch int 10; char ptri (char char ch A"; Loo int  ptr2 int )Gch; L Ptr1 return C char *) Uio*) 200 Xout L} Py2; Dereferencing Pointer in C++ To dereference a pointer, i.e. to access the value of the variable whose address is stored by the pointer variable, we use the dereference operator 1oo I0 Io d 86 ia+ X - 10 ), 46 Xpb (in+r) 'at * xph { Loot 41 *; " 10 10 0 2ou+ 1 1 2 out L< xpi = / |0 ralve pt 4 516 = 512 + 4 4| 100 (Y+) 2 516 int main() { int 516; char ptr (char Ex; cout (int) ptr endl; 86 return Pl #) + 12 8 = 2 16 2   21 2 2"2' 2 32-bi UA= 6y+ 32 + I+ 8+4+2+| Rh LOJLOl7 1y- 31 16-23 f- 15 8 @ 4*6 244 B ' 3 -273/20 10 0 10 = %-b,b 662 (0 | LL (x)*Pk_ Ir 4 0 Ga #1 when WP Jer't + 1 ' what h2apeas 8ov ' & {a Qw Pointer Arithmetic 16 4 &ara (tt i5 Sta(e '^ A pointer variable only supports arithmetic addition and subtraction operations_ Moreover, in C++ we can also subtract two pointer variables_ "(0 4b 80 i0o LIS Pointers Lod Pk ? $7', xpb; % (Un0t 3*40 ((hnof#) Qo ut w 5 Jr aday o8y_ Yrad Faee _

## Page 3

A pointer variapie oniy suppors ariinmetc adaition ana suptraction operations_ Moreover, in C++, we can also subtract two pointer variables_ 4b 86 i0o #) 8'af X = lo 60 (im 10; 48 XQry int #xph =8,, ' 1/ 196 (out Ll xer; xpt ++; @t+D 1/ (in+ ) xpi xph + |. sizey L xpPr ; 1/164 i00 (0 4 xpr siuyGim) k Rt + const Pointer vs Pointer to const VS const Pointer to const Fn Lons+ Sn+ J -2', 22J 8+ 2 '7Io; X J xtef? xxr} vui Jt; 1] emr , ] $ Xr+ Works uut 4 *ph1 " {a+ xnef = X / xreftt I 12 Zou + l2 X 2{ *yf; Lonst int 8 > ref 2 = *; 11 evry xyetett; 4d 'at X = (a+) 10; iat * (0 Lou+ L2 +P+; I/w PY 2 Ptr^ Cict * ) mi++; (*pr1)++, Lov+ & $ 0*4) 1/ I #at ph 2 = Ipbztt (2 16o _ |m | LIS Pointers + /.4 {ou+ ;qki xpb + k read-palj Ioo 8*') 0t1 = Gat # ) 8*', Lonst Fazc

## Page 4

4/7 lpb2tt 0 ,B St 10 : Sot #Pt | 2 8*) Lpcft "aF 6} phz iar (oosrph 3 7 {ar V (*ph') ++, (= 'a+ 7 Xqt 8*) wrst Rat eh1 r LonSt Pc+ ~8*) (en)+rv {at * pry (*pw3 )++ Rn"^*' X X CJ boJ2 6 3) 62 tp3' 0r7 ) wcSt T0 QTY Ph ^o/t Pr Lng + Pointers and Functions Poss @lve piss void increment(int a) void increment(intu ref) ref C int main() int main( ) Mjja int int Pointers Ld"3 87') Pw3 Pt ( Wost 8 * ') ptri++; plztt = Phy)tt; RY 3++= Pks) ++ 8*') #Qti Pwy Qw} ph2 rit2= P w | + + (Y3 = 8x; ph ?t+ _ Wncy (*phz) + + pr3 +~, X ocSt (xeh w)+t Jfc & one-siJed analts Ucst a Wnst Page -

## Page 5

0 int maint) int main( ) Njio int int lincrement(a) ; increment(a); cout endl; cout endl; Ii1 volv € PossicJ possing adj' 61 % void increment(int  ptr) Ioo void increment intk6 ptrRef) aptr) ic ~ptiRef) int main() int main() int int ptr 6a; int* ptr Brd - exR increment (ptr) ; increment (ptr) ; Pw _ cout 755 endl; cout endl; Cintt Tetto 64 vobe int multiolylint 0, int D) {0 Inte multiplytint Int p) Int mulciply( Ert Int D) Int @00 nt Tocal int ~6; relocal Jole 4 return C OR retur 6C; int miint) int maint) 6i] int maint) cout mulciply(ze endl; cout mulcipty(?, endi; ccut Umulciply(2 endl; ECluEn ECtuEn 8E FAfuE Derg"ag Ref Fresten Don9 lng Ronkr Rosteo Tena ajay 6j voke Tef} - 6L rp int c; global Watiabin Int €; Tahle Int €; clobal vacfable Inte uultiplytint int b) Int Qultiolyt nt 0,int 0) Int multiptytin 0, int Di { 00 Lolut *8 FULuEt Lc fttucn 7 %vj Oo) Can) Int mainu) int maint) Int moin() cout Multiply(z endl; cout Multiply(? endl; cout multiply{z, endl; Tetucn 6 e Faturn Void or Generic Pointers A generic or void pointer (void*) can be used to address of a variable of any type. LIS Pointers adar int * add" Fage -

## Page 6

int main() char ch 'a' ; voidk ptr Gch; cout ptr 733 endl; (0d Ioo et 8) In Ct+, void pointers cannot be dereferenced. Null Pointers A null pointer is a pointer variable that contains the null pointer value and therefore it points to nowhere. int main() int * nullptr; int * int k NULL; In Ct+, null pointers cannot be dereferenced. 700 46 Pointer to Pointer In C++ we can create a pointer to to another pointer. *xph ; Zod 60 100 xel *#xxRh) int main() (int*) +# * xxxiw int 10; int xptr Ex; 3o0 int xxptr Exptr; 20 xxRh int xxxptr exxptr; LL return lint *+r) Pointers and Arrays int At[] = $ (,29, *,*9, In C++_ we can think of name of an array as a pointer to the element at the Oth index index arr value 20 30 40 50 address Koaya8 112 116 46 '%,ye 4 4T 2 4k + |  Grr [6] 3 100 220 0Ak 3 IL inkowlly #Ccr +0) = Anl;] RarD J 2 1by 100 +/. 4 QA^ +| x (cr +2) =anl() =30 2 Io 4 Yar(2 ? = G4 +2 +8 = a C, ) a LIS Pointers Vo;' 0 point xxl awl J=i (08 Paget

## Page 7

W 7 G4k +2 = O6m y +8 2 ar C, ) Q aw [6 ) ati I) ikowy am + L. 0 *Ar =10 +(Qh+1) =20 +(pr t2) .3d  10 (l [ 2) = % Since the name of an array in Ct+ works exactly how a pointer works, we can assign an array name to a pointer. 2 10 20 30 {n+x=i; Int Fain( ) (00 104 103 PkG) 9 +Cpn+i) Int Orr) {10, 28 , J0, 40,50, 60,  70} ; ia+9e*; nt Size0flarr) Sizeofiint); Int  ptr arr; b0j 1roj forlint 120; Ten; cout ptr [il Or #iptt+i) J retufn Pt Lict The difference between a pointer and array name is that while a pointer can be assigned a different address, the array name cannot be assigned anything: LIS Pointers brg / Vexy #ast 5i 204Cint ) hme 0Pzoron Ptco= Pt + +V 0wr +1X Fazc

