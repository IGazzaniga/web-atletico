"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import (url, include)
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from web import views
from web.views import (search, web_view, novedades_institucionales_view, historia_view, estadio_view, 
                       sede_view, comision_view, novedades_futbol_view, novedades_futbol_detail, 
                       plantel_ct_futbol_view, fix_pos_futbol_view, novedades_inferiores_view,
                       plantel_ct_inferiores_view, fix_pos_inferiores_view, gurises_view, novedades_senior_view,
                       plantel_ct_senior_view, fix_pos_senior_view, novedades_basquet_view, 
                       plantel_ct_basquet_view,fix_pos_basquet_view, novedades_hockey_view, 
                       plantel_ct_hockey_view, fix_pos_hockey_view) #Importamos las vistas

urlpatterns = [url(r'^admin/', include(admin.site.urls)),
    url(r'^$', web_view, name="index"),
    
    url(r'^novedades-institucionales$', novedades_institucionales_view, name="novedades-institucionales"),
    url(r'^historia$', historia_view, name="historia"),
    url(r'^estadio$', estadio_view, name="estadio"),
    url(r'^sede$', sede_view, name="sede"),
    url(r'^autoridades$', comision_view, name="autoridades"),

    
    
    
   
    url(r'^novedades-futbol$', novedades_futbol_view, name="novedades-futbol"),
    url(r'^plantel-ct-futbol$', plantel_ct_futbol_view, name="plantel-ct-futbol"),
    url(r'^fix-pos-futbol$', fix_pos_futbol_view, name="fix-pos-futbol"),
   
    

   
    url(r'^novedades-inferiores$', novedades_inferiores_view, name="novedades-inferiores"),
    url(r'^plantel-ct-inferiores$', plantel_ct_inferiores_view, name="plantel-ct-inferiores"),
    url(r'^fix-pos-inferiores$', fix_pos_inferiores_view, name="fix-pos-inferiores"),
    url(r'^gurises$', gurises_view, name="gurises"),

    
    url(r'^novedades-senior$', novedades_senior_view, name="novedades-senior"),
    url(r'^plantel-ct-senior$', plantel_ct_senior_view, name="plantel-ct-senior"),
    url(r'^fix-pos-senior$', fix_pos_senior_view, name="fix-pos-senior"),

    
    url(r'^novedades-basquet$', novedades_basquet_view, name="novedades-basquet"),
    url(r'^plantel-ct-basquet$', plantel_ct_basquet_view, name="plantel-ct-basquet"),
    url(r'^fix-pos-basquet$', fix_pos_basquet_view, name="fix-pos-basquet"),
    
    
    url(r'^novedades-hockey$', novedades_hockey_view, name="novedades-hockey"),
    url(r'^plantel-ct-hockey$', plantel_ct_hockey_view, name="plantel-ct-hockey"),
    url(r'^fix-pos-hockey$', fix_pos_hockey_view, name="fix-pos-hockey"),
    
    url(r'^noticia/(?P<slug>[\w-]+)$', novedades_futbol_detail, name="detail"),
    url(r'^search/$', search, name="search"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)