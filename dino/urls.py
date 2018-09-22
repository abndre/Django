from django.urls import path

from . import views

app_name = 'dino'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('login', views.login, name='Login')
]
