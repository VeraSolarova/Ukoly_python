"""
vytvořte soubor 05_for_cyklus.py

v listu lze zapsat data i takto pod sebe:

kde budou data = [
    8848, # Mount Everest
    8611, # K2
    4808, # Mont Blanc
    5895, # Kilimanjaro
    3776, # Mount Fuji
    5642, # Elbrus
    1603, # Sněžka
    1492, # Praděd
    1323, # Lysá hora
]

logika bude následující:
for cyklem projděte všechny nadmořské výšky a pokud:
je hora nižší jak 3000 m - napište X je nizká výška
je hora 3000 m a více, ale zároveň méně jak 6000 m - napište X je střední výška
jinak napište X je vysoká výška
.. kde X je výška
"""
# za pomoci chat GPT

seznam_hor = [
    8848, "Mount Everest",
    8611, "K2",
    4808, "Mont Blanc",
    5895, "Kilimanjaro",
    3776, "Mount Fuji",
    5642, "Elbrus",
    1603, "Sněžka",
    1492, "Praděd",
    1323, "Lysá hora"
]

for i in range(0, len(seznam_hor), 2):
    """cyklus projde prvky i od nultého do posledního (funkce len řekne počet prvků), po kroku 2 prvků  - for i in range(start, stop, step): 
     a řekne která hora je nízká, střední, vysoká """
    nadmorska_vyska = seznam_hor[i]
    nazev_hory = seznam_hor[i + 1]

    if nadmorska_vyska < 3000:
        print(f"Hora {nazev_hory} je nízká, měří: {nadmorska_vyska}m")
    elif 3000 <= nadmorska_vyska < 6000:
        print(f"Hora {nazev_hory} je střední výšky, měří: {nadmorska_vyska}m")
    else:
        print(f"Hora {nazev_hory} je vysoké výšky, měří: {nadmorska_vyska}m")