from django.urls import path, include
from rest_framework.routers import DefaultRouter
from movies_api import views


router = DefaultRouter()
router.register('', views.MovieFeedViewSet)


urlpatterns = [
    path('', include(router.urls))
]
