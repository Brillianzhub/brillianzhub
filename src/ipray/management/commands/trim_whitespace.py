from django.db import models
from django.core.management.base import BaseCommand
from ipray.models import VerseKJV


class Command(BaseCommand):
    help = 'Trims trailing whitespace from text in MyModel'

    def handle(self, *args, **kwargs):
        instances = VerseKJV.objects.all()
        for instance in instances:
            instance.text = instance.text.rstrip()

        VerseKJV.objects.bulk_update(instances, ['text'])
        self.stdout.write(self.style.SUCCESS(
            'Successfully trimmed whitespace from all instances'))
