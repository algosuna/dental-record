from django.conf.urls import patterns, url

from clinica.views import (
    InterrogatorioPDF, HistorialDetail, PacienteDetail, OdontogramaDetail,
    ProcedimientosView, HistorialView, InterrogatorioView, InterrogatorioUpdate
)


urlpatterns = patterns(
    'clinica.views',

    url(r'^$', 'paciente_search', name='paciente_search'),

    url(r'^(?P<paciente_id>\d+)/odontograma/$',
        'odontograma', name='odontograma'),

    url(r'^procedimiento/(?P<procedimiento_id>\d+)/$',
        'bitacora_create', name='bitacora_create'),

    url(r'^(?P<pk>\d+)/detail/$',
        PacienteDetail.as_view(), name='paciente_detail'),

    url(r'^odontograma/(?P<pk>\d+)/detail/$',
        OdontogramaDetail.as_view(), name='odontograma_detail'),

    url(r'^procedimientos/(?P<pk>\d+)/$',
        ProcedimientosView.as_view(), name='procedimientos'),

    url(r'^historial/(?P<pk>\d+)/$',
        HistorialView.as_view(), name='historial'),

    url(r'^historial/procedimiento/(?P<pk>\d+)/$',
        HistorialDetail.as_view(), name='historial_detail'),

    url(r'^interrogatorio/(?P<pk>\d+)/$',
        InterrogatorioView.as_view(), name='interrogatorio'),

    url(r'^interrogatorio/update/(?P<pk>\d+)/$',
        InterrogatorioUpdate.as_view(), name='interrogatorio_edit'),

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        InterrogatorioPDF.as_view(), name='pdf'),

)
