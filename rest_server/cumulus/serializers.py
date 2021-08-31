from .models import Member, Project, Thunder
from rest_framework import serializers, viewsets
from django.contrib.auth.hashers import make_password

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(MemberSerializer, self).create(validated_data)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['member'] =  MemberSerializer(read_only=True)
        return super(ProjectSerializer, self).to_representation(instance)


class ThunderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thunder
        fields = '__all__'
