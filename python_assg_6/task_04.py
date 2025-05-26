
# 4. Class Variables and Class Methods
# Assignment: Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows 
# changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account holder is {self.account_holder} and her Bank name is {self.bank_name}")


account1 = Bank("Anosha")
account2 = Bank("Fatima")

account1.display()
account2.display()

Bank.change_bank_name("UBL Bank")

account1.display()
account2.display()