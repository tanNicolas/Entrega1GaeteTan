from django.db import models

# Create your models here.
from django.utils import timezone

class Juegos(models.Model):
    nombre = models.CharField(max_length=50, default='Juego')
    precio = models.IntegerField(default=0)
    plataforma = models.CharField(max_length=50, default='PC')
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'juegos'