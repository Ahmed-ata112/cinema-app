from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies_api import views


router = DefaultRouter()
router.register('movies', views.MovieFeedViewSet)
router.register('cinemas', views.CinemaFeedViewSet)
router.register('genres', views.GenresViewSet)

urlpatterns = [
    path('', include(router.urls))
]
