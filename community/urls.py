from django.urls import path
from django.contrib.auth import views as auth_views
from community import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index')
]
