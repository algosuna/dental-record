from django.conf.urls import patterns, url
from paquete.views import ReportarPaquete, busqueda, EditPaqueteView,PaqueteC,\
 Pending

urlpatterns = patterns('paquete.views',

    url(r'^pendientes/$',Pending.as_view()),
    url(r'^tipoPaquete/$', 'PaqueteItem'),
    url(r'^paquetes/', PaqueteC),    
    url(r'^paquetes/matreq/', PaqueteC),
    url(r'^tipoPaquete/edit/(?P<pk>\d+)$',EditPaqueteView.as_view()),
    url(r'^detalle/$',ReportarPaquete),
    
    

)

urlpatterns += patterns('',

    #Reportes PDF
    #url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
