from django.shortcuts import render, redirect  
from peliculas.forms import PeliculasForm  
from peliculas.models import Peliculas 

def peliculas_index(request):  
    peliculas = Peliculas.objects.all()  
    return render(request,"peliculas/index.html",{'peliculas':peliculas})  

def peliculas_add(request):  
    if request.method == "POST":  
        form = PeliculasForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/peliculas')  
            except:  
                pass  
    return render(request,'peliculas/add.html')  


def peliculas_edit(request, id):  
    pelicula = Peliculas.objects.get(id=id)  
    return render(request,'peliculas/edit.html', {'pelicula':pelicula})  

def peliculas_update(request, id):  
    pelicula = Peliculas.objects.get(id=id)  
    form = PeliculasForm(request.POST, instance = pelicula)  
    if form.is_valid():  
        form.save()  
        return redirect("/peliculas")  
    return render(request, 'peliculas/edit.html', {'pelicula': pelicula})  

def peliculas_destroy(request, id):  
    pelicula = Peliculas.objects.get(id=id)  
    pelicula.delete()  
    return redirect("/peliculas")  