import re
from django.shortcuts import render

# Create your views here.
def addbook(request):
        return render(request,'book/book.html')

def index(request):
        return render(request, 'user/book.html')

def index(request):
        return render(request,'')

