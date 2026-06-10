from django.db import models
from usuarios.models import UsuarioPersonalizado

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Sala(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ej: Sala 1, Sala 2, etc.")
    capacidad = models.IntegerField()
    

    def __str__(self):
        return f"{self.nombre} ({self.capacidad} asientos)"

class Funcion(models.Model):
    FORMATO_CHOICES = [
        ('2D', 'Proyección 2D'),
        ('3D', 'Proyección 3D'),
        ('4D', 'Proyección 4D'),
    ]
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='funciones')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='funciones')
    fecha_hora = models.DateTimeField()
    precio_entrada = models.DecimalField(max_digits=8, decimal_places=2)
    formato = models.CharField(max_length=2, choices=FORMATO_CHOICES, default='2D')

    def __str__(self):
        return f"{self.pelicula.titulo} ({self.formato}) - {self.sala.nombre} - {self.fecha_hora.strftime('%d/%m %H:%M')}"


class Ticket(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='tickets')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='tickets')
    cantidad_asientos = models.IntegerField()
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.usuario.username} ({self.cantidad_asientos} ent.)"


class Resena(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE, related_name='resenas')
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='resenas')
    comentario = models.TextField()
    puntuacion = models.IntegerField(help_text="Del 1 al 5")

    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.pelicula.titulo} ({self.puntuacion}⭐)"