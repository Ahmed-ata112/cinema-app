from django.core.management.base import BaseCommand
from parser import Parser
from movies_api.models import *
from movies_api.tasks import demo_task
from background_task.models import Task, CompletedTask
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, **options):
        # Task.objects.all().delete()
        # daily would make it happen one time
        # demo_task("Hi after 60 min", repeat=Task.DAILY)

        MovieItem.objects.all().delete()
        CinemaItem.objects.all().delete()
        Parser().init()
