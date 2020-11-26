class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance 
 
    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int,float)):
            return  self.balance + other
        raise 
    
    def __sub__(self, other):
        if isinstance(other, BankAccount):
            return self.balance - other.balance
        if isinstance(other, (int,float)):
            return  self.balance - other
        
b = BankAccount('Bob', 500)
c = BankAccount('Mary', 1200)
print(b - 2)
print(c - b)

