from django.http import JsonResponse
from math import radians, sin, cos, sqrt, atan2
from .models import Hospital, Appointment
from user.models import UserLocation
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes


def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_nearby_hospitals(request):
    try:
        user_location = UserLocation.objects.get(user=request.user)
        nearby = []
        for hospital in Hospital.objects.all():
            distance = haversine(user_location.latitude, user_location.longitude, hospital.latitude, hospital.longitude)
            if distance <= 50:
                nearby.append({
                    'id': hospital.id,
                    'name': hospital.name,
                    'address': hospital.address,
                    'latitude': hospital.latitude,
                    'longitude': hospital.longitude,
                    'distance_km': round(distance, 2)
                })
        return Response({'hospitals': nearby})
    except Exception as e:
        return Response({'error': str(e)}, status=400)

@api_view(['GET'])
def hospital_detail(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return Response({
        'id': hospital.id,
        'name': hospital.name,
        'address': hospital.address,
        'latitude': hospital.latitude,
        'longitude': hospital.longitude,
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    try:
        hospital_id = request.data.get('hospital_id')
        date = request.data.get('date')
        time = request.data.get('time')
        hospital = get_object_or_404(Hospital, id=hospital_id)
        Appointment.objects.create(user=request.user, hospital=hospital, date=date, time=time)
        return Response({'message': 'Appointment booked'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)