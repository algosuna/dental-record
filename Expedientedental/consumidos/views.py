from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.shortcuts import (
    render_to_response, render, redirect, get_object_or_404)
from django.views.generic import UpdateView, ListView, CreateView

from core.utils import generic_search


from servicios.models import Servicio
from consumidos.models import PaqueteConsumido, PaqueteConsumidoItem
from consumidos.forms import (
    PaqueteForm, PaqueteConsumidoForm, PCItemForm, PeticionForm,
    ProductoConsumidoForm)


def paquete_item(request):

    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})


class paquetec(CreateView):
    model = PaqueteConsumido
    succes_url = '/'
    template_name = 'salida_pack.html'
    form_class = PaqueteConsumidoForm
    context_object_name = 'pconsumido'

    def get_peticion(self):
        if self.peticion:
            return self.peticion

    def get_succes_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super(paquetec, self).get_context_data(**kwargs)
        context.update({'pconsumido': self.peticion()})
        return context


def manage_paquetes(request, pk):
    paquete_consumido = get_object_or_404(PaqueteConsumido, pk=pk)
    items = paquete_consumido.paqueteconsumidoitem_set.all()
    # initial list para items predeterminados
    initial_list = []
    if not items.exists():
        initial_list = paquete_consumido.get_item_initials()
    # agregamos initial para un formulario vacio
    # initial_list.append({'paquete_consumido': paquete_consumido})
    # Se usa empty form generada por formset
    if request.method == 'POST':
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=0)
        formset = ItemFormset(request.POST)

        if formset.is_valid():
            print "VALIDO"
            for form in formset:
                form.save(paquete_consumido)
        else:
            print "INVALIDO"
            print request.POST
            print formset.errors

    else:
        print 'len', len(initial_list)
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=len(initial_list))
        formset = ItemFormset(queryset=items, initial=initial_list)
    context = {
        'formset': formset,
        'paquete': paquete_consumido
    }
    return render(request, 'paquete_def.html', context)


class suplied(ListView):
    model = PaqueteConsumidoItem
    context_object_name = 'consumidos'
    template_name = 'delivered_pacages.html'


class EditPaqueteView(UpdateView):
    model = PaqueteConsumidoItem
    succes_url = '/'
    template_name = 'packDetail.html'
    form_class = PaqueteConsumidoItem

    def get_succes_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super(EditPaqueteView, self).get_context_data(**kwargs)
        context['action'] = reverse('paquete-edit',
                                    kwargs={'pk': self.object.id})
        return context


class peticionesView(ListView):
    model = PaqueteConsumido
    form_class = PeticionForm
    context_object_name = 'peticiones'
    template_name = 'peticiones.html'


class PeticionView(CreateView):
    form_class = PeticionForm
    template_name = 'peticion.html'
    success_url = '/peticiones/list/'
    servicio = None

    def get_form_kwargs(self):
        kwargs = super(PeticionView, self).get_form_kwargs()
        servicio = self.get_servicio()
        odontograma = servicio.paquete.odontograma
        kwargs.update({
            'medico': odontograma.medico,
            'paciente': odontograma.paciente,
            'servicio': servicio,  # TODO: cambiar a 'servicio'
            })
        return kwargs

    def get_servicio(self):
        if self.servicio:
            return self.servicio
        self.servicio = Servicio.objects.get(
            pk=self.kwargs.get('pk'))
        return self.servicio

    def get_context_data(self, **kwargs):
        context = super(PeticionView, self).get_context_data(**kwargs)
        context.update({'servicio': self.get_servicio()})
        return context

    def get_succes_url(self):
        paciente = self.get_servicio().odontograma.paciente
        return reverse('paciente_detail', args=[paciente])


class producto_consumido(CreateView):
    form_class = ProductoConsumidoForm
    template_name = 'prconsumido.html'
    succes_url = '/'


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        PaqueteConsumido: ['paquete__nombre', 'paquete__descripcion']
    }

    objects = []

    for model, fields in MODEL_MAP.items():
        objects += generic_search(request, model, fields, query)

    return render_to_response('paqueteedit.html', {'objects': objects,
                              'search_string': request.GET.get(query, ''), })
