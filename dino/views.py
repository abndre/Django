from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render_to_response

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
