from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from Expedientedental.home.forms import *
from Expedientedental.home.models import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.db.models import Q
# Create your views here.

def index_view(request):



	return render_to_response('home/index.html',ctx ,context_instance = RequestContext(request))
