"""vytvořte 12_try_except.py

kde budou data:
mesta_cr = {
    "Praha": 1300000,
    "Brno": 380000,
    "Ostrava": 290000,
    "Plzeň": 170000,
    "Liberec": 100000,
    "Olomouc": 100000,
    "Ústí nad Labem": 92000,
    "Hradec Králové": 93000,
    "České Budějovice": 94000,
    "Pardubice": 90000
}

vytvořte funkci info, které dokáže zjistit informace o měste
použíjte try except pro KeyError
pro print použijte 

def info(nazev_mesta):
    # použijte
    # print(nazev_mesta, mesta_cr[nazev_mesta])
    # tento print musí být ošetřen, protože k prvkům dict přistupujeme přímo

použití:
info('Praha') # vyprintuje Praha 1300000
info('New York') # vyprintuje 'neznámé město'
"""

mesta_cr = {
    "Praha": 1300000,
    "Brno": 380000,
    "Ostrava": 290000,
    "Plzeň": 170000,
    "Liberec": 100000,
    "Olomouc": 100000,
    "Ústí nad Labem": 92000,
    "Hradec Králové": 93000,
    "České Budějovice": 94000,
    "Pardubice": 90000
}

def info(nazev_mesta):
    try:
        if nazev_mesta in mesta_cr:
            print(nazev_mesta, mesta_cr[nazev_mesta])
        else: 
             raise KeyError # raise zavolá výslovně KeyError
    except(KeyError): # Pokud nstane Key Error, nezastaví se program, ale vyprintuje..   
            print("Neznámé město")
    
info("Praha")
info("New York")

def info2(nazev_mesta):
        if nazev_mesta in mesta_cr:
            print(nazev_mesta, mesta_cr[nazev_mesta])
        else: 
             print("Neznámé město")

info2("Praha")
info2("New York")
