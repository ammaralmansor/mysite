from .models import *
from rest_framework import serializers


class AlbumSerializer(serializers.ModelSerializer):
    artist = serializers.StringRelatedField()

    class Meta:
        fields = '__all__'
        model = Album


class MusicianSerializer(serializers.ModelSerializer):
    AlbumSerializer(many=True, source='album_set')

    class Meta:
        fields = '__all__'
        model = Musician
        
class ListMusicianSerializer(serializers.ModelSerializer):
    albums = serializers.ListSerializer(child=AlbumSerializer(), source='album_set')

    class Meta:
        fields = '__all__'
        model = Musician
        
