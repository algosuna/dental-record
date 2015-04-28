# encoding:utf-8
from django.db.models import Q
from datetime import datetime
from django.views.generic import ListView, UpdateView, UpdateView
from django.core.urlresolvers import reverse
from django.shortcuts import (render, redirect, render_to_response,
                              get_object_or_404)
from wkhtmltopdf.views import PDFTemplateView
from Inventario.forms import ProductoForm, UnidadMedidaForm, EntradasForm, DevolucionesForm
from Inventario.models import UnidadMedida, Producto, Entradas
from Inventario.utils import generic_search
from django.contrib import messages


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['producto', 'porciones'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render_to_response('entradas.html', {'objects': objects,
                              'search_string': request.GET.get(query, ''), }
                              )


class EditProductView(UpdateView):
    model = Producto
    success_url = '/entradas/'
    template_name = 'producto.html'
    form_class = ProductoForm

    def get_success_url(self):
        return '/entradas/'

    def get_context_data(self, **kwargs):
        context = super(EditProductView, self).get_context_data(**kwargs)
        context['action'] = reverse('producto-edit',
                                    kwargs={'pk': self.object.id})
        return context


def productoView(request):
    if request.method == 'POST':
        modelform = ProductoForm(request.POST)
        if modelform.is_valid():
            producto = modelform.save(commit=False)
            producto.precioUnidad = producto.total()
            producto.save()
            return redirect('/inventario/productos/')
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})


class productos(ListView):
    model = Producto
    context_object_name = 'productos'
    template_name = 'productos.html'


class productoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto.html'
    success_url = '/inventario/producto/'


def unidadView(request):
    if request.method == 'POST':
        modelform = UnidadMedidaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/inventario/unidades/')
    else:
        modelform = UnidadMedidaForm()
    return render(request, "unidad.html", {"form": modelform})


class Unidad(ListView):
    model = UnidadMedida
    context_object_name = 'unidades'
    template_name = 'unidades.html'
    success_message = "%(name)s was created successfully"


def ingresarCantidad(request, entrada_id):
    # id de la entrada de producto
    entrada = get_object_or_404(Entradas, pk=entrada_id)
    if request.method == "POST":
        modelform = EntradasForm(request.POST)
        if modelform.is_valid():
            # modelform.save()
            producto = modelform.cleaned_data.get('producto')
            cantidad = int(modelform.cleaned_data.get('agregar'))
            entrada = Entradas.objects.get(producto=producto)
            entrada.agregar(cantidad)
            entrada.save()
            print entrada
            producto = entrada.producto
            producto.save()
            print producto
            return redirect("/productos/ingresar/")
    else:
        modelform = EntradasForm()
    return render(request, "ingresar.html", {"form": modelform,
                                             'entrada': entrada, })


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
