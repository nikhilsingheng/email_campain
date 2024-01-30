from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['POST'])
def add_subscriber(request):
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    if not email or not first_name:
        return Response({'error': 'Email and first_name are required'}, status=400)
    subscriber, created = Subscriber.objects.get_or_create(email=email, defaults={'first_name': first_name})
    return Response({'success': 'Subscriber added successfully'}, status=201 if created else 200)

@api_view(['POST'])
def unsubscribe(request, email):
    subscriber = get_object_or_404(Subscriber, email=email)
    subscriber.is_active = False
    subscriber.save()
    return Response({'success': 'Unsubscribed successfully'})