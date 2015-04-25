from django.conf.urls import patterns, url

from clinica.views import InterrogatorioPDF


urlpatterns = patterns(
    'clinica.views',

    url(r'^$', 'paciente_search', name='paciente_search'),

    url(r'^detail/(?P<paciente_id>\d+)/$',
        'paciente_detail', name='paciente_detail'),

    url(r'^odontograma/(?P<paciente_id>\d+)/$',
        'odontograma', name='odontograma'),

    url(r'^odontograma/detail/(?P<odontograma_id>\d+)/$',
        'odontograma_detail', name='odontograma_detail'),

    url(r'^procedimientos/(?P<paciente_id>\d+)/$',
        'procedimientos', name='procedimientos'),

    url(r'^procedimiento/(?P<procedimiento_id>\d+)/$',
        'bitacora_create', name='bitacora_create'),

    url(r'^historial/(?P<paciente_id>\d+)/$', 'historial', name='historial'),

    url(r'^historial/procedimiento/(?P<procedimiento_id>\d+)/$',
        'historial_detail', name='historial_detail'),

    # Agregado para Interrogatorio
    url(r'^interrogatorio/(?P<paciente_id>\d+)/$',
        'interrogatorio', name='interrogatorio'),

)

urlpatterns += patterns(
    '',

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        InterrogatorioPDF.as_view(), name='pdf'),

)
