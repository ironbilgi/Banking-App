from mainFunc import Account
from decimal import Decimal

def mainInterface():
    # Creates an account object
    account = Account()
    print("Welcome to the bank! Choose one of these options to start")
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Exit")
        print("5. Go to Logs")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = Decimal(input("Enter the amount to deposit: "))
            account.deposit(amount)
            print("Amount deposited successfully!")
            return [account.transactionLog, account.transactionLogTime]
        elif choice == "2":
            amount = Decimal(input("Enter the amount to withdraw: "))
            if account.get_balance() < amount:
                print("Insufficient balance!")
            else:
                account.withdraw(amount)
                print("Amount withdrawn successfully!")
                return [account.transactionLog, account.transactionLogTime]
        elif choice == "3":
            print("Your account balance is: ", account.get_balance())
        elif choice == "4":
            print("Thank you for using our service!")
            break
        elif choice == "5":   
            print("Invalid choice! Please enter a valid choice.")   
            break
        else:
            print("Invalid choice! Please enter a valid choice.")