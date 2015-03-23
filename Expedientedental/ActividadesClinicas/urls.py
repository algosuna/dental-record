from django.conf.urls import patterns, url

from ActividadesClinicas.views import (
    InterrogatorioPDF, TratamientoNewView, TratamientoUpdateView, TratamientosView,
    DiagnosticoNewView, DiagnosticoUpdateView, DiagnosticosView
    )
from Inventario.views import ProductosPDF

urlpatterns = patterns('ActividadesClinicas.views',

    url(r'^$', 'inicio'),
    url(r'^detalle-paciente/(?P<paciente_id>\d+)/$', 'detalle_paciente'),
    url(r'^odontograma/(?P<paciente_id>\d+)/$', 'odontograma'),
    url(r'^odontograma/(?P<paciente_id>\d+)/detalle/(?P<odontograma_id>\d+)/$',
        'detalle_odontograma', name='detalle_odontograma'),

 	#Agregado para Interrogatorio/Historial Clinico
 	url(r'^interrogatorio/(?P<paciente_id>\d+)/$', 'HistoriaClinicaView'),

)

urlpatterns += patterns('',

    url(r'^tratamiento/new/$', TratamientoNewView.as_view()),
    url(r'^tratamiento/edit/(?P<pk>\d+)/$', TratamientoUpdateView.as_view()),
    url(r'^tratamientos/$', TratamientosView.as_view(), name='tratamientos'),
    url(r'^diagnostico/new/$', DiagnosticoNewView.as_view()),
    url(r'^diagnostico/edit/(?P<pk>\d+)/$', DiagnosticoUpdateView.as_view()),
    url(r'^diagnosticos/$', DiagnosticosView.as_view(), name='diagnosticos'),

    #Reportes PDF
    url(r'^productos/pdf/$',ProductosPDF.as_view()),
    url(r'^interrogatorios/(?P<paciente_id>\d+)/pdf/$',InterrogatorioPDF.as_view()),

)
