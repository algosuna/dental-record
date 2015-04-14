# encoding:utf-8
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView

from altas.models import Grupo, Tratamiento, TratamientoPreventivo,\
    Evaluacion, Medico, Paciente
from altas.forms import MedicoForm, PacienteForm, GrupoForm, TratamientoForm,\
    TratamientoPreventivoForm, EvaluacionForm


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

    def get_success_url(self):
        return reverse('precios', args=[self.object.id])


class GruposView(ListView):
    model = Grupo
    context_object_name = 'grupos'
    template_name = 'grupos.html'


class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url = '/altas/grupos/'


class MetodoMixin(object):
    name = None
    slug = None
    # form_class = MetodoForm
    template_name = 'metodo.html'

    def get_success_url(self):
        if self.slug:
            path_name = self.slug
        else:
            path_name = self.name

        return '/altas/%s/' % path_name

    def get_context_data(self, **kwargs):
        context = super(MetodoMixin, self).get_context_data(**kwargs)
        context['title'] = self.name.title()

        if self.slug:
            context['name'] = self.slug

        else:
            context['name'] = self.name

        return context


class MetodoNewView(MetodoMixin, CreateView):
    pass


class MetodoListView(MetodoMixin, ListView):
    template_name = 'metodos.html'


class MetodoUpdateView(MetodoMixin, UpdateView):
    pass


class TratamientoNewView(MetodoNewView):
    name = 'tratamiento'
    form_class = TratamientoForm


class TratamientosView(MetodoListView):
    name = 'tratamiento'
    model = Tratamiento


class TratamientoUpdateView(MetodoUpdateView):
    model = Tratamiento
    name = 'tratamiento'
    form_class = TratamientoForm


class EvaluacionNewView(MetodoNewView):
    name = 'evaluacion'
    form_class = EvaluacionForm


class EvaluacionesView(MetodoListView):
    name = 'evaluacion'
    model = Evaluacion


class EvaluacionUpdateView(MetodoUpdateView):
    model = Evaluacion
    name = 'evaluacion'
    form_class = EvaluacionForm


class TratamientoPreventivoNewView(MetodoNewView):
    name = 'tratamiento preventivo'
    slug = 'preventivo'
    form_class = TratamientoPreventivoForm


class TratamientosPreventivosView(MetodoListView):
    name = 'tratamiento preventivo'
    model = TratamientoPreventivo
    slug = 'preventivo'


class TratamientoPreventivoUpdateView(MetodoUpdateView):
    model = TratamientoPreventivo
    name = 'tratamiento preventivo'
    slug = 'preventivo'
    form_class = TratamientoPreventivoForm
