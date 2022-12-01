from django.db import models
# Create your models here.
from django.contrib.auth.models import User

from datetime import datetime as dt


class Category(models.Model):
    last = models.BooleanField(default=True)
    local = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    sport = models.BooleanField(default=False)


class Media(models.Model):
    Type_CHOICES = (
        ('Image', 'image'),
        ('Audio', 'audio'),
        ('Video', 'video'),
        ('NoMedia', 'nomedia'),
    )
    mdeia_url = models.ImageField(upload_to='images/%y/&m/%d',)
    media_type = models.CharField(max_length=20, choices=Type_CHOICES)


class Tracking(models.Model):
    createby = models.ForeignKey(User, related_name="create_relation" ,on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now=True)
    Modifiedby = models.ForeignKey(User,related_name="modify_relation" , on_delete=models.CASCADE)
    createdon = models.DateTimeField(auto_now=True)


class AppRegisteration(models.Model):
    pass


class New(models.Model):
    LANGUAGE_CHOICES = (('en', 'en'), ('ar', 'ar'), ('fr', 'fr'))
    PLATFORM_CHOICES = (('iso', 'iso'), ('android', 'android'))
    title = models.TextField(max_length=150, blank=False)
    lang = models.CharField(choices=LANGUAGE_CHOICES,
                            max_length=13, blank=True, default='en')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=False)
    Thumb = models.FileField(upload_to=None, max_length=100)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    FB_link = models.URLField(max_length=200)
    ispublished = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    platform = models.CharField(choices=LANGUAGE_CHOICES,
                                max_length=7, blank=False, default='ios')
