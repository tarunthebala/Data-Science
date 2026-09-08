"""
Author: Tarun Balasubramaniam
Assignment Title: BankAccount class
Assignment Description: Create a BankAccount class and methods
Due Date: 09/02/2026
Date Created: 09/01/2026
Date Last Modified: 09/01/2026
"""
class BankAccount:
    def __init__(self, new_name, checking_balance, savings_balance):
        self.new_name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance

    def deposit_checking(self, amount):
        if amount > 0:
            self.checking_balance += amount

    def deposit_savings(self, amount):
        if amount > 0:
            self.savings_balance += amount

    def withdraw_checking(self, amount):
        if amount > 0:
            self.checking_balance -= amount

    def withdraw_savings(self, amount):
        if amount > 0:
            self.savings_balance -= amount

    def transfer_to_savings(self, amount):
        if amount > 0:
            self.withdraw_checking(amount)
            self.deposit_savings(amount)

if __name__ == '__main__':  
    #data abstraction
    #process
    account = BankAccount("Mickey", 500.00, 1000.00)
    account.checking_balance = 500
    account.savings_balance = 500
    account.withdraw_savings(100)
    account.withdraw_checking(100)
    account.transfer_to_savings(300)

    #output
    print(f"{account.new_name}\n${account.checking_balance:.2f}\n${account.savings_balance:.2f}")
