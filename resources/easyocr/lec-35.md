# Lecture 35 (EasyOCR)

**Source:** `L35 - Heaps and HashMaps.pdf`

---

## Page 1

K Largest Elements K Largest Elements 40 60,50 Given an array nums of N integers and a positive number Kt<N); design an algorithm to the K largest elements in the given array: Note You can print the K largest element in any order: Example Input nums [60, 50,70, 20,730, 40],k = 3 Output 40, 50, 60 } St ~ Sovt aar 0loj 9 1 Jemet R 2 . alogn+1 Xato 0 mixltea p 244 ~Pot bansjrm avoy kico k elemtars 2. extol + klej^ +h0 (8t k - YIves ito kl ar {nses & 54%pe" ~ictJaP remjin'~) Jemeab 810 tne ~-r (1-A) ( Ja 0 { eod demrnt tm+ eemint 's then do ~Pt ) nic+taP' met nintvap dement `^ tc 9ii +e eemrots } - Aeop klogk + klak + nlo9 K kloj k + nloj k n + HashMaps print "ppr tp-R exmeu Kr" ~Ioq k loaK+ lra k ) ded< #t Tl( acd PoPk ) kloa k exha# hbar Eoak alo K kl%d ^ alan + k Hcapa Fajc

## Page 2

K Largest Elements in a Stream K Largest Elements in a Stream Given a running stream of integers and a positive integer K, design an algorithm to the K largest elements in the stream every time you read a -1 from the stream. Note You can print the K largest element in any order. Example Input [60, 50,10,-729,30,-1,70,21,J.], K=3 Output {10, 50, 60 } {30, 50, 60 } = 40 , 50, 60 } 0 Si 2e R s9,)2 38 I',9,60 49 50, L3S - Heaps and HashMaps Page 2 print nianra bo, S9160 49,50,60

## Page 3

Merge K-Sorted Linked Lists Merge_K-Sorted Linked List Given the K sorted linked list, design an algorithm to merge them such that the merged linked list is also sorted. MP hi 60 70 50 Lo Kmp dummy 4m s + F^ 74 Ln3 3= F 20 F_ ( 4 2 0 3 n 40 Len | VO K-i)o ko Kn +Ra 30 + un + Qo+ 4 + + k) L35 Heaps and Hash Maps ktn 274 Ar En= 7 YG? Page

## Page 4

30+ 4n T Qo+ + k) n ( 2 + 3+4 + klrt') 2 pz 3 Ul 40 710 20)-) $9 300 39) 67-90 = n? nz miantap Jummy kmQ 40 6 0 30 ko? tmp Lem? smr Hrmk Lme kml Lemk + ka ( lok  n kl%gk L35 Heaps and Hash Maps ~ k? nk2 Jm lwk ) ~luqk Page

## Page 5

[RJIHW] Merge K-Sorted Arrays Merge K-Sorted Arrays Given the K sorted arrays, design an algorithm to merge them such that the merged array is also sorted: Example Input 2 3 1 | 3 | 7 10 2 | 4 | 5 | 11 2 0 | 6 | 8 | 9 Output 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 10 11 L35 Heaps and HashMaps Page 5

## Page 6

[RIIHW] Reorganize String Reorganize String Given a string, design an algorithm to check if the characters of the given string can be  reorganized in a way that no two characters with the same value are adjacent to each other. Example Input "aab" Input "aabca" Input "aaab" L35 Heaps and HashMaps Page

## Page 7

[RJHW] Median of a Running Stream Median of a Running Stream Given a running stream of integers, design an algorithm to print the median of the numbers in the stream each time a new integer is added to the stream: Example Input Stream 4 6 | 2 | 5 | 3 | 1 | 7 | 9 | 8 Median 4 | 5 | 4 |4.5 4 3.5 4 4.5 5 L35 and HashMaps Page Heaps

## Page 8

Introduction HashTable HashMap It is data structure which is used to store collection of key-value pairs. (kcy) (valc (Valvr ) ~J number Valve (Kej pes Km J (rit < woro | - m1 Jo.8 ph woj2 ~ Mz Wizg 240 Phz Pz Word } ~) nada : ~) 250 t20 Ta tea 3 €i 3 ) Wtda upkee Why use a HashTable ? HashTable, as a data-structure supports very efficient lookup operatipn. Mip 27 nrl7 Wos+ {ser t ov9 " 'S/ F C $ e etisf 0 (1 ) et'S6 (I26^ #n4 fod Reason behind Efficiency ? Data is stored in HashTable in an unordered-way: LJS Heups and HashMaps Qame S0n Key Pka und? deed B^ Pape

## Page 9

HashTable Implementation HashTable Implementation 7 captry d hsh- texble (4e3 - Kea = L Example m 7 Se % hach trble (, ) Value '7CC 7 0 -5 at (;) = 1 | 2 | 3 | 4 Tt anC; ] 2" 1762 Koe= 0L ) ioe-mi vie > hme hne 0(+) Limitations  6p1 Viw Keys are integer values that exceed the valid range of indices_ Keys are non-integer values_ 9. strings To solve this problem_ we use hash function mathematic function that transformn the keys into valid index inside the hash table a.ka hash index: Example_ kf ~ ba t/ n Value F^-5 hoc.04) ~3 44444 36 4164 8 tmc: 061) In h} kc-1= Xths JAf hashi> 7-1 At Limitatons Multiple (key, value) pairs can be 'meRed tOsmle )dex - collidr hoshidz Example Value Handling Collision 1o Lo6 Closed Hashing or Open Addressing Linear Probing Quadratic Probing Double Hashing Open Hashing or Chaining The idea behind   chaining Is t0 maintain linked list at each index or bucket the hash table to store all the (key value) pairs that have been mapped to that index Key Value Jbl = 'nbert buekehs lnst Jolec hp h} kJ, six 7 hashiJx ) 2 at Owy 4 i~ 2 2 It Rehashing or wtr Pator Key: vo lvc {ooo The idea behind rehashing is to double the capacity of hash table once the load twn m - 0 0 8o' factor MIN exceeds certain threshold. {c xne Q How ^ ~5 1aj By creating new hash table with twice the 827r2% curent hash table and tvrn rehashing (key; value pairs from current hash_ to The new hash table_ This way we can lower the load factor inprove InE eficiency of operations on hash table. We will internally represent the hash table using dynamic array of singly linked lists such each node of the linked list present at the ith 0<-i<-N-1) index of the hash table contains (key, value) pair that was hashedimapped to the ith index of the hash table_ Fen MIS H4EMu Fu" Key Dn [, ) 0(1) KJ =8 V /-4 Ked- 8 Ji Key Ke s Ntcd 2Q hashi  eed ) noa un {nse,+ miotaiat buuco s hech,x oed grotun Io whee

## Page 10

0 kcn 9 hot RR J+ tpsh iJr 3 2J ~Ecn r_MrunFu: node hthidx Iptones

## Page 11

iat Rl aun in+Ca?) pm (im*) S+ Ustnde K tt nen bstnelet [0 ] 54 {NJ 20 blj { M+t ~Ecn r_MrunFu: +-8 (oljn Leel Tuntsh

## Page 12

-HcnauHa i:na Ruah>

