from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index')
]
