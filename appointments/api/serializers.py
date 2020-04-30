from rest_framework import serializers
from appointments.models import Appointment
from clients.models import Client
from staff.models import Staff
from services.models import Service

from clients.api.serializers import ClientSerializer
from services.api.serializers import ServiceSerializer
from staff.api.serializers import StaffSerializer



class AppointmentClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class AppointmentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')


class AppointmentStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('__all__')

class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('__all__')


class AppointmentListSerializer(serializers.ModelSerializer):
    client = AppointmentClientSerializer(many=False, read_only=True)
    service = AppointmentServiceSerializer()
    staff = AppointmentStaffSerializer()

    class Meta:
        model = Appointment
        fields = ['service','date','staff','client','duration','uuid','notes']
