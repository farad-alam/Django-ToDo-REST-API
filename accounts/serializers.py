from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    username = serializers.CharField(read_only=True)
    
    class Meta:
        model = CustomUser
        # Exclude the username from the fields since it's auto-generated
        fields = ['first_name', 'last_name', 'email', 'username', 'phone_number', 'password']
    
    def create(self, validated_data):
        # Let the manager handle the username generation and user creation
        return CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', '')
        )

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'phone_number', 'date_joined']
