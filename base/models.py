from django.db import models
from django.db.models.functions import Now
from datetime import timedelta
from django.utils import timezone


class FileManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            expiration_time__gt=Now()
        )


class File(models.Model):
    uuid = models.UUIDField()
    file = models.FileField(upload_to='files')
    name = models.CharField(max_length=250)
    path = models.CharField(max_length=100, null=True)
    request_code = models.CharField(max_length=6, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField(
        db_index=True, default=Now()+timedelta(minutes=10), editable=False)

    def is_expired(self):
        return timezone.now() - self.created_at > timedelta(minutes=10)

    # objects = FileManager()

    def __str__(self):
        return self.name
