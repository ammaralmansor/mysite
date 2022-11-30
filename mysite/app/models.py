from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from datetime import datetime as dt 

<<<<<<< HEAD
class Category(models.Model):
    last           =    models.BooleanField(default=True)
    local          =    models.BooleanField(default=False)
    international  =    models.BooleanField(default=False)
    sport          =    models.BooleanField(default=False)

class Media(models.Model):
    Type_CHOICES = (
        ('Image', 'image'),
        ('Audio', 'audio'),
        ('Video', 'video'),
        ('NoMedia', 'nomedia'),
    )
    mdeia_url            =      models.ImageField(upload_to='images/%y/&m/%d',)
    media_type           =      models.CharField(max_length=20, choices=Type_CHOICES)  

=======

class Tracking(models.Model):
    createby    = models.ForeignKey(User , ondelete = models.CASCADE)
    createdon   = models.DateTimeField(auto_now=True)
    Modifiedby  = models.ForeignKey(User , ondelete = models.CASCADE)
    createdon   = models.DateTimeField(auto_now=True)



class AppRegisteration(models.Model):
    pass

    
>>>>>>> 7f5fc09b7043354248408ec369030009816c4340
class New(models.Model):
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
   


