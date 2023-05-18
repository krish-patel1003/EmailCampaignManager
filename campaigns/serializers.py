from rest_framework import serializers
from campaigns.models import EmailCampaign

class EmailCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCampaign
        fields = (
            "id", 
            "subject",
            "preview_text",
            "article_url",
            "html_content", 
            "plain_text_content", 
            "published_date"
        )