from django.shortcuts import render, redirect  
from libros.forms import LibrosForm  
from libros.models import Libros

def libros_index(request):  
    libros = Libros.objects.all()  
    return render(request,"libros/index.html",{'libros':libros})  

def libros_add(request):  
    if request.method == "POST":  
        form = LibrosForm(request.POST)  
        if form.is_valid():  
            print('wenaoe')  
            form.save()
            print('malaoe')  
            return redirect('/libros')  

    else:  
        form = LibrosForm()  
    return render(request,'libros/add.html',{'form':form})  


def libros_edit(request, id):  
    libro = Libros.objects.get(id=id)  
    return render(request,'libros/edit.html', {'libro':libro})  

def libros_update(request, id):  
    libro = Libros.objects.get(id=id)  
    form = LibrosForm(request.POST, instance = libro)  
    if form.is_valid():  
        form.save()  
        return redirect("/libros")  
    return render(request, 'libros/edit.html', {'libro': libro})  

def libros_destroy(request, id):  
    libros = Libros.objects.get(id=id)  
    libros.delete()  
    return redirect("/libros")  