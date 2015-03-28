# encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import render_to_response, render, get_object_or_404
from django.shortcuts import render_to_response, render, redirect
from cotizacion.models import Cotizacion,CotizacionItem
from ActividadesClinicas.models import Odontograma
from procesocoopago.models import Pago,PagoAplicado
from procesocoopago.forms import PagoForm,PagoAplicadoForm
from django.core.urlresolvers import reverse
import datetime

def pagos(request):
        orders = Odontograma.objects.all()
        return render_to_response('/pago.html',
        {'orders': orders})
        

def aplicarpago(request):
    if request.method=='POST':
        modelform =PagoAplicadoForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('pago/process/')
    else:
        modelform = PagoAplicadoForm()
    return render(request, "proceso.html", {"form": modelform})





        













