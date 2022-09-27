from tkinter import CASCADE
from django.db import models
from django.conf import settings

# Create your models here.


class MovieGenre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre_name


class CinemaItem(models.Model):
    cinema_name = models.CharField(max_length=50)
    cinema_link = models.CharField(max_length=50)

    def __str__(self):
        '''return Model as String '''
        return self.cinema_name

# python manage.py migrate --run-syncdb


class MovieItem(models.Model):
    movie_title = models.CharField(unique=True,
                                   max_length=500, null=False)
    movie_image = models.TextField()
    movie_description = models.TextField()
    movie_genres = models.ManyToManyField(
        MovieGenre,  related_name='genres')

    movie_link_id = models.CharField(max_length=20)
    movie_rating = models.FloatField()
    cinema = models.ManyToManyField(
        CinemaItem,  related_name='movies')

    def __str__(self):
        '''return Model as String '''
        return self.movie_title
