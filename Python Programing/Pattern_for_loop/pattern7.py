a = int(input("Enter the number"))
for i in range(1,a):
    for j in range(1,a-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for l in range(1,k+1):
        print(1,end=" ")
    print()

