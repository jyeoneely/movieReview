from django.urls import path
from django.contrib.auth import views as auth_views
from review import views

app_name = 'review'
urlpatterns = [
    path('', views.index, name='index')
]
