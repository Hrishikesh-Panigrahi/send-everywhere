from django.db import models
import os


class File(models.Model):
    uuid = models.UUIDField()
    file = models.FileField(upload_to='files')
    name = models.CharField(max_length=45)
    path = models.CharField(max_length=100, null=True)