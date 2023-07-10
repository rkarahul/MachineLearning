
'''
10. Write a program to count the total number of digits in a number
For example, the number is 75869, so the output should be 5.
'''
num = int(input("Enter the number"))
count= 0
while num > 0:
    digit = num % 10
    count+=1
    eld = num //  10
    num = eld
print(count)


    
