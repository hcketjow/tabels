from django.contrib import admin
from .models import Rachunki

@admin.register(Rachunki)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["tytul", "rodzaj_operaji"]
    search_fields = ("tytul", "rodzaj_operaji")