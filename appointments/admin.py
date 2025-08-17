from django.contrib import admin
from .models import Appointment   # ✅ must match class name exactly

admin.site.register(Appointment)
