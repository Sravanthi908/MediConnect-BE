from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="doctors")
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.specialization}"
