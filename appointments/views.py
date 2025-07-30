from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Appointment
from hospitals.models import Hospital
import json

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.get(id=data['user_id'])
        hospital = Hospital.objects.get(id=data['hospital_id'])
        appointment = Appointment.objects.create(
            user=user,
            hospital=hospital,
            date=data['date'],
            time=data['time']
        )
        return JsonResponse({'message': 'Appointment booked'})
    return JsonResponse({'error': 'Invalid method'}, status=405)
