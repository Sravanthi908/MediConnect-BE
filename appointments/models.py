from django.db import models
from django.conf import settings  # ✅ This fixes NameError

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    appointment_datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.appointment_datetime}"
