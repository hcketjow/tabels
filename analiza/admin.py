from analiza.resources import RachunkiResource
from django.contrib import admin
from .models import Rachunki
from import_export.admin import ImportExportModelAdmin


class RachunkiAdmin(ImportExportModelAdmin):
    resource_class = RachunkiResource

admin.site.register(Rachunki, RachunkiAdmin)