## Generates 8-digit hexadecimal


Step 1 understands the problem and its scale:
to get every single number that can be generated to 8-digit hexadecimal, it would be 4,294,967,295 because this number in hexa is 0xffffffff
To not repeat the numbers, we must store the numbers at the list to database (to check if we already generated this number or not)

Step 2 Generate and store the 4 billion numbers:
I searched for some optimizations and found some ways and the first solution was storing the 4 billion users in 10 hours and I ended with optimizing it to ~ 1.26 hours
and this is with just SQLite database, and I found more better ways to do that but I think this solution will be good for now

Step 3 Get Random number from 1 to the number of the rows at the list:
After storing all the 4 billion numbers at a table called selected table, want to generate a random number not more than the count of the list at this table


Step 4 make the validation:
after getting the list of the invalid numbers from wiki page (thanks for explaining that you want it to deal with any number of data)

if number % 286331153 ==0
then it’s like 0xAAAAAAAA
all the numbers

    0 The hexadecimal of 0 is _ 0x00000000
    1 The hexadecimal of 286331153 is _ 0x11111111
    2 The hexadecimal of 572662306 is _ 0x22222222
    3 The hexadecimal of 858993459 is _ 0x33333333
    4 The hexadecimal of 1145324612 is _ 0x44444444
    5 The hexadecimal of 1431655765 is _ 0x55555555
    6 The hexadecimal of 1717986918 is _ 0x66666666
    7 The hexadecimal of 2004318071 is _ 0x77777777
    8 The hexadecimal of 2290649224 is _ 0x88888888
    9 The hexadecimal of 2576980377 is _ 0x99999999
    10 The hexadecimal of 2863311530 is _ 0xaaaaaaaa
    11 The hexadecimal of 3149642683 is _ 0xbbbbbbbb
    12 The hexadecimal of 3435973836 is _ 0xcccccccc
    13 The hexadecimal of 3722304989 is _ 0xdddddddd
    14 The hexadecimal of 4008636142 is _ 0xeeeeeeee
    15 The hexadecimal of 4294967295 is _ 0xffffffff
   


val2_increasing_number
if the (number - 19088743) % 286331153 ==0, then it's not valid

    0 The hexadecimal of 19088743 is _ 0x01234567
    1 The hexadecimal of 305419896 is _ 0x12345678
    2 The hexadecimal of 591751049 is _ 0x23456789
    3 The hexadecimal of 878082202 is _ 0x3456789a
    4 The hexadecimal of 1164413355 is _ 0x456789ab
    5 The hexadecimal of 1450744508 is _ 0x56789abc
    6 The hexadecimal of 1737075661 is _ 0x6789abcd
    7 The hexadecimal of 2023406814 is _ 0x789abcde
    8 The hexadecimal of 2309737967 is _ 0x89abcdef

not on invalid list
    searching in the nvalid_list to see if this object is invalid
    if the list is ordered, then we ca use something like binary search tree, because it will give us O(log n) performance
     If not, we can just check if the list has this value or not, and this is O(n) performance



Step 5 If the number is not valid, delete it and if it's valid print it and put it in the new table
here I did second table to have all the valid data so after printing all the data once, we have the option of:

1- just change the name of unselected table(the empty one) with the selected table and then repeat the whole steps in case we want to add a validation number into the validation list from WIKI 

2- no need to recheck the data again, we can just get a random number from the second table, because its all data are valid


------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
x = 4294967295
until_valid = 4294967294

the number of possible Hex
The maximum size of a database file is 4294967294 pages.
At the maximum page size of 65536 bytes, this translates into a maximum database size of approximately 1.4e+14 bytes
(281 terabytes, or 256 tebibytes, or 281474 gigabytes or 256,000 gibibytes).

The theoretical maximum number of rows in a table is 264 (18446744073709551616 or about 1.8e+19). 
------------------------------------------------------------------------------
 
save one million with print
21:26:59
21:27:44
1000000 : 1
4294967294 :

just save i = from 1 to 1 million without printing
21:31:08
21:31:17
1000000 : 9
4294967294 :

------------------------------------------------------------------------------
100 million
23:29:42
23:44:47
done

100000000 : 5
4294967294 :

23:57:19
00:12:24
done


fetch

99999999
00:34:44
00:35:34
done


------------------------------------------------------------------------------
batch_inserts for 100000000
03:33:45
03:35:31

100000000 : 106
4294967294 :

done after 1:46
106 s



06:57:32
06:59:20
done after 1:58
done
100000000 : 120
4294967294 : 1.4

------------------------------------------------------------------------------
select time
99999999
07:02:18
07:03:09
done

[(28647397,)]
07:19:15
07:19:23
done

[(53379292,)]
07:19:57
07:20:05
done

[(10941313,)]
07:29:27
07:29:35
done

the validation:
The hexadecimal of 0xAAAAAAAA is _ 2863311530
The hexadecimal of 0xBBBBBBBB is _ 3149642683
1.1
The hexadecimal of 0xbbbbbbbb is _ 3149642683
The hexadecimal of 0xcccccccc is _ 3435973836
-286,331,153
The hexadecimal of 0xdddddddd is _ 3722304989

from
2863311530 with adding 
286,331,153


The hexadecimal of 286331153 is _ 0x11111111
The hexadecimal of 572662306 is _ 0x22222222
The hexadecimal of 858993459 is _ 0x33333333
The hexadecimal of 1145324612 is _ 0x44444444
The hexadecimal of 1431655765 is _ 0x55555555
The hexadecimal of 1717986918 is _ 0x66666666
The hexadecimal of 2004318071 is _ 0x77777777
The hexadecimal of 2290649224 is _ 0x88888888
The hexadecimal of 2576980377 is _ 0x99999999
The hexadecimal of 2863311530 is _ 0xaaaaaaaa
The hexadecimal of 3149642683 is _ 0xbbbbbbbb
The hexadecimal of 3435973836 is _ 0xcccccccc
The hexadecimal of 3722304989 is _ 0xdddddddd
The hexadecimal of 4008636142 is _ 0xeeeeeeee
The hexadecimal of 4294967295 is _ 0xffffffff


the next is not with us
The hexadecimal of 4581298448 is _ 0x111111110




[ 1044942	
,	12235020	
,	464367618	
,	19229	
,	2343432205	
,	2880289470	
,	2969956365	
,	2976579765	
,	184594741	
,	3131746989	
,	3131961357	
,	3134333474	
,	3135097598	
,	3405689018	
,	2965027518	
,	3203381950	
, 	2952847021	
,	3221229823	
,	212601099710477	
,	3405691582	
,	3405697037	
,	3472551422	
,	219540062	
,	3669732608	
,	3735890861	
,	3735927469	
,	3735927486	
,	3735928495	
,	295990755083049101712519384016336453749	
,	3735928559	
,	3735929054	
,	3735936685	
,	3735932941	
,	3735943697	
,	3735883980	
,	3735944941	
,	3737844653	
,	3741239533	
,	3503344330	
,	3759263696	
,	61868	
,4207849484	
,	4207869677	
,	4222467823	
,	4276215469	
,	4276992702	
,	4276994270	
,	18369614221190020847	
,	4290436369	
,	4027431614]


