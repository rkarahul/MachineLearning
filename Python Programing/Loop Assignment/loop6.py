
'''
6. WAP to check prime number entered through keyboard.
'''
num = int(input("Enter the number"))

for i in range(2, num):
    if (num % 2 == 0):
        print("Not Prime number")
        break
    else:
        print("prime number")
