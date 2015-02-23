#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from .forms import ProductoForm 
from .forms import CategoriaForm
from Inventario.models import Categoria 
from Inventario.models import Producto
import datetime

def categoria(request):
    if request.method == "POST":
        modelform = CategoriaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/categorias/")
    else:
        modelform = CategoriaForm()
    return render(request, "categoriaProd.html", {"form": modelform})



def producto(request):
    if request.method == "POST":
        modelform = ProductoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/producto/")
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})

