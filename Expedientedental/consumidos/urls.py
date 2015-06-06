from django.conf.urls import patterns, url
from consumidos.views import (
    Paquetes, PaqueteCreate, PaqueteDetail, PaqueteUpdate, Peticiones,
    PeticionesAtendidas, PeticionCreate, PeticionUpdate,
    ProductoConsumidoCreate, PeticionDetail, ReciboPeticionPDF,
    ProductosConsumidos, ProductoConsumidoDetail, PaqueteDeactivate,
    Deactivatedpack, PackDeactivateDetail
)

urlpatterns = patterns(
    'consumidos.views',

    url(r'^paquetes/$', Paquetes.as_view(), name='paquete_list'),

    url(r'^paquete/new/$', PaqueteCreate.as_view(), name='paquete_new'),

    url(r'^paquete/(?P<pk>\d+)/detail/$',
        PaqueteDetail.as_view(), name='paquete_detail'),

    url(r'^paquete/(?P<pk>\d+)/update/$',
        PaqueteUpdate.as_view(), name='paquete_edit'),

    url(r'^paquete/(?P<pk>\d+)/deactivate/$',
        PaqueteDeactivate.as_view(), name='paquete_deactivated'),

    url(r'^paquete/deactivated/list/$', Deactivatedpack.as_view(),
        name='deactivated-list'),

    url(r'^paquete/(?P<pk>\d+)/deactivated/detail/$',
        PackDeactivateDetail.as_view(), name='deactivated-detail'),

    url(r'^salidas/peticiones/$', Peticiones.as_view(), name='peticion_list'),

    url(r'^salidas/peticiones/surtido/$',
        PeticionesAtendidas.as_view(), name='peticion_surtido_list'),

    url(r'^clinica/peticion/servicio/(?P<pk>\d+)/new/$',
        PeticionCreate.as_view(), name='peticion_new'),

    url(r'^salidas/peticion/(?P<pk>\d+)/update/$',
        PeticionUpdate.as_view(), name='peticion_update'),

    url(r'^salidas/peticion/(?P<pk>\d+)/detail/$',
        PeticionDetail.as_view(), name='peticion_detail'),

    url(r'^salidas/peticion/(?P<pk>\d+)/insumos/add/$',
        'paquete_item_create', name='paquete_item_create'),

    url(r'^salidas/producto/new/$',
        ProductoConsumidoCreate.as_view(), name='consumido_new'),

    url(r'^salidas/productos/$',
        ProductosConsumidos.as_view(), name='consumido_list'),

    url(r'^salidas/producto/detail/(?P<pk>\d+)/$',
        ProductoConsumidoDetail.as_view(), name='consumido_detail'),

    url(r'^salidas/paquete/(?P<pk>\d+)/recibo/pdf/$',
        ReciboPeticionPDF.as_view(), name='recibo_paquete'),

)