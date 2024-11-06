# Create a bank account and add,withdraw and show balance of account after transaction 
class BankAccount:
    def details(self):
        print("Bank Account Details")
        self.name = input("Enter name of the account holder: ")
        self.account_number = input("Enter account number: ")
        self.balance = 5000
        print("Your balance is 5000")
    def add(self):
        self.amount = int(input("Enter amount to be added:"))
        self.balance = self.balance + self.amount
        print("Your balance is",self.balance)
    def withdraw(self):
        self.withdraw = int(input("Enter amount to be withdrawn: "))
        self.balance = self.balance - self.withdraw
        print("Your balance is",self.balance)

A1 = BankAccount()
A1.details()
A1.add()
A1.withdraw()
