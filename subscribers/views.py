from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from subscribers.models import Subscriber
from subscribers.serializers import SubscriberSerializer
# Create your views here.

class SubscribeView(ListCreateAPIView):

    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data=request.data)

        try:
            Subscriber.objects.get(email=request.data['email'])
            return Response(
                {"message": "You have already subscribed to our Email Campaign."}, status=status.HTTP_400_BAD_REQUEST)
        except Subscriber.DoesNotExist:
            pass

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "You have successfully subscribed to our Email Campaign."}, status=status.HTTP_201_CREATED)
        
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class Unsubscribe(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            subscriber = Subscriber.objects.get(email=request.data['email'])
            subscriber.active = False
            subscriber.save()
            return Response(
                {"message": "You have successfully unsubscribed from our Email Campaign."}, status=status.HTTP_200_OK)
        except Subscriber.DoesNotExist:
            return Response(
                {"message": "You are not subscribed to our Email Campaign."}, status=status.HTTP_400_BAD_REQUEST)

