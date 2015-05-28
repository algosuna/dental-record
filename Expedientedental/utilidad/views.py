# from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import DetailView

from core.utils import generic_search
from core.mixins import LoginRequiredMixin

from altas.models import Paciente
from consumidos.models import PaqueteConsumido
from servicios.models import Servicio


@login_required
def paciente_search(request):
    query = 'q'
    MODEL_MAP = {
        Paciente: [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'credencialPaciente'
        ]
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, 'utilidad-search.html', {
        'objects': objects,
        'search_string': request.GET.get(query, ''),
        'us_active': 'active'
        })


class ServiciosPaciente(LoginRequiredMixin, DetailView):
    ''' Lista de servicios de paciente. '''
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'utilidad-servicios.html'

    def get_context_data(self, **kwargs):
        context = super(ServiciosPaciente, self).get_context_data(**kwargs)
        servicios = Servicio.objects.filter(status__in=['parcial', 'pagado'])
        context.update({'servicios': servicios, 'us_active': 'active'})
        return context


class UtilidadServicio(LoginRequiredMixin, DetailView):
    ''' Detalle de precio de servicio y costo de productos. '''
    ''' TODO: create manager for PaqueteConsumidoItem to sum the prices. '''
    model = Servicio
    context_object_name = 'servicio'
    template_name = 'utilidad-servicio.html'

    def get_context_data(self, **kwargs):
        context = super(UtilidadServicio, self).get_context_data(**kwargs)
        paciente = self.object.paquete.odontograma.paciente
        consumidos = PaqueteConsumido.objects.filter(
            servicio=self.object, status='surtido')
        consumido_items = []
        costo_total = 0

        for c in consumidos:
            ''' Gathers PaqueteConsumido's PaqueteConsumidoItems. '''
            items = c.paqueteconsumidoitem_set.all()
            # TODO: Fix this (esta' a lo cholo) after creating manager
            c_total = items.aggregate(Sum('precio'))['precio__sum']
            if c_total is None:
                c_total = 0
            costo_total += c_total
            consumido_items.extend(items)

        diff = self.object.precio - costo_total

        context.update({
            'paciente': paciente,
            'consumido_items': consumido_items,
            'costo_total': costo_total,
            'diff': diff,
            'us_active': 'active'
            })
        return context
