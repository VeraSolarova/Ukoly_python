"""2) udělejte jednoduchou hru:

# pomocí modulu random vygenerujte náhodné číslo od 1 do 10

pak pomocí while True:
od uživatele získejte číslo
a pokud je toto číslo stejné jako vygenerované číslo před while cyklem
tak ukončete while cyklus, a vypište mu to dané číslo



Jak to udělat:
1) do proměnné cislo si vygeneruji náhodné číslo
2) while True:
3) od uživatele získam hodnotu pomocí input
4) porovnám zadonou hodnu s vygenerovaným číslem (pozor na datové typy)
5) pokud je shoda, ukončím cyklus pomocí break

v opačním případě nic nedělám a cyklus by se měl dále ptát na další číslo"""

from random import randrange

nahodne_cislo = randrange (1, 11, 1) # čísla od 1 do 10 s krokem 1 
print(nahodne_cislo) #napověda

uzivatelske_cislo = ""

while nahodne_cislo != uzivatelske_cislo:
    uzivatelske_cislo = int(input("Hádej číslo od 1 do 10, dokud jej neuhodneš"))

print("Hurá, uhodl jsi", nahodne_cislo)
