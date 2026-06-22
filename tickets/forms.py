from django import forms
from .models import Pelicula, Funcion

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'sinopsis', 'duracion', 'poster']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = ['pelicula', 'sala', 'fecha_hora', 'precio_entrada', 'formato']
        widgets = {
            'pelicula': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'precio_entrada': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'formato': forms.Select(attrs={'class': 'form-control'}),
        }