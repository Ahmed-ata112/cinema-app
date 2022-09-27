import django_filters
from movies_api import models


class MoviesFilter(django_filters.FilterSet):
    movie_title = django_filters.CharFilter(lookup_expr='icontains')
    movie_genres = django_filters.ModelMultipleChoiceFilter(
        field_name='movie_genres__genre_name',
        queryset=models.MovieGenre.objects.all(), to_field_name='genre_name')
    movie_rating = django_filters.NumberFilter(
        field_name='movie_rating', lookup_expr='gte')

    class Meta:
        model = models.MovieItem
        fields = ['movie_title', 'movie_genres', 'movie_rating']
