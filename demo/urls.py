"""bookopedia URL Configuration"""



from django.contrib import admin
from django.urls import path
from django.urls import include
from demo import views

urlpatterns = [

    path('', views.index),


]
    
