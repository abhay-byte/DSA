# Lecture 26 (EasyOCR)

**Source:** `L26 - Recursion.pdf`

---

## Page 1

N Queens Queens Optimization Recording https:/ drive google com/file/d/1Ppnls_KM9TIMdXLiI9S6NonDIECzLkMbIview?usp_sharing NQueens Given a N x N chessboard_ and N queens, design a recursive algorithm to place the queens on the chessboard such that no two queens attack each other we say that two queens will attack each other when are placed along the same row, column or diagonal 0 =4 0 0 0, G1 43 Example 2 3 N=4 @o 2 3 01 Qo 2 3 Q3 3 4x4 (T =- ^ ) { Jeve 6ui + 'ait T =0 Voi;) N-1 00 T ; : 8t-1 Joo Con Plak & (r ftr) r+1 B i eitcv 61n % ',2,}...7-1 N-1 NxN G 8n +o 00 04j 4 0-| m, + takes deusion 5   + Sd(u? trs 211 tov Or + a-' "$ je10e for Q7 ic YoW Fo+) J{vd ( me Qr where Vstor (vedovL Tolj axo Uor 7 L26 Recursion Page they T-od Bkg L;, J''Uc Wi0 Plece Jo'M Ln4v? Lsm^9 v p

## Page 2

V e Uhy 2 v{ur L vedor <smhg7 boavd; 0 = 4 j (i-', /en, '++) { smcd s( n,' . ) S++i0] s (^ , beatd' 0b vpdov ( Vc Uorc smaj ? 2 Jiigpev08 0; 02 | 47- 1 wil 's 0. + Qr-' Por &r 0+2 when thpr) '$ Placed r-4 0o +0 Sume r-3 wi 3 8; {dw 0 t 7 04 | ey-| alon) T-1 the sam? L1 / rek+ &v3h+ &4 ha jm wi N r-2 r-1 0-17 jti 7-2 5j+2 r-3 M)+3 r-3 J+l Jti_ L26 Recursion Page shg (s)) Voi d vt on) y Pleced Parv _ 7v e Pq

## Page 3

[RJIHW] Solve Sudoku Solve Sudoku Given a partially filled 9x9 Sudoku Grid, design a recursive algorithm to assign a digit in the range 1 to 9 to all the empty cells such that each rOW _ column & V9 x V9 sub-grid contain exactly one instance of a digit. Example 3 6 5 8 4 5 32 8 3 3 8 9 8 | 6 3 5 5 9 6 3 2 | 5 4 5 2 6 3 N-1 L26 Recursion Page

## Page 4

N-1 NxN 3 6 5 8 4 5 | 2 8 | 3 3 8 9 | 8 | 6 | 3 5 A 5 9 6 1 | 3 2 | 5 7 4 5 2 | 6 3 L26 Recursion Page -

## Page 5

Time Space Complexity Analysis of Recursive Algorthms Loe Cec - cavis hme spot i0 Pou (ai Time & Space Complexity Analysis of Recursive Algorithms ixtu Non Mctn' Bac 8vbs +7 +(o) = tI-') #t( (ecn-w+c)+c void fin) tlo-i) + ( t(0) = tlo-12 +20 Dase Case UNt tCn-')= &la-1) tla-3) +(-3) + 3€ Tetutn; Ela-1) 8 recursive case Ik:0 Kc Kin ttn-' tW) = +c-k) (0-') ( (0-i)c # 0c o(o) ~ OC 0 ) Pz n'€ OC n ) Pc-3 Pn- 2 #o- 1 Po 8 +n ? t(n-/)+c 0 +a) = +62)+2c 2= void f(n) (n-')c +.c t(n-') tk-2) t(-y) (-)'c base Case Itin +(0-1) 3 ) (4-1) c-( (o-'JC O-c Feturn; J + (_2  + =+(-2 recursive case +64) = A-k =| K-n| fortint 1-0; 44+); J + Oc 4 (0-2 )c (o-' + fin-1; (1 - (k-n) c t(-k ) + 2) (n-)c +0c c + Qc + (n-2) fn 6-'2c < ( 2 t2] k' 7 - ocz' 2, Po-2 ~c ~ 0 ( n2 ) Pz L Pa- 3 Pa-1 spece 2 C Dla Ya-! fz Jop + k fa (ah L A1 t(n) 2+ (c/2) + +(n) = 2+(/2) + € Int I(0) +(ll) = 2tln/w) + € 2( 250n/4 ) +c) + c base casc 2c + C It( = 31 tln/y) 2t(a/8)+6 2+63) + return tlni+) 2t2 21 +6) iet & = t(o lnst 3t(0- 'c t(0-) 1-0; O(n2 ) ~2 Cn-2) € Stk tn) Wart 2+03 )+c) +

## Page 6



## Page 7

'Ll tln/y) = 2t(ol8 )+6 + It( 27+03)- return recursive case +Ca)=c 2(10g242" %75 return i(n/zi 0(n/21; Lclz) 2c+2c +28c ~1 86 29 +k )+ 22 + Zc+2ct 2 € + K 125 ? 2* +642 Lo #g, 2' .c zc+2'+2c 2*+61 ) Li Pg, 2 .c 2 ~ 26 . € + +2c zk 7 Ll o(c ) a -2' = /` 9 P Tz2 3.c rt #=k+1 c [ 2 - '] L3 2 -1] 2* 1ogf c [ &3U - +] 5) K= 1o53 20 '7 i  - Lk Jv0 + 0( (05n) Cm Stk #a c 1ex U W( zok- 2 ~ OCn ) tm qcdn Pa (1 boue cd^ (" etk m " Uo ) tlo) = 2t(2)+0 € void tIn) t(o) = 2ttch2 ) +Oc +nc 4* ) 2(2+0/4 ) Aafe 2 +l) = 2el9)w) +Oirt 21(o18 ) +CtL - Rnc itin tknia) 2*+0) + OCACP Tecuttive Co8 ^ * ntzi; +o 3C 3nc Inzl; 2 +6)+ dlnia/a Ataun un In Oinl Kine + KOL oc K? Ig " 2" t&g) ac Fq Ied 2 + nc 2 42_6/ 443/4 + 3"%5^ ( Y # = ^l 0 Cologc) Fq,Y9 Iq t D( ^ ) oCwg^ ) due # Jue + nc 6 (2/1 (2 kmp LK 44 8+k '^ Merse 7 K? 'es f 31 1 2+ nc (kti) Jl Hoe scral #Ievely L7 Kac nc n Iognc 2' otalv9n) ticil) 2 K = 0 + ..+ +2'€+28 -(22"-1 ) c C2+2'+2l - 1 6 85 &74 1a € e < | 1+39) +ol) +o/i) +z0c 2" (2t'3 2+49) 2+7 | 21 = 9 I50-oc Ac 2prc & tch (eU

## Page 8

#_) 2*,) 2 -|

## Page 9

int fIn) abase case ifin Ii 0 _ J) ( retutn 0; recursive case return T(n-I) n-21;

## Page 10



