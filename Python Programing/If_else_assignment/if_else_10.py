'''
10. Write a program that has following menu:
Enter code w for withdraw.
Enter code d for deposit.
Enter code c for checking balance.

Note: 1 take initial amount as input from user.

Note:2 You can withdraw an amount only if balance is greater
than or equal to 500 and withdrawing amount should be less than
balance.
'''


bal = float(input("Enter the initial bal: "))

op = input("""Select an option
d. Deposit
w. Withdraw
c. Check bal

""")

match (op):
    case "d":
        amt = float(input("Enter the amt :"))
        bal = bal + amt
        print("Update Balnace: ",bal)


    case "w":
        amt = float(input("Enter amount:"))
        if(bal<amt):
            print("insufficient bal ")

        elif (bal-amt>500):
            bal = bal-amt
            print("Update balance :",bal)
        else:
            print("500 min bal is not maintained")
            

    case "c":
        print("Avilable balance : ",bal)

    case _:
        print("Invalide Syntax")

        
        
