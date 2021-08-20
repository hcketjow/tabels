from django.db.models import fields
from django_filters.filters import ChoiceFilter
from .models import Rachunki
import django_filters

class RachunkiFilter(django_filters.FilterSet):
    tytul = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Rachunki
        fields = [
            'id',
            'tytul',
            'rodzaj_operaji',
            'kwota',
            'waluta',
            'konto_zrodlowe', 
            'konto_docelowe',
            'data_realizacji', 
            'data_zlecenia_przelewu',
            'zleceniodawca',
            'beneficjent',
            'kod_rodzaju_transakcji',
        ]