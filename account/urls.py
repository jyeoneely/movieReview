from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
]
