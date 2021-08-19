from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from .models import Rachunki

def index(request):
    dane_rach = Rachunki.objects.all()
    szukaj_id = request.GET.get('szukaj_id')
    szukaj_tytul = request.GET.get('szukaj_tytul')
    szukaj_oper = request.GET.get('szukaj_oper')
    szukaj_kwota = request.GET.get('szukaj_kwota')
    szukaj_waluta = request.GET.get('szukaj_waluta')
    szukaj_zrod = request.GET.get('szukaj_zrod')
    szukaj_docel = request.GET.get('szukaj_docel')
    szukaj_data_real = request.GET.get('szukaj_data_real')
    szukaj_data_zl = request.GET.get('szukaj_data_zl')
    szukaj_zlece = request.GET.get('szukaj_zlece')
    szukaj_bene = request.GET.get('szukaj_bene')
    szukaj_kod_rodz = request.GET.get('szukaj_kod_rodz')

    def is_valid_queryparam(param):
        return param !='' and param is not None

    if is_valid_queryparam(szukaj_id):
        dane_rach = dane_rach.filter(id__icontains=szukaj_id)
    if is_valid_queryparam(szukaj_tytul):
        dane_rach = dane_rach.filter(tytul__icontains=szukaj_tytul)
    if is_valid_queryparam(szukaj_oper):
        dane_rach = dane_rach.filter(rodzaj_operaji__icontains=szukaj_oper)
    if is_valid_queryparam(szukaj_kwota):
        dane_rach = dane_rach.filter(kwota__icontains=szukaj_kwota)
    if is_valid_queryparam(szukaj_waluta):
        dane_rach = dane_rach.filter(waluta__icontains=szukaj_waluta)
    if is_valid_queryparam(szukaj_zrod):
        dane_rach = dane_rach.filter(konto_zrodlowe__icontains=szukaj_zrod)
    if is_valid_queryparam(szukaj_docel):
        dane_rach = dane_rach.filter(konto_docelowe__icontains=szukaj_docel)
        # zmień ------------
    if is_valid_queryparam(szukaj_data_real):
        dane_rach = dane_rach.filter(data_realizacji__gte=szukaj_data_real)
    if is_valid_queryparam(szukaj_data_zl):
        dane_rach = dane_rach.filter(data_zlecenia_przelewu__gte=szukaj_data_zl)
        # ---------------------
    if is_valid_queryparam(szukaj_zlece):
        dane_rach = dane_rach.filter(zleceniodawca__icontains=szukaj_zlece)
    if is_valid_queryparam(szukaj_bene):
        dane_rach = dane_rach.filter(beneficjent__icontains=szukaj_bene)
    if is_valid_queryparam(szukaj_kod_rodz):
        dane_rach = dane_rach.filter(kod_rodzaju_transakcji__icontains=szukaj_kod_rodz)
    
    paginator = Paginator(dane_rach,25)
    page = request.GET.get('page')

    try: 
        analiza_dane = paginator.page(page)
    except PageNotAnInteger: 
        analiza_dane = paginator.page(1)
    except EmptyPage: 
        analiza_dane = paginator.page(paginator.num_pages)

    context = {
        'dane': analiza_dane
    }
    return render(request,'analiza.html',context)
