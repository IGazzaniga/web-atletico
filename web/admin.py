from django.contrib import admin

# Register your models here.
from .models import Articulo, Equipo, Torneo, Posiciones

class ArticuloAdmin(admin.ModelAdmin):
    fields = ['titulo', 'categoria', 'cuerpo', 'fecha_hora', 'foto', 'url_video', 'album_flickr']

admin.site.register(Articulo, ArticuloAdmin)

class EquipoAdmin(admin.ModelAdmin):
    fields = ['nombre']
admin.site.register(Equipo, EquipoAdmin)


class PosicionesInline(admin.TabularInline):
    model = Posiciones
    extra= 0

class TorneoAdmin(admin.ModelAdmin):
    inlines = (PosicionesInline,)
    
admin.site.register(Torneo, TorneoAdmin)