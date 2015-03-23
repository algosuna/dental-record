#encoding:utf-8
from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView

from wkhtmltopdf.views import PDFTemplateView

from ActividadesClinicas.forms import (
    OdontogramaForm, HistoriaClinicaForm, ProcedimientoForm,
    ProcedimientoFormSet, TratamientoForm, DiagnosticoForm
    )
from ActividadesClinicas.models import (
    HistoriaClinica, Odontograma, Tratamiento, Procedimiento, Diagnostico
    )
from ActividadesClinicas.utils import generic_search

from altas.models import Paciente


def inicio(request):
    query = 'q'
    MODEL_MAP = {
        Paciente: ['nombre','apellidoPaterno','apellidoMaterno'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request,model,fields,query)

    return render_to_response('inicio.html',
        {'objects': objects,
        'search_string': request.GET.get(query,''),
        })


def detalle_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    odontograma = paciente.odontograma_set.order_by('-created_at')[:10]
    detalle_paciente = 'active'

    return render(request, 'detalle-paciente.html',
        {'paciente': paciente,
        'odontograma': odontograma,
        'detalle_paciente': detalle_paciente})


def odontograma(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    tratamientos = Tratamiento.objects.all()

    if request.method == 'POST':
        modelform = OdontogramaForm(request.POST)
        formset = ProcedimientoFormSet(request.POST, request.FILES)
        if modelform.is_valid():
            odontograma = modelform.save()

            if formset.is_valid():
                for form in formset:
                    form.instance.odontograma = odontograma
                    form.save()

            else:
                print formset.errors

            return redirect(reverse('detalle', args=[paciente.id, odontograma.id]))
    else:
        modelform = OdontogramaForm()
        formset = ProcedimientoFormSet()

    odontograma_active = 'active'

    return render(request, 'odontograma.html',
        {'form': modelform,
        'formset': formset,
        'paciente': paciente,
        'tratamientos': tratamientos,
        'odontograma_active': odontograma_active
        })


def detalle_odontograma(request, paciente_id, odontograma_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    procedimientos = Procedimiento.objects.all()

    return render(request, 'detalle.html',
        {'paciente': paciente,
        'procedimientos': procedimientos,
        'odontograma': odontograma
        })


# TODO: Figure out how to name this thing
def HistoriaClinicaView(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    expediente = 'active'

    if request.method == 'POST':
        modelform = HistoriaClinicaForm(request.POST)

        if modelform.is_valid():
            modelform.save()
            return redirect('/')
    else:
        modelform = HistoriaClinicaForm()

    return render(request,'interrogatorio.html',
        {'form': modelform,
        'paciente': paciente,
        'expediente': expediente})


class InterrogatorioPDF(PDFTemplateView):
    filename = 'Interrogatorio.pdf'
    template_name = 'interrogatorio_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioPDF, self).get_context_data(**kwargs)
        self.paciente_id = int(kwargs.get('paciente_id'))
        paciente = get_object_or_404(Paciente, pk=self.paciente_id)
        context['paciente'] = paciente
        context['interrogatorio'] = HistoriaClinica.objects.get(paciente=paciente)
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context


class TratamientoNewView(CreateView):
    form_class = TratamientoForm
    template_name = 'tratamiento.html'

    def get_success_url(self):
        return reverse('tratamientos')


class TratamientosView(ListView):
    model = Tratamiento
    context_object_name = 'tratamientos'
    template_name = 'tratamientos.html'


class TratamientoUpdateView(UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento.html'

    def get_success_url(self):
        return reverse('tratamientos')


class DiagnosticoNewView(CreateView):
    form_class = DiagnosticoForm
    template_name = 'diagnostico.html'

    def get_success_url(self):
        return reverse('diagnosticos')


class DiagnosticosView(ListView):
    model = Diagnostico
    context_object_name = 'diagnosticos'
    template_name = 'diagnosticos.html'

class DiagnosticoUpdateView(UpdateView):
    model = Diagnostico
    form_class = DiagnosticoForm
    template_name = 'diagnostico.html'

    def get_success_url(self):
        return reverse('diagnosticos')

