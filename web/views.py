from django.shortcuts import (redirect, render, render_to_response, )
from django.views import View
from django.utils import timezone
from django.template import loader, Context, RequestContext
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Articulo, Equipo, Torneo, Posiciones
from django.db.models import Q
import operator
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

# Create your views here.


def search(request):
    results = []
    query = request.GET.get('q', '')
    if query:
            qset = Q(titulo__icontains=query) | Q(cuerpo__icontains=query)
            results = Articulo.objects.filter(qset).distinct()
    return render_to_response('web/buscar.html', {"results": results, "query": query})

#Inicio
def web_view(request):
    """Returns the website."""
    articulos = Articulo.objects.all().order_by('-fecha_hora')[:5]
    articulos_fut = Articulo.objects.filter(categoria="Primera y Sub 21").order_by('-fecha_hora')[:3]
    articulos_inf = Articulo.objects.filter(categoria="Inferiores").order_by('-fecha_hora')[:3]
    articulos_senior = Articulo.objects.filter(categoria="Senior").order_by('-fecha_hora')[:3]
    articulos_inst = Articulo.objects.filter(categoria="Institucionales").order_by('-fecha_hora')[:3]
    articulos_basquet = Articulo.objects.filter(categoria="Basquet").order_by('-fecha_hora')[:3]
    articulos_hockey = Articulo.objects.filter(categoria="Hockey").order_by('-fecha_hora')[:3]
    
    return render(request, 'web/index.html', {'articulos': articulos, 
                                             'articulos_fut': articulos_fut,
                                             'articulos_inf': articulos_inf,
                                             'articulos_senior': articulos_senior,
                                             'articulos_inst': articulos_inst,
                                             'articulos_basquet': articulos_basquet,
                                             'articulos_hockey': articulos_hockey})

#Institucional
def novedades_institucionales_view(request):
    """Returns the page Novedades institucionales."""
    articulos_inst = Articulo.objects.filter(categoria="Institucionales").order_by('-fecha_hora')
    return render(request, 'web/novedades-institucionales.html', {'articulos': articulos_inst})

def historia_view(request):
    """Returns the page Historia."""
    return render(request, 'web/historia.html')

def estadio_view(request):
    """Returns the page Estadio."""
    return render(request, 'web/estadio.html')

def sede_view(request):
    """Returns the page Sede."""
    return render(request, 'web/sede.html')

def comision_view(request):
    """Returns the page Comision."""
    return render(request, 'web/autoridades.html')

#Primera y Sub-21
def novedades_futbol_view(request):
    """Returns the page Novedades Fútbol."""
    articulos_fut = Articulo.objects.filter(categoria="Primera y Sub 21").order_by('-fecha_hora')
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_fut, 3)
    
    try:
        articulos_fut = paginator.page(page)
    except PageNotAnInteger:
        articulos_fut = paginator.page(1)
    except EmptyPage:
        articulos_fut = paginator.page(paginator.num_pages)
    return render(request, 'web/novedades-futbol.html', {'articulos':articulos_fut})

def novedades_futbol_detail(request, slug):
    articulo_fut = get_object_or_404(Articulo, slug=slug)
    return render(request,'web/articulo_detail.html', {'articulo':articulo_fut})

def plantel_ct_futbol_view(request):
    """Returns the page Plantel y cuerpo técnico Fútbol."""
    return render(request, 'web/plantel-ct-futbol.html')

def fix_pos_futbol_view(request):
    """Returns the page Fixture y posiciones Fútbol."""
    primera = Posiciones.objects.filter(torneo__nombre="Primera").order_by('-puntos','-dif_gol', '-goles_favor')
    sub21 = Posiciones.objects.filter(torneo__nombre="Sub-21").order_by('-puntos','-dif_gol', '-goles_favor')
    general_primera = Posiciones.objects.filter(torneo__nombre="General Primera").order_by('-puntos','-dif_gol', '-goles_favor')
    general_sub21 = Posiciones.objects.filter(torneo__nombre="General Sub-21").order_by('-puntos','-dif_gol', '-goles_favor')
    return render(request, 'web/fix-pos-futbol.html', {'tablas':primera, 'tablas_sub21': sub21, 'general_p':general_primera, 'general_sub21':general_sub21})

#Inferiores
def novedades_inferiores_view(request):
    """Returns the page Novedades Inferiores."""
    articulos_inf = Articulo.objects.filter(categoria="Inferiores").order_by('-fecha_hora')
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_inf, 3)
    
    try:
        articulos_inf = paginator.page(page)
    except PageNotAnInteger:
        articulos_inf = paginator.page(1)
    except EmptyPage:
        articulos_inf = paginator.page(paginator.num_pages)
    return render(request, 'web/novedades-inferiores.html', {'articulos':articulos_inf})

