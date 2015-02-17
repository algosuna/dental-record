# Create your views here.
rom django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from .forms import ProductoForm
from django.shortcuts import render_to_response, render, redirect
import datetime
from paquete.models import Paquete
from paquete.models import ContenidoPaquete





def paquete(request):
	if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/paquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "paquete.html", {"form": modelform})