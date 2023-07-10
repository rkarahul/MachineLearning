# break keywords

while(True):
    a = int(input("Enter first number"))
    b = int(input("Enter first number"))
    print(a*b)
    ch = input("do you want run it agin(y/n)?")
    if(ch == 'y'):
        continue
    if(ch == 'n'):
        break
print("Thank you")
