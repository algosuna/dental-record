from django.conf.urls import patterns, url

from clinica.views import (
    InterrogatorioPDF, HistorialDetail, PacienteDetail,
    ProcedimientosView, HistorialView, InterrogatorioView, OdontogramaDetail,
    Radiografias, RadiografiaCreate, RadiografiaDetail, RadiografiaUpdate
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

    url(r'^(?P<pk>\d+)/radiografias/$',
        Radiografias.as_view(), name='radiografias'),

    url(r'^(?P<pk>\d+)/radiografia/new/$',
        RadiografiaCreate.as_view(), name='radiografia_create'),

    url(r'^radiografia/(?P<pk>\d+)/detail/$',
        RadiografiaDetail.as_view(), name='radiografia_detail'),

    url(r'^radiografia/(?P<pk>\d+)/update/$',
        RadiografiaUpdate.as_view(), name='radiografia_update'),

    # Reportes PDF
    url(r'^interrogatorio/(?P<paciente_id>\d+)/pdf/$',
        InterrogatorioPDF.as_view(), name='pdf'),

)
