# banking/urls.py
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
