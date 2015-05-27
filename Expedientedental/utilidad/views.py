from decimal import Decimal

from django.contrib.auth.decorators import login_required
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
        'search_string': request.GET.get(query, '')
        })


''' Specs:
Tomar el precio por servicio, o el costo que se le cobro al paciente
se suma:
- el precio de productos
'''


class ServiciosPaciente(LoginRequiredMixin, DetailView):
    ''' Lista de servicios de paciente. '''
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'utilidad-servicios.html'

    def get_context_data(self, **kwargs):
        context = super(ServiciosPaciente, self).get_context_data(**kwargs)
        consumidos = PaqueteConsumido.objects.filter(paciente=self.object)
        servicios = []

        for c in consumidos:
            servicio = c.servicio
            servicios.append(servicio)

        context.update({'servicios': servicios})
        return context


class UtilidadServicio(LoginRequiredMixin, DetailView):
    ''' Detalle de precio de servicio y costo de productos. '''
    ''' TODO: create manager for PaqueteConsumidoItem to sum the prices. '''
    model = Servicio
    context_object_name = 'servicio'
    template_name = 'utilidad-servicio.html'

    def get_context_data(self, **kwargs):
        context = super(UtilidadServicio, self).get_context_data(**kwargs)
        consumidos = PaqueteConsumido.objects.filter(servicio=self.object)
        paciente = consumidos[0].paciente
        consumido_items = []
        costo_total = 0

        for c in consumidos:
            ''' Gathers PaqueteConsumido's PaqueteConsumidoItems. '''
            items = c.paqueteconsumidoitem_set.all()

            # TODO: Fix this (esta' a lo cholo) after creating manager
            for item in items:
                ''' For item in PaqueteConsumidoItems it adds the price. '''
                costo_total = item.aggregate(Decimal(item.precio))

            consumido_items.append(items)

        diff = self.object.precio - costo_total

        context.update({
            'paciente': paciente,
            'consumidos': consumidos,
            'consumido_items': consumido_items,
            'costo_total': costo_total,
            'diff': diff
            })
        return context

        # TODO: Commit my changes and update consumidos model so I can do some
        # tests and then discard those changes!
