# Lecture 24 (EasyOCR)

**Source:** `L24 - Recursion.pdf`

---

## Page 1

Replace Pi Pi 37 "3 ./4 '/ Replace Pi Given a string, represented as a character array, design a recursive algorithm to replace all the pi's in the given string with 3.14 & print the resulting string: Example 'vP "eieei" Input 'pip" Ee" Output '3.14p" " W)P ` 3.14 P 3-14 3.| 4 P Input 'pippi" Seiiei" Output "3.14p3.14" '/p Ee", "i 3+4i 3 Iy  3 .14 & 3 "4 fziead in { 1 inplo] = = P' and i~P[iJ =2" {lse twue 9 $ k Jev fvead +0 JF tnc 1 TePi @ce "Pi" witn l,')h fx wim "8.1Y ' 3 . 14 " i^ icp[i .1-'7 2  Lsk Jovr (rerd to]replee p' Wim "3+14" 8a Bapc] 'ait i=0 pi;) : i+ 's a jn tmr L24 Recursion Page "p; " Te plae

## Page 2

'ait I=0 tmr #l) Cfo:#h repleees 9i tc <vrcat P; wim "3-(Y"11 iap; = = '(' Jn4 ie;+u = =" 1^ "^Pt /_.1-01 fhse +tve J+ ) te tnc c',+ ix wi "3'Y" Jii dav. Starhhg 0) snift N; (+2 2sk15 ~xa' {apc ; ] 3' ; 7 e^(t+o7 ipc,+2] = i^Pcf+] = "4; 2 . fe ` termS Cose 2 (inp t;)=z' |o' ) { L24 Recursion Page Prebical ~(i+1 "P;" Place p (+4) 8 & 4 3 ase wrii 74

## Page 3

Generate Subsequences tnere W'U be 2 su 6s uente} Sq . % si6 ^ _ "06" "ct" 2 0 6 X Generate Subsequences Subsels 2 Given a string, design a recursive algorithm to generate all of its subsequences. A subsequence of a sequence is a sequence which can be obtained by removing or more elements from the given sequence such that the relative order blw the sequence elements doesn't change. Example 76.c " Input ~abc Output "abc' "ab" "ac" "a" "bc" "b" "c" Ae3 0 € 4 6 ab € w te WJkenevev weile Kolvic] Jworhon , J"' thea 4 build Jeusion Huke Seq' 8 t d: 0 Kewrsive g( 21i Jw"u QU m me IS keusion take wiu Aone ticen re s4bs1 we'ue + Hele 0 T G deusioo) 0- Atu'sionj ~sh' % whemc + eccn dnov J Or exd' '+ frm %r So (^ +0 J 60} Id Q Aewrsfve we"vP to d0 Ju tns tne (St chat teSh 's Jeci de (an be telcen aUl tne Aeusionj selrsivxyy: Giead { Y iopr Rad - exd KecWAull aze } Gjr " 9c6d "06" "6c" xer cvs i+el] Aeu'siof Y(nerd ) Suild (^Q` Otobifm golv €

## Page 4

4"p' LyLIY Rad - exd Sip}; 7 U|. ^p{) i+ :s fa 2 dec' = for Jait {o i9 X {o next 8ree 8 - 0 tnis 4o Sdlve JusF Jor exd = A+ti+,i) 7 outcj]= 7fu+,") 63^) 5 / 8 dut 0 2 lalblc {np(] #- j= 6 Out[] 3 KcWAul aze 4 OUt[) +not  7+(,;) 5/ons tuxes 0-'7 Inp [ i _ char 5 '+ 1 ) '5 dot 9ues dejae {cPt;] inu; inPc;] 8arC, ) ==' |o' You+cy) . ' L2 cot ~7r4

## Page 5

Jiz0 J= 0 out[] 2 3 # fije6 8-z jeo f-zj-z fi-2 JFI fzj;' fiesje' f-sj= f-sj-1 f;-s j= fi-3 )=1 Jiz; fi-; ;-2 Fi-sjez 9-3 inpc] @lic f_ @ (pi J? 0 | 2 $ # fizva 80 f-? jeo fi-z j' FR-jA f-zj-z #~f-Jfizj- f-sjee fitsj=i fi-sje1 {-; j-} fi-vj-1  Fisjer 6 6b 0L 06c KecWAull aze $ Dut[)

## Page 6

Generate Parentheses Generate Parentheses Given N pairs of parentheses, design a recursive algorithm to generate all the combinations of parentheses_ Example (( )) 4ez2 Input N=2 ()C) Output "(()" "(O" ")(" 2) ( € A: 3 (7) L 2)€ 4 ( ) ) ) (7) ( > ( ) (()) ( ) 9-4 :2 <  $ 1 21 opn+6n+ Uosc (n+ La - | Out ( ] +ake Aects/ms for +0 ~em)ij (s init {-0 Qn-1 0l > 0 Ll >0 +6   So kxe tns 8e0d} fer me LZ4 Recursion Page 2 (( ) f(;,oc,c ) - jush

## Page 7

t6 So (  TT'> U - 8 e0d} for me closknt <^ ofraln+ 2n e* Qos outcr) =' )' 0c, c+i) 6c+1, Cc) h 2n ) S DC_-n Jnd (L-n Dott<)= `10 ) Uot2l out) ~& LZ4 Recursion Page outC;) = ' ( F6+ 3 ( i = =

## Page 8

Generate Balanced Parentheses Generate Balanced Parentheses Given N pairs of parentheses, design a recursive algorithm to generate all the combinations of well-formed parentheses. Example ((y) ) 2) ( (X Input :N=2 (26 ) Output "()", "((" 2 ( c)x Input N=3 Output "())" "(())", "(O" "(())" "'(oo" (( ( ) ) ) (2)) (( * (3( )( ) ((72) ( ) ((2( ) ) L2A Recursion Page 0 =2 ) ( ( ))

## Page 9

[HW] Coin Toss Coin Toss Given N coins, such that each coin has two sides H (heads) and T (tails) , design a recursive algorithm to generate all the possible outcomes that we can get upon tossing the N coins simultaneously: Example Input N=2 Output "HH" 'HT" "TH" , "TT" Input N =3 Output "HHH", "HHT" "HTH" , "HTT" "THH" "THT' "TTH" "TTT" L24 Recursian Puye

## Page 10

[HW] Restricted Coin Toss Restricted Coin Toss Given N coins, such that each coin has two sides H (heads) & T (tails) , design a recursive algorithm to generate all the possible outcomes that we can get upon tossing the N coins simultaneously such that an outcome should not contain consecutive heads_ Example Input N=2 Output "HT" "TH", "TT" Input N=3 Output "HTH", "HTT" "THT" , "TTh" "TTT" L24 Recursiun Puge

## Page 11

[HW] Creating Expression https:]Icodeforces com/groupMWSDmqGsZmIcontest/223339/problemIv L24 Recursion 11 Page

## Page 12

[HW] Generate Binary Strings without Adjacent Zeros https [Leetcode com/problemsIgenerate-binary-strings-without-adjacent-zeros/descriptionL L24 Recursion 12 Page

