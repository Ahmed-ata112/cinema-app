from django.core.management.base import BaseCommand
from parser import Parser
from movies_api.models import *


class Command(BaseCommand):
    def handle(self, **options):
        MovieItem.objects.all().delete()
        CinemaItem.objects.all().delete()
        Parser("https://elcinema.com/en/theater/1").parse_cinames()
