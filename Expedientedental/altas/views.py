# encoding:utf-8
from django.views.generic import CreateView, ListView, UpdateView

from altas.models import Grupo, Tratamiento, Evaluacion, TratamientoPreventivo,\
    Medico, Paciente
from altas.forms import MedicoForm, PacienteForm, GrupoForm, TratamientoForm,\
    EvaluacionForm, TratamientoPreventivoForm


class MedicoCreate(CreateView):
    form_class = MedicoForm
    template_name = 'medico.html'
    success_url = '/altas/medicos/'


class Medicos(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'medicos.html'


class MedicoUpdate(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico.html'
    success_url = '/altas/medicos/'


class PacienteCreate(CreateView):
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = '/altas/pacientes/'


class Pacientes(ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'pacientes.html'


class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = '/altas/pacientes/'


class GrupoNewView(CreateView):
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url = '/altas/grupos/'


class GruposView(ListView):
    model = Grupo
    context_object_name = 'grupos'
    template_name = 'grupos.html'


class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url = '/altas/grupos/'


class TratamientoNewView(CreateView):
    form_class = TratamientoForm
    template_name = 'tratamiento.html'
    success_url = '/altas/tratamientos/'


class TratamientosView(ListView):
    model = Tratamiento
    context_object_name = 'tratamientos'
    template_name = 'tratamientos.html'


class TratamientoUpdateView(UpdateView):
    model = Tratamiento
    form_class = TratamientoForm
    template_name = 'tratamiento.html'
    success_url = '/altas/tratamientos/'


class EvaluacionNewView(CreateView):
    form_class = EvaluacionForm
    template_name = 'evaluacion.html'
    success_url = '/altas/evaluaciones/'


class EvaluacionesView(ListView):
    model = Evaluacion
    context_object_name = 'evaluaciones'
    template_name = 'evaluaciones.html'


class EvaluacionUpdateView(UpdateView):
    model = Evaluacion
    form_class = EvaluacionForm
    template_name = 'evaluacion.html'
    success_url = '/altas/evaluaciones/'


class TratamientoPreventivoNewView(CreateView):
    form_class = TratamientoPreventivoForm
    template_name = 'tratamiento.html'
    success_url = '/altas/tratamientos-preventivos/'


class TratamientosPreventivosView(ListView):
    model = TratamientoPreventivo
    context_object_name = 'tratamientos'
    template_name = 'tratamientos.html'


class TratamientoPreventivoUpdateView(UpdateView):
    model = TratamientoPreventivo
    form_class = TratamientoPreventivoForm
    template_name = 'tratamiento.html'
    success_url = '/altas/tratamientos-preventivos/'
