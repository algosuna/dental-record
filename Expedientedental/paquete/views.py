from datetime import datetime
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.forms.models import modelformset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.core.context_processors import csrf
from wkhtmltopdf.views import PDFTemplateView
from .forms import (PaqueteForm, PaqueteConsumidoForm, PCItemForm)
from paquete.models import Paquete, PaqueteItem, PaqueteConsumido,\
Paquet
from django.views.generic import UpdateView, ListView

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

            paquete_consumido = modelform.save()
            succes_url = reverse('insumos', args=[paquete_consumido.pk])
            return redirect(succes_url)
    else:
        modelform = PaqueteConsumidoForm()
    return render(request, "salida_pack.html", {"form": modelform})


def manage_paquetes(request, pk):
    paquete_consumido = get_object_or_404(PaqueteConsumido, pk=pk)
    items = paquete_consumido.paqueteconsumidoitem_set.all()
    # initial list para items predeterminados
    initial_list = paquete_consumido.get_item_initials()
    # agregamos initial para un formulario vacio
    initial_list.append({'paquete_consumido': paquete_consumido})
    ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                       form=PCItemForm,
                                       extra=len(initial_list))
    if request.method == 'POST':
        formset = ItemFormset(request.POST)


        if formset.is_valid():
            formset.save()
            

    else:
        formset = ItemFormset(queryset=items, initial=initial_list)
    context = {
        'formset': formset,
        'paquete': paquete_consumido
    }
    return render_to_response('paquete_def.html', context)


class Pending(ListView):
    model = PaqueteConsumido
    context_object_name = 'paquetes'
    template_name = 'pendingorders.html'


def ReportarPaquete(request):
    if request.method == "POST":
        modelform = PaqueteConsumidoItemForm(request.POST)
        if modelform.is_valid():
            modelform.save()
            return redirect("/orden/")
    else:
        modelform = PaqueteConsumidoItemForm()
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
