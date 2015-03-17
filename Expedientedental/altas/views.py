#encoding:utf-8
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, ListView, UpdateView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from altas.models import Medico, Paciente, Grupo
from altas.forms import MedicoForm, PacienteForm, GrupoForm


def datosmedico_view(request):
	if request.method=='POST':
		form=MedicoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/medicos/')
	else:
		form=MedicoForm()
	ctx = {'form':form}
	return render_to_response('/medicos.html',ctx,context_instance=RequestContext(request))


def datospaciente_view(request):
	if request.method=='POST':
		form=PacienteForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			return HttpResponseRedirect('/pacientes/')
	else:
		form=PacienteForm()
	ctx = {'form':form}
	return render_to_response('/pacientes.html',ctx,context_instance=RequestContext(request))


class GrupoNewView(CreateView):
	form_class = GrupoForm
	template_name = 'grupo.html'

	def get_success_url(self):
		return reverse('grupos')


class GruposView(ListView):
	model = Grupo
	context_object_name = 'grupos'
	template_name = 'grupos.html'


class GrupoUpdateView(UpdateView):
	model = Grupo
	form_class = GrupoForm
	template_name = 'grupo.html'

	def get_success_url(self):
		return reverse('grupos')
