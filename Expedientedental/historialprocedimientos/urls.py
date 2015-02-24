from django.conf.urls.defaults import *

urlpatterns = patterns('dbe.historialprocedimientos.views',
    (r"^item_action/(hecho|delete|onhold)/(\d*)/$", "item_action"),
    (r"^progreso/(\d*)/$", "progreso"),
    (r"^onhold_done/(onhold|hecho)/(on|off)/(\d*)/$", "onhold_done"),
)