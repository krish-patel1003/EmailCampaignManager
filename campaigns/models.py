from django.db import models

# Create your models here.

class EmailCampaign(models.Model):
    subject = models.CharField(max_length=100)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject   