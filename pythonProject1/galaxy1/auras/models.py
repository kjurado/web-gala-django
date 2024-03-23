from django.db import models

# Create your models here.
class Aura (models.Model):
    nombre = models.CharField(max_length=100)
    puntos_de_autoridad = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='media/auras/')  # La carpeta 'auras/' almacenará las imágenes

    def __str__(self):
        return f'Nombre: {self.nombre} Puntos de Autoridad: {self.puntos_de_autoridad}'