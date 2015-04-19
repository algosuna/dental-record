from django.conf.urls import patterns, url

from clinica.views import InterrogatorioPDF


urlpatterns = patterns(
    'clinica.views',

    url(r'^$', 'inicio'),
    url(r'^detalle/(?P<paciente_id>\d+)/$', 'detalle_paciente'),
    url(r'^odontograma/(?P<paciente_id>\d+)/$', 'odontograma'),
    url(r'^detalle/(?P<paciente_id>\d+)/odontograma/(?P<odontograma_id>\d+)/$',
        'detalle_odontograma', name='detalle_odontograma'),
    url(r'^procedimientos/(?P<paciente_id>\d+)/$', 'procedimientos',
        name='procedimientos'),
    url(r'^procedimiento/(?P<procedimiento_id>\d+)/$', 'procedimiento'),

    # Agregado para Interrogatorio
    url(r'^interrogatorio/(?P<paciente_id>\d+)/$',
        'interrogatorio', name='interrogatorio'),

)

urlpatterns += patterns(
    '',

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        InterrogatorioPDF.as_view()),

)
