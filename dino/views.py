from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.contrib.auth.forms import UserCreationForm

from .models import Player

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return render_to_response('dino/index.html')
    return render(request, 'dino/index.html')
# Create your views here.
#class IndexView(generic.ListView):
#    template_name = 'dino/index.html'
#    def get_queryset(self):
#        return HttpResponse("Hello, world. You're at the polls index.")
#    #template_name = 'dino/index.html'

def login(request):
    form = UserCreationForm()
    #form = 
    return render(request, 'dino/Login.html',{'form':form})

def vote(request, question_id):
    pass
