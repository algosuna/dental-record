from django.conf.urls import patterns, url
from consumidos.views import (
    PeticionCreate, Peticiones, PeticionUpdate, PeticionesAtendidas,
    Consumidos, producto_consumido,
    ConsumidoDetail, PaqueteCreate, Paquetes, PaquetebillPDF,
    SalidaCancel, SalidaPDF
)

urlpatterns = patterns(
    'consumidos.views',

    url(r'^paquetes/$', Paquetes.as_view(), name='paquete_list'),

    url(r'^paquete/new/$', PaqueteCreate.as_view(), name='paquete_new'),

    url(r'^peticiones/$', Peticiones.as_view(), name='peticion_list'),

    url(r'^peticiones/surtido/$',
        PeticionesAtendidas.as_view(), name='peticion_surtido_list'),

    url(r'^peticion/new/servicio/(?P<pk>\d+)/$',
        PeticionCreate.as_view(), name='peticion_new'),

    url(r'^peticion/(?P<pk>\d+)/update/$',
        PeticionUpdate.as_view(), name='peticion_update'),

    url(r'^peticion/(?P<pk>\d+)/insumos/add/$',
        'paquete_item_create', name='paquete_item_create'),




    url(r'^paquete/producto/$', producto_consumido.as_view(),
        name='prconsumido'),

    url(r'^paquetes/pconsumido/list/$', Consumidos.as_view(),
        name='consumido'),

    url(r'^paquetes/detail/(?P<pk>\d+)/$', ConsumidoDetail.as_view(),
        name='cons_detail'),

    url(r'^paquetes/salida/cancel/$', SalidaCancel.as_view(),
        name='cancel_list'),


    url(r'^(?P<pk>\d+)/pdf/$', SalidaPDF.as_view(), name='pdf'),
    url(r'^paquete/(?P<pk>\d+)/recibo/pdf/$',
        PaquetebillPDF.as_view(), name='paquete_recibo'),
)
