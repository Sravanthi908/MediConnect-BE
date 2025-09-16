from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

User = get_user_model()  # Always fetch the active user model


# Register user
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return User.objects.all()


# Login user (returns JWT tokens)
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


# View user profile (protected)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
