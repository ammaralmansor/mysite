"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from app.views import index

from rest_framework import routers

from apps.api.views.news_views import CreateListNewsViewSet
from music.views import List

router = routers.DefaultRouter()
router.register('music', List, basename="music")


# SwaggerUIRenderer.template = 'swagger-ui.html'

news_list_view = CreateListNewsViewSet.as_view({'get': 'get'})
# news_create_view = CreateListNewsViewSet.as_view({'post': 'post'})

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', news_list_view),
    # path('', news_create_view),
    
            
    path('l' , index , name="index" )
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)