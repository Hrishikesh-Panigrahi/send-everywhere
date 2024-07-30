from . import models
from celery import shared_task
from django.utils import timezone
import datetime


@shared_task
def removeFile():
    expired_instances = models.File.objects.filter(
        created_at__lte=timezone.now() - datetime.timedelta(minutes=10))
    expired_instances.delete()
