"""bookopedia URL Configuration"""



from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import AddBook
from .views import viewBooks, DetailBooks, DeleteBooks, UpdateBooks

urlpatterns = [

    path('add/',AddBook.as_view(),name='add_Books'),
    path('view/',viewBooks.as_view(),name='view_Books'),
    path('detail/<int:pk>/',DetailBooks.as_view(),name='detail_Books'),
    path('delete/<int:pk>/',DeleteBooks.as_view(),name='delete_Books'),
    path('update/<int:pk>/',UpdateBooks.as_view(),name='update_Books'),
    
    

]
    
