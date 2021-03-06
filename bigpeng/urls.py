"""bigpeng URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from bigpeng import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include(('user.urls','user'),namespace='user')),
    path('status/', include(('status.urls','status'),namespace='status')),
    path('news/', include(('news.urls','news'),namespace='news')),
    path('datas/', include(('datas.urls','datas'),namespace='datas')),
    path('control/', include(('control.urls','control'),namespace='control')),
    path('tinymce/',include('tinymce.urls')),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# 拼接图片的地址
# urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)