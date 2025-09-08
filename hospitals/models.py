from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    img = models.URLField(max_length=500, blank=True, null=True)
    availableDoctors = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.specialty})"
