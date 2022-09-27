from rest_framework import serializers
from movies_api import models

# serializer that is used to return a list of genres available


class MovieGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieGenre
        fields = ('genre_name',)


class MovieItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    # cinema = serializers.ManyRelatedField()
    movie_genre = serializers.SlugRelatedField(
        read_only=True,
        slug_field='genre_name'
    )
    
    class Meta:
        model = models.MovieItem
        fields = ('movie_title', 'movie_description',
                  'movie_image', 'movie_genre', 'movie_link_id', 'movie_rating', 'cinema')
        depth = 1


class CinemaItemSerializer(serializers.ModelSerializer):
    '''Serializer for feed items'''
    # movies is the related_name
    movies = MovieItemSerializer(many=True)

    class Meta:
        model = models.CinemaItem
        fields = ('cinema_name', 'cinema_link', 'movies')
