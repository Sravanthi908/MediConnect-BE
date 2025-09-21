from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(write_only=True)
    
    role = serializers.ChoiceField(choices=[("patient", "Patient"), ("doctor", "Doctor")])

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "confirm_password", "full_name", "role"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        full_name = validated_data.pop("full_name")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email", ""),
            password=validated_data["password"],
            role=validated_data.get("role", "patient"),
        )
        # ✅ save full_name
        user.full_name = full_name
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        data["user"] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # ✅ include full_name so frontend gets it
        fields = ["id", "username", "email", "full_name", "role"]
