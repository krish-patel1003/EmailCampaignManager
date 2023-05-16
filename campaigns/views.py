from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from campaigns.models import EmailCampaign
from campaigns.serializers import EmailCampaignSerializer
from campaigns.utils import send_email
# Create your views here.


class EmailCampaignView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EmailCampaignSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            render(request, "campaigns/email_campaign_template.html", {"campaign": serializer.data})
            send_email(data=serializer.data)
            return Response(
                {"data": serializer.data, "message": "Campaign Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    