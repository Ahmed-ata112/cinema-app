from re import search
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.settings import api_settings
from movies_api import serializers
from movies_api import models
from rest_framework.response import Response
from rest_framework import permissions
from movies_api.filters import MoviesFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class MovieFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieItemSerializer
    queryset = models.MovieItem.objects.all()
    search_fields = ['movie_title', 'movie_genre__genre_name', ]
    filter_backends = (filters.SearchFilter,
                       DjangoFilterBackend)
    filterset_class = MoviesFilter


class CustomSearchFilter(filters.SearchFilter):
    def filter_queryset(self, request, queryset, view):
        # to Return only the first 5 results in Search results
        return super().filter_queryset(request, queryset, view)[:5]


class CinemaFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CinemaItemSerializer
    queryset = models.CinemaItem.objects.all()
    filter_backends = (CustomSearchFilter,)
    search_fields = ['cinema_name', ]


class GenresViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieGenreSerializer
    queryset = models.MovieGenre.objects.all()

    def list(self, request, *args, **kwargs):
        lis = self.queryset.values_list('genre_name', flat=True)
        return Response(lis)
