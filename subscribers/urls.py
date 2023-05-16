from django.urls import path
from .views import SubscriberView, UnsubscribeView

urlpatterns = [
    path('subscriber/', SubscriberView.as_view(), name='subscriber'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
]