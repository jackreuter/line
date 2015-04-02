from django.core.management.base import BaseCommand
from search.models import Query

class Command(BaseCommand):
    help = 'gets all search queries'

    def handle(self, *args, **options):
        all_entries = Query.objects.all()
        for index,entry in enumerate(all_entries):
            self.stdout.write('%s "%s" %s' % (index, entry.text, entry.searched_by))
