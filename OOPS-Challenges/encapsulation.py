## Hiding Banking Details ##
from pycparser.c_ast import Return


class Bank:
    def __init__(self,Name, Account_number, Balance):
        self.Name = Name
        self.Account_number=Account_number
        self.Balance = Balance

    def Deposit(self,amount):
        self.Balance = self.Balance+amount


    def Withdrawl(self,amount):
        self.Balance = self.Balance-amount


    def Total_Balance(self):
        return self.Balance

user = Bank("Priya",987525, 122233)
user.Deposit(3500)
print(user.Total_Balance())




