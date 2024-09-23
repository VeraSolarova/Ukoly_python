"""
vytvořte třídu MobilePhone

vymyslete k této třídě smysluplné atributy a metody
- 3-5 atributy (jaké vlastnosti a parametry by mohl mít mobilní telefon?)
- 2 metody (jaké chování (metody) by telefon mohl mít?)

vytvořte 2 instance

"""
#řešení za pomoci chat GPT

class MobilePhone:
    all_mobiles = [] # list všech vytvořených instancí

    def __init__(self, brand, _type, screen_size, battery):
        self.brand = brand
        self._type = _type
        self.screen_size = screen_size
        self.battery = battery

        MobilePhone.all_mobiles.append(self)

    @classmethod 
    def order_max_battery(cls):
         # seradi vsechny mobily dle kapacity baterie
        return sorted(cls.all_mobiles, key=lambda mobile: mobile.battery, reverse = True) #reverse = True  - sestupné řazení
        #lambda mobile: mobile.battery = lambda - anonymní funkce, jako vstup dostane prvek z listu all_mobiles - zde nazvaný mobile (instanci) a vrátí její vlastnost - kapacitu baterie  

    def print_attributes(self):
        print(self.brand, self._type,"úhlopříčka dipleje je" ,self.screen_size,"palců, kapacita baterie je", self.battery, "mAh")
        
mobile_sgs23 = MobilePhone("Samsung", "Galaxy S23", 6.1, 3900)
mobile_ai13128gb = MobilePhone("Apple", "iPhone 13 128GB", 6.1, 3240)
mobile_mrp50u12512gb = MobilePhone("Motorola", "Razr 50 Ultra 12GB/512GB", 6.9, 4000)


for mobile in MobilePhone.all_mobiles:
     #vypíše všechny mobily s jejich vlastnostmi
    mobile.print_attributes()

ordered_mobiles = MobilePhone.order_max_battery()

for mobile in ordered_mobiles:
     #vypíše všechny mobily seřazené podle kapacity baterie s jejich dalšími vlastnostmi
    mobile.print_attributes()