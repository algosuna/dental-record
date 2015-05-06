# encoding:utf-8
from datetime import datetime

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, UpdateView, CreateView

from wkhtmltopdf.views import PDFTemplateView
from core.utils import generic_search

from inventario.models import UnidadMedida, Producto
from inventario.forms import (
    ProductoForm, UnidadMedidaForm, EntradasForm, DevolucionesForm,
    EgresosForm)


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['producto', 'porciones'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render_to_response('entradas.html', {'objects': objects,
                              'search_string': request.GET.get(query, '')})


class Productos(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos.html'


class ProductoCreate(CreateView):
    form_class = ProductoForm
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:productos')


class ProductoUpdate(UpdateView):
    form_class = ProductoForm
    model = Producto
    template_name = 'producto.html'
    success_url = reverse_lazy('inventario:productos')


class Unidades(ListView):
    model = UnidadMedida
    context_object_name = 'unidades'
    template_name = 'unidades.html'


class UnidadCreate(CreateView):
    form_class = UnidadMedidaForm
    model = UnidadMedida
    template_name = 'unidad.html'
    success_url = reverse_lazy('inventario:unidades')


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


class EntradasProducto(BaseProductoUpdate):
    form_class = EntradasForm
    template_name = 'ingresar.html'
    success_url = reverse_lazy('inventario:productos')

    def form_valid(self, form):
        producto = self.get_producto()
        porciones = int(form.cleaned_data.get('porciones'))
        producto.agregar(porciones)
        producto.save()
        return super(EntradasProducto, self).form_valid(form)


class EgresoCreate(BaseProductoUpdate):
    form_class = EgresosForm
    template_name = 'egresos.html'
    success_url = reverse_lazy('inventario:productos')


def devoluciones(request):
    if request.method == 'POST':
        modelform = DevolucionesForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/inventario/devolucion/')
    else:
        modelform = DevolucionesForm()
    print modelform.helper
    messages.add_message(request, messages.SUCCESS, 'Profile details updated.',
                         fail_silently=True)
    return render(request, "devoluciones.html", {"form": modelform})


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
