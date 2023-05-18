from django.core import mail
from django.template.loader import render_to_string
from smtplib import SMTPException  



def render_email_template(campaign, subscriber):
    
    email_content = {
        'html_message': render_to_string('campaigns/email_campaign_template.html', {'campaign': campaign, 'subscriber': subscriber}),
        'plain_message': campaign.plain_text_content,
    }

    return email_content


def send_email(campaign, subscriber, email_content):

    try:
        mail.send_mail(
            subject=campaign.subject,
            message=email_content["plain_message"],
            from_email="gujjubkc01@gmail.com",
            recipient_list=[subscriber.email],
            html_message=email_content["html_message"],
            fail_silently=False,
        )
        return 
    except SMTPException as e:          
        print('There was an SMTP error sending an email.'+ str(e))

    except Exception as e:
        print('There was an error sending an email.'+ str(e))