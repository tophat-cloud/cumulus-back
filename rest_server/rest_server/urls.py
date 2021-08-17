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
from django.conf.urls import url, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# import cumulus.api

# app_name = 'cumulus'

# router = routers.DefaultRouter()
# router.register('members', cumulus.api.MemberViewSet)

# schema_urlpatterns = [
#     path('api/', include('cumulus.api')),
# ]
# schema_view = get_schema_view(
#     openapi.Info(
#         title="Cumulus API",
#         default_version='v1',
#         terms_of_service="https://www.google.com/policies/terms/",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
#     patterns=schema_urlpatterns,
# )


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'cumulus/', include('cumulus.urls')),
]
