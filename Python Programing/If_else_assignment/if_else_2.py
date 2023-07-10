#2. If cost price and selling price of an item is input through keyboard.Write a program to determine how much profit he made or how much loss he got.

cost_price = float(input("Enter the Cost Price : "))
selling_price = float(input("Enter the Selling Price :"))
d = selling_price - cost_price
if (d < 0):
    print(" Profit amt : ",d)
else:
    print("Loss amt : ", d)

