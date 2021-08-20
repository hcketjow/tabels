from django.shortcuts import render
from .models import Rachunki
from django.views.generic import ListView
from .filters import RachunkiFilter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

class RachunkiView(ListView):
    model = Rachunki
    template_name = 'analiza.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filter'] = RachunkiFilter(self.request.GET, queryset=self.get_queryset())
        return context
    
    # def analiza_paginacja(request):
    #     lista = Rachunki.objects.all()
        
    #     paginator = Paginator(lista,25)
    #     page = request.GET.get('page')
    #     try: 
    #         lists = paginator.page(page)
    #     except PageNotAnInteger: 
    #         lists = paginator.page(1)
    #     except EmptyPage: 
    #         lists = paginator.page(paginator.num_pages)

    #     context={
    #         'dane': lists,
    #     }
    #     return context