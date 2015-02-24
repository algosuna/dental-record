from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from historialprocedimientos.models import HistogramaItem,DateTime
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse




class HistogramaItemAdmin(admin.ModelAdmin):
    list_display = ["nombre", "prioridad", "dificultad", "inicio", "progreso_",
                    "delete", "onhold", "hecho"]
    list_filter = ["prioridad", "dificultad", "onhold", "hecho"]
    search_fields = ["nombre"]


class ItemInline(admin.TabularInline):
    model = HistogramaItem


class DateAdmin(admin.ModelAdmin):
    list_display = ["fecha"]
    inlines = [ItemInline]
    

    def response_add(self, request, obj, post_url_continue='../%s/'):
        """Determines the HttpResponse for the add_view stage."""
        opts = obj._meta
        pk_value = obj._get_pk_val()

        msg = "Item(s) were added successfully."
        # Here, we distinguish between different save types by checking for
        # the presence of keys in request.POST.
        if request.POST.has_key("_continue"):
            self.message_user(request, msg + ' ' + _("You may edit it again below."))
            if request.POST.has_key("_popup"):
                post_url_continue += "?_popup=1"
            return HttpResponseRedirect(post_url_continue % pk_value)

        if request.POST.has_key("_popup"):
            return HttpResponse(
              '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");'
              '</script>' % (escape(pk_value), escape(obj)))
        elif request.POST.has_key("_addanother"):
            self.message_user(request, msg + ' ' + (_("You may add another %s below.") %
                                                    force_unicode(opts.verbose_name)))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)

            for item in HistogramaItem.objects.filter(inicio__fecha=obj):
                if not item.user:
                    item.user = request.user
                    item.save()
            return HttpResponseRedirect(reverse("admin:historialprocedimientos_item_changelist"))


admin.site.register(HistogramaItem, HistogramaItemAdmin)
admin.site.register(DateTime, DateAdmin)