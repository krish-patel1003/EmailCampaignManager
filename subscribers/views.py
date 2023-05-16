from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializer
# Create your views here.

class SubscriberView(ListCreateAPIView):

    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def post(self, request, *args, **kwargs):
        serizlier = SubscriberSerializer(data=request.data)

        try:
            Subscriber.objects.get(email=request.data["email"])
            return Response(
                {"message": "This Email is already subscribed"}, status=status.HTTP_400_BAD_REQUEST)
        except Subscriber.DoesNotExist:
            pass

        if serizlier.is_valid():
            serizlier.save()
            return Response(
                {"data": serizlier.data, "message": "Subscribed Successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": serizlier.errors},status=status.HTTP_400_BAD_REQUEST)



class UnsubscribeView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            subscriber = Subscriber.objects.get(email=request.data["email"])
            subscriber.active = False
            subscriber.save()
            return Response({"message": "Unsubscribed Successfully"}, status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response({"message": "This Email is not subscribed"}, status=status.HTTP_400_BAD_REQUEST)