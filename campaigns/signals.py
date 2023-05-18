from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from campaigns.models import EmailCampaign
from campaigns.email_dispatcher import send_emails
from campaigns.views import publish_email_campaign
import redis
import threading

@receiver(post_save, sender=EmailCampaign, dispatch_uid="email_campaign_created")
def send_email_campaigns(sender, instance, **kwargs):

    publish_email_campaign(sender, instance, **kwargs)

    red = redis.StrictRedis(host='localhost', port=49153, decode_responses=True, password="redispw")
    sub = red.pubsub()
    sub.subscribe('email_campaign')
    print("subscribed to email_campaign channel, listening for messages")
    for i in sub.listen():
        print(i)
    for message in sub.listen():
        campaign_id = message.get('data')
        print(f"message received on email_campaign channel, message={campaign_id}")
        if campaign_id == str(instance.id):
            campaign = EmailCampaign.objects.get(id=campaign_id)
            send_emails(campaign)
