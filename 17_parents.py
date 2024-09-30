"""
vytvořte třídu Person, která bude mít atributy:
- name: str
- mother (odkaz na matku) - volitené, defaultně None
- father (odkaz na otce) - volitené, defaultně None

metody:
- get_parents() - která vrátí tuple (mother, father)


Použití:

john = Person('John')
lena = Person('Lena')

peter = Person('Peter', mother=lena, father=john)

print(peter.get_parents()) // vrátí (john, lena) - jako instance v tuple

print(lena.get_parents()) //vrítí (None, None)
"""

class Person:
    def __init__(self, name: str, mother=None, father=None) -> None:
        self.name = name
        self.mother = mother
        self.father = father

    def get_parents(self):
        if self.mother: #if True - pokud existuje
            mother_name = self.mother.name
        else:
            mother_name = "None"
        
        if self.father: 
            father_name = self.father.name
        else:
            father_name = "None"

        return (mother_name, father_name) 
    

babicka1 = Person ("Veronika")

dedecek1 = Person ("Vladimír")

babicka2 = Person ("Marie")

dedecek2 = Person ("Martin")

matka = Person("Hana", babicka1, dedecek1)

otec = Person("Honza", babicka2, dedecek2)

dcera = Person("Rozálie", matka, otec)

print(babicka1.get_parents())
print(matka.get_parents())
print(dcera.get_parents())