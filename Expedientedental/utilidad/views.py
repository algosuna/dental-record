''' Specs:
Tomar el precio por servicio, o el costo que se le cobro al paciente
se suma:
- el precio de productos
'''
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from core.utils import generic_search
from core.mixins import LoginRequiredMixin

from altas.models import Paciente
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


class ServiciosPaciente(LoginRequiredMixin, DetailView):
    ''' Lista de servicios de paciente. '''
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'utilidad-servicios.html'

    def get_context_data(self, **kwargs):
        context = super(ServiciosPaciente, self).get_context_data(**kwargs)
        context.update({})
        return context


class UtilidadServicio(LoginRequiredMixin, DetailView):
    ''' Detalle de precio de servicio y costo de productos. '''
    model = Servicio
    context_object_name = 'servicio'
    template_name = 'utilidad-servicio.html'

    def get_context_data(self, **kwargs):
        context = super(UtilidadServicio, self).get_context_data(**kwargs)
        context.update({})
        return context
