"""1) vytvořte soubor 03_funkce.py

v souboru vytvořte funkci:

def test_heslo(heslo: str):

tato funkce otestuje, zda uživatel zadal heslo alespoň o délce 5 znaků

test_heslo('1234') # vrátí False
test_heslo('12345') # vrátí True
test_heslo('TajnéHeslo') # vrátí True"""

heslo = input("Zadejte heslo delší než 4 znaky: ")

def test_heslo(heslo: str):
      if len(heslo) >= 5:
        return True
      else:
        return False

vysledek = test_heslo(heslo)
print (vysledek)
    