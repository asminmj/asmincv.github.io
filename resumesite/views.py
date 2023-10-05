from django.shortcuts import render
from . import urls 

def home(request):
    return render(request, 'home.html', {})