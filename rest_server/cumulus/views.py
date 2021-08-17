from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import MemberSerializer, ProjectSerializer
from .models import Member, Project


class MemberView(APIView):
    """
    POST /user
    """
    def post(self, request):
        member_serializer = MemberSerializer(data=request.data)

        if member_serializer.is_valid():
            member_serializer.save()
            return Response(member_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(member_serializer.error, status=status.HTTP_400_BAD_REQUEST)
 
    """
    GET /user
    GET /user/{user_id}
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
    PUT /user/{user_id}
    """
    def put(self, request):
        return Response("test ok", status=200)
 
    """
    DELETE /user/{user_id}
    """
    def delete(self, request):
        return Response("test ok", status=200)


class ProjectView(APIView):
    """
    POST /user
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
    GET /user
    GET /user/{user_id}
    """
    def get(self, request, **kwargs):
        if kwargs.get('project_id') is None:
            return Response("no such project", status=status.HTTP_404_NOT_FOUND)
        else:
            project_id = kwargs.get('project_id')
            project_serializer = ProjectSerializer(Project.objects.get(id=project_id))
            return Response(project_serializer.data, status=status.HTTP_200_OK)
 
    """
    PUT /user/{user_id}
    """
    def put(self, request):
        return Response("test ok", status=200)
 
    """
    DELETE /user/{user_id}
    """
    def delete(self, request, **kwargs):
        if kwargs.get('project_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            project_id = kwargs.get('project_id')
            project = Project.objects.get(id=project_id)
            project.delete()
            return Response("deleted", status=status.HTTP_200_OK)
 