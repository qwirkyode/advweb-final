from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Contact, ContactForm

def index(request):
  if request.method == "POST":
    contact = ContactForm(request.POST)
    if contact.is_valid():
        contact.save()
        return HttpResponseRedirect("/index.html")
  else:
      contact = ContactForm()
  
  contacts = Contact.objects.all()
  return render(request, "index.html", {"contacts": contacts})

def about(request):
  return render(request, "about.html")

def blog(request):
  return render(request, "blog.html")

def coffees(request):
  return render(request, "coffees.html")

def contact(request):
  return render(request, "contact.html")