def plantel_ct_inferiores_view(request):
    """Returns the page Plantel y cuerpo técnico Inferiores."""
    return render(request, 'web/plantel-ct-inferiores.html')

def fix_pos_inferiores_view(request):
    """Returns the page Fixture y posiciones inferiores."""
    novena = Posiciones.objects.filter(torneo__nombre="Novena").order_by('-puntos','-dif_gol', '-goles_favor')
    octava = Posiciones.objects.filter(torneo__nombre="Octava").order_by('-puntos','-dif_gol', '-goles_favor')
    septima = Posiciones.objects.filter(torneo__nombre="Septima").order_by('-puntos','-dif_gol', '-goles_favor')
    sexta = Posiciones.objects.filter(torneo__nombre="Sexta").order_by('-puntos','-dif_gol', '-goles_favor')
    general = Posiciones.objects.filter(torneo__nombre="General Inferiores").order_by('-puntos','-dif_gol', '-goles_favor')
    return render(request, 'web/fix-pos-inferiores.html', {'novena':novena, 'octava': octava,'septima':septima, 'sexta': sexta,'general':general })

def gurises_view(request):
    """Returns the page Los Gurises"""
    return render(request, 'web/gurises.html')

#Senior
def novedades_senior_view(request):
    """Returns the page Novedades Senior."""
    articulos_senior = Articulo.objects.filter(categoria="Senior").order_by('-fecha_hora')
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_senior, 3)
    
    try:
        articulos_senior = paginator.page(page)
    except PageNotAnInteger:
        articulos_senior = paginator.page(1)
    except EmptyPage:
        articulos_senior = paginator.page(paginator.num_pages)
    return render(request, 'web/novedades-senior.html', {'articulos':articulos_senior})

def plantel_ct_senior_view(request):
    """Returns the page Plantel y cuerpo técnico Senior."""
    return render(request, 'web/plantel-ct-senior.html')

def fix_pos_senior_view(request):
    """Returns the page Fixture y posiciones senior."""
    senior = Posiciones.objects.filter(torneo__nombre="Senior").order_by('-puntos','-dif_gol', '-goles_favor')
    senior_g = Posiciones.objects.filter(torneo__nombre="General Senior").order_by('-puntos','-dif_gol', '-goles_favor')
    return render(request, 'web/fix-pos-senior.html', {'senior':senior, 'general':senior_g})

#Básquet
def novedades_basquet_view(request):
    """Returns the page Novedades Básquet."""
    articulos_basquet = Articulo.objects.filter(categoria="Básquet").order_by('-fecha_hora')
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_basquet, 3)
    
    try:
        articulos_basquet = paginator.page(page)
    except PageNotAnInteger:
        articulos_basquet = paginator.page(1)
    except EmptyPage:
        articulos_basquet = paginator.page(paginator.num_pages)
    return render(request, 'web/novedades-basquet.html', {'articulos':articulos_basquet})

def plantel_ct_basquet_view(request):
    """Returns the page Plantel y cuerpo técnico Básquet."""
    return render(request, 'web/plantel-ct-basquet.html')

def fix_pos_basquet_view(request):
    """Returns the page Fixture y posiciones Básquet."""
    return render(request, 'web/fix-pos-basquet.html')

#Hockey
def novedades_hockey_view(request):
    """Returns the page Novedades Hockey."""
    articulos_hockey = Articulo.objects.filter(categoria="Hockey").order_by('-fecha_hora')
    page = request.GET.get('page', 1)
    paginator = Paginator(articulos_hockey, 3)
    
    try:
        articulos_hockey = paginator.page(page)
    except PageNotAnInteger:
        articulos_hockey = paginator.page(1)
    except EmptyPage:
        articulos_hockey = paginator.page(paginator.num_pages)
    return render(request, 'web/novedades-hockey.html', {'articulos':articulos_hockey})

def plantel_ct_hockey_view(request):
    """Returns the page Plantel y cuerpo técnico Hockey"""
    return render(request, 'web/plantel-ct-hockey.html')

def fix_pos_hockey_view(request):
    """Returns the page Fixture y posiciones Hockey."""
    primera = Posiciones.objects.filter(torneo__nombre="Hockey Primera").order_by('-puntos','-dif_gol', '-goles_favor')
    sexta = Posiciones.objects.filter(torneo__nombre="Hockey Sexta").order_by('-puntos','-dif_gol', '-goles_favor')
    septima = Posiciones.objects.filter(torneo__nombre="Hockey Septima").order_by('-puntos','-dif_gol', '-goles_favor')
    return render(request, 'web/fix-pos-hockey.html',{'primera': primera, 'sexta': sexta, 'septima':septima})










