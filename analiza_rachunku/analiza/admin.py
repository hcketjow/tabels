from .resources import RachunkiResource
from django.contrib import admin
from .models import Rachunki
from import_export.admin import ImportExportModelAdmin


class FilmAdmin(admin.ModelAdmin):
    list_display = ["tytul", "rodzaj_operaji"]
    search_fields = ("tytul", "rodzaj_operaji")
  

class RachunkiAdmin(ImportExportModelAdmin):
    resource_class = RachunkiResource

admin.site.register(Rachunki, RachunkiAdmin)

