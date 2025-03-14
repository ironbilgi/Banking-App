from datetime import datetime
from decimal import Decimal
from uuid import uuid1
class Account:
    # Constructor, intantiate the balance to 0.00
    def __init__(self,balance=Decimal("0.00")):
        self.balance = balance
    def deposit(self,amount): # Deposit amount, creates uuid and datetime
        self.balance += amount
        self.transactionLog = uuid1()
        self.transactionLogTime = datetime.now()
    def withdraw(self,amount): # Withdraw amount, creates uuid and datetime
        self.balance -= amount
        self.transactionLog = uuid1()
        self.transactionLogTime = datetime.now()
    def get_balance(self): # Get balance
        return self.balance
