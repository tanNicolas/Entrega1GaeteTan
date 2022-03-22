from django import forms  
from juegos.models import Juegos
class JuegosForm(forms.ModelForm):  
    class Meta:  
        model = Juegos  
        fields = "__all__"  