from django.db.models import fields
from import_export import resources
from .models import Rachunki

class RachunkiResource(resources.ModelResource):
    class Meta:
        model = Rachunki
    

        