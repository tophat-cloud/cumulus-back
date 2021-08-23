from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MemberSerializer, ProjectSerializer
from .models import Member, Project


class MemberView(APIView):
    """
    POST /api/member
    """
    def post(self, request):
        member_serializer = MemberSerializer(data=request.data)

        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(member_serializer.error, status=status.HTTP_400_BAD_REQUEST)
 
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
 