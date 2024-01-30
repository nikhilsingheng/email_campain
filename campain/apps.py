# campain/apps.py
from django.apps import AppConfig
from threading import Thread
from queue import Queue

class CampainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'campain'

    def ready(self):
        from .email_dispatcher import EmailDispatcher
        from django.apps import apps

        email_queue = Queue()
        email_dispatcher = EmailDispatcher(email_queue)
        print("email_dispatcher",email_dispatcher)
        for _ in range(5):
            dispatcher = EmailDispatcher(email_queue)
            dispatcher.daemon = True
            dispatcher.start()
