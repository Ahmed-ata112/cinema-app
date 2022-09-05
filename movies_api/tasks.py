from background_task import background
from logging import getLogger
from background_task.models import CompletedTask

logger = getLogger(__name__)


@background(schedule=15)
def demo_task(message):
    print(message)
    with open('out.txt', 'w') as f:
        f.write(message)

    if CompletedTask.objects.count() > 3:
        CompletedTask.objects.all().delete()

    logger.debug('demo_task. message={0}'.format(message))
