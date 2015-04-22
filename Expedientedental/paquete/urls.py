from django.conf.urls import patterns, url
from paquete.views import (EditPaqueteView, PaqueteC,
                           Pending, manage_paquetes)

urlpatterns = patterns('paquete.views',

    url(r'^pendientes/$', Pending.as_view()),
    url(r'^tipoPaquete/$', 'PaqueteItem'),
    url(r'^paquetes/$', PaqueteC),
    url(r'^paquetes/insumos/(?P<pk>\d+)/$', manage_paquetes, name='insumos'),
    url(r'^tipoPaquete/edit/(?P<pk>\d+)$', EditPaqueteView.as_view()),


)

urlpatterns += patterns('',
    # Reportes PDF
    # url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
