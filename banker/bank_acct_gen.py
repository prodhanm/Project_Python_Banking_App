import random

class BankAccountNumber:
    def __init__(self, account_number):
        self.account_number = account_number

    @staticmethod
    def generate_account_number():
        account_number = str(random.randint(100000000, 999999999))
        return account_number
    
    def get_account_number(self):
        print(f"The account number is {self.account_number}")
    
bank_account_number = BankAccountNumber(BankAccountNumber.generate_account_number())
bank_account_number.get_account_number()

