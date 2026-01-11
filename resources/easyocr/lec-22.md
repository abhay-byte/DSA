# Lecture 22 (EasyOCR)

**Source:** `L22 - Recursion.pdf`

---

## Page 1

Recursion Intro redvUh 0 a 'ju Reduchoc Reduction algoX ) 2 SoinY Recursion It is a kind of Reduction_ Suppose you are given a problem X for which you want to design a recursive algorithm then recursion says If you can solve X directly then solve it directly. [Base Case] Otherwise, reduce X into one or more smaller instances &f7 the same problem (sub-problem): [Recursive Case] Jx Xi   Y2 Y3 #ried Kecuot Pace

## Page 2

4 l si^X fx { fx1 fxn LzI Kecuot Paee _

## Page 3

LzI Kecuot Paee _

## Page 4

Factorial Factorial of a Number Given a non-negative number n, design a recursive algorithm to compute nl. 9 -5 5! : 5, 4 3 .2: / = $. ( 4-3.2-') =s 4' 2 2_ (a -,) / 46_ .A tn + Rewrence Qet' 8+ {s a fo fias n, A 76) = 5 p(42 5 7") 0. 36,) 4192 84 ` 0 Po 3' fo) Rewrsire (ase ttt   finas (a-,x (+t ) = 0 * H ( 844 36) '^vold fn Gi/ 1 Gase Cas e } () = Hme = Int flint n) { base case #rec: lavs tm? Qatn (aii 'n In E 0) { 11 i(0) Tind 0!  A0 Bas < 8e Case retumn # 7 $ 4=1 recursive casc Pnerd  - I f(n) find p 1 {a-2 Il 1 ask your friend to find 2 Int f(n 17; $ Asa Pa-, return f n=" Ja Mox no d stoc A= #ome 0(n ) 24 Lcst +0 oT Voe Rc Co |' Stk glod foc Fa &vume Lor Rc-urs_nd Fae 120 286 8 peaF wnst wasr 0-(ils Qped *0 scoce Qoon 40

## Page 5

pr &d &rome Rc-urs_nd Fae 8toc base 0 $ Q

## Page 6

Fibonacci Numbers Fibonacci Numbers Given a non-negative number n, design a recursive algorithm to compute the nth Fibonacci number. 13 21 34 4 + & 0o 5 Rena tre 8+ 1s 0 +n tr+ Acds 8s: nd 4y 736) PCa-2) 0 /8rena Pz 4 / Rend 0 ase ( $ € P_ 8_ t 4-2 #ails #6 iovo I/'d Co|i$ +o + 8-' #2' +, = icvol'd ( & |1S 2 l ) ~ ( aoc 0 Def (ora: + 01 Wn ' L2? Rccugion "R. (4-1*2;e: 0t J(n-,) nod e eacn To0 + problem ) rion T el= Subovobiem Fs-

## Page 7

(oi9" r" + O1 Wrt = 0o - 80 i0n T Q E {o lec} totw ^d Gose ) gob = otr solving Jo no to+a Ise @ u$ Lo Max level he @ L2 Mar: depmn L3 c ncle 3 : . MGX h'6 n; & = 3 tne hree #s Ro Po 3 Lo 02 Li A-) tnend A> L2? Rccugion Subfro-biem total ~des Iee Wts = nodes basp 'Qrbiems Tewrs iFueq = +e '6ht 6=0 Cazc

## Page 8

CI A -1 #nena Yo + A= " 0=1 - A= L2 ie-" {~ Ro L3 Beot2 +y An-3 Po Pt- % 2, La iru, V+ Grj 0 1 (rom (0 0 60 olj theve 8tk Hme te   An (o ) 0i Kax' 06 on   #o # |eoles tromeo Ca V 0 - A - (euz!s fromes Sqace = 4 doe + Qat) for (i V #n #s+r hromex Hum L2? Rccugion 6=0 3 + #,& 0 'ven guboro6 8kck 8+K gtocK b(n) wavf Stk 8fc " St1 Fs-

## Page 9

Multiply Numbers Multiply Numbers Given two non-negative integers X and y, design a recursive algorithm to compute their product. Xz $ J= 4 4 = 12 3 * X * | x + X+_tx X * ) = 1-' #ne Erea & X + 0 To +nt : '$ (0 | X * ` 8 *e f(x)) M ( fc add 5 ~X d A / fned flxo) =  x + J (x-' 8 nvb;d Qase (ase Lz? Recursion LU-tines ma tme x + f(x,&-) flx,) = Page

## Page 10

int flint X, int y) { #ime: 0j ) 11 base case if (y = 0) { x3 ;-o| 6C4) 11 f(x, 0) 5 add return 0 Jve + #n Xe3 j-1 Coii Stk 11 recursive case I1 f(x, Y) = add 4 Xeldz 3 11 1. ask your fried int A = f(x, y - 1) ; X334-r return X + A; € X~3 A 12 LzZ Recursion space; 4y Paze

## Page 11

Print Increasing Print Increasing Given a positive integer N, design a recursive algorithm to print numbers from to N in the increasing order. 2   3 4 S Qz$ 0 - 2 0- 5 2 ? Jriend void f(int n) { I1 base case if (n = 0) { 3 # 0 / p' 4234 5 11 f(0) print nos return; I/ mandator 3 € 11 recursive case #rer _) 8_ +ne : 0(o ) 11 f(n) print nos. fr 11 1. ask your friend O(n) Jr f(n 51 ] 1) ; 3 f Gi Str_ cout +o Pa return; 11 optional 5 } A-0 L22 Recursion Spoce : Page

## Page 12

Print Decreasing Print Decreasing Given a positive integer N, design a recursive algorithm to print numbers from N to 1 in the decreasing order. A~ $ {(n-' ) 3   1 ` 1- | I- 2 PCo) void flint n) { 1/ base case if (n = 0) { 11 f(0) print nos 5 3 2 2 return; 11 mandator I1 recursive case # 11 f(n) print nos. fre cout 32n < Anerd # I1 1. ask your friend f(n 1) ; return; 11 optional F L22 Recursion } Page

## Page 13

[HW] 3n + 1 Sequence https gIcodeforces com/group/MWSDmgGsZm/contest/223339/problem/Q L22 Recursion Page 13

## Page 14

Power Power Given two non-negative integers x and y, design a recursive algorithm to compute xv Example Input Xe2y=3 Output 2 8 A (fnend ) J-' #me 2 X. Y.X tncs J XA F(x,`) tnot mui' X , L &+ fs ~a fa i+ ;s  4 Po {-e J that (d| . x] X A/fned (x, 6) = #nc: 0)) X-2 Jeq 7 X3l sqace : 09) 5 1 42 dve +o A 8 fn &u 13f X-1 F+ A gte 7 } XrJl 32 X AA Is (Nr Y/2 Jswi~) J 3 3 3 3 3 9lz Yh X _ > . X 4" - 45.48 Recumion +n's F(x,d-') #;en +J- +3 Yi2 4 $ A'A X Fs-

## Page 15

JI Yh X - X x - X 4" = 4f45 J 4' 5l2 3 " . 3 ' } ' 3 2 2 3 ` 3' 3 4' ~ + 5 41. 9'+ J 1/2' - / 9 2 2K= > J 12' ^ 1 Ju* 7 } K = 1v9,4 5) Y cst 4 Y/2} ~ Ioj 2 : 9( 6 K+l 6( loay ) 2 Ize" ' Gos< Cas6 Joe +o 0 ( '9y ) fa (" Recumion `s 64 Warn - 919y Sll 4 | 9/1, ^ Sp ac e ; stk Fs-

## Page 16

[HW] Count Good Numbers https [Ileetcode com/problems/count-good-numbersL L22 Recursion 16 Page

## Page 17

[RJIHW] Generate Binary Generate Binary Given a position integer N, design a recursive algorithm to generate its binary Example Input N = 20 Output 10100 L22 Recursion Page 17

## Page 18

[RJ[HW] String to Integer 123 123' String to Integer (stricj Crct) Given a string str, design a recursive algorithm to convert it to an integer. Example Input str "123" st 8 ("123" )-123 Output 123 (ia+) ("123-")5' ( (oc) (on9 to_shing (112) ~"ehy_ ('n+ ) (smcj L22 Recursion T2 3--- Sto RQ Page

## Page 19

[HW] Spell Number Spell Number Given a positive integer N, design a recursive algorithm to spell it. Example Input N = 123 Pp A= Lbz Output one two three Oae two tnre e e r L22 Recursion Page 19

## Page 20

[HW] Move X Move X Given a string "str' design a recursive algorithm to move all the x' characters to the end of the given string such that relative position of non-x characters doesn't change. Example Input str = "xaxbxc" 3 a 6 Xx Output "abcxxx" X 0 X6 Input str = "axbxcx" Output "abcxxx" 0cab xx " c x 9 * 6" _ L22 Recursion Page 20

## Page 21

Tower of Hanoi Tower of Hanoi Given a three towers and N disks of varying sizes that can slide onto any Of the towers Initially  all the N disks are placed in the decreasing order of their sizes on the 1st tower (source) i.e. the smallest disk at its top and the largest disk at its bottom Design a recursive Blgorithm for generating the steps required t0 move the N disks from the source tower to the 3rd tower (destination) using the tower (helper) such that at any point of time you can move a one disk from top of one tower t0 the top of another. you cannot place a larger disk on of smaller disk Example Input AN4 heiper dos1^ ourte A 4 move disk from Ato C " |P = A D move disk from Ato B 2 ' move disk from Cto B 3 move disk from Ato C 6 move disk from B to A 4' move disk from B to C s . D A move disk from Ato C 6 D C 0_ 3 Mou*s 34 + C 0= 4 m ou*5 =5 1 n- $ MoJps ~31 2 _ 0- disks 0 $ + Src 6 A src ( 'A' ) +o dst ('c') usiss dst ( &' O- Jrsks   hom usinj ('A' ) to n-i d i skS Jrm Plm-) -) 1* Src +o J sr ect d,i*s K bwm ('A' ) (`6' S (A ' Mou & Igt9 E Jsing 2 ' '(G') t O-i d1 kS txm M 0JQ 3 - PE 2 2nd= top + 1 a hlp hie ('0') sztn ) hip ( 0') Mour Stc Move ds+ (`&) nip #l- ) -

