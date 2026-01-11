# Lecture 41 (EasyOCR)

**Source:** `L41 - Dynamic Programming.pdf`

---

## Page 1

Rod Cutting Problem Rod Cutting Problem 3 Given a rod of length n and the prices of its pieces of different lengths to n Design a recursive algorithm to find the maximum profit you can make by cutting the 7 =18 rod and selling its pieces. +8 Flo Example 2 3 Input.T=18 45 E5 length 3 5 | 6 7 8 prices 9 10 | 17 17 20 Output 22 Explanation 5(2) + 17(6) = 22 WC 2 #a = €z? x ( 4 f +A t Ande Mjx- Preft fo- trm ( Tod Y Ieam ~ ca^ Moke prices = { Po, P1, Pz, I-j +Po +Pz +Pn-1 Mjy %- + HQ-) fa 73 R 1?X p {a- Recursive Case Let f (n) be a function which computes the maximum profit one can make by cutting a rod of length n and selling its pieces then f (n) = maxc +f (n-j) Base Case fl) What is the reason behind exponential time complexity ? fn fn-1 In-2 fo LII Dynamic Programming from 21J {a-2 P[-1] Pjge

## Page 2

In-- In-2 fo -n-T Un-2 fo fn-3 fo fn-3 fo fo fo Top-Down Dynamic Programming fn Jo tv fn Tn-1 In-2 fo un'i " -n-- n-3 n+ | In-2 fo fn-3 fo fn-3 fo -n-3 fo fo iait: - J k? P where_ f (i) is a function which computes the maximum   profit one can make by cutting a rod of length and selling its pieces. Anul~g Bottom-Up Dynamic Programming aPo =fn J0, ~ k?- J8; dp JQ; 5# where , Pind m m'x 0 + 1 f (i) is a function which computes the maximum profit one GoRt #or 0 can make by cutting a rod of length and selling its pieces. ~03 From recurrence_ Rnz L4I Dynamic Programming -n-3 -n-3 Qa=&a 98p;-i dnaf Jpc ) 3 Pjge

## Page 3

D'yy 760 " From recurrence _ Rn- 1 f (i) = max pli-1] + f (i-j) ; i>0 j-1 Therefore , ~o = 0;-+#; dpti] = max pli-1] + dp[yj] 171 _ j-1 ix P;1+#;; 9 Yi - )?( LII Dynamic Programming Mjx Pjge

## Page 4

Partition Array for Maximum Sum Partition Array for Maximum Sum Given an integer array, partition the array into (contiguous) subarrays of length at most K such that after the partitioning each subarray has their value changed to the maximum value of the subarray: Design an algorithm to find the largest sum k-3 of the given array after partitioning: Input K=3 1"c : ~9 2 7' 15 7 | 9 2 10 243 3 & 3 2 ! 3 9   9   9 "" %: 64 | ~ 3 <3 25 32} =6 Ir | 9  ( ( 0 tinj me Mix Svm 8o Pa-tNwizy Gwlo _ 0- ) j+ 4R-1 )+i= n-" 5 mJ;)xCj-inY Sov: Sum Ioo ++ > Fc )- 7 Pind m? 0-1 pont Koninj oxiC i  "3 R; = mIx T S-i+) t + Sol-e tnis jei =(j+i) In" ^ex+ wt Recursive Case Let f (i) be a function which finds the largest sum of the given array that starts at the ith index after partitioning then, 1#" j<i+k and (i) max max (arr__j)) (j-i+1) + f (j+1) } j = Base Case ;it i<0 #lzzn) =0 Dynamic Progrinining Fagt ma7i j deude

## Page 5

What is the reason behind exponential time complexity 02 40 Top-Down Dynamic Programming A+) Jpa where, f (i) is a function which finds the largest sum of the given array that starts at the ith index after partitioning Bottom-Up Dynamic Programming zJ8.  X dp 4 From recurrence, <itk and < n (_) max max (arrg_j) (j-i+1) + f (j+1) } Therefore, Lsitrand < n dp[i] max max (arri_j) (j-i+1) + dpbj n Dynamic Progrinining Fagt Oipo=fn J;a#; '94 JPC) JPaefn=0 210; ~ Qos/ Case Rml ~

## Page 6

[RJ[HW] Tenzing and Balls Tenzing and Balls C Tenan]end Halla #ecee Tem LT4nt Oenenodan Fr tloiuty Luhan [44l4ua70474eadriinientem44 Lcoeinautterlun a |eaa afae a-aklela =0 Seettus Me "mendotdeltodntdviatd eda ceretR Cena enet deth tctotilo' - MEnaa]nde Tianrn-0nt8e eertntean Leau&m-ttffntteel Fealateel 47EAEAtsereA4An #eed 7 4 Iu Ounean Ad [= @TA[a Jr Atul Mniu: E 4uLAut Recursive Case Let f (i) be a function that find the maximum no of balls Tenzing can remove from ali _n-1] then; max { f(i+1) , max ( (j-i+1) + f (+1) ) } such that ali] is equal to a] ji+1 Base Case What is the reason behind exponential time complexity [Xunmic Fucmmmminy Fac (

