from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'), #영화 목록 페이지
    path('<int:pk>', views.detailview, name='detail'), #영화 상세 페이지
    path('create', views.createview, name='create'), #영화 등록 페이지
    path('modify/<int:pk>', views.modifyview, name='modify'), #영화 수정 페이지
    path('delete/<int:pk>', views.delete, name='delete'), #영화 삭제 (링크)
]
