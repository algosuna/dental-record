# encoding:utf-8
from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView

from wkhtmltopdf.views import PDFTemplateView
from core.utils import generic_search
from core.mixins import PermissionRequiredMixin
from core.views import CreateObjFromContext

from inventario.models import UnidadMedida, Producto, Entrada, CancelEntrada
from inventario.forms import (
    ProductoForm, UnidadMedidaForm, EntradaForm, EntradaCanceladaForm,
    CancelEntradaForm
)


@permission_required('inventario.add_producto')
def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['producto', 'porciones'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render(request, 'producto-search.html', {
        'objects': objects,
        'search_string': request.GET.get(query, ''),
        's_active': 'active'})


class Productos(PermissionRequiredMixin, ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos.html'
    permission_required = 'inventario.add_producto'

    def get_context_data(self, **kwargs):
        context = super(Productos, self).get_context_data(**kwargs)
        context.update({'i_active': 'active'})
        return context


class ProductoCreate(PermissionRequiredMixin, CreateView):
    form_class = ProductoForm
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:producto_list')
    permission_required = 'inventario.add_producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoCreate, self).get_context_data(**kwargs)
        context.update({'pc_active': 'active'})
        return context


class ProductoUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ProductoForm
    model = Producto
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:producto_list')
    permission_required = 'inventario.change_producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoUpdate, self).get_context_data(**kwargs)
        context.update({'i_active': 'active'})
        return context


class Unidades(PermissionRequiredMixin, ListView):
    model = UnidadMedida
    context_object_name = 'unidades'
    template_name = 'unidades.html'
    permission_required = 'inventario.add_unidadmedida'


class UnidadCreate(PermissionRequiredMixin, CreateView):
    form_class = UnidadMedidaForm
    model = UnidadMedida
    template_name = 'unidad.html'
    success_url = reverse_lazy('inventario:unidades')
    permission_required = 'inventario.add_unidadmedida'


class EntradaList(PermissionRequiredMixin, ListView):
    model = Entrada
    queryset = model.objects.filter(is_cancelled=False)
    context_object_name = 'entradas'
    template_name = 'entradas.html'
    permission_required = 'inventario.add_entrada'

    def get_context_data(self, **kwargs):
        context = super(EntradaList, self).get_context_data(**kwargs)
        context.update({'e_active': 'active'})
        return context


class EntradaDetail(PermissionRequiredMixin, UpdateView):
    form_class = EntradaCanceladaForm
    model = Entrada
    context_object_name = 'entrada'
    template_name = 'entrada-detail.html'
    permission_required = 'inventario.change_entrada'

    def get_context_data(self, **kwargs):
        context = super(EntradaDetail, self).get_context_data(**kwargs)
        context.update({'e_active': 'active'})
        return context

    def get_success_url(self):
        url = reverse('inventario:entrada_cancel', kwargs=self.kwargs)
        return url


class EntradaProducto(PermissionRequiredMixin, CreateObjFromContext):
    form_class = EntradaForm
    template_name = 'entrada.html'
    ctx_model = Producto
    initial_value = 'producto'
    success_url = reverse_lazy('inventario:producto_list')
    permission_required = 'inventario.change_producto'

    def get_context_data(self, **kwargs):
        context = super(EntradaProducto, self).get_context_data(**kwargs)
        context.update({'i_active': 'active'})
        return context

    def form_valid(self, form):
        producto = self.get_obj()
        porciones = int(form.cleaned_data.get('porciones'))
        producto.agregar(porciones)
        producto.save()
        return super(EntradaProducto, self).form_valid(form)


class EntradasCancelledList(PermissionRequiredMixin, ListView):
    model = Entrada
    queryset = model.objects.filter(is_cancelled=True)
    context_object_name = 'entradas'
    template_name = 'entradas-canceladas.html'
    permission_required = 'inventario.add_cancelentrada'

    def get_context_data(self, **kwargs):
        context = super(EntradasCancelledList, self).get_context_data(**kwargs)
        cancelled = CancelEntrada.objects.all()
        context.update({'cancelentrada': cancelled, 'ec_active': 'active'})
        return context


class EntradaCancel(PermissionRequiredMixin, CreateObjFromContext):
    form_class = CancelEntradaForm
    ctx_model = Entrada
    template_name = 'entrada-cancel.html'
    success_url = reverse_lazy('inventario:entradas_canceladas')
    permission_required = 'inventario.add_cancelentrada'
    initial_value = 'entrada'

    def get_context_data(self, **kwargs):
        context = super(EntradaCancel, self).get_context_data(**kwargs)
        context.update({'e_active': 'active'})
        return context


class EntradaCancelDetail(PermissionRequiredMixin, DetailView):
    model = CancelEntrada
    template_name = 'entradacancel-detail.html'
    permission_required = 'inventario.add_cancelentrada'
    context_object_name = 'cancelentrada'

    def get_context_data(self, **kwargs):
        context = super(EntradaCancelDetail, self).get_context_data(**kwargs)
        entrada = self.object.entrada
        print entrada
        context.update({'entrada': entrada})
        return context


class ProductosPDF(PDFTemplateView):
    filename = 'productos.pdf'
    template_name = 'productos_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kargs):
        context = super(ProductosPDF).get_context_data(**kargs)
        context['productos'] = Producto.objects.order_by('producto__producto')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
