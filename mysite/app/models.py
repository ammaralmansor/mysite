from django.db import models
# Create your models here.
from django.contrib.auth.models import User


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
    mdeia_url = models.ImageField(upload_to=None)
    media_type = models.CharField(max_length=20, choices=Type_CHOICES)


class Tracking(models.Model):
    created_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name="createdby")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="modifiedby")
    modified_on = models.DateTimeField(auto_now=True)


class AppRegisteration(models.Model):
    pass


# >>>>>>> 7f5fc09b7043354248408ec369030009816c4340
class New(models.Model):
    PLATEFORM_CHOICES = (
        ('android', 'android'),
        ('ios', 'ios'),
    )
    LANGUAGE_CHOICES = (
        ('en', 'en'),
        ('ar', 'ar'),
        ('fr', 'fr'),
    )

    title = models.TextField(max_length=150, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discription = models.CharField(max_length=255)
    thumb = models.FileField(upload_to=None)
    fb_link = models.URLField(max_length=200)

    language_code = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=13, blank=True, default='en')
    
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    is_puplished = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    platform = models.TextField(
        max_length=1000, blank=False, choices=PLATEFORM_CHOICES)
