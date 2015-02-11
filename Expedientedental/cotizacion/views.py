# Create your views here.
from django.template.loader import get_template
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
import datetime
from cotizacion.models import Cotizacion
from cotizacion.models import CotizacionServicios
from .forms import CotizacionForm
from django.forms.models import BaseInlineFormSet, inlineformset_factory







def Cotizacion(request):

   # Utilizamos la propiedad inline formset para poder ingresar N numero de productos a la cotizacion
    inline_GrupoServicio = inlineformset_factory(Cotizacion,CotizacionServicios)
    if request.method=='POST': 
        # Enviamos los datos del formulario que contiene al cliente y medico
        formulario_Paciente = PacienteCotizacion(request.POST)
        if formulario_paciente.is_valid():
            paciente = formulario_Paciente.save(commit=False)
            if formulario_medico.is_valid():
            	medico=formulario_medico.save(commit=False)
            # Generamos el formulario y instanciamos al cliente 
            servicios_formset = inline_GrupoServicio(request.POST, instance=paciente)
            if GrupoServicio_formset.is_valid():
                paciente.save()
                medico.save()
                GrupoServicio_formset.save()
            return HttpResponseRedirect('/')
    else:
        formulario_paciente =PacienteCotizacion()
        GrupoServicio_formset = inline_producto()       
    return render_to_response('cotizacion.html',{'Paciente':Paciente,'GrupoServicios_formset':GrupoServicios_formset}, context_instance=RequestContext(request))
