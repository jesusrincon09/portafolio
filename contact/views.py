from django.shortcuts import render
from .models import Contact
from datetime import datetime
# Create your views here.

def contact(request):
    contacts = Contact.objects.all()
  
    return render(request, 'contact/contact.html', {'contacts':contacts})