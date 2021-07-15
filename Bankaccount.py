


class BankAccount:

    def __init__(self, User):
        self.balance = self.a\

    def deposit(self):
        amount = float(input(f"Please enter how much to deposit: "))
        self.balance += amount
        print("\n Amount deposited is: ",amount) 
    def withdraw(self):
       amount = float(input(f"Enter amount to be withdrawn: "))
       if self.balance <= amount:
            self.balance -= amount
            print("\nAmount left in account is: ", amount)
       else:
            print("\n Not enough money!")

    def yield_intrest(self):
        pass
    def display(self):
        print("\nAccount Balance is : ", self.balance)



class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

User = ("Tom", "Tom@gmail.com")
x = BankAccount

x.deposit("Tom")
x.withdraw("Tom")