from django.db import models
from django.conf import settings

# Create your models here.


class MovieFeedItem(models.Model):
    movie_title = models.CharField(max_length=500)
    movie_image = models.TextField()
    movie_description = models.TextField()
    movie_genre = models.CharField(max_length=20)
    movie_link_id = models.CharField(max_length=20)
    movie_rating = models.FloatField()
    
    
    def __str__(self):
        '''return Model as String '''
        return self.movie_title

