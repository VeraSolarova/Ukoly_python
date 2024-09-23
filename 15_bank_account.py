"""
bude obsahovat třídu BankAccount (Bankovní účet)
atributy:
- owner (str) - jméno vlastníka účtu
- balance (int) - stav konta

oba atributy lze zadat v __init__, balance bude mít defaultně hodnotu 0 pokud není zadáno jinak

Metody:
- deposit (vklad)
- withdraw (výběr)
- print (vytiskne stav konta) - jméno a aktuální stav

Příklad použití:

muj_ucet = BankAccount('Jan Novák', 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print()
"""

class BankAccount:
    def __init__(self, owner, balance=0,):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:   
            self.balance += amount
        else:
            print("vkládaná částka musí být větší nez nula.")
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Nelze vybrat požadovanou částku, aktuální stav účtu je:", self.balance)
    
    def print(self):
        print(self.owner, self.balance)

muj_ucet = BankAccount("Jan Noavak", 1000)
muj_ucet.deposit(10000)
muj_ucet.withdraw(500)
muj_ucet.print()
