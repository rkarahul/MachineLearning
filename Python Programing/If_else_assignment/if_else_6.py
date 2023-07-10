'''
6. Admission to professional course in a college according to
following conditions:
Marks in Mathematics are greater than or equal to 60 and marks in
physics is greater than or equal to 50 and marks in chemistry is
greater than or equal to 40

OR

Total marks in mathematics, physics and chemistry is greater than or
equal to 200.

OR

Total marks in mathematics and physics are greater than or equal to
150.
Marks of all three subjects will be entered through the keyboard.
WAP to tell whether a student is qualifying for admission or not.
'''


math = float(input("Enter the math marks: "))
physics = float(input("Enter the physics marks: "))
chemistry= float(input("Enter the chemistry marks: "))

if (math>=60 and physics>=50 and chemistry >=40):
         print("student is qualifying for admission")
    
else:
      print("student is qualifying for admission or not")
