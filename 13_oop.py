"""3. vytvořte soubor 13_oop.py
a v něm třídu Planeta, která bude obsahovat:
atributy:
- poradi 
- nazev

a metodu info
která řekne "Toto je [název planety] a je [pořadí] od Slunce"

vytvořte 2 instance
- Země
- a nějakou další planetu """


class Planeta:
    def __init__(self, name, order):
        self.nazev_planety = name
        self.poradi = order

    def info(self):
        print(f"Toto je {self.nazev_planety} a je {self.poradi}. od Slunce")

zeme = Planeta("Země", 3)
zeme.info()

merkur = Planeta("Merkur", 1)
merkur.info()


