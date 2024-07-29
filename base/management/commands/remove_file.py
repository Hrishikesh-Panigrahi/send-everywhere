# app_name/management/commands/remove_expired_stories.py

from django.core.management.base import BaseCommand
from django.db.models.functions import Now

from base.models import File

class Command(BaseCommand):
    help = 'clear expired messages'

    def handle(self, *args, **options):
        File._base_manager.filter(expiration_time__gte=Now()).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted expired files'))