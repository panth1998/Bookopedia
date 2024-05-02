from re import template
from django.shortcuts import render
from django.forms import models 
from django.template import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Books



# Create your views here.
class AddBook(CreateView):
    model = Books
    fields = '__all__'
    template_name = 'crud/add_Books.html'
    success_url = '/crud/view'

class viewBooks(ListView): 
       model = Books
       Books = model.objects.all()
       context_object_name = 'Books'
       template_name='crud/view_Books.html'

class DetailBooks(DetailView):
    model = Books
    context_object_name = 'Books'
    template_name = 'crud/detail_Books.html'

class DeleteBooks(DeleteView):
    model = Books
    template_name = 'crud/delete_Books.html'
    success_url = '/crud/view'

class UpdateBooks(UpdateView):
    model = Books
    fields = '__all__'
    template_name = 'crud/update_Books.html'
    success_url = '/crud/view'
