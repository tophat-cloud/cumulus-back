from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.hashers import check_password

from cumulus.models import Member


# Create your views here.
class LoginView(APIView):
    def get(self, request):
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        member_object = Member.objects.get(email=email)
        if member_object:
            if check_password(password, member_object.password):
                request.session['user'] = member_object.id
                return redirect('/api/project')
        else:
            return Response("member not found", status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def get(self, request):
        return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, **kwargs):
        request.session.pop('user')
        return redirect('/api/project')