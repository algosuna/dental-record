#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from .forms import CategoriaProdForm
from .forms import ProductoForm
from .forms import TipoPaqueteForm
from .forms import PaqueteForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from Inventario.models import categoriaProducto
from Inventario.models import producto
from Inventario.models import tipoPaquete
from Inventario.models import paquete

def categoriaProducto(request):
	if request.method == "POST":
		modelform = CategoriaProdForm(request.POST)
		if modelform.is_valid():
			modelform.save()
			return redirect("/categoriaProd/")
	else:
		modelform=CategoriaProdForm()
	return render(request,"categoriaProd.html",{"form":modelform})

def producto(request):
    if request.method == "POST":
        modelform = ProductoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/producto/")
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})


def tipoPaquete(request):
    if request.method == "POST":
        modelform = TipoPaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = TipoPaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})


def paquete(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/paquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "paquete.html", {"form": modelform})

