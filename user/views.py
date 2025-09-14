from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User  # Import your custom User model

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.none()  # Required for CreateAPIView with custom model

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            serializer.to_representation(user),
            status=status.HTTP_201_CREATED
        )