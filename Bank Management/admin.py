from bank import Bank

class Admin:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_account (self, name, email, address, account_type):
        from user import User
        User (name, email, address, account_type)
        print (f'Account Created Successfully for {name}')

    def delete_account (self, account_number):
        if account_number in Bank.users:
            del Bank.users[account_number]
            del Bank.transactions[account_number]
            print (f'Account {account_number} deleted Successfully')
        else:
            print ('Account not found')

    def see_all_account (self):
        for account in Bank.users:
            print (f'Account Number: {account}, Name: {Bank.users[account].name}')

    def view_total_bank_balance (self):
        total_balance = sum(user.balance for user in Bank.users.values())
        print (f'Total Available Bank Balance: {total_balance}')

    def total_loan (self):
        print (f'Total loan amount: {Bank.total_loan_amount}')

    def toggle_loan_feature (self):
        Bank.loan_enabled = not Bank.loan_enabled
        status = 'Enabled' if Bank.loan_enabled else 'Disabled'
        print(f'Loan feature is now {status}!')

    def toggle_bankrupt_feature (self):
        # if Bank.is_bankrupt == True:
        #     Bank.is_bankrupt = False
        # else:
        #     Bank.is_bankrupt = True

        # return Bank.is_bankrupt
        Bank.is_bankrupt = not Bank.is_bankrupt
        status = 'Enabled' if Bank.is_bankrupt else 'Disabled'
        print(f'Bank is BankRupt {status}!')

