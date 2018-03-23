"""wechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from .views import CheckWeChat

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^taiga/', include('taiga.urls'), ),
    url('^webhook/', include('webhook.urls'), ),
    url('^check$', CheckWeChat.as_view({'get': 'get'}), ),
]

if getattr(settings, 'SHOW_DOCS', False):
    urlpatterns.append(url('^docs', get_swagger_view('接口文档'), ))
