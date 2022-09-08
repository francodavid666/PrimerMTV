from re import template
from django.shortcuts import render
from .models import familiar_1
from django.http import HttpResponse
from django.template import Context, Template

# Create your views here.

def fami (request):
    
    gisel = familiar_1(nombre = "GISEL", apellido = "GOMEZ", edad = 41)
    damian = familiar_1(nombre = "DAMIAN", apellido = "GOMEZ", edad = 37)
    ricardo = familiar_1(nombre = "RICARDO", apellido = "GOMEZ", edad = 70)
    
    gisel.save()
    damian.save()
    ricardo.save()
    
    texto = f"Mi familiar se llama {gisel.nombre} su apellido es {gisel.apellido} y tiene {gisel.edad} anios"
    texto_2 = f"Mi familiar se llama {damian.nombre} su apellido es {damian.apellido} y tiene {damian.edad} anios"
    

    diccionario = {"nombre": gisel.nombre,"apellido":gisel.apellido,"edad":gisel.edad,"fecha":gisel.fecha,
                   "nombre_damian": damian.nombre,"apellido_damian":damian.apellido,"edad_damian":damian.edad,
                   "nombre_ricardo": ricardo.nombre,"apellido_ricardo":ricardo.apellido,"edad_ricardo":ricardo.edad
                   }
   
    
    
    mihtml = open("C:/Users/david/OneDrive/Escritorio/PrimerMTV/ProyectoFami/templates/templade1.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    
    contexto = Context(diccionario)
    documento = plantilla.render(contexto)
    return HttpResponse(documento)
