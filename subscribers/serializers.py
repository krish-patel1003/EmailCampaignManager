from rest_framework import serializers
from subscribers.models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"
        extra_kwargs = {"active": {"read_only": True}}