from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('register/', views.Index, name='register'),
    path('login/', views.Index, name='login'),
    path('ingredients/', views.Index, name='ingredients'),



]
