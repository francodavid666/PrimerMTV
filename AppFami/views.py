from re import template
from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Context, Template,loader

# Create your views here.

def fami (request):
    
    gisel = Familiar(nombre = "GISEL", apellido = "GOMEZ", edad = 41, fecha_nacimiento= "1990-07-20")
    damian = Familiar(nombre = "DAMIAN", apellido = "GOMEZ", edad = 37, fecha_nacimiento= "1984-04-29")
    ricardo = Familiar(nombre = "RICARDO", apellido = "GOMEZ", edad = 70,  fecha_nacimiento= "1960-05-24")
    
    gisel.save()
    damian.save()
    ricardo.save()
    
    familiares = [gisel,damian,ricardo]
    
    plantilla = loader.get_template("templade1.html")
    contexto = {"familiares":familiares}
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
    
    
    
    