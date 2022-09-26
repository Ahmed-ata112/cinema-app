import django_filters
from movies_api import models


class MoviesFilter(django_filters.FilterSet):
    movie_title = django_filters.CharFilter(lookup_expr='icontains')
    movie_genre = django_filters.CharFilter(
        field_name='movie_genre', lookup_expr='iexact')
    movie_rating = django_filters.NumberFilter(
        field_name='movie_rating', lookup_expr='gte')

    class Meta:
        model = models.MovieItem
        fields = ['movie_title', 'movie_genre', 'movie_rating']
