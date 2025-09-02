# hospitals/views.py
from rest_framework.viewsets import ModelViewSet
from .models import Hospital, Doctor
from .serializers import HospitalSerializer, DoctorSerializer

class HospitalViewSet(ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
