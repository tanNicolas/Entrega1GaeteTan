from django.shortcuts import render, redirect  
from juegos.forms import JuegosForm  
from juegos.models import Juegos 

def juegos_index(request):  
    juegos = Juegos.objects.all()  
    return render(request,"juegos/index.html",{'juegos':juegos})  

def juegos_add(request):  
    if request.method == "POST":  
        form = JuegosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/juegos')  
            except:  
                pass  
    else:  
        form = JuegosForm()  
    return render(request,'juegos/add.html',{'form':form})  


def juegos_edit(request, id):  
    juego = Juegos.objects.get(id=id)  
    return render(request,'juegos/edit.html', {'juego':juego})  

def juegos_update(request, id):  
    juego = Juegos.objects.get(id=id)  
    form = JuegosForm(request.POST, instance = juego)  
    if form.is_valid():  
        form.save()  
        return redirect("/juegos")  
    return render(request, 'juegos/edit.html', {'juegos': juego})  

def juegos_destroy(request, id):  
    juegos = Juegos.objects.get(id=id)  
    juegos.delete()  
    return redirect("/juegos")  