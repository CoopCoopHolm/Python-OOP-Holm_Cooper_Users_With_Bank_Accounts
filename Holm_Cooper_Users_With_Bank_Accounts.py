class BankAccount:
    def __init__(self, int_rate = .001, balance = 0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def yield_interest(self):
        return self
    def display_BankAccount_balance(self):
        return self.balance

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount()
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.display_BankAccount_balance()}")
        return self
    def transfer_money(self, other_user, amount):
        other_user.deposit(amount)
        self.account.withdraw(amount)
        return self

coopcoopholm = User("Cooper Holm", "coop.coop@coop.com")
jodoe = User("Joe Doe", "joe@joe.com")
goobypls = User("Gooby Please", "gooby@please.com")

coopcoopholm.make_deposit(10)
coopcoopholm.make_deposit(10)
coopcoopholm.make_deposit(10)
coopcoopholm.make_withdrawal(5)
coopcoopholm.display_user_balance()