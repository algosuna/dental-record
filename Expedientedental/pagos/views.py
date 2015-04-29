# encoding:utf-8
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime


from altas.models import Paciente
from core.utils import generic_search
from wkhtmltopdf.views import PDFTemplateView

from servicios.models import Paquete
from pagos.models import Pago
from pagos.forms import PagoForm, PagoAplicadoFormset


def pagos(request, paquete_id):

    paquete = get_object_or_404(Paquete, pk=paquete_id)
    total = paquete.total()
    servicios = paquete.servicio_set.filter(status__in=['aceptado', 'parcial'])
    paciente = paquete.odontograma.paciente
    initial = []

    for servicio in servicios:
        initial.append({
            'importe': 0,
            'servicio': servicio
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

                if pago_aplicado.importe > 0:
                    servicio = pago_aplicado.servicio
                    total_aplicado = servicio.pagoaplicado_set.total_pagado()

                    if total_aplicado == servicio.precio:
                        servicio.status = 'pagado'

                        servicio.procedimiento.status = 'autorizado'
                        servicio.procedimiento.save()

                    else:
                        servicio.status = 'parcial'

                    servicio.save()

            pago.aplicamonto(monto_aplicado)
            pago.save()

            return redirect(reverse('pagos:pagos_detail', args=[pago.id]))

    else:
        modelform = PagoForm(initial={
                             'monto': paquete.total_adeudado(),
                             'paciente': paciente
                             })
        pa_formset = PagoAplicadoFormset(initial=initial)

    servicios = [form.servicio for form in pa_formset]

    return render(request, 'pago.html', {
                  'form': modelform,
                  'pa_formset': pa_formset,
                  'servicios': servicios,
                  'total': total,
                  'paquete': paquete,
                  'r_active': 'active'
                  })


def pagos_list(request):
    pagos = Pago.objects.order_by('-fecha')
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
                  'search_string': request.GET.get(query, ''),
                  'r_active': 'active'
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

    return render(request, 'pago-paciente-search.html', {
                  'objects': objects,
                  'search_string': request.GET.get(query, ''),
                  'rp_active': 'active'
                  })


def pagos_paciente(request, paciente_id):
    '''
    Lista de pagos por paciente.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    pagos = paciente.pago_set.all()

    return render(request, 'pago-paciente.html', {
                  'paciente': paciente,
                  'pagos': pagos,
                  'r_active': 'active'
                  })


def pagos_pending(request, paciente_id):
    '''
    Lista de pagos pendientes agrupados por cotizacion.
    '''
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paquetes = Paquete.objects.filter(odontograma__paciente=paciente)
    # Quitamos paquetes que no tengan items que cobrar (total = 0)
    paquetes = [
        p for p in paquetes if p.total() != 0 and p.total_adeudado() != 0
    ]

    return render(request, 'pago-pending.html', {
                  'paciente': paciente,
                  'paquetes': paquetes,
                  'rp_active': 'active'
                  })


def pagos_detail(request, pago_id):
    '''
    Resumen de pago.
    '''
    pago = get_object_or_404(Pago, pk=pago_id)
    paciente = pago.paciente

    return render(request, 'pago-detail.html', {
                  'pago': pago,
                  'paciente': paciente,
                  'r_active': 'active'
                  })


class RecibodePagoPDF(PDFTemplateView):
    filename = 'recibo.pdf'
    template_name = 'recibo_pago.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(RecibodePagoPDF, self).get_context_data(**kwargs)
        self.pago_id = int(kwargs.get('pago_id'))
        pago = get_object_or_404(Pago, pk=self.pago_id)
        context['pago'] = pago
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
