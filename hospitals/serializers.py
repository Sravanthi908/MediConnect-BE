from rest_framework import serializers
from .models import Hospital, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = '__all__'
