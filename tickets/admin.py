from django.contrib import admin
from .models import Pelicula, Sala, Funcion, Ticket, Resena

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracion') 
    search_fields = ('titulo', 'sinopsis') # busqueda por titulo o texto
    ordering = ('titulo',) # ordenado alfabeticamente

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad')
    search_fields = ('nombre',)

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'sala', 'formato', 'fecha_hora', 'precio_entrada')
    list_filter = ('formato', 'sala', 'fecha_hora') # filtros laterales re chetos
    search_fields = ('pelicula__titulo',) # buscar por el titulo de la película 
    ordering = ('fecha_hora',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'funcion', 'cantidad_asientos', 'fecha_compra')
    list_filter = ('fecha_compra', 'funcion__formato')
    search_fields = ('usuario__username', 'funcion__pelicula__titulo')
    ordering = ('-fecha_compra',) # el menos (-) hace que los mas nuevos aparezcan primero 

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'puntuacion')
    list_filter = ('puntuacion',)
    search_fields = ('usuario__username', 'pelicula__titulo', 'comentario')