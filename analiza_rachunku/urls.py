"""analiza_rachunku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from analiza.views import index,export_excel,export_xml,main,przeplywy_mie_kont,salda_kont,salda_docel,graphs
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('', main, name="poczatek"),
    path('analiza/',index, name="main"),
    path('export_excel', export_excel, name='export_excel'),
    path('export_xml', export_xml, name='export_xml'),
    path('przeplywy_kont',przeplywy_mie_kont,name='przeplywy_kont'),
    path('salda_kont',salda_kont,name='salda_kont'),
    path('salda_docel',salda_docel,name='salda_docel'),
    path('graphs',graphs,name='graphs'),
  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)