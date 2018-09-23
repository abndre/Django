from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Player

def index(request):
    return render(request, 'dino/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dino:login')
    else:
        form = UserCreationForm()
    return render(request, 'dino/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in User
            return redirect('dino:game')
    else:
        form = AuthenticationForm()
    return render(request, 'dino/login.html',{'form':form})

def game(request):
    return render(request, 'dino/game.html')


def vote(request, question_id):
    pass
