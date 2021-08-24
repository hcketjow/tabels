from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Rachunki
from django.views.generic import ListView
from .filters import RachunkiFilter
from . import filters
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core import serializers
import xlwt
from django.http import HttpResponse
from .resources import RachunkiResource
from tablib import Dataset

def index(request):
    analiza_list = Rachunki.objects.all()
    user_filter = RachunkiFilter(request.GET, queryset=analiza_list)
    filtered_qs = RachunkiFilter(request.GET, queryset=Rachunki.objects.all()).qs
    paginator = Paginator(filtered_qs, 25)
    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
    context={
        'dane': response,
        'filter': user_filter
    }
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


