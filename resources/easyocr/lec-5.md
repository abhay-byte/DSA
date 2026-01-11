# Lecture 5 (EasyOCR)

**Source:** `L5 - Intro to C^M^M.pdf`

---

## Page 1

Sum of Digits Sum of Digits Given a positive integer N, design an algorithm to find the sum of its digits. Example Input N=123 Yxo I+2+3 = 6 Swm 2xy 6 Output 6 Input Ns456 4+5+6 = IS Output 15 Gumedx w 4 1 L5 Intro to C^M~M Page

## Page 2

Reverse a number Reverse a Number Given a positive number N, design an algorithm to reverse the number. Example (1 0 10 1)_ 5 ( 21 ) 2 Input N = 123 Output 321 2'222' 20 Input N = 456 i6+D+4+ + | Output 654 1 5 ( ) % (10 : ~1 ): 5 ( ? ) w @Okxio = /X2 + 0 dxio @xio + % 0 B2xo + 3 312Xio + = 12 3 Vr ;218 Ls J05 0 * i0 + 6 %p 6 5 4 6*1 + 5 6 5*10 +4 6s4 L5 Intro to C^M^M ox2 + { 2 *2 + =iXid + 2 ~S*2 + = oX 2 + | = 2 ' Ie/j Page

## Page 3

Variable Scope Variable Scope In Ctt, scope of a variable can be thought of as the visibility of the variable. In general, a variable can either have a block scope or a global scope. Block Scope variable declared within a block {} ) has a block scope i.e. it visible / accessible from the point of its declaration till the end of the block. We call variables with block scope as Iocal variables. Global Scope variable declared not within a block {} ) has a global scope and we such variables as global variables. int main( ) { int X 100; 11 global variable l2 X; /1 int X 5 10; 11 tocal variable int main() { 00 cout 4< X 4 endl; J) 10 cout X endl; return 0: return 0 ; Variable Scope Resolution LS Intro to C^M^M Page 3 Any Any call (woy <out _

## Page 4

int main() { int 10; cout < X 4 endl; 10 int y 20; cout X 4 2 endl; L0 Z0 Zoul 2 & X ) /1 40 return 0 Loul 2 L 92 Il € mst int main() { int 10; cout 4 X << endl; 710 int X 30; int y 20; 30 20 cout 4 4 endl; Zout 62 x) w 10 return 0; LS Intro to C^M^M Page 4

## Page 5

int X 100 ; 1/ global variable int main() { cout 4 4 endl; 10 0 int X 10 cout endl; 10 int X 30; int y 20 10 cout 4 endl; ou+ 2e *) I1  1 return 0; Scope Resolution Operator [ : : ] One of the use cases of the scope resolution operator [ ]is to be able to access a global variable when there is a local variable with the same name int 100; 1/ global variable int main() { int X 10; 11 Local variable cout endl; "X ? 10 cout endl; return LS Intro to C^M^M Page 5 3 0 :t'j

## Page 6

Static Variables Voy local vay ~ global: 8 Cope sule L' Blec dvraho 2' automzhc 2 ' |TuvJ+o0 block Supe Voy tne bi6UL w/i oS 'ot 3 '48 0$ Ia+ 9) biocjus C vsibilty 's 4i; DS ;a tne 4> Ions Js (cj zeso +hej iit ( oni) LS Intro to C^M^M Page 6 9lo 631 Stab'c Stahc dvrhoo Stahc vis,8;= S000 *1 4 27/1 Ovet Stahc 6loc L tne mem' temjins tun $ ' /albo) Stahe 6) Jyfovt tuio Wn - Ote Vo Y - gtahc once

## Page 7

Fibonacci Numbers Fibonacci Numbers 6 8y 3 = 8 70 5 + Given a non-negative integer n, design a algorithm to find the nth Fibonacci number. 124 1e8 21 177 5 "Jp : 3 f (n)| 0 | 1 | 1 | 2 5 13 34 -#b- $ + 1 = #4++ f-2 07 2 | Lout 2L 0j 1;2 else { 0 2 6 3 '~po} " 0 Ast b : | /) 1st = "c= a+6; 11 2" 4m 4 = 6 ) {-c) 6-b ') 6 - c / r r - 4+b) )) wkh L5 Intro to C^MAM Page scv " 9=- ) { }( Q==0 714  4 - 0 // otn 5244 ~rd 3r0 2r4 ~C= a+8) //3*4

## Page 8

L 6 ` C / C- 4+6, ) 4m L5 Intro t0 C MAM Page

## Page 9

Largest of N numbers Largest of N numbers Given N integer values, design an algorithm to find the largest of the N numbers. Example Input Nas ~-PX & Output 8 L5 Intro to C^M^M Page Isf :

## Page 10

Controlling Loops in C++ Break Statement The break statement is used to pre-maturely terminate a int main( ) { while ( _. ) { int count 0; int data; while(true) { (3. { cin 7> data; if(data < 0) { break; kcek; Bceak count t "'ner cout 4 count endl; return 0 ; Iwp Continue Statement The continue statement is used to an iteration of the loop. 0<5? iexLx Xs 5 LF int main() { 1<52 - int 1 0; 225? - Whileli < 5) { 1 1+1; if(i S 2) { I-3 22X continue; V DP: 4 ,3,4,5 Sksp cout << 1 << } 2.22 * return 0 ; LS Intro to CM^M Page 10 loop. waile Ju Uhiic skip 3 <$ 9 2 : - 2 2 4222?X 5 22% *

## Page 11

Ternary Operator in C++ Ternary Operator in C++ The ternary or conditional operator evaluates a condition & executes a block of code based of the result of the condition. Palx condition expressioni expression2; int main) { int main() { int marks; int marks; cin 55 marks; cin 72 marks; if (marks 2 40) { marks 40 cout 4 "pass cout "fai" cout 42 'pass" return } else { 410 & cout << "fail"; Pskse return 0; L5 Intro to C^M M Page [  tiue

## Page 12

int main() { int 1; cin 2> 1; int j; int main() { if(i%2 95 0) { int 1; j = 1; cin 22 1; } else { int j0i%2 S= 0 ? 1 : 0 return j = 0; tvve return In C++, the ternary or conditional operator can be nested i.e. we can use a ternary operator within a ternary operator: int main() { int n; cin 57 n; int main() { if(n > 0) { int n; cout 4 "+ive" cin 5> n; } else if(n < 0) { cout 4< "+ive" 0 cout 2 "-ive" ; n < 0 cout 4 "_ive" cout 44 "zero' } else { return 0; cout 44 zero" return 0; L5 Intro to C^M^M Page 12 0;

## Page 13

[HW] Check Fibonacci Number Check Fibonacci Number Given a non-negative integer N, check if it is a Fibonacci number. n 2 ~3 4 | 5 6 8 9 f (n) 0 | 1 | 1 | 2 | 3 | 5 13 21 34 Example : Input : N = 1C Output ' false Input : N = 8 Output : true LS Intro to C^M^M Page 13

## Page 14

Check Prime Check Prime Given a positive number N (>1), design an algorithm to check if the given number is a prime number: 2 3 4 5 6 + 8 Example 2  3 1-9 Input N =5 Output true Input N =4 Output false number n is & prime no. if it is divisible by only 1 & the number itself: LS Intro t0 C^M^M Page 14

## Page 15

Square Root of a Number 1 Ja 7 0 2 ( ) 2 2 Find Square Root Given a non-negative integer N, design an algorithm to find its square root. Example 22 S Input N = 64 Output 8 Input N = 30 J J36 Output 5.47 4 (y:2 49 1 82 (6y = 8 Jy - 3 181 = 9 fib = 4 2 $ 4 4 252~ 6.02 < 422v 9-42 L.12 < 422v LS Intro to C^M^M Page 15 J2s 425 7 2 4 25 7 22 42s ? 2s) L 37 < 425? " 2 4 25? X

## Page 16

Ja $ = 6 < 422v 2 < 422 X LS Intro to C^M^M Page 16

