"""
Vytvořte soubor 04_funkce.py

ve kterém budou 2 funkce:

1) funkce pro výpočet obsahu kruhu
2) funkce pro vpočet obvodu kruhu

vstupní parametr bude poloměr

Viz zde:
https://www.umimeto.org/asset/system/um/img/rules/ilustrace-obsah-obvod-prehled.png


řecké písmeno PI definujte jako 3.14 nebo importujte modul math, kde se nachází konstanta pi

import math

print(math.pi)

obě funkce otestujte
"""
# - výsledek práce s chat GPT. Mým vrcholným výkonem bylo pochopit, co se děje.  

import math # umožní mi použít hodnotu pí 
import re # Modul re poskytuje nástroje pro práci s regulárními výrazy (regex).

print("Hodnota pí:, ", math.pi)

def zpracuj_vstup(polomer):
    """Funkce zajistí, aby ze vstupní hodnoty poloměru zadané uživatelem byla hodnota float, desetinnou čárku převede na tečku, 
pokud byla zadána jednotka za číslem (cokoliv jiného kromě číslic a teček) s mezerou nebo bez mezery, dokáže ji oddělit a oříznout mezery"""  
    polomer = polomer.replace(',', '.') # Vymění desetinnou čárku za tečku

    match = re.match(r"([0-9.]+)([^\d]*)", polomer)
        # předpokládáme nejdříve číselnou hodnotu s desetinnou tečkou ([0-9.]+) a jednotku jako následující ([^\d]*) hledá jakýkoli znak, který není číslice \d , a to libovolně krát * ..i nula krát      
        # Funkce re.match(pattern, string) se pokouší najít shodu pro regulární výraz na stringu polomer. Pokud najde shodu, vrátí objekt match. Pokud ne, vrátí None.
     
    if match: # pokud hodnota funkce match je True 
            hodnota, jednotka = match.groups() # rozdělí objekt na proměnné hodonta a jednotka 
            float_polomer = float(hodnota)
    else:
        # Pokud regulární výraz nenajde shodu, vypíše chybu
        print("Zadaný formát je neplatný. Ujisti se, že zadáváš číslo s jednotkou nebo pouze číslo.")
        return None, None
    
    return float_polomer, jednotka.strip()  # Odeber mezery kolem jednotky


def obvod_kruhu(float_polomer):
    obvod = 2 * math.pi * float_polomer
    return round(obvod, 2)


def obsah_kruhu(float_polomer): 
    obsah =  math.pi * float_polomer * float_polomer 
    return round(obsah, 2)

polomer = input("Zadej poloměr kruhu: ")
float_polomer, jednotka = zpracuj_vstup(polomer)  # Zavolá funkci zpracuj_vstup s proměnnou polomer, kterou zadal uživatel. Výstup funkce se uloží do proměnných float_polomer a jednotka

if float_polomer is not None:
    print("Poloměr kruhu je:", float_polomer, jednotka)
    print("Obvod kruhu je:", obvod_kruhu(float_polomer), jednotka)
    print("Obsah kruhu je:", obsah_kruhu(float_polomer), jednotka)
else:
    print("Byl zadán neplatný formát.")




