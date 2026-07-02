"""
main.py
-------
The console menu. This is the only file that talks to the user
(input/print). All the actual rules live in bank.py, and all the
Excel file handling lives in database.py. Run this file to use
the program.
"""

from bank import Bank, BankError


def print_header():
    print("-" * 50)
    print(" BANK MANAGEMENT SYSTEM (Excel-backed)")
    print("-" * 50)


def about():
    print("\nBank Management System — now backed by an Excel database "
          "(bank_data.xlsx), so your accounts and transactions persist "
          "between runs instead of resetting every time.")


def create_account(bank: Bank):
    print("\nCreating a new account:")
    try:
        name = input("Enter your full name: ")
        age = int(input("Enter your age: "))
        phone_number = input("Enter your phone number: ")
        account_type = input("Enter account type (Savings/Current): ")
        initial_balance = float(input("Enter initial balance (minimum $1000): "))

        account = bank.create_account(name, age, phone_number, account_type, initial_balance)
        print(f"\nAccount created successfully!\nAccount Number: {account['Account Number']}")
    except ValueError:
        print("\nInvalid input — age and balance must be numbers.")
    except BankError as e:
        print(f"\nError: {e}")


def deposit(bank: Bank):
    print("\nDepositing money:")
    try:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to deposit: "))
        new_balance = bank.deposit(account_number, amount)
        print(f"\nDeposit successful! New balance: ${new_balance}")
    except ValueError:
        print("\nInvalid input — account number and amount must be numbers.")
    except BankError as e:
        print(f"\nError: {e}")


def withdraw(bank: Bank):
    print("\nWithdrawing money:")
    try:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        new_balance = bank.withdraw(account_number, amount)
        print(f"\nWithdrawal successful! New balance: ${new_balance}")
    except ValueError:
        print("\nInvalid input — account number and amount must be numbers.")
    except BankError as e:
        print(f"\nError: {e}")


def check_balance(bank: Bank):
    print("\nChecking balance:")
    try:
        account_number = int(input("Enter your account number: "))
        print(f"\nCurrent balance: ${bank.get_balance(account_number)}")
    except ValueError:
        print("\nInvalid input — account number must be a number.")
    except BankError as e:
        print(f"\nError: {e}")


def display_transactions(bank: Bank):
    print("\nDisplaying transactions:")
    try:
        account_number = int(input("Enter your account number: "))
        transactions = bank.get_transactions(account_number)
        if not transactions:
            print("\nNo transactions yet.")
            return
        print("\nTransaction history:")
        for t in transactions:
            print(f"{t['Date/Time']} | {t['Type']:<15} | "
                  f"{t['Amount']:>10} | Balance after: {t['Balance After']} | {t['Description']}")
    except ValueError:
        print("\nInvalid input — account number must be a number.")
    except BankError as e:
        print(f"\nError: {e}")


def transfer_funds(bank: Bank):
    print("\nTransferring funds:")
    try:
        sender = int(input("Enter your account number: "))
        recipient = int(input("Enter the recipient's account number: "))
        amount = float(input("Enter the amount to transfer: "))
        bank.transfer(sender, recipient, amount)
        print("\nFunds transferred successfully!")
    except ValueError:
        print("\nInvalid input — account numbers and amount must be numbers.")
    except BankError as e:
        print(f"\nError: {e}")


def view_account_details(bank: Bank):
    print("\nViewing account details:")
    try:
        account_number = int(input("Enter your account number: "))
        account = bank.get_account_details(account_number)
        print("\nAccount details:")
        for key, value in account.items():
            print(f"{key}: {value}")
    except ValueError:
        print("\nInvalid input — account number must be a number.")
    except BankError as e:
        print(f"\nError: {e}")


def close_account(bank: Bank):
    print("\nClosing account:")
    try:
        account_number = int(input("Enter your account number: "))
        bank.close_account(account_number)
        print("\nAccount closed successfully!")
    except ValueError:
        print("\nInvalid input — account number must be a number.")
    except BankError as e:
        print(f"\nError: {e}")


def view_all_accounts(bank: Bank):
    print("\nViewing all accounts:")
    accounts = bank.list_all_accounts()
    if not accounts:
        print("No accounts found.")
        return
    for account in accounts:
        for key, value in account.items():
            print(f"{key}: {value}")
        print("-" * 30)


def change_or_link_phone_numbers(bank: Bank):
    print("\nChanging or linking phone numbers:")
    try:
        account_number = int(input("Enter your account number: "))
        account = bank.get_account_details(account_number)
        print(f"\nCurrent linked phone numbers: {account['Phone Numbers']}")
        choice = input("Do you want to (C)hange or (L)ink a new phone number? ").upper()
        new_number = input("Enter the phone number: ")
        if choice == "C":
            bank.change_phone_number(account_number, new_number)
            print("\nPhone number changed successfully!")
        elif choice == "L":
            bank.link_phone_number(account_number, new_number)
            print("\nPhone number linked successfully!")
        else:
            print("\nInvalid choice. Please enter 'C' or 'L'.")
    except ValueError:
        print("\nInvalid input — account number must be a number.")
    except BankError as e:
        print(f"\nError: {e}")


MENU = """
Bank Operations Menu:
1.  About
2.  Create Account
3.  Deposit
4.  Withdraw
5.  Check Balance
6.  Display Transactions
7.  Transfer Funds
8.  View Account Details
9.  Close Account
10. View All Accounts
11. Change/Link Phone Numbers
12. Exit
"""


def main():
    print_header()
    bank = Bank("bank_data.xlsx")

    actions = {
        "1": about,
        "2": create_account,
        "3": deposit,
        "4": withdraw,
        "5": check_balance,
        "6": display_transactions,
        "7": transfer_funds,
        "8": view_account_details,
        "9": close_account,
        "10": view_all_accounts,
        "11": change_or_link_phone_numbers,
    }

    while True:
        print(MENU)
        choice = input("Enter your choice (1-12): ").strip()
        if choice == "12":
            print("Exiting program. Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please enter a number between 1 and 12.")
            continue
        if action is about:
            action()
        else:
            action(bank)


if __name__ == "__main__":
    main()