from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from campaigns.serializers import EmailCampaignSerializer
from campaigns.email_dispatcher import send_emails
# Create your views here.

class EmailCampaignView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = EmailCampaignSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            send_emails(campaign=serializer.data)
            return Response(
                {"data": serializer.data, "message": "Campaign Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
