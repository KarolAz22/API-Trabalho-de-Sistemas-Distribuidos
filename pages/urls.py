from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('details/<int:pk>', views.details, name='details'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('alter-monography/<int:pk>', views.alterMonograph, name='alter-monography'),
    path('monographs/', views.showAllMonographs, name="show-all-monographs"),
    path('users/', views.showAllUsers, name='show-all-users'),
]

