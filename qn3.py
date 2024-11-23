# Create a banking system that has two parent classes i.e. Account and Customer, and a derived class Bank_Account that inherits from both  Account and Customer classes
# Classes:
# Account Class: Manages basic account details.
# Customer Class: Manages customer information.
# Bank_Account Class: Inherits from both Account and Customer, and adds functionality for deposit and withdrawal"

class Account:
        
    def __init__(self,balance):
        self.balance=balance
        # super().__init__(*args, **kwargs)

    def check(self):
        return self.balance
        
    
              

class Customer:
        
    def __init__(self,name,type,number,email):
        self.name=name
        self.type=type
        self.number=number
        self.email=email
        # super().__init__(*args, **kwargs)


class bank_account(Account,Customer):
      
    def __init__(self,name,type,number,email,balance):
        Account.__init__(self,balance)
        Customer.__init__(self,name,type,number,email)


    def deposit(self,amount):
        self.balance=amount


    def withdrawl(self,amount):
        w=0
        if self.balance>=amount:
            w=amount
            print("withdrawn",w)
        else:
            print("cancelled")


b=bank_account("a","saving",12,"aa@gmail",0)
b.deposit(10)
b.withdrawl(11)

##super init method args kwargs kinda confusing

