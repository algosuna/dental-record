from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^search/$', views.busqueda, name='producto_search'),

    url(r'^productos/$', views.Productos.as_view(), name='producto_list'),
    url(r'^producto/new/$',
        views.ProductoCreate.as_view(), name='producto_create'),
    url(r'^producto/(?P<pk>\d+)/edit/$',
        views.ProductoUpdate.as_view(), name='producto_update'),
    url(r'^producto/(?P<pk>\d+)/detail/$',
        views.ProductoDetail.as_view(), name='producto_detail'),
    url(r'^producto/(?P<pk>\d+)/cancel/$',
        views.ProductoCancel.as_view(), name='producto_cancel'),
    url(r'^productos/cancelled/$',
        views.ProductosCancelled.as_view(), name='productos_cancelados'),
    url(r'^producto/cancelled/(?P<pk>\d+)/$',
        views.ProductoCancelDetail.as_view(), name='productocancelado_detail'),

    url(r'^entradas/$',
        views.EntradaList.as_view(), name='entradas'),
    url(r'^entrada/(?P<pk>\d+)/$',
        views.EntradaDetail.as_view(), name='entrada_detail'),
    url(r'^producto/(?P<pk>\d+)/entrada/$',
        views.EntradaProducto.as_view(), name='entradas_producto'),
    url(r'^entradas/cancelled/$',
        views.EntradasCancelledList.as_view(), name='entradas_canceladas'),
    url(r'^entrada/(?P<pk>\d+)/cancel/$',
        views.EntradaCancel.as_view(), name='entrada_cancel'),
    url(r'^entrada/cancelled/(?P<pk>\d+)/$',
        views.EntradaCancelDetail.as_view(), name='entradacancelada_detail'),

    url(r'^unidades/$', views.Unidades.as_view(), name='unidades'),
    url(r'^unidad/new/$', views.UnidadCreate.as_view(), name='unidad_create'),

    url(r'^productos/pdf/$',
        views.ProductosPDF.as_view(), name='productos_pdf'),

    url(r'^producto/(?P<pk>\d+)/pdf/$',
        views.ProductoPdf.as_view(), name='producto_pdf'),

    url(r'^producto/cancelled/(?P<pk>\d+)/pdf/$',
        views.ProductoCanceladoPDF.as_view(), name='producto_cancelado_pdf'),

    url(r'^entradas/pdf/$',
        views.EntradasPDF.as_view(), name='entradas_pdf'),

    url(r'^entrada/(?P<pk>\d+)/pdf/$',
        views.EntradaPDF.as_view(), name='entrada_pdf'),

    url(r'^entradas/cancelled/pdf/$',
        views.EntradasCanceladasPDF.as_view(), name='entradas_canceladas_pdf'),
    url(r'^entrada/cancelled/(?P<pk>\d+)/pdf/$',
        views.EntradaCanceladaPDF.as_view(), name='entrada_cancelada_pdf'),
]