## Page 7

Top-Down Dynamic Programming where (i) be a function that find the maximum no_ of balls Tenzing can remove from ali _n-1] then, Bottom-Up Dynamic Programming dp From recurrence J<n max f(i+1), max (-i+1) + f (j+1) ) } such that ali] is equal to al] 1=1+1 Therefore 1<n dp[i] max { dp[i+1], max ( (j-i+1) dp[i+1] ) } such that ali] is equal to ali] 1 =1+1 Time Optimization Bottom-Up Dynamic Programming [Xunmic Fucmn ar ]

## Page 8

[Xunmic Fucmn Fac 4

## Page 9

[YTIHW] Best Time to and Sell Stock IV https:IIwww youtube comlwatch?v-bXq1-S3hWNY&t-2953s Best Time_to Buy and Sell Stock IV You are given an integer array prices where prices [i] is the price of a given stock on the ith day, and an integer K Design an algorithm to find the maximum profit you can achieve by completing at most K transactions: Note You may note engage in multiple transactions simultaneously i.e. you must sell the stock before you again: Input K= 2 2 prices 2 4 Input K= 2 0 TT 2 T3 T 4 5 prices 3 ~2 | 6 | 5 | 0 3  2 3 4 n-1 L4I Dynamic Programming Page 9 Buy buy

## Page 10

1-1 i+1 n-1 Recursive Case Let f (i, k) be a function which computes the maximum profit one can make by completing at most k transactions starting from the ith then, n-1 f (i,k) = max { f (i+1, k), max {prices[i]-prices[i] + f (j+1, k-1)} } j=i+1 Base Case L4I Dynamic Programming Page 10

## Page 11

What is the reason behind exponential time complexity ? ~2 3 4 n-1 Top-Down Dynamic Programming L4I Dynamic Programming Page 11

## Page 12

K (N+1) x (K+1) where, f (i, k) is a function which computes the maximum profit one can make by completing at most k transactions starting from the ith day Bottom-Up Dynamic Programming K (N+1) x (K+1) where, f (i, k) is a function which computes the maximum   profit one can make by completing at most k transactions starting from the ith day L4I Dynamic Programming Page 12

## Page 13

From recurrence, n-1 f (i, k) = max { f (i+1, k); max{ prices[i]-prices[i] + f (j+1, k-1)} } j=i+1 Therefore, n-1 dp[i][k] = max { dp[i+1][k], max{prices[j] prices[i] dp[i+1]Ik-1]} } j=i+1 i+1 j+1 N (N+1) x (K+1) L4I Dynamic Programming Page 13

## Page 14

[YTIHW] Count Palindromic Partitioning https Ilwww youtube comlwatch?v-VPlphqlYzIA&t-110s Count Palindromic Partitioning Given a string of length N, design a recursive algorithm to count the number of its palindromic partitioning: Example Input N =5 1 | 2 | 3 4 a | b | a | & a i+1 i+2 i+3 L4I Dynamic Programming Page 14

## Page 15

i+1 i+2 Recursive Case Let f(i) be a function which counts the number of palindromic partitioning of str[i n-1] then, n-1 f () = Xf(j+1) such that str[i . . . j] is a palindrome j-i Base Case L4I Dynamic Programming Page 15

## Page 16

What is the reason behind exponential time complexity ? fo f1 f2 fn f2 fn f3 fn f3 fn fn fn Top-Down Dynamic Programming fo f2 fn f2 fn f3 fn f3 fn fn fn L4I Dynamic Programming Page 16

## Page 17

where; f(i) is a function which counts the number of palindromic partitioning of str[i n-1]. Bottom-Up Dynamic Programming dp where, f(i) is a function which counts the number of palindromic partitioning of str[i n-1] From recurrence, n-1 f () = }-{ (+1) such that str[i j] is a palindrome Therefore , n-1 dp[i] = X dp[ij+1] such that str[i j] is a palindrome j-i L4I Dynamic Programming Page 17

## Page 18

i+1 j-1 2   3  4 j-1 N-1 L4I Dynamic Programming Page 18

## Page 19

j-1 N-1 i+1 N-1 NxN L4I Dynamic Programming Page 19

## Page 20

[YTHHW] Split Array Largest Sum to also solve this problem using binary search [DP solution] https IIwwwyoutube comlwatch?v-S6KpZiuvkFA&t-133s Split Array Largest Sum Given an integer array nums, and an integer K, split the array into K non-empty subarrays such that the largest sum of the any subarray is minimized. Design an algorithm to find the minimized largest sum of the split Input : K = 2 1 | 2 | 3 4 7 | 2 | 5 | 10 8 2 ~3  4 L4I Dynamic Programming Page 20 Try

## Page 21

i-1 i+1 L4I Dynamic Programming Page 2 1

## Page 22

Recursive Case Let f (i, k) be a function which finds the minimized largest sum upon partitioning splitting arr[i n-1] into k non-empty subarrays then, f (i, k) = min { max [ f (j+1,k-1) ] } j=i Base Case L4I Dynamic Programming Page 22 Sarrli: . jh

## Page 23

What is the reason behind exponential time complexity ? 2   3  4 Top-Down Dynamic Programming k (N+1) x (K+1) where, fli,k) is a function which finds the minimized largest sum upon partitioning splitting arr[i 0 n-1] into k non-empty subarrays L4I Dynamic Programming Page 23

