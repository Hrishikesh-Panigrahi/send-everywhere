from . import models
from django.db.models.functions import Now
from datetime import timedelta

def removeFile():
    files = models.File.objects.all()
    for file in files:
        if file.expiration_time < Now():
            #delete this file
            file.delete()
        else:
            continue