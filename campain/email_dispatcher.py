from threading import Thread, Lock
from queue import Queue
from django.core.mail import send_mail
from .models import Campaign, Subscriber

class EmailDispatcher(Thread):
    def __init__(self, email_queue):
        super().__init__()
        self.queue = email_queue
        self.lock = Lock() 

    def run(self):
        print("Thread is running...")
        while True:
            campaign, recipients = self.queue.get()
            print("Campaign in run method:", campaign)
            self.send_email(campaign, recipients)
            self.queue.task_done()

    def send_email(self, campaign, recipients):
        print("Sending email...")
        print(" campaign.subject,", campaign.plain_text_content,recipients)
        try:
            send_mail(
                campaign.subject,
                campaign.plain_text_content,
                'nikhilsingheng@email.com',
                recipients,
                html_message=campaign.html_content,
            )
            print(f'Successfully sent campaign "{campaign.subject}" to {len(recipients)} recipients.')
        except Exception as e:
            print(f'Failed to send campaign "{campaign.subject}". Error: {str(e)}')


email_queue_instance = Queue()
email_dispatcher_instance = EmailDispatcher(email_queue_instance)
email_dispatcher_instance.start()
