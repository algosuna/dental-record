from datetime import datetime
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, render, get_object_or_404
from django.views.generic import UpdateView, ListView, CreateView, DetailView

from wkhtmltopdf.views import PDFTemplateView
from core.mixins import PermissionRequiredMixin
from core.utils import generic_search
from core.views import CreateObjFromContext

from consumidos.models import (
    PaqueteConsumido, PaqueteConsumidoItem, Paquete, ProductoConsumido,
    CancelSalida
)
from consumidos.forms import (
    PaqueteForm, AtenderPaqueteForm, PCItemForm, PeticionForm,
    ProductoConsumidoForm, SalidaCanceladaForm
)
from servicios.models import Servicio


class Paquetes(ListView):
    model = Paquete
    context_object_name = 'paquetes'
    template_name = 'paquetes.html'

    def get_context_data(self, **kwargs):
        context = super(Paquetes, self).get_context_data(**kwargs)
        context.update({'ps_active': 'active'})
        return context


class PaqueteCreate(CreateView):
    form_class = PaqueteForm
    template_name = 'paquete.html'

    def get_success_url(self):
        return reverse('consumidos:armar', kwargs=self.kwargs)

    def get_context_data(self, **kwargs):
        context = super(PaqueteCreate, self).get_context_data(**kwargs)
        context.update({'pn_active': 'active'})
        return context


class Peticiones(ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status="en_espera")
    form_class = PeticionForm
    context_object_name = 'peticiones'
    template_name = 'peticiones.html'

    def get_context_data(self, **kwargs):
        context = super(Peticiones, self).get_context_data(**kwargs)
        context.update({'pe_active': 'active'})
        return context


class PeticionCreate(CreateObjFromContext):
    form_class = PeticionForm
    template_name = 'peticion.html'
    ctx_model = Servicio
    initial_value = 'servicio'

    def get_initial(self):
        initial = super(PeticionCreate, self).get_initial()
        initial = initial.copy()
        odontograma = self.get_obj().paquete.odontograma
        initial.update({
            'medico': odontograma.medico,
            'paciente': odontograma.paciente
            })
        return initial

    def get_context_data(self, **kwargs):
        context = super(PeticionCreate, self).get_context_data(**kwargs)
        context.update({
            'paciente': self.get_initial()['paciente'],
            'p_active': 'active'
            })
        return context

    def get_success_url(self):
        url = reverse('clinica:paciente_detail',
                      kwargs={'pk': self.get_initial()['paciente'].pk})
        return url


class PeticionUpdate(UpdateView):
    model = PaqueteConsumido
    template_name = 'peticion-update.html'
    form_class = AtenderPaqueteForm
    context_object_name = 'pconsumido'

    def get_context_data(self, **kwargs):
        context = super(PeticionUpdate, self).get_context_data(**kwargs)
        context.update({'pe_active': 'active'})
        return context

    def get_success_url(self):
        return reverse('consumidos:paquete_item_create', kwargs=self.kwargs)


class PeticionesAtendidas(ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status="surtido")
    context_object_name = 'consumidos'
    template_name = 'peticiones-atendidas.html'

    def get_context_data(self, **kwargs):
        context = super(PeticionesAtendidas, self).get_context_data(**kwargs)
        context.update({'psl_active': 'active'})
        return context


def paquete_item_create(request, pk):
    paquete_consumido = get_object_or_404(PaqueteConsumido, pk=pk)
    items = paquete_consumido.paqueteconsumidoitem_set.all()
    initial_list = []

    if not items.exists():
        initial_list = paquete_consumido.get_item_initials()

    if request.method == 'POST':
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=0)
        formset = ItemFormset(request.POST)

        if formset.is_valid():
            for form in formset:
                form.save(paquete_consumido)
    else:
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=len(initial_list))
        formset = ItemFormset(queryset=items, initial=initial_list)

    return render(request, 'paquete-items.html', {
        'formset': formset,
        'paquete': paquete_consumido,
        'paciente': paquete_consumido.paciente,
        'pe_active': 'active'
        })


class EditPaqueteView(UpdateView):
    model = PaqueteConsumidoItem
    succes_url = '/'
    template_name = 'packDetail.html'
    form_class = PaqueteConsumidoItem


class producto_consumido(CreateView):
    form_class = ProductoConsumidoForm
    template_name = 'prconsumido.html'
    context_object_name = 'prconsumido'
    success_url = '/'


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


class SalidaCancelledList(PermissionRequiredMixin, ListView):
    model = CancelSalida
    queryset = model.objects.filter()
    context_object_name = 'salidas'
    template_name = 'salida-cancel.html'
    permission_required = 'consumidos.add_cancelsalida'

    def get_context_data(self, **kwargs):
        context = super(SalidaCancelledList, self).get_context_data(**kwargs)
        cancelled = CancelSalida.objects.all()
        context.update({'cancelsalida': cancelled, 'cs_active': 'active'})
        return context


class SalidaCancel(PermissionRequiredMixin, CreateObjFromContext):
    form_class = SalidaCanceladaForm
    ctx_model = CancelSalida
    template_name = 'salida-cancel.html'
    success_url = reverse_lazy('consumidos:entradas_canceladas')
    permission_required = 'consumidos.add_cancelsalida'
    initial_value = 'salida'

    def get_context_data(self, **kwargs):
        context = super(SalidaCancel, self).get_context_data(**kwargs)
        context.update({'s_active': 'active'})
        return context


class EntradaCancelDetail(PermissionRequiredMixin, DetailView):
    model = CancelSalida
    template_name = 'salidacancel-detail.html'
    permission_required = 'consumidos.add_cancelsalida'
    context_object_name = 'cancelsalida'

    def get_context_data(self, **kwargs):
        context = super(EntradaCancelDetail, self).get_context_data(**kwargs)
        salida = self.object.salida
        context.update({'salida': salida, 'sc_active': 'active'})
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
