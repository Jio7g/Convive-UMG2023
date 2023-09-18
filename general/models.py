from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User,unique=True, null=True, db_index=True, on_delete=models.CASCADE)
    carnet = models.CharField(max_length=15, blank=False)
    semestre = models.IntegerField(null=True)
    def __str__(self):
        return self.user.username

class Evento(models.Model):
    ano = models.IntegerField(null=True)
    estado = models.BooleanField(default=True)    
    nombre = models.CharField(max_length=150, blank=False)
    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE,null=True)
    nombre = models.CharField(max_length=150, blank=False)
    fecha = models.DateField(null = True)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Asistencia(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE,null=True)
    docente = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    estudiante = models.ForeignKey(Perfil, on_delete=models.CASCADE,null=True)
    codigo = models.CharField(max_length=10, null=True, unique=True)
    def __str__(self):
        return self.actividad.nombre
    
    