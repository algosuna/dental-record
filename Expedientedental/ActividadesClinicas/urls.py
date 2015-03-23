from django.conf.urls import patterns, url
from ActividadesClinicas.views import InterrogatorioPDF

urlpatterns = patterns('ActividadesClinicas.views',

    url(r'^$', 'inicio'),
    #url(r'^interrogatorio/$', 'HistoriaClinicaView'),
 	#Agregado para Interrogatorio/Historial Clinico
 	url(r'^interrogatorio/(?P<paciente_id>\d+)$', 'HistoriaClinicaView'),
 	url(r'^odontograma/(?P<paciente_id>\d+)$', 'odontograma'),
    url(r'^odontograma/(?P<paciente_id>\d+)/detalle/(?P<odontograma_id>\d+)$', 'detalle', name='detalle'),
    url(r'^paciente/(?P<paciente_id>\d+)$', 'detallePaciente', name='detallePaciente'),
    url(r'^diagnosticos/$', 'diagnosticos'),
    url(r'^evaluacion/$', 'buscarpaciente'),

)

urlpatterns += patterns('',

    #Reportes PDF
    
    url(r'^interrogatorios/(?P<paciente_id>\d+)/pdf/$',InterrogatorioPDF.as_view()),

)
