from django.db import models

class Peliculas(models.Model):
    nombre = models.CharField(max_length=50, default='Pelicula')
    director = models.CharField(max_length=50, default='Director')
    genero = models.CharField(max_length=50, default='Genero')
    duracion = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'peliculas'
