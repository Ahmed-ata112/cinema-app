from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.settings import api_settings
from movies_api import serializers
from movies_api import models
from rest_framework.response import Response
from rest_framework import permissions


class MovieFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.MovieItemSerializer
    queryset = models.MovieItem.objects.all()


class CinemaFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.CinemaItemSerializer
    queryset = models.CinemaItem.objects.all()
