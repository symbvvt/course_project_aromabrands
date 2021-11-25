from django.urls import path
from . import views

urlpatterns = [

    path('first', views.first),
    path('second', views.second),
    path('third', views.third),
    path('home', views.home),
    path('men', views.men),
    path('women', views.women),
    path('aboutus', views.aboutus),
]