# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from dbe.todo.models import *
from django.core.urlresolvers import reverse


def onhold_done(request, mode, action, pk):
    """Toggle Done / Onhold on/off."""
    item = Item.objects.get(pk=pk)

    if action == "on":
        if mode == "hecho": item.hecho = True
        elif mode == "onhold": item.onhold = True
    elif action == "off":
        if mode == "hecho": item.hecho = False
        elif mode == "onhold": item.onhold = False

    item.save()
    return HttpResponse('')

def progreso_(request, pk):
    """Set task progress."""
    p = request.POST
    if "progreso" in p:
        item = Item.objects.get(pk=pk)
        item.progress = int(p["progreso"])
        item.save()
    return HttpResponse('')

def item_action(request, action, pk):
    """Mark done, toggle onhold or delete a todo item."""
    if action == "hecho":
        item = Item.objects.get(pk=pk)
        item.done = True
        item.save()
    elif action == "onhold":
        item = Item.objects.get(pk=pk)
        if item.onhold:
            item.onhold = False
        else:
            item.onhold = True
        item.save()
    elif action == "delete":
        Item.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))
