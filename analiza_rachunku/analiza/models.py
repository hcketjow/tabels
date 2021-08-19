from django.db import models

class Rachunki(models.Model):
    WALUTA = {
        ('PLN', 'PLN'),
        ('EUR','EUR'),
    }
    tytul = models.CharField(default="", max_length=1150)
    rodzaj_operaji = models.CharField(default="", max_length=1150)
    kwota = models.PositiveSmallIntegerField(default=0)
    waluta = models.CharField(max_length=4,default="", choices=WALUTA)
    konto_zrodlowe = models.CharField(default="",max_length=100)
    konto_docelowe = models.CharField(default="",max_length=100)
    data_realizacji = models.DateField(blank=True, null=True)
    data_zlecenia_przelewu = models.DateField(blank=True, null=True)
    zleceniodawca = models.CharField(default="", max_length=1500)
    beneficjent = models.CharField(default="", max_length=1550)
    kod_rodzaju_transakcji = models.CharField(default="", max_length=1200)

    def __str__(self):
        return self.analzia_danych()

    def analzia_danych(self):
        return "{} ({})".format(self.tytul, self.rodzaj_operaji)