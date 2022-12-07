from apps.news.models import News
from .serializers import *
from django.http.response import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets 
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser 

class List(ListCreateAPIView ,viewsets.GenericViewSet):
    queryset = Musician.objects.all()
    serializer_class = ListMusicianSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    