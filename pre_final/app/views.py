from re import template
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import riesgoso, inofensivo, potencial_riesgo


def principal(request):
    return render(request,"inicio.html")

def riesgose(request):
    pacientes_riesgosos = riesgoso.objects.all()
    return render(request, "riesgosos.html", {"pacientes_R": pacientes_riesgosos})


def potenciales(request):
    pacientes_potenciales = potencial_riesgo.objects.all()
    return render(request, "riesgo_potencial.html", {"pacientes_RP": pacientes_potenciales})
    
def inofensivos(request):
    pacientes_inofensivos = inofensivo.objects.all()
    return render(request, "inofensivos.html", {"pacientes_i": pacientes_inofensivos})

def buscar(request):
    #mensaje="Paciente buscado: %r" %request.GET["buscador"]
    
    if request.GET["buscador"]:

        pac=request.GET["buscador"]

        paci=riesgoso.objects.filter(nombre__icontains=pac)

        return render(request, "resultado_busqueda.html", {"paci":paci, "query":pac})
    
    else:

        mensaje=""


    return HttpResponse(mensaje)
