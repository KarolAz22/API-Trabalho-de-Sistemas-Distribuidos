"""projeto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from projeto1.api import viewsets as recordsviewset

route = routers.DefaultRouter()

route.register(r'register-monograph', recordsviewset.RecordsViewSet, basename ='monograph')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('records/', include('records.urls')),
    path('', include('pages.urls')),
    path('api/',include(route.urls))
]
