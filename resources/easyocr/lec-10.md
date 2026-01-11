# Lecture 10 (EasyOCR)

**Source:** `L10 - 1D Arrays.pdf`

---

## Page 1

Bubble Sort Bubble Sort Given an array of N integers, sort the array using the bubble sort algorithm: Example Input Bubble Sort DNF Sort Sott Tda) loun"ag Sort 50 40 30 20 10 Selww Output Insthun Soct Sor+ Rewrsibn 10 20 30 40 50 Metj} Qurlk Sott Heaps Htap Sost The bubble sort algorithm works in passes such that in its each pass; we Slace 30 the largest element in the un-sorted part of the array to its correct position. 40 3 0 unsor+ed 30 20 10 4 < 1-1 4o % 8 20 I0 2 , 3 wmp Poss 40 50 7y,10 3 , 4 4o 30 Lo 56 > Aes 02 ) < 4 2 40 30 20 /0 50 55 35 20 10 50 2 3 tmp  unsottpd Soated 2 , 3 0= 2 1 - 2 I-j ^4 30 10 50 2 Poss 6 4 J 2 3 8=2 30 20 *x:su 3 30 20 Iv !wo S Sorrd jti 2 wmp = q-s 10 40 50 = 17 3 unso( + d 1-3 wmp 23 Poss 20 x6 &t J7 20 10 30 45 57 04 ) 2 2 Sockd wmp 1-5 30 40 =4 LIO ID Arnays 3 O-i = A- = 2 3r0 Fajc

## Page 2

