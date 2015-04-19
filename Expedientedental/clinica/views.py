# encoding:utf-8
from datetime import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response,\
    get_object_or_404

from wkhtmltopdf.views import PDFTemplateView

from clinica.models import Interrogatorio, Odontograma, Procedimiento, Bitacora
from clinica.forms import OdontogramaForm, InterrogatorioForm, BitacoraForm,\
    ProcedimientoFormSet
from altas.models import Paciente, Tratamiento

from core.utils import generic_search


def inicio(request):
    query = 'q'
    MODEL_MAP = {
        Paciente: ['nombre', 'apellidoPaterno', 'apellidoMaterno'],
    }

    objects = []

    for model, fields in MODEL_MAP.iteritems():
        objects += generic_search(request, model, fields, query)

    return render_to_response('inicio.html', {
                              'objects': objects,
                              'search_string': request.GET.get(query, '')
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

            return redirect(reverse(
                'detalle_odontograma', args=[paciente.id, odontograma.id]))
    else:
        modelform = OdontogramaForm()
        formset = ProcedimientoFormSet()

    odontograma_active = 'active'

    return render(request, 'odontograma.html', {
                  'form': modelform,
                  'formset': formset,
                  'paciente': paciente,
                  'tratamientos': tratamientos,
                  'odontograma_active': odontograma_active
                  })


def detalle_odontograma(request, paciente_id, odontograma_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    odontograma = get_object_or_404(Odontograma, pk=odontograma_id)
    procedimientos = Procedimiento.objects.all()

    return render(request, 'detalle-odontograma.html', {
                  'paciente': paciente,
                  'procedimientos': procedimientos,
                  'odontograma': odontograma
                  })


def procedimientos(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    procedimientos = Procedimiento.objects.filter(
        odontograma__paciente=paciente,
        status__in=['autorizado', 'en_proceso']
    )

    bitacoras = Bitacora.objects\
        .filter(procedimiento__odontograma__paciente=paciente)\
        .order_by('-created_at')[:10]

    p_active = 'active'

    return render(request, 'procedimientos.html', {
                  'paciente': paciente,
                  'procedimientos': procedimientos,
                  'bitacoras': bitacoras,
                  'p_active': p_active
                  })


def procedimiento(request, procedimiento_id):
    procedimiento = get_object_or_404(Procedimiento, pk=procedimiento_id)
    paciente = procedimiento.odontograma.paciente
    bitacoras = procedimiento.bitacora_set.all()

    if request.method == 'POST':
        form = BitacoraForm(request.POST)

        if form.is_valid():
            is_complete = form.cleaned_data.get('is_complete')

            if is_complete:
                procedimiento.status = 'completado'

            else:
                procedimiento.status = 'en_proceso'

            form.save()
            procedimiento.save()

            return redirect(reverse('procedimientos', args=[paciente.id]))

    else:
        form = BitacoraForm(initial={'procedimiento': procedimiento})

    p_active = 'active'

    return render(request, 'procedimiento.html', {
                  'procedimiento': procedimiento,
                  'paciente': paciente,
                  'form': form,
                  'bitacoras': bitacoras,
                  'p_active': p_active
                  })


def interrogatorio(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    expediente = 'active'

    if request.method == 'POST':
        modelform = InterrogatorioForm(request.POST)

        if modelform.is_valid():
            modelform.save()

    else:
        modelform = InterrogatorioForm()

    return render(request, 'interrogatorio.html', {
                  'form': modelform,
                  'paciente': paciente,
                  'expediente': expediente
                  })


class InterrogatorioPDF(PDFTemplateView):
    filename = 'interrogatorio.pdf'
    template_name = 'interrogatorio_pdf.html'
    cmd_options = {
        'margin-top': 13,
    }

    def get_context_data(self, **kwargs):
        context = super(InterrogatorioPDF, self).get_context_data(**kwargs)
        self.paciente_id = int(kwargs.get('paciente_id'))
        paciente = get_object_or_404(Paciente, pk=self.paciente_id)
        interrogatorio = Interrogatorio.objects.get(paciente=paciente)
        context['paciente'] = paciente
        context['interrogatorio'] = interrogatorio
        context['fecha'] = datetime.now().strftime("%d/%m/%Y")
        context['hora'] = datetime.now().strftime("%I:%M %p")
        return context
