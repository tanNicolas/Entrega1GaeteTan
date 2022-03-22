from django.shortcuts import render

from django.shortcuts import render, redirect
from juegos.models import Juegos
from peliculas.models import Peliculas
from libros.models import Libros

def buscador_index(request):   
    return render(request,"buscador/search.html")  

def buscador_resultado(request): 
    if request.method == "POST": 
        buscado = request.POST['buscador']

        juegos = Juegos.objects.filter(nombre__icontains=buscado)
        peliculas = Peliculas.objects.filter(nombre__icontains=buscado)
        libros = Libros.objects.filter(titulo__icontains=buscado)

        resultados = []

        for juego in juegos:
            resultados.append({
                'nombre': juego.nombre,
                'categoria': 'Juego',
            })

        for pelicula in peliculas:
            resultados.append({
                'nombre': pelicula.nombre,
                'categoria': 'Pelicula',
            })

        for libro in libros:
            resultados.append({
                'nombre': libro.titulo,
                'categoria': 'Libro',
            })
        return render(request,"buscador/result.html",{'resultados':resultados})
        
    return render(request,"buscador/search.html")  

