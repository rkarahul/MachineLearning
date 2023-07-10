# BMI
# Logical/Solution --- > the_weight / (the_height/100)**2

weight = float(input("Enter the weight in kg : "))
height = float(input(" Enter the height in cm : "))
bmi = weight / (height/100)**2
print("Your Body Mass Index is ", round(bmi))
