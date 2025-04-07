from mainFunc.userInput import mainInterface
from mainFunc.accountFunc import Account

def addTransaction():
    recentTransactions = mainInterface()
    # Creates an account object
    account = Account() 
    # Creates a transaction object  
    transaction = account.transactionLog
    # Creates a transaction time object
    transactionTime = account.transactionLogTime
    # Creates a transaction amount object