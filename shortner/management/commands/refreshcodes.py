from django.core.management.base import BaseCommand, CommandError
from shortner.models import KirrUrl

class Command (BaseCommand):
    help = 'refreshes all Kirrurl shot codes'
    def add_arguments( self, parser):
        parser.add_argument('--items' , type=int)

    def handle(self, *args, ** options):

        return KirrUrl.objects.refresh_shotcode(items=options['items'])
