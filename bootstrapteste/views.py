from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return render_to_response('dino/index.html')
    return render(request, 'bootstrapteste/index.html')
