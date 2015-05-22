from datetime import datetime
from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.models import modelformset_factory
from django.shortcuts import (
    render_to_response, render, redirect, get_object_or_404)
from django.views.generic import UpdateView, ListView, CreateView, DetailView
from wkhtmltopdf.views import PDFTemplateView


from core.utils import generic_search


from servicios.models import Servicio
from consumidos.models import (
    PaqueteConsumido, PaqueteConsumidoItem, Paquete, ProductoConsumido)
from consumidos.forms import (
    PaqueteForm, AtenderPaqueteForm, PCItemForm, PeticionForm,
    ProductoConsumidoForm)


class PaqueteItem(CreateView):
    form_class = PaqueteForm
    template_name = 'crear_paquete.html'

    def get_succes_url(self):
        return reverse('consumidos:armar', kwargs=self.kwargs)


class Paquetes(ListView):
    model = Paquete
    context_object_name = 'paquetes'
    template_name = 'paquetes.html'


class AtencionPaquete(UpdateView):
    model = PaqueteConsumido
    template_name = 'atencion_paquete.html'
    form_class = AtenderPaqueteForm
    context_object_name = 'pconsumido'

    def get_success_url(self):
        return reverse('consumidos:insumos', kwargs=self.kwargs)


def manage_paquetes(request, pk):
    paquete_consumido = get_object_or_404(PaqueteConsumido, pk=pk)
    # print paquete_consumido
    items = paquete_consumido.paqueteconsumidoitem_set.all()
    # print items

    # initial list para items predeterminados
    initial_list = []
    if not items.exists():
        initial_list = paquete_consumido.get_item_initials()
        # for item in items:
            # initial_list = item.get_item_initials()
    # agregamos initial para un formulario vacio
            # initial_list.append({'paquete_consumidoitem': paquete_consumido,
            #                      'items': items})
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
        # print 'len', len(initial_list)
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=len(initial_list))
        formset = ItemFormset(queryset=items, initial=initial_list)
    context = {
        'formset': formset,
        'paquete': paquete_consumido
    }
    print formset.empty_form
    return render(request, 'paquete_def.html', context)


class Suplied(ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status="surtido")
    context_object_name = 'consumidos'
    template_name = 'entregados.html'


class EditPaqueteView(UpdateView):
    model = PaqueteConsumidoItem
    succes_url = '/'
    template_name = 'packDetail.html'
    form_class = PaqueteConsumidoItem

    def get_succes_url(self):
        return '/'


class PeticionView(CreateView):
    form_class = PeticionForm
    template_name = 'peticion.html'
    servicio = None
    paciente = None

    def get_paciente(self):
        if self.paciente is None:
            self.paciente = self.get_servicio().paquete.odontograma.paciente
        return self.paciente

    def get_form_kwargs(self):
        kwargs = super(PeticionView, self).get_form_kwargs()
        servicio = self.get_servicio()
        odontograma = servicio.paquete.odontograma
        kwargs.update({
            'medico': odontograma.medico,
            'paciente': odontograma.paciente,
            'servicio': servicio,
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

    # def get_succes_url(self):
    #     paciente = self.get_servicio().odontograma.paciente
    #     return reverse('consumidos:pconsumido', kwargs=[paciente])

    def get_success_url(self):
        url = reverse('clinica:paciente_detail',
                      kwargs={'pk': self.get_paciente().pk})
        return url


class peticionesView(ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status="en_espera")
    form_class = PeticionForm
    context_object_name = 'peticiones'
    template_name = 'peticiones.html'


class producto_consumido(CreateView):
    form_class = ProductoConsumidoForm
    template_name = 'prconsumido.html'
    context_object_name = 'prconsumido'

    def get_succes_url(self):
        return '/'


class Consumidos(ListView):
    model = ProductoConsumido
    context_object_name = 'consumidos'
    template_name = 'pconsumido.html'


class ConsumidoDetail(DetailView):
    model = ProductoConsumido
    context_object_name = 'consumido'
    template_name = 'consumido-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ConsumidoDetail, self).get_context_data(**kwargs)
        producto = self.object.producto
        context.update({'cd_active': 'active', 'producto': producto})
        return context


class SalidaPDF(PDFTemplateView):
    filename = 'salida.pdf'
    template_name = 'printit_salida.html'

    def get_context_data(self, **kwargs):
        context = super(SalidaPDF, self).get_context_data(**kwargs)
        producto = get_object_or_404(ProductoConsumido)
        context['producto'] = producto
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context


class PaquetebillPDF(PDFTemplateView):
    filename = 'recibo_de_entrega.pdf'
    template_name = 'materiales_salida.html'

    def get_context_data(self, **kwargs):
        context = super(PaquetebillPDF, self).get_context_data(**kwargs)
        pc = PaqueteConsumido.objects.get(pk=self.kwargs.get('pk'))
        items = pc.paqueteconsumidoitem_set.all()
        fecha = datetime.now().strftime("%d/%m/%Y")
        hora = datetime.now().strftime("%I:%M %p")
        context.update({
            'pc': pc, 'items': items,
            'fecha': fecha, 'hora': hora
        })
        return context


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
