from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.http import JsonResponse

from .serializers import MemberSerializer, ProjectSerializer, ThunderSerializer
from .models import Member, Project, Thunder


class MemberView(APIView):
    """
    POST /api/member
    """
    @swagger_auto_schema(request_body=MemberSerializer)
    def post(self, request):
        member_serializer = MemberSerializer(data=request.data)

        user_email = request.data.get('email')

        if member_serializer.is_valid():
            if not Member.objects.filter(email=user_email).exists():
            member_serializer.save()
                return JsonResponse(member_serializer.data, status=status.HTTP_201_CREATED)
        else:
                return JsonResponse({"message":"email already exists", "status": f"{status.HTTP_400_BAD_REQUEST}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
 
    """
    GET /api/member
    GET /api/member/{member_id}
    """
    def get(self, request, **kwargs):
        if kwargs.get('member_id') is None:
            member_queryset = Member.objects.all()
            member_queryset_serializer = MemberSerializer(member_queryset, many=True)
            return Response(member_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            member_id = kwargs.get('member_id')
            member_serializer = MemberSerializer(Member.objects.get(id=member_id))
            return Response(member_serializer.data, status=status.HTTP_200_OK)
 
    """
    PUT /api/member/{member_id}
    """
    @swagger_auto_schema(request_body=MemberSerializer)
    def put(self, request, **kwargs):
        if kwargs.get('member_id') is None:
            return Response("member not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            member_id = kwargs.get('member_id')
            member_object = Member.objects.get(id=member_id)

            updated_member_serializer = MemberSerializer(member_object, data=request.data)
            if updated_member_serializer.is_valid():
                updated_member_serializer.save()
                return Response(updated_member_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(updated_member_serializer.error, status=status.HTTP_400_BAD_REQUEST)
            
    """
    DELETE /api/member/{member_id}
    """
    @swagger_auto_schema(request_body=MemberSerializer)
    def delete(self, request, **kwargs):
        if kwargs.get('member_id') is None:
            return Response("member not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            member_id = kwargs.get('member_id')
            member_object = Member.objects.get(id=member_id)
            member_object.delete()
            return Response("member deleted", status=status.HTTP_200_OK)


class ProjectView(APIView):
    """
    POST /api/project
    """
    def post(self, request):
        new_project_data = {
            'domain': request.data['domain'],
            'title': request.data['title'],
            'member': request.data['member']
        }
        project_serializer = ProjectSerializer(data=new_project_data)

        if project_serializer.is_valid():
            project_serializer.save()
            return Response(project_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(project_serializer.error, status=status.HTTP_400_BAD_REQUEST)
 
    """
    GET /api/project
    GET /api/project/{project_id}
    """
    def get(self, request, **kwargs):
        if kwargs.get('project_id') is None:
            return Response("project not found", status=status.HTTP_404_NOT_FOUND)
        else:
            project_id = kwargs.get('project_id')
            project_serializer = ProjectSerializer(Project.objects.get(id=project_id))
            return Response(project_serializer.data, status=status.HTTP_200_OK)
 
    """
    PUT /api/project/{project_id}
    """
    def put(self, request, **kwargs):
        if kwargs.get('project_id') is None:
            return Response("project not found", status=status.HTTP_404_NOT_FOUND)
        else:
            project_id = kwargs.get('project_id')
            member_object = Member.objects.get(id=project_id)

            updated_member_serializer = ProjectSerializer(member_object, data=request.data)
            if updated_member_serializer.is_valid():
                updated_member_serializer.save()
                return Response(updated_member_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(updated_member_serializer.error, status=status.HTTP_400_BAD_REQUEST)


    """
    DELETE /api/project/{project_id}
    """
    def delete(self, request, **kwargs):
        if kwargs.get('project_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            project_id = kwargs.get('project_id')
            project = Project.objects.get(id=project_id)
            project.delete()
            return Response("project deleted", status=status.HTTP_200_OK)


class ThunderView(APIView):
    """
    POST /api/thunder
    """
    def post(self, request):
        try:
            project_id = request.data['project_id']
        except AttributeError:
            return Response("project not found", status=status.HTTP_404_NOT_FOUND)

        if Thunder.objects.filter(project_id=project_id).exists():
            try:
                id = request.data['thunder_id']
            except:
                thunder_object = Thunder.objects.filter(project_id=project_id)
                thunder_serializer = ThunderSerializer(thunder_object, many=True)
                return Response(thunder_serializer.data, status=status.HTTP_200_OK)

            if Thunder.objects.filter(project_id=project_id, id=id).exists():
                thunder_object = Thunder.objects.get(project_id=project_id, id=id)
                thunder_serializer = ThunderSerializer(thunder_object)
                return Response(thunder_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("thunder not found", status=status.HTTP_404_NOT_FOUND)


    """
    DELETE /api/thunder/{thunder_id}
    """
    def delete(self, request):
        try:
            project_id = request.data['project_id']
        except AttributeError:
            return Response("project not found", status=status.HTTP_404_NOT_FOUND)

        if Thunder.objects.filter(project_id=project_id).exists():
            try:
                thunder_id = request.data['thunder_id']
            except AttributeError:
                return Response("thunder not found", status=status.HTTP_404_NOT_FOUND)

            if Thunder.objects.filter(project_id=project_id, thunder_id=thunder_id).exists():
                thunder_object = Thunder.objects.get(project_id=project_id, thunder_id=thunder_id)
                thunder_object.delete()
                return Response("delete success", status=status.HTTP_200_OK)
            else:
                return Response("thunder not found", status=status.HTTP_404_NOT_FOUND)


class CreateThunderView(APIView):
    """
    POST /api/thunder
    """
    def post(self, request):
        thunder_serializer = ThunderSerializer(data=request.data)

        if thunder_serializer.is_valid():
            thunder_serializer.save()
            return Response(thunder_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(thunder_serializer.error, status=status.HTTP_400_BAD_REQUEST)
 