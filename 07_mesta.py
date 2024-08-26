""""
soubor se bude jmenovat 07_mesta.py

máme tato data se sloupci
1. nazev
2. pocet_obyvatel
3. rozloha

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]

pomocí for cyklu zjistěte:
1) jaký je celkový počet obyvatel v těchto městech
2) které město má nejvíce a nejměně obyvatel
"""

eu_cities = [
    ['Berlín', 3669491, 891],
    ['Madrid', 3223334, 604],
    ['Řím', 2872800, 1285],
    ['Paříž', 2165423, 105],
    ['Bukurešť', 1883425, 228],
    ['Budapešť', 1746344, 525],
    ['Varšava', 1790658, 517],
    ['Vídeň', 1921153, 414],
    ['Hamburk', 1841179, 755],
    ['Barcelona', 1620343, 101]
]


mesto_max_obyvatel = 0
nazev_mesto_max_obyvatel = ""
mesto_min_obyvatel = 1000000000000000
nazev_mesto_min_obyvatel = ""

pocet_obyvatel_celkem = 0

for mesto, pocet_obyvatel, rozloha in eu_cities:
    pocet_obyvatel_celkem  = pocet_obyvatel + pocet_obyvatel_celkem

print("Počet obyvatel ve všech městech dohromady je: ", pocet_obyvatel_celkem)   



for item in eu_cities:
    if item [1] > mesto_max_obyvatel:
        mesto_max_obyvatel = item[1]
        nazev_mesto_max_obyvatel = item[0]
    elif item [1] < mesto_min_obyvatel:
        mesto_min_obyvatel = item [1]
        nazev_mesto_min_obyvatel = item[0]

print("Nejvíce obyvatel má: ",nazev_mesto_max_obyvatel , mesto_max_obyvatel, "nejméně obyvatel má: ", nazev_mesto_min_obyvatel, mesto_min_obyvatel )         



     