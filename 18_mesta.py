"""vytvořte soubor 18_mesta.py a v něm 2 třídy:

Stat
Mesto

oba budou mít název, mesto bude mít referenci na stát
Mesto tedy na venek dokáže zjistit název státu ke kterému patří
Mesto bude mít metodu info, která vypíše:
- "Město ABC leží ve státě XYZ"

Bonusový úkol:
Stat bude mít metodu info, která dokáže zjistit, kolik má měst
- implementaci nechám na vás

použití:

dansko = Stat('Dansko')
norsko = Stat('Norsko')

kodan = Mesto('Kodaň', dansko)
hovedstaden = Mesto('Hovedstaden', dansko)

oslo = Mesto('Oslo', norsko)

oslo.info() # vypíše "Město Oslo leží ve státě Norsko"
kodan.info() # vypíše "Město Kodan leží ve státě Dánsko"""

class Stat:
    def __init__(self, nazev_statu: str,) -> None:
        self.nazev_statu = nazev_statu
        self.seznam_mest = [] # každy stát bude mít list se svými městy 

    def pridat_mesto(self, mesto: "Mesto"):
    # metoda na přidání města do listu příslušného státu, zavolá si ji každé nově vzniklé město 
        self.seznam_mest.append(mesto) 

    def __str__(self):
        return self.nazev_statu
      
    def info(self):
        print("Ve státě", self.nazev_statu, "leží", len(self.seznam_mest) , "měst/a a jsou to:", self.seznam_mest) 


class Mesto:
    def __init__(self, nazev_mesta: str, stat_kde_lezim: Stat) -> None:
        self.nazev_mesta = nazev_mesta
        self.stat_kde_lezim = stat_kde_lezim
        self.stat_kde_lezim.pridat_mesto(self.mesto) # volá metodu pridat_mesto z class Stat - přidá město do listu 

    def info(self):
        print(f"Město {self.nazev_mesta} leží ve státě {self.stat_kde_lezim}") 


zeme_cz = Stat("Česká Republika")
mesto_cz_1 = Mesto("Praha", zeme_cz)
mesto_cz_2 = Mesto("Brno", zeme_cz)
zeme_sk = Stat("Slovenská republika")
mesto_sk_1 = Mesto("Bratislava", zeme_sk)
mesto_sk_2 = Mesto("Košice", zeme_sk)

mesto_cz_1.info()
mesto_sk_1.info()
zeme_cz.info()
zeme_sk.info()
