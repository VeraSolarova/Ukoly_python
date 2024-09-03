"""1. práce s dict
vytvořte soubor 10_dict.py
kde bude:
ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}

a) přidejte novou položku 'mléko' s částkou 25
b) zjistete, který produkt je nejlevnější
c) kolik mě bude stát, když si koupím 4x jablka, 1x máslo, a 2x sýr
udělejte printy pro kontrolu
"""

ceny_potravin = {
    'máslo': 30,
    'chleba': 20,
    'sýr': 30,
    'jablko': 5
}

ceny_potravin["mleko"] = 25

nejnizsi_cena = 1000
nejlevnejsi_potravina = ""

for potravina, cena in ceny_potravin.items():
    print(potravina, cena)
    if cena < nejnizsi_cena:
        nejnizsi_cena = cena
        nejlevnejsi_potravina = potravina

print("Nejlevnější potravina je", nejlevnejsi_potravina, "a stojí", nejnizsi_cena)

cena_nakupu = 4*(ceny_potravin['jablko']) + (ceny_potravin['máslo']) + 2*(ceny_potravin['sýr'])
print("Nákup 4x jablka, 1x máslo, a 2x sýr stojí", cena_nakupu) 
