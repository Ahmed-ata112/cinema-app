import django_filters
from movies_api import models
from django_filters import OrderingFilter


class MoviesFilter(django_filters.FilterSet):
    movie_title = django_filters.CharFilter(lookup_expr='icontains')
    movie_genres = django_filters.ModelMultipleChoiceFilter(
        field_name='movie_genres__genre_name',
        queryset=models.MovieGenre.objects.all(), to_field_name='genre_name')
    movie_rating = django_filters.NumberFilter(
        field_name='movie_rating', lookup_expr='gte')

    order = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('movie_rating', 'rating'),
        ),

        # labels do not need to retain order
        field_labels={
        }
    )

    class Meta:
        model = models.MovieItem
        fields = ['movie_title', 'movie_genres', 'movie_rating']


# class CinemaFilter(django_filters.FilterSet):
#     cinema_name = django_filters.CharFilter(
#         lookup_expr='icontains', field_name='cinema_name')

#     class Meta:
#         model = models.CinemaItem

#         fields = ['cinema_name']
