"""domácí úkol:
vytvořte soubor 06_cisla.py

máte tato čísla

cisla = [-98, 23, 27, 91, -46, -26, -69, -53, -62, -93, 17, 50, -65, 18, -38, -4, 75, -79, -98, -56, -57, 89]

pomocí for cyklu určete, kolik je jich záporných a kolik kladných

vytvořte si 2 proměnné, např:
pocet_zapornych = 0
pocet_kladnych = 0

pak for cyklus,
pokud je cislo záporné, zvýším pocet_zapornych o 1
pokud je cislo kladné, zvýším pocet_kladnych o 1

pak mimo for cyklus vytiskněte kolik je kladných a záporných"""

cisla = [-98, 23, 27, 91, -46, -26, -69, -53, -62, -93, 17, 50, -65, 18, -38, -4, 75, -79, -98, -56, -57, 89]

pocet_zapornych = 0
pocet_kladnych = 0

for cislo in cisla:
    if cislo >= 0:
        pocet_kladnych += 1
    else: 
        pocet_zapornych += 1

print("Počet kladných čísel je:", pocet_kladnych, " a počet záporných čísel je:", pocet_zapornych )
print(f"celkem je čísel: {len(cisla)}")
 
