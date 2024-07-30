import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendEverywhere.settings')

BROKER_URL = "amqp://localhost:5672"

# used redis broker if it exists
app = Celery('sendEverywhere',broker="amqp://localhost:5672", backend="amqp://localhost:5672", namespace='CELERY')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)

app.conf.broker_url = BROKER_URL
CELERY_BROKER_URL = BROKER_URL

app.conf.beat_schedule = {

    'removeFile': {
        'task': 'base.task.removeFile',
        'schedule': 600.0,
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')