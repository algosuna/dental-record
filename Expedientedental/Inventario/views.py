#encoding:utf-8
import datetime

from django.shortcuts import render, redirect

from wkhtmltopdf.views import PDFTemplateView

from Inventario.forms import ProductoForm, CategoriaForm
from Inventario.models import Categoria, Producto

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
            modelform.save()
            return redirect("/producto/")
    else:
        modelform = ProductoForm()
    return render(request, "producto.html", {"form": modelform})


class ProductosPDF(PDFTemplateView):
    filename = 'productos.pdf'
    template_name = 'productos_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(ProductosPDF, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.order_by('categoria')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context

