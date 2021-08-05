from django.urls import path
from django.contrib.auth import views as auth_views
from master import views

app_name = 'master'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('master', views.master, name='master'),       # :8000/master/master
    path('movies', views.movies, name='movies'),
    path('users', views.users, name='users'),
]
