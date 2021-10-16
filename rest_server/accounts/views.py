from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from django.contrib.auth import get_user_model

from .serializers import UserRegistrationSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': "true",
            'status code': status_code,
            'message': "user registered successfully",
        }
        return Response(response, status=status_code)