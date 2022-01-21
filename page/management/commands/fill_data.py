from django.core.management.base import BaseCommand, CommandError
from page.models import AdvStatus


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        for i in range(10000):
            AdvStatus(name='active' + str(i)).save()
