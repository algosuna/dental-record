# encoding:utf-8
from datetime import datetime

from django.contrib.auth.decorators import permission_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView

from wkhtmltopdf.views import PDFTemplateView
from core.utils import generic_search
from core.mixins import PermissionRequiredMixin

from inventario.models import UnidadMedida, Producto, Entradas
from inventario.forms import (
    ProductoForm, UnidadMedidaForm, EntradasForm, EntradaCanceladaForm
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
    success_url = reverse_lazy('inventario:productos')
    permission_required = 'inventario.add_producto'

    def get_context_data(self, **kwargs):
        context = super(ProductoCreate, self).get_context_data(**kwargs)
        context.update({'pc_active': 'active'})
        return context


class ProductoUpdate(PermissionRequiredMixin, UpdateView):
    form_class = ProductoForm
    model = Producto
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:productos')
    permission_required = 'inventario.change_producto'


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


class BaseProductoUpdate(CreateView):
    '''
    Base class that contains methods in common for updating Producto class.
    '''
    def get_producto(self):
        producto = Producto.objects.get(pk=self.kwargs.get('pk'))
        return producto

    def get_context_data(self, **kwargs):
        context = super(BaseProductoUpdate, self).get_context_data(**kwargs)
        context.update({'producto': self.get_producto()})
        return context

    def get_initial(self):
        initial = super(BaseProductoUpdate, self).get_initial()
        initial = initial.copy()
        initial['producto'] = self.get_producto()
        return initial


class EntradasList(PermissionRequiredMixin, ListView):
    model = Entradas
    context_object_name = 'entradas'
    template_name = 'entradas.html'
    permission_required = 'inventario.add_entradas'


class EntradaDetail(PermissionRequiredMixin, UpdateView):
    form_class = EntradaCanceladaForm
    model = Entradas
    context_object_name = 'entrada'
    template_name = 'entrada-detail.html'
    success_url = reverse_lazy('inventario:entradas')
    permission_required = 'inventario.change_entradas'


class EntradasProducto(PermissionRequiredMixin, BaseProductoUpdate):
    form_class = EntradasForm
    template_name = 'entrada.html'
    success_url = reverse_lazy('inventario:producto_list')
    permission_required = 'inventario:change_producto'

    def form_valid(self, form):
        producto = self.get_producto()
        porciones = int(form.cleaned_data.get('porciones'))
        producto.agregar(porciones)
        producto.save()
        return super(EntradasProducto, self).form_valid(form)


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
