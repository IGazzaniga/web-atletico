from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Articulo(models.Model):
    """Un artículo de la página"""
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default="")
    CATEGORIAS = (
        ('Primera y Sub 21', 'Primera y Sub 21'),
        ('Inferiores', 'Inferiores'),
        ('Básquet', 'Básquet'),
        ('Hockey', 'Hockey'),
        ('Gurises', 'Gurises'),
        ('Generales', 'Generales'),
        ('Institucionales', 'Institucionales'),
        ('Senior', 'Senior'),
    )
    categoria = models.CharField(
        max_length=200,
        choices=CATEGORIAS
    )
    cuerpo = RichTextField()
    fecha_hora= models.DateTimeField()
    url_foto = models.CharField(help_text='Url de la imagen, previamente subida a FB u otro lugar', default="", max_length=1500)
    url_video = models.CharField(help_text='Url del video de facebook (opcional). Para obtener el link, ir al video, apretar donde están los 3 puntitos y poner "insertar". Pegar aquí solo el link del video, borrar el resto. Ejemplo: https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2FJuanCruzPiornoOficial%2Fvideos%2F302760100205413', max_length=500,blank=True)
    album_flickr = models.CharField(help_text="Subir fotos a Flickr, crear un álbum, compartirlo eligiendo la opción 'Insertar', elegir el tamaño más grande, y pegar el link aquí", max_length=700, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)

        super(Articulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    

class Equipo(models.Model):
    """Equipos de la todos los deportes, se agregan los necesarios a cada tabla"""
    nombre = models.CharField(max_length=200) #Nombre del equipo

    def __str__(self):
        return self.nombre


class Torneo(models.Model):
    """Cada torneo contiene un nombre (Apertura/Clausura/Liguilla), y a su vez contiene equipos"""
    NOMBRES = (
        ('Primera', 'Primera'),
        ('Sub-21', 'Sub-21'),
        ('General Primera', 'General Primera'),
        ('General Sub-21', 'General Sub-21'),
        ('Novena', 'Novena'),
        ('Octava', 'Octava'),
        ('Septima', 'Septima'),
        ('Sexta', 'Sexta'),
        ('General Inferiores', 'General Inferiores'),
        ('Senior', 'Senior'),
        ('General Senior', 'General Senior'),
        ('Hockey Primera', 'Hockey Primera'),
        ('Hockey Sexta', 'Hockey Sexta'),
        ('Hockey Septima', 'Hockey Septima'),
    )
    nombre = models.CharField(
        max_length=200,
        choices=NOMBRES
    )
    equipos = models.ManyToManyField(Equipo, through='Posiciones')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)

class Posiciones(models.Model):
    """Tabla de posiciones de cada torneo"""
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=0, verbose_name='Pts') #Puntos del actual torneo
    p_jugados = models.IntegerField(default=0, verbose_name='PJ') #Partidos jugados en el actual toreno
    p_ganados = models.IntegerField(default=0, verbose_name='PG') #Partidos ganados en el actual torneo
    p_empatados = models.IntegerField(default=0, verbose_name='PE') #Partidos empatados en el actual torneo
    p_perdidos = models.IntegerField(default=0, verbose_name='PP') #Partidos perdidos en el actual torneo
    goles_favor = models.IntegerField(default=0, verbose_name='GF') #Goles a favor en el actual torneo
    goles_contra = models.IntegerField(default=0, verbose_name='GC') #Goles en contra en el actual torneo
    dif_gol = models.IntegerField(default=0, verbose_name='DG') #Diferencia de gol en el actual torneo
    






