from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('authors' , views.registerOfAuthors, name='authors'),
  path('co-advisor' , views.registerOfCoAdvisor, name='co-advisor'),
  path('advisor/', views.registerOfAdvisor, name='advisor'),
  path('students' , views.registerOfStudents, name='students'),
  path('monographs' , views.registerOfmonographs, name='monographs'),
  ]