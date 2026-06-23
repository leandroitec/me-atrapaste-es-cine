# tickets/context_processors.py
from datetime import datetime
from .models import Pelicula

def info_cine(request):
    #retorna un diccionario con variables globales 
    return {
        'nombre_cine': '🍿 Me Atrapaste, Es Cine',
        'anio_actual': datetime.now().year,
        'total_peliculas': Pelicula.objects.count() 
    }