import random
from bank import Bank

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_number = random.randint(100000, 999999)
        self.loan_count = 0
        Bank.users[self.account_number] = self
        Bank.transactions[self.account_number] = []

    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            Bank.transactions[self.account_number].append (f'Deposited: {amount}')
            print (f'{amount} Deposited to your account Successfully')

    def withdraw (self, amount):
        if Bank.is_bankrupt:
            print ('Bank is Bankrupt')
            return
        
        if amount > self.balance:
            print ('Withdrawal amount exceeded')
        else:
            self.balance -= amount
            Bank.transactions[self.account_number].append (f'Withdrawn: {amount}')
            print (f'{amount} Withdrawn Successfully')

    def check_balance (self):
        print (f'Your available balance is {self.balance}')

    def transaction_history (self):
        print(f'Transaction History for Account: {self.account_number}')
        for transaction in Bank.transactions[self.account_number]:
            print (transaction)

    def take_loan (self, amount):
        if Bank.is_bankrupt:
            print ('Bank is Bankrupt')
            return
        
        if Bank.loan_enabled:
            if self.loan_count < 2:
                self.balance += amount
                self.loan_count += 1
                Bank.total_loan_amount += amount
                Bank.transactions[self.account_number].append (f'Loan Taken: {amount}')
                print (f'Loan of {amount} Successful!')
            else:
                print ('You have already taken the maximum number of loans')
        else:
            print ('Sorry. Loan feature is currently disabled')

    def transfer (self, receiver_account, amount):
        if Bank.is_bankrupt:
            print ('Bank is Bankrupt')
            return
        
        if amount <= self.balance:
            if receiver_account in Bank.users:
                receiver = Bank.users[receiver_account]
                self.balance -= amount
                receiver.balance += amount
                Bank.transactions[self.account_number].append (f'Transferred: {amount} to {receiver_account}')
                Bank.transactions[receiver_account].append (f'Received: {amount} from {self.account_number}')
                print (f'Transferred {amount} to {receiver.name} Successfully')
            else:
                print ('Account does not exist')
        else:
            print ('Insufficient Balance')
