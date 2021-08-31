from django.forms import models
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from cumulus import models, serializers

# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = '__all__'
        extra_kwards = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(MemberSerializer, self).create(validated_data)


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
 
    def validate(self, data):
        user = authenticate(**data)
        if models.Member.objects.get(email=user):
            return user
        raise serializers.ValidationError("Incorrect Credentials")