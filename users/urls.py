from django.contrib import admin
from django.views.static import serve
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]