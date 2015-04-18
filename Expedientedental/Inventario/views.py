#encoding:utf-8
from datetime import datetime
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q
from django.views.generic import UpdateView
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse

from wkhtmltopdf.views import PDFTemplateView

from Inventario.forms import ProductoForm, UnidadMedidaForm, EntradasForm
from Inventario.models import UnidadMedida, Producto, Entradas

from Inventario.utils import generic_search



def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        Producto: ['producto','porciones'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request,model,fields,query)

    return render_to_response('entradas.html', {'objects':objects, 'search_string' : request.GET.get(query,''), } )


class EditProductView(UpdateView):  
    model = Producto
    success_url = '/entradas/'
    template_name = 'producto.html'
    form_class = ProductoForm


    def get_success_url(self):
        return '/entradas/'
    

    def get_context_data(self,**kwargs):
        context=super(EditProductView,self).get_context_data(**kwargs)
        context['action']=reverse('producto-edit',
                                    kwargs={'pk': self.object.id})
        return context



def productoView(request):
    if request.method=='POST':
        modelform=ProductoForm(request.POST)
        if modelform.is_valid():
            producto = modelform.save(commit=False)
            producto.precioUnidad = producto.total()
            producto.save()
            return redirect('/producto/')
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})

def unidadView(request):
    if request.method == 'POST':
        modelform = UnidadMedidaForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect('/unidad/')
    else:
        modelform = UnidadMedidaForm()
    return render(request, "unidad.html", {"form": modelform})

class Unidad(ListView):
    model = UnidadMedida
    context_object_name = 'unidades'
    template_name = 'unidades.html'


def ingresarCantidad(request, entrada_id):
    # id de la entrada de producto
    entrada = get_object_or_404(Entradas, pk=entrada_id)
    if request.method == "POST":
        modelform = EntradasForm(request.POST)
        if modelform.is_valid():
            #modelform.save()
            producto = modelform.cleaned_data.get('producto')
            cantidad = int(modelform.cleaned_data.get('agregar_cantidad'))           
            cambioPrecio = int(modelform.cleaned_data.get('agregar_precio'))           
            entrada = Entradas.objects.get(producto=producto)
            entrada.agregar(cantidad)
            entrada.save()
            producto=entrada.producto
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
    def get_context_data(self ,**kargs):
        context=super(ProductosPDF).get_context_data(**kargs)
        context['productos'] = Producto.objects.order_by('producto__producto')
        context['categorias'] = Categoria.objects.order_by('nombre')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context





    




