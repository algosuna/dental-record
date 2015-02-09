#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from .forms import OdontogramaForm
from .forms import InterrogatorioForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from ActividadesClinicas.models import Interrogatorio
from ActividadesClinicas.models import Odontograma

def interrogatorio(request):
	if request.method == "POST":
		modelform = InterrogatorioForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/interrogatorio/")
	else:
		modelform=InterrogatorioForm()
	return render(request,"interrogatorio.html",{"form":modelform})

def odontograma(request):
    if request.method == "POST":
        modelform = OdontogramaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/odontograma/")
    else:
        modelform = OdontogramaForm()
    return render(request, "odontograma.html", {"form": modelform})