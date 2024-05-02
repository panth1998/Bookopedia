from django import views
from django.contrib import admin
from django.urls import URLPattern, path
from django.urls import include

from .views import BaseRegisterView, UserLoginView
from User import views

app_name = 'User_urls'

urlpatterns = [ 
    path('registration/', BaseRegisterView.as_view(), name='registration'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('', views.index),



]