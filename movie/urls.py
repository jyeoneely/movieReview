from django.urls import path

from . import views

app_name = "movie"
urlpatterns = [
    path('', views.index),
    path('/movie', views.listview),
    
]