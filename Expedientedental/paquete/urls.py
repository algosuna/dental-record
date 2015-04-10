from django.conf.urls import patterns, url
from paquete.views import PaquetesPDF, ReportarPaquete, busqueda,\
EditPaqueteView, PaqueteC

urlpatterns = patterns('paquete.views',

    
    url(r'^tipoPaquete/$', 'PaqueteItem'),
    url(r'^paquetes/$', 'PaqueteC'),   
    url(r'^tipoPaquete/edit/(?P<pk>\d+)$',EditPaqueteView.as_view()),
    url(r'^detalle/$',ReportarPaquete),
    url(r'^pack/detalles/$',busqueda),
    

)

urlpatterns += patterns('',

    #Reportes PDF
    url(r'^paquetes/pdf/$',PaquetesPDF.as_view()),
)
