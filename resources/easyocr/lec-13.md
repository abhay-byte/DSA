# Lecture 13 (EasyOCR)

**Source:** `L13 - 1D Arrays.pdf`

---

## Page 1

Rain-Water Trapping Rain-Water Trapping Given an array of N integers representing height of N buildings, find the total amount of rainwater that can be trapped between the building such width of each building is 1 unit Example 10 Wo W, 33 0 0 1 o/8 : 6 7 7 7 9 0 | 2 9 4 5 6 + 8 9 (0 a-i +043) Ws+er Zh: 0 00 wj Ry ; bufuicg tP % A; -G+ : ) Ah; =( ; bo)e T 4; Q; - K; min ( @; W; ? h; - hi W; - W; : 0 ; - h; W M;a ( 9;, $ ) - h; IsF-h; i-1 ~i+1 Is}= h; J; 3 Li: LIS ID Aruys Page I' Rped mJx 9 17;) 9 N : (Io_iJ) m ax 0-+))

## Page 2

Isf- h; 2; 3 m a* ('_'W) W; (8,5) - h; 9; > ik (6xn)) Ya-/ > ha-' 3; = mJx (7i+,h;) (6r"__0-'7) ' hrj M J* (T;+, h; ) 1; M?X 0_-') 7 (; T; AC;) A; ) W; MJx MjX A[_i]) = Aro__+-J) 4;-, Qo Ao Wa 8 10 h 0T7l 3 L2LD 0 3- 313 [ 3 3 bbLsb 3 [L2L2L2la Q; mJX Q;-', h;) T AjX (t,+',hi ) a () W; mnlli;) hC;) ( ACr,ni7) njX MpX (Ao_i7) 7 2 '} 8 < %1 tmm =w;  = 8- h; uak i++ LIS ID Aruys Page 2 mia max Th+l (;-', Min 17 | Mjx 2[ | 7 7

## Page 3

8= mjx (hlo ..i] ) j2j e |se T = MJX A - hy Wj= J" - - , LIS ID Aruys Page } (hCj --n-'J)

## Page 4

[HW] Product of Array Except Self Product of Array Except Self Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]: The product of prefix or suffix of nums is guaranteed to fit in a 32-bit integer: Example Input 2 3 4 2 3 | 4 | 5 Output 2 3 120 60 40 30 24 LI3 1D any Arrays Page -

## Page 5

[RJIHW] 3Sum [HW] https [Ileetcode com/problems/3sum-closestL [HW] https [Ileetcode com/problems/AsumL 3Sum Given an integer array nums, return all the triplets { numsi, numsj; numsk} such that i != j, i!= k and j != k and numsi + numsj numsk == 0. Notice that the solution set must not contain duplicate triplets. Example Input 2 3 4 5 1 | 0 | 1 | 2 | -1 -4 Ll3 ID Arrays Page

## Page 6

[HW] 3Sum Closest [HW] https IIleetcode com/problems/3sum-closestL LI3 1D Arrays Page

## Page 7

[HW] 4Sum [HW] https [Ileetcode com/problems/AsumL LI3 1D Arrays Page

## Page 8

DNF Sort DNF (Dutch National Flag) Sort tme: 0(a) Given an array containing Os, Is & 2s design an algorithm to sort the array: Example Input N=9 3 5 6 2 | 0 | 1 | 2 Output 2 3 5 6 8 [0_low -'J zev $ Cmrd_ ngh] Ynk 0| 0 | 1 | 41 | 1 | 2 | 2 [ low mid-'J = ones chight ^-'7 5) tus t tne t0 tce + +nc 9 nid (qals low = Ioc: Aigh (oc ' ^pxt +wo % Pur tne Tejim tne next Fem The idea behind the DNF algorithm is to partition the given array into four parts using three pointers low, mid & high and then to iteratively shrink the unknown part to zero elements so that the array is sorted. Mte his^ zeros ones unknown twos 2 3 5 8 arr 2 0 2 47/ 77r7 zers 0^es +vos 94 m;47,4 Clou? ) (Gmmid) ==6) swp (ort Iow++ wdt- low high 1 11 (cm (mid) =3') 2 ~3 5 6 8 3+ ++ arr 2 0 2 ze/5 Daes unis twos (oly Tinbh Sswoplon (md),an(hyv) YT 3 | 5 8 arr 0 1 | 1 | 1 | 1 2 kigh -- ) LIS ID Arrays Po;ats jvu Lunpre Poichs Where Ik Ist e/ (u+ Yej n uak m mid Page

## Page 9

TTYT 3 T 4 | 5 8 arr 0 | 0 | 1 | 1| 1 | 2 Kgh -- ) ZeYds on8s Un1 lolo low) 5 3thd arr 0 0 | 2 2 Pl 7eyus d^rS tws Stovs mi4 -0 >1-1 hijh LIS ID Arrays toS nid 20 Page

## Page 10

Counting Sort m?p I 1i14 Rr"v B1eTETE Counting Sort 3 Given an array of N non-negative integers,  design to ele[ok] sort the array such that each array element is <Fa given integer K: Example e' Siv 00 | | 2 2 2 33 Input N=9,k3 2 5 8 3o0808 800 Output 2 3 | 4 | 5 | 6 | 7 8 0 T 0 T1TT 2T 2T2T 3 T 3 Ia '02 2a 6   %6 Dr 4 Srts (tw @a Os 1 I 24 2 6 cuahng Sot LI3 ID Arrays Page 10 Kntalgorithm 72 2-3 37 2 2 6

## Page 11

[RJ[HW] Generalized Counting Sort Generalized Counting Sort Given an array of n integers, design an algorithm to sort the array such that each array element is in the range [ I, r ] assume <=r Example Input n = 10,1=2,0=4 1 | 2 | 3 4 | 5 | 6 | 7 | 8 9 4 3 2 | 2 | 4 | 3 | 5 | 4 | 5 2 Output 2 3 | 4 5 | 6 | 7 | 8 9 2 2 2 | 3 | 3 | 4 | 4 | 4 | 5 | 5 L13 ID Arrays 11 Page

