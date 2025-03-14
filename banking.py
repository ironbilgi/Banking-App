import datetime
from decimal import Decimal
from uuid import uuid1

class Account:
    def __init__(self,balance=Decimal("0.00")):
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
