'''
8. Write a program that has following menu:
Enter 1 to find out whether the entered number is even or odd.
Enter 2 to find out whether the entered number is positive or
negative.
'''


op = input(""" Enter the Option
1. even_odd
2. postive_negative

""")

match(op):

    case "1":
        num = float(input("Enter the number"))
        if (num % 2 == 0):
                print("This is even number")
        else:
                print("This is odd number")

    case "2":
        num = float(input("Enter the number"))
        if (num>0):
            print("This number is postive")
        else:
            print("This number is negative")

    


