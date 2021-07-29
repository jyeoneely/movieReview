from django.urls import path
from django.contrib.auth import views as auth_views
from movie import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),
]
