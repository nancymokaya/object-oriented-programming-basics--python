class BankAccount:
    def __init__(self, account_number, holder, balance=0):
        self.account_number = account_number
        self.holder = holder        
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:   
            print("Insufficient funds.")
        elif amount > 0:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Invalid withdrawal amount.")

    def display(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


#  Example usage 
account = BankAccount("0001160021766", "Nancy Mokaya", 2000)

account.display()
account.deposit(1000)
account.withdraw(500)
account.display()