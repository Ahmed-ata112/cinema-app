from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.settings import api_settings
from movies_api import serializers
from movies_api import models


class MovieFeedViewSet(viewsets.ModelViewSet):
    '''Handle creating ,Reading and updating profile feed item'''

    serializer_class = serializers.MoviesFeedItemSerializer
    queryset = models.MovieFeedItem.objects.all()
