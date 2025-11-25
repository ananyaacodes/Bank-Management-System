import random, datetime

 
#DATABASE TO STORE ACCOUNT INFORMATION
accounts = [] 

print('----------------------------------------')
print("          BANK MANAGEMENT SYSTEM")
print('----------------------------------------')

def about():
    print("You are welcome in BANK MANAGEMENT SYSTEM project.It includes 12 choices.")

# FUNCTION TO DISPLAY ALL METHODS AND FUNCTIONS USED IN THE PROGRAM
def display_functions():
    print("\nMethods and Functions Used in the Program:")
    print("1. about()")
    print("2. display_functions()")
    print("3. create_account()")
    print("4. deposit()")
    print("5. withdraw()")
    print("6. check_balance()")
    print("7. display_transactions()")
    print("8. transfer_funds()")
    print("9. view_account_details()")
    print("10. close_account()")
    print("11. view_all_accounts()")
    print("12. exit()")
    print("\nFunctions and Built-in Functions Used in the Program:")
    print("\nString Operations:")
    print("   - string.lower()")
    print("   - string.capitalize()")
    print("\nList Operations:")
    print("   - list.append()")
    print("\nTuple Operations:")
    print("   - tuple.count()")
    print("   - tuple.index()")
    print("\nDictionary Operations:")
    print("   - dict.keys()")
    print("   - dict.values()")
    print("   - dict.items()")
 

# FUNCTION TO CREATE A NEW ACCOUNT
def create_account(): 
    print("\nCreating a new account:")
    
    name = input("Enter your full name: ") 
    age = int(input("Enter your age: ")) 

    # VALIDATE AGE FOR INDEPENDENT ACCOUNT OR BREAK AND SHOW MENU AGAIN
    if age >= 18: 
        phone_number = input("Enter your phone number: ") 


        # VALIDATE PHONE NUMBER LENGHT
        while len(phone_number) < 10: 
            print("Error: Phone number must be of 10 digits.") 
            phone_number = input("Enter your phone number: ") 
    else: 
        print("\nError: Individuals under 18 cannot create an independent account. They can get their account number linked to another account.") 

        return
    account_type = input("Enter account type (Savings/Current): ").capitalize() 
    initial_balance = float(input("Enter initial balance (minimum $1000): ")) 


    # VALIDATE INITIAL BALANCE  
    while initial_balance < 1000: 
        print("Error: Initial balance must be $1000 or more.") 

        initial_balance = float(input("Enter initial balance (minimum $1000): ")) 
 

    # GENERATE A 16-DIGIT ACCOUNT NUMBER 
    account_number =  int(random.random()*pow(10,16)) 


    # ADD NEW ACCOUNT TO THE DATA BASE
    account = { 

        'Name': name, 

        'Age': age, 

        'Phone Numbers': [phone_number], 

        'Account Type': account_type, 

        'Balance': initial_balance, 

        'Account Number': account_number, 

        'Transactions': [] 

    } 

    accounts.append(account) 

    print(f"\nAccount created successfully!\nAccount Number: {account_number}") 


# FUNCTION TO DEPOSIT MONEY
def deposit(): 
    print("\nDepositing money:") 

    account_number =  int(input("Enter your account number: "))

    amount = float(input("Enter the amount to deposit: ")) 

    # FIND THE ACCOUNT IN THE DATABASE
    for account in accounts: 

        if account['Account Number'] == account_number:
            
            # GET THE CURRENT DATE AND TIME
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

            account['Balance'] += amount 

            account['Transactions'].append(f"{current_datetime} - Deposit: +${amount}") 

            print(f"\nDeposit successful! New balance: ${account['Balance']}") 

            return 
 
    print("\nAccount not found. Please check your account number.") 

# FUNCTION TO WITHDRAW MONEY 
def withdraw(): 

    print("\nWithdrawing money:") 

    account_number =  int(input("Enter your account number: "))
    
    amount = float(input("Enter the amount to withdraw: ")) 
 
    # FIND THE ACCOUNT IN THE DATABASE
    for account in accounts: 

        if account['Account Number'] == account_number: 

            # GET THE CURRENT DATE AND TIME 
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

            if account['Balance'] >= amount: 

                account['Balance'] -= amount 

                account['Transactions'].append(f"{current_datetime} - Withdrawal: -${amount}") 

                print(f"\nWithdrawal successful! New balance: ${account['Balance']}") 

            else: 

                print("\nInsufficient funds.") 

            return 

    print("\nAccount not found. Please check your account number.") 


# FUNCTION TO CHECK BALANCE 
def check_balance(): 

    print("\nChecking balance:") 
    account_number =  int(input("Enter your account number: "))
    
    # FIND THE ACCOUNT IN THER DATABASE
    for account in accounts: 

        if account['Account Number'] == account_number: 

            print(f"\nCurrent balance: ${account['Balance']}") 

            return 

    print("\nAccount not found. Please check your account number.") 

# FUNCTION TO DISPLAY TRANSACTIONS
def display_transactions():
    
    print("\nDisplaying transactions:") 

    account_number = int(input("Enter your account number: "))

    # FIND THE ACCOUNT IN THE DATABASE 
    for account in accounts: 

        if account['Account Number'] == account_number: 

            print("\nTransaction history:") 

            for transaction in account['Transactions']: 

                print(transaction) 

            return 

    print("\nAccount not found. Please check your account number.") 
         


