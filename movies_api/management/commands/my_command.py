from django.core.management.base import BaseCommand
from parser import Parser
from movies_api.models import *
from movies_api.tasks import demo_task
from background_task.models import Task, CompletedTask


class Command(BaseCommand):
    def handle(self, **options):
        Task.objects.all().delete()
        demo_task("Hi after 60 min", repeat=5)
        # MovieItem.objects.all().delete()
        # CinemaItem.objects.all().delete()
        # Parser("https://elcinema.com/en/theater/1").parse_cinames()
