from django.shortcuts import render
from .models import Materia
# Create your views here.
def inicio_vista(requese):
    lasmateria=Materia.objects.all()
    return render(requese,"gestionarMateria.html")