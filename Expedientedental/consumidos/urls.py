from django.conf.urls import patterns, url
from consumidos.views import (
    Paquetes, PaqueteCreate, Peticiones, PeticionesAtendidas, PeticionCreate,
    PeticionUpdate, ProductoConsumidoCreate, PeticionDetail,
    ProductosConsumidos, ProductoConsumidoDetail,
    SalidaCancel, SalidaPDF, PaquetebillPDF
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

    url(r'^peticion/(?P<pk>\d+)/detail/$',
        PeticionDetail.as_view(), name='peticion_detail'),

    url(r'^peticion/(?P<pk>\d+)/insumos/add/$',
        'paquete_item_create', name='paquete_item_create'),

    url(r'^producto/new/$',
        ProductoConsumidoCreate.as_view(), name='productoconsumido_new'),





    url(r'^paquetes/pconsumido/list/$', ProductosConsumidos.as_view(),
        name='consumido'),

    url(r'^paquetes/detail/(?P<pk>\d+)/$', ProductoConsumidoDetail.as_view(),
        name='cons_detail'),





    url(r'^paquetes/salida/cancel/$', SalidaCancel.as_view(),
        name='cancel_list'),

    url(r'^(?P<pk>\d+)/pdf/$', SalidaPDF.as_view(), name='pdf'),

    url(r'^paquete/(?P<pk>\d+)/recibo/pdf/$',
        PaquetebillPDF.as_view(), name='paquete_recibo'),

)
