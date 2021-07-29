from django.urls import path
from django.contrib.auth import views as auth_views
from review import views

app_name = 'review'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.load_list, name='list'),                       # 홈(리뷰목록)
    path('create/', views.reviewCreate, name='create'),           # 리뷰등록
    path('modify/<int:pk>/', views.reviewModify, name='modify'),  # 리뷰수정
    path('delete/<int:pk>/', views.reviewDelete, name='delete'),  # 리뷰삭제
    path('detail/<int:pk>/', views.reviewDetail, name='detail'),  # 리뷰상세조회
]
