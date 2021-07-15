



class User:
    
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):

        self.account_balance += amount
    
    def make_withdraw(self, amount):

        self.account_balance -= amount
    
    # def make_transfer(self, amount, User):

    #     self.account_balance -= amount
    #     amount += 

Michael = User("Michael Luckiest", "Luckiestpet@hi.com")
Bob = User("Bobby Brown", "bob@hi.com")
Linda = User("Linda Luckiest", "Linda@hi.com")

Michael.make_deposit(300).make_deposit(500)
Linda.make_deposit(400).make_withdraw(100)
Bob.make_deposit(1000).make_withdraw(100).make_withdraw(200)

print(f"Michael your account Balance is :",Michael.account_balance)
print(f"Linda your account Balance is :",Linda.account_balance)
print(f"Bob your account Balance is :",Bob.account_balance)

# Bob.make_transfer(100, Linda)
# print(f"Linda your account Balance is :",Linda.account_balance)
# print(f"Bob your account Balance is :",Bob.account_balance)