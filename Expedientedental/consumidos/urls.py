from django.conf.urls import patterns, url
from consumidos.views import (
    Paquetes, PaqueteCreate, PaqueteDetail, PaqueteUpdate, Peticiones,
    PeticionesAtendidas, PeticionCreate, PeticionUpdate, PeticionCancel,
    ProductoConsumidoCreate, PeticionDetail, ReciboPeticionPDF,
    ProductosConsumidos, ProductoConsumidoDetail, PaqueteCancel,
    PaqueteCancelled, PaqueteCancelledDetail, PeticionCancelled
)

urlpatterns = patterns(
    'consumidos.views',

    url(r'^paquetes/$', Paquetes.as_view(), name='paquete_list'),

    url(r'^paquete/new/$', PaqueteCreate.as_view(), name='paquete_new'),

    url(r'^paquete/(?P<pk>\d+)/detail/$',
        PaqueteDetail.as_view(), name='paquete_detail'),

    url(r'^paquete/(?P<pk>\d+)/update/$',
        PaqueteUpdate.as_view(), name='paquete_edit'),

    url(r'^paquete/(?P<pk>\d+)/cancel/$',
        PaqueteCancel.as_view(), name='paquete_cancel'),

    url(r'^paquete/cancelled/$',
        PaqueteCancelled.as_view(), name='paquete_cancelled_list'),

    url(r'^paquete/cancelled/(?P<pk>\d+)/$',
        PaqueteCancelledDetail.as_view(), name='paquete_cancelled_detail'),

    url(r'^salidas/peticiones/$', Peticiones.as_view(), name='peticion_list'),

    url(r'^salidas/peticiones/surtido/$',
        PeticionesAtendidas.as_view(), name='peticion_surtido_list'),

    url(r'^clinica/peticion/servicio/(?P<pk>\d+)/new/$',
        PeticionCreate.as_view(), name='peticion_new'),

    url(r'^salidas/peticion/(?P<pk>\d+)/detail/$',
        PeticionDetail.as_view(), name='peticion_detail'),

    url(r'^salidas/peticion/(?P<pk>\d+)/insumos/add/$',
        'paquete_item_create', name='paquete_item_create'),

    url(r'^salidas/peticion/(?P<pk>\d+)/update/$',
        PeticionUpdate.as_view(), name='peticion_update'),

    url(r'^salidas/peticion/(?P<pk>\d+)/cancel/$',
        PeticionCancel.as_view(), name='peticion_cancel'),

    url(r'^salidas/peticiones/cancelled/$',
        PeticionCancelled.as_view(), name='peticiones_canceladas'),

    url(r'^salidas/producto/new/$',
        ProductoConsumidoCreate.as_view(), name='consumido_new'),

    url(r'^salidas/productos/$',
        ProductosConsumidos.as_view(), name='consumido_list'),

    url(r'^salidas/producto/detail/(?P<pk>\d+)/$',
        ProductoConsumidoDetail.as_view(), name='consumido_detail'),

    url(r'^salidas/paquete/(?P<pk>\d+)/recibo/pdf/$',
        ReciboPeticionPDF.as_view(
            template_name='peticion-pdf.html',
            header_template='headerpdf.html',
            footer_template='footerpdf.html'), name='recibo_paquete'),

)
