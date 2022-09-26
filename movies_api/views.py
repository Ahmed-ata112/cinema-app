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


class MovieFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieItemSerializer
    queryset = models.MovieItem.objects.all()
    search_fields = ['movie_title', 'movie_genre', ]
    filterset_fields = ['movie_genre', 'movie_rating']
    filter_backends = (filters.SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend)


class CinemaFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CinemaItemSerializer
    queryset = models.CinemaItem.objects.all()
