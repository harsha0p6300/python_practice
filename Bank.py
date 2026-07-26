#Create a BankAccount class with deposit(), withdraw(), and display_balance() methods.

class BankAccount: #A class is a blueprint or template used to create objects.
    def __init__(self,balance=0):#constructor It automatically runs whenever an object is created.
        self.balance=balance

    def deposit(self,amount):#A function inside a class is called a method.which is the money to deposit.
        self.balance+=amount
        print(f"Deposited:{amount}")

    def withdraw(self,amount):#Another method.#Withdraw money from the account.
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn:{amount}")
        else:
            print("Insufficient balance: ")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account=BankAccount() #This creates an actual object.

account.deposit(10000)
account.withdraw(3000)
account.display_balance()

#If you consider the user input #or

class BankAccount:#A class is a blueprint or template used to create objects.
    def __init__(self,balance=0):#constructor It automatically runs whenever an object is created.
        self.balance=balance

    def deposit(self,amount):#A function inside a class is called a method.which is the money to deposit.
        self.balance+=amount
        print(f"Deposited:{amount}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn:{amount}")
        else:
            print("Insufficient balance: ")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

account=BankAccount()

deposit_amount=int(input("Enter the deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount=int(input("Enter the withdrawal amount: "))
account.withdraw(withdraw_amount)

account.display_balance()#Display the final values