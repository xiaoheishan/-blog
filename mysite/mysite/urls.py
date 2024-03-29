"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from myblog import views
from myblog import api



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='myblog_index'),
    path('chakan/<int:id>/', views.chakan,name='myblog_chakan'), 
    path('api/index', api.indexData),

    # 后台CMS管理系统--程序 尽量少使用vuejs
    path('hsadmin/', include('hscms.urls')),
    #summernote富文本编辑器
    path('summernote/', include('django_summernote.urls')),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    # + static(settings.IMAGES_URL , document_root=settings.IMAGES_ROOT)
