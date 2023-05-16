from django.urls import path
from campaigns.views import EmailCampaignView

urlpatterns = [
    path('campaign/', EmailCampaignView.as_view(), name='campaign'),
]