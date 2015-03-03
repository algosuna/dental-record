#encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect

from procesocoopago.models import Abono,Pago,procesoPago
from procesocoopago.forms import AbonoForm,PagoForm,procesoPagoForm
import datetime

def Abono(request):
    if request.method == "POST":
        modelform = AbonoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/abono/")
    else:
        modelform = AbonoForm()
    return render(request, "abono.html", {"form": modelform})


def Pago(request):
    if request.method == "POST":
        modelform = PagoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/pago/")
    else:
        modelform = PagoForm()
    return render(request, "pago.html", {"form": modelform})


def Proceso(request):
    if request.method == "POST":
        modelform = procesoPagoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/proceso/")
    else:
        modelform = procesoPagoForm()
    return render(request, "proceso.html", {"form": modelform})



