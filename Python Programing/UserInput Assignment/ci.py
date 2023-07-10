# CI Stnad for Compound Interest.
# Logical/Solution --- > A = P*(pow((1 + R/100),t))
# Compound Interest annual  = A - p
# variable names details
# A = A is  Compound Amount.
# P = P is the Pricipal amount
# R = R is the Rate.
# T = T is the time span.


P = float(input("Enter number of Principal amount : "))# 1200
R = float(input("Enter number  Rate : "))# 5.4
t = float(input("Enter the time : "))#2

A = P*(pow((1 + R/100),t))

ci = A - P

print ("Annual Compound Interest : ", ci)


