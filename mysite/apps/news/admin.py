from django.contrib import admin
from apps.news.models import Category,Media,News


class Category_admin(admin.ModelAdmin):
    list_display = ['last', 'local','international' , 'sport']

admin.site.register(Category,Category_admin)


admin.site.register(Media)
admin.site.register(News)
