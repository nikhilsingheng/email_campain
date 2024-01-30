from django.core.management.base import BaseCommand
from queue import Queue  # Import Queue
from campain.email_dispatcher import EmailDispatcher
from campain.models import Campaign, Subscriber

class Command(BaseCommand):
    help = 'Send emails for a specific campaign'

    def add_arguments(self, parser):
        parser.add_argument('--campaign_id', type=int, help='ID of the campaign to send')

    def handle(self, *args, **options):
        campaign_id = options['campaign_id']
        campaign = Campaign.objects.get(pk=campaign_id)
        email_queue_instance = Queue()
        email_dispatcher = EmailDispatcher(email_queue_instance)
        email_dispatcher.start()
        recipients = list(Subscriber.objects.filter(is_active=True).values_list('email', flat=True))
        email_dispatcher.queue.put((campaign, recipients))
