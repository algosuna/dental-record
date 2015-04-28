from django.core.urlresolvers import reverse
#from django.template import RequestContext
from django.forms.models import modelformset_factory
from django.http import Http404, HttpResponse
from django.shortcuts import (render_to_response, render, redirect,
                              get_object_or_404)
from django.utils.datastructures import MultiValueDictKeyError


from .forms import (PaqueteForm, PaqueteConsumidoForm, PCItemForm)
from paquete.models import (Paquete, PaqueteItem, PaqueteConsumido,
                            PaqueteConsumidoItem)
from django.views.generic import UpdateView, ListView
from core.utils import generic_search


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
    initial_list = []
    if not items.exists():
        initial_list = paquete_consumido.get_item_initials()
    # agregamos initial para un formulario vacio
    # initial_list.append({'paquete_consumido': paquete_consumido})
    # Se usa empty form generada por formset
    if request.method == 'POST':
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=0)
        formset = ItemFormset(request.POST)

        if formset.is_valid():
            print "VALIDO"
            for form in formset:
                form.save(paquete_consumido)
        else:
            print "INVALIDO"
            print request.POST
            print formset.errors

    else:
        print 'len', len(initial_list)
        ItemFormset = modelformset_factory(PaqueteConsumidoItem,
                                           form=PCItemForm,
                                           extra=len(initial_list))
        formset = ItemFormset(queryset=items, initial=initial_list)
    context = {
        'formset': formset,
        'paquete': paquete_consumido
    }
    return render(request, 'paquete_def.html', context)


class Pending(ListView):
    model = PaqueteConsumido
    context_object_name = 'paquetes'
    template_name = 'pendingorders.html'


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


def busqueda(request):
    query = 'q'
    MODEL_MAP = {
        PaqueteConsumido: ['paquete__nombre', 'paquete__descripcion']
    }

    objects = []

    for model, fields in MODEL_MAP.items():
        objects += generic_search(request, model, fields, query)

    return render_to_response('paqueteedit.html', {'objects': objects,
                              'search_string': request.GET.get(query, ''), }   
                               )