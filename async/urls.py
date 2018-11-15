"""async URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import  url
from django.urls import path
from thread.views import *

urlpatterns = [
    path('',index, name='index'),
    path('startThread',startThreadTask, name='startThreadTask'),
    url(r'^checkThread/(?P<id>[0-9]+)/?$',checkThreadTask, name='checkThreadTask'),
    path('admin/', admin.site.urls),
]
