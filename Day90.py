# Day 90 of 100 days of coding challenge
# Working with Hierarchical inheritance
class BankAcc:
    def __init__(self,name,bankacc,balance):
        self.name = name
        self.acc = bankacc
        self.balance = balance
    def display(self):
        print("Name of the Account Holder:",self.name)
        print("Account Number:",self.acc)
        print("Balance:",self.balance)

class Savings(BankAcc):
    def __init__(self,name,bankacc,balanace,money):
        super().__init__(name,bankacc,balanace)
        self.money = money

    def deposit(self):
        super().display()
        self.balance += self.money
        print("Final balanace after deposit is:",self.balance)
    def withdraw(self):
        super().display()
        self.balance -= self.money
        print("Final balance after withdrawal is:",self.balance)

class FD(BankAcc):
    def __init__(self,name,bankacc,balance,t,r):
        super().__init__(name,bankacc,balance)
        self.t = t
        self.r = r
    def displayInfo(self):
        super().display()
        interest = self.balance * self.r * self.t / 100
        print("Interest gained is:",interest)

bk = Savings("Ab","19073773822",200000,12000)
bk.withdraw()
print("__"*20)
fk = FD("Ab","19073773822",200000,10,5)
fk.displayInfo()

