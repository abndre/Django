from django.urls import path

from . import views

app_name = 'dino'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('game', views.game, name='game'),
]
