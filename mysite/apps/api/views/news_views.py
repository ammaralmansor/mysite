from apps.news.models import News
from apps.api.serializers.news_serializers import NewsSerializer
from django.http.response import JsonResponse,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, viewsets 
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser 

class CreateListNewsViewSet(ListCreateAPIView, viewsets.GenericViewSet):
    "a"
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = []
    category_field = [ 'category__local','category__international' , 'category__sport']
    
    # def get_queryset(self, category ):
        # return self.queryset.filter(category__local=True)
        
    def get(self, request, *args, **kwargs):
        qs = super().get_queryset( *args, **kwargs)
        
        #convert lookup_data to a list of tuples to filter according to each tuble
        lookup_data=dict.fromkeys(self.category_field, True)  
        lookup_data = list(lookup_data.items())
        
        serializer={}
        for i in range(0,3):
            serializer[lookup_data[i][0].split('_')[2]]= self.get_serializer(qs.filter(lookup_data[i]), many=True).data

        return Response(serializer)



