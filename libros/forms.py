from django import forms  
from libros.models import Libros
class LibrosForm(forms.ModelForm):  
    class Meta:  
        model = Libros  
        fields = "__all__"  