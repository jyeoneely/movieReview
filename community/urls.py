from django.urls import path
from django.contrib.auth import views as auth_views
from community import views

app_name = 'community'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.boardView, name="boardView"),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('write/', views.writePageView, name='write'),

]
