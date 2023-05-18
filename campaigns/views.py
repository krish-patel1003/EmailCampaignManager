from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from campaigns.serializers import EmailCampaignSerializer
import redis
# Create your views here.

class EmailCampaignView(APIView):

    red = redis.StrictRedis(host='localhost', port=49153, decode_responses=True, password="redispw")

    def post(self, request, *args, **kwargs):
        serializer = EmailCampaignSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"data": serializer.data, "message": "Campaign Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def publish_email_campaign(sender, instance, **kwargs):
    red = redis.StrictRedis(host='localhost', port=49153, decode_responses=True, password="redispw")
    red.publish('email_campaign', str(instance.id))
    print(f"message published on email_campaign channel, message={str(instance.id)}")