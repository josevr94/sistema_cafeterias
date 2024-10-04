from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    model = Contacto
    fields = ['nombre','apellido','email','descripcion']