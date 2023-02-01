# Create your views here.
from django.shortcuts import render
from .models import About
from datetime import datetime
# Create your views here.

def about(request):
    abouts = About.objects.all()
   
    return render(request, 'about/about.html', {'abouts':abouts})