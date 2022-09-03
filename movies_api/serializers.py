from rest_framework import serializers
from movies_api import models


class MoviesFeedItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    class Meta:
        model = models.MovieFeedItem
        fields = ('id', 'movie_title', 'movie_description',
                  'movie_image', 'movie_genre', 'movie_link_id', 'movie_rating',)
