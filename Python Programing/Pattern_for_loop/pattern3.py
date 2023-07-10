'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
'''
for i in range(1, 16):
    for j in range(1,i+1):\
        print(j, end=" ")
    print()
'''
temp = 0
for i in range(1, 7):
    for j in range(1,i):
        temp = temp +1
        print(temp, end=" ")
    print()