'''
7. Write a program that has following menu:
Enter 1 to find the area of rectangle.
Enter 2 to find the area of circle.
Values for length and width of a rectangle and value of a radius of
circle will be entered through keyboard.
'''

length = float(input("Enter the len number: "))

width = float(input("Enter the wid number"))

radius = float(input("Enter the radius number"))

choice = input('''Enter the option
1. area of rectangle
2. area of circle
''')

match(choice):

    case "1":

        print(length*width)

    case "2":

        print(3.14*radius*radius)

    case _:
        print("invalide")
        

