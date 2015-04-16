# encoding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from altas.models import Paciente
from core.utils import generic_search
from cotizacion.models import Cotizacion
from pagos.models import Pago
from pagos.forms import PagoForm, PagoAplicadoFormset


def pagos(request, cotizacion_id):

    cotizacion = get_object_or_404(Cotizacion, pk=cotizacion_id)
    total = cotizacion.total_aceptado()
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

                # TODO: simplificar esta condicion. ver si mover a forms.py
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
        modelform = PagoForm(initial={'monto': cotizacion.total_adeudado()})
        pa_formset = PagoAplicadoFormset(initial=initial)

    items = [form.item for form in pa_formset]

    return render(request, 'pago.html', {
                  'form': modelform,
                  'pa_formset': pa_formset,
                  'items': items,
                  'total': total,
                  'cotizacion': cotizacion
                  })


def pagos_list(request):
    pagos = Pago.objects.all()
    query = 'q'

    MODEL_MAP = {
        Paciente: [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'credencialPaciente'
        ],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, 'pago-list.html', {
                  'pagos': pagos,
                  'objects': objects,
                  'search_string': request.GET.get(query, '')
                  })


def paciente_search(request):
    '''
    Lista de pacientes con pagos pendientes.
    '''
    query = 'q'

    MODEL_MAP = {
        Paciente: [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'credencialPaciente'
        ],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, 'paciente-search.html', {
                  'objects': objects,
                  'search_string': request.GET.get(query, '')
                  })


def pagos_paciente(request, paciente_id):
    '''
    Lista de pagos por paciente.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    pagos = paciente.pago_set.all()

    return render(request, 'pago-paciente.html', {
                  'paciente': paciente,
                  'pagos': pagos
                  })


def pagos_pending(request, paciente_id):
    '''
    Lista de pagos pendientes agrupados por cotizacion.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    cotizaciones = Cotizacion.objects.filter(odontograma__paciente=paciente)
    # Quitamos cotizaciones que no tengan items que cobrar (total = 0)
    cotizaciones = [c for c in cotizaciones if c.total() != 0]

    return render(request, 'pago-pending.html', {
                  'paciente': paciente,
                  'cotizaciones': cotizaciones,
                  })


def pagos_detail(request, pago_id):
    '''
    Resumen de pago.
    '''
    pago = get_object_or_404(Pago, pk=pago_id)

    return render(request, 'pago-detail.html', {'pago': pago})
