from django.conf.urls import patterns, url
from consumidos.views import (
    AtencionPaquete, manage_paquetes, PeticionView,
    peticionesView, producto_consumido, PaqueteItem, Paquetes)

urlpatterns = patterns(
    'consumidos.views',

    url(r'^paquete/(?P<pk>\d+)/peticion/create/$',
        PeticionView.as_view(), name='request'),

    url(r'^paquete/agroup/new/$', PaqueteItem.as_view(), name='armar'),

    url(r'^paquetes/list/$', Paquetes.as_view(), name='paquetes_list'),

    url(r'^peticiones/list/$', peticionesView .as_view(),
        name='request_list'),

    url(r'^paquete/producto/$', producto_consumido.as_view(),
        name='prconsumido'),

    url(r'^paquetes/(?P<pk>\d+)/$', AtencionPaquete.as_view(),
        name='pconsumido'),

    url(r'^paquetes/insumos/(?P<pk>\d+)/$', manage_paquetes, name='insumos'),

)

urlpatterns += patterns(
    '',
    # Reportes PDF
    # url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