## Page 24

Bottom-Up Dynamic Programming K dp (N+1) x (K+1) where, fli,k) is a function which finds the minimized largest sum upon partitioning splitting arr[i n-1] into k non-empty subarrays From recurrence, <= n-k f (i, k) = min max [ Sarr[i . jl f (j+1,k-1) ]} j=i Therefore, n-k dp[i]Ik] = min { max Sarrli . JJ   dp[j+1]Ik-1] ) } = L4I Dynamic Programming Page 24

## Page 25

[HW] Matrix Chain Multiplication [HW] Burst Balloons on Leetcode Matrix Chain Multiplication MCM ) Given a sequence of N matrices {A1 Az , Aw}, design an algorithm to find the minimum no. of operations (i.e. scalar multiplications) required to multiply them, assume the dimensions of the matrices are compatible for multiplication: Example Input N = 3 2 Output 16 a11 a12 b11 b12 b13 C11 a21 a22 b21 b22 b23 C21 C22 C23 a31 a32 2x3 C31 C32 C33 3x2 3x3 Input N = 3 2 | 2 | Input : N = 4 4 L4I Dynamic Progrutting C12 C13 Pjge _

## Page 26

Aj Ak Aj Recursive Case Let f (i, j) be a function which computes the minimum no. of operations required to multiply a chain of matrices { Ai , Ai+1 Aj } then, j-1 f (i, j) = min { f (i, k) + f (k+1,j) + d [i-1] * d [k] d[i] } k=i L4I Dynumic Progrtning Pjge _

## Page 27

Base Case What is the reason behind exponential time complexity ? Top-Down Dynamic Programming NxN where, f (, j) is a function which computes the minimum no. of operations required to multiply a chain of matrices {Ai , Ai+1 Aj} Bottom Up Dynamic Programming NxN where , f (i, j) is a function which computes the minimum no. of operations required to multiply a chain of matrices {Ai _ Ai+1 Aj} L4I Dynamic Progrutting Pjge _

## Page 28

From recurrence, j-1 min { f (i, k) + f (k+1,j) + d [i-1] d [k] d[] } ;i<j k=i f (i, j) = ;i=j Therefore, j-1 min { dp[i]Ik] + dp[k+1]L] + d [i-1]*d [k]*dli] } ;i<j k=i dp[i]D] ;i=Fj i+1 NxN L4I Dynamic Progrutting Pjge _

## Page 29

[YTIHW] LIS-K Problem https IIwww youtubecomlwatch?v-9322KuDul8&t=75s Longest Increasing Subsequence (LIS-K) Problem Given an array of N integers and a non-negative integer K (< N), design a recursive algorithm to compute the length of the longest increasing subsequence that starts at the Kth index of the given integer array: Example Input N =7,K =1 2 3 4 5 6 2 5 | 3 | 0 | 4 6 Output 4 Explanation The LIS starting at index is {2, 3, 4, 6} i+1 i+2 i+3 L4I Dynamic Programming Page 29 1st

## Page 30

i+1 i+2 i+3 Recursive Case Let f(i) be a function which computes the length of the longest increasing subsequence that starts at the ith index of the given array of integers then, n-1 f (i) = 1 + max f (j) Alj] >= A[i] j=i+1 Base Case What is the reason behind exponential time complexity ? L4I Dynamic Programming Page 30

## Page 31

fk 'fk+1 (fk+2 _ fn-1 fn-1 (k+3e fn-1 (k+3" fn-1 fn-1 fn-1 Top-Down Dynamic Programming fk fk+1 (fk+2 fn-1 (ik+2 ` fn-1 (k+34 fn-1 (k+3" fn-1 fn-1 fn-1 L4I Dynamic Programming Page 31 Tk+2

## Page 32

where , is a function which computes the length of the longest increasing subsequence that starts at the ith index of the given array of integers. Bottom-Up Dynamic Programming dp where , f(i) is a function which computes the length of the longest increasing subsequence that starts at the ith index of the given array of integers. From recurrence, n-1 f (i) = 1 + max f (j) ALi] >= A[i]; i < n-1 j-i+1 Therefore , n-1 dp [i] = 1 + max dpli] j-i+1 L4I Dynamic Programming Page 32 f(i)

## Page 33

[YTJHW] LIS Problem Try to solve in O(nlogn) [DP solution] https IIwwW youtube com/watch?v-9322KuDul8&t-75s Longest Increasing Subsequence Problem Given an array of N integers design a recursive algorithm to compute the length of the longest increasing subsequence in the given integer array: Example Input N =7 2 3 4 5 6 2 5 | 3 | 0 4 6 Output :5 Explanation The LIS starting at 1st index is {1, 2, 4, 4, 6} L4] Dynamic Programming Page 33

