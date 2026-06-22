from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Pelicula, Funcion
from .forms import PeliculaForm, FuncionForm


@login_required
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'tickets/lista_peliculas.html', {'peliculas': peliculas})


@login_required
@permission_required('tickets.add_pelicula', login_url='home', raise_exception=True)
def crear_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'tickets/formulario_pelicula.html', {'form': form, 'titulo_accion': 'Agregar Película'})


@login_required
@permission_required('tickets.change_pelicula', login_url='home', raise_exception=True)
def editar_pelicula(request, id_pelicula):
    pelicula = get_object_or_404(Pelicula, id=id_pelicula)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'tickets/formulario_pelicula.html', {'form': form, 'titulo_accion': 'Editar Película'})


@login_required
@permission_required('tickets.delete_pelicula', login_url='home', raise_exception=True)
def eliminar_pelicula(request, id_pelicula):
    pelicula = get_object_or_404(Pelicula, id=id_pelicula)
    if request.method == 'POST':
        pelicula.delete()
        return redirect('lista_peliculas')
    return render(request, 'tickets/confirmar_eliminar.html', {'objeto': pelicula})

# vistas de las funciones

@login_required
def lista_funciones(request):
    funciones = Funcion.objects.all().order_by('fecha_hora')
    return render(request, 'tickets/lista_funciones.html', {'funciones': funciones})

@login_required
@permission_required('tickets.add_funcion', login_url='home', raise_exception=True)
def crear_funcion(request):
    if request.method == 'POST':
        form = FuncionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funciones')
    else:
        form = FuncionForm()
    return render(request, 'tickets/formulario_funcion.html', {'form': form, 'titulo_accion': 'Programar Nueva Función'})


@login_required
@permission_required('tickets.change_funcion', login_url='home', raise_exception=True)
def editar_funcion(request, id_funcion):
    funcion = get_object_or_404(Funcion, id=id_funcion)
    if request.method == 'POST':
        form = FuncionForm(request.POST, instance=funcion)
        if form.is_valid():
            form.save()
            return redirect('lista_funciones')
    else:
        form = FuncionForm(instance=funcion)
    return render(request, 'tickets/formulario_funcion.html', {'form': form, 'titulo_accion': 'Editar Función'})


@login_required
@permission_required('tickets.delete_funcion', login_url='home', raise_exception=True)
def eliminar_funcion(request, id_funcion):
    funcion = get_object_or_404(Funcion, id=id_funcion)
    if request.method == 'POST':
        funcion.delete()
        return redirect('lista_funciones')
    return render(request, 'tickets/confirmar_eliminar.html', {'objeto': funcion})