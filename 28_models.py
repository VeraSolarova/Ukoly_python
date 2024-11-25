 # One-to-one  -  uraz = models.OneToOneField(Uraz, on_delete=models.CASCADE) -  jeden pacient muze mit prave jeden uraz(jedno id_urazu) a naopak 
            # on_delete=models.CASCADE bude-li smazan uraz, bude smazan i zaznam o pacientovi 

# One-to-many -  podkategorie = models.ForeignKey(Podkategorie, on_delete=models.PROTECT)  # Jak došlo k úrazu  --- jeden uraz ma pouze jeden zpusob, jak k němu došlo. Jine urazy ale mohjou mit stejnou podkategorii
            # on_delete=models.PROTECT - zabrání smazání podkategorie, pokud je na ně navázán nějaký záznam o úrazu - vyvolá IntegrityError
            # on_delete=models.SET_NULL  pokud je akceptovatelné, aby úrazy zůstaly v databázi bez přiřazené podkategorie a může li podkategorie obsahovat pole hodnotu NULL

# Many-to-many - diagnozy = models.ManyToManyField(Diagnoza) - jeden uraz (id urazu) muze mit vice diagnoz zaroven a naopak

# null=True,blank=True, 
            # null=True - umožňuje hodnotu NULL
            # blank=True - Uživatel může toto pole přeskočit a formulář lze uložit, uloží se hodnota NULL.
            # podkategorie = models.ForeignKey(Podkategorie, null=True,blank=True,  on_delete=models.PROTECT)   

# CharField(max_length=100) -  krátké texty, povinný parametr  max_lenght,  name = models.CharField(max_length=100), ukládá jako "varchar"
# TextField - dlouhé texty bez omezení délky, ukládá se jako "text"
# IntegerField - Volitelný atribut validators - pro omezení , jen celá čísla, ukládá se jako "integer"
 

from django.db import models


class Diagnoza(models.Model):
    kod = models.CharField(max_length=7, unique=True)  #  např. S00_S09
    popis = models.CharField(max_length=100) #  např. "Poranění hlavy."

    def __str__(self):
        return f"{self.kod}: {self.popis}"



class Vaznost(models.Model):
    kod = models.CharField(max_length=7, unique=True) #  např. I-a
    popis = models.CharField(max_length=100)  #  např. "Úraz ošetřený pouze ambulantně, bez další léčby a následků"

    def __str__(self):
        return f"{self.kod}: {self.popis}"
    


class Podkategorie(models.Model): # jak došlo k úrazu
    kod = models.CharField(max_length=10, unique=True)   #  např.V80-V89 
    popis = models.CharField(max_length=200)  #  např. "Nehody při pozemní dopravě."

    def __str__(self):
        return f"{self.kod}: {self.popis}"
    


class Umrti(models.Model):
    kod = models.CharField(max_length=10, null=True)  # Může obsahovat NULL  #  např. III-b
    popis = models.CharField(max_length=200)  #  např. Úmrtí při léčbě/ po léčbě/ okamžitě

    def __str__(self):
        return f"{self.kod}: {self.popis}"


class Kraj(models.Model):
    kod = models.CharField(max_length=5)
    popis = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.kod}: {self.popis}"

class Pohlavi(models.Model):
    kod = models.IntegerField
    popis = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.kod}: {self.popis}"

class Vek(models.Model):
    kod = models.IntegerField
    popis = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.kod}: {self.popis}"


class Uraz(models.Model):
    id_urazu = models.IntegerField()
    rok = models.IntegerField()  # Rok úrazu
    mesic = models.IntegerField()  # Měsíc úrazu
    operace = models.BooleanField(default=False)  # Byla operace?
    dlouha_jip = models.BooleanField(default=False)  # Dlouhá hospitalizace na JIP?
    masledna_pece = models.BooleanField(default=False)  # Byla poskytnuta následná péče?
    
    kraj_icz = models.ForeignKey(Kraj, on_delete=models.PROTECT)  # Kód kraje, kde byla poskytnuta péče
    podkategorie = models.ForeignKey(Podkategorie, null=True,blank=True,  on_delete=models.PROTECT)  # Jak došlo k úrazu  
    umrti = models.ForeignKey(Umrti, null=True, blank=True, on_delete=models.PROTECT)  
    diagnozy = models.ManyToManyField(Diagnoza)  # Může být i více diagnóz (tj. více druhů zranění) pro jeden úraz - jedno id_urazu
    
    def __str__(self):
        return f"Úraz {self.id_urazu}"



class Pacient(models.Model):
    polytrauma = models.BooleanField(default=False)  # Má pacient polytrauma?

    pohlavi = models.ForeignKey(Pohlavi, on_delete=models.PROTECT)
    vek_kat = models.ForeignKey(Kraj, on_delete=models.PROTECT)
    kraj_pacient = models.ForeignKey(Kraj, on_delete=models.PROTECT)  # Kód kraje, odkud je pacient
    uraz = models.OneToOneField(Uraz, on_delete=models.CASCADE)  # Vztah na Úraz (každý pacient má jeden úraz)

    def __str__(self):
        return f"Pacient {Uraz.id_urazu}: {self.pohlavi}"