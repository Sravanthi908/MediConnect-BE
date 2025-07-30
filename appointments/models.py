from django.db import models
from django.contrib.auth.models import User
from hospitals.models import Hospital

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} at {self.hospital.name} on {self.date} {self.time}"
