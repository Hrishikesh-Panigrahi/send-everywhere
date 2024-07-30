import time
from . import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import random
import math


def generateCode():
    digits = [i for i in range(0, 10)]
    random_str = ""

    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


@receiver(post_save, sender=models.File)
def createRequestCode(sender, instance, created, **kwargs):
    if created:
        instance.request_code = generateCode()
        instance.save()
        print("Request code created")
