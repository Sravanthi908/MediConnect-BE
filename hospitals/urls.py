from django.urls import path
from .views import get_nearby_hospitals, hospital_detail, book_appointment

urlpatterns = [
    path('nearby/', get_nearby_hospitals),
    path('detail/<int:hospital_id>/', hospital_detail),
    path('book/', book_appointment),
]