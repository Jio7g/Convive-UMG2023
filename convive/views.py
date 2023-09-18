from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse
from general.models import *
from .form import *

@login_required
def index(request):
    if (request.user.is_staff!=True and request.user.email[-12:]!="miumg.edu.gt"):
        request.user.delete()
        return render(request, "login.html")
    try:
        if(request.user.perfil is None and request.user.is_staff==False):
            return redirect(reverse('registar'))    
    except:
        if(request.user.is_staff==False):
            return redirect(reverse('registar'))   
    evento = Evento.objects.get(estado=True)
    actividades = Actividad.objects.filter(evento=evento).order_by('fecha')
    return render(request, 'index.html',{'evento':evento,'actividades':actividades})


def Login(request):
    if request.method == "GET":
        return render(request, "login.html")


def registrar_perfil(request):
    if request.method == 'POST':
        perfil_form = PerfilForm(request.POST)
        if perfil_form.is_valid():
            form = perfil_form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect(reverse('index'))
    else:
        return render(request, "user/edit.html")           
