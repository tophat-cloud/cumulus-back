"""rest_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from . import views

app_name = 'cumulus'
urlpatterns = [
    path('member', views.MemberView.as_view(), name='member'),
    path('member/<int:member_id>', views.MemberView.as_view(), name='member_detail'),
    path('project', views.ProjectView.as_view(), name='project'),
    path('project/<str:project_id>', views.ProjectView.as_view(), name='project_detail'),
    path('project/enroll', views.ProjectView.as_view(), name='domain_enroll'),
    path('thunder', views.ThunderView.as_view(), name='thunder'),
    path('thunder/create', views.CreateThunderView.as_view(), name='thunder_create')
]
