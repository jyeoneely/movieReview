from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'community'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.detail, name='detail')

]
