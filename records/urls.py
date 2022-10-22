from django import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  path('authors' , views.registerOfAuthors, name='authors'),
  path('co-authors' , views.registerOfCoAdvisor, name='co-authors'),
  path('students' , views.registerOfStudents, name='students'),
  path('monographs' , views.registerOfmonographs, name='monographs'),
  ]