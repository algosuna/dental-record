# encoding:utf-8
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView

from altas.models import (
    Grupo, Tratamiento, TratamientoPreventivo, Evaluacion, Medico, Paciente
)
from altas.forms import (
    MedicoForm, PacienteForm, GrupoForm, TratamientoForm, EvaluacionForm,
    TratamientoPreventivoForm, MedicoUserForm
)


def medico_create(request):
    ''' Creates Medico and User. '''
    if request.method == 'POST':
        medico_user_form = MedicoUserForm(request.POST)
        medico_form = MedicoForm(request.POST)

        if medico_user_form.is_valid() and medico_form.is_valid():
            user = medico_user_form.save()
            medico = medico_form.save(commit=False)
            medico.user = user
            medico.save()
            return redirect('altas:medicos')

    else:
        medico_user_form = MedicoUserForm()
        medico_form = MedicoForm()

    return render(request, 'medico.html',
                  {'medico_user_form': medico_user_form,
                   'medico_form': medico_form})


class Medicos(ListView):
    model = Medico
    context_object_name = 'medicos'
    template_name = 'medicos.html'


class MedicoUpdate(UpdateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'medico.html'
    success_url = reverse_lazy('altas:medicos')


class PacienteCreate(CreateView):
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = reverse_lazy('altas:pacientes')


class Pacientes(ListView):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'pacientes.html'


class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name = 'paciente.html'
    success_url = reverse_lazy('altas:pacientes')


class GrupoNewView(CreateView):
    form_class = GrupoForm
    template_name = 'grupo.html'

    def get_success_url(self):
        return reverse('precios:precios', args=[self.object.id])


class GruposView(ListView):
    model = Grupo
    context_object_name = 'grupos'
    template_name = 'grupos.html'


class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'grupo.html'
    success_url = reverse_lazy('altas:grupos')


class MetodoMixin(object):
    name = None
    slug = None
    # form_class = MetodoForm
    template_name = 'metodo.html'

    def get_success_url(self):
        if self.slug:
            url = self.slug
        else:
            url = self.name

        return 'altas:%s' % url

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
