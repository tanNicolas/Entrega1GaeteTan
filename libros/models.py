from statistics import mode
from django.db import models

# Create your models here.
from django.utils import timezone

class Libros(models.Model):
    titulo = models.CharField(max_length=50, default='Título')
    autor = models.CharField(max_length=50, default='Autor')
    genero = models.CharField(max_length=50, default='Género')
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'libros'
