# encoding:utf-8
from django.shortcuts import render, get_object_or_404,\
    redirect

from cotizacion.models import Cotizacion
from procesocoopago.models import Pago
from procesocoopago.forms import PagoForm, PagoAplicadoForm, PagoAplicadoFormset


def pagos(request, cotizacion_id):

    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    total = cotizacion.total()
    items = cotizacion.cotizacionitem_set.filter(status__in=['aceptado'])
    initial = []

    for item in items:
        initial.append({
            'importe': 0,
            'cotizacion_item': item
            })

    pa_formset = None

    if request.method == "POST":
        modelform = PagoForm(request.POST)
        pa_formset = PagoAplicadoFormset(request.POST, initial=initial)

        if modelform.is_valid():
            pago = modelform.save()

            for form in pa_formset:
                if form.is_valid():
                    form.save(pago)
    else:
        modelform = PagoForm(initial={'monto': cotizacion.total()})
        pa_formset = PagoAplicadoFormset(initial=initial)

    items = [form.item for form in pa_formset]

    return render(request, "pago.html", {
                  'form': modelform,
                  'pa_formset': pa_formset,
                  'items': items,
                  'total': total,
                  'cotizacion': cotizacion
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
