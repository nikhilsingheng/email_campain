from django.urls import path
from campain.views import add_subscriber, unsubscribe

urlpatterns = [
    path('add-subscriber/', add_subscriber, name='add_subscriber'),
    path('unsubscribe/<str:email>/', unsubscribe, name='unsubscribe'),

]