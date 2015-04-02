from django.core.management.base import BaseCommand
from feedback.models import Feedback

class Command(BaseCommand):
    help = 'gets all feedback'

    def handle(self, *args, **options):
        all_entries = Feedback.objects.all()
        for index,entry in enumerate(all_entries):
            self.stdout.write('%s "%s" %s' % (index, entry.text, entry.posted_by))
