from django.db import models
from django.conf import settings   # ✅ correct import
from hospitals.models import Hospital

class Appointment(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    appointment_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.hospital.name} on {self.appointment_datetime}"
