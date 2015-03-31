# encoding:utf-8
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView
from django.shortcuts import render_to_response, render, get_object_or_404
from django.shortcuts import render_to_response, render, redirect
from cotizacion.models import Cotizacion, CotizacionItem
from ActividadesClinicas.models import Odontograma
from procesocoopago.models import Pago, PagoAplicado
from procesocoopago.forms import PagoForm, PagoAplicadoForm,PagoAplicadoFormset
from django.core.urlresolvers import reverse
import datetime

def pagos(request , cotizacion_id):
    
    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    items = cotizacion.cotizacionitem_set.filter(status__in=['aceptado'])
    initial = []
    for item in items:
        initial.append({
            'importe':0,
            'cotizacion_item':item
            })
        
    pa_formset = None
    if request.method == "POST":
        modelform = PagoForm(request.POST)
        pa_formset = PagoAplicadoFormset(request.POST, initial=initial)
       
        if modelform.is_valid():
            pago=modelform.save()

            for form in pa_formset:
                if form.is_valid():
                    form.save(pago)
    else:
        modelform = PagoForm()
        pa_formset = PagoAplicadoFormset(initial=initial)

    items = [form.item for form in pa_formset]

    return render(request, "pago.html", {
                        'form': modelform,
                        'pa_formset': pa_formset,
                        'items': items
                    })



def aplicarpagoitem(request):
    pago = Pago.objects.all()
    paciente = 'meh'

    if request.method == "POST":
        modelform = PagoAplicadoForm(request.post)
        if modelform.is_valid():
            modelform.save()
            return redirect("/pago/process/")
    else:
        modelform = PagoAplicadoForm()
    return render(request, 'proceso.html',
                  {'form': modelform,
                   'pago': pago,
                   'paciente': paciente})






        













