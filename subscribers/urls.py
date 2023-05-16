from django.urls import path
from subscribers.views import SubscribeView, Unsubscribe

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/', Unsubscribe.as_view(), name='unsubscribe'),
]