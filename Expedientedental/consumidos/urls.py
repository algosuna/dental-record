from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^paquetes/$', views.Paquetes.as_view(), name='paquete_list'),

    url(r'^paquete/new/$', views.PaqueteCreate.as_view(), name='paquete_new'),

    url(r'^paquete/(?P<pk>\d+)/detail/$',
        views.PaqueteDetail.as_view(), name='paquete_detail'),

    url(r'^paquete/(?P<pk>\d+)/update/$',
        views.PaqueteUpdate.as_view(), name='paquete_edit'),

    url(r'^paquete/(?P<pk>\d+)/cancel/$',
        views.PaqueteCancel.as_view(), name='paquete_cancel'),

    url(r'^paquete/cancelled/$',
        views.PaqueteCancelled.as_view(), name='paquete_cancelled_list'),

    url(r'^paquete/cancelled/(?P<pk>\d+)/$',
        views.PaqueteCancelledDetail.as_view(),
        name='paquete_cancelled_detail'),

    url(r'^salidas/peticiones/$',
        views.Peticiones.as_view(), name='peticion_list'),

    url(r'^salidas/peticiones/surtido/$',
        views.PeticionesAtendidas.as_view(), name='peticion_surtido_list'),

    url(r'^clinica/peticion/servicio/(?P<pk>\d+)/new/$',
        views.PeticionCreate.as_view(), name='peticion_new'),

    url(r'^salidas/peticion/(?P<pk>\d+)/detail/$',
        views.PeticionDetail.as_view(), name='peticion_detail'),

    url(r'^salidas/peticion/(?P<pk>\d+)/insumos/add/$',
        views.paquete_item_create, name='paquete_item_create'),

    url(r'^salidas/peticion/(?P<pk>\d+)/update/$',
        views.PeticionUpdate.as_view(), name='peticion_update'),

    url(r'^salidas/peticion/(?P<pk>\d+)/cancel/$',
        views.PeticionCancel.as_view(), name='peticion_cancel'),

    url(r'^salidas/peticiones/cancelled/$',
        views.PeticionCancelled.as_view(), name='peticiones_canceladas'),

    url(r'^salidas/producto/new/$',
        views.ProductoConsumidoCreate.as_view(), name='consumido_new'),

    url(r'^salidas/productos/$',
        views.ProductosConsumidos.as_view(), name='consumido_list'),

    url(r'^salidas/producto/detail/(?P<pk>\d+)/$',
        views.ProductoConsumidoDetail.as_view(), name='consumido_detail'),

    url(r'^salidas/paquete/(?P<pk>\d+)/recibo/pdf/$',
        views.ReciboPeticionPDF.as_view(), name='recibo_paquete'),

]
