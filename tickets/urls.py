from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
    path('peliculas/nueva/', views.crear_pelicula, name='crear_pelicula'),
    path('peliculas/editar/<int:id_pelicula>/', views.editar_pelicula, name='editar_pelicula'),
    path('peliculas/eliminar/<int:id_pelicula>/', views.eliminar_pelicula, name='eliminar_pelicula'),
    
    #urls de vista funciones    
    path('funciones/', views.lista_funciones, name='lista_funciones'),
    path('funciones/nueva/', views.crear_funcion, name='crear_funcion'),
    path('funciones/editar/<int:id_funcion>/', views.editar_funcion, name='editar_funcion'),
    path('funciones/eliminar/<int:id_funcion>/', views.eliminar_funcion, name='eliminar_funcion'),
]