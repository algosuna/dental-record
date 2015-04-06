# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect
from wkhtmltopdf.views import PDFTemplateView
from .forms import PaqueteForm, PaqueteConsumidoForm,PaqueteConsumidoItemForm
from paquete.models import Paquete, PaqueteItem,PaqueteConsumido,PaqueteConsumidoItem
from datetime import datetime
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from core.utils import generic_search

def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        PaqueteConsumido: ['paquete__nombre', 'paquete__descripcion']
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request,model,fields,query)

    return render_to_response('paqueteedit.html',
        {'objects':objects, 'search_string': request.GET.get(query,''), } )


def paquete(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/paquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "paquete.html", {"form": modelform})



def PaqueteItem(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})


class PaquetesPDF(PDFTemplateView):
    filename = 'paquetes.pdf'
    template_name = 'paquetes_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(PaquetesPDF, self).get_context_data(**kwargs)
        context['paquetes'] = EntryPaquete.objects.order_by('nombre__nombre')
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context



def ReportarPaquete (request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/orden/")
    else:
        modelform = PaqueteForm()
    return render(request, "packDetail.html", {"form": modelform})

class EditPaqueteView(UpdateView):  
    model=PaqueteConsumidoItem
    succes_url='/'
    template_name = 'packDetail.html'
    form_class = PaqueteConsumidoItem
    

    def get_succes_url(self):
        return  '/'

    def get_context_data(self,**kwargs):
        context=super(EditPaqueteView,self).get_context_data(**kwargs)
        context['action']=reverse('paquete-edit',
                                    kwargs={'pk': self.object.id})
        return context





