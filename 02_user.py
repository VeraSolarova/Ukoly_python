"""2) vytvořte 02_user.py kde
uživatel zadá své jmeno a věk pomocí input
uložte tyto informace do souboru
02_user.txt"""


jmeno = input ("Jak se jmenuješ? ")
vek = input ("Kolik je Ti let? ")

with open ("02_user.txt", "a") as file:
    file.write(jmeno + ", " + vek + "\n")