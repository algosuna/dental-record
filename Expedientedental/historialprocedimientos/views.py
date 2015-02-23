# Create your views here.
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class DateAdmin(admin.ModelAdmin):
    list_display = ["datetime"]
    inlines = [ItemInline]

    def response_add(self, request, obj, post_url_continue='../%s/'):
        """ Determines the HttpResponse for the add_view stage.  """
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

            return HttpResponseRedirect(reverse("admin:todo_item_changelist"))



	@staff_member_required
	def mark_done(request, pk):
	    item = histogramaItem.objects.get(pk=pk)
	    item.done = True
	    item.save()
	    return HttpResponseRedirect(reverse("admin:histograma_item_changelist"))
	    
	@staff_member_required
	def item_action(request, action, pk):
	    """Mark done, toggle onhold or delete a todo item."""
	    if action == "done":
	        item = Item.objects.get(pk=pk)
	        item.done = True
	        item.save()
	    elif action == "onhold":
	        item = Item.objects.get(pk=pk)
	        if item.onhold: item.onhold = False
	        else: item.onhold = True
	        item.save()
	    elif action == "delete":
	        Item.objects.filter(pk=pk).delete()

	    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))

   def onhold_done(request, mode, action, pk):
        """Toggle Done / Onhold on/off."""
        item = Item.objects.get(pk=pk)

        if action == "on":
            if mode == "done": item.done = True
            elif mode == "onhold": item.onhold = True
        elif action == "off":
            if mode == "done": item.done = False
            elif mode == "onhold": item.onhold = False

            item.save()
            return HttpResponse('')

    def progress(request, pk):
        """Set task progress."""
        p = request.POST
        if "progress" in p:
            item = Item.objects.get(pk=pk)
            item.progress = int(p["progress"])
            item.save()
        return HttpResponse('')
   