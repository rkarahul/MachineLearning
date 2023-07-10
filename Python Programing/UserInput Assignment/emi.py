# EMI
# Logical/Solution --- >  p * r * (1+r)**n/((1+r)**n - 1)
# Monthly Interest Rate(r) ---> R/(12*100)

# Variable name  details :
# p = Principal or Loan Amount
# r = Interest Rate Per Month
# n = NUmber Of monthly installments



p = float(input("Enter the Principal Amount:" )) # 1000000
R = float(input("Enter the annul interest rate: "))# 7
n = float(input("Enter the number of month : "))# 120

r = R/(12*100)

emi = p * r * (1+r)**n / ((1+r)**n-1)

print("Monthly EMI : ",round(emi,2))


