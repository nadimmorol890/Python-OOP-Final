from admin import Admin
from user import User

def user_menu (user):
    while True:
        print ("--- User Menu ---")
        print ("1. Deposit")
        print ("2. Withdraw")
        print ("3. Check Balance")
        print ("4. Transaction History")
        print ("5. Take Loan")
        print ("6. Transfer")
        print ("7. Logout")

        choice = int (input ('Enter Your Choice: '))

        if choice == 1:
            amount = float (input ('Enter Amount to Deposit: '))
            user.deposit (amount)

        elif choice == 2:
            amount = float (input ('Enter Amount to Withdraw: '))
            user.withdraw (amount)

        elif choice == 3:
            user.check_balance ()

        elif choice == 4:
            user.transaction_history ()

        elif choice == 5:
            amount = float (input ('Enter Loan Amount: '))
            user.take_loan (amount)

        elif choice == 6:
            receiver = int (input ('Enter Receiver Account Number: '))
            amount = float (input ('Enter Transfer Amount: '))
            user.transfer (receiver, amount)

        elif choice == 7:
            break

        else:
            print ('Invalid Choice')

def admin_menu (admin):
    while True:
        print ("--- Admin Menu ---")
        print ("1. Create an Account")
        print ("2. Delete an Account")
        print ("3. View All Accounts")
        print ("4. Check Total Bank Balance")
        print ("5. Check Total Loan Amount")
        print ("6. Toggle Loan Feature")
        print ("7. Toggle BankRupt Feature")
        print ("8. Logout")

        choice = int (input ('Enter Your Choice: '))

        if choice == 1:
            name = input ("Enter your name: ")
            email = input ("Enter your email: ")
            address = input ("Enter your address: ")
            account_type = input ("Enter account type (Savings/Current): ")
            admin.create_account (name, email, address, account_type)

        elif choice == 2:
            account_number = int (input ('Enter Account Number: '))
            admin.delete_account (account_number)

        elif choice == 3:
            admin.see_all_account ()

        elif choice == 4:
            admin.view_total_bank_balance ()

        elif choice == 5:
            admin.total_loan ()

        elif choice == 6:
            admin.toggle_loan_feature ()

        elif choice == 7:
            admin.toggle_bankrupt_feature ()

        elif choice == 8:
            break
        else:
            print ('Invalid Choice')


while True:
    print ('Welcome !!')
    print ('1. User')
    print ('2. Admin')
    print ('3. Exit')

    choice = int (input ('Enter Your Choice: '))

    if choice == 1:
        name = input ("Enter your name: ")
        email = input ("Enter your email: ")
        address = input ("Enter your address: ")
        account_type = input ("Enter account type (Savings/Current): ")

        current_user = User (name, email, address, account_type)
        user_menu (current_user)

    elif choice == 2:
        admin = Admin ("Admin Name", "admin@example.com")
        admin_menu (admin)

    elif choice == 3:
        break

    else:
        print('Invalid Choice!')
