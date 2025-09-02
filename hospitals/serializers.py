# hospitals/serializers.py
from rest_framework import serializers
from .models import Hospital, Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ("id", "name", "specialization")

class HospitalSerializer(serializers.ModelSerializer):
    # Always give React both a single `doctor` string and an optional `doctors` list
    doctors = DoctorSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True, allow_null=True, required=False)
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = Hospital
        fields = ("id", "name", "description", "image", "doctor", "doctors")

    def get_doctor(self, obj):
        # if you filled the `doctor` CharField, use that
        if getattr(obj, "doctor", None):
            return obj.doctor
        # else, fall back to the first related doctor’s name (if any)
        first = obj.doctors.first() if hasattr(obj, "doctors") else None
        return first.name if first else None
