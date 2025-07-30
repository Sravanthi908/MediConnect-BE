from django.urls import path
from .views import RegisterView, LoginView, SetLocationView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('set-location/', SetLocationView.as_view()),
]