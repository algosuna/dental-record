#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from .forms import OdontogramaForm
from .forms import InterrogatorioDentalForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from ActividadesClinicas.models import Interrogatorio
from ActividadesClinicas.models import ListadeDiagnositico
from ActividadesClinicas.models import Odontograma


def Interrogatorio (request):
	if request.method == "POST"
		modelform=InterrogatorioDentalForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("Odontograma")
    else:
    	modelform=InterrogatorioDentalForm()
    return render(request,"Interrogatorio.html"{"form":modelform})


def  Odontograma(request):
	if request.method == "POST"
		modelform=OdontogramaForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/Odontograma/")
	else:
		modelform=OdontogramaForm()
	return render(request,"Odontograma.html",{"form"}:modelform})