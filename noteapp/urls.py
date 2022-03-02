from django.contrib import admin
from django.views.static import serve
from django.urls import path, re_path
from . import views
from mysite import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('note/<int:id>/', views.note, name='note'),
    re_path('^static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}),

]

handler404 = 'noteapp.views.handle_not_found'