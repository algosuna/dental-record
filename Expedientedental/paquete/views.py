from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from wkhtmltopdf.views import PDFTemplateView
from .forms import PaqueteForm, PaqueteConsumidoForm, PaqueteConsumidoIForm
from paquete.models import Paquete, PaqueteItem, PaqueteConsumido,\
PaqueteConsumidoItem
from datetime import datetime
from django.views.generic import UpdateView, ListView

from django.core.urlresolvers import reverse
from core.utils import generic_search


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        PaqueteConsumido: ['paquete__nombre', 'paquete__descripcion']
    }

    objects = []

    for model, fields in MODEL_MAP.items():
        objects += generic_search(request, model, fields, query)

    return render_to_response('paqueteedit.html',
        {'objects':objects, 'search_string': request.GET.get(query, ''), }
        )

def PaqueteItem(request):
    if request.method == "POST":
        modelform = PaqueteForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/tipoPaquete/")
    else:
        modelform = PaqueteForm()
    return render(request, "tipoPaquete.html", {"form": modelform})


def PaqueteC(request):
    if request.method == "POST":
        modelform = PaqueteConsumidoForm(request.POST)
        if modelform.is_valid():

            modelform.save()
            return redirect('/paquetes/')
    else:
        modelform = PaqueteConsumidoForm()
    return render(request, "salida_pack.html", {"form": modelform})



        













class Pending(ListView):
    model = PaqueteConsumido
    context_object_name = 'paquetes'
    template_name = 'pendingorders.html'


def ReportarPaquete(request):
    if request.method == "POST":
        modelform = PaqueteConsumidoIForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/orden/")
    else:
        modelform = PaqueteConsumidoIForm()
    return render(request, "paquetes.html", {"form": modelform})


class EditPaqueteView(UpdateView):
    model = PaqueteConsumidoItem
    succes_url = '/'
    template_name = 'packDetail.html'
    form_class = PaqueteConsumidoItem

    def get_succes_url(self):
        return '/'

    def get_context_data(self, **kwargs):
        context = super(EditPaqueteView, self).get_context_data(**kwargs)
        context['action'] = reverse('paquete-edit',
                                    kwargs={'pk': self.object.id})
        return context
