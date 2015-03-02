from django.conf.urls import patterns, url

urlpatterns = patterns('ActividadesClinicas.views',

    url(r'^$', 'inicio'),
    url(r'^interrogatorio/$', 'HistoriaClinicaView'),
 		url(r'^odontograma/(?P<paciente_id>\d+)$', 'odontograma'),
    url(r'^diagnosticos/$', 'diagnosticos'),
    url(r'^evaluacion/$', 'buscarpaciente'),
    url(r'^detalles/$', 'detallespaciente'),

)
