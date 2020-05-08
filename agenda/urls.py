"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from .views import *
from services.api.views import OfficeListCreateView, OfficeRetrieveUpdateDestroyAPIView

schema_view = get_schema_view(title='MaxiAgenda API',
                description='An API to manage your business appointments.')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('clients/', include('clients.api.urls')),
    path('services/', include('services.api.urls')),
    path('appointments/', include('appointments.api.urls')),
    path('staff/', include('staff.api.urls')),
    path('saloons/', include('saloons.api.urls')),
    path('owners/', include('owners.api.urls')),
    path('schema/', schema_view),
    path('offices/', OfficeListCreateView.as_view()),
    path('offices/<int:pk>', OfficeRetrieveUpdateDestroyAPIView.as_view()),

    path('hello-world', HelloWorld.as_view())
]
