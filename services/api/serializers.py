from rest_framework import serializers
from services.models import Service, Office

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('__all__')
