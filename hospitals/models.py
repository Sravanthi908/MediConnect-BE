# hospitals/models.py
from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=120)
    specialization = models.CharField(max_length=120, blank=True)

    def __str__(self): return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="hospitals/", blank=True, null=True)
    # Either store one name:
    doctor = models.CharField(max_length=120, blank=True)  # optional single doctor string
    # Or relate many doctors (optional):
    doctors = models.ManyToManyField(Doctor, blank=True)

    def __str__(self): return self.name