wmp 30 40 =4 unsothd 9- 4 wnp A- = pess i0 2o Z0 40 50 04 ) < | BS wiM Sitc N, for 40 aroj % Acve 0 -' Pas ses 8-1; izan-'; 6+) the 8 te im pass , 5 (ard 'st eement 8o am( ] t 8ts (nt Dos _ ~1 4 ? 171 3 7 1-2 l-2 2 ~ 1-3 i:3 0vss [ ~ 1- 9 6~ 4 (pm (' m Pjss j jti 121 4 0- | 0 412 n-i + 0 #oo +4} void bubbleSort(int arr[], Int n): #oa? Tor (int 1; i  0 40 2 0-) +0-1 +n -0 1 in the Ith, place the largest ele part of tne arr[] to its correct 0 + 21-2 -2 fo5 {intafr[il 1; iil} / 3 2 (a+i) -0 arrpilrr[3Tr irrl}  1]) ; 3 t 20-3 9- 3 0 + ^ (a -i) 2 tine, 2 10o 2 LIO ID Arnays l =4 4h Jor ( fa t Picce unsosk4 ^-S Qot 40-01-) Fajc

## Page 3

tine 10o2 41 tonst Io  0(q+) Lbd-" St 6A[1 16 2o 30 40 055 _ Rzs (s5 4t 'f (toJ %s aheodj then w i M g+p cfkr ''e' we'U do ne olj 0- cmp 86 Vra-O3a LIO ID Arnays "57 21q 3*4 p)ss Sozk d 5 $ (st Do s$ Fajc

## Page 4

Selection Sort Selection Sort Given an array of N integers, sort the array using the selection sort algorithm. Example Input 50 40 10 30 20 Output 10 20 30 40 50 The selection sort algorithm works in passes such that in its pass we place the   smallest element in the un-sorted part of the array to its correct position. vnseted [0 50 nin Idx :px2 tn P?ss Sw'p (ar [67, ar(22) tn iJ> 0 Low : Pos = 50 30 40 20   Unsorkd St 0oss mijxeX%4 SF low pos Swap av [11, 4w [42) v 40 30 So7kd Nialdx 3 arv [27, 4nts) 0J55 Swjp UYv Dos 'dx 4 nla Ij = Sorkd 5v pss Swapl am01, An [w)) / (os: Ss wiM Site 1 for 0n ao] % D Aays /452 each Sor kct Unfork 2nd 46 x:x 4 34 2/ ';Jx tw -

## Page 5

SS wiM Site 1 jor an aoj  % ^cve 0 -' Pas ses 8 ++) 3 ({= 0 '/ 8 4 ^-2 ' Jor tne {n the Rass tne oyted RSt eement io smji) A WrY Qos: anr ( 7 to {ca + 9 Jx i m iIJx = l #wm? void selectionSort(int arr[], int n) { 0- +LL_ for (int 1 '0; 1 n 2; i++) { n-2 0- | 2 + 0- | n (n-') I/in the ith pass, place the Smallest 2 - 11 unsorted part of the arri] to its cq 3 + A-| ^-3 11 1.e, ith index Posses int minIdx 1; // at the start 0f the Unst for (int j =1 + 1; ] < n _ 1; j++) if (arr[j] arr[minIdx]) { // you 2 1-1 +0-1 minIdx J; // therefore update oCal ) 10 5+ 4 0 3 0 2 D swap(arr[minIdx] arr[i]); 0 m m'^ T/xed 0 $5 Place unst ^tayt

## Page 6

Insertion Sort Insertion Sort Given an array of N integers, sort the array using the insertion sort algorithm: Example Input 50 40 10 30 20 Output 10 20 30 40 50 The insertion sort algorithm works in passes such that in its each pass; we place the first element in the un-sorted part of the array to its correct position in the sorted part of the array: So h" 10 30 20 S0. uaset+ed 2 40 qw [i ] Key St Q?5s 5a 30 20 U So l aw C1 7 210 2 p?ss Kej? uasotkd 40 5d 30 20 Sotpd 50 aw[37 30 37* Poss LIO Iol ?  7 Ke] ATY Pule

## Page 7

20 9 40 basotkd Key = 4h pss IS wlM Ste 1, for 4n (rto] % ACve 0 -1 Pas ses (++) 3  (i=1 ; 1z=a-i ; for arC;7/ Kej - + its +he Kc) '^ So} ia me lTy tne Onro] L #wmr void insertionSort(int arr[], int n) { for (int 1 = 1; 1< n - 1; i++) { 0 + 0 int arr[i]; + 0 ; 2 : ^l:2 I/ in the ith pass, insert the key in the sorted part of the array 2 +v 0 int j while (j and arr[j]) loast arr[j 1] arr[j]; arr[j 1] = 4-1 1+-2 * 0 J e €. otder tncn I8 aw6j 's pt te ~(DSC en kua" W r' N 26 16 30 2c u n Sd 50 40 J LIO - ID Sorpd aw [77 = Z0 s/kJ Pos - Octt ; key "2? key key ; 0 (0l) Worj F NTY Puee

## Page 8

26 16 30 26 36 wo JD 50, 49 2.0 3 0  4 6 X W_2; (0 30 ~ 4 6 3 6 20 30 6 40 26 Y 0 5 C 2 6 4 6 16 36 (6 aw 0% "5 'f fhpo alr radj d0 2 Qo 6lj '^ 0ass lmp 8v M-1 Comp 0 6) tobl h'me Sb 0 Il pusseS QCros) LIO 28 yoor Sored &y U eoch np'UU ATY Pule

## Page 9

Search Iog," I= /024 = 2" Binary Search binay ] Given a sorted array of N distinct integers & an integer T, implement the binary search algorithm to find the index of T in the given array: note output -1 if T is not present in the given array: iv 19 132 =/v Example Owoj Input t2 /o V N=7;t=2u "s 01 0y bmplf 9R' - 10 20 30 40 50 60 70 787>#54 Output : 1 Xi > Xl 7) S'0tu) space Amotwrally Tig ) Kaootw)HvJe 26 ) ecf) ~is f^ bihbj s Pattn DX 3 X17 Y2 {(1Y jnc Pn fc 7 X +d Jns 6 [s e ] ~0 m = St e e= ^ -| at Cn ] = = & tvc ) (falc ) matun) tL cCm  t> uw Cm? {ood the at  iJx 'n' turau Cs,e J +o 8+p e] + Cn+1,e) S2-e s* IDAMvsFSL   Binary "'Gt an[1] Sortd A0^dtor/( Nt (On w & #lx,)>Pt2) Moabha ^ea- rily Mobtn / aqa _ de 'ou' v e [S,m-1) CS, (0 < r wAile Bi' )

## Page 10

Slzt 4 a = 0 2 " 4 9/1 : 2, 2 = kti =2- 3 #ikev o No s 4 5 ~ 2, Vo5^ K+l 21 6( (o6,2 1 - tuke Lk= Iu5 0 6 6 Ama > Pale (0 6 e While Bicd ) Wuorst An')5} 6ath ^)y Ivgn + J n / 8 wnsh 2 k 2k - F bl $ 1o52 I52} lej & 

## Page 11

First Occurrence in Sorted Array 0 3 4 S 6 +z2 Lo 20 Z0 Zozo 20 3 0 ) Jas =m S-0 m-3 e= 6 First Occurrence in Sorted Array Given a sorted array of N integers, & an integer T, design an t-20 algorithm to find the index of the 1st occurrence of T in the given array: Youve to output -1 if T isn't present in the array: Example L  3 40 20 20 26 3 0 Input N = 8 ; T = 30 2 3 4 5 6 7 10 20 30 30 30 30 40 50 S30 Mzl e=4 Output 2 e-$ 5 C_$ 2 {alrqey M = S + (e_s) bvea ?"ro woc ' hoc(en S+ (5-) 2s 7 6 2 $ + 5 S -< C-5 ev i+{AY6  2 ovex Plow Caa (S+e ) 5+5 < 5 LlO ID Arrays Page 1 [ Telede hipni

## Page 12

[RJ[HW] Last Occurrence in Sorted Array Last Occurrence in Sorted Array Given a sorted array of N integers, & an integer T, design an algorithm to find the index of the last occurrence of T in the given array. You've to output -1 if T isn't present in the array: Example Input : N = 8 ; T = 30 2 3 4 35 ~6 10 20 30 30 30 30 40 50 Output : 5 LIO ID Arrays 12 Page

## Page 13

[RJIHW] Count Occurrences in Sorted Array Count Occurrences in Sorted t=20 Given a sorted array of N integers, & an integer T, design an algorithm to count the total no. of the occurrences of T in the given array: You've to output -1 if T isn't present in the array: 2 Example ILD 30 0 20 Input N = 8 ; T = 30 0 2 3 4 5 6 10 20 30 30 30 30 40 50 Output 4 Ic =s fcA lc - fc +I LIO ID Arrays Page 13 Array

