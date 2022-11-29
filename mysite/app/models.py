from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from datetime import datetime as dt 
class New(models.Model):
   CATEGORY_CHOICES = (
        ('last', 'last'),
        ('local', 'local'),
        ('international', 'international'),
        ('sport', 'sport'),
    )
   LANGUAGE_CHOICES = (
        ('en', 'en'),
        ('ar', 'ar'),
        ('fr', 'fr'),
    )
   lang  = models.CharField(choices=LANGUAGE_CHOICES, max_length=13, blank=True, default='en')
   category = models.CharField(choices=CATEGORY_CHOICES, max_length=13, blank=True, default='last')
   title = models.TextField(max_length=150,blank=False)
   creation_datetime = models.DateTimeField(auto_now=True)
   img_1 = models.ImageField(upload_to='images/%y/&m/%d')
   img_2 = models.ImageField(upload_to='images/%y/&m/%d')
   img_3 = models.ImageField(upload_to='images/%y/&m/%d')

   details = models.TextField(max_length=1000,blank=False)
   


