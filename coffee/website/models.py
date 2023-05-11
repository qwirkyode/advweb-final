from django.db import models

# Create your models here.
from django.db import models
from django import forms


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Message: {self.message}"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'