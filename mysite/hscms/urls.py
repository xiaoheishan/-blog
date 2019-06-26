from django.urls import path
from hscms import views

urlpatterns = [
    path('', views.index),
    path('list/', views.list),
    path('artical/<int:id>/', views.artical),
    # 发布文章
    path('fabu/', views.fabu),
    # 删除文章
    path('delete/<int:id>/', views.delete_artical, name='artical_delete'),
]