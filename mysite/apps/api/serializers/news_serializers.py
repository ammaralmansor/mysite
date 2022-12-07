from apps.news.models import News, Media,Category
from rest_framework import serializers
from rest_framework.relations import RelatedField

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
        
    def to_representation(self, data):
        data= {key:value for (key, value) in data.__dict__.items() if value == True}
        return super().to_representation(data)
        
# LIST_SERIALIZER_KWARGS = (
#     'read_only', 'write_only', 'required', 'default', 'initial', 'source',
#     'label', 'help_text', 'style', 'error_messages', 'allow_empty',
#     'instance', 'data', 'partial', 'context', 'allow_null'
# )
     

class NewsSerializer(serializers.ModelSerializer):
    "NewsSerializer"
    media_details = MediaSerializer(source='media' ,read_only=True )
    category_details = CategorySerializer(source='category' ,read_only=True )#allow_blank=True, max_length=100, required=False)
    media = serializers.FileField(required=True, write_only =True)
    
    class Meta:
        model = News
        fields = [
                'title',
                'discription',
                'category',
                'category_details',
                'fb_link',
                'thumb',
                'language_code',
                'is_puplished',
                'is_active',
                'platform',
                'media',
                'media_details',
        ]
        
        extra_kwargs = {
            'media_type' : {'write_only': True},
            'category': {'write_only': True},
                    }

