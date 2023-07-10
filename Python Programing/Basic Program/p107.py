'''

Pattern printing
---------------------
1.

2 4 6
3 6 9
4 8 12

'''

for i in range(2,5):
    for j in range(1,4):
        print(i*j,end=' ')
    print("\n")

'''
2.



1
12
123
1234
12345

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')

    print()
    



for i in range(6,0,-1):
    for j in range(1,i):
        print(j,end=' ')

    print()
'''
3.

1
23
456
78910

'''
for i in range(1,11):
    for j in range(i):
       print(j,end=" ")
       
    print("\n")

        
'''
4.


54321
5432
543
54
5

for i in range(0,6):
    for j in range(5,i,-1):
       print(j,end=" ")
       
    print("\n")


5.





            1
           12
          123
         1234
        12345






'''




for i in range(2,7):
    for j in range(6,i,-1):
       print(" ", end=" ")
       
    for k in range(1,i):
       print(k,end=" ")
    print()
'''
 6.




 *
 * *
 * * *
 * * * *
 * * * * *

'''
'''
 7.


 A
 A B
 A B C
 A B C D
 A B C D E


     for j in range(66,78):
         for j in range():
         print(char(j),end=" ")

    print()
       




 key points to remeber:
 --------------------------------
 > for simplicity go with for loop
> use nested for loop
> outer loop controls num of rows

> nested loop controls num of cols in each row
> always try to print patern horizontally
> use a separated nested loop for starting spaces


'''



'''

for i in range(1,6):
    for j in range(i):
       print(i,end=" ")
       
    print("\n")
'''

























