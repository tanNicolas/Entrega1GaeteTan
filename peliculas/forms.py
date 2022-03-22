from django import forms  
from peliculas.models import Peliculas

class PeliculasForm(forms.ModelForm):  
    class Meta:  
        model = Peliculas  
        fields = "__all__"  