from django.conf.urls import patterns, url
from consumidos.views import (
    EditPaqueteView, paquetec, manage_paquetes, PeticionView,
    peticionesView, producto_consumido)

urlpatterns = patterns(
    'consumidos.views',

    url(r'^peticiones/list/$', peticionesView .as_view()),
    url(r'^paquete/producto/$', producto_consumido.as_view()),
    url(r'^tipoPaquete/$', 'paquete_item'),
    url(r'^paquetes/$', paquetec, name='paquete_consumido'),
    url(r'^paquetes/insumos/(?P<pk>\d+)/$', manage_paquetes, name='insumos'),
    url(r'^tipoPaquete/edit/(?P<pk>\d+)$', EditPaqueteView.as_view()),
    url(r'^paquete/(?P<pk>\d+)/peticion/create/$',
        PeticionView.as_view(), name='peticion'),

)

urlpatterns += patterns(
    '',
    # Reportes PDF
    # url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
