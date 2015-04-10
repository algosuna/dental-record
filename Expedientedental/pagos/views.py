# encoding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from cotizacion.models import Cotizacion
from pagos.models import Pago
from pagos.forms import PagoForm, PagoAplicadoFormset


def pagos_list(request):
    pagos = Pago.objects.all()

    return render(request, 'pago-list.html', {
                  'pagos': pagos
                  })


def pagos(request, cotizacion_id):

    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    total = cotizacion.total()
    items = cotizacion.cotizacionitem_set\
                      .filter(status__in=['aceptado', 'parcial'])
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

        if modelform.is_valid() and pa_formset.is_valid():
            pago = modelform.save()

            monto_aplicado = 0
            for form in pa_formset:
                form.instance.importe
                pago_aplicado = form.save(pago)
                monto_aplicado += pago_aplicado.importe

                # TODO: simplificar esta condicion
                if pago_aplicado.importe > 0:
                    item = pago_aplicado.cotizacion_item
                    total_aplicado = item.pagoaplicado_set.total_pagado()

                    if total_aplicado == item.precio:
                        item.status = 'pagado'

                    else:
                        item.status = 'parcial'

                    item.save()

            pago.aplicamonto(monto_aplicado)
            pago.save()

            return redirect(reverse('pagos_detail', args=[pago.id]))

    else:
        monto_total = cotizacion.total_adeudado()

        modelform = PagoForm(initial={'monto': monto_total})
        pa_formset = PagoAplicadoFormset(initial=initial)

    items = [form.item for form in pa_formset]

    return render(request, 'pago.html', {
                  'form': modelform,
                  'pa_formset': pa_formset,
                  'items': items,
                  'total': total,
                  'cotizacion': cotizacion
                  })


def pagos_detail(request, pago_id):
    pago = get_object_or_404(Pago, pk=pago_id)
    # TODO: arreglar este query feo
    # cotizacion = pago.paciente.odontograma_set.get().cotizacion_set.get()

    return render(request, 'pago-detail.html', {
                  'pago': pago,
                  # 'cotizacion': cotizacion
                  })
