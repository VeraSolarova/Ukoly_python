"""
2) vytvořte 16_animal.py a v něm:

- obecou trídu Animal, která bude mít v init name jako privátní proměnou

- třída Dog - pro metodu sound() - bude printovat jméno + "wof"
- třída Cat - pro metodu sound() - bude printovat jméno + "mňau"


příklad použití:
my_dog = Dog('Stark')
my_dog.sound() # printuje 'Stark: Wof'

my_cat = Cat('Dizzy')
my_cat.sound() # printuje 'Dizzy: mňau'

name v bude v obou případech dostupné přes ._name
= privátní attribut/proměnná

my_dog._name
my_cat._name

"""
class Animal:
    def __init__(self, name):
        self._name = name
     
    def sound(self):
        print(self._name)

class Dog(Animal):    
    def sound(self):
        print(f"{self._name} + wof") 

my_dog = Dog("Stark")
my_dog.sound()     

class Cat(Animal):    
    def sound(self):  
        print(f"{self._name} + mňau")  #

my_cat = Cat("Dizzy")
my_cat.sound()  


"""-----------------------------------------------------------------------------------------------"""
class Animal2:
    def __init__(self, name, my_sound):
        self._name = name
        self.my_sound = my_sound

    def sound(self):
        print(f"{self._name} + {self.my_sound}")

class Dog2(Animal2):
    def __init__(self, name):
        super().__init__(name, "wof") # zavolá konstruktor třídy Animal2 a předá zvuk "wof". Super -  volání metod/atributů z nadřazené (rodičovské) třídy - prohledává rodiče zleva do prava - MRO (Method Resolution Order) 

alik2 = Dog2("Alík 2")

alik2.sound() # printuje: Alík 2 + wof

    
