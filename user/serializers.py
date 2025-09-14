from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User  # Import your custom User model

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all())]  # Use custom User model
    )
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]  # Use custom User model
    )
    name = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # Split name into first and last name
        full_name = validated_data.pop('name', '')
        first_name, last_name = full_name.split(' ', 1) if ' ' in full_name else (full_name, '')
        
        # Create user with split names
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=first_name,
            last_name=last_name
        )
        return user

    def to_representation(self, instance):
        # Customize the response data
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'first_name': instance.first_name,
            'last_name': instance.last_name
        }