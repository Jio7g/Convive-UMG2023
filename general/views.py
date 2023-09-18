from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import *
from django.urls import reverse
import string
import random

@login_required
def ViewActividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    mensaje = ""
    if request.method == 'POST':
        cod = request.POST.get("codigo", "")
        try:
            asistencia = Asistencia.objects.get(codigo=cod, actividad=actividad)
            if(asistencia.estudiante is None):
                asistencia.estudiante = request.user.perfil
                asistencia.save()
                mensaje = "Registro exitoso"
            else:
                mensaje = "Codigo ya a sido utilizado"
        except:
            mensaje = "Codigo no valido"
       
    if(request.user.is_staff):
        a=random.choice(string.ascii_letters)
        b=random.choice(string.ascii_letters)
        c=random.choice(string.ascii_letters)
        asistencia = Asistencia.objects.create(actividad=actividad,docente=request.user)
        codigo = str(asistencia.id)+a+b+c
        asistencia.codigo = codigo
        asistencia.save()
    else:
        try:
            asistencia = Asistencia.objects.get(estudiante=request.user.perfil,actividad=actividad)
            codigo = asistencia.codigo
        except:
            codigo = "Sin asistencia"
            asistencia = None
    return render(request, 'actividad/view.html', {'actividad': actividad,'codigo':codigo,'asistencia':asistencia,'mensaje':mensaje})
