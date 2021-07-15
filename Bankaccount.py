


class BankAccount:

    def __init__(self):
        self.balance = 0

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

    # def yield_intrest(self):
       
    def display(self):
        print("\nAccount Balance is : ", self.balance)



tom = BankAccount

tom.deposit(tom)
tom.withdraw(tom)