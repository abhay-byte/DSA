# Lecture 27 (EasyOCR)

**Source:** `L27 - Linked List.pdf`

---

## Page 1

Introduction to Linked List D's Quous bcaron 37 52 40 20 Introduction to Linked List A Linked List is a linear data structure that is used to store a sequence of values of the same type_ at [; ] t(rr +: ) 'at 4m [ 1 { 10 , 22, 30 , 40,50 _ 0 < | = 0-1 2   3 4 wntguous awy + ` * siz 8Cin) at id 201 30 40 5 D 0 |lo( a buo 206 4r 46 40 40 40 MJX' ste J atroj ~) 206 208 205 mited Mj> 6] 206 20 5 amt_ wnh gudus Z {'0 have Luo B (veev,7 Qt6] '5 L) Tesi1e op' @"sF iF $ & '0 howoever _ thpa Q ve'j Visualizing a Linked List Uaxed ~st 10 20 30 40 50 foworo-Lst ( (++) ioo 30 400 Sob 10 Lob 20 30o 30 460 40 $0' 50 aui ^od € ~de aodu ad € Gia) d boked mst 1s klieu'n Inod*s addy  ne xt 0 node L27 Linked List wnt "hle } )) exrCnsive Jynomrc Jaked SicayJ vji 9 ^P Pape

## Page 2

class ListNode int main( ) ListNode t nei ListNode( 10) public return int val; ListNodet next; ListNode( int val) Custarort) (*c) . va L OD this->val val; od this->next NULL; 10 NUL }; Stack Heap 9iext Unkea Ust ( fofword 4a,) (Ustn er* ) stt ) Linked List Terminology 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL Heod Tai Nok Node head (macd = (Ustnode #) @nxed Mst te tail Aeod ph Rstade#) Yoo 1 00 206 3oo 400 NULL 10 206 io 20 306 200 30 400 300 40 NULL Ta ; Nude class ListNode DL naia tuin public Lo 0 Lint val; head J 40; ' Pry Qad ListNode - next; bo7 ListNode: prev; (~Xv' ierthdelek) (ey 6 hoas ListNode(int val) this >val wal; Doh tnis >next NULL; 07 ? verJ  Htuent this ~prev NULL; end $ L27 Linked List n - uil S;calj Sod Loplonz ) alorJ) teorespots w<u Lstaode # ) Pape

## Page 3

Linked List Insertion Linked List Insertion node in linked list can be inserted in the following ways at the head i.e. at its beginning at the tail i.e. at its end at a random position i.e. at a given index U (6 0 Qo 300 400 S70 1p 10 J L 3) 30 J40 -Su Insertion at head 40 - $7 '0t %/: 0-10- 20 30 in+ 0 = I0/ Ido 600 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL {4 6 3 Bo head  ' Ustade * 0 aew ustnode " hoe: (lstcode*) 0 -aexb heed 0( 1 ) 2 ' 3  head = ^ ) Lo - 20 - 30 5 40 -57 Insertion at tail 30 _ 40 3) Sd id - %p 602 100 200 300 400 500 600 10 200 20 300 30 400 40 500 50 100 +ail 5) head usta ode K 0 = aep bstode (Lstnadet) 2. bstive K toi) de Tsil (kcat) ) 3 . tuil 4 = ^ ; Qtcv vl Ineenticn at indev L2? Linked List Lo)) 360 20- (66) / next Page _

## Page 4

ftcv 8 v? l Insertion at index 100 200 300 400 500 610x 10 200 20 304 30 400 40 500 50 NULL 600 100 J5|Al 30 0 head 7 aewn Wst node (val)) 660 I ~ W'stnode 0 l'st aa Prev ~ ) 2 ` 7txt 3 0 + next 7 2 4; fywv ^ / L2? Linked List Pyrv 7 0'X+ Page.

## Page 5

Linked List Deletion Linked List Deletion node in a linked list can be deleted in the following ways from the head i.e. from its beginning from the tail i.e. from its end from a random position i.e. from a given index Ld - 20 9 30 + 40- 57 Deletion at head ` - }o-) 40 -) n %/8 : 100 200 300 400 500 kne T0 200 20 300 30 400 40 500 50 NULL 2eo 1oJ kmp = heod ',) head 6( 4 ) heod = head-next [eke 20 - 30 7 60-}2 lb ) 26) 30-540 Deletion at tail '/8 : lxr Himt: oln) 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NUL L27 Linked List Page 8/q : kr? ) l0 - /r ' spale : 0C, )

## Page 6

TUU Zuu SUu 4UU JUu 0(i ) 10 200 20 300 30 400 40 500 UL 100 head luv Prey next = nuii) Deletion at index 22 3 100 200 300 400 500 10 200 20 300 40 500 50 NULL 100 head (a_') Lur 2 Py ?v=n*XY) 9arrt 3 delek Wr ) L27 Linked List Page Soale : " rev Dev Qrev = Wy deee Qrev Jetnoco prev luv next wr-> P rev

## Page 7

Linked List Length Linked List Length f=s The length of the a linked list is defined as the no. of nodes present in the linked list_ 100 200 300 400 500 Lat eYylzxs 10 200 20 300 30 400 40 500 50 NULL 100 head find tt (e' " 1 tne Ll + (heet ) { J (head .^0/) ~e0 ; 100 200 300 400 500 next ) , 10 200 20 300 30 400 40 500 50 NULL in+ % = T0 100 head (0 7 30 1) 40 hm} 4(^) t6-) + € } o6) +le) Int computeLengthRecursive(ListNode head) hek, JU base case (head MuLL) {// linkedList 1s empty 100 200 300 400 500 return 0; hedtbo 10 200 20 300 30 400 40 500 50 NULL recursive case f(head) find the length of the give I71. ask your friend to find the length of 2 storts from the node Ahich cones after int computelengthRecursive(head->ne heatasoo return 1 3 beat headwt hme Oln ) Lz? Linked List fCheod - 1++) X+l heakvo Rad 37d0 Marc

## Page 8

head wt hme Oln ) space: o()_ + Jve k (o R+il Lz? Linked List Puxe 8

## Page 9

[RJIHW] Searching in a Linked List 'IP' t7 /o' t+30 ')c' koe %' {olse Searching in a Linked List Given a linked list and a target;, check if the target is present in the linked or 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL 100 head 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL 100 head L27 Linked List Page not.

## Page 10

Reverse a Linked List Waip tewrsise Jla' . + [rj [#w ] JF Tevrtse t1e Riav '0 Reverse in a Linked List 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL iIp : 100 head 500 400 300 200 100 %p 50 400 40 300 30 200 20 100 10 NULL 500 head 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL 100 20| #) 460 head kmp 100 200 300 400 500 10 NULL 20 100 30 403 40 500 50 NULL 100 360 _ (NY I. kak 2 Qux Anert while head UStaider) nvll / 2. Luy ~ptey; Lvt Ar ev = {uy ; 24y 7 heaa 3 ~ 4 - (MY teme ; dl/ ) hmp kmp Io €= <0 6 3 F> 50 L27 Linked List Page [0 ey Gistnede Jext Zavie Ptev Hime : O(o ) Pycv spall Prev

## Page 11

4 0 Em) 50 WY Zvy 100 200 300 400 500 10 200 20 300 30 400 40 500 50 NULL 100 head L27 Linked List Page Io & < ( %

## Page 12

[RJIHW] K-Reverse a Linked List K= 2 K-Reverse in a Linked List 100 200 300 400 500 600 10 200 20 300 30 400 40 500 50 600 60 NULL 100 head 200 100 400 300 600 500 20 100 10 400 40 300 30 600 60 500 50 NULL 200 head 100 200 300 400 500 600 10 200 20 300 30 400 40 500 50 600 60 NULLI 100 head L27 Linked List Page 12

