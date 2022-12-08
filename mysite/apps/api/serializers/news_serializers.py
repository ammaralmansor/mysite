from apps.news.models import News, Media,Category
from rest_framework import serializers
from rest_framework.relations import RelatedField

from django.contrib.auth import get_user_model
User = get_user_model()

class MediaSerializer(serializers.ModelSerializer):
    "MediaSerializer"
    media_url = serializers.FileField(required=True)
    
    class Meta:
        model = Media
        fields =  ['media_url','media_type']

# from rest_framework.fields import (  # NOQA # isort:skip
#     CreateOnlyDefault, CurrentUserDefault, SkipField, empty
# )


class CategorySerializer(serializers.ModelSerializer):
    "CategorySerializer"
    
    class Meta:
        model = Category
        fields =  ['id','last', 'local','international' , 'sport']  
 
        
# LIST_SERIALIZER_KWARGS = (
#     'read_only', 'write_only', 'required', 'default', 'initial', 'source',
#     'label', 'help_text', 'style', 'error_messages', 'allow_empty',
#     'instance', 'data', 'partial', 'context', 'allow_null'
# )
     

class NewsSerializer(serializers.ModelSerializer):
    "NewsSerializer"
    media_file = serializers.FileField( write_only =True)
    media_type = serializers.CharField( write_only =True)

    #readonly attributes
    media_details = MediaSerializer(source='media',read_only=True)
    category_details = CategorySerializer(source='category' ,read_only=True )#allow_blank=True, max_length=100, required=False)
        
    class Meta:
        model = News
        fields = [
                'title',
                'discription',
                'category',
                'fb_link',
                'thumb',
                'language_code',
                'platform',
                
                'media_file',
                'media_type',
                
                #readonly attributes
                'category_details',
                'media_details',
        ]
        
        extra_kwargs = {
            'category': {'write_only': True},
                    }


    def create(self, validated_data):
        
        media_file = validated_data . pop('media_file')
        media_type = validated_data . pop('media_type')
        
        media_instance = Media.objects.create(media_url= media_file ,media_type= media_type)

        validated_data['media'] = media_instance
        validated_data['created_by'] = User.objects.get(id=1)####
        validated_data['modified_by'] = User.objects.get(id=1)####
                
        news_instance = (self.Meta.model).objects.create(**validated_data)

        return news_instance
