from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, DoctorViewSet

router = DefaultRouter()
router.register(r'hospitals', HospitalViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
