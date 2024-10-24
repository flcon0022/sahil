# Banking program

def show_balance():
    print(f" Your balance is Rs{balance:2f}")
   
def deposite():
    amount= float(input(" Enter a amount to be deposited:"))

    if amount< 0 :
        print(" That's not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to be withdrawn:"))

    if amount> balance:
        print(" Insufficiant funds")
    elif amount < 0:
        print(" Amount must be Greater then 0")
    else :
        return amount

balance =0
is_running =True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposite")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter the number of your choice (1-4):")

    if choice== '1':
        show_balance()
    elif choice =='2':
        balance +=deposite()
    elif choice =='3':
        balance-=withdraw()
    elif choice =='4':
        is_running = False
    else:
        print(" That is not a valid choice")

print(" Thank you ! Have a nice Day")
    