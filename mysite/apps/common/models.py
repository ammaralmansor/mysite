from django.db import models
from django.conf import settings


class Auditable(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="modified_by")
    modified_on = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True    


class AppRegisteration(models.Model):
    LANGUAGE_CHOICES = (
        ('en', 'en'),
        ('ar', 'ar'),
        ('fr', 'fr'),
    )
    OPERATOR_CHOICES = (
        ('MTC', 'MTC'),
        ('Touch', 'Touch'),
    )
    PLATEFORM_CHOICES = (
        ('android', 'android'),
        ('ios', 'ios'),
    )
    MobileNumber = models.IntegerField()
    operator = models.TextField(max_length=5, blank=False, choices=OPERATOR_CHOICES)
    AllNotification = models.BooleanField(default=False)
    ImageNotification = models.BooleanField(default=False)
    VideoNotification = models.BooleanField(default=False)
    AudioNotification = models.BooleanField(default=False)
    platform = models.TextField(max_length=1000, blank=False, choices=PLATEFORM_CHOICES)
    language_code = models.CharField(choices=LANGUAGE_CHOICES ,  max_length=13 , blank=True, default='en')
    FirebaseToken = models.CharField(max_length=100 , default=None)
