#encoding:utf-8
import datetime

from django.shortcuts import render, redirect, render_to_response
from django.db.models import Q
from django.template import RequestContext

from ActividadesClinicas.forms import OdontogramaForm, HistoriaClinicaForm, ListadeDiagnosticosForm
from ActividadesClinicas.models import HistoriaClinica, Odontograma, ListadeDiagnosticos
from ActividadesClinicas.utils import generic_search

from altas.models import Paciente

def inicio(request):
    query = 'q'
    MODEL_MAP = {
        Paciente: ['nombre','apellidoPaterno','apellidoMaterno', 'id', ''],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects+=generic_search(request,model,fields,query)

    return render_to_response('inicio.html', {'objects':objects, 'search_string' : request.GET.get(query,''), } )

def HistoriaClinica(request):
    if request.method == "POST":
        modelform = HistoriaClinicaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/interrogatorio/")
    else:
        modelform=HistoriaClinicaForm()
    return render(request,"interrogatorio.html",{"form":modelform})

def odontograma(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(paciente__nombre__exact=query)
        )
        results = Odontograma.objects.filter(qset).distinct()
    else:
        results = []
    consulta = Odontograma.objects.all()
    if request.method == "POST":
        modelform = OdontogramaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/odontograma/")
    else:
        modelform = OdontogramaForm()
    return render(request, "odontograma.html", {"form": modelform,'datospaciente': consulta[0:],"results": results,
        "query": query})


def diagnosticos(request):
    if request.method == "POST":
        modelform = ListadeDiagnosticosForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/diagnosticos/")
    else:
        modelform = ListadeDiagnosticosForm()
    return render(request, "diagnosticos.html", {"form": modelform})

def datospaciente(request):
    consulta = Odontograma.objects.all()
    return render(request, 'prueba.html', {'datospaciente': consulta[0:]})

def buscarpaciente(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(nombre__contains=query)
        )
        results = Paciente.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, "evaluacion.html", {"results": results,"query": query})

def detallespaciente(request):
    consulta = Odontograma.objects.all()
    detalles = Paciente.objects.all()
    return render(request, 'detalles.html', {'detallespaciente': consulta[0:], 'detalles': detalles})