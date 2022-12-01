from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(New)
admin.site.register(Category)
admin.site.register(Tracking)
admin.site.register(Media)
