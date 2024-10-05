"""
vytvořte 19_unittest.py

v něm třídu pro test case

toto je testovaná funkce, vaším úkolem je napsat test
vaším úkolem není implementace této funkce, ale pouze test, který neprojde

pro faktorial se značí vykřičníkem a platí:
!0 = 1
!1 = 1
!2 = 1 * 2
!3 = 1 * 2 * 3
!4 = 1 * 2 * 3 * 4
atd ...
pro zápornou hodnotu vyhodí ValueError

měli byste tedy otestovat čísla:
0, 1 -> by měl vracet 1
pak libovolné číslo -> faktorial daného čísla, např !5 = 120
pozor faktorial roste obrovským skokem !10 = 3628800
pak záporné číslo -> ValueError


def faktorial(cislo):
    # tuto funkci neimplementujte, uděláme si ve škole
    pass

faktorial wiki
https://cs.wikipedia.org/wiki/Faktori%C3%A1l

"""

import unittest 
import nazev_testovaneho_souboru

class TestFaktorial(unittest.TestCase):
    def test_0(self):
        result = nazev_testovaneho_souboru.faktorial(0)
        self.assertEqual(result, 1) # assertEqual == srovná hodnoty výsledku funkce (při zadání vstupní hodnoty 0 do fce) s očekávaným výsledkem 1

    def test_1(self):
        result = nazev_testovaneho_souboru.faktorial(1)
        self.assertEqual(result, 1)

    def test_5(self):
        result = nazev_testovaneho_souboru.faktorial(5)
        self.assertEqual(result, 120)

    def test_zaporne(self):
        with self.assertRaises(ValueError):
            nazev_testovaneho_souboru.faktorial(-1) # with self.assertRaises(ValueError) - testuje zda při zadání vstupní hodnoty -1 do fce vyhodí testovaná funkce ValueError

unittest.main()