from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from estudiatnes.models import *
from general.models import *
# Create your views here.
@login_required
def docentes(request):
    request.user.is_staff=True
    request.user.save()
    return redirect(reverse('index'))

@login_required
def reporte(request, semestre):
    if(request.user.is_staff==False):
        return redirect(reverse('index'))
    estudiantes = Perfil.objects.filter(semestre=int(semestre))
    evento = Evento.objects.get(estado=True)
    actividades=Actividad.objects.filter(evento=evento)
    for i in estudiantes:
        i.asistencias = Asistencia.objects.filter(estudiante=i,actividad__evento=evento)
        i.asis = i.asistencias.count()
    
    for i in estudiantes:
        i.actividades = []
        for x in actividades:
            centinela = True
            for z in i.asistencias:
                if(x.id == z.actividad.id):
                    i.actividades.append("check")
                    centinela = False
                    break
            if(centinela):
                i.actividades.append("clear")
                    
    return render(request, 'reporte.html', {'estudiantes':estudiantes,'actividades':actividades,'semestre':semestre})

@login_required
def semestres(request):
    return render(request,'semestres.html')