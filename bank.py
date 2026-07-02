"""
bank.py
-------
The business-logic layer. Every rule about how a bank account is
allowed to behave lives here (minimum balance, age limits, phone
number rules, transfer rules, etc). Nothing in this file calls
input() or print() — that keeps it reusable and unit-testable,
and is the same separation professional codebases use.
"""

import random
from datetime import datetime
from database import ExcelDatabase


class BankError(Exception):
    """Base class for all bank-related errors."""


class AccountNotFoundError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class ValidationError(BankError):
    pass


MIN_OPENING_BALANCE = 1000
MIN_PHONE_LENGTH = 10


class Bank:
    def __init__(self, db_path: str = "bank_data.xlsx"):
        self.db = ExcelDatabase(db_path)

    # ---------- helpers ----------

    def _generate_account_number(self) -> int:
        while True:
            candidate = random.randint(10**15, 10**16 - 1)  # 16 digits
            if not self.db.account_number_exists(candidate):
                return candidate

    def _require_account(self, account_number: int) -> dict:
        account = self.db.get_account(account_number)
        if account is None:
            raise AccountNotFoundError(f"No account found with number {account_number}.")
        return account

    # ---------- account lifecycle ----------

    def create_account(self, name: str, age: int, phone_number: str,
                        account_type: str, initial_balance: float) -> dict:
        if age < 18:
            raise ValidationError(
                "Individuals under 18 cannot open an independent account. "
                "Their number can be linked to a guardian's account instead."
            )
        if len(phone_number) < MIN_PHONE_LENGTH:
            raise ValidationError(f"Phone number must be at least {MIN_PHONE_LENGTH} digits.")
        if account_type.capitalize() not in ("Savings", "Current"):
            raise ValidationError("Account type must be 'Savings' or 'Current'.")
        if initial_balance < MIN_OPENING_BALANCE:
            raise ValidationError(f"Initial balance must be at least ${MIN_OPENING_BALANCE}.")

        account_number = self._generate_account_number()
        account = {
            "Account Number": account_number,
            "Name": name.strip(),
            "Age": age,
            "Phone Numbers": phone_number,
            "Account Type": account_type.capitalize(),
            "Balance": round(initial_balance, 2),
            "Status": "Active",
            "Created On": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.db.insert_account(account)
        self.db.add_transaction(account_number, "Account Opened", initial_balance,
                                 initial_balance, "Initial deposit")
        return account

    def close_account(self, account_number: int):
        account = self._require_account(account_number)
        if account["Balance"] > 0:
            raise ValidationError(
                f"Account has a remaining balance of ${account['Balance']}. "
                "Withdraw all funds before closing."
            )
        self.db.delete_account(account_number)

    # ---------- money movement ----------

    def deposit(self, account_number: int, amount: float) -> float:
        if amount <= 0:
            raise ValidationError("Deposit amount must be positive.")
        account = self._require_account(account_number)
        new_balance = round(account["Balance"] + amount, 2)
        self.db.update_account(account_number, Balance=new_balance)
        self.db.add_transaction(account_number, "Deposit", amount, new_balance)
        return new_balance

    def withdraw(self, account_number: int, amount: float) -> float:
        if amount <= 0:
            raise ValidationError("Withdrawal amount must be positive.")
        account = self._require_account(account_number)
        if account["Balance"] < amount:
            raise InsufficientFundsError(
                f"Insufficient funds. Current balance: ${account['Balance']}"
            )
        new_balance = round(account["Balance"] - amount, 2)
        self.db.update_account(account_number, Balance=new_balance)
        self.db.add_transaction(account_number, "Withdrawal", -amount, new_balance)
        return new_balance

    def transfer(self, sender_number: int, recipient_number: int, amount: float):
        if amount <= 0:
            raise ValidationError("Transfer amount must be positive.")
        if sender_number == recipient_number:
            raise ValidationError("Cannot transfer to the same account.")

        sender = self._require_account(sender_number)
        recipient = self._require_account(recipient_number)

        if sender["Balance"] < amount:
            raise InsufficientFundsError(
                f"Insufficient funds. Current balance: ${sender['Balance']}"
            )

        sender_new_balance = round(sender["Balance"] - amount, 2)
        recipient_new_balance = round(recipient["Balance"] + amount, 2)

        self.db.update_account(sender_number, Balance=sender_new_balance)
        self.db.update_account(recipient_number, Balance=recipient_new_balance)

        self.db.add_transaction(sender_number, "Transfer Out", -amount,
                                 sender_new_balance, f"To {recipient_number}")
        self.db.add_transaction(recipient_number, "Transfer In", amount,
                                 recipient_new_balance, f"From {sender_number}")

    # ---------- queries ----------

    def get_balance(self, account_number: int) -> float:
        return self._require_account(account_number)["Balance"]

    def get_account_details(self, account_number: int) -> dict:
        return self._require_account(account_number)

    def get_transactions(self, account_number: int) -> list[dict]:
        self._require_account(account_number)  # raises if missing
        return self.db.get_transactions(account_number)

    def list_all_accounts(self) -> list[dict]:
        return self.db.get_all_accounts()

    # ---------- phone numbers ----------

    def change_phone_number(self, account_number: int, new_number: str):
        if len(new_number) < MIN_PHONE_LENGTH:
            raise ValidationError(f"Phone number must be at least {MIN_PHONE_LENGTH} digits.")
        self._require_account(account_number)
        self.db.update_account(account_number, **{"Phone Numbers": new_number})

    def link_phone_number(self, account_number: int, new_number: str):
        if len(new_number) < MIN_PHONE_LENGTH:
            raise ValidationError(f"Phone number must be at least {MIN_PHONE_LENGTH} digits.")
        account = self._require_account(account_number)
        if account["Age"] < 18:
            raise ValidationError("Guardian's approval required to link a new phone number.")
        existing = account["Phone Numbers"]
        updated = f"{existing};{new_number}"
        self.db.update_account(account_number, **{"Phone Numbers": updated})