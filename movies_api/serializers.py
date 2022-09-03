from rest_framework import serializers
from movies_api import models


class MovieItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''

    class Meta:
        model = models.MovieItem
        fields = ('movie_title', 'movie_description',
                  'movie_image', 'movie_genre', 'movie_link_id', 'movie_rating', 'cinema_id')


class CinemaItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    # movies is the related_name
    movies = MovieItemSerializer(many=True)

    class Meta:
        model = models.CinemaItem
        fields = ('cinema_name', 'movies')
