from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import Project, Thunder
from rest_framework import serializers, viewsets


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
    
    def to_representation(self, instance):
        # self.fields['member'] =  MemberSerializer(read_only=True)
        return super(ProjectSerializer, self).to_representation(instance)


class ThunderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thunder
        fields = '__all__'