# FUNCTION TO TRANSFER FUNDS
def transfer_funds(): 

    print("\nTransferring funds:") 

    sender_account_number =  int(input("Enter your account number: "))

    recipient_account_number =  int(input("Enter your account number: "))

    amount = float(input("Enter the amount to transfer: ")) 


    # Find the sender's account in the database 
    for sender_account in accounts: 

        if sender_account['Account Number'] == sender_account_number: 

            # Check if the sender has sufficient funds 
            if sender_account['Balance'] >= amount: 

                # Find the recipient's account in the database 
                for recipient_account in accounts: 

                    if recipient_account['Account Number'] == recipient_account_number: 

                        # Transfer funds 
                        sender_account['Balance'] -= amount 

                        sender_account['Transactions'].append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Transfer to {recipient_account_number}: -${amount}") 

                        recipient_account['Balance'] += amount 

                        recipient_account['Transactions'].append(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Transfer from {sender_account_number}: +${amount}") 

                        print("\nFunds transferred successfully!") 

                        return 

                print("\nRecipient's account not found. Please check the recipient's account number.") 

                return 

            print("\nInsufficient funds.") 

            return

    print("\nSender's account not found or PAN number does not match. Please check your account number and PAN number.") 

 

# Function to view account details 
def view_account_details(): 

    print("\nViewing account details:") 

    account_number =  int(input("Enter your account number: "))


    # Find the account in the database 
    for account in accounts: 

        if account['Account Number'] == account_number: 

            print("\nAccount details:") 

            for key, value in account.items(): 

                if key != 'Transactions' and key != 'PAN Number': 

                    print(f"{key}: {value}") 

            return
        
    print("\nAccount not found. Please check your account number.") 

# Function to close account 
def close_account(): 

    print("\nClosing account:") 

    account_number = int(input("Enter your account number: ")) 

 
    # Find and remove the account from the database 
    for account in accounts: 

        if account['Account Number'] == account_number: 

            accounts.remove(account) 

            print("\nAccount closed successfully!") 

            return 

    print("\nAccount not found. Please check your account number.") 

 

# Function to view all accounts 
def view_all_accounts(): 

    print("\nViewing all accounts:") 

    if not accounts: 

        print("No accounts found.") 

    else: 

        for account in accounts: 

            print("\nAccount details:") 

            for key, value in account.items(): 

                if key != 'Transactions': 

                    print(f"{key}: {value}") 

            print("-" * 30) 

 

# Function to change or link phone numbers 
def change_or_link_phone_numbers(): 

    print("\nChanging or linking phone numbers:") 

    account_number =  int(input("Enter your account number: "))


    # Find the account in the database 
    for account in accounts: 

        if account['Account Number'] == account_number: 

            print(f"\nCurrent linked phone numbers: {', '.join(account['Phone Numbers'])}") 

             
            # Ask user if they want to change or link a new phone number 
            choice = input("Do you want to (C)hange or (L)ink a new phone number? ").upper() 

            if choice == 'C': 

                new_phone_number = input("Enter the new phone number: ") 


                # Validate new phone number length 
                while len(new_phone_number) < 10: 

                    print("Error: Phone number must be at least 10 digits.") 

                    new_phone_number = input("Enter the new phone number: ") 

                account['Phone Numbers'] = [new_phone_number] 

                print("\nPhone number changed successfully!") 

                return 

            elif choice == 'L': 

                new_phone_number = input("Enter the new phone number to link: ") 

 

                # Validate new phone number length 
                while len(new_phone_number) < 10: 

                    print("Error: Phone number must be at least 10 digits.") 

                    new_phone_number = input("Enter the new phone number to link: ") 

 

                # Check recipient's age for linking a new phone number 
                if account['Age'] >= 18: 

                    account['Phone Numbers'].append(new_phone_number) 

                    print("\nPhone number linked successfully!") 

                    return 

                else: 

                    print("\nGuardian's approval required to link a new phone number.")
                    
                    return 

            else: 

                print("Invalid choice. Please enter 'C' for change or 'L' for link.") 

                return
            
    print("\nAccount not found. Please check your account number.") 


# Main menu 
while True: 

    print("\nBank Operations Menu:")
    print("1. About")
    print("2. Display functions")
    print("3. Create Account") 
    print("4. Deposit") 
    print("5. Withdraw") 
    print("6. Check Balance") 
    print("7. Display Transactions")  
    print("8. Transfer Funds") 
    print("9. View Account Details") 
    print("10. Close Account") 
    print("11. View All Accounts") 
    print("12. Change/Link Phone Numbers") 
    print("13. Exit")

    
    # GET USER CHOICE
    choice = input("Enter your choice (1-12): ")
    
    
    # PERFORM SELECTED OPERATION
    if choice == '1': 
       about()
       
    elif choice == '2':
        display_functions()
        
    elif choice == '3': 
        create_account() 
        
    elif choice == '4': 
        deposit() 

    elif choice == '5': 
        withdraw() 

    elif choice == '6': 
        check_balance() 

    elif choice == '7': 
        display_transactions() 

    elif choice == '8': 
        transfer_funds() 

    elif choice == '9': 
        view_account_details() 

    elif choice == '10': 
        close_account() 

    elif choice == '11': 
        view_all_accounts() 

    elif choice == '12': 
        change_or_link_phone_numbers() 

    elif choice == '13':
        
        print("Exiting program. Goodbye!") 
        break 
    else: 
        print("Invalid choice. Please enter a number between 1 and 12.") 
