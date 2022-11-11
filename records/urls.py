from django import views
from django.urls import path
from . import views

urlpatterns = [
  path('register-authors/', views.registerOfAuthors, name='register-authors'),
  path('register-co-advisor/', views.registerOfCoAdvisor, name='register-co-advisor'),
  path('register-advisor/', views.registerOfAdvisor, name='register-advisor'),
  path('register-student/', views.registerOfStudent, name='register-student'),
  path('register-monograph/', views.registerOfmonographs, name='register-monograph'),
  path('alter-author/<int:pk>', views.alterAuthor, name='alter-author'),
  path('alter-advisor/<int:pk>', views.alterAdvisor, name='alter-advisor'),
  path('alter-coadvisor/<int:pk>', views.alterCoAdvisor, name='alter-coadvisor'),
  path('alter-student/<int:pk>',views.alterStudent, name='alter-student'),
  path('delete-author/<int:pk>', views.deleteAuthor, name='delete-author'),
  path('delete-advisor/<int:pk>', views.deleteAdvisor, name='delete-advisor'),
  path('delete-coadvisor/<int:pk>', views.deleteCoadvisor, name='delete-coadvisor'),
  path('delete-student/<int:pk>', views.deleteStudent, name='delete-student'),
  ]