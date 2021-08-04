from django.urls import path
from django.contrib.auth import views as auth_views
from master import views

app_name = 'master'
urlpatterns = [
    path('', views.index, name='index'),
    path('master', views.master, name='master'),       # :8000/master/master
]
