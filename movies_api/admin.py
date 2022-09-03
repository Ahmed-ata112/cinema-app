from django.contrib import admin
from movies_api import models

# Register your models here.
admin.site.register(models.MovieItem)
admin.site.register(models.CinemaItem)
