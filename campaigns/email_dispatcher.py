from subscribers.models import Subscriber
import threading
from campaigns.utils import render_email_template, send_email


def process_email(campaign, subscriber):

    email_content = render_email_template(campaign, subscriber)
    
    retries = 3  # Number of retries
    while retries > 0:
        try:
            print(f"trying to send email, {campaign.subject} to {subscriber.email}")
            send_email(campaign, subscriber, email_content)
            print(f"email sent, {campaign.subject} to {subscriber.email}")
            return  # Email sent successfully, exit the loop
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
            retries -= 1

    print(f"Max retries exceeded for email: {campaign.subject} to {subscriber.email}")


def send_emails(campaign):

    subscribers = Subscriber.objects.filter(active=True)
    threads = []

    # Create threads for processing emails
    for subscriber in subscribers:
        print(f"processing email thread, {campaign.subject} to {subscriber.email}")
        thread = threading.Thread(
            target=process_email, 
            args=(campaign, subscriber)
        )
        thread.start()
        threads.append(thread)
        print(f"email thread started, {campaign.subject} to {subscriber.email}")

    # Wait for all the threads to complete
    for thread in threads:
        thread.join()