'''
5. The marks obtain by a student in 5 different subjects are input
through keyboard. The student gets the division as per the
following rules:
Percentage above or equal to 60- first division
Percentage between 50 and 59- second division
Percentage between 40 and 49 – third division
Percentage below 40- fails.
'''

python = int(input("Enter the marks : "))
java = int(input("Enter the marks : "))
dotnot = int(input("Enter the marks : "))
c = int(input("Enter the marks : "))
nodejs = int(input("Enter the marks : "))

sum = python +  java + dotnot + c + nodejs 
per = sum *100/500
print(per)

if(per>=60):
    print("First division")

elif (per > 50 and per < 60):
    print("second division")

elif (per >40 and per < 50):
    print("Third division")

else:
    print("fails")
