#1.WAP to test a number is divisible by 3 or 5 and both

num  = int(input("Enter the number"))
if (num % 3 == 0):
           print(" This number is divisible by 3")

elif ( num % 5 == 0 ):
    print("This number is divisible by 5")

else:
    print("This number is not divisible by 3 or 5")
