#4. WAP to find the greatest of three numbers entered through keyboard

num1,num2,num3 = input("Enter the first number").split()
if (num1 >= num2 and num1 >= num3):
    greatest = num1
elif(num2 >= num1 and num2 >= num3):
    greatest = num2
else :
    greatest = num3
print("The greates number of value is : ", greatest)
