from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
        extra_kwargs = {"password": {"write_only":True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user