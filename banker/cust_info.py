from bank_acct_gen import BankAccountNumber
import random
import json


class Customer(BankAccountNumber):
    def __init__(self, name, address, city, state, zip_code, phone_number, email):
        self.id = self.generate_id()
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def generate_id(self):
        id = str(random.randint(100000000, 999999999))
        print(f"ID number: {id}")
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_city(self):
        return self.city
    
    def get_state(self):
        return self.state   
    
    def get_zip(self):
        return self.zip_code
    
    def get_phone(self):
        return self.phone_number
    
    def get_email(self):
        return self.email
    

# create a new customer object
#customer_id = Customer(Customer.generate_id(self=Customer))
customer = Customer(input("Enter your name: "), input("Enter your address: "), input("Enter your city: "), input("Enter your state: "), input("Enter your zip code: "), input("Enter your phone number: "), input("Enter your email: "))

customer.generate_id()
customer.get_name()
customer.get_address()
customer.get_city()
customer.get_state()
customer.get_zip()
customer.get_phone()
customer.get_email()


# create a dictionary of customer instances
'''customers = {}
customers[customer.id] = customer

# print the dictionary of customer instances
print(customers)
'''

