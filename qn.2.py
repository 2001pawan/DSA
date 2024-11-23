# Question 2)  Write a bank account class. Your class should have methods to make deposits, make withdrawals, and check the balance on the account.
# If a user tries to withdraw an amount that is above the available balance, your code should print out a statement letting the user know that the available balance is lower than the requested amount and that the transaction will be canceled.


# Below is an outline of the class:

class BankAccount:
 
    def __init__(self): 
        self.balance=None


    def deposit(self, amount):
        self.balance=amount


    def withdraw(self, amount): 

        withdrawl=0
        if self.balance>=amount:
            withdrawl=amount
            self.balance=self.balance-withdrawl
            print("withdraw",withdrawl)
        
        else:
            print("balance not enough,transaction cancelled")
            
        

    def get_balance(self):
        print(self.balance)


b=BankAccount()
b.deposit(10)
b.get_balance()
b.withdraw(10)
b.get_balance()