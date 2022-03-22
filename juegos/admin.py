from django.contrib import admin
from .models import Juegos
# Register your models here.

class JuegosAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Juegos, JuegosAdmin)