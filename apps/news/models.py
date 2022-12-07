from django.db import models
from apps.common.models import Auditable


class Category(models.Model):

    last = models.BooleanField(default=True)
    local = models.BooleanField(default=False)
    international = models.BooleanField(default=False)
    sport = models.BooleanField(default=False)


class Media(models.Model):
    MEDIA_TYPE = (
        ('Image', 'image'),
        ('Audio', 'audio'),
        ('Video', 'video'),
        ('NoMedia', 'nomedia'),
    )
    media_url = models.FileField(upload_to=None)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE)


class News(Auditable):
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
    discription = models.CharField(max_length=255)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    
    fb_link = models.URLField(max_length=200)
    thumb = models.FileField(upload_to=None)
    language_code = models.CharField(choices=LANGUAGE_CHOICES, max_length=13, blank=True, default='en')

    is_puplished = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    platform = models.TextField(max_length=1000, blank=False, choices=PLATEFORM_CHOICES)
    
    class Meta:
        verbose_name_plural = "News"
        
        
