from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Rachunki
from .filters import RachunkiFilter
from django.core.paginator import  Paginator
from django.core import serializers
from django.http import HttpResponse
from .resources import RachunkiResource
from django.db.models import Sum
from pyvis import network as net
import networkx  as nx


def graphs(request):
    g = net.Network(notebook=True)
    nxg = nx.complete_graph(4)
    g.from_nx(nxg)
    grafy = Rachunki.objects.all() 
    
    return render(request, 'basic.html',{'grafy':grafy})

def main(request):

    return render(request, 'main.html',{})

# definicja dla przeplywow
def przeplywy_mie_kont(request):
    context = {}
    przeplywy = Rachunki.objects.values(
        'konto_zrodlowe',
        'zleceniodawca',
        'konto_docelowe',
        'beneficjent',
        'waluta'
    ).annotate(Kwota_suma_3=Sum('kwota'))   
    context['dane'] = przeplywy

    count_rach = przeplywy.count() # odpowiednik SELECT * from przelewy_poiiids43_2020.analiza_rachunki
    context['przeplywy_ilosc'] = count_rach

    return render(request, 'przeplywy_kont.html',context)

# template dla sald kont źródłowych
def salda_kont(request):
  
    return render(request, 'salda_kont.html',{})


# Definicja dla wyliczeń sald kont docelowych
def salda_docel(request):
    context = {}
    salda = Rachunki.objects.values('konto_zrodlowe','zleceniodawca','waluta').annotate(Kwota_suma_2=Sum('kwota'))
    context['dane'] = salda
    return render(request, 'salda_docel.html',context)


def index(request):
    context = {}
    rachunki_filter = RachunkiFilter(request.GET, queryset=Rachunki.objects.all())
    context['filter'] = rachunki_filter
    ile_wierszy_strona= request.GET.get('choice_rows_page',1)
    paginator_rachunki = Paginator(rachunki_filter.qs, ile_wierszy_strona)
    page_number = request.GET.get('page',1) #pobranie danych z analiza.html metod get
    rachunki_page_obj = paginator_rachunki.get_page(page_number) 
    context['dane'] = rachunki_page_obj # wysanie zawartosci tabeli do analiza.html
    # całośiowa ilość danych
    rachunki = Rachunki.objects.all() #odpowienik SELECT ALL
    count_rach = rachunki.count() # odpowiednik SELECT * from przelewy_poiiids43_2020.analiza_rachunki
    context['filter_rachunki_count'] = count_rach
    # ----------------------------------
    count= rachunki_filter.qs.count()
    suma_page_kwota = rachunki_filter.qs.aggregate(kwota = Sum('kwota'))
    context['suma_kwota'] = suma_page_kwota
    # suma_page = rachunki_filter.qs.aggregate(Sum('kwota'))
    suma_page = rachunki_filter.qs.values('waluta').annotate(kwota=Sum('kwota'))
    context['suma_pag_front'] = suma_page
    context['filter_count'] = count

    return render(request, 'analiza.html',context)

def export_xml(request):
    location = Rachunki.objects.all()
    filter = RachunkiFilter(request.GET, queryset=location).qs
    queryset = serializers.serialize('xml',filter)
    return HttpResponse(queryset, content_type="application/xml")


def export_excel(request):
    rachunki_resource = RachunkiResource()
    dataset = rachunki_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="analiza.xls"'
    return response


