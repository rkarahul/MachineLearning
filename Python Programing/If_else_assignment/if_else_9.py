'''
9. WAP that implements the simple calculator that has following menu:
Enter 1 to find the addition of two numbers.
Enter 2 to find the subtraction of two numbers.
Enter 3 to find the multiplication of two numbers.
Enter 4 to find the division of two numbers.
Enter 5 to find the inverse of a number.
Enter 6 to find the square of a number.
Enter 7 to find the cube of a number.
'''

op = input("""

1. add
2. sub
3. mul
4. div
5. inverse
6. square
7. cube

""")

match (op):

    case "1":

        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))

        add = num1 + num2

        print("Addition : ", add)

    case "2":
        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))

        sub = num1 - num2

        print("Subtraction : ", sub)

    case "3":

        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))

        mul = num1 * num2

        print("Multiplication : ", mul)

    case "4":
        num1 = float(input("Enter the first number"))
        num2 = float(input("Enter the second number"))

        div = num1 / num2

        print("Division: ", div)

    case "5":
        num = float(input("Enter the first number"))
        
        inverse = num**-1
        print("Inverse: ", inverse)
        
    case "6":
        num = float(input("Enter the number"))
        
        square = num**2
        print("Square: ", square)

    case "7":
        num = float(input("Enter the number"))
        cube = num**3
        print("Cube : ", cube)

    case _:
        print("Invalide Option")






        

    
