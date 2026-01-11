# Lecture 4 (EasyOCR)

**Source:** `L4 - Intro to C^M^M.pdf`

---

## Page 1

Introduction to C++ Introduction to C++ The extension of C++ file is .cpp HLL LLL 010101 compiler cpp 010101 010101 source code machine code preprocessor compiler 010101 cpp 010101 010101 source code machine code What is a function ? In Ctt, a function is a group of statements which upon invocation or calling performs a task In general, you can compare them with mathematical functions f(x) = x2 ft) 7 4 qjme 2 . or Mo re Atjs' g(x; y) =x2+y2 3 . task 3 I3 4' 1 &tt fa (n Ye 7 41 0 67 4 mi: Baif 911 ihs stots are cxeWtrd Js J5 Jov #include<iostream> et . It; Sh+ ajme P~t; tne bdj * namespace std; te fc, 3#+pe Int] main() 26t a*35 ~ $ eds fn bod) cout 'Hello World" have mbixpik return  +  9 fn Cjn As sn J5 n8t = #C Ist Ju the fn erdu - Oat incerhon Chazoder %p Dpry Lout L 40 thrs fo "5 Kout 22`X ) Ya Lout 4< Jyned tnk 's Lovt LL 3.14) fa (ai1 fi le LL (0 +20 ' (but LZ trve; 11 4 2out ~f 2i faise . h) MMr f() J(2,3) d (4,5) Sdon 'using tne Smt. e Wlnkt tor Ieam ^ Dodes

## Page 2

<out L2 trve ; 11 4 Zout Zoot 2l favse ; Comments in Ct+ A comment is a line of text which is used to document a program and is ignored by the compiler_ mineluderiostreanz #includeziostrean> usine nonespoce std; Using namespace std; {ot Main( ) int maint) chls rnulei-line comtent this i5 single-line comment chis mutti-tine coiteng chis multi-Line comment cout "Hello Vorlo; cout "Hello Vorld; IetUIn 0; TetUIn 0; 16 = 8 6its Reading Input in Ct+ '+ - 48 (32-bik) Siu Gleat ) 1B (6-6 ,+3) sizeef (int) 9 fundommsl Lhor tpe Heat 4 4B (s1-bits ) char ) Siney duusk ) Jouble 4 86 ( 64-si6) Size d foe| 7 16 (6-6,5 ) String 521/0 // Size y bool ) Vjt_ajme tnu type 7 (1010) 2 Syntox for (40)0 vtm'tsle 0 0 . id /0 (;a+) iat X 28 46 has (uwor _ 6 / Lhar ch' ip (docble ) ( bo2)_ Jouble J ) (6 86 Cic 77 int X (jii #D tn$ fn " exttocKun I tov 'p Jefine '28 3| 32 | -2 t 2 2 48 "*€ 32 bils Lzlimib 'n+ (ic+ ) + 2 Int_Min Wotks Wtn 0g 0 006 . 0 Jorzut +t nt CMuk - (27 ), dedcahoo 6vo & t0 ( Ttroa tne <231 Int_MAX

## Page 3

'n+ LJ tic+ ) 226 *2~X Int_Min Wotks Wtn 0g 0 00" 40 c+t bj Jefoult intege (Dox . 80 27,] 864 = 0 20-' S bous = 3[-~" LD" 0m= =) 27'-1 9-+ 7 2 s6405 0* .0 '3 S 2 s6nuj Lqis. 19 40 i  3 26/6 Ga+ ) unsigned Iat *; [0, 2 o0 - 2 =) 0 UINT-MAX ie [9 2" _ '1 n-6ils ~7 2" 6n0s 772 -' option?| 86 i e 64 6its long  long Iat 0y 63 lonj  long * / + 2 - LLONG-MaX LLoNG -Min huno | Ion5 Iict X) 86 i e unsigned Iong 64-8ib 2 I0 10 2 4 1000 = 2 31 to 2"-1 20 nt: -2 2 N 109 10 + 2 N 63 12 +2-' 240 N 10 bonj 18 + |0 260 0 60 id lorg log 2 Naming Rules for Variables It must only contain uppercase or lowercase alphabets, digits and underscore_ It must not start with a digit. It should not a keyword: e.g: return, main, int; true, false etc. In C+t, variable names are case-sensitive. 'c+ X= I0o/ in+ # = 5o; X Sw iuo Zoull X; Common Issues using Variables MuR ] X;v INT_MAX 7 - 2" Sign f site'9 2_7 Signrd 1 67_,7 [ %, -MAX Ullonc_ 10 3 I0 & Id $ 30 1 long 1618 Io " Lout/ m

## Page 4

In C++ You cannot use a variable before you declare it. X - {at Io; You can create multiple variables with the same names_ You cannot re-declare a variable. X v 'A' em; thot By default a variable contains a garbage value. Ll Y ) I1) am6ij uos '4 X) {at 7, kt reded or3kon /Jemr MuR| Zou+

## Page 5

Arithmetic Operators in C++ Arithmetic Operators in Ct+ Ct+ supports five basic arithmetic operations, these include Addition ) to add two numbers Subtraction ( - ) to subtract two numbers or to denote negative number Multiplication to multiply two numbers Division ( / ) to divide two numbers Modulus % ) returns remainder of dividing the 1st operand by the 2nd Int "10; I0 67 int 5; 6 // addition cout endl; 115 I subtraction cout endl; 5 1/ multiplication cout endl; 50 i/division 2 cout 0 endl; // modulus 1 J Lo#J a  3 cout endl; So <+ fw-2]-5 'nt 'nt EEzzfn iat 3 7,0 / 2 4 / 2 6 }loet o 3' 5 (floct) # 1 2 +yge- cokr) Operator Precedence and Associativity The precedence of an operator dictates the order of operations in an expression. Example 0 _4 Ia * 4 = 2 3 Intco CM M Page fioov ceil [ 7 't 3.$ 35 Plvat exelfcet

