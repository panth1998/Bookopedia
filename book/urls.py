"""bookopedia URL Configuration"""



from django.contrib import admin
from django.urls import path
from django.urls import include
from book import views

urlpatterns = [

    path('addbook/',views.addbook),
    


]
    
