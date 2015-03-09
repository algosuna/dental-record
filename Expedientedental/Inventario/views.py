#encoding:utf-8
from datetime import datetime
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q

from wkhtmltopdf.views import PDFTemplateView

from Inventario.forms import ProductoForm, CategoriaForm, EntradasForm
from Inventario.models import Categoria, Producto, Entradas

from Inventario.utils import generic_search


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['nombre'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request,model,fields,query)

    return render_to_response('entradas.html', {'objects':objects, 'search_string' : request.GET.get(query,''), } )


def categoria(request):
    if request.method == "POST":
        modelform = CategoriaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/categoria/")
    else:
        modelform = CategoriaForm()
    return render(request, "categoriaProd.html", {"form": modelform})


def producto(request):
    if request.method == "POST":
        modelform = ProductoForm(request.POST)
        if modelform.is_valid():
            producto=modelform.save()

            Entradas.objects.create(
                        fecha=datetime.now(),
                        nombre=producto,
                        cantidad=0
                )
            return redirect("/producto/")
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})


def ingresarCantidad(request, entrada_id):
    # id de la entrada de producto
    entrada = get_object_or_404(Entradas, pk=entrada_id)
    if request.method == "POST":
        modelform = EntradasForm(request.POST)
        if modelform.is_valid():
            #modelform.save()
            producto = modelform.cleaned_data.get('nombre')
            cantidad = int(modelform.cleaned_data.get('agregar_cantidad'))           
            cambioPrecio = int(modelform.cleaned_data.get('agregar_precio'))           
            entrada = Entradas.objects.get(nombre=producto)
            entrada.agregar(cantidad)
            entrada.save()
            producto=entrada.nombre
            producto.precio=cambioPrecio
            producto.save()
            return redirect("/entradas/")
    else:
        modelform = EntradasForm()
    return render(request, "ingresar.html", {"form": modelform, 'entrada': entrada,})


def detallesProd(request, entrada_id):
    # id de la entrada de producto
    entrada = get_object_or_404(Entradas, pk=entrada_id)
    return render(request, "detallesProd.html", {'entrada': entrada, })


class ProductosPDF(PDFTemplateView):
    filename = 'productos.pdf'
    template_name = 'productos_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(ProductosPDF, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.order_by('categoria__nombre')
        context['categorias'] = Categoria.objects.order_by('nombre')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context

