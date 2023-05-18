from subscribers.models import Subscriber
from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):
    help = "To add mock subscribers"

    def create_subscribers(self, email, first_name):
        subscriber = Subscriber.objects.create(
            email=email,
            first_name=first_name
        )
        subscriber.save()
        print(f"subscriber created, {subscriber.email}")
        


    def handle(self, *args, **kwargs):
        with open("subscribers/management/commands/mock_subscribers.json", "r") as f:
            data = json.load(f)
            subscriber = {}
            print(data)
            for sub in data:
                self.create_subscribers(sub["email"], sub["first_name"])
            