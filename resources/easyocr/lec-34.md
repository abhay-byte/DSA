# Lecture 34 (EasyOCR)

**Source:** `L34 - Heaps.pdf`

---

## Page 1

Perfect Binary Tree Perfect Binary Trees binary tree is said to be a perfect binary tree if all its levels are completely filled i.e. every internal node in the binary tree has exactly two child nodes. level 0 2 = 2 ' level 1 level 2 The height of a perfect binary tree is logarithmic. level 0 26 level 1 2 ' 7 =n level 2 22 level k 2k 20 + 21 + 22 + 23 + +2k = n This is a finite GP where, a = 20 =1 6 r=2 € #=k+tlv The sum of finite GP given as follows Aighest Leved 3 = a * [ (r#-1) / (r-1) ] Tt6 € L34 Heaps Page 2i 1 = 20 4 = 22

## Page 2

Substituting the values of a, r, and #, we get 1 * [ (2k+1-1) / (2-1) ] 2k+1_1 2k Heraht Therefore, k = logzn The number of nodes in a perfect binary tree that has n nodes at a height h is 6/2h+7 1= + h =0 [r1 2 height hz | 0 4 [zt] 2 2 h a 2 [21 L34 Heaps Page 2 4 Tr

## Page 3

Complete Binary Tree Complete Binary Trees binary tree is said to be a complete binary tree if all its levels are completely filled except for the last level which may or may not be filled: And, in case the last level is partially filled then it is filled in the left to right direction. 2' CBtv Petx p17 X Cet* The height of a complete binary tree is logarithmic. The max no. of nodes in complete binary tree that has n nodes at a height h is 7 Linear Representation of Complete Binary Trees 044  2i+/ Lea ic/ Viev I~5 '~6 7e @8 L 1 2   3 4   5 6 Inki | {1 }-132 A  e lc i| Viwv 5/2*2 623 3 2 3+2 = 8 L34 Heaps 2 0 20 22 Rbtv (Btv TT2h+1 i1 2i+2 W}n 2.1+224 2.1+1-3 2.3+1-7 Page

## Page 4

Heap Introduction Heap It is a kind of complete binary tree in which every node satisfies the heap property: Types of Heap Min-Heap optimized for operations on minimum element Max-Heap optimized for operations on maximum element Min-Heap It is a kind of  complete binary tree in which every node satisfies the min-heap property: The min-heap property states that value of each node in the heap must be less than the value of all the nodes in its left subtree and its right subtree: (Bt y nincap 3 2 5 8 L34 Heaps Page

## Page 5

Max-Heap It is a kind of complete binary tree in which every node satisfies the max-heap property: The maX-heap property states that value of each node in the must be greater than the value of all the nodes in its left subtree and its right subtree: CBt Y 8 5 2 L34 Heaps heap maxh lapv Page

## Page 6

Heap Implementation Implementation of Heaps eep ninteep k; 1 vedotz > Linear Representation of Heaps 2i+ | 17 2i+2 2   3   4   5   6 i12 3 2 3 2 | 7 | 5/ 4| 6 8 '1 5 Jeu0v27 8 2, +2 2 n 2' +) minteap Heap Operations 1. Push to insert an element onto the heap. 2. Pop to delete and return the smallestllargest element from the 3. to access the smallestllargest element withoc?opping from the 4.. Size return the size of the heap 1 5. Empty return True is heap is empty, False otherwise. @nst Wns Wnst L34 Page mjXH Jjaami € xed i J > 6} ) (Vca heap. Top heap: Heaps

## Page 7

Heap Operations Heap Push Operation 5 9 2 4s 4 | 6 @ 5 ;akjn) VieD legicl Heap Operation VCo) , VCa -0) 2 " v-PPp- baci ) 3 Tix me ni-heep (rp' 31 hec Pity (0 tx voor 8 TETSTATJ 8 3 8 =0 2 2   3  4   5   6   7 276 2 2 TT5 | 4 6 | 8 5 72 x 3 8 L34 Heaps sw Pop Swap( Page

## Page 8

Merge Ropes * N*3^ 7| se+ nl3n b0s 0-| hme cJs,`, 61 tC Fuo 07'6 7 € Merge Ropes c46,6 ] 4y Wcr 3 € 6, 9 ) 3 ' tDtoi + - Laeat Given the lengths of N ropes, design an algorithm to the' minimum cost to ~ Tre 4+6 =/0 connect these N ropes into one rope such that any point of time you can only merge two ropes and cost to connect two ropes is equal to the sum of their lengths_ F kchs Id+3 = 0 Sttk X Example Input [4, 3, 2, 6] 9-4 3 Output 29 4,3,2,6 7- 2 7 2 +3 < 5 y6 L0 7 4t $ ~ 9 FA 36 2 + 3 5 4+ (2+3) = 9 (4+6+3)+6 =ij L34- OaF La+ Tepeat +476) prek 16) Meqe-lt ~st 6rt compulet_ {csu+ 6 RI 13+2-i$ 3 8 79+6 : 5 Henpa Fijc

## Page 9

Build Heap from Array ~35 30 Building Heap from an Array 5 0 2 0 40 2 3 5 0 arr 10 20 50 30 140 {1v, 2' , $9, %2 , t 50 50 50 50 40 30 40 30 30 40 30 40 20 10 10 20 20 10 10 20 arr 10 20 50 30 Ao 10 2 arr 10 20 50 30 Ko 20 50 30 40 % Jin9 L34 Heaps Sor oca1va~) Ordey Kme" = Page

## Page 10

50 1 2   3 arr 50 40 30 20 10 40 30 20 10 p S0 17 arr 10 20 50 30 40 30 70 1 40 30 40 r0 Xme {oy Ar "I2 heapity I-is non-Ie8 0;7 = bt le38 - 4 13=8 non-Ird8 &+ ^oo - led ? 3 The heapify operation, in worst case, takes time proportional to the height of the node on which it invoked: The maximum number of nodes in a complete binary tree at a height h n / 2h+1 The total amount of work done at nodes which are at height h, (n 2h+1) * 8 (h) Therefore, the total amount otwoik derle at all the non-leaf nodes, h=l +lj" Jogab  2 ( n2h+1) Qh  L34 Heaps 670  6caiv9 hme' € ko8 ^-n/2 Page

## Page 11

logan _ 63, (n/2h+4) Qb togzn X (n/2h+1) * 0 ( h ) E ~ 2 h=1 '2 logzn h- (n/2h+4) - 21 2+3*2~ 2' 22 X (n/2h+1) 0 ( h)e Zc kzoJ te hz0 ~ O(^ ) X (n/ (2.2h) ) h.c h=0 nclz > ( 1 / 2h ) * h h=0 X (h /2h ) h-0 n.c ~0 (n ) L34 Heaps 8 o (hk 2 A+* ncl2 ` Page

## Page 12

[RJ[HW] Heap Sort Heap Sort Algorithm Given an array of n integers, sort them using the heap-sort algorithm. Example Input 2 3 20 10 50 40 30 Output : 2 3 10 20 30 40 50 20 2 3 20 10 50 40 130 2 10 50 3 40 30 50 2 3 50 40 20 10 30 2 L34 12 Heaps Page

## Page 13

50 40 20 10 130 40 20 3 10 30 L34 13 Heaps Page

