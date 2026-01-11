# Lecture 38 (EasyOCR)

**Source:** `L38 - Tries.pdf`

---

## Page 1

Tries Introduction Introduction to Tries Given a sequence of N words and a sequence of Q queries; design an algorithm to check if  each of the queries are present in the given sequence of N words_ Example Wtj Input words [cede" #coder" 'ooding DIOck bblocks" "'nerst] queries code" 'coding"' , "blocked" , "block" "news "new" Output L True, True, False, True' True; False 1+9 Px blol%E N wols 1 | | using Linear Search 0 0a Ant spent +we srs 1-14J CdSC '4 mC w~peji j In +he mio (Ple^ witn 1/1 te D word3 _ 6 g/3le qutrj ie^ 3 Sz ) N , nio Naxj , 4a-8 ) N , ( 7>> Wavd / Qav0 + 2 ? + P 8: N nia Wava ~9v3 3) hsh-;4 hae lngt (461  ~ GN 2A S{ec e: 0lt) evr 2. using HashSet (unordered_set) ('0)~ "c N= N w 9 7i) Jt (,44),, 1 tn *r {~Se Kno 0J9 me {kj' k 2 - '^ m & loorvp eawhn qv*d o(~) ape + Jnd se habh-el  1ot hzeh - bC~+ 9) N . 5"a Q: 4 using Tries N= wav6 wocds 0 0 T;€ 0 11 Tr0 {a$ m e Gwru oQ Q' 49"9 0 vet 2 ;o mf hr `e Ieeco P 9ord N--7+ 0 € ~+ 0) Tric: Fure queries wt" 4 $', wdt8+ - 1-2714' 98.23" 91-222 _ 275 M~+ DcJs iosert hosh- s8 Avey'4s Dvr $ 0c+ space: ~0, + cls Rt0 k 9 >? Roc

## Page 2

Tries Introduction II What are Tries ? It is a data structure, specifically a kind of generic tree that supports efficient lookups and insert operations that on average take time proportional to the key length: A  genarictree is a tree data-structure in which each node has 0 or more child nodes: 0 ) ( L38 Tries Page

## Page 3

Tries Insert W0 [ c Ie^ #m e Lut String Insertion in Tries Example id Input "code # 0 4 :3 9 io0 32-72 kut 2 1 C Cnot 4+300 booQ kesniol' m.r ('8r * 740? cor 60 2z WT 4oo 3 350 07 55 % Tries Page 3 String Td ( 9 2 1 chfIJA? unotderro _ i-66 1 - 72 70 D Goo % ~

## Page 4

Tries String Lookup String Lookup in Tries wy @ 0 & W 2 4 5 == 0 L) E S R L38 Tries Page 5 5 = = =

## Page 5

Tries Unique Prefix Shortest Unique Prefix Array Given an array of strings, design an algorithm to find the shortest unique prefix for each string in the given array: If there is no unique prefix, return empty string Example Input code coder "coding" new "neon' LO Output 'coder" "codi' 'new "neo' Co K C Ld Co Je "code" 'coder" "coding "new "neon' Objo~ & 64 7 der Co dicd Jas = 2 3 Lq R L38 Tries Page 5 Array Co 0 - Co 22 -6 cod :

## Page 6

Tries Longest Common Prefix Longest Common Prefix Given an array of strings, design an algorithm to find the longest common prefix string amongst the given strings. If there is no common prefix, return empty string: Example Input "flow" "floor" "flys' J Output "fl" flow JaS = ~PS fixs L,3 floov 0,2 W,1 5,1 R;1 L38 Tries Yq # Page'

## Page 7

Tries Integer Insert (2+ ) 0 5 ( 9 2 4 ~3 2 00 . 777r284 29 = 16+8 +2+1 Integer Insertion in Tries L 1' 1 3|_ 2" 28 29 Example 1 lep+ k 7 TDot 72.2 " Z€yr isR 2 Ue D 32 1 | 04x 8 Tcs Pirc / 3rd ~ant L u5t }

## Page 8

Tries Lookup Integer Integer Lookup in Tries Wv USy 1 1 0 0 Example : 3 0 1 2nd 1st Oth 2 4 5 8 10 1 | 0 | 0 L38 Tries 3rd 79 Page

## Page 9

[RJIHW] Tries Maximum XOR Pair Maximum XOR Pair Given an array of N non-negative integers, design an algorithm to compute the maximum XOR possible between a pair of integers in the given Example : Input a b a^b 2 3 4 2 5 8 10 Output : 15 i : Explanation 5410 = 15 0 Input 2 | 3 4 2 | 4 | 5 | 8 10 2nd Oth 2 4 5 8 1 | 10 1 | 0 | L38 Tries Page 9 array: 3rd 1st

## Page 10

3rd 2nd 1st Oth X=2 0 | 0 | 0 Yideal Yactual (x^y)ideal 41 | 1 | (x"y)actual 1st Oth x= 5 0 | 1 | 0 | Yideal Yactual (x^y)ideal | 1 | 1 | (x"y)actual L38 Tries Page 10 3rd 2nd

## Page 11

[RI[HW] Tries Maximum Subarray XOR Maximum Subarray XOR Given an array of N integers, design an algorithm to find the maximum subarray XOR Example Input 2 ~3 | 4 5 25 10 2 | 8 | 5 | 3 Output 31 arr 2 ~3 4 5 25 10 | 2 | 8 | 5 / 3 cxor 1 | 2 | 3 | 4 | 5 | 6 L38 Tries Page 11

## Page 12

i-1 arr arr 2 3 4 5 25 10 | 2 | 8 | 5 3 cxor 2 3 4 | 5 6 25 | 19 | 17 | 25 | 28 31 L38 Tries Page 12

