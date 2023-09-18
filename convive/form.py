from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from general.models import *
from django import forms


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('carnet','semestre')
