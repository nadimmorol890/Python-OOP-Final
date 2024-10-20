class Bank:
    users = {}
    transactions = {}
    loan_enabled = True
    total_loan_amount = 0
    is_bankrupt = False

    def __init__(self, name):
        self.name = name
