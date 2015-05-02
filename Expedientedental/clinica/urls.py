from django.conf.urls import patterns, url

from clinica.views import InterrogatorioPDF, HistorialDetail, PacienteDetail


urlpatterns = patterns(
    'clinica.views',

    url(r'^$', 'paciente_search', name='paciente_search'),

    url(r'^odontograma/(?P<paciente_id>\d+)/$',
        'odontograma', name='odontograma'),

    url(r'^odontograma/detail/(?P<odontograma_id>\d+)/$',
        'odontograma_detail', name='odontograma_detail'),

    url(r'^procedimientos/(?P<paciente_id>\d+)/$',
        'procedimientos', name='procedimientos'),

    url(r'^procedimiento/(?P<procedimiento_id>\d+)/$',
        'bitacora_create', name='bitacora_create'),

    url(r'^historial/(?P<paciente_id>\d+)/$', 'historial', name='historial'),

    # Agregado para Interrogatorio
    url(r'^interrogatorio/(?P<paciente_id>\d+)/$',
        'interrogatorio', name='interrogatorio'),

)

urlpatterns += patterns(
    '',

    url(r'^detail/(?P<pk>\d+)/$',
        PacienteDetail.as_view(), name='paciente_detail'),

    url(r'^historial/procedimiento/(?P<pk>\d+)/$',
        HistorialDetail.as_view(), name='historial_detail'),

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        InterrogatorioPDF.as_view(), name='pdf'),

)
