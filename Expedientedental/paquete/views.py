# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect

from .forms import PaqueteForm, EntryPaqueteForm
from paquete.models import Paquete, EntryPaquete

import datetime


def paquete(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/paquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "paquete.html", {"form": modelform})


def tipoPaquete(request):
    if request.method == "POST":
        modelform = EntryPaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = EntryPaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})