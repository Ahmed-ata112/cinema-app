from rest_framework import serializers
from movies_api import models


class MovieItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    class Meta:
        model = models.MovieItem
        fields = ('id', 'movie_title', 'movie_description',
                  'movie_image', 'movie_genre', 'movie_link_id', 'movie_rating',)


class CinemaItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    class Meta:
        model = models.CinemaItem
        fields = ('id', 'cinema_name',)
