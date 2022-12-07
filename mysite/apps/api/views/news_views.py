from apps.news.models import News
from apps.api.serializers.news_serializers import NewsSerializer
from django.http.response import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets 
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser 

class CreateListNewsViewSet(ListCreateAPIView ,viewsets.GenericViewSet):
    "a"
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    
    
    # def get_queryset(self, category ):
        
        # return self.queryset.filter(category__local=True)
        
    def get(self, request, *args, **kwargs):
        print(self.get_queryset().filter(category__local=True))
        serializer ={'local': self.get_serializer(self.get_queryset().filter(category__local=True), many=True).data,
                     'international':self.get_serializer(self.get_queryset().filter(category__international=True),many=True).data,
                     'sport':self.get_serializer(self.get_queryset().filter(category__sport=True),many=True).data}

        return Response(serializer)
        
        
        # data = {
        #     local : self. 
        # }
    

    def post(self, request, *args, **kwargs):
        super().Post(self, request, *args, **kwargs)
        


