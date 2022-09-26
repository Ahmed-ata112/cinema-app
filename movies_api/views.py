from re import search
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.settings import api_settings
from movies_api import serializers
from movies_api import models
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import filters
import django_filters.rest_framework

from movies_api.filters import MoviesFilter


class MovieFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieItemSerializer
    queryset = models.MovieItem.objects.all()
    search_fields = ['movie_title', 'movie_genre__genre_name', ]
    filter_backends = (filters.SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend)
    filterset_class = MoviesFilter


class CinemaFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CinemaItemSerializer
    queryset = models.CinemaItem.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['cinema_name', ]


class GenresViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieGenreSerializer
    queryset = models.MovieGenre.objects.all()
