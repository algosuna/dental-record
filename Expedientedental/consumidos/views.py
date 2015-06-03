from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.forms.models import modelformset_factory
from django.shortcuts import (
    render_to_response, render, get_object_or_404, redirect
)
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
    PaqueteForm, AtenderPeticionForm, PaqueteItemCreateForm, PeticionForm,
    ProductoConsumidoForm, SalidaCanceladaForm
)
from servicios.models import Servicio


class Paquetes(PermissionRequiredMixin, ListView):
    model = Paquete
    context_object_name = 'paquetes'
    template_name = 'paquetes.html'
    permission_required = 'consumidos.add_paquete'

    def get_context_data(self, **kwargs):
        context = super(Paquetes, self).get_context_data(**kwargs)
        context.update({'ps_active': 'active'})
        return context


class PaqueteCreate(PermissionRequiredMixin, CreateView):
    ''' Creates Paquete object with PaqueteItems. The magic is in the form! '''
    form_class = PaqueteForm
    template_name = 'paquete.html'
    success_url = reverse_lazy('consumidos:paquete_list')
    permission_required = 'consumidos.add_paqueteitem'

    def get_context_data(self, **kwargs):
        context = super(PaqueteCreate, self).get_context_data(**kwargs)
        context.update({'pn_active': 'active'})
        return context


class PaqueteDetail(PermissionRequiredMixin, DetailView):
    model = Paquete
    context_object_name = 'paquete'
    template_name = 'paquete-detail.html'
    permission_required = 'consumidos.add_paquete'

    def get_context_data(self, **kwargs):
        context = super(PaqueteDetail, self).get_context_data(**kwargs)
        context.update({'ps_active': 'active'})
        return context


class PaqueteUpdate(PermissionRequiredMixin, UpdateView):
    ''' TODO: en la segunda iteracion. Requiere trabajo en la forma. '''
    form_class = PaqueteForm
    model = Paquete
    template_name = 'paquete.html'
    success_url = reverse_lazy('consumidos:paquete_list')
    permission_required = 'consumidos.change_paqueteitem'

    def get_context_data(self, **kwargs):
        context = super(PaqueteUpdate, self).get_context_data(**kwargs)
        context.update({'ps_active': 'active'})
        return context


class Peticiones(PermissionRequiredMixin, ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status='en_espera')
    context_object_name = 'paqueteenespera'
    template_name = 'peticiones.html'
    permission_required = 'consumidos.change_paqueteconsumido'

    def get_context_data(self, **kwargs):
        context = super(Peticiones, self).get_context_data(**kwargs)
        por_entregar = self.model.objects.filter(status='por_entregar')
        context.update({
            'pe_active': 'active',
            'paqueteporentregar': por_entregar
            })
        return context


class PeticionCreate(PermissionRequiredMixin, CreateObjFromContext):
    ''' Creates PaqueteConsumido with null Paquete from Servicio. '''
    form_class = PeticionForm
    template_name = 'peticion.html'
    ctx_model = Servicio
    initial_value = 'servicio'
    permission_required = 'consumidos.add_paqueteconsumido'

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


class PeticionUpdate(PermissionRequiredMixin, UpdateView):
    ''' Adds Paquete (and PaqueteItems) to PaqueteConsumido. '''
    form_class = AtenderPeticionForm
    model = PaqueteConsumido
    context_object_name = 'paqueteconsumido'
    template_name = 'peticion-update.html'
    permission_required = 'consumidos.change_paqueteconsumido'

    def get_context_data(self, **kwargs):
        context = super(PeticionUpdate, self).get_context_data(**kwargs)
        context.update({'pe_active': 'active'})
        return context

    def get_success_url(self):
        return reverse('consumidos:paquete_item_create', kwargs=self.kwargs)


class PeticionesAtendidas(PermissionRequiredMixin, ListView):
    model = PaqueteConsumido
    queryset = model.objects.filter(status="surtido")
    context_object_name = 'paqueteconsumidos'
    template_name = 'peticiones.html'
    permission_required = 'consumidos.change_paqueteconsumido'

    def get_context_data(self, **kwargs):
        context = super(PeticionesAtendidas, self).get_context_data(**kwargs)
        context.update({'psl_active': 'active'})
        return context


@permission_required('consumidos.add_paqueteconsumidoitem')
def paquete_item_create(request, pk):
    ''' Creates PaqueteConsumidoItems from PaqueteItems and adds or
    removes extra items (products). '''
    paquete_consumido = get_object_or_404(PaqueteConsumido, pk=pk)
    items = paquete_consumido.paqueteconsumidoitem_set.all()
    initial_list = []

    if not items.exists():
        initial_list = paquete_consumido.get_item_initials()

    if request.method == 'POST':
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PaqueteItemCreateForm,
                                           extra=0)
        formset = ItemFormset(request.POST)

        if formset.is_valid():
            for form in formset:
                form.save(paquete_consumido)

        return redirect(reverse(
            'consumidos:peticion_detail', args=[paquete_consumido.id]))
    else:
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PaqueteItemCreateForm,
                                           extra=len(initial_list))
        formset = ItemFormset(queryset=items, initial=initial_list)

    return render(request, 'paquete-items.html', {
        'formset': formset,
        'paquete': paquete_consumido,
        'paciente': paquete_consumido.paciente,
        'pe_active': 'active'
        })


class PeticionDetail(PermissionRequiredMixin, DetailView):
    ''' Detail of PaqueteConsumido with its items (PaqueteConsumidoItem) '''
    model = PaqueteConsumido
    template_name = 'peticion-detail.html'
    context_object_name = 'paquete'
    permission_required = 'consumidos.change_paqueteconsumido'

    def get_context_data(self, **kwargs):
        context = super(PeticionDetail, self).get_context_data(**kwargs)
        items = PaqueteConsumidoItem.objects.filter(
            paquete_consumido=self.object)
        context.update({'pe_active': 'active', 'paqueteitems': items})
        return context


class ProductoConsumidoCreate(CreateView):
    form_class = ProductoConsumidoForm
    template_name = 'prconsumido.html'
    context_object_name = 'prconsumido'
    success_url = '/'


class ProductosConsumidos(ListView):
    model = ProductoConsumido
    context_object_name = 'consumidos'
    template_name = 'pconsumido.html'


class ProductoConsumidoDetail(DetailView):
    model = ProductoConsumido
    context_object_name = 'consumido'
    template_name = 'consumido-detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ProductoConsumidoDetail, self).get_context_data(**kwargs)
        producto = self.object.producto
        ctx.update({'cd_active': 'active', 'producto': producto})
        return ctx


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