## Page 6

The precedence of an operator dictates the order of operations in an expression: Example = 2 3 3 + 5 * 4 =23 s-4, 3 + $ 8 _ 4/2 = 6 2 0 In C++, we can use parentheses to enforce precedence  (3 + 5) 4 =32 (8 _ 4) /2 = 2 The associativity of an operator is used to determine the order of operations when operators in an expression have the same precedence 100 / 10 10 = 100 5 _ 2 +3=6 a8souo hie lef ~ Xn+ 10o R 10 (oo / 1o 5 - 2 + 3 Simple Interest Given the values of principal, rate and time, write program to find simple interest '^+ 'at 'at L| Intco CM M Page Io 9

## Page 7

Relational Operators in Ct+ Relational or Boolean Operators in C++ Ct+ offers six different Relational or Boolean operators Boolean Comparator Example Meaning a > b a greater than b a < b a less than b >= a >= b a greater than or equal to b a <=b a less than or equal to b a == b a equal to b a != b a not equal to b A Relational or Boolean operator always evaluates to True or False 'a+ 0 = 10 / 'a+ b= $; 12 (~a > 6 ) Ldut Ll (a --6) Ll (4 ! - 4) ) L4 Intro to C^M^M 2ou4 Lout Page

## Page 8

Logical Operators in C++ Logical Operators in C++ J0 88 Ctt offers three different logiczr operators 7 0t , P P and Q P or Q P not P True True True True True False True False False True False True False True False True False False False False precedence(not) precedence(and) 7 precedence(or) AIl the logical operators are left to right associative: Jolse Short-Circuiting of Logical and & or Operators P  &d /0 Consider two Boolean expressions "P" & "Q" flse 0 {S adl During evaluation of expression P and Q, if "P" evaluates to False, since overall expression evaluates to False, expression "Q" will not be evaluated: During evaluation of expression P or Q, if "P" evaluates to True, since the overall expression evaluates to True, expression "Q' will not be evaluated. NYur L 67 1= & is nF Truthy vs Falsy Values 490 e (vo/ L4 Intro to C^M^M Page & thee a

## Page 9

In C++_ individual values can evaluate to True or False. The values which evaluate to True are considered Truthy & values that evaluate to False are considered Falsy: Truthy values include non-zero numbers, and the constant true. In contrast; Falsy values include the numeric zero-value and the constants false & NULL. 0 + folse #include<iostream> using namespace std; ve; +ve Atve int main() { Jo int X 10, y = 0; Jnd cout 44 (x and y) 4 endl; 10 cout 4< (x 01 y) < endl; tie return 0 ; Fsl 1o 6r 0_ tyve Pobse Nve L4 Intro to C^M^M Page

## Page 10

Conditionals in C++ Conditional Logic in C++ if Statement int main() { 7 trve if(condition) filse 11 body return 0; else Statement L4 Intro to C^M^M Page 10

## Page 11

int main() { 4vue if(condition) { 11 St else { 11 return 0 ; else if Statement int main() { Ai-100 11 if(condition_1) { 81- 4 ='6' } else if(condition_2) { 9'€' } else if(condition_3) { 7'0 } else { 51 - SF' return 0; L4 Intro to C^M^M Page 11 body body 9'a' A1- %0 61 - 7o ophonal 60 = `€' Otncrw  Sc

## Page 12

Largest of three numbers Given three numbers, design an algorithm to find the largest number: Example Input : 2, 6, 4 Output : 6 L4 Intro to C^M^M Page 12

## Page 13

Loops in Ct+ Loops in C++ A loop is programming construct that allows you to do the same task repeatedly while a condition is true. In general, a loop has four components Initialization Condition Checking Body of the loop Update Rule The while Loop int main() { ait 11 {olsc 11 initializatfon hiee Je & While(condition) te loxp I1 body the loop vpdale Lle bod) return 0; aqk A=s i | 1 $ 4 $ L4 Intro to CM^M Page 13 ~tn lcdn 4 of

## Page 14

Homework N=5 N=5 N=4 1 1 2 ' 2 3 ; 0 2 3 2   3 4 1 0 1 4 5 6 1  2 3 4 5 1   0 1 0 1 7   8 9 10 N=5 N=5 1 1 2 5 2 3 2 3 4 3 4 5 4 3 4 5 6 7 4 5 6 7 6 5 4 5 ] 6 7 8 9 5] 6 7 8 9 8 7 6 5 n = 5 n = 5 n = 5 * * * * * * * X * * * * * * * * * * *  : * * *  * * * * * * * n = 5 n = 5 * * * * * * * * * * * * * * * * * * * * * * * * * * * L4 Intro to C^M^M Page 14 * * *

