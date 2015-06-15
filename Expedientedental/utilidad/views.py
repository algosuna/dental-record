from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from core.utils import generic_search
from core.mixins import LoginRequiredMixin
from core.views import DetailListView

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


class ServiciosPaciente(LoginRequiredMixin, DetailListView):
    ''' Lista de servicios de paciente. '''
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'utilidad-servicios.html'
    list_model = Servicio
    list_queryset = list_model.objects.filter(status__in=['parcial', 'pagado'])
    list_paginate_by = 20
    list_context_name = 'servicios'

    def get_context_data(self, **kwargs):
        context = super(ServiciosPaciente, self).get_context_data(**kwargs)
        servicios = self.get_list_queryset()
        consumidos = PaqueteConsumido.objects.filter(
            paciente=self.object, status='surtido')
        costo_total = 0

        for c in consumidos:
            c_total = c.precio_total()
            costo_total += c_total

        diff = servicios.total_pagado() - costo_total

        context.update({
            'global_servicios': servicios,
            'costo_total': costo_total,
            'diff': diff,
            'us_active': 'active'})
        return context


class UtilidadServicio(LoginRequiredMixin, DetailView):
    ''' Detalle de precio de servicio y costo de productos. '''
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
            c_total = c.precio_total()
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
